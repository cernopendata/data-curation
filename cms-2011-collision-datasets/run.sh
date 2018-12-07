#!/bin/sh

## 1) prepare inputs
#
# $ wget -O inputs/fwyzard-hlt-2011-dataset.txt https://fwyzard.web.cern.ch/fwyzard/hlt/2011/dataset

## 2) prepare outputs

mkdir -p ./outputs

## 3) create EOS file indexes
#
# aiadm> export EOS_MGM_URL=root://eospublic.cern.ch
# aiadm> source /afs/cern.ch/project/eos/installation/cms/etc/setup.sh
# aiadm> source ./code/eos-get-listings.sh # ...and copy outputs to /inputs/eos-file-indexes

## 4) populate DAS JSON store (to be run on LXPLUS with CMS credentials)
#
# python2 ./code/create_das_json_store.py # ...and copy outputs to ./inputs/das-json-store

## 5) create config download script (to be run on LXPLUS with CMS credentials)
#
# python2 ./code/create_config_download_script.py # ...and copy outputs to ./inputs/config-store

## 6) create config file records
#
# python2 ./code/create_reco_config_file_records.py > ./outputs/cms-configuration-files-Run2011A-RECO.xml 2> ./outputs/link_info.py

## 7) create collision dataset records

python2 ./code/create_collision_dataset_records.py > ./outputs/cms-primary-datasets-Run2011A.xml

## 8) verify results

xmllint --noout ./outputs/*.xml
