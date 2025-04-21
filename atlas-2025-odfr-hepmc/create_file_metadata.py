#!/usr/bin/env python3

# For timestamps on the json files
import datetime

# For reading and writing json metadata files
import json

# For identifying existing metadata records so we know what to skip
import glob

# Grab the list of datasets that we want to run over
dataset_input = 'dataset_list.txt'

# Set a post-fix for the file, so that we can nicely version things
static_did_post = '_'+datetime.date.today().isoformat()

# Dictionary mapping datasets to file names
datasets = {}
# Dictionary of Datasets --> dictionary of file names
#    file names --> dictionary of properties (checksum, events, uri, type, size)
file_locations = {}

# Get the previously created metadata
previously_processed = []
md_archives = glob.glob('od_hepmc_file_mapping*.json')
for md_archive in md_archives:
    with open( md_archive , 'r' ) as file_backup:
        md_data = json.load(file_backup)
        previously_processed += [ x for x in md_data['file_dictionary'] ]
# Let folks know what we've done so far
print(f'Found {len(previously_processed)} previously processed datasets in {len(md_archives)} archive files')

# Create the input dataset list that I'm going to use
with open('HEPMC_datasets.txt','r') as input_hepmc:
    for aset_line in input_hepmc:
        # Check for duplicates and skip
        if aset_line.strip() in previously_processed:
            continue
        # Initialize our dataset lists and file location lists
        datasets[ aset_line.strip() ] = []
        file_locations[ aset_line.strip() ] = {}
# Let the people know how much work we need to do next
print(f'Read in {len(datasets.keys())} datasets')

# Get our rucio client ready
from rucio.client.client import Client
rc = Client()

# Loop over all the datasets
for dataset_number,dataset in enumerate(datasets):
    # Let the people know how we're doing
    print(f'Working on dataset {dataset_number+1} of {len(datasets)}: {dataset}')

    # Get the scope - dataset names are saved without the scope on them
    my_scope=dataset.split('.')[0]

    # Grab the list of files from rucio - for education and outreach, we are always going to take _all_ the events
    fl = rc.list_files(scope=my_scope,name=dataset)
    # Note that we're stashing the full file list so we can check if we got all the files later
    for a in fl:
        # Update the map of datasets : files
        datasets[dataset] += [ a['name'] ]
        # Get the first part of the per-file metadata
        file_locations[dataset][ a['scope']+':'+a['name'] ] = { 'checksum':'adler32:'+a['adler32'], 'size':a['bytes'], 'events':a['events'], 'type':'HEPMC' }

    # Second rucio query, needed to get the file location on eos
    replicalist = rc.list_replicas([{'scope':my_scope,'name':dataset}])
    # Go through all the results (all the files in the dataset again)
    for areplica in replicalist:
        # Make sure we found that file before - just error checking, this should never be printed
        if areplica['scope']+':'+areplica['name'] not in file_locations[dataset]:
            print(f'Warning: did not find {areplica["scope"]} {areplica["name"]} in file_locations for {dataset}')
            continue
        # Go through the physical locations and get the one at the open data endpoint
        for a_pfn in areplica['pfns']:
            if areplica['pfns'][a_pfn]['rse']=='CERN-PROD_OPENDATA':
                file_locations[dataset][ areplica['scope']+':'+areplica['name'] ]['uri'] = a_pfn
                break
        else:
            # We didn't find one on the open data endpoint
            print(f'Did not find {dataset} file {my_scope+":"+areplica["name"]} on eos in pfns {areplica["pfns"]}')

# Record the file mapping that we established if we had at least one dataset
if len(datasets)>0:
    with open( 'od_hepmc_file_mapping'+static_did_post+'.json' , 'w' ) as file_backup:
        json.dump( obj={'file_dictionary':datasets, 'file_locations':file_locations} , fp=file_backup )
else:
    print('No new datasets identified')

# All done!
