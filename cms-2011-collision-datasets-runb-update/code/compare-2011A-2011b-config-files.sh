#!/usr/bin/env bash

while IFS= read -r dataset; do
    dataset_short=$(echo $dataset | awk -F '/' '{print $2}')
    echo "==> $dataset_short"
    file_2011a=''
    for file in $(ls -1 ../cms-2011-collision-datasets/inputs/config-store/*); do
        if grep -q reco_2011A_${dataset_short} $file; then
            file_2011a=$file
        fi
    done
    file_2011b=''
    for file in $(ls -1 ./inputs/config-store/*); do
        if grep -q reco_2011B_${dataset_short} $file; then
            file_2011b=$file
        fi
    done
    if [[ -e $file_2011a ]] && [[ -e $file_2011b ]]; then
        colordiff $file_2011a $file_2011b
    else
        if [[ ! -e $file_2011a ]]; then
            echo ' --> 2011a file missing'
        fi
        if [[ ! -e $file_2011b ]]; then
            echo ' --> 2011b file missing'
        fi
    fi
done < ./inputs/cms-2011-collision-datasets.txt
