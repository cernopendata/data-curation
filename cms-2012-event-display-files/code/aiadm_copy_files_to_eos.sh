#!/bin/sh

for dataset in \
    BJetPlusX \
    BTag \
    Commissioning \
    DoubleElectron \
    DoubleMuParked \
    DoublePhoton \
    DoublePhotonHighPt \
    ElectronHad \
    HcalNZS \
    HTMHTParked \
    JetHT \
    JetMon \
    MET \
    MinimumBias \
    MuEG \
    MuHad \
    MuOnia \
    NoBPTX \
    PhotonHad \
    SingleElectron \
    SingleMu \
    SinglePhoton \
    TauParked \
    TauPlusX \
    VBF1Parked \
    ; do

    for run_period in Run2012B Run2012C; do
        version=22Jan2013-v1
        if [ "$dataset" = "DoublePhoton" ] && [ "${run_period}" = "Run2012C" ]; then
            version=22Jan2013-v2
        fi
        eos mkdir /eos/opendata/cms/${run_period}/${dataset}/IG
        eos mkdir /eos/opendata/cms/${run_period}/${dataset}/IG/${version}
        file=${dataset}_${run_period}_0.ig
        eos cp ./inputs/ig/${file} /eos/opendata/cms/${run_period}/${dataset}/IG/${version}/${file}
    done

done
