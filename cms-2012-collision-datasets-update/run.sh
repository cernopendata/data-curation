#!/bin/sh

## 1) create EOS file indexes:
#
# simko@aiadm> export EOS_MGM_URL=root://eospublic.cern.ch
# simko@aiadm> mkdir -p inputs/eos-file-indexes
# simko@aiadm> python ./code/create_eos_file_indexes.py
# simko@laptop> scp -r simko@lxplus-cloud.cern.ch:/<remote-path>/eos-file-indexes/ ./inputs/eos-file-indexes

## 2) prepare inputs
#
# populate inputs/das-json-store/*.json by running code/create-das-json-store.sh as CERNAPCMS on LXPLUS
#
# cernapcms@lxplus> ./code/create-das-json-store.sh
# simko@laptop> sscp -r cernapcms@lxplus.cern.ch:tibor/data-curation/cms-2012-collision-datasets-update/inputs/das-json-store ./inputs/das-json-store
#
# populate inputs/das-json-config-store/*.json and inputs/config-store by running code/create-das-json-config-store.sh as CERNAPCMS on LXPLUS
# cernapcms@lxplus> ./code/create-das-json-config-store.sh
# simko@laptop> sscp -r cernapcms@lxplus.cern.ch:tibor/data-curation/cms-2012-collision-datasets-update/inputs/das-json-config-store ./inputs/das-json-config-store
# simko@laptop> sscp -r cernapcms@lxplus.cern.ch:tibor/data-curation/cms-2012-collision-datasets-update/inputs/config-store ./inputs/config-store
#
# the following line is not needed for 2012, the hlt path file for 2012 is already in inputs
# $ wget -O inputs/fwyzard-hlt-2011-dataset.txt https://fwyzard.web.cern.ch/fwyzard/hlt/2011/dataset

## 3) compare RECO files to verify that we don't need to create any:
#
# ./code/compare-2012released-2012new-config-files.sh

## 4) HLT config files and trigger paths should already exist for 2012 datasets, no need to create them here

## 5) now you can create collision data

mkdir -p outputs
python ./code/create_dataset_records.py > ./outputs/cms-primary-datasets-Run2012-update.json

## 6) check the validity of resulting JSON files

jsonlint -q ./outputs/*.json

## 7) now you can copy them to COD3 fixtures working directory

\cp outputs/*.json ../../opendata.cern.ch/cernopendata/modules/fixtures/data/records
