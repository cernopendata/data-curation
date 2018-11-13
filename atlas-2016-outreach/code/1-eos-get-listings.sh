#!/usr/bin/env bash

# Usage:
#
# aiadm> export EOS_MGM_URL=root://eospublic.cern.ch
# aiadm> source ./eos-get-listings.sh

rootdir=/eos/opendata/atlas/OutreachDatasets/2016-07-29

for subdir in Data MC VM SW; do
    for onefile in $(eos ls -1 ${rootdir}/${subdir}); do
            fileindex=${onefile}_file_index.txt
            fileindex=$(echo ${fileindex} | sed 's,.root,,')
            fileindex=$(echo ${fileindex} | sed 's,.vdi.gz,,')
            fileindex=$(echo ${fileindex} | sed 's,.tar.gz,,')
            filesizes=${onefile}_file_sizes.xml
            filesizes=$(echo ${filesizes} | sed 's,.root,,')
            filesizes=$(echo ${filesizes} | sed 's,.vdi.gz,,')
            filesizes=$(echo ${filesizes} | sed 's,.tar.gz,,')
            rm -f $fileindex
            rm -f $filesizes
            echo "root://eospublic.cern.ch/${rootdir}/${subdir}/${onefile}" >> $fileindex
            echo "    <datafield tag=\"856\" ind1=\"7\" ind2=\" \">
      <subfield code=\"2\">xrootd</subfield>
      <subfield code=\"u\">root://eospublic.cern.ch/${rootdir}/${subdir}/${onefile}</subfield>
      <subfield code=\"s\">$(eos ls -l ${rootdir}/${subdir}/${onefile} | awk '{print $5;}')</subfield>
    </datafield>" >> $filesizes
    done
done
