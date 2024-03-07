#!/bin/sh

## 1) create EOS file indexes:

# lxplus> eos find --xurl --size --checksum /eos/opendata/jade/upload/documentation/LogBooks | grep pdf > ./inputs/eos-file-information-logbooks.txt

## 2) create JADE logbook records

mkdir -p outputs
python ./code/create_logbook_records.py > ./outputs/jade-logbooks.json
python ./code/create_cn_records.py

## 6) check the validity of resulting JSON files

jsonlint -q ./outputs/*.json

## 7) copy them to CERN Open Data fixtures directory

# \cp outputs/*.json ../../opendata.cern.ch/cernopendata/modules/fixtures/data/records
