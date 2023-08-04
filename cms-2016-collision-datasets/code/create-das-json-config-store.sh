#!/usr/bin/env bash

#
# Note: to be run as cernapcms on LXPLUS.  Example:
#
# cernapcms@lxplus031> mkdir xxx
# cernapcms@lxplus031> cd xxx
# cernapcms@lxplus031> voms-proxy-init --voms cms
# cernapcms@lxplus031> ./create-das-json-config-store.sh
#
# The resulting `*.json` files are to be copied to ../inputs/das-json-config-store/
# directory on the working laptop.

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
