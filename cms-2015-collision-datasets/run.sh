#!/bin/sh

## 1) prepare inputs for EOS file indexes

# simko@aiadm> export EOS_MGM_URL=root://eospublic.cern.ch
# simko@aiadm> mkdir -p inputs/eos-file-indexes
# simko@aiadm> python2 ./code/create_eos_file_indexes.py
# simko@laptop> scp -r simko@lxplus-cloud.cern.ch:/<remote-path>/eos-file-indexes/ ./inputs/eos-file-indexes

## 2) prepare inputs for dataset file and size information

# cernapcms@lxplus> ./code/create-das-json-store.sh
# simko@laptop> sscp -r cernapcms@lxplus.cern.ch:tibor/data-curation/cms-2011-collision-datasets-runb-update/inputs/das-json-store ./inputs/das-json-store

## 3) prepare inputs for dataset RECO configuration file information

# cernapcms@lxplus> ./code/create-das-json-config-store.sh
# simko@laptop> scp -r cernapcms@lxplus.cern.ch:tibor/data-curation/cms-2015-collision-datasets/inputs/das-json-config-store ./inputs/das-json-config-store
# simko@laptop> scp -r cernapcms@lxplus.cern.ch:tibor/data-curation/cms-2015-collision-datasets/inputs/config-store ./inputs/config-store

## 4) create HLT config files and trigger paths

python ./code/create_hlt_config_file_records.py > ./outputs/cms-hlt-configuration-files-2015.json
python ./code/create_hlt_trigger_path_records.py > ./outputs/cms-hlt-trigger-paths-2015.json

## 5) create RECO config files

python ./code/create_reco_config_file_records.py > ./outputs/cms-reco-configuration-files-2015.json

## 6) now you can create collision data

python ./code/create_cms_2015_collision_datasets.py > ./outputs/cms-primary-datasets-Run2015D.json

## 7) prepare trigger information record snippet

python ./code/create_hlt_trigger_information_record.py > ./outputs/cms-trigger-information-2015.json

## 8) check the validity of resulting JSON files

for file in outputs/*.json; do jsonlint -q "$file"; done

## 9) now you can copy outputs to OPENDATA fixtures working directory
#
\cp outputs/*.json ../../opendata.cern.ch/cernopendata/modules/fixtures/data/records
