#!/usr/bin/env sh

mkdir -p ./inputs/das-json-store
while IFS= read -r dataset; do
    dataset_result_file=$(echo $dataset | tr '/' '@')
    dasgoclient -query "dataset=$dataset" -json > ./inputs/das-json-store/"${dataset_result_file}.json"
done < ./inputs/cms-2016-collision-datasets.txt
