#!/bin/sh

## 1) create EOS file indexes:
#
# python3 ./code/create_eos_file_indexes.py
#
# # copy produced files to EOS as a CMS curator:
# # server> cd ./inputs/eos-file-indexes && for file in *.sh; do sh $file; done

## 2) prepare inputs
#
# ./code/create-das-json-store.sh
# ./code/create-das-json-config store.sh

## 3) create HLT config files and trigger paths
#
# python3 ./code/create_hlt_trigger_listings.py
python3 ./code/create_hlt_config_file_records.py > ./outputs/cms-hlt-configuration-files-2017.json
python3 ./code/create_hlt_trigger_path_records.py > ./outputs/cms-hlt-trigger-paths-2017.json
python3 ./code/create_hlt_trigger_information_record.py > ./outputs/cms-trigger-information-2017.json

## 4) create RECO config files
#
python3 ./code/create_reco_config_file_records.py > ./outputs/cms-reco-configuration-files-2017.json

## 5) now you can create collision data

python3 ./code/create_cms_2017_collision_datasets.py > ./outputs/cms-primary-datasets-Run2017.json

## 6) transfer produced files to local data-curation instance

# laptop> rsync -avz cernapcms@lxplus.cern.ch:/eos/home-c/cernapcms/data-curation/cms-2016-collision-datasets/outputs/ ./outputs

## 7) check the validity of resulting JSON files

# laptop> jsonlint -q ./outputs/*.json

## 8) now you can copy them to COD3 fixtures working directory

# laptop> \cp outputs/*.json ../../opendata.cern.ch/cernopendata/modules/fixtures/data/records

