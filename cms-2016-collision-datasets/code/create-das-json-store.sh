#!/usr/bin/env sh

mkdir -p ./inputs/das-json-store
while IFS= read -r dataset; do
    dataset_result_file=$(echo $dataset | tr '/' '@')
    dasgoclient -query "dataset=$dataset" -json > ./inputs/das-json-store/"${dataset_result_file}.json"
done < ./inputs/cms-2016-collision-datasets.txt

# minis=$(cat inputs/cms-2016-collision-datasets.txt | grep '/MINI')
# for dataset in $minis; do
#     parent=$(dasgoclient -query "parent dataset=$dataset")
#     dataset_result_file=$(echo $parent | tr '/' '@')
#     dasgoclient -query "dataset=$parent" -json > ./inputs/das-json-store/"${dataset_result_file}.json"
# done

