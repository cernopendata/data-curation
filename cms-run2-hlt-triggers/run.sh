#!/bin/sh

# Move to the directory the script is in
script_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd $script_path

# prepare outputs
mkdir -p ./outputs

# init CMSSW
cd ./outputs
scramv1 project CMSSW CMSSW_10_6_10
cd CMSSW_10_6_10/src
eval `scramv1 runtime -sh`
git cms-addpkg HLTrigger/Configuration
cd ../../..

# convert configuration files
python3 ./code/create_hlt_trigger_configurations.py

# create HLT trigger information records
python3 ./code/create_hlt_trigger_information_records.py > ./outputs/cms-trigger-information-run2-helper.html