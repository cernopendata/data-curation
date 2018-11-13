#!/usr/bin/env bash

# Usage:
#
# aiadm> export EOS_MGM_URL=root://eospublic.cern.ch
# aiadm> source ./eos-get-listings.sh

rootdir=/eos/opendata/atlas/MasterclassDatasets/ZPath/2015

for dataset in $(eos ls -1 ${rootdir}); do
    fileindex=ATLAS_MasterclassDatasets_ZPath_2015_dataset_${dataset}_file_index.txt
    filesizes=ATLAS_MasterclassDatasets_ZPath_2015_dataset_${dataset}_file_sizes.xml
    rm -f "$fileindex"
    rm -f "$filesizes"
    for onefile in $(eos ls -1 ${rootdir}/${dataset}); do
        echo "root://eospublic.cern.ch/${rootdir}/${dataset}/${onefile}" >> $fileindex
        echo "    <datafield tag=\"856\" ind1=\"7\" ind2=\" \">
      <subfield code=\"2\">xrootd</subfield>
      <subfield code=\"u\">root://eospublic.cern.ch/${rootdir}/${dataset}/${onefile}</subfield>
      <subfield code=\"s\">$(eos ls -l ${rootdir}/${dataset}/${onefile} | awk '{print $5;}')</subfield>
    </datafield>" >> $filesizes
    done
done
