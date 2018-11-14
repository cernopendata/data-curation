#!/usr/bin/env bash

# Usage:
#
# aiadm> export EOS_MGM_URL=root://eospublic.cern.ch
# aiadm> source /afs/cern.ch/project/eos/installation/cms/etc/setup.sh
# aiadm> source ./eos-get-listings.sh

for dataset in BTag DoubleElectron DoubleMu ElectronHad ForwardTriggers HT Jet MET METBTag MinimumBias MuEG MuHad MuOnia MultiJet Photon PhotonHad SingleElectron SingleMu Tau TauPlusX; do
    version=$(eos ls -1 /eos/opendata/cms/Run2011A/${dataset}/AOD/*)
    for volume in $(eos ls -1 /eos/opendata/cms/Run2011A/${dataset}/AOD/${version}/*); do
        fileindex=CMS_Run2011A_${dataset}_AOD_${version}_${volume}_file_index.txt
        filesizes=CMS_Run2011A_${dataset}_AOD_${version}_${volume}_file_sizes.xml
        rm -f $fileindex
        rm -f $filesizes
        for filename in $(eos ls -1 /eos/opendata/cms/Run2011A/${dataset}/AOD/${version}/${volume}); do
            echo "root://eospublic.cern.ch//eos/opendata/cms/Run2011A/${dataset}/AOD/${version}/${volume}/${filename}" >> $fileindex
                echo "    <datafield tag=\"856\" ind1=\"7\" ind2=\" \">
      <subfield code=\"2\">xrootd</subfield>
      <subfield code=\"u\">root://eospublic.cern.ch//eos/opendata/cms/Run2011A/${dataset}/AOD/${version}/${volume}/${filename}</subfield>
      <subfield code=\"s\">$(eos ls -l /eos/opendata/cms/Run2011A/${dataset}/AOD/${version}/${volume}/${filename} | awk '{print $5;}')</subfield>
    </datafield>" >> $filesizes
        done
    done
done
