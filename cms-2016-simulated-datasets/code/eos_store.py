#!/usr/bin/env python2

"""
Create EOS rich index files for CMS 2012 MC datasets.

Creates files in the eos_dir (see below) but also copies them onto EOS final
destination (unless DEBUG is set).

To be run on AIADM:

$ export EOS_MGM_URL=root://eospublic.cern.ch
$ python ./code/create-eos-rich-file-indexes.py

"""

import json
import os
import sys
import re
import subprocess
from utils import get_dataset_name, \
                  get_dataset_runperiod, \
                  get_dataset_version, \
                  get_dataset_format, \
                  get_dataset_year

XROOTD_URI_BASE = 'root://eospublic.cern.ch/'

XROOTD_DIR_BASE = '/eos/opendata/'

MCDIR_BASE = 'mc'

EXPERIMENT = 'cms'

DEBUG = True


def check_datasets_in_eos_dir(datasets, eos_dir):
    "Return subset of datasets that have EOS information in eos_dir"
    # FIXME this function is extremely slow. Takes some minutes for 3k datasets
    dataset_full_names = []
    for dataset in datasets:
        dataset_index_file_base = get_dataset_index_file_base(dataset)
        if subprocess.call('ls ' + eos_dir + ' | grep -q ' + dataset_index_file_base, shell=True):
            print('[ERROR] Missing EOS information, ignoring dataset ' + dataset,
                  file=sys.stderr)
        else:
            dataset_full_names.append(dataset)

    return dataset_full_names


def get_dataset_index_file_base(dataset):
    "Return index file base for given dataset."
    filebase = EXPERIMENT.upper() + '_' + \
               MCDIR_BASE + '_' + \
               get_dataset_runperiod(dataset) + '_' + \
               get_dataset_name(dataset) + '_' + \
               get_dataset_format(dataset) + '_' + \
               get_dataset_version(dataset)
    return filebase

def get_dataset_location(dataset):
    "Return EOS location of the dataset."
    return XROOTD_DIR_BASE + \
        EXPERIMENT + '/' + \
        MCDIR_BASE + '/' + \
        get_dataset_runperiod(dataset) + '/' + \
        get_dataset_name(dataset) + '/' + \
        get_dataset_format(dataset) + '/' + \
        get_dataset_version(dataset)


def get_dataset_volumes(dataset):
    "Return list of volumes for the given dataset."
    volumes = []
    dataset_location = get_dataset_location(dataset)
    try:
        output = subprocess.check_output('eos ls -1 ' + dataset_location, shell=True)
    except subprocess.CalledProcessError:
        return []
    output = str(output.decode("utf-8"))
    for line in output.split('\n'):
        if line and line != 'file-indexes':
            volumes.append(line)
    return volumes


def get_dataset_volume_files(dataset, volume):
    "Return file list with information about name, size, location for the given dataset and volume."
    files = []
    dataset_location = get_dataset_location(dataset)
    output = subprocess.check_output('eos oldfind --size --checksum ' + dataset_location + '/' + volume, shell=True)
    output = str(output.decode("utf-8"))
    for line in output.split('\n'):
        if line and line != 'file-indexes':
            match = re.match(r'^path=(.*) size=(.*) checksum=(.*)$', line)
            if match:
                path, size, checksum = match.groups()
                files.append({'filename': os.path.basename(path),
                              'size': int(size),
                              'checksum': 'adler32:' + checksum,
                              'uri': XROOTD_URI_BASE + path})
    return files


def create_index_file(dataset, volume, files, eos_dir, style='txt'):
    "Create index file in the given style format (text, json)."
    filebase = get_dataset_index_file_base(dataset) + '_' + \
               volume + '_' + \
               'file_index'
    filename = filebase + '.' + style
    fdesc = open(eos_dir + '/' + filename, 'w')
    if style == 'txt':
        for afile in files:
            fdesc.write(afile['uri'])
            fdesc.write('\n')
    elif style == 'json':
        fdesc.write(json.dumps(files, indent=2, sort_keys=True))
        fdesc.write('\n')
    fdesc.close()
    return filename


def copy_index_file(dataset, volume, filename, eos_dir):
    "Copy index file filename to its final destination on EOS."
    dataset_location = get_dataset_location(dataset)
    cmd = 'eos cp ' + eos_dir + '/' + filename + ' ' + dataset_location + '/file-indexes/' + filename
    if DEBUG:
        print(cmd)
    else:
        os.system(cmd)


def create_index_files(dataset, volume, eos_dir):
    "Create index files for the given dataset and volumes."
    files = get_dataset_volume_files(dataset, volume)
    filename = create_index_file(dataset, volume, files, eos_dir, 'txt')
    copy_index_file(dataset, volume, filename, eos_dir)
    filename = create_index_file(dataset, volume, files, eos_dir, 'json')
    copy_index_file(dataset, volume, filename, eos_dir)


def main(datasets = [], eos_dir = './inputs/eos-file-indexes/'):
    "Do the job."

    if not os.path.exists(eos_dir):
        os.makedirs(eos_dir)

    for dataset in datasets:
        volumes = get_dataset_volumes(dataset)
        for volume in volumes:
            create_index_files(dataset, volume, eos_dir)


if __name__ == '__main__':
    main()
