#!/bin/sh

## 1) create EOS file indexes:
#
# simko@lxplus8> export EOS_MGM_URL=root://eospublic.cern.ch
# simko@lxplus8> mkdir -p inputs/eos-file-indexes
# simko@lxplus8> python2 ./code/create_eos_file_indexes.py
# simko@laptop> rsync -av simko@lxplus8.cern.ch:/<remote-path>/inputs/eos-file-indexes/ ./inputs/eos-file-indexes

## 2) prepare inputs
#
# populate inputs/das-json-store/*.json by running code/create-das-json-store.sh as CERNAPCMS on lxplus8
#
# cernapcms@lxplus8> ./code/create-das-json-store.sh
# simko@laptop> rsync -av cernapcms@lxplus8.cern.ch:tibor/data-curation/cms-2012-collision-datasets-update/inputs/das-json-store/ ./inputs/das-json-store
#
# populate inputs/das-json-config-store/*.json and inputs/config-store by running code/create-das-json-config-store.sh as CERNAPCMS on lxplus8
# cernapcms@lxplus8> ./code/create-das-json-config-store.sh
# simko@laptop> rsync -av cernapcms@lxplus8.cern.ch:tibor/data-curation/cms-2012-collision-datasets-update/inputs/das-json-config-store/ ./inputs/das-json-config-store
# simko@laptop> rsync -av cernapcms@lxplus8.cern.ch:tibor/data-curation/cms-2012-collision-datasets-update/inputs/config-store/ ./inputs/config-store

## 3) compare RECO files to verify which ones we need to create for new datasets:
#
# ./code/compare-reco-config-files-2012abcd.sh
# mkdir -p outputs
python ./code/create_reco_config_files.py
python ./code/create_reco_config_file_records.py > ./outputs/cms-reco-configuration-files-2012-update.json

## 4) HLT config files and trigger paths should already exist for 2012 datasets, no need to create them here

## 5) now you can create collision data

python ./code/create_dataset_records.py --run-period Run2012A > ./outputs/cms-primary-datasets-Run2012A.json
python ./code/create_dataset_records.py --run-period Run2012D > ./outputs/cms-primary-datasets-Run2012D.json

## 6) check the validity of resulting JSON files

jsonlint -q ./outputs/*.json

## 7) now you can copy them to COD3 fixtures working directory

\cp outputs/*.json ../../opendata.cern.ch/cernopendata/modules/fixtures/data/records
