#!/bin/sh
#
# To be run on AIADM after setting:
# $ export EOS_MGM_URL=root://eospublic.cern.ch

eos find --size /eos/opendata/cms/Run2012B > ./inputs/eos-file-information.txt
eos find --size /eos/opendata/cms/Run2012C >> ./inputs/eos-file-information.txt
