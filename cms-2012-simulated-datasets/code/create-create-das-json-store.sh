#!/usr/bin/env sh
#
# Creates a shell script file that is to be run as cernapcms on LXPLUS.  Example:
#
# tibor@laptop> ./code/create-create-das-json-store.sh > ./outputs/create-das-json-store.sh
# cernapcms@lxplus> mkdir tibor
# tibor@laptop> scp outputs/create-das-json-store.sh cernapcms@lxplus.cern.ch:tibor
# cernapcms@lxplus> cd tibor
# cernapcms@lxplus> voms-proxy-init --voms cms
# cernapcms@lxplus> ./create-das-json-store.sh
# tibor@laptop> mkdir -p ./inputs/das-json-store
# tibor@laptop> scp -r cernapcms@lxplus.cern.ch:tibor/{config,dataset,parent} ./inputs/das-json-store
#
# The resulting `*.json` files are to be copied to ../inputs/das-json-store/
# directory on the working laptop.

mcdatasets=./inputs/mc-datasets.txt

echo mkdir -p ./dataset
echo mkdir -p ./parent
echo mkdir -p ./config

while IFS= read -r dataset_full_name
do
    dataset=$(echo "${dataset_full_name}" | awk -F'/' '{print $2;}')
    if ls ./inputs/eos-file-indexes/ | grep -q "${dataset}"; then
        # take only datasets that have EOS file information
        result_file=$(echo "${dataset_full_name}" | tr '/' '@')
        echo "dasgoclient -query \"dataset=${dataset_full_name}\" -json > ./dataset/${result_file}.json"
        echo "dasgoclient -query \"parent dataset=${dataset_full_name}\" -json > ./parent/${result_file}.json"
        echo "dasgoclient -query \"config dataset=${dataset_full_name}\" -json > ./config/${result_file}.json"
    fi
done < "$mcdatasets"
