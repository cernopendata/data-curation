#!/usr/bin/env zsh

## 0) Create EOS file indexes for Run2010A datasets:
# (we can reuse 2012 code)
#
# (cd inputs; ln -sf ./cms-Run2010A-collision-datasets.txt ./cms-2012-collision-datasets.txt)
# python ../cms-2012-collision-datasets/code/create_eos_file_indexes.py
# rm -f ./inputs/cms-2012-collision-datasets.txt
#
# (cd inputs; ln -sf ./cms-Commissioning10-collision-datasets.txt ./cms-2012-collision-datasets.txt)
# python ../cms-2012-collision-datasets/code/create_eos_file_indexes.py
# rm -f ./inputs/cms-2012-collision-datasets.txt

## 1) prepare inputs
#
# wget -O inputs/fwyzard-hlt-2010-dataset.txt https://fwyzard.web.cern.ch/fwyzard/hlt/2010/dataset

## 2) prepare outputs
#
# mkdir -p ./outputs

# 3) create HLT config records
python ./code/create_hlt_config_file_records.py > ./outputs/cms-hlt-configuration-files-2010.json
