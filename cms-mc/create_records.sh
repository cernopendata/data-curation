#!/bin/bash

# This bash script reads the local cache and creates a json record for the
# dataset list in lists/CMS-YYYY-mc-datasets.txt

year=2012

list="lists/CMS-"$year"-mc-datasets.txt"
recordfile="cms-simulated-datasets-"$year".json"
errorfile="records-"$year".err"
doi="./inputs/doi-cms-mc-"$year"-released.txt"
recid="./inputs/recid-cms-mc-"$year"-datasets.py"

echo -e "Creating json record for" $list
echo -e "DOI file:\t" $doi
echo -e "RECID file:\t" $recid

python cms-mc/interface.py --create-records \
                           --eos-dir  ./cache/$year/eos-file-indexes/ \
                           --das-dir  ./cache/$year/das-json-store/ \
                           --mcm-dir  ./cache/$year/mcm-store/ \
                           --conf-dir ./cache/$year/config-store/ \
                           --doi-file $doi \
                           --recid-file $recid \
                           $list > $recordfile 2>$errorfile || exit $?

echo -e "\nDone :)"
echo -e "Output file is " $recordfile
echo -e "Check errors in " $errorfile