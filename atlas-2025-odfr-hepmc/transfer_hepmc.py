#!/usr/bin/env python3
import datetime
import json

# The file containing the datasets to be processed
hepmc_dataset_input = 'HEPMC_datasets.txt'

# The rucio RSE we're using
rucio_RSE = 'CERN-PROD_OPENDATA' #'MWT2_OPENDATA' #'CERN-PROD_OPENDATA'

# Flag to disable the use of rucio - so that we can test and make json files without making rules
really_use_rucio = True
if really_use_rucio:
    print('Really using rucio for data transfers')
else:
    print('Not really using rucio - test run')

# The input dataset list that I'm going to use
datasets = []
with open(hepmc_dataset_input,'r') as dataset_list_file:
    for bline in dataset_list_file:
        # Allow for commented lines in the input file in case folks are excluding datasets
        aline = bline.split('#')[0].strip()
        if len(aline)<2:
            continue
        # Current lines have dataset name
        datasets += [ aline ]
# Let the people know what we need to do next
print(f'Will process {len(datasets)} datasets')

# Get our rucio client ready
from rucio.client.client import Client
rc = Client()

# Set the proper account
import os
os.environ['RUCIO_ACCOUNT'] = 'opendata'

# Samples to transfer
transfer_did_list = []

total_so_far = 0.
total_to_move = 0.
count_so_far = 0
count_to_move = 0

# Loop over all the datasets
for dataset in datasets:
    my_scope = dataset.split('.')[0]
    ds_total = 0.
    for afile in rc.list_files(scope=my_scope,name=dataset):
        ds_total += afile['bytes']

    for arule in rc.list_did_rules(scope=my_scope, name=dataset):
        if arule['rse_expression'] == rucio_RSE:
            #print(f'Rule found for {dataset=}. Continuing.')
            total_so_far += ds_total
            count_so_far += 1
            break
    else:
        ## No rule found - Add the entire dataset to the list that we'll transfer
        #transfer_did_list += [ { 'scope':my_scope, 'name':dataset } ]
        total_to_move += ds_total
        count_to_move += 1
        print(f'Making a rule for {my_scope} {dataset}')
        if really_use_rucio:

            # Go through the datasets inside the container
            datasetlist = rc.list_content(scope=my_scope,name=dataset)
            for ads in datasetlist:
                rid = rc.add_replication_rule(dids=[{ 'scope':ads['scope'], 'name':ads['name']}], # The list of datasets we want to transfer
                                              copies=1, # Just one copy please
                                              rse_expression=rucio_RSE, # Destination RSE
                                              account='opendata', # Official open data account
                                              activity='Data Consolidation', # Recommended by Mario
                                              notify='N', # No need for notifications
                                              comment='Transfer for Open Data') # Comment to make these visible in the system
                print(rid)

print(f'Already moved {total_so_far*1e-12} TB, with {total_to_move*1e-12} TB still to go')
print(f'That includes {count_so_far} datasets moved already and {count_to_move} still to go')

### Create rule(s) for our new dataset(s)
## Fake transfer IDs in case they help later
#rid = ['0b527f5c31444f5a892af8b736875887', 'b8b526f691fb4f6f9f368bf3309c79b0', 'a57914d5bd8846878a378ef856f3dbd6']
#if really_use_rucio:
#    try:
#        rid = rc.add_replication_rule(dids=transfer_did_list, # The list of datasets we want to transfer
#                                      copies=1, # Just one copy please
#                                      rse_expression=rucio_RSE, # Destination RSE
#                                      account='opendata', # Official open data account
#                                      activity='Data Consolidation', # Recommended by Mario
#                                      notify='N', # No need for notifications
#                                      comment='Transfer for Open Data') # Comment to make these visible in the system
#        # Or activity="User Subscriptions"
#    except Exception as e:
#        print('An error occurred during rucio rule creation. Check the rules carefully!')
#        print(e)
#print(f'Created rules {rid} for {len(transfer_did_list)} datasets to be transferred')

# All done!
