#!/usr/bin/env python2

"""
Create EOS rich index files for datasets.

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

XROOTD_URI_BASE = 'root://eospublic.cern.ch/'

XROOTD_DIR_BASE = '/eos/opendata/'

EXPERIMENT = 'cms'

INPUT = './inputs/cms-2012-collision-datasets.txt'

OUTPUTDIR = './inputs/eos-file-indexes'

DEBUG = True


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


def get_dataset_location(dataset):
    "Return EOS location of the dataset."
    return XROOTD_DIR_BASE + EXPERIMENT + '/' + \
        get_dataset_runperiod(dataset) + '/' + \
        get_dataset_name(dataset) + '/' + \
        get_dataset_format(dataset) + '/' + \
        get_dataset_version(dataset)


def get_volumes(dataset):
    "Return list of volumes for the given dataset."
    volumes = []
    dataset_location = get_dataset_location(dataset)
    output = subprocess.check_output('eos ls -1 ' + dataset_location, shell=True)
    for line in output.split('\n'):
        if line and line != 'file-indexes':
            volumes.append(line)
    return volumes


def get_files(dataset, volume):
    "Return file list with information about name, size, location for the given dataset and volume."
    files = []
    dataset_location = get_dataset_location(dataset)
    output = subprocess.check_output('eos find --size --checksum ' + dataset_location + '/' + volume, shell=True)
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


def create_index_file(dataset, volume, files, style='txt'):
    "Create index file in the given style format (text, json)."
    filebase = EXPERIMENT.upper() + '_' + \
               get_dataset_runperiod(dataset) + '_' + \
               get_dataset_name(dataset) + '_' + \
               get_dataset_format(dataset) + '_' + \
               get_dataset_version(dataset) + '_' + \
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
    files = get_files(dataset, volume)
    filename = create_index_file(dataset, volume, files, 'txt')
    copy_index_file(dataset, volume, filename)
    filename = create_index_file(dataset, volume, files, 'json')
    copy_index_file(dataset, volume, filename)


def main():
    "Do the job."

    for line in open(INPUT, 'r').readlines():
        dataset = line.strip()
        volumes = get_volumes(dataset)
        for volume in volumes:
            create_index_files(dataset, volume)


if __name__ == '__main__':
    main()
