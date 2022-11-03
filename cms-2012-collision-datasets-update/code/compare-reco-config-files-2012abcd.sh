#!/usr/bin/env bash

while IFS= read -r dataset; do
    dataset_short=$(echo $dataset)

    if [[ "$1" != "" ]] && [[ "$dataset_short" != "$1" ]]; then
        continue
    fi

    echo
    echo
    echo "==> $dataset_short"

    file_2012a=''
    for file in $(ls -1 ./inputs/config-store/*); do
        if grep -q reco_2012A_${dataset_short}.py $file; then
            file_2012a=$file
        fi
    done

    file_2012b=''
    for file in $(ls -1 ../cms-2012-collision-datasets/inputs/reco-config-files/*); do
        if grep -q reco_2012B_${dataset_short}.py $file; then
            file_2012b=$file
        fi
    done

    file_2012c=''
    for file in $(ls -1 ../cms-2012-collision-datasets/inputs/reco-config-files/*); do
        if grep -q reco_2012C_${dataset_short}.py $file; then
            file_2012c=$file
        fi
    done

    file_2012d=''
    for file in $(ls -1 ./inputs/config-store/*); do
        if grep -q reco_2012D_${dataset_short}.py $file; then
            file_2012d=$file
        fi
    done

    if [[ -e $file_2012a ]]; then
        echo " --> 2012a file $file_2012a"
        grep 'process = cms.Process' $file_2012a
    else
        echo " --> 2012a file missing"
    fi
    if [[ -e $file_2012b ]]; then
        echo " --> 2012b file $file_2012b"
        grep 'process = cms.Process' $file_2012b
    else
        echo " --> 2012b file missing"
    fi
    if [[ -e $file_2012c ]]; then
        echo " --> 2012c file $file_2012c"
        grep 'process = cms.Process' $file_2012c
    else
        echo " --> 2012c file missing"
    fi
    if [[ -e $file_2012d ]]; then
        echo " --> 2012d file $file_2012d"
        grep 'process = cms.Process' $file_2012d
    else
        echo " --> 2012d file missing"
    fi

    if [[ -e $file_2012a ]] && [[ -e $file_2012b ]]; then
        echo " --> 2012 RunA RunB"
        echo " --> colordiff $file_2012a $file_2012b"
        colordiff "$file_2012a" "$file_2012b"
    fi
    if [[ -e $file_2012a ]] && [[ -e $file_2012c ]]; then
        echo " --> 2012 RunA RunC"
        echo " --> colordiff $file_2012a $file_2012c"
        colordiff "$file_2012a" "$file_2012c"
    fi
    if [[ -e $file_2012a ]] && [[ -e $file_2012d ]]; then
        echo " --> 2012 RunA RunD"
        echo " --> colordiff $file_2012a $file_2012d"
        colordiff "$file_2012a" "$file_2012d"
    fi
    if [[ -e $file_2012b ]] && [[ -e $file_2012c ]]; then
        echo " --> 2012 RunB RunC"
        echo " --> colordiff $file_2012b $file_2012c"
        colordiff "$file_2012b" "$file_2012c"
    fi
    if [[ -e $file_2012b ]] && [[ -e $file_2012d ]]; then
        echo " --> 2012 RunB RunD"
        echo " --> colordiff $file_2012b $file_2012d"
        colordiff "$file_2012b" "$file_2012d"
    fi
    if [[ -e $file_2012c ]] && [[ -e $file_2012d ]]; then
        echo " --> 2012 RunC RunD"
        echo " --> colordiff $file_2012c $file_2012d"
        colordiff "$file_2012c" "$file_2012d"
    fi

done < <(cat ./inputs/cms-2012-collision-datasets-update.txt | awk -F/ '{print $2;}' | sort -u)
