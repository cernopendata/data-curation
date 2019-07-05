#!/usr/bin/env python


"""
Create MC 2010 file list information for fixtures.
"""

import hashlib
import json
import re
import os
import subprocess
import sys
import zlib

from create_eos_file_indexes import \
    XROOTD_URI_BASE, \
    get_dataset_index_file_base, \
    get_dataset_location


def get_file_size(afile):
    """Return the size of a file."""
    return os.path.getsize(afile)


def get_file_checksum(afile):
    """Return the ADLER32 checksum of a file."""
    return hex(zlib.adler32(open(afile, 'rb').read(), 1) & 0xffffffff)[2:]


def get_dataset(dataset_full_name):
    "Return short dataset name from dataset full name."
    return re.search(r'^/(.*?)/', dataset_full_name).groups()[0]


def get_dataset_version(dataset_full_name):
    "Return dataset version from dataset full name."
    return re.search(r'^.*Summer12_DR53X-(.*)/AODSIM$', dataset_full_name).groups()[0]


def get_dataset_index_files(dataset_full_name):
    """Return list of dataset file information {path,size} for the given dataset."""
    files = []
    dataset_index_file_base = get_dataset_index_file_base(dataset_full_name)
    output = subprocess.getoutput('ls ./inputs/eos-file-indexes/ | grep ' + dataset_index_file_base)
    for line in output.split('\n'):
        afile = line.strip()
        if afile.endswith('.txt') or afile.endswith('.json'):
            # take only TXT files
            afile_uri = XROOTD_URI_BASE + get_dataset_location(dataset_full_name) + '/file-indexes/' + afile
            afile_size = get_file_size('./inputs/eos-file-indexes/' + afile)
            afile_checksum = get_file_checksum('./inputs/eos-file-indexes/' + afile)
            files.append((afile_uri, afile_size, afile_checksum))
    return files


def newer_dataset_version_exists(dataset_full_name):
    "Return whether the newer version of dataset exists."
    dataset_full_name_until_version = dataset_full_name[0:dataset_full_name.rfind('-')]
    output = subprocess.getoutput('grep ' + dataset_full_name_until_version + ' ./inputs/datasets.txt')
    similar_datasets = output.split('\n')
    similar_datasets.sort()
    return similar_datasets[-1] != dataset_full_name


def create_record(dataset_full_name):
    """Create record snippet for the given dataset."""

    rec = {}

    dataset = get_dataset(dataset_full_name)

    rec['files'] = []
    rec_files = get_dataset_index_files(dataset_full_name)
    for index_type in ['.json', '.txt']:
        index_files = [f for f in rec_files if f[0].endswith(index_type)]
        for file_number, (file_uri, file_size, file_checksum) in enumerate(index_files):
            rec['files'].append({
                'checksum': 'adler32:' + file_checksum,
                'size': file_size,
                'type': 'index' + index_type,
                'uri': file_uri
            })

    rec['title'] = dataset_full_name

    return rec


def create_records(dataset_full_names):
    """Create records."""
    records = []
    for dataset_full_name in dataset_full_names:
        records.append(create_record(dataset_full_name))
    return records


def print_records(records):
    """Print records."""
    print('[')
    for (idx, rec) in enumerate(records):
        print(json.dumps(rec, indent=2, sort_keys=True))
        if idx == len(records) - 1:
            pass
        else:
            print(',')
    print(']')


def main():
    "Do the job."
    dataset_full_names = []
    for line in open('./inputs/datasets.txt', 'r').readlines():
        dataset_full_name = line.strip()
        dataset_index_file_base = get_dataset_index_file_base(dataset_full_name)
        if subprocess.call('ls ./inputs/eos-file-indexes/ | grep -q ' + dataset_index_file_base, shell=True):
            print('[ERROR] Missing EOS information, ignoring dataset ' + dataset_full_name,
                  file=sys.stderr)
        elif newer_dataset_version_exists(dataset_full_name):
            print('[WARNING] Including older dataset version ' + dataset_full_name,
                  file=sys.stderr)
            dataset_full_names.append(dataset_full_name)
        else:
            dataset_full_names.append(dataset_full_name)
    records = create_records(dataset_full_names)
    print_records(records)


if __name__ == '__main__':
    main()
