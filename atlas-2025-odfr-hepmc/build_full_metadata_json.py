#!/usr/bin/env python3

# Simple script to convert csv metadata file into a full js code file

# For pretty printing and writing json
import json

# For csv reading
import csv

# File with the mapping of file names for each dataset - merge all the metadata files we have
json_file_locations = {}
with open('od_hepmc_file_mapping.json','r') as json_metadata_file:
    json_file_locations.update( json.load(json_metadata_file)['file_locations'] )

no_uris = []

dsid_tot = 0
dsid_wfiles = 0
events = 0
dsid_wfilesCOM = {'13':0,'13p6':0}
eventsCOM = {'13':0,'13p6':0}

# Open our metadata file to go through all the EVNT samples we've gathered metadata for
with open('EVNT_metadata.csv','r') as evgen_metadata_csv_file, open('database_metadata13.json','w') as metadata_json_file13, open('database_metadata13p6.json','w') as metadata_json_file13p6:

    # For each line in the metadata file we're going to compose a final metadata entry
    full_md = {'13':{},'13p6':{}}

    # Open the metadata as a formatted dictionary
    md_reader = csv.DictReader(evgen_metadata_csv_file, delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL,lineterminator='\n')
    # Loop through all the rows in the file (header skipped automatically for DictReader)
    for row in md_reader:
        my_dsid = row['DSID']
        if row['CoMEnergy'] not in ['13000.0','13600.0']:
            print(f'Did not understand CoM Energy: {row["CoMEnergy"]}')
        ci = '13' if row['CoMEnergy']=='13000.0' else '13p6'

        full_md[ci][my_dsid] = { x:row[x] for x in ['CoMEnergy','kFactor','GenEvents','Filters','GenTune','PDF','Release'] }
        # List of files if we have it
        for akey in json_file_locations:
            if akey.split('.')[1]==my_dsid:
                full_md[ci][my_dsid]['file_list'] = [ json_file_locations[akey][x]['uri'] for x in json_file_locations[akey] if 'uri' in json_file_locations[akey][x] ]
                for x in json_file_locations[akey]:
                    if 'uri' not in json_file_locations[akey][x]:
                        if akey not in no_uris: no_uris += [akey]
        # Now a few parts of the metadata that need to be reformated
        full_md[ci][my_dsid]['keywords'] = [ x.strip() for x in row['Keywords'].split(',') ]
        full_md[ci][my_dsid]['job_path'] = row['JobOptions']
        full_md[ci][my_dsid]['genFiltEff'] = row['FiltEff']
        full_md[ci][my_dsid]['nEvents'] = row['Events']
        full_md[ci][my_dsid]['generator'] = row['GenName']
        full_md[ci][my_dsid]['description'] = row['PhysComment']
        full_md[ci][my_dsid]['physics_short'] = row['PhysicsShort']
        full_md[ci][my_dsid]['cross_section_pb'] = row['XSec']
        full_md[ci][my_dsid]['cross_section_uncertainty'] = row['Uncertainty']
        full_md[ci][my_dsid]['hepmc_version'] = row['HEPMC']

        dsid_tot += 1
        if 'file_list' in full_md[ci][my_dsid]:
            dsid_wfiles += 1
            events += int(row['Events'])
            dsid_wfilesCOM[ci] += 1
            eventsCOM[ci] += int(row['Events'])

    json.dump(
        [ full_md['13'] ],
        metadata_json_file13,
        indent=2,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ": "),
    )

    json.dump(
        [ full_md['13p6'] ],
        metadata_json_file13p6,
        indent=2,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ": "),
    )

print('Missing URIs:')
for akey in no_uris: print(akey)

print(f'Releasing {dsid_tot:,} total datasets in the metadata with {dsid_wfiles:,} datasets containing {events:,} events')
print(f'   In the releases, we have {len(full_md["13"])} 13 TeV datasets and {len(full_md["13p6"])} 13.6 TeV datasets')
print(f'   with {dsid_wfilesCOM["13"]} files ({eventsCOM["13"]} events) at 13 TeV and')
print(f'   with {dsid_wfilesCOM["13p6"]} files ({eventsCOM["13p6"]} events) at 13.6 TeV')

