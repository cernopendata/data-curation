#!/bin/bash

# Usage:
# $ YYYY=2010 ./create_records.sh

# This bash script reads the local cache and creates 2 json records for the
# dataset list in inputs/CMS-YYYY-mc-datasets.txt:
# - cms-simulated-datasets-YYYY.json
# - cms-simulated-datasets-YYYY-conffiles.json

if [ -z ${YYYY} ]; then
    echo "[ERROR] Please set YYYY environment variable with wanted year."
    echo "[ERROR] Example: YYYY=2010 $0"
    exit 1
fi

year=${YYYY}

list="inputs/CMS-"$year"-mc-datasets.txt"

recordfile="outputs/cms-simulated-datasets-"$year".json"
conffile="outputs/cms-simulated-datasets-"$year"-conffiles.json"

errorfile=$(echo $recordfile | sed 's,.json,.err,g')
conferrorfile=$(echo $conffile | sed 's,.json,.err,g')

doi="./inputs/doi-cms-mc-"$year"-released.txt"
recid="./inputs/recid-cms-mc-"$year"-datasets.py"

mkdir -p outputs

echo -e "Creating JSON records for" $list
echo -e "DOI file:\t" $doi
echo -e "RECID file:\t" $recid

python code/interface.py --create-records \
                           --eos-dir  ./cache/$year/eos-file-indexes/ \
                           --das-dir  ./cache/$year/das-json-store/ \
                           --mcm-dir  ./cache/$year/mcm-store/ \
                           --conf-dir ./cache/$year/config-store/ \
                           --doi-file $doi \
                           --recid-file $recid \
                           $list > $recordfile 2>$errorfile || exit $?

python code/interface.py --create-conffile-records \
                           --eos-dir  ./cache/$year/eos-file-indexes/ \
                           --das-dir  ./cache/$year/das-json-store/ \
                           --mcm-dir  ./cache/$year/mcm-store/ \
                           --conf-dir ./cache/$year/config-store/ \
                           --doi-file $doi \
                           --recid-file $recid \
                           $list > $conffile 2>$conferrorfile || exit $?

echo -e "\nDone :)\n"
echo -e "Output files are: " $recordfile $conffile
echo -e "Check errors in: " $errorfile $conferrorfile
