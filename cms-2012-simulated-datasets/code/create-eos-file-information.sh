#!/bin/sh
#
# To be run on AIADM after setting:
# $ export EOS_MGM_URL=root://eospublic.cern.ch

MCDIR=/eos/opendata/cms/MonteCarlo2012/Summer12_DR53X
datasets=$(eos ls -1 ${MCDIR}/*)
for dataset in ${datasets}; do
    eos find --size "${MCDIR}/${dataset}" > "./inputs/eos-file-information/${dataset}-file-list.txt"
done
