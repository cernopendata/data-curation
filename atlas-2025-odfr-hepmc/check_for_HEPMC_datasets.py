#!/usr/bin/env python3

# Identify new HEPMC datasets that we should release in this round

# Get our rucio client ready
try:
    from rucio.client.client import Client
    rc = Client()
except ImportError:
    print('Do not forget to set up rucio first!')
    print('lsetup rucio')
    print('And then voms proxy init')
    import sys
    sys.exit(1)

# The input dataset list that I'm going to use
datasets = []
# For looping over several files in one go
import fileinput
for aset_line in fileinput.input(['EVNT_prod_request15.csv','EVNT_prod_request23.csv']):
    # Allow for commented lines in the input file in case folks are excluding datasets
    aline = aset_line.split('#')[0].strip()
    if len(aline.split())<2:
        continue
    # Deal with the format of the production spreadsheet - could parse csv, but this is easy enough
    datasets += [ aline.split('","')[1].strip() ]
# Let the people know what we need to do next
print(f'Will process {len(datasets)} datasets')

# De-duplicate...
already_processed = []
# Make sure it exists before opening it
import os
if os.access('HEPMC_datasets.txt',os.R_OK):
    with open('HEPMC_datasets.txt','r') as hepmc_list:
        for aline in hepmc_list:
            already_processed += [ aline.split('.HEPMC')[0] ]
print(f'Will exclude {len(already_processed)} samples')

# Now build a list of HEPMC datasets that we've identified
no_hepmc = []
with open('HEPMC_datasets.txt','a') as output_list:
    for ndataset,adataset in enumerate(datasets):
        # MC15 scope moved
        dataset = adataset.replace('mc15_13TeV','mc16_13TeV')
        # Let folks know where we are in the process
        if (ndataset+1)%100==0:
            print(f'Processing dataset {ndataset+1}')
        # The list does not have scopes attached
        my_scope = dataset.split('.')[0]
        # Check if the dataset has already been processed
        if dataset.split('.EVNT')[0] in already_processed:
            continue
        # Try to find out the name of the corresponding HEPMC dataset
        dsname = dataset.replace('.EVNT.','.HEPMC.')+'_e*'
        dids = [ did for did in rc.list_dids(scope=my_scope,filters={'name':dsname}) if '_tid' not in did ]
        # This should not happen - HEPMC datasets should be unique (no reason for multiple versions)
        if len(dids)>1:
            print(f'Multiple HEPMC sets found for {dataset}: {dids}')
        # Record the one we think is the correct one
        if len(dids)>0:
            output_list.write(dids[0]+'\n')
        # If we didn't find one, then add it to the list of sets still to go
        else:
            no_hepmc += [dataset]

print(f'Looked through {len(datasets)} datasets, found {len(no_hepmc)} without HEPMC files.')
