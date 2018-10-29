#!/usr/bin/env python

import re
import os
import subprocess


def read_titles(filename):
    """Read dataset titles from filename."""
    titles = {}
    for line in open(filename).readlines():
        line = line.strip()
        if line:
            titles[line] = 1
    return list(titles.keys())


def get_datasets_from_dir(inputdir):
    """Get datasets from directory or txt file."""
    inputdatasets = []

    if re.search(r'.txt$', inputdir):
        for datasettitle in read_titles(inputdir):
            if datasettitle not in inputdatasets:
                inputdatasets.append(datasettitle)
        return inputdatasets

    for dirpath, dummy, inputfilenames in os.walk(inputdir):
        for inputfilename in inputfilenames:
            for datasettitle in read_titles(os.path.join(inputdir,
                                                         inputfilename)):
                if datasettitle not in inputdatasets:
                    inputdatasets.append(datasettitle)

    return inputdatasets


def get_dataset_name(dataset):
    "Return dataset name without version information."
    return dataset.split('/')[1]


def get_dataset_runperiod(dataset):
    "Return dataset run period."
    return dataset.split('/')[2].split('-')[0]


def get_dataset_version(dataset):
    "Return dataset run period."
    return dataset.split('/')[2].split('-', 1)[1]


def get_dataset_format(dataset):
    "Return dataset format."
    return dataset.split('/')[-1]


def check_datasets_in_eos_dir(datasets, eos_dir):
    "Return subset of datasets that have EOS information in eos_dir"
    dataset_full_names = []
    for dataset in datasets:
        dataset_index_file_base = get_dataset_index_file_base(dataset)
        if subprocess.call('ls ' + eos_dir + ' | grep -q ' + dataset_index_file_base, shell=True):
            print('[ERROR] Missing EOS information, ignoring dataset ' + dataset,
                  file=sys.stderr)
        else:
            dataset_full_names.append(dataset)

    return dataset_full_names


def get_dataset_index_file_base(dataset, experiment='CMS', mcdir='MonteCarlo2012'):
    "Return index file base for given dataset."
    filebase = experiment.upper() + '_' + \
               mcdir + '_' + \
               get_dataset_runperiod(dataset) + '_' + \
               get_dataset_name(dataset) + '_' + \
               get_dataset_format(dataset) + '_' + \
               get_dataset_version(dataset)
    return filebase
