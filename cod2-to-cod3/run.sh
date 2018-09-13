#!/bin/sh
#
# Pre-requisites:
#
# $ cd ~/private/src/opendata.cern.ch && git checkout qa # COD2
# $ ./scripts/populate-fft-file-cache.sh # COD2
#
# $ cd ~/private/project/opendata/cod2-to-cod3-data-conversion
# $ python ./code/fft_file_cache_info_create.py > ./code/fft_file_cache_info.py

# Usage:
#
# $ cd ~/private/project/opendata/cod3-to-cod3-data-conversion
# $ docker run -i -t --rm -v `pwd`:/data-conversion tiborsimko/invenio:1.2.2 /data-conversion/run.sh
# $ jsonlint -q outputs/*.json

DIR=/data-conversion

for file in $(ls -1 ${DIR}/inputs/*.xml); do
    filebase=$(basename ${file} .xml)
    python ${DIR}/code/convert_records.py ${DIR}/inputs/${filebase}.xml > ${DIR}/outputs/${filebase}.json
done
