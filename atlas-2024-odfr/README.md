# ATLAS Open Data for Research

This contains the scripts necessary for creating the json records for the CERN open data portal for the first release of ATLAS Open Data for research. The files in brief are:

- A series of metadata files describing the MC datasets, `mc_*`, made from blocks of `mc_sets.txt`
- A json file mapping MC datasets to files, `file_mapping_OpenData_v0_2024-02-28.json`
- A python script for transferring MC datasets to the CERN Open Data endpoint, `transfer_mc.py`
- A simple shell script for transferring collision data to the CERN Open Data endpoint, `transfer_data.sh`
- The full list of data, `pp_data.txt` (this is just the concatenation of the two individual years)
- The full list of MC datasets, `pp_mc_full.txt`. This is a list of datasets, not the metadata described above
- A json file mapping collision data to files, `data_file_mapping_OpenData_v0_2024-04-03.json`
- A python script for generating that file mapping json file, `filenames_data.py`
- A python script for generating the draft open data portal records and associated text files, `mkjson.py`
