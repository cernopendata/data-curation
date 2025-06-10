#!/usr/bin/env python3

# Simple script to convert csv metadata file into a full js code file

# For pretty printing and writing json
import json

# For csv reading
import csv

# File with the mapping of file names for each dataset - merge all the metadata files we have
import glob
json_file_locations = {}
for md_file in glob.glob('od_hepmc_file_mapping*.json'):
    with open(md_file,'r') as json_metadata_file:
        json_file_locations.update( json.load(json_metadata_file)['file_locations'] )

# Open our metadata file to go through all the EVNT samples we've gathered metadata for
with open('EVNT_metadata.csv','r') as evgen_metadata_csv_file, open('database_metadata.json','w') as metadata_json_file:

    # For each line in the metadata file we're going to compose a final metadata entry
    full_md = {}

    # Open the metadata as a formatted dictionary
    md_reader = csv.DictReader(evgen_metadata_csv_file, delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL,lineterminator='\n')
    # Loop through all the rows in the file (header skipped automatically for DictReader)
    for row in md_reader:
        my_dsid = row['DSID']
        full_md[my_dsid] = { x:row[x] for x in row if x!='DSID' }
        for akey in json_file_locations:
            if akey.split('.')[1]==my_dsid:
                full_md[my_dsid]['file_list'] = [ json_file_locations[akey][x]['uri'] for x in json_file_locations[akey] ]
        full_md[my_dsid]['Keywords'] = [ x.strip() for x in full_md[my_dsid]['Keywords'].split(',') ]

    json.dump(
        [ full_md ],
        metadata_json_file,
        indent=2,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ": "),
    )
