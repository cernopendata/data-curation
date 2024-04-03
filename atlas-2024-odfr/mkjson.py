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
  'pp_2015_data.txt':'Run 2 2015 proton-proton collision data',
  'pp_2016_data.txt':'Run 2 2016 proton-proton collision data',
  'mc_boson_nominal.txt':'MC simulation electroweak boson nominal samples',
  'mc_exotics_nominal.txt':'MC simulation exotic signal samples',
  'mc_higgs_nominal.txt':'MC simulation Higgs nominal samples',
  'mc_higgs_systematics.txt':'MC simulation Higgs systematic variation samples',
  'mc_jet_nominal.txt':'MC simulation QCD jet nominal samples',
  'mc_jet_systematics.txt':'MC simulation QCD jet systematic variation samples',
  'mc_susy_nominal.txt':'MC simulation SUSY signal samples',
  'mc_top_nominal.txt':'MC simulation top nominal samples',
  'mc_top_systematics.txt':'MC simulation top systematic variation samples'
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
        "DAOD_PHYSLITE"
      ],
    },
    # Dataset type information for Open Data Portal
    "type": {
      "primary": "Dataset",
      "secondary": [
        "Collision"
      ]
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
    }

}

# File with the mapping of file names for each dataset
filename_mc_json_file = open('file_mapping_OpenData_v0_2024-02-28.json','r')
filename_mc_json = json.load(filename_mc_json_file)
filename_data_json_file = open('data_file_mapping_OpenData_v0_2024-04-03.json','r')
filename_data_json = json.load(filename_data_json_file)

for adataset in dataset_files:
    my_json = {}
    # Update with the stuff that's always good
    my_json.update(evergreen_data)
    # Simple abstract for the collection
    my_json['abstract'] = {'description':dataset_files[adataset]+' from the ATLAS experiment'}
    # Name of the collections, systematically set
    my_json['collections'] = ['ATLAS-MC-Simulation-Datasets' if 'mc_' in adataset else 'ATLAS-pp-Collision-Datasets']
    # data-taking year during which the collision data or for which the simulated data, software and other assets were produced
    if 'data' in adataset:
        my_json['date_created'] = [adataset.split('_')[1]]
        my_json['run_period'] = [adataset.split('_')[1]]
    else:
        my_json['date_created'] = ['2015','2016']
        my_json['run_period'] = ['2015','2016']
    my_json['title'] = 'ATLAS DAOD_PHYSLITE format '+dataset_files[adataset]
    my_json['methodology'] = {'description':'<p>These data were created during LS2 as part of a major reprocessing campaign of the Run 2 data. All data were reprocessed using Athena Release 22, and new corresponding MC simulation samples were produced, in an MC simulation campaign called MC20a. These data and MC simulation datasets were processed into DAOD_PHSYLITE format files; this is a light-weight data format intended for general analysis use, sufficient to support a wide variety of ATLAS analyses.'}
    # Do I need to specify a doi? Should be automatically added, I believe
    # Add a record of the files for this dataset
    my_json['files'] = []
    # Make a text file with the files for this dataset
    with open(adataset,'r') as dataset_list_file:
        for dataset_line in dataset_list_file:
            # Make up the name of the text file we'll use for the dataset based on the input lists
            if 'data' in adataset:
                # This is a simple list of dataset names
                # It is normal to sometimes not find files; this just indicates there was no
                #  good data in that run, and it was still processed
                filename = 'Run_'+dataset_line.split('.')[1].strip()+'_filelist.txt'
                if dataset_line.strip() not in filename_data_json['file_dictionary']:
                    print(f'Did not find data dataset {dataset_line.strip()} in json file')
                    continue
                my_files = filename_data_json['file_dictionary'][dataset_line.strip()]
                if len(my_files)==0:
                    print(f'No files identified for {dataset_line.strip()}')
                    continue
            else:
                # This is a list of metadata for the MC samples
                filename = 'MC_'+dataset_line.split()[2].strip().replace('\\','')+'_filelist.txt'
                # Get the list of files
                my_did = dataset_line.split()[0].strip()
                my_full_did_names = [ x for x in filename_mc_json['file_dictionary'] if '.'+my_did+'.' in x ]
                if len(my_full_did_names)>1:
                    print(f'Warning: Found multiple matching DIDs from {my_did} : {my_full_did_names}')
                elif len(my_full_did_names)==0:
                    print(f'Found no matching DIDs from {my_did} : {my_full_did_names}')
                    continue
                my_full_did_name = my_full_did_names[0]
                my_files = filename_mc_json['file_dictionary'][my_full_did_name]
            # Set the metadata in the json
            my_json['files'] += [ { 'uri':filename } ]
            # Now open that file and write the file names there
            with open(output_directory+'/'+filename,'w') as dataset_filelist_file:
                for a_file in my_files:
                    dataset_filelist_file.write(a_file+'\n')

    # Write myself a json file
    with open(output_directory+'/'+adataset.replace('.txt','.json'),'w') as outfile:
        json.dump( my_json , outfile )

# Maybe we want to include something about sizes, checksums, whatever else for the files?
# Not clear if for the individual files or the full datasets, or the lists, or ...
