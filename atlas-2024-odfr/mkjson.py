#!/usr/bin/env python3

output_directory = 'test'
import os
try:
    os.mkdir(output_directory)
except:
    pass

'''
Notes on the plan:

-) One record for the 2015 data
	- Structure in the record to represent the individual runs
-) One record for the 2016 data
	- Structure in the record to represent the individual runs
-) One record for each of the "blocks" of MC that we had in the note (https://cds.cern.ch/record/2875752)
	- 9 tables in total for the time being
	- Structure in the record to represent the individual MC datasets

You can see an example of this kind of structure in the "File Indexes" section of this record:
https://opendata.cern.ch/record/24464

I'd then write a draft _very short_ description for each of the 11 pages, linking to the main documentation
and explaining in a few sentences what that particular record represents. We would give each record a DOI,
and we could create a `meta record' containing links to all 11 pages that summarize the full release of Open Data.
'''

import json

# Get datasets
dataset_files = {
  'pp_2015_data_p6026_tids.txt':{'name':'Run 2 2015 proton-proton collision data','recid':'80000','name_short':'pp-2015-data',
              'categories':{'source':'ATLAS Collaboration'}},
  'pp_2016_data_p6026_tids.txt':{'name':'Run 2 2016 proton-proton collision data','recid':'80001','name_short':'pp-2016-data',
              'categories':{'source':'ATLAS Collaboration'}},
  'mc_boson_nominal.txt':{'name':'MC simulation electroweak boson nominal samples','recid':'80010','name_short':'mc-pp-boson-nominal',
              'categories':{'primary':'Standard Model Physics','secondary':['ElectroWeak','Drell-Yan'], 'source':'ATLAS Collaboration'}},
  'mc_exotics_nominal.txt':{'name':'MC simulation exotic signal samples','recid':'80011','name_short':'mc-pp-exotics-nominal',
              'categories':{'primary':'Exotica', 'secondary':['Miscellaneous'], 'source':'ATLAS Collaboration'}},
  'mc_higgs_nominal.txt':{'name':'MC simulation Higgs nominal samples','recid':'80012','name_short':'mc-pp-higgs-nominal',
              'categories':{'primary':'Higgs Physics','secondary':['Standard Model'], 'source':'ATLAS Collaboration'}},
  'mc_higgs_systematics.txt':{'name':'MC simulation Higgs systematic variation samples','recid':'80013','name_short':'mc-pp-higgs-syst',
              'categories':{'primary':'Higgs Physics','secondary':['Standard Model'], 'source':'ATLAS Collaboration'}},
  'mc_jet_nominal.txt':{'name':'MC simulation QCD jet nominal samples','recid':'80014','name_short':'mc-pp-jet-nominal',
              'categories':{'primary':'Standard Model Physics','secondary':['QCD'], 'source':'ATLAS Collaboration'}},
  'mc_jet_systematics.txt':{'name':'MC simulation QCD jet systematic variation samples','recid':'80015','name_short':'mc-pp-jet-syst',
              'categories':{'primary':'Standard Model Physics','secondary':['QCD'], 'source':'ATLAS Collaboration'}},
  'mc_susy_nominal.txt':{'name':'MC simulation SUSY signal samples','recid':'80016','name_short':'mc-pp-susy-nominal',
              'categories':{'primary':'Exotica','secondary':['Miscellaneous'], 'source':'ATLAS Collaboration'}},
  'mc_top_nominal.txt':{'name':'MC simulation top nominal samples','recid':'80017','name_short':'mc-pp-top-nominal',
              'categories':{'primary':'Standard Model Physics','secondary':['Top physics'], 'source':'ATLAS Collaboration'}},
  'mc_top_systematics.txt':{'name':'MC simulation top systematic variation samples','recid':'80018','name_short':'mc-pp-top-syst',
              'categories':{'primary':'Standard Model Physics','secondary':['Top physics'], 'source':'ATLAS Collaboration'}},
    }

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
    "date_published": "2024",
    # ATLAS experiment
    "experiment": [
      "ATLAS"
    ],
    # Thanks to the Open Data Portal
    "publisher": "CERN Open Data Portal",
    # Note: beginning of the reprocessing
    "date_reprocessed": "2020",
    "distribution": {
      "formats": [
        "DAOD_PHYSLITE",
        "ROOT"
      ],
    },
    # Dataset type information for Open Data Portal
    "type": {
      "primary": "Dataset",
    },
    # Information about usage
    "usage": {
      "description": "<p> The data and MC simulation provided by the ATLAS experiment in DAOD_PHYSLITE format is released under a CC0-BY license. This format can be used directly like a ROOT ntuple for simple studies or processed into secondary ntuples with systematic uncertainties included using the ATLAS AnalysisBase software. <p>Extensive instructions for interacting with the data, as well as documentation of the dataset naming conventions and their contents, are provided on the ATLAS Open Data website linked below.",
      "links": [
        {
          "description": "ATLAS Open Data Website",
          "url": "http://opendata.atlas.cern"
        },
        {
          "description": "Citation of ATLAS Open Data",
          "url": "https://opendata.atlas.cern/docs/documentation/ethical_legal/citation_policy"
        },
        {
          "description": "ATLAS Analysis Software Tutorial",
          "url": "https://atlassoftwaredocs.web.cern.ch/ASWTutorial/TutorialWeek/"
        }
      ]
    },
    # Information about (production) methodology
    'methodology': {
      'description':'<p>These data were created during LS2 as part of a major reprocessing campaign of the Run 2 data. All data were reprocessed using Athena Release 22, and new corresponding MC simulation samples were produced, in an MC simulation campaign called MC20a. These data and MC simulation datasets were processed into DAOD_PHSYLITE format files; this is a light-weight data format intended for general analysis use, sufficient to support a wide variety of ATLAS analyses.'},
    "license": {
      "attribution": "CC BY"
    }
}

# File with the mapping of file names for each dataset - merge these together for MC
mc_json_filenames = ['mc_file_mapping_OpenData_v1_p6026_2024-04-23_with_metadata.json',
                     'mc_file_mapping_OpenData_v0_p6026_2024-04-16_with_metadata.json']
mc_json_files = [ open(x,'r') for x in mc_json_filenames ]
mc_json_sets = [ json.load(x) for x in mc_json_files ]
mc_json = None
for json_set in mc_json_sets:
    if mc_json is None:
        mc_json = json_set
        continue
    for akey in mc_json:
        if type(mc_json[akey])==dict: mc_json[akey].update( json_set[akey] )
        elif type(mc_json[akey])==list: mc_json[akey] += json_set[akey]
        else: print(f'Unidentified object {akey} {type(d1[akey])}')

# Only one file for data
data_json_file = open('data_file_mapping_OpenData_v0_p6026_2024-04-15.json','r')
data_json = json.load(data_json_file)

for adataset in dataset_files:
    my_json = {}
    # Update with the stuff that's always good
    my_json.update(evergreen_data)
    # Simple abstract for the collection
    my_json['abstract'] = {'description':dataset_files[adataset]['name']+' from the ATLAS experiment'}
    # Name of the collections, systematically set
    my_json['collections'] = ['ATLAS-Simulated-Datasets' if 'mc_' in adataset else 'ATLAS-Primary-Datasets']
    # data-taking year during which the collision data or for which the simulated data, software and other assets were produced
    if 'data' in adataset:
        my_json['date_created'] = [adataset.split('_')[1]]
        my_json['run_period'] = [adataset.split('_')[1]]
        my_json['type']['secondary'] = ['Collision']
    else:
        my_json['date_created'] = ['2015','2016']
        my_json['run_period'] = ['2015','2016']
        my_json['type']['secondary'] = ['Simulated']
    # Add categories, mostly for MC datasets
    my_json['categories'] = dataset_files[adataset]['categories']
    my_json['title'] = 'ATLAS DAOD_PHYSLITE format '+dataset_files[adataset]['name']
    # Add a record ID for CERN Open Data. Reserved range for this release
    my_json['recid'] = dataset_files[adataset]['recid']
    # Do I need to specify a doi? Should be automatically added, I believe
    # Add a record of the files for this dataset
    my_json['files'] = []
    # Make a json file with the files for this dataset
    with open(adataset,'r') as dataset_list_file:
        for dataset_line in dataset_list_file:
            # Make up the name of the text file we'll use for the dataset based on the input lists
            if 'data' in adataset:
                # This is a simple list of dataset names
                # It is normal to sometimes not find files; this just indicates there was no
                #  good data in that run, and it was still processed
                filename = 'Run_'+dataset_line.split('.')[1].strip()+'_filelist.json'
                if dataset_line.strip() not in data_json['file_locations']:
                    print(f'Did not find data dataset {dataset_line.strip()} in json file')
                    continue
                # Grab the dictionary of file metadata from the json file
                my_files_dict = data_json['file_locations'][dataset_line.strip()]
                # Convert the dictionary into the format we want for the open data portal
                my_files = []
                for afile in my_files_dict:
                    my_files += [ {'filename':afile,
                                   'checksum':my_files_dict[afile]['checksum'],
                                   'size':my_files_dict[afile]['size'],
                                   'events':my_files_dict[afile]['events'],
                                   'type':my_files_dict[afile]['type'],
                                   'uri_root':my_files_dict[afile]['uri'] } ]
                # Final check that we have at least one file
                if len(my_files)==0:
                    print(f'No files identified for {dataset_line.strip()}')
                    continue
            else:
                # This is a list of metadata for the MC samples
                filename = 'MC_'+dataset_line.split()[2].strip().replace('\\','')+'_filelist.json'
                # Get the list of files
                my_did = dataset_line.split()[0].strip()
                my_full_did_names = [ x for x in mc_json['file_locations'] if '.'+my_did+'.' in x ]
                if len(my_full_did_names)>1:
                    print(f'Warning: Found multiple matching DIDs from {my_did} : {my_full_did_names}')
                elif len(my_full_did_names)==0:
                    print(f'Found no matching DIDs from {my_did} : {my_full_did_names}')
                    continue
                my_full_did_name = my_full_did_names[0]
                # Grab the dictionary of file metadata from the json file
                my_files_dict = mc_json['file_locations'][my_full_did_name]
                # Convert the dictionary into the format we want for the open data portal
                my_files = []
                for afile in my_files_dict:
                    my_files += [ {'filename':afile,
                                   'checksum':my_files_dict[afile]['checksum'],
                                   'size':my_files_dict[afile]['size'],
                                   'events':my_files_dict[afile]['events'],
                                   'type':my_files_dict[afile]['type'],
                                   'uri_root':my_files_dict[afile]['uri'] } ]
                # Final check that we have at least one file
                if len(my_files)==0:
                    print(f'No files identified for {my_full_did_name} from {my_did}')
                    continue

            # Set the metadata in the `super` (open data portal record) json
            my_json['files'] += [ { 'filename':filename } ]
            # Now open that file and write the file names there
            with open(output_directory+'/'+filename,'w') as dataset_filelist_file:
                json.dump( my_files , dataset_filelist_file )

    # Write myself a json file
    summary_file_name = 'atlas-2024-'+dataset_files[adataset]['name_short']+'.json'
    with open(output_directory+'/'+summary_file_name,'w') as outfile:
        json.dump( my_json , outfile )

# Not clear if I need to generate adler checksums for the index json files I'm creating here
