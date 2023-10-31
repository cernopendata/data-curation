#!/bin/sh

## 1) To be run on LXPLUS as CMS

# # Move to the directory the script is in
# script_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
# cd $script_path
#
# # prepare outputs
# mkdir -p ./outputs
#
# # init CMSSW
# cd ./outputs
# scramv1 project CMSSW CMSSW_12_6_4
# cd CMSSW_10_6_30/src
# eval `scramv1 runtime -sh`
# git cms-addpkg HLTrigger/Configuration
# cd ../../..
#
# # convert configuration files
# python3 ./code/create_hlt_trigger_configurations.py

## 2) create HLT config file records
python3 ./code/create_hlt_config_file_records.py > ./outputs/cms-hlt-configuration-files-2013.json

## 3) create HLT trigger information records helper
python3 ./code/create_hlt_trigger_information_helper.py > ./outputs/cms-trigger-information-2013-helper.html

## 4) create HLT trigger information record
python3 ./code/create_hlt_trigger_information_record.py > ./outputs/cms-trigger-information-2013.json

## 5) create HLT trigger path records
python3 ./code/create_hlt_trigger_path_records.py > ./outputs/cms-hlt-trigger-paths-2013.json

## 6) check the validity of resulting JSON files
jsonlint -q ./outputs/*.json

## 7) copy them to the CERN Open Data fixtures directory
\cp outputs/*.json ../../opendata.cern.ch/cernopendata/modules/fixtures/data/records
