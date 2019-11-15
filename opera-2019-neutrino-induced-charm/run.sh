#!/bin/sh

# prepare inputs
cd inputs && unzip -q events && cd ..

# prepare outputs
mkdir -p ./outputs

# create event records
python ./code/create_opera_events.py

# verify results
jsonlint -q ./outputs/opera-events.json

# wash our bowl
rm -rf ./inputs/events
