#!/bin/sh

# prepare outputs
mkdir -p ./outputs

# create L1 trigger records
python2 ./code/create_l1_trigger_information_records.py > ./outputs/cms-l1-trigger-information-Run2011A.xml

# verify results
xmllint --noout ./outputs/*.xml
