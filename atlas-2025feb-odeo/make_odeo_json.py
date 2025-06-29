#!/usr/bin/env python3

output_directory = 'test'
import os
try:
    os.mkdir(output_directory)
except:
    pass

'''
This creates json files for the Open Data Portal with:

-) One record per skim of detector data
	- One file per period
-) One record per skim of the MC
	- One file per DSID / MC simulation configuration

We have a _very short_ description for each of the pages, linking to the main documentation
and explaining in a few sentences what that particular record represents. Each record has a DOI,
and we create a `meta record' containing links to all pages that summarizes the full release of
Open Data for Education and Outreach.
'''

# For working with the metadata records
import json

# For making deep copies of the evergreen data, since we want to change some things
import copy

# Need new recids and DOIs

# Map of skim names into pretty-print descriptions
skim_name_map = {
    '1LMET30':'At least one lepton with at least 7 GeV of p<sub>T</sub> and 30 GeV of missing transverse momentum (i.e. a leptonically-decaying W-boson enhanced selection)',
    '2to4lep':'Two to four leptons with at least 7 GeV of p<sub>T</sub> each',
    '2muons':'At least two muons with at least 10 GeV of p<sub>T</sub> (i.e. a leptonically-decaying Z-boson enhanced selection)',
    '3J1LMET30':'At least three jets with at least 20 GeV of p<sub>T</sub>, at least one lepton passing tight identification requirements with at least 7 GeV of p<sub>T</sub>, and 30 GeV of missing transverse momentum (i.e. a semi-leptonic top-quark enhanced selection)',
    'GamGam':'At least two photons with at least 25 GeV of p<sub>T</sub> each (i.e. a Higgs boson decaying to two photons enhanced selection)',
    '2J2LMET30':'At least two jets with at least 20 GeV of p<sub>T</sub>, at least two leptons passing tight identification requirements with at least 7 GeV of p<sub>T</sub>, and 30 GeV of missing transverse momentum (i.e. a di-leptonic top-quark enhanced selection)',
    '2bjets':'At least two jets with at least 20 GeV of p<sub>T</sub> identified as containing at least one heavy flavor hadron using the 85% working point (i.e. a Higgs boson decaying to b-quarks enhanced selection)',
    '3lep':'At least three leptons with at least 7 GeV of p<sub>T</sub> each',
    'exactly3lep':'Exactly three leptons with at least 7 GeV of p<sub>T</sub> (i.e. a leptonically-decaying W+Z boson enhanced selection)',
    '4lep':'At least four leptons with at least 7 GeV of p<sub>T</sub> each',
    'exactly4lep':'Exactly four leptons with at least 7 GeV of p<sub>T</sub> (i.e. a leptonically-decaying ZZ boson or Higgs to four leptons enhanced selection)',
    'noskim':'none.'
  }

# recid doi
recid_doi_pairs = [
('93911', '10.7483/OPENDATA.ATLAS.ZPCQ.9VO2'),
('93912', '10.7483/OPENDATA.ATLAS.CMHX.9D8M'),
('93913', '10.7483/OPENDATA.ATLAS.NNF8.76IX'),
('93914', '10.7483/OPENDATA.ATLAS.SCWS.LYYX'),
('93915', '10.7483/OPENDATA.ATLAS.GYRR.GRP3'),
('93916', '10.7483/OPENDATA.ATLAS.IBFR.R9L3'),
('93917', '10.7483/OPENDATA.ATLAS.L5QV.U2XC'),
('93918', '10.7483/OPENDATA.ATLAS.7UW9.C9LL'),
('93919', '10.7483/OPENDATA.ATLAS.ZXYW.FXJO'),
('93920', '10.7483/OPENDATA.ATLAS.71IP.L3OC'),
('93921', '10.7483/OPENDATA.ATLAS.6VGH.HN41'),
('93922', '10.7483/OPENDATA.ATLAS.IMZO.7U52'),
('93923', '10.7483/OPENDATA.ATLAS.OMF2.CICK'),
('93924', '10.7483/OPENDATA.ATLAS.3ATL.Q9Z2'),
('93925', '10.7483/OPENDATA.ATLAS.211Z.76E7'),
('93926', '10.7483/OPENDATA.ATLAS.CIU5.U5YX'),
('93927', '10.7483/OPENDATA.ATLAS.1P1H.J3QK'),
('93928', '10.7483/OPENDATA.ATLAS.XNPI.CX93'),
('93929', '10.7483/OPENDATA.ATLAS.KPYL.P0EE'),
('93930', '10.7483/OPENDATA.ATLAS.AR66.6RTA'),
('93931', '10.7483/OPENDATA.ATLAS.9VTD.OT28'),
('93932', '10.7483/OPENDATA.ATLAS.IPG4.6M6X'),
('93933', '10.7483/OPENDATA.ATLAS.VV3I.0WJE'),
('93934', '10.7483/OPENDATA.ATLAS.0CJR.N7ZT'),
      ]

# Get datasets
dataset_files = {}
with open('dataset_list.txt','r') as dslist:
    for aline in dslist:
        # Account for commented out lines
        if len(aline.split('#')[0].strip())==0:
            continue
        skim = aline.split('_')[2]
        if skim=='noskim':
            skim = 'no' # Fun little hack to fix the English...
        name_short = '-'.join(aline.split('_')[2:4]).lower()
        if '_data' in aline.lower():
            name = f'Run 2 2015+2016 proton-proton collision data beta release, {skim} skim'
        else:
            name = f'MC simulation, 2015+2016 proton-proton collisions beta release, {skim} skim'
        rec_doi = recid_doi_pairs.pop()
        dataset_files[ aline.strip() ] = {'name_short':name_short, 'name':name,
                                          'categories':{'source':'ATLAS Collaboration'},'doi':rec_doi[1],'recid':rec_doi[0]}

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
      "energy": "13TeV",
      "type": "pp"
    },
    # Published this year!
    "date_published": "2025",
    # ATLAS experiment
    "experiment": [
      "ATLAS"
    ],
    # Thanks to the Open Data Portal
    "publisher": "CERN Open Data Portal",
    # data-taking year during which the collision data or for which the simulated data, software and other assets were produced
    "date_created": ['2015','2016'],
    "run_period": ['2015','2016'],
    # Note: beginning of the reprocessing
    "date_reprocessed": "2020",
    "distribution": {
      "formats": [
        "root"
      ],
    },
    # Dataset type information for Open Data Portal
    "type": {
      "primary": "Dataset",
    },
    # Information about usage
    "usage": {
      "description": "<p> The data and MC simulation provided by the ATLAS experiment in root ntuple format is released under a CC0 license; citation of the data and acknowledgement of the collaboration is requested. This format can be used directly using ROOT or uproot for simple studies and is primarily intended for educational and outreach purposes. <p>Extensive instructions for interacting with the data, as well as documentation of the dataset naming conventions and their contents, are provided on the ATLAS Open Data website linked below. For those interested in implementing a research-quality data analysis, the open data designed for research (also linked below) may be a better starting point. Please be sure to cite the Open Data that you use, in line with the policy below.",
      "links": [
        {
          "description": "ATLAS Open Data Website",
          "url": "http://opendata.atlas.cern"
        },
        {
          "description": "Resources to understand and use the open data for education and outreach",
          "url": "https://opendata.atlas.cern/docs/category/13-tev-2025-beta-release"
        },
        {
          "description": "More about this ntuple format",
          "url": "https://opendata.atlas.cern/docs/data/for_education/13TeV25_details#variable-list"
        },
        {
          "description": "Ntuple making framework (PhysLiteToOpenData)",
          "url": "https://doi.org/10.5281/zenodo.15791091"
        },
        {
          "description": "Citation policy",
          "url": "https://opendata.atlas.cern/docs/documentation/ethical_legal/citation_policy"
        },
      ]
    },
    # Information about (production) methodology
    'methodology': {
      'description':'<p>These data were created during LS2 as part of a major reprocessing campaign of the Run 2 data. All data were reprocessed using Athena Release 22, and new corresponding MC simulation samples were produced. These data and MC simulation datasets were processed into ROOT ntuple files from the DAOD_PHYSLITE format that is released as open data for research. For the files in this record, the following skimming selection was applied: '
    },
    "license": {
      "attribution": "CC0-1.0"
    }
}

# File with the mapping of file names for each dataset
json_metadata_file = open('odeo_file_mapping_ODEO_v0_FEB2025_2025-06-30.json','r')
json_file_locations = json.load(json_metadata_file)['file_locations']

# Sums for use later on
big_total_files = 0
big_total_events = 0
big_total_size = 0

# Now loop through all the datasets that we are going to publish
for adataset in dataset_files:
    # Start from the stuff that's always good
    my_json = copy.deepcopy(evergreen_data)
    # Simple abstract for the collection
    my_json['abstract'] = {'description':dataset_files[adataset]['name']+' from the ATLAS experiment'}
    # Name of the collections, systematically set
    my_json['collections'] = ['ATLAS-Simulated-Datasets' if 'mc_' in adataset else 'ATLAS-Primary-Datasets']
    if '_data' in adataset.lower():
        my_json['type']['secondary'] = ['Collision']
    else:
        my_json['type']['secondary'] = ['Simulated']
    # Add categories, mostly for MC datasets
    my_json['categories'] = dataset_files[adataset]['categories']
    my_json['title'] = 'ATLAS ROOT ntuple format '+dataset_files[adataset]['name']
    # Add a record ID for CERN Open Data. Reserved range for this release
    my_json['recid'] = dataset_files[adataset]['recid']
    # Add the DOI - these are pre-reserved by the Open Data Portal team
    my_json['doi'] = dataset_files[adataset]['doi']
    # Update the methodology section with the skim description
    skim = adataset.split('_')[2]
    my_json['methodology']['description'] = evergreen_data['methodology']['description']+skim_name_map[skim]
    # Add a record of the files for this dataset
    my_json['files'] = []
    # Make list of files for this dataset
    # For direct upload, only the size, checksum, and uri_root are needed; see https://github.com/cernopendata/data-curation/pull/258#issuecomment-2747547600
    my_json['files'] = [ {#'filename':afile,
                          # Bug in the metadata creation script, no ':' after adler32; patching here to skip metadata recreation
                          'checksum':json_file_locations[adataset][afile]['checksum'],
                          'size':json_file_locations[adataset][afile]['size'],
                          #'events':json_file_locations[adataset][afile]['events'],
                          #'type':json_file_locations[adataset][afile]['type'],
                          # We don't need the special port for eospublic access, despite what rucio tells us
                          'uri':json_file_locations[adataset][afile]['uri'].replace('eospublic.cern.ch:1094','eospublic.cern.ch') } for afile in json_file_locations[adataset] ]
    # Counters to be used in updating the metadata for the overall record
    total_files = len(my_json['files'])
    total_events = sum( [ int(json_file_locations[adataset][afile]['events']) for afile in json_file_locations[adataset] ] )
    total_size = sum( [ int(x['size']) for x in my_json['files'] ] )
    # Add the file and event sums to the top-level record
    my_json['distribution']['number_events'] = total_events
    my_json['distribution']['number_files'] = total_files
    my_json['distribution']['size'] = total_size
    # Update the running sums
    big_total_events += total_events
    big_total_files += total_files
    big_total_size += total_size
    # Link to the top-level record
    my_json['relations'] = [ {'description':'For citing all the Open Data for Education and Outreach from this release, and to find other related datasets, please see',
                              'doi':'10.7483/OPENDATA.ATLAS.B5M9.44TN',
                              'recid':'93910',
                              'title':'ROOT ntuple format 2015-2016 proton-proton Open Data for Education and Outreach from the ATLAS experiment',
                              'type':'isChildOf'
                             } ]
    # Write myself a json file
    summary_file_name = 'atlas-odeo-FEB2025-'+dataset_files[adataset]['name_short']+'.json'
    with open(output_directory+'/'+summary_file_name,'w') as outfile:
        json.dump(
            [ my_json ],
            outfile,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ": "),
        )

# Add the top-level json file
my_json = {}
# Update with the stuff that's always good
my_json.update(evergreen_data)
# Simple abstract for the collection
my_json['abstract'] = {'description':'Run 2 2015+2016 proton-proton collision data and corresponding MC simulation Open Data for Education and Outreach from the ATLAS experiment'}
# Name of the collections, systematically set
my_json['collections'] = ['ATLAS-Simulated-Datasets','ATLAS-Primary-Datasets']
my_json['type']['secondary'] = ['Simulated','Collision']
# Description needs a simple update
my_json['methodology']['description'] = evergreen_data['methodology']['description'].replace('the following skimming selection was applied: ','several event pre-selections are available to accelerate analysis, as well as an inclusive set of all events.')
# Add categories, mostly for MC datasets
my_json['categories'] = {'source':'ATLAS Collaboration'}
my_json['title'] = 'ROOT ntuple format 2015-2016 proton-proton Open Data for Education and Outreach beta release from the ATLAS experiment'
# Add a record ID for CERN Open Data. Reserved range for this release
my_json['recid'] = '93910'
# Add the DOI - these are pre-reserved by the Open Data Portal team
my_json['doi'] = '10.7483/OPENDATA.ATLAS.B5M9.44TN'
# Add the file and event sums to the top-level record
my_json['distribution']['number_events'] = big_total_events
my_json['distribution']['number_files'] = big_total_files
my_json['distribution']['size'] = big_total_size
# Link to the other datasets
my_json['relations'] = []
for adataset in dataset_files:
    my_json['relations'] += [ {'description':dataset_files[adataset]['name'],
                               'doi':dataset_files[adataset]['doi'],
                               'recid':dataset_files[adataset]['recid'],
                               'title':dataset_files[adataset]['name'],
                               'type':'isParentOf'
                              } ]

# Write myself a json file
summary_file_name = 'atlas-odeo-FEB2025-summary.json'
with open(output_directory+'/'+summary_file_name,'w') as outfile:
    json.dump(
        [ my_json ],
        outfile,
        indent=2,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ": "),
    )
