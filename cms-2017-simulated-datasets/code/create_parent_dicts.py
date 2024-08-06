#!/usr/bin/env python3

import datetime
import fnmatch
import os
import re
import requests
import subprocess
import urllib3

from dataset_records import *
from das_json_store import get_parent_dataset

def main(datasets):
    nano_to_mini = dict()
    mini_to_nano = dict()
    
    for dataset in datasets:
        if dataset.endswith('NANOAODSIM'):
            nano = dataset
            mini = get_parent_dataset(nano, das_dir= './inputs/das-json-store')
            try:
                
                if mini.endswith('/AODSIM'):
                    print('AODSIM parent dataset found for', dataset)
                    result = subprocess.run(f'dasgoclient -query="parent dataset={nano}"', capture_output= True, shell= True, text= True).stdout.split('\n')
                    for line in result:
                        if line.endswith('MINIAODSIM'):
                            mini = line
            except:
                print('No MINIAODSIM parent dataset found for', nano)

            if mini:
                nano_to_mini[nano] = mini
                mini_to_nano[mini] = nano
            else:
                print('No parent dataset found for', nano)

    for dataset in datasets:
        if dataset.endswith('MINIAODSIM'):
            if dataset not in mini_to_nano.keys():
                print('No child dataset found for', dataset)

    with open('inputs/parent_dicts.py', 'w') as py_file:
        py_file.write('nano_to_mini = {\n')
        for key, value in nano_to_mini.items():
            py_file.write(f'    "{key}": "{value}",\n')
        py_file.write('}\n')
        py_file.write('\n')
        py_file.write('mini_to_nano = {\n')
        for key, value in mini_to_nano.items():
            py_file.write(f'    "{key}": "{value}",\n')
        py_file.write('}\n')
    
    print('Parent dictionaries created in parent_dicts.py')
