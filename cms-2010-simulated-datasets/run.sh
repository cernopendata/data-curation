#!/bin/sh

# 1) create EOS file indexes: (on LXPLUS)
#
export EOS_MGM_URL=root://eospublic.cern.ch
#mkdir -p ./outputs
#python ./code/create_eos_file_indexes.py > ./outputs/z.sh
#source ./outputs/z.sh
#rm ./outputs/z.sh

# 2) create record fixture snippets:
python3 ./code/create_dataset_records_files.py > ./outputs/cms-simulated-datasets-2010-files.json
