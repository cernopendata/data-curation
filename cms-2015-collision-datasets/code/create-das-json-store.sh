#!/usr/bin/env sh
#
# Note: to be run as cernapcms on LXPLUS.  Example:
#
# cernapcms@lxplus031> mkdir xxx
# cernapcms@lxplus031> cd xxx
# cernapcms@lxplus031> voms-proxy-init --voms cms
# cernapcms@lxplus031> ./create-das-json-store.sh
#
# The resulting `*.json` files are to be copied to ../inputs/das-json-store/
# directory on the working laptop.

for dataset in \
    /Tau/Run2015D-16Dec2015-v1/AOD \
    /SinglePhoton/Run2015D-16Dec2015-v1/AOD \
    /SingleMuon/Run2015D-16Dec2015-v1/AOD \
    /SingleElectron/Run2015D-08Jun2016-v1/AOD \
    /MuonEG/Run2015D-16Dec2015-v1/AOD \
    /MuOnia/Run2015D-16Dec2015-v1/AOD \
    /MET/Run2015D-16Dec2015-v1/AOD \
    /JetHT/Run2015D-16Dec2015-v1/AOD \
    /HTMHT/Run2015D-16Dec2015-v1/AOD \
    /DoubleMuonLowMass/Run2015D-16Dec2015-v1/AOD \
    /DoubleMuon/Run2015D-16Dec2015-v1/AOD \
    /DisplacedJet/Run2015D-16Dec2015-v1/AOD \
    /Charmonium/Run2015D-16Dec2015-v1/AOD \
    /BTagMu/Run2015D-16Dec2015-v1/AOD \
    /BTagCSV/Run2015D-16Dec2015-v1/AOD \
    /DoubleEG/Run2015D-08Jun2016-v1/AOD \
    /ZeroBias/Run2015D-16Dec2015-v1/AOD \
    /Tau/Run2015D-16Dec2015-v1/MINIAOD \
    /SinglePhoton/Run2015D-16Dec2015-v1/MINIAOD \
    /SingleMuon/Run2015D-16Dec2015-v1/MINIAOD \
    /SingleElectron/Run2015D-08Jun2016-v1/MINIAOD \
    /MuonEG/Run2015D-16Dec2015-v1/MINIAOD \
    /MuOnia/Run2015D-16Dec2015-v1/MINIAOD \
    /MET/Run2015D-16Dec2015-v1/MINIAOD \
    /JetHT/Run2015D-16Dec2015-v1/MINIAOD \
    /HTMHT/Run2015D-16Dec2015-v1/MINIAOD \
    /DoubleMuonLowMass/Run2015D-16Dec2015-v1/MINIAOD \
    /DoubleMuon/Run2015D-16Dec2015-v1/MINIAOD \
    /DisplacedJet/Run2015D-16Dec2015-v1/MINIAOD \
    /Charmonium/Run2015D-16Dec2015-v1/MINIAOD \
    /BTagMu/Run2015D-16Dec2015-v1/MINIAOD \
    /BTagCSV/Run2015D-16Dec2015-v1/MINIAOD \
    /DoubleEG/Run2015D-08Jun2016-v1/MINIAOD \
    /ZeroBias/Run2015D-16Dec2015-v1/MINIAOD \
    ; \
    do
        dataset_result_file=$(echo $dataset | tr '/' '@')
        dasgoclient -query "dataset=$dataset" -json > "${dataset_result_file}.json"
done
