#!/usr/bin/env bash
#
# Note: to be run as cernapcms on lxplus8.  Example:
#
# cernapcms@lxplus8> mkdir xxx
# cernapcms@lxplus8> cd xxx
# cernapcms@lxplus8> voms-proxy-init --voms cms
# cernapcms@lxplus8> ./create-das-json-config-store.sh
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
done < ./inputs/cms-2013-collision-datasets-hi-ppref.txt

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
cat urls | awk -F/ '{print "curl -o ./inputs/config-store/"$6".configFile -k --key /tmp/x509up_u102955 --cert /tmp/x509up_u102955 " $0}' | bash
