#!/usr/bin/env python2

"""
Create EOS rich index files for datasets.

Creates files in the OUTPUTDIR (see below) but also copies them onto EOS final
destination (unless DEBUG is set).

To be run on AIADM:

$ export EOS_MGM_URL=root://eospublic.cern.ch
$ python ./code/create_eos_file_indexes_alice.py
$ ls -l ./inputs/eos-file-indexes/

"""

import json
import os
import re
import subprocess

XROOTD_URI_BASE = 'root://eospublic.cern.ch/'

XROOTD_DIR_BASE = '/eos/opendata/'

EXPERIMENT = 'alice'

FORMAT = 'ESD'

INPUTS = [
    {'dataset': 'LHC10b_pp_ESD_117222', 'location': '/eos/opendata/alice/2010/LHC10b/000117222/'},
    {'dataset': 'LHC10h_PbPb_ESD_138275', 'location': '/eos/opendata/alice/2010/LHC10h/000138275/'},
    {'dataset': 'LHC10h_PbPb_ESD_139038', 'location': '/eos/opendata/alice/2010/LHC10h/000139038/'},
    {'dataset': 'LHC10h_PbPb_ESD_139173', 'location': '/eos/opendata/alice/2010/LHC10h/000139173/'},
    {'dataset': 'LHC10h_PbPb_ESD_139437', 'location': '/eos/opendata/alice/2010/LHC10h/000139437/'},
    {'dataset': 'LHC10h_PbPb_ESD_139438', 'location': '/eos/opendata/alice/2010/LHC10h/000139438/'},
    {'dataset': 'LHC10h_PbPb_ESD_139465', 'location': '/eos/opendata/alice/2010/LHC10h/000139465/'},
    {'dataset': 'LHC10c_pp_ESD_120076', 'location': '/eos/opendata/alice/2010/LHC10c/000120076/'},
    {'dataset': 'LHC10c_pp_ESD_120244', 'location': '/eos/opendata/alice/2010/LHC10c/000120244/'},
    {'dataset': 'LHC10c_pp_ESD_120505', 'location': '/eos/opendata/alice/2010/LHC10c/000120505/'},
    {'dataset': 'LHC10c_pp_ESD_120616', 'location': '/eos/opendata/alice/2010/LHC10c/000120616/'},
    {'dataset': 'LHC10c_pp_ESD_120822', 'location': '/eos/opendata/alice/2010/LHC10c/000120822/'},
    {'dataset': 'LHC10c_pp_ESD_120824', 'location': '/eos/opendata/alice/2010/LHC10c/000120824/'},
    {'dataset': 'LHC10c_pp_ESD_120829', 'location': '/eos/opendata/alice/2010/LHC10c/000120829/'},
]

OUTPUTDIR = './inputs/eos-file-indexes'

DEBUG = True


def get_dataset_index_file_base(dataset):
    "Return index file base for given dataset."
    filebase = EXPERIMENT.upper() + '_' + \
        dataset
    return filebase


def get_files(dataset, location):
    "Return file list with information about name, size, location for the given dataset."
    files = []
    output = subprocess.check_output('eos find --size --checksum ' + location, shell=True)
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


def create_index_file(dataset, files, style='txt'):
    "Create index file in the given style format (text, json)."
    filebase = EXPERIMENT.upper() + '_' + \
        dataset + '_' + \
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


def copy_index_file(dataset, location, filename):
    "Copy index file filename to its final destination on EOS."
    cmd = 'eos cp ' + OUTPUTDIR + '/' + filename + ' ' + location + 'ESD' + '/file-indexes/' + filename
    if DEBUG:
        print(cmd)
    else:
        os.system(cmd)


def create_index_files(dataset, location):
    "Create index files for the given dataset."
    files = get_files(dataset, location)
    filename = create_index_file(dataset, files, 'txt')
    copy_index_file(dataset, location, filename)
    filename = create_index_file(dataset, files, 'json')
    copy_index_file(dataset, location, filename)


def main():
    "Do the job."

    for dataset_info in INPUTS:
        create_index_files(dataset_info['dataset'], dataset_info['location'])


if __name__ == '__main__':
    main()
