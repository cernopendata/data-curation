#!/usr/bin/env python3

# Simple script to convert csv metadata file into a full js code file

# For pretty printing and writing json
import json

# For csv reading
import csv

# File with the mapping of file names for each dataset
json_metadata_file = open('odeo_file_mapping_ODEO_v0_FEB2025_2025-06-30.json','r')
json_file_locations = json.load(json_metadata_file)['file_locations']

# Open our metadata file to go through all the EVNT samples we've gathered metadata for
input_md = {}
with open('metadata.csv','r') as metadata_csv_file:
    # Open the metadata as a formatted dictionary
    md_reader = csv.DictReader(metadata_csv_file, delimiter=',',quotechar='"',lineterminator='\n') #quoting=csv.QUOTE_ALL,lineterminator='\n')
    # Loop through all the rows in the file (header skipped automatically for DictReader)
    for row in md_reader:
        my_dsid = row['dataset_number']
        input_md[my_dsid] = { x:row[x] for x in row if x!='dataset_number' }

# Final MD with file listings
full_md = {}
# For each row, we're going to extend and then copy over the MD
for aset in input_md:
    # Start by listing out all the skims
    full_md[aset]={'skims':[]}
    # No skim goes into the regular file list field
    full_md[aset]['file_list'] = [ json_file_locations['opendata:opendata.ODEO_FEB2025_noskim_MC_v0'][afile]['uri'] for afile in json_file_locations['opendata:opendata.ODEO_FEB2025_noskim_MC_v0'] if f'mc_{aset}' in afile ]
    # Now go through each skim, add the files and publish the metadata
    for askim in ['2J2LMET30', '1LMET30', '3J1LMET30', 'exactly4lep', '2muons',
                  '2to4lep', '4lep', 'exactly3lep', 'GamGam', '3lep']:
        full_md[aset]['skims'] += [ {'skim_type':askim,
                                     'file_list':[json_file_locations[f'opendata:opendata.ODEO_FEB2025_{askim}_MC_v0'][afile]['uri'] for afile in json_file_locations[f'opendata:opendata.ODEO_FEB2025_{askim}_MC_v0'] if f'mc_{aset}' in afile ]} ]
    # Special handling for the different naming
    for askim in ['2bjets']:
        full_md[aset]['skims'] += [ {'skim_type':askim,
                                     'file_list':[json_file_locations[f'opendata:opendata.ODEO_FEB2025_{askim}_mc_v1'][afile]['uri'] for afile in json_file_locations[f'opendata:opendata.ODEO_FEB2025_{askim}_mc_v1'] if f'mc_{aset}' in afile ]} ]

    full_md[aset].update(input_md[aset])
# Write out the file
with open(f'mc_database_metadata_2025e.json','w') as metadata_json_file:
    json.dump(
        full_md,
        metadata_json_file,
        indent=2,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ": "),
    )

# Reformat and then write the data metadata to a file
data_metadata={'data':{'skims':[],'file_list':[]}}
data_metadata['data']['file_list'] = [ json_file_locations['opendata:opendata.ODEO_FEB2025_noskim_Data_v0'][x]['uri'] for x in json_file_locations['opendata:opendata.ODEO_FEB2025_noskim_Data_v0'] ]
for askim in ['2J2LMET30', '1LMET30', '3J1LMET30', 'exactly4lep', '2muons',
              '2to4lep', '4lep', 'exactly3lep', 'GamGam', '3lep']:
    data_metadata['data']['skims'] += [ {'skim_type':askim,
                                         'file_list':[ json_file_locations[f'opendata:opendata.ODEO_FEB2025_{askim}_Data_v0'][x]['uri'] for x in json_file_locations[f'opendata:opendata.ODEO_FEB2025_{askim}_Data_v0'] ]} ]
# Special handling for the different naming
for askim in ['2bjets']:
    data_metadata['data']['skims'] += [ {'skim_type':askim,
                                         'file_list':[ json_file_locations[f'opendata:opendata.ODEO_FEB2025_{askim}_data_v1'][x]['uri'] for x in json_file_locations[f'opendata:opendata.ODEO_FEB2025_{askim}_data_v1'] ]} ]
with open(f'data_database_metadata_2025e.json','w') as data_metadata_json_file:
    json.dump(
        data_metadata,
        data_metadata_json_file,
        indent=2,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ": "),
    )
