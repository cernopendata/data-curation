#!/usr/bin/env python3
import datetime

dataset_input = 'pp_data.txt'
static_did_post = '_OpenData_v0_'+datetime.date.today().isoformat()

dataset_list_file = open(dataset_input,'r')
datasets = {}
for bline in dataset_list_file:
    aline = bline.split('#')[0].strip()
    if len(aline)<2:
        continue
    datasets[ aline.strip() ] = []
dataset_list_file.close()
print(f'Read in {len(datasets.keys())} datasets')

from rucio.client.didclient import DIDClient

dc = DIDClient()

# Loop over all the datasets
for dataset in datasets:
    did_file_list = []
    my_scope=dataset.split(':')[0]
    fl = dc.list_files(scope=my_scope,name=dataset.split(':')[1])
    # Minimal number of files required to reach the desired target
    sorted_fl = sorted(fl , key=lambda x: x['events'], reverse=True)
    # Note that we're stashing the full file list so we can check if we got all the files later
    if len(sorted_fl)==0:
        print(f'Warning: no files found for dataset {dataset}')
        continue
    for a in sorted_fl:
        # Keep a list of datasets in the format we'll want them in for rucio
        datasets[dataset] += [ a['name'] ]

# Record the file mapping that we established
import json
file_backup = open( 'data_file_mapping'+static_did_post+'.json' , 'w' )
json.dump( obj={'file_dictionary':datasets} , fp=file_backup )
file_backup.close()

