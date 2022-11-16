#!/bin/sh

## 1) create EOS file indexes:
#
# simko@aiadm> export EOS_MGM_URL=root://eospublic.cern.ch
# simko@aiadm> python ./code/create_eos_file_indexes.py
# simko@laptop> scp <remote>/eos-file-indexes/ ./inputs/eos-file-indexes

## 2) prepare inputs
#
# populate inputs/das-json-store/*.json by running code/create-das-json-store.sh as CERNAPCMS on LXPLUS
#
# $ wget -O inputs/fwyzard-hlt-2012-dataset.txt https://fwyzard.web.cern.ch/fwyzard/hlt/2012/dataset

## 3) create HLT config files and trigger paths
#
# python ./code/create-hlt-config-file-records.py > ./outputs/cms-hlt-configuration-files-2012.json
# python ./code/create-hlt-trigger-path-records.py > ./outputs/cms-hlt-trigger-paths-2012.json

## 4) create RECO config files
#
# python ./code/create-reco-config-file-records.py > ./outputs/cms-reco-configuration-files-2012.json

## 5) now you can create collision data

python ./code/create-cms-2012-collision-datasets.py --run-period Run2012B > ./outputs/cms-primary-datasets-Run2012B.json
python ./code/create-cms-2012-collision-datasets.py --run-period Run2012C > ./outputs/cms-primary-datasets-Run2012C.json

## 6) check the validity of resulting JSON files

jsonlint -q ./outputs/*.json

## 7) now you can copy them to COD3 fixtures working directory
#
#\cp outputs/*.json ../../opendata.cern.ch/cernopendata/modules/fixtures/data/records
\cp outputs/cms-primary-datasets-Run2012B.json ../../opendata.cern.ch/cernopendata/modules/fixtures/data/records
\cp outputs/cms-primary-datasets-Run2012C.json ../../opendata.cern.ch/cernopendata/modules/fixtures/data/records
