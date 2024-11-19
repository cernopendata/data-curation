#!/usr/bin/env python3

# Scope for the rucio datasets I'll be creating
scope_did = 'opendata' #'user.zmarshal'

# Don't forget to export RUCIO_ACCOUNT=opendata if we need it
import os
if scope_did == 'opendata':
    os.environ['RUCIO_ACCOUNT'] = 'opendata'

dataset_list = []
with open('dataset_list.txt','r') as dataset_list_file:
   for line in dataset_list_file:
       dataset_list += [ line.strip() ]

# Get our rucio client ready
really_use_rucio = True
from rucio.client.client import Client
rc = Client()

# Overall containers
overall_containers = []

# Loop over the data first and create new datasets
new_data_datasets = []
new_mc_datasets = []

# We know everything was transferred here, so we need to add all the files
for a_ds in dataset_list:
    old_scope = a_ds.split(':')[0]
    # Keep the dataset name, but move it into the new scope
    new_ds_name = a_ds.split(':')[1]

    # Create the new dataset with that name - only if we really are interacting with rucio
    if really_use_rucio:
        if len( [x for x in rc.list_dids(scope=scope_did,filters=[{'name':new_ds_name}]) ] )>0:
            print(f'Appears {scope_did}:{new_ds_name} already exists - skipping')
            if 'data' in old_scope:
                new_data_datasets += [ {'scope':scope_did,'name':new_ds_name} ]
            if 'mc' in old_scope:
                new_mc_datasets += [ {'scope':scope_did,'name':new_ds_name} ]
            continue
        rc.add_dataset(scope=scope_did,name=new_ds_name)
    print(f'{"" if really_use_rucio else "(Not) "}Creating dataset {scope_did}:{new_ds_name}')

    # Prepare the list of files in the format we need
    # Attach our files to that dataset - again, only if we really are interacting with rucio
    if really_use_rucio:
        did_file_list = [ {'scope':x['scope'],'name':x['name']} for x in rc.list_files( scope=old_scope, name=new_ds_name ) ]
        if len(did_file_list)==0:
            print(f'No files found in dataset {new_ds_name} - skipping')
        else:
            # Do this in 500-file chunks
            for chunk in range(0,len(did_file_list),500):
                rc.add_files_to_datasets( [ { 'scope':scope_did , 'name':new_ds_name , 'dids':did_file_list[chunk:500+chunk] } ] )

    if 'data' in old_scope:
        new_data_datasets += [ {'scope':scope_did,'name':new_ds_name} ]
    if 'mc' in old_scope:
        new_mc_datasets += [ {'scope':scope_did,'name':new_ds_name} ]
new_container_data = 'opendata_pp_data15_2024_release_p6480_v1'
new_container_mc = 'opendata_pp_data16_2024_release_p6480_v1'

if really_use_rucio:
    if len( [x for x in rc.list_dids(scope=scope_did,filters=[{'name':new_container_data}]) ] )==0:
        rc.add_container(scope=scope_did,name=new_container_data)
    rc.add_datasets_to_containers([{'scope':scope_did,'name':new_container_data,'dids':new_data_datasets}])
    if len( [x for x in rc.list_dids(scope=scope_did,filters=[{'name':new_container_mc}]) ] )==0:
        rc.add_container(scope=scope_did,name=new_container_mc)
    rc.add_datasets_to_containers([{'scope':scope_did,'name':new_container_mc,'dids':new_mc_datasets}])
overall_containers += [ {'scope':scope_did,'name':new_container_data} ]
overall_containers += [ {'scope':scope_did,'name':new_container_mc} ]
print(f'{"" if really_use_rucio else "(Not) "}Created container {scope_did}:{new_container_data}')
print(f'{"" if really_use_rucio else "(Not) "}Created container {scope_did}:{new_container_mc}')

# Finally create a single top-level container that includes everything
overall_container = 'opendata_PbPb_2024_release_p6480_v1'
if really_use_rucio:
    if len( [x for x in rc.list_dids(scope=scope_did,filters=[{'name':overall_container}]) ] )==0:
        rc.add_container(scope=scope_did,name=overall_container)
    rc.add_containers_to_containers([{'scope':scope_did,'name':overall_container,'dids':overall_containers}])
print(f'{"" if really_use_rucio else "(Not) "}Created container {scope_did}:{overall_container}')

print(f"\nDon't forget:")
print(f'rucio add-rule --activity "Data Consolidation" --notify N --comment "Transfer for Open Data" --account opendata --skip-duplicates {scope_did}:{overall_container} 1 CERN-PROD_OPENDATA')

