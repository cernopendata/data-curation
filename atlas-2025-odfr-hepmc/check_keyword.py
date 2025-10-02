#!/usr/bin/env python3

# For reading the csv metadata file
import csv

# Set up the record map with names and keywords, then add sample counters
from sample_rules import record_map

# The dictionary of keywords and number of entries matching each keyword
unsorted_kw_dict = {}

import sys
test_kws = []
test_not_kws = []
not_kws = False
show_samples = False
exclude_sorted = False
for x in sys.argv[1:]:
    if x == '-n':
        not_kws = True
    elif x == '-s':
        show_samples = True
    elif x == '-x':
        exclude_sorted = True
    elif not_kws:
        test_not_kws += x.split(',')
    else:
        test_kws += x.split(',')
if len(test_kws)==0 and len(test_not_kws)==0:
    test_kws=['']
print(f'Searching for keywords {test_kws} and not keywords {test_not_kws}')

with open('EVNT_metadata.csv','r') as evgen_metadata_csv_file:
    # Open this as a formatted dictionary
    md_reader = csv.DictReader(evgen_metadata_csv_file, delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL,lineterminator='\n')
    # Loop through all the rows in the file (header skipped automatically for DictReader)
    for row in md_reader:
        # Get the list of keywords for this sample
        kw_list = [x.strip() for x in row['Keywords'].split(',')]

        # First see if this one is already sorted and we wanted to ignore sorted records
        if exclude_sorted:
            found = False
            for anitem in record_map:
                # Identified a match
                if all([ (x in kw_list) for x in anitem['kwl'] ]) and not any([ (x in kw_list) for x in anitem['not_kwl'] ]):
                    found = True
                    break
            if found:
                continue

        if all([x in kw_list for x in test_kws]) and not any([x in kw_list for x in test_not_kws]):
            if show_samples:
                print(f'Sample {row["DSID"]}')
            for kw in kw_list:
                if kw not in unsorted_kw_dict:
                    unsorted_kw_dict[kw] = 0
                unsorted_kw_dict[kw] += 1

print(unsorted_kw_dict)
