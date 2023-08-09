#!/usr/bin/env bash
#
# Note: to be run as cernapcms on lxplus8.  Example:
#
# cernapcms@lxplus031> mkdir xxx
# cernapcms@lxplus031> cd xxx
# cernapcms@lxplus031> voms-proxy-init --voms cms
# cernapcms@lxplus031> ./create-das-json-store.sh
#
# The resulting `*.json` files are to be copied to ../inputs/das-json-store/
# directory on the working laptop.

mkdir -p ./inputs/das-json-store
while IFS= read -r dataset; do
    dataset_result_file=$(echo $dataset | tr '/' '@')
    dasgoclient -query "dataset=$dataset" -json > ./inputs/das-json-store/"${dataset_result_file}.json"
done < ./inputs/cms-2015-collision-datasets-hi-ppref.txt
