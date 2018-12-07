#!/bin/sh

## 1) prepare outputs

mkdir -p ./outputs

## 2) create EOS file indexes
#
# aiadm> export EOS_MGM_URL=root://eospublic.cern.ch
# aiadm> source /afs/cern.ch/project/eos/installation/cms/etc/setup.sh
# aiadm> source ./code/eos-get-listings.sh # ...and copy outputs to /inputs/eos-file-indexes

## 3) populate DAS JSON store (to be run on LXPLUS with CMS credentials)
#
# python2 ./code/create_das_json_store.py # ...and copy outputs to ./inputs/das-json-store

## 4) classify datasets (and agree with CMS on the results)
#
# python2 ./code/classify_datasets.py

## 5) create config download script (to be run on LXPLUS with CMS credentials)
#
# python2 ./code/create_config_download_script.py # ...and run and xcopy outputs to ./inputs/config-store

## 6) create config file records
#
# python2 ./code/create_config_file_records.py > ./outputs/cms-configuration-files-Run2011A.xml 2> ./outputs/config_files_link_info.py

## 7) create HLT config file records
#
# python2 ./code/create_hlt_config_file_records.py > ./outputs/cms-hlt-2011-configuration-files.xml 2> ./outputs/hlt_link_info.py

## 7) create simulated dataset records

python2 ./code/create_simulated_dataset_records.py > ./outputs/cms-simulated-datasets-Run2011A.xml

## 8) verify results

xmllint --noout ./outputs/*.xml
