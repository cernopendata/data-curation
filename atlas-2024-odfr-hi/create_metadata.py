#!/usr/bin/env python3
import datetime

# Grab the list of datasets that we want to run over
dataset_input = 'dataset_list.txt'

# Set a post-fix for the file, so that we can nicely version things
static_did_post = '_OpenData_v0_p6480_'+datetime.date.today().isoformat()

# Dictionary mapping datasets to file names
datasets = {}
# Dictionary of Datasets --> dictionary of file names
#    file names --> dictionary of properties (checksum, events, uri, type, size)
file_locations = {}

# Let's go over the list of files...
with open(dataset_input,'r') as dataset_list_file:
    for bline in dataset_list_file:
        # Make sure we ignore comments - in case folks are commenting out datasets
        aline = bline.split('#')[0].strip()
        if len(aline)<2:
            continue
        # Initialize our dataset lists and file location lists
        datasets[ aline.strip() ] = []
        file_locations[ aline.strip() ] = {}
print(f'Read in {len(datasets.keys())} datasets')

# Get our rucio client ready
from rucio.client.client import Client
rc = Client()

# Loop over all the datasets
for dataset_number,dataset in enumerate(datasets):
    # Let the people know how we're doing
    if (dataset_number+1)%10==0:
        print(f'Working on dataset {dataset_number+1} of {len(datasets)}: {dataset}')

    # Get the scope
    my_scope=dataset.split(':')[0]

    # Grab the list of files from rucio - for HI, we are always going to take _all_ the events
    fl = rc.list_files(scope=my_scope,name=dataset.split(':')[1])
    # Note that we're stashing the full file list so we can check if we got all the files later
    for a in fl:
        # Update the map of datasets : files
        datasets[dataset] += [ a['name'] ]
        # Get the first part of the per-file metadata
        file_locations[dataset][ my_scope+':'+a['name'] ] = { 'checksum':'adler32'+a['adler32'], 'size':a['bytes'], 'events':a['events'], 'type':'DAOD_HION14' }
    # Second rucio query, needed to get the file location on eos
    replicalist = rc.list_replicas([{'scope':my_scope,'name':dataset.split(':')[1]}])
    # Go through all the results (all the files in the dataset again)
    for areplica in replicalist:
        # Make sure we found that file before - just error checking, this should never be printed
        if areplica['scope']+':'+areplica['name'] not in file_locations[dataset]:
            print(f'Warning: did not find {areplica["scope"]} {areplica["name"]} in file_locations for {dataset}')
            continue
        # Go through the physical locations and get the one at the open data endpoint
        for a_pfn in areplica['pfns']:
            if 'opendata/atlas' in a_pfn:
                file_locations[dataset][ my_scope+':'+areplica['name'] ]['uri'] = a_pfn
                break
        else:
            # We didn't find one on the open data endpoint
            print(f'Did not find {dataset} file {my_scope+":"+areplica["name"]} on eos in pfns {areplica["pfns"]}')

# Record the file mapping that we established
import json
with open( 'hion_file_mapping'+static_did_post+'.json' , 'w' ) as file_backup:
    json.dump( obj={'file_dictionary':datasets, 'file_locations':file_locations} , fp=file_backup )

# All done!
