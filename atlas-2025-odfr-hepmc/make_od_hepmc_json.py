#!/usr/bin/env python3

output_directory = 'test'
import os
try:
    os.mkdir(output_directory)
except:
    pass

'''
This creates json files for the Open Data Portal with one record per dataset ID for HEPMC data.
We have a _very short_ description for each of the pages, linking to the main documentation
and explaining in a few sentences what that particular record represents. Each record has a DOI,
and we create a `meta record' containing links to all pages that summarizes the full release of
Event Generator Open Data from ATLAS
'''

# For working with the metadata records
import json

# For making deep copies of the evergreen data, since we want to change some things
import copy

# Get the record map with names and keywords
with open( 'od_hepmc_sample_map.json' , 'r' ) as metadata_map_file:
    record_map = json.load( metadata_map_file )['sample_dict']

# Load the existing list of dictionaries
# Each dictionary has a doi and a recid
# We assign a record to it in the dictionary
# The original is from
# https://github.com/cernopendata/opendata.cern.ch/pull/3737
with open('doi_recid_assignment.json','r') as f:
    doirecid_list = json.load(f)

# recid doi pairs. We will need _lots_ of these eventually
def get_recid_doi_pair(name_short):
    global doirecid_list
    # Search our global list of dictionaries of dois and record ids
    for doirecid in doirecid_list:
        # If we have a match and used this one, give it back
        if 'name_short' in doirecid and doirecid['name_short']==name_short:
            return (doirecid['recid'],doirecid['doi'])
        # If we have used this one, don't re-use it
        elif 'name_short' in doirecid:
            continue
        # If we have never used this one, then assign it
        else:
            doirecid['name_short'] = name_short
            return (doirecid['recid'],doirecid['doi'])
    print(f'ERROR: ran out of DOIs / Record IDs! None for {name_short} found')
    raise RuntimeError('No more DOI/Record IDs')

# Prepare the records to get lists of HEPMC datasets
for a_record in record_map:
    record_map[a_record]['hepmc13'] = []
    record_map[a_record]['hepmc13p6'] = []

# Get datasets that will correspond to each record. Because the lists we have are EVNT, this is
# where we will do the mapping from EVNT to HEPMC.
def match_EVNT_HEPMC(evnt,hepmc):
    # Check for a DID match
    if evnt.split('.')[1]!=hepmc.split('.')[1]:
        return False
    # Check for an e-tag match
    if evnt.split('.')[-1]!=hepmc.split('.')[-1].split('_')[0]:
        return False
    # Check for a center of mass energy match
    if evnt.split('_')[1].split('.')[0]!=hepmc.split('_')[1].split('.')[0]:
        return False
    # Otherwise we're good
    return True

# Add the files to the records. Under normal circumstances there are about the same number of
# files being added as there are files in the lists, so the order of the loop doesn't matter
dataset_files = {}
with open('HEPMC_datasets.txt','r') as dslist:
    # All the HEPMC datasets we located
    for aline in dslist:
        found = False
        # All the Open Data Portal Records we want to build
        for a_record in record_map:
            # All the samples for this Open Data Portal Record
            for a_sample in record_map[a_record]['samples']:
                # If we have a match, keep it!
                if match_EVNT_HEPMC(a_sample.strip(),aline.strip()):
                    if '13p6TeV' in aline:
                        record_map[a_record]['hepmc13p6'] += [ aline.strip() ]
                    else:
                        record_map[a_record]['hepmc13'] += [ aline.strip() ]
                    found = True
                    break
            # Matches should be unique; no need to keep looking if we found a match
            if found:
                break

# Now create the real records for anything that has samples attached
records_to_build = []
for a_record in record_map:
    if len(record_map[a_record]['hepmc13p6'])>0:
        this_record = {'name':a_record+' 13.6 TeV','name_short':'13p6tev-'+a_record.lower().replace(' ','-')}
        this_record['description'] = a_record+' samples at sqrt(s)=13.6 TeV'
        rec_doi = get_recid_doi_pair(this_record['name_short'])
        this_record['recid'] = rec_doi[0]
        this_record['doi'] = rec_doi[1]
        this_record['categories'] = {'source':'ATLAS Collaboration','primary':record_map[a_record]['keywords'][0]}
        if len(record_map[a_record]['keywords'])>1:
            this_record['categories']['secondary']=record_map[a_record]['keywords'][1:]
        this_record['date_created'] = ['2022','2023','2024','2025','2026']
        this_record['run_period'] = ['2022','2023','2024','2025','2026']
        this_record['hepmc'] = record_map[a_record]['hepmc13p6']
        records_to_build += [this_record]
    elif len(record_map[a_record]['hepmc13'])>0:
        this_record = {'name':a_record+' 13 TeV','name_short':'13tev-'+a_record.lower().replace(' ','-')}
        this_record['description'] = a_record+' samples at sqrt(s)=13 TeV'
        rec_doi = get_recid_doi_pair(this_record['name_short'])
        this_record['recid'] = rec_doi[0]
        this_record['doi'] = rec_doi[1]
        this_record['categories'] = {'source':'ATLAS Collaboration','primary':record_map[a_record]['keywords'][0]}
        if len(record_map[a_record]['keywords'])>1:
            this_record['categories']['secondary']=record_map[a_record]['keywords'][1:]
        this_record['date_created'] = ['2015','2016','2017','2018']
        this_record['run_period'] = ['2015','2016','2017','2018']
        this_record['hepmc'] = record_map[a_record]['hepmc13']
        records_to_build += [this_record]
    else:
        print(f'Skipping record {a_record} because no HEPMC files were found')
print(f'Will construct {len(records_to_build)} of {len(record_map)*2} possible records')

# Populate fields
# This is applicable for the pp data only!
evergreen_data = {
    # Accelerator - just CERN LHC
    "accelerator": "CERN-LHC",
    # ATLAS Collaboration; recid only if we need a specific author list
    "collaboration": {
      "name": "ATLAS collaboration",
     },
    # Basic collision data - this applies only to the pp data
    "collision_information": {
      "type": "pp"
    },
    # Collection information is static because this is all HEPMC
    "collections": ["ATLAS-Simulated-Datasets"],
    # Published this year!
    "date_published": "2025",
    # ATLAS experiment
    "experiment": [
      "ATLAS"
    ],
    # Thanks to the Open Data Portal
    "publisher": "CERN Open Data Portal",
    # Note: beginning of the reprocessing
    "date_reprocessed": "2025",
    "distribution": {
      "formats": [
        "HEPMC"
      ],
    },
    # Dataset type information for Open Data Portal
    "type": {
      "primary": "Dataset",
      "secondary": ["Simulated"]
    },
    # Information about usage
    "usage": {
      "description": "<p> The event generation output provided by the ATLAS experiment in HEPMC format is released under a CC0 license; citation of the data and acknowledgement of the collaboration is requested. This format can be used in simple analysis scripts (it is text-based) or as input to various phenomenological tools. <p>Extensive instructions for interacting with the data, as well as documentation of the dataset naming conventions and their contents, are provided on the ATLAS Open Data website linked below. If any problems are identified with the data, please contact the team through the website below. Please be sure to cite the Open Data that you use, in line with the policy below.",
      "links": [
        {
          "description": "ATLAS Open Data Website",
          "url": "http://opendata.atlas.cern"
        },
        {
          "description": "Resources to understand and use the event generation open data",
          "url": "https://opendata.atlas.cern/docs/data/for_research/evgen_data"
        },
        {
          "description": "More about the HEPMC format",
          "url": "https://github.com/alisw/hepmc/tree/master"
        },
        {
          "description": "Citation policy",
          "url": "https://opendata.atlas.cern/docs/documentation/ethical_legal/citation_policy"
        },
      ]
    },
    # Information about (production) methodology
    'methodology': {
      'description':'<p>These data were created over the years from the start of Run 2 up to today. Event generation is run continuously by the experiment, with new samples replacing old on a regular basis as improved configurations are identified and new generator versions become available. All data were reprocessed using Athena Release 25 to create HEPMC files from the ROOT-based EVNT format used internally in the collaboration.'
    },
    "license": {
      "attribution": "CC0-1.0"
    }
}

# File with the mapping of file names for each dataset - merge all the metadata files we have
import glob
json_file_locations = {}
for md_file in glob.glob('od_hepmc_file_mapping*.json'):
    json_metadata_file = open(md_file,'r')
    json_file_locations.update( json.load(json_metadata_file)['file_locations'] )

# Sums for use later on
big_total_files13 = 0
big_total_events13 = 0
big_total_size13 = 0
big_total_files13p6 = 0
big_total_events13p6 = 0
big_total_size13p6 = 0

# Relationships for the files
doirec_13 = get_recid_doi_pair('atlas-hepmc-13tev-summary')
relation_13TeV = [ {'description':'For citing all the 13 TeV HEPMC data, and to find other related datasets, please see',
                            'doi':doirec_13[0],
                          'recid':doirec_13[1],
                          'title':'HEPMC format 13 TeV proton-proton Open Data from the ATLAS experiment',
                           'type':'isChildOf'
                             } ]
doirec_13p6 = get_recid_doi_pair('atlas-hepmc-13p6tev-summary')
relation_13p6TeV = [ {'description':'For citing all the 13.6 TeV HEPMC data, and to find other related datasets, please see',
                              'doi':doirec_13p6[0],
                            'recid':doirec_13p6[1],
                            'title':'HEPMC format 13.6 TeV proton-proton Open Data from the ATLAS experiment',
                             'type':'isChildOf'
                             } ]

created_records = {}

# Now loop through all the datasets that we are going to publish
for a_record in records_to_build:
    # Start from the stuff that's always good
    my_json = copy.deepcopy(evergreen_data)
    # Simple abstract for the collection
    my_json['abstract'] = {'description':a_record['description']+' from the ATLAS experiment. This record collects related samples. Some care is required when combining samples in order to ensure a complete physics representation without overlaps or omissions; please read the documentation of the open data, linked below, carefully.'}
    # Add a link to the top-level record where everything is linked together
    if '13 TeV' in a_record['name']:
        my_json['relations'] = relation_13TeV
        my_json['collision_information']['energy'] = '13TeV'
        energy_stub = '13tev'
    elif '13.6 TeV' in a_record['name']:
        my_json['relations'] = relation_13p6TeV
        my_json['collision_information']['energy'] = '13.6TeV'
        energy_stub = '13p6tev'
    else:
        print(f'Could not identify com energy for dataset {a_record}')
    # Add categories, mostly for MC datasets
    my_json['categories'] = a_record['categories']
    my_json['title'] = 'ATLAS HEPMC format '+a_record['name']
    # Add a record ID for CERN Open Data. Reserved range for this release
    my_json['recid'] = a_record['recid']
    # Add the DOI - these are pre-reserved by the Open Data Portal team
    my_json['doi'] = a_record['doi']
    # Add the other collision information we set up in advance based on c.o.m. Energy
    my_json['date_created'] = a_record['date_created']
    my_json['run_period'] = a_record['run_period']
    # Add a record of the files for this dataset
    my_json['files'] = []
    # Counters to be used in updating the metadata for the overall record
    total_files = 0
    total_events = 0
    total_size = 0
    created_records[ a_record['name_short'] ] = []
    # Make a json file with the files for this dataset
    for a_hepmc in a_record['hepmc']:
        # Establish the file name for this list of HEPMC files
        my_did = a_hepmc.split('.')[1]
        my_short = a_hepmc.split('.')[2]
        filename = 'MC_'+my_did+'_'+energy_stub+'_'+my_short+'_hepmc_filelist.json'
        # Create the list of files for this HEPMC sample
        my_files = []
        if a_hepmc not in json_file_locations:
            print(f'Warning: did not find {a_hepmc} in JSON file locations')
            continue
        for a_file in json_file_locations[a_hepmc]:
            my_files += [ { 'filename':a_file.split(':')[1] if ':' in a_file else a_file,
                            'checksum':json_file_locations[a_hepmc][a_file]['checksum'],
                            'size':json_file_locations[a_hepmc][a_file]['size'],
                            'events':json_file_locations[a_hepmc][a_file]['events'],
                            'type':json_file_locations[a_hepmc][a_file]['type'],
                            # We don't need the special port for eospublic access, despite what rucio tells us
                            'uri_root':json_file_locations[a_hepmc][a_file]['uri'].replace('eospublic.cern.ch:1094','eospublic.cern.ch') } ]
            total_files += 1
            total_events += int(json_file_locations[a_hepmc][a_file]['events'])
            total_size += int(json_file_locations[a_hepmc][a_file]['size'])
        if len(my_files)==0:
            print(f'Warning: no files identified for sample {a_hepmc}')
            continue

        # Set the metadata in the `super` (open data portal record) json
        my_json['files'] += [ { 'filename':filename } ]
        # Now open that file and write the file names there
        with open(output_directory+'/'+filename,'w') as dataset_filelist_file:
            json.dump( my_files ,
                       dataset_filelist_file,
                       indent=2,
                       sort_keys=True,
                       ensure_ascii=False,
                       separators=(",", ": "),
                     )
        # Extra book-keeping
        created_records[ a_record['name_short'] ] += [ a_hepmc ]
    # Add the file and event sums to the top-level record
    my_json['distribution']['number_events'] = total_events
    my_json['distribution']['number_files'] = total_files
    my_json['distribution']['size'] = total_size
    # Counters to be used in updating the metadata for the overall record
    if '13 TeV' in a_record['name']:
        big_total_events13 += total_events
        big_total_files13 += total_files
        big_total_size13 += total_size
    elif '13.6 TeV' in a_record['name']:
        big_total_events13p6 += total_events
        big_total_files13p6 += total_files
        big_total_size13p6 += total_size
    # Write myself a json file
    summary_file_name = 'atlas-hepmc-'+a_record['name_short']+'.json'
    with open(output_directory+'/'+summary_file_name,'w') as outfile:
        json.dump(
            [ my_json ],
            outfile,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ": "),
        )

# Add the top-level json files - 13 TeV first - only if we have some data
if big_total_files13>0:
    my_json = {}
    # Update with the stuff that's always good
    my_json.update(evergreen_data)
    # Simple abstract for the collection
    my_json['abstract'] = {'description':'HEPMC format 13 TeV proton-proton Open Data from the ATLAS experiment'}
    # Name of the collections, systematically set
    my_json['collections'] = ['ATLAS-Simulated-Datasets']
    my_json['type']['secondary'] = ['Simulated']
    # Add categories, mostly for MC datasets
    my_json['categories'] = {'source':'ATLAS Collaboration'}
    my_json['title'] = 'HEPMC format 13 TeV proton-proton Open Data from the ATLAS experiment'
    # Collision information for 13 TeV data
    my_json['collision_information']['energy'] = '13TeV'
    my_json['date_created'] = ['2015','2016','2017','2018']
    my_json['run_period'] = ['2015','2016','2017','2018']
    # Add a record ID for CERN Open Data. Reserved range for this release
    my_json['recid'] = doirec_13[0]
    # Add the DOI - these are pre-reserved by the Open Data Portal team
    my_json['doi'] = doirec_13[1]
    # Add the file and event sums to the top-level record
    my_json['distribution']['number_events'] = big_total_events13
    my_json['distribution']['number_files'] = big_total_files13
    my_json['distribution']['size'] = big_total_size13
    # Link to the other datasets
    my_json['relations'] = []
    for adataset in dataset_files:
        if '13 TeV' in dataset_files[adataset]['name']:
            my_json['relations'] += [ {'description':dataset_files[adataset]['name'],
                                       'doi':dataset_files[adataset]['doi'],
                                       'recid':dataset_files[adataset]['recid'],
                                       'title':dataset_files[adataset]['name'],
                                       'type':'isParentOf'
                                      } ]
    # Write myself a json file
    summary_file_name = 'atlas-hepmc-13tev-summary.json'
    with open(output_directory+'/'+summary_file_name,'w') as outfile:
        json.dump(
            [ my_json ],
            outfile,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ": "),
        )
    # Extra book-keeping
    created_records[ 'Summary_13TeV' ] = []
else:
    print('No 13 TeV samples identified')

# Now the same for the 13.6 TeV HEPMC
if big_total_files13p6>0:
    my_json = {}
    # Update with the stuff that's always good
    my_json.update(evergreen_data)
    # Simple abstract for the collection
    my_json['abstract'] = {'description':'HEPMC format 13.6 TeV proton-proton Open Data from the ATLAS experiment'}
    # Name of the collections, systematically set
    my_json['collections'] = ['ATLAS-Simulated-Datasets']
    my_json['type']['secondary'] = ['Simulated']
    # Add categories, mostly for MC datasets
    my_json['categories'] = {'source':'ATLAS Collaboration'}
    my_json['title'] = 'HEPMC format 13.6 TeV proton-proton Open Data from the ATLAS experiment'
    # Collision information for 13.6 TeV data
    my_json['collision_information']['energy'] = '13.6TeV'
    my_json['date_created'] = ['2022','2023','2024','2025','2026']
    my_json['run_period'] = ['2022','2023','2024','2025','2026']
    # Add a record ID for CERN Open Data. Reserved range for this release
    my_json['recid'] = doirec_13p6[0]
    # Add the DOI - these are pre-reserved by the Open Data Portal team
    my_json['doi'] = doirec_13p6[1]
    # Add the file and event sums to the top-level record
    my_json['distribution']['number_events'] = big_total_events13p6
    my_json['distribution']['number_files'] = big_total_files13p6
    my_json['distribution']['size'] = big_total_size13p6
    # Link to the other datasets
    my_json['relations'] = []
    for adataset in dataset_files:
        if '13.6 TeV' in dataset_files[adataset]['name']:
            my_json['relations'] += [ {'description':dataset_files[adataset]['name'],
                                       'doi':dataset_files[adataset]['doi'],
                                       'recid':dataset_files[adataset]['recid'],
                                       'title':dataset_files[adataset]['name'],
                                       'type':'isParentOf'
                                      } ]
    # Write myself a json file
    summary_file_name = 'atlas-hepmc-13p6tev-summary.json'
    with open(output_directory+'/'+summary_file_name,'w') as outfile:
        json.dump(
            [ my_json ],
            outfile,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ": "),
        )
    # Extra book-keeping
    created_records[ 'Summary_13TeV' ] = []
else:
    print('No 13.6 TeV samples identified')

# Final check against previously created records
# Get the last run results from the json file, protecting for bad runs
last_records = {}
if os.access('last_record_creation.json',os.R_OK):
    with open('last_record_creation.json','r') as last_record_file:
        last_records_data = json.load(last_record_file)
        if 'records' in last_records_data:
            last_records = last_records_data['records']
# Go through the two and compare and contrast
difference = False
for a_rec in last_records:
    if a_rec not in created_records:
        print(f'Error: {a_rec} had previously been created but was not this round. Something is wrong!')
        difference = True
for a_rec in created_records:
    if a_rec not in last_records:
        print(f'Created new record {a_rec} with samples {created_records[a_rec]}')
        difference = True
    elif sorted(last_records[a_rec])!=sorted(created_records[a_rec]):
        if len(last_records[a_rec])>len(created_records[a_rec]):
            print(f'Error: {a_rec} previously had {len(last_records[a_rec])-len(created_records[a_rec])} more files than it has now.')
        elif len(last_records[a_rec])<len(created_records[a_rec]):
            print(f'Update: {a_rec} had {len(created_records[a_rec])-len(last_records[a_rec])} files added to it.')
        print(f'  Files in old and not new: {[ x for x in last_records[a_rec] if x not in created_records[a_rec] ]}')
        print(f'  Files in new and not old: {[ x for x in created_records[a_rec] if x not in last_records[a_rec] ]}')
        difference = True
if not difference:
    print('No changes with respect to previous deployment were identified')

# And now write what we did to the record of the last run
with open('last_record_creation.json','w') as outfile:
    json.dump(
        {'records':created_records},
        outfile,
        indent=2,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ": "),
    )

# Finally, record a new DOI + Record ID list
with open('doi_recid_assignment.json','w') as f:
    json.dump( obj=doirecid_list, fp=f )
