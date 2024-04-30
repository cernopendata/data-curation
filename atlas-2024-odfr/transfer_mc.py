#!/usr/bin/env python3
import datetime
import json

# The file containing the datasets to be processed
mc_dataset_input = 'pp_mc_physlite_p6026_v3.txt'
# Previous version: 'pp_mc_physlite_p6026.txt'

# Scope for the rucio datasets I'll be creating
scope_did = 'user.zmarshal'

# Prefix for the rucio datasets I'll be creating
static_did_pre = scope_did+'.'

# Postfix for the rucio datasets I'll be creating
static_did_post = '_OpenData_v0_p6026_'+datetime.date.today().isoformat()

# Previous request json files to ensure we don't bother processing duplicate datasets
previous_requests = ['mc_file_mapping_OpenData_v0_p6026_2024-04-16_with_metadata.json',
                     'mc_file_mapping_OpenData_v1_p6026_2024-04-23_with_metadata.json']
already_processed_datasets = []
for old_request_json in previous_requests:
    with open(old_request_json,'r') as old_request_file:
        old_request_data = json.load(old_request_file)
        already_processed_datasets += old_request_data['file_dictionary'].keys()

# Flag to disable the use of rucio - so that we can test and make json files without making rules
really_use_rucio = True
if really_use_rucio:
    print('Really using rucio for data transfers')
else:
    print('Not really using rucio - test run')

# The input dataset list that I'm going to use
datasets = {}
with open(mc_dataset_input,'r') as dataset_list_file:
    for bline in dataset_list_file:
        # Allow for commented lines in the input file in case folks are excluding datasets
        aline = bline.split('#')[0].strip()
        if len(aline.split())<2:
            continue
        # Make sure that we don't process things we've already dealt with
        if aline.split()[0].strip() in already_processed_datasets:
            print(f'Already processed dataset; ignoring {aline.split()[0].strip()}')
            continue
        # Current lines have dataset name, number of files, size, units of size, and number of events
        datasets[ aline.split()[0].strip() ] = int( aline.split()[4].strip() )
# Let the people know what we need to do next
print(f'Will process {len(datasets.keys())} datasets')

# Get our rucio client ready
from rucio.client.client import Client
rc = Client()

# List of user DIDs for transfer (including those that have been created and those that we take whole)
user_did_list = []
# Dictionary mapping datasets to files - only those files at CERN that we've transferred
file_dictionary = {}
# Dictionary mapping ATLAS dataset names to user-created dataset names
user_did_dict = {}

# Loop over all the datasets
for dataset in datasets:
    # Sum of events for this dataset
    did_sum = 0
    # File list for this dataset
    did_file_list = []
    # Scope for this dataset (list does not contain scope)
    my_scope=dataset.split('.')[0]
    # Get all the files in this dataset from rucio
    fl = rc.list_files(scope=my_scope,name=dataset)
    # Minimal number of files required to reach the desired target - need to sort
    sorted_fl = sorted(fl , key=lambda x: x['events'], reverse=True)
    # Note that we're stashing the full file list so we can check if we got all the files later
    for a in sorted_fl:
        # Add to the number of events in the (temporary) dataset the events in this file
        did_sum += a['events']
        # Keep a list of datasets in the format we'll want them in for rucio
        did_file_list += [ {'scope':my_scope,'name':a['name']} ]
        # If we got enough events, we can stop adding files now
        if did_sum >= datasets[dataset]:
            break
    # Check that we reached the right number
    if did_sum < datasets[dataset]:
        print(f'Warning: dataset {dataset} appears to have {did_sum} < {datasets[dataset]} events - will move the whole thing')
    # Should we just take the entire dataset?
    if did_sum < datasets[dataset] or len(sorted_fl)==len(did_file_list):
        # Add the entire dataset to the list that we'll transfer
        user_did_list += [ { 'scope':my_scope, 'name':dataset } ]
        # Add the entire file list to the dictionary of files
        file_dictionary[ dataset ] = [ x['name'] for x in did_file_list ]
        # Let the people know what we're doing
        print(f'Taking {dataset} in its entirety for {did_sum} events (wanted {datasets[dataset]})')
    else:
        # Grab the DSID of the input MC dataset
        did_number = dataset.split('.')[1]
        # Create a new dataset name based on that DSID and our pre- and post-fixes
        new_ds_name = f'{static_did_pre}{did_number}{static_did_post}'
        # Create the new dataset with that name - only if we really are interacting with rucio
        if really_use_rucio:
            rc.add_dataset(scope=scope_did,name=new_ds_name)
        # Attach our files to that dataset - again, only if we really are interacting with rucio
        if really_use_rucio:
            rc.add_files_to_datasets( [ { 'scope':scope_did , 'name':new_ds_name , 'dids':did_file_list } ] )
        # Update bookkeeping - dictionary of files and map of ATLAS dataset to user dataset names
        file_dictionary[ dataset ] = [ x['name'] for x in did_file_list ]
        user_did_dict[ dataset ] = new_ds_name
        # Add the dataset to our list of datasets to transfer
        user_did_list += [ { 'scope':scope_did, 'name':new_ds_name } ]
        # Let the people know what we're doing
        print(f'From {dataset} created {new_ds_name} containing {len(did_file_list)} files with {did_sum} events (requested {datasets[dataset]})')

## Create rule(s) for our new dataset(s)
# Fake transfer IDs in case they help later
rid = ['0b527f5c31444f5a892af8b736875887', 'b8b526f691fb4f6f9f368bf3309c79b0', 'a57914d5bd8846878a378ef856f3dbd6']
if really_use_rucio:
    try:
        rid = rc.add_replication_rule(dids=user_did_list, # The list of datasets we want to transfer
                                      copies=1, # Just one copy please
                                      rse_expression='CERN-PROD_OPENDATA', # Destination RSE
                                      account='zmarshal', # My account for the time being
                                      activity='Data Consolidation', # Recommended by Mario
                                      notify='N', # No need for notifications
                                      comment='Transfer for Open Data') # Comment to make these visible in the system
        # Or activity="User Subscriptions"
    except Exception as e:
        print('An error occurred during rucio rule creation. Check the rules carefully!')
print(f'Created rules {rid} for {len(user_did_list)} datasets to be transferred')

# Record the rules that we just made
with open( 'mc_rule_list'+static_did_post+'.txt' , 'w' ) as rule_list:
    rule_list.write( '\n'.join(rid) )

# Record the file mapping that we established
with open( 'mc_file_mapping'+static_did_post+'.json', 'w' ) as file_backup:
    json.dump( obj={'file_dictionary':file_dictionary,'user_did_dictionary':user_did_dict,'rule_list':rid} , fp=file_backup )

# All done!
