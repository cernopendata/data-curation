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
    /BJetPlusX/Run2012B-22Jan2013-v1/AOD \
    /BTag/Run2012B-22Jan2013-v1/AOD \
    /Commissioning/Run2012B-22Jan2013-v1/AOD \
    /DoubleElectron/Run2012B-22Jan2013-v1/AOD \
    /DoubleMuParked/Run2012B-22Jan2013-v1/AOD \
    /DoublePhoton/Run2012B-22Jan2013-v1/AOD \
    /DoublePhotonHighPt/Run2012B-22Jan2013-v1/AOD \
    /ElectronHad/Run2012B-22Jan2013-v1/AOD \
    /HTMHTParked/Run2012B-22Jan2013-v1/AOD \
    /HcalNZS/Run2012B-22Jan2013-v1/AOD \
    /JetHT/Run2012B-22Jan2013-v1/AOD \
    /JetMon/Run2012B-22Jan2013-v1/AOD \
    /MET/Run2012B-22Jan2013-v1/AOD \
    /MinimumBias/Run2012B-22Jan2013-v1/AOD \
    /MuEG/Run2012B-22Jan2013-v1/AOD \
    /MuHad/Run2012B-22Jan2013-v1/AOD \
    /MuOnia/Run2012B-22Jan2013-v1/AOD \
    /MuOniaParked/Run2012B-22Jan2013-v1/AOD \
    /NoBPTX/Run2012B-22Jan2013-v1/AOD \
    /PhotonHad/Run2012B-22Jan2013-v1/AOD \
    /SingleElectron/Run2012B-22Jan2013-v1/AOD \
    /SingleMu/Run2012B-22Jan2013-v1/AOD \
    /SinglePhoton/Run2012B-22Jan2013-v1/AOD \
    /TauParked/Run2012B-22Jan2013-v1/AOD \
    /TauPlusX/Run2012B-22Jan2013-v1/AOD \
    /VBF1Parked/Run2012B-22Jan2013-v1/AOD \
    /BJetPlusX/Run2012C-22Jan2013-v1/AOD \
    /BTag/Run2012C-22Jan2013-v1/AOD \
    /Commissioning/Run2012C-22Jan2013-v1/AOD \
    /DoubleElectron/Run2012C-22Jan2013-v1/AOD \
    /DoubleMuParked/Run2012C-22Jan2013-v1/AOD \
    /DoublePhoton/Run2012C-22Jan2013-v2/AOD \
    /DoublePhotonHighPt/Run2012C-22Jan2013-v1/AOD \
    /ElectronHad/Run2012C-22Jan2013-v1/AOD \
    /HTMHTParked/Run2012C-22Jan2013-v1/AOD \
    /HcalNZS/Run2012C-22Jan2013-v1/AOD \
    /JetHT/Run2012C-22Jan2013-v1/AOD \
    /JetMon/Run2012C-22Jan2013-v1/AOD \
    /MET/Run2012C-22Jan2013-v1/AOD \
    /MinimumBias/Run2012C-22Jan2013-v1/AOD \
    /MuEG/Run2012C-22Jan2013-v1/AOD \
    /MuHad/Run2012C-22Jan2013-v1/AOD \
    /MuOnia/Run2012C-22Jan2013-v1/AOD \
    /MuOniaParked/Run2012C-22Jan2013-v1/AOD \
    /NoBPTX/Run2012C-22Jan2013-v1/AOD \
    /PhotonHad/Run2012C-22Jan2013-v1/AOD \
    /SingleElectron/Run2012C-22Jan2013-v1/AOD \
    /SingleMu/Run2012C-22Jan2013-v1/AOD \
    /SinglePhoton/Run2012C-22Jan2013-v1/AOD \
    /TauParked/Run2012C-22Jan2013-v1/AOD \
    /TauPlusX/Run2012C-22Jan2013-v1/AOD \
    /VBF1Parked/Run2012C-22Jan2013-v1/AOD; \
    do
        dataset_result_file=$(echo $dataset | tr '/' '@')
        dasgoclient -query "dataset=$dataset" -json > "${dataset_result_file}.json"
done
