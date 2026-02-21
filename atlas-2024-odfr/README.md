# ATLAS Open Data for Research

This contains the scripts necessary for creating the json records for the CERN open data portal for the first release of ATLAS Open Data for research.

The scripts involved are:

- `transfer_data.sh` for transferring collision data to the CERN ATLAS Open Data endpoint.
- `transfer_mc.py` for transferring MC simulation datasets to the CERN ATLAS Open Data endpoint. Note that this is significantly more complicated than data because for MC we transfer only a subset of many datasets, rather than trying to provide the full statistics (to keep sizes down). This outputs a json file with much of the metadata needed for the MC.
- `create_data_metadata.py` to create a json file with the necessary metadata for all data files, including dataset:file mapping.
- `add_file_locations_to_mc.py` for updating the MC metadata json record to include file locations and other metadata needed for the open data records.

These scripts start from text file inputs, which are mostly lists of datasets and their metadata:

- `pp_data_p6026_GRL.txt`, the full list of collision data datasets in 2015 and 2016 processed with p-tag p6026
- `pp_2015_data_p6026_tids.txt`, the list of collision data datasets for 2015 data only
- `pp_2016_data_p6026_tids.txt`, the list of collision data datasets for 2016 data only
- `pp_mc_physlite_p6026*.txt` the lists of MC simulation datasets processed with p-tag p6026
- A series of metadata files describing the MC datasets, `mc_*`, made from blocks of `mc_sets.txt`

From running the scripts and the transfers, a number of metadata json records are created:

- `mc_file_mapping_OpenData_*.json`, a json file resulting from the `transfer_mc.py` script, containing three objects:
    - A list of transfer rules (`rule_list`)
    - A map of the datasets to the files transferred to CERN within them (`file_dictionary`)
    - A map from the ATLAS dataset name to the name of the subset of data transferred to CERN
- `mc_file_mapping_OpenData_*_with_metadata.json`, a json file that is an extended version of `mc_file_mapping_OpenData_*.json` also containing a dictionary (`file_locations`) keyed on datasets, with values that are also dictionaries, keyed on files. For each file, the dictionary contains:
    - The adler 32 checksum for the file
    - The size of the file in bytes
    - The number of events in the file
    - The type of the file (`DAOD_PHYSLITE`)
    - The location of the file at CERN (the `uri`)
- `data_file_mapping_OpenData_v0_p6026_2024-04-15.json`, a json file resulting from the `create_data_metadata.py` script, containing two dictionaries. One dictionary is a map from datasets to files (`file_dictionary`), and the other is a dictionary like the metadata dictionary created for the MC (`file_locations`).

To generate the open data records themselves, a final script is provided, `mkjson.py`. This script takes in the above-created text and json files and attempts to stitch together the actual open data portal json files.

