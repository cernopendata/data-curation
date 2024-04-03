#!/usr/bin/env python3
import datetime

mc_dataset_input = 'pp_mc_physlite_240228.txt' #'pp_mc_full.txt' #'pp_mc_test.txt'
scope_did = 'user.zmarshal'
static_did_pre = scope_did+'.'
static_did_post = '_OpenData_v0_'+datetime.date.today().isoformat()

really_use_rucio = True

dataset_list_file = open(mc_dataset_input,'r')
datasets = {}
for bline in dataset_list_file:
    aline = bline.split('#')[0].strip()
    if len(aline.split())<2:
        continue
    datasets[ aline.split()[0].strip() ] = int( aline.split()[1].strip() )
dataset_list_file.close()
print(f'Read in {len(datasets.keys())} datasets')

from rucio.client.ruleclient import RuleClient
from rucio.client.didclient import DIDClient

dc = DIDClient()
rc = RuleClient()
user_did_list = []
file_dictionary = {}
user_did_dict = {}

# Loop over all the datasets
for dataset in datasets:
    did_sum = 0
    did_file_list = []
    my_scope=dataset.split('.')[0]
    fl = dc.list_files(scope=my_scope,name=dataset)
    # Minimal number of files required to reach the desired target
    sorted_fl = sorted(fl , key=lambda x: x['events'], reverse=True)
    # Note that we're stashing the full file list so we can check if we got all the files later
    for a in sorted_fl:
        did_sum += a['events']
        # Keep a list of datasets in the format we'll want them in for rucio
        did_file_list += [ {'scope':my_scope,'name':a['name']} ]
        if did_sum >= datasets[dataset]:
            # Got enough files
            break
    # Check that we reached the right number
    if did_sum < datasets[dataset]:
        print(f'Warning: dataset {dataset} appears to have {did_sum} < {datasets[dataset]} events - will move the whole thing')
    # Should we just take the entire dataset?
    if did_sum < datasets[dataset] or len(sorted_fl)==len(did_file_list):
        user_did_list += [ { 'scope':my_scope, 'name':dataset } ]
        file_dictionary[ dataset ] = [ x['name'] for x in did_file_list ]
        print(f'Taking {dataset} in its entirety for {did_sum} events (wanted {datasets[dataset]})')
    else:
        # Grab the DSID of the input MC dataset
        did_number = dataset.split('.')[1]
        # Create a new dataset name based on that DSID and our pre- and post-fixes
        new_ds_name = f'{static_did_pre}{did_number}{static_did_post}'
        # Create the new dataset with that name
        if really_use_rucio:
            dc.add_dataset(scope=scope_did,name=new_ds_name)
        # Attach our files to that dataset
        if really_use_rucio:
            dc.add_files_to_datasets( [ { 'scope':scope_did , 'name':new_ds_name , 'dids':did_file_list } ] )
        # Update bookkeeping
        file_dictionary[ dataset ] = [ x['name'] for x in did_file_list ]
        user_did_dict[ dataset ] = new_ds_name
        # Add the dataset to our list
        user_did_list += [ { 'scope':scope_did, 'name':new_ds_name } ]
        print(f'From {dataset} created {new_ds_name} containing {len(did_file_list)} files with {did_sum} events (requested {datasets[dataset]})')

## Create a rule for our new dataset
if really_use_rucio:
    rid = rc.add_replication_rule(dids=user_did_list, # The list of datasets we want to transfer
                                  copies=1, # Just one copy please
                                  rse_expression='CERN-PROD_OPENDATA', # Destination RSE
                                  lifetime=10368000, # Set a several month lifetime so these aren't there forever
                                  account='zmarshal', # My account for the time being
                                  activity='Data Consolidation', # Recommended by Mario
                                  notify='N', # No need for notifications
                                  comment='Transfer for Open Data') # Comment to make these visible in the system
    # Or activity="User Subscriptions"
else:
    # Fake transfer IDs in case they help later
    rid = ['0b527f5c31444f5a892af8b736875887', 'b8b526f691fb4f6f9f368bf3309c79b0', 'a57914d5bd8846878a378ef856f3dbd6']
print(f'Created rules {rid} for {len(user_did_list)} datasets to be transferred')

# Record the rules that we just made
rule_list = open( 'rule_list'+static_did_post+'.txt' , 'w' )
rule_list.write( '\n'.join(rid) )
rule_list.close()

# Record the file mapping that we established
import json
file_backup = open( 'file_mapping'+static_did_post+'.json' , 'w' )
json.dump( obj={'file_dictionary':file_dictionary,'user_did_dictionary':user_did_dict} , fp=file_backup )
file_backup.close()

