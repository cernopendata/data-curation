#!/usr/bin/env python3

# For reading and writing json metadata files
import json

# Grab the list of datasets that we want to run over
dataset_input = 'HEPMC_datasets.txt'

# Dictionary mapping datasets to file names
datasets = {}
# Dictionary of Datasets --> dictionary of file names
#    file names --> dictionary of properties (checksum, events, uri, type, size)
file_locations = {}

# Get the previously created metadata
previously_processed = []
import os
if os.access('od_hepmc_file_mapping.json', os.R_OK):
    with open( 'od_hepmc_file_mapping.json' , 'r' ) as file_backup:
        md_data = json.load(file_backup)
        datasets = md_data['file_dictionary']
        file_locations = md_data['file_locations']
        previously_processed += [ x for x in md_data['file_dictionary'] ]
# Let folks know what we've done so far
print(f'Found {len(previously_processed)} previously processed datasets')

# Create the input dataset list that I'm going to use
with open(dataset_input,'r') as input_hepmc:
    for aset_line in input_hepmc:
        # Check for duplicates and skip
        if aset_line.strip() in previously_processed:
            continue
        # Initialize our dataset lists and file location lists
        datasets[ aset_line.strip() ] = []
        file_locations[ aset_line.strip() ] = {}
# Let the people know how much work we need to do next
print(f'Read in {len(datasets.keys())} datasets')

# Now we will remove by hand a couple of datasets so that their information is re-added
for aset in []:
    datasets[aset] = []
    file_locations[aset] = {}

# Get our rucio client ready
from rucio.client.client import Client
rc = Client()

added_datasets = 0
# Loop over all the datasets
for dataset_number,dataset in enumerate(datasets):
    # Let the people know how we're doing
    print(f'Working on dataset {dataset_number+1} of {len(datasets)}: {dataset}')
    # Get the scope - dataset names are saved without the scope on them
    my_scope=dataset.split('.')[0]
    verbose = False #dataset in ['mc16_13TeV.345056.PowhegPythia8EvtGen_NNPDF3_AZNLO_ZH125J_MINLO_vvbb_VpT.evgen.HEPMC.e5706_e8601']

    # Get a list of files if we don't already have one
    if len( datasets[dataset] )==0:
        # Get the scope - dataset names are saved without the scope on them
        my_scope=dataset.split('.')[0]

        # Go through the datasets inside the container
        datasetlist = rc.list_content(scope=my_scope,name=dataset)
        for ads in datasetlist:
            # Grab the list of files from rucio - for education and outreach, we are always going to take _all_ the events
            fl = rc.list_files(scope=ads['scope'],name=ads['name'])
            # Note that we're stashing the full file list so we can check if we got all the files later
            for a in fl:
                if verbose:
                    print(f'Working on {dataset} {a}')
                # Update the map of datasets : files
                datasets[dataset] += [ a['name'] ]
                # Get the first part of the per-file metadata
                file_locations[dataset][ a['scope']+':'+a['name'] ] = { 'checksum':'adler32:'+a['adler32'], 'size':a['bytes'], 'events':a['events'], 'type':'HEPMC' }
    
            # Rucio query to get the file location on eos
            replicalist = rc.list_replicas([{'scope':ads['scope'],'name':ads['name']}], rse_expression='CERN-PROD_OPENDATA')
            # Go through all the results (all the files in the dataset again)
            for areplica in replicalist:
                if verbose: 
                    print(f'Working on replica {dataset} {areplica}')
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
            if verbose:
                print(f'Found {dataset} with {len(file_locations[dataset])} files')
        added_datasets += 1
    else:
        print(f'Already have information for {dataset}')
    if added_datasets>600:
        print('Added over 600 datasets. Thats enough work for one pass. Stopping here.')
        break
else:
    print('Got the metadata for all the datasets!')

# Record the file mapping that we established if we had at least one dataset
with open( 'od_hepmc_file_mapping.json' , 'w' ) as file_backup:
    json.dump( obj={'file_dictionary':datasets, 'file_locations':file_locations} , fp=file_backup )

# All done!
