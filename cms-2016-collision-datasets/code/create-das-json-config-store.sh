#!/usr/bin/env bash

# get dataset configuration info
mkdir -p ./inputs/das-json-config-store
while IFS= read -r dataset; do
    dataset_result_file=$(echo $dataset | tr '/' '@')
    okay=0
    while [ $okay -lt 1 ]; do
	echo "==> DAS config dataset=$dataset"
	dasgoclient -query "config dataset=$dataset" -json > ./inputs/das-json-config-store/"${dataset_result_file}.json"
	if [ $? -eq 0 ]; then
	    okay=1
	fi
    done
done < ./inputs/cms-2016-collision-datasets.txt

# get the config file info for the RECO step (the parent of MINI)
minis=$(cat inputs/cms-2016-collision-datasets.txt | grep '/MINI')
for dataset in $minis; do
    parent=$(dasgoclient -query "parent dataset=$dataset")
    dataset_result_file=$(echo $parent | tr '/' '@')
    okay=0
    while [ $okay -lt 1 ]; do
	echo "==> DAS config dataset=$parent"
	dasgoclient -query "config dataset=$parent" -json > ./inputs/das-json-config-store/"${dataset_result_file}.json"
	if [ $? -eq 0 ]; then
	    okay=1
	fi
    done
done

# extract configuration file URLs
rm -f temp_urls
for file in $(ls -1 inputs/das-json-config-store/*.json); do
    cat $file | jq -S '.[].config [] | .urls' | grep https >> temp_urls
done
sed -i -e 's,",,g' temp_urls
sed -i -e 's,configFile\,,configFile,g' temp_urls
cat temp_urls | sort -u > urls

# download configuration files
mkdir -p ./inputs/config-store
cat urls | awk -F/ '{print "curl -o ./inputs/config-store/"$6".configFile -k --key ~/.globus/userkey.nodes.pem --cert ~/.globus/usercert.pem " $0}' | bash

# remove config files with process HARVESTING
configs_harvesting=$(grep -l HARVESTING inputs/config-store/*)
for c in $configs_harvesting; do 
    rm $c; 
done
