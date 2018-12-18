#!/bin/bash

# Usage:
# $ YYYY=2010 ./make_local_cache.sh

# this script makes a local cache of a list of CMS MC datasets

if [ -z ${YYYY} ]; then
    echo "[ERROR] Please set YYYY environment variable with wanted year."
    echo "[ERROR] Example: YYYY=2010 $0"
    exit 1
fi

year=${YYYY}

datasets="inputs/CMS-"$year"-mc-datasets.txt"

# TODO
# targz each step
# mount the dirs in RAM to avoid file number limit

# step 1
export EOS_MGM_URL=root://eospublic.cern.ch
python code/interface.py --create-eos-indexes \
                           --eos-dir ./cache/$year/eos-file-indexes/ \
                           $datasets 2>eos-indexes-${year}.err || exit $?

# step 2
# you should have voms-proxy here!
# voms-proxy-init --voms cms --rfc --valid 190:00
python code/interface.py --create-das-json-store \
                           --ignore-eos-store \
                           --eos-dir ./cache/$year/eos-file-indexes/ \
                           --das-dir ./cache/$year/das-json-store/ \
                           $datasets 2>das-store-${year}.err || exit $?

# step 3
python code/interface.py --create-mcm-store \
                           --ignore-eos-store \
                           --eos-dir ./cache/$year/eos-file-indexes/ \
                           --das-dir ./cache/$year/das-json-store/ \
                           --mcm-dir ./cache/$year/mcm-store/ \
                           $datasets 2>mcm-store-${year}.err || exit $?

# step 4
# in ~/.globus/ dir, follow the instructions from
# https://ca.cern.ch/ca/help/?kbid=024010 and also this other command:
# $ openssl pkcs12 -in myCert.p12 -nocerts -nodes -out userkey.nodes.pem
python code/interface.py --get-conf-files \
                           --ignore-eos-store \
                           --eos-dir ./cache/$year/eos-file-indexes/ \
                           --das-dir ./cache/$year/das-json-store/ \
                           --mcm-dir ./cache/$year/mcm-store/ \
                           --conf-dir ./cache/$year/config-store/ \
                           $datasets 2>conffiles-${year}.err || exit $?

echo -e "\n\n"
echo -e ":)"
echo -e "Local cache created in ./cache/${year}/"
echo -e "Check the error files in current dir:"
echo -e "\t - eos-indexes-${year}.err"
echo -e "\t - das-store-${year}.err"
echo -e "\t - mcm-store-${year}.err"
echo -e "\t - conffiles-${year}.err"
