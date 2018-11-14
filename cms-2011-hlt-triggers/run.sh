#!/bin/sh

# prepare outputs
mkdir -p ./outputs

# create HLT trigger information records
python2 ./code/create_hlt_trigger_information_records.py > ./outputs/cms-trigger-information-Run2011A-helper.html

# create HLT trigger path records
python2 ./code/create_hlt_trigger_path_records.py > ./outputs/cms-trigger-path-Run2011A.xml

# verify results
xmllint --noout ./outputs/*.xml
