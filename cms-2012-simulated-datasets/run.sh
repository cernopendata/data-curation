#!/bin/sh

# 1) create EOS file indexes:
#
# simko@aiadm> export EOS_MGM_URL=root://eospublic.cern.ch
# simko@aiadm> python ./code/create_eos_file_indexes.py
# simko@laptop> rsync -avz simko@aiadm.cern.ch:private/project/opendata/cms-2012-open-data-release/simulated-data/inputs/eos-file-indexes/ ./inputs/eos-file-indexes

# 2) prepare DAS JSON store creation script:

# ./code/create-create-das-json-store.sh > ./outputs/create-das-json-store.sh

# 3) run it on AIADM:

# tibor@laptop> ./code/create-create-das-json-store.sh > ./outputs/create-das-json-store.sh
# cernapcms@lxplus> mkdir tibor
# tibor@laptop> scp outputs/create-das-json-store.sh cernapcms@lxplus.cern.ch:tibor
# cernapcms@lxplus> cd tibor
# cernapcms@lxplus> voms-proxy-init --voms cms
# cernapcms@lxplus> ./create-das-json-store.sh
# tibor@laptop> mkdir -p ./inputs/das-json-store
# tibor@laptop> scp -r cernapcms@lxplus.cern.ch:tibor/{config,dataset,parent} ./inputs/das-json-store

# 4) create conffile download script:

#python ./code/create-create-config-store.py > ./outputs/create-config-store.sh

# 5) run conffile download script:

# tibor@laptop> ./code/create-create-config-store.sh > ./outputs/create-config-store.sh
# cernapcms@lxplus> mkdir tibor
# tibor@laptop> scp outputs/create-config-store.sh cernapcms@lxplus.cern.ch:tibor
# cernapcms@lxplus> cd tibor
# cernapcms@lxplus> voms-proxy-init --voms cms
# cernapcms@lxplus> source ./create-config-store.sh
# tibor@laptop> mkdir -p ./inputs/config-store
# tibor@laptop> scp -r cernapcms@lxplus.cern.ch:tibor/config-store/* ./inputs/config-store

# *) allocate recIDs

# python ./code/allocate_recids.py

# *) create config file records

python ./code/create_configfile_records.py > ./outputs/cms-configuration-files-2012.json

# *) create MC 2012 records

python ./code/create_dataset_records.py > ./outputs/cms-simulated-datasets-2012.json

# *) check the validity of resulting JSON files:

#jsonlint -q ./outputs/*.json

## *) now you can copy them to COD3 fixtures working directory
#
# \cp outputs/*.json /home/simko/private/src/opendata.cern.ch/cernopendata/modules/fixtures/data/records
