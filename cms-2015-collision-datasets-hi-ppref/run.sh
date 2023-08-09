#!/bin/sh

## 1) create EOS file indexes:
#
# simko@lxplus8> export EOS_MGM_URL=root://eospublic.cern.ch
# simko@lxplus8> mkdir -p inputs/eos-file-indexes
# simko@lxplus8> python2 ./code/create_eos_file_indexes.py
# simko@laptop> rsync -av simko@lxplus8.cern.ch:/<remote-path>/inputs/eos-file-indexes/ ./inputs/eos-file-indexes

## 2) populate inputs/das-json-store/*.json by running code/create-das-json-store.sh as CERNAPCMS on lxplus8
#
# cernapcms@lxplus8> ./code/create-das-json-store.sh
# simko@laptop> rsync -av cernapcms@lxplus8.cern.ch:tibor/data-curation/cms-2015-collision-datasets-hi-ppref/inputs/das-json-store/ ./inputs/das-json-store

## 3) create HLT config file and trigger path records
#
# Was done as part of the cms-2015-collision-datasets release. (Includes HI data.)

## 4) create RECO config file records

python ./code/create_reco_config_file_records.py > ./outputs/cms-reco-configuration-files-HIpp-Run2015E.json

## 5) create collision data records

python ./code/create_dataset_records.py > ./outputs/cms-primary-datasets-HIpp-Run2015E.json

## 6) check the validity of resulting JSON files

jsonlint -q ./outputs/*.json

## 7) copy them to the CERN Open Data fixtures directory

\cp outputs/*.json ../../opendata.cern.ch/cernopendata/modules/fixtures/data/records
