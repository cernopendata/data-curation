#!/usr/bin/env python3

# For reading the csv metadata file
import csv

# For storing a metadata json output
import json

# Get the record map with names and keywords, then add sample counters
from sample_rules import record_map
for a in record_map:
    a['entries'] = 0
    a['ds_list'] = []

# The dictionary of keywords and number of entries matching each keyword
unsorted_kw_dict = {}
samples = {'sorted':0, 'unsorted':0}
unsorted_samples = []

# Open our metadata file to go through all the EVNT samples we've gathered metadata for
with open('EVNT_metadata.csv','r') as evgen_metadata_csv_file:
    # Open this as a formatted dictionary
    md_reader = csv.DictReader(evgen_metadata_csv_file, delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL,lineterminator='\n')
    # Loop through all the rows in the file (header skipped automatically for DictReader)
    for row in md_reader:
        # Get the list of keywords for this sample
        kw_list = [x.strip() for x in row['Keywords'].split(',')]
        # Check for a bad sample
        if len(kw_list)==0:
            print(f'Warning: sample {row["DSID"]} has no keywords')
        if '' in kw_list:
            print(f'Found empty keyword in sample {row["DSID"]}')

        # First see if this one is already established
        found = False
        for anitem in record_map:
            # Identified a match
            if all([ (x in kw_list) for x in anitem['kwl'] ]) and not any([ (x in kw_list) for x in anitem['not_kwl'] ]):
                if found:
                    print(f'Sample {row["DSID"]} with keywords {kw_list} found more than once')
                found = True
                anitem['entries'] += 1
                anitem['ds_list'] += [ row['DSID'] ]

        # If the sample wasn't found, add it to the unsorted sample list
        if not found:
            samples['unsorted'] += 1
            # Add the keywords to the dictionaries
            for kw in kw_list:
                if kw not in unsorted_kw_dict:
                    unsorted_kw_dict[kw] = 0
                unsorted_kw_dict[kw] += 1
            unsorted_samples += [ row['DSID'] ]
        else:
            samples['sorted'] += 1

print('\nList of unsorted sample keywords')
for kw in unsorted_kw_dict:
    print(f'{unsorted_kw_dict[kw]} instances of keyword {kw}')
print('\nKnown sample breakdown (check for balance)')
uniq_record_names = list(set( [ x['name'] for x in record_map ] ))
for anitem in uniq_record_names:
    my_count = sum( [ x['entries'] for x in record_map if x['name']==anitem ] )
    print(f'Collection {anitem} has {my_count} samples')
print(f'\n{samples["sorted"]} samples sorted into {len(uniq_record_names)} entries; {samples["unsorted"]} still to go')
if 0<len(unsorted_samples)<10:
    print(f'Unsorted DSIDs remaining: {unsorted_samples}')

# Now create a small metadata JSON file
# This one we will build as a dictionary indexed by name, with the samples we want included
sample_dict = {}
for anitem in uniq_record_names:
    sample_dict[anitem] = {'samples':[],'keywords':[]}
    for a_record in record_map:
        if a_record['name'] == anitem:
            sample_dict[anitem]['samples'] += a_record['ds_list']
            sample_dict[anitem]['keywords'] = a_record['ODkwl']

# Record the sample and keyword mapping that we established
with open( 'od_hepmc_sample_map.json' , 'w' ) as file_backup:
    json.dump( obj={'sample_dict':sample_dict},
               fp=file_backup,
               indent=2,
               sort_keys=True,
               ensure_ascii=False,
               separators=(",", ": ") )
# All done!
