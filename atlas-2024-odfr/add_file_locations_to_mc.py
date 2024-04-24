#!/usr/bin/env python3
import datetime
import json

# Previous request json files created when rucio rules were set up
previous_requests = ['mc_file_mapping_OpenData_v1_p6026_2024-04-23.json']
# Already did: 'mc_file_mapping_OpenData_v0_p6026_2024-04-16.json']

# Get our rucio client ready
from rucio.client.client import Client
rc = Client()

# Loop over the previous requests and grab the json files
for old_request_json in previous_requests:
    with open(old_request_json,'r') as old_request_file:
        # Holder dictionary for our file location data
        # Dictionary of Datasets --> dictionary of file names
        #    file names --> dictionary of properties (checksum, events, uri, type, size)
        file_locations = {}
        # Load the old request json data
        old_request_data = json.load(old_request_file)
        # Load the old request datasets
        datasets = old_request_data['file_dictionary'].keys()
        # Loop through the datasets
        for dataset_number,dataset in enumerate(datasets):
            # Let the people know how we're doing
            if (dataset_number+1)%10==0:
                print(f'Working on dataset {dataset_number+1} of {len(datasets)}: {dataset}')
            # Set up the file location dictionary
            file_locations[dataset] = {}
            # Get the scope - datasets do not have the scope by default
            my_scope=dataset.split('.')[0]
            # Frst rucio query to get the file location on eos
            replicalist = rc.list_replicas([{'scope':my_scope,'name':dataset}])
            # Go through all the results (all the files in the dataset again)
            for areplica in replicalist:
                # Go through the physical locations and get the one at the open data endpoint
                # This will not necessarily succeed - for some large MC sets, not all files are at CERN
                for a_pfn in areplica['pfns']:
                    if 'opendata/atlas' in a_pfn:
                        file_locations[dataset][ my_scope+':'+areplica['name'] ] = {'uri':a_pfn}
                        break
            # Compare the list of files we found on eos to the list we expected to find
            # This is slow, but I think the error checking is worth it (and we don't run this script often)
            # Checking both directions for extra security
            for afile in file_locations[dataset]:
                # file_locations includes scope
                if afile.split(':')[1] not in old_request_data['file_dictionary'][dataset]:
                    print(f'File {afile} in rucio on eos and not in json list')
            for afile in old_request_data['file_dictionary'][dataset]:
                # old_request_data does not include scope
                if my_scope+':'+afile not in file_locations[dataset]:
                    print(f'File {afile} not in rucio on eos and in json list')
            # Now add the rest of the metadata for the files based on a different rucio query
            # Grab the list of files from rucio
            fl = rc.list_files(scope=my_scope,name=dataset)
            # Put together the rest of the file record
            for a in fl:
                # Make sure this file is in our list
                if my_scope+':'+a['name'] not in file_locations[dataset]:
                    continue
                # Update the per-file metadata
                file_locations[dataset][ my_scope+':'+a['name'] ].update( { 'checksum':'adler32'+a['adler32'], 'size':a['bytes'], 'events':a['events'], 'type':'DAOD_PHYSLITE' } )

        # Record the file mapping that we established
        import json
        with open( old_request_json.replace('.json','_with_metadata.json') , 'w' ) as file_backup:
            json.dump( obj={'file_dictionary':old_request_data['file_dictionary'],
                            'user_did_dictionary':old_request_data['user_did_dictionary'],
                            'rule_list':old_request_data['rule_list'],
                            'file_locations':file_locations} , fp=file_backup )
    # Looping over requests
# All done!
