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
# tibor@laptop> scp cernapcms@lxplus.cern.ch:tibor/*.json ./inputs/das-json-store
#
# The resulting `*.json` files are to be copied to ../inputs/das-json-store/
# directory on the working laptop.

mcdatasets=./inputs/mc-datasets.txt

while IFS= read -r dataset_full_name
do
    dataset=$(echo "${dataset_full_name}" | awk -F'/' '{print $2;}')
    if [ -e "./inputs/eos-file-information/${dataset}-file-list.txt" ]; then
        # take only datasets that have EOS file information
        result_file=$(echo "${dataset_full_name}" | tr '/' '@')
        echo "dasgoclient -query "dataset=${dataset_full_name}" -json > ${result_file}.json"
    fi
done < "$mcdatasets"
