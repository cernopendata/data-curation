# ATLAS Heavy Ion Open Data for Research

This contains the scripts necessary for creating the json records for the CERN open data portal for the first release of ATLAS Heavy Ion Open Data for research.

The scripts involved are:

- `transfer_data.sh` for transferring all data to the CERN ATLAS Open Data endpoint with the opendata account (permissions must be granted to use this account).
- `recreate_containers.py` for recreating all the containers in the opendata scope and adding some top-level containers
- `create_metadata.py` to create a json file with the necessary metadata for all files, including dataset:file mapping.

These scripts start from text file inputs, which are mostly lists of datasets and their metadata:

- `dataset_list.txt`, all the data and MC datasets processed with tag p6480
- `hi_p6480_data.txt`, the list of collision data datasets for 2015 data only
- `hi_p6480_mc.txt`, the list of MC simulation datasets

From running the scripts and the transfers, a number of metadata json records are created:

- `hion_file_mapping_OpenData_v0_p6480_2024-11-19.json`, a json file resulting from the `create_metadata.py` script, containing three objects:
    - A map of the datasets to the files transferred to CERN within them (`file_dictionary`)
    - A dictionary (`file_locations`) keyed on datasets, with values that are also dictionaries, keyed on files. For each file, the dictionary contains:
       - The adler 32 checksum for the file
       - The size of the file in bytes
       - The number of events in the file
       - The type of the file (`DAOD_HION14`)
       - The location of the file at CERN (the `uri`)

To generate the open data records themselves, a final script is provided, `mk_hi_json.py`. This script takes in the above-created text and json files and attempts to stitch together the actual open data portal json files. Three json files are created for records: one for MC, one for data, and one to link them. Individual json files are also created for each dataset with the file information for that dataset.

Finally, the records are to be enriched with file indexes by means of `create_file_indexes.py` script:

```
$ python ./create_file_indexes.py > test/x.sh
$ cd test && zip -r x.zip x.sh eos-file-indexes
```

The generated helper script `x.sh` is to be executed on LXPLUS by the CERN Open Data team to copy the generated EOS file indexes to the expected place in EOSPUBLIC.
