#!/bin/sh

## 1) prepare inputs and outputs

mkdir -p ./inputs/ig
mkdir -p ./outputs

## 2) download IG files from CMS DocDB:
#
# ./code/download_ig_files_from_cms_docdb.sh

## 3) transfer files to EOS and copy them to appropriate destination directories:
#
# ./code/aiadm_copy_files_to_eos.sh   # to be run on AIADM

## 4) create event display records

if [[ ! -e ../cms-2012-collision-datasets/outputs/cms-primary-datasets-Run2012B.json ]] ||
   [[ ! -e ../cms-2012-collision-datasets/outputs/cms-primary-datasets-Run2012C.json ]]; then
    echo "[ERROR] Required input files from 'cms-2012-collision-datasets' do not exist."
    echo "[ERROR] Please run the 'cms-2012-collision-datasets' record creation first."
else
    python ./code/create-eventdisplay-files.py --run-period Run2012B > ./outputs/cms-eventdisplay-files-Run2012B.json
    python ./code/create-eventdisplay-files.py --run-period Run2012C > ./outputs/cms-eventdisplay-files-Run2012C.json
fi

## 4) check the validity of resulting JSON files:

jsonlint -q ./outputs/*.json
