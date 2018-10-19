#!/usr/bin/env python2

"""
Create EOS rich index files for CMS 2012 MC datasets.

Creates files in the OUTPUTDIR (see below) but also copies them onto EOS final
destination (unless DEBUG is set).

To be run on AIADM:

$ export EOS_MGM_URL=root://eospublic.cern.ch
$ python ./code/create-eos-rich-file-indexes.py

"""

import json
import os
import re
import subprocess
from utils import get_dataset_name, \
                  get_dataset_runperiod, \
                  get_dataset_version, \
                  get_dataset_format

XROOTD_URI_BASE = 'root://eospublic.cern.ch/'

XROOTD_DIR_BASE = '/eos/opendata/'

MCDIR = 'MonteCarlo2012'

EXPERIMENT = 'cms'

INPUT = './inputs/mc-datasets.txt'

OUTPUTDIR = './inputs/eos-file-indexes'

DEBUG = True


def get_dataset_location(dataset):
    "Return EOS location of the dataset."
    return XROOTD_DIR_BASE + \
        EXPERIMENT + '/' + \
        MCDIR + '/' + \
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
    output = subprocess.check_output('eos find --size --checksum ' + dataset_location + '/' + volume, shell=True)
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


def get_dataset_index_file_base(dataset):
    "Return index file base for given dataset."
    filebase = EXPERIMENT.upper() + '_' + \
               MCDIR + '_' + \
               get_dataset_runperiod(dataset) + '_' + \
               get_dataset_name(dataset) + '_' + \
               get_dataset_format(dataset) + '_' + \
               get_dataset_version(dataset)
    return filebase


def create_index_file(dataset, volume, files, style='txt'):
    "Create index file in the given style format (text, json)."
    filebase = get_dataset_index_file_base(dataset) + '_' + \
               volume + '_' + \
               'file_index'
    filename = filebase + '.' + style
    fdesc = open(OUTPUTDIR + '/' + filename, 'w')
    if style == 'txt':
        for afile in files:
            fdesc.write(afile['uri'])
            fdesc.write('\n')
    elif style == 'json':
        fdesc.write(json.dumps(files, indent=2, sort_keys=True))
        fdesc.write('\n')
    fdesc.close()
    return filename


def copy_index_file(dataset, volume, filename):
    "Copy index file filename to its final destination on EOS."
    dataset_location = get_dataset_location(dataset)
    cmd = 'eos cp ' + OUTPUTDIR + '/' + filename + ' ' + dataset_location + '/file-indexes/' + filename
    if DEBUG:
        print(cmd)
    else:
        os.system(cmd)


def create_index_files(dataset, volume):
    "Create index files for the given dataset and volumes."
    files = get_dataset_volume_files(dataset, volume)
    filename = create_index_file(dataset, volume, files, 'txt')
    copy_index_file(dataset, volume, filename)
    filename = create_index_file(dataset, volume, files, 'json')
    copy_index_file(dataset, volume, filename)


def main(datasets = []):
    "Do the job."

    if not os.path.exists(OUTPUTDIR):
        os.makedirs(OUTPUTDIR)

    for dataset in datasets:
        volumes = get_dataset_volumes(dataset)
        for volume in volumes:
            create_index_files(dataset, volume)


if __name__ == '__main__':
    main()
