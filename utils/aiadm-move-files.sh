#!/bin/bash

# Move files for a given dataset from CMS Open Data upload staging area to the
# CMS Open Data production target area.
#
# Needs to run under `bash`.
#
# Usage:
#
# aiadm> export EOS_MGM_URL=root://eospublic.cern.ch
# aiadm> DATASET=BTag source ./aiadm-move-files.sh
#
# Use with care!

# for collision data, use something like:
#DATASET=${DATASET:DoubleElectron}
SOURCEDIR=/eos/opendata/cms/upload/data/Run2011A
TARGETDIR=/eos/opendata/cms/Run2011A

# for simulated data, use something like:
#DATASET=SMHiggsToZZTo4L_M-125_8TeV-powheg15-JHUgenV3-pythia6
#SOURCEDIR=/eos/opendata/cms/upload/mc/Summer12_DR53X
#TARGETDIR=/eos/opendata/cms/MonteCarlo2012/Summer12_DR53X

# for true execution, use:
echo=''

# for debugging, use:
#echo='echo'

if [ "$DATASET" = "" ]; then
    echo "[ERROR] Please set DATASET environment variable."
    echo "[ERROR] Example: DATASET=SMHiggsToZZTo4L_M-125_8TeV-powheg15-JHUgenV3-pythia6 source ./aiadm-move-files.sh"
    exit 1
fi

# part one: create directories

files=$(eos find -d "$SOURCEDIR/$DATASET" | sed 's,path=,,g')
for file in $files; do
    if [ "${file: -1}" == "/" ]; then
        filebase=${file:${#SOURCEDIR}}
        $echo eos mkdir -p "$TARGETDIR$filebase"
    else
        echo "[ERROR] Unexpected file found."
    fi
done

# part two: move files

files=$(eos find -f "$SOURCEDIR/$DATASET" | sed 's,path=,,g')
for file in $files; do
    if [ "${file: -1}" == "/" ]; then
        echo "[ERROR] Unexpected directory found."
    else
        filebase=${file:${#SOURCEDIR}}
        $echo eos file rename "$file" "$TARGETDIR$filebase"
    fi
done

# part three: remove empty directories

dirs=$(eos find -d "$SOURCEDIR/$DATASET" | awk '{print length, $0;}' | sort -n -r | awk '{print $2;}' | sed 's,path=,,g')
for dir in $dirs; do
    if eos find -d --childcount "$dir" | grep -q "nfiles=0"; then
        echo -n "Removing empty directory $dir..."
        $echo eos rmdir "$dir"
        echo "done."
    fi
done
