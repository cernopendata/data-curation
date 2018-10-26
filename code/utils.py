#!/usr/bin/env python

import re
import os

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
