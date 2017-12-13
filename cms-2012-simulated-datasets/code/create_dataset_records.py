#!/usr/bin/env python


"""
Create MC 2012 records.
"""

import hashlib
import json
import re
import os
import subprocess
import sys

from create_eos_file_indexes import \
    XROOTD_URI_BASE, \
    get_dataset_index_file_base, \
    get_dataset_location


RECID_INFO = {}
# read RECID_INFO dictionary created by a friendly program ahead of this one:
exec(open('./outputs/recid_info.py', 'r').read())


def get_from_deep_json(data, akey):
    "Traverse DATA and return first value matching AKEY."
    if type(data) is dict:
        if akey in data.keys():
            return data[akey]
        else:
            for val in data.values():
                if type(val) is dict:
                    aval = get_from_deep_json(val, akey)
                    if aval:
                        return aval
                if type(val) is list:
                    for elem in val:
                        aval = get_from_deep_json(elem, akey)
                        if aval:
                            return aval
    if type(data) is list:
        for elem in data:
            aval = get_from_deep_json(elem, akey)
            if aval:
                return aval
    return None


def get_das_store_json(dataset, query='dataset'):
    "Return DAS JSON from the DAS JSON Store for the given dataset and given query."
    filepath = './inputs/das-json-store/' + query + '/' + dataset.replace('/', '@') + '.json'
    with open(filepath, 'r') as filestream:
        return json.load(filestream)


def get_number_events(dataset):
    """Return number of events for the dataset."""
    number_events = get_from_deep_json(get_das_store_json(dataset), 'nevents')
    if number_events:
        return number_events
    return 0


def get_number_files(dataset):
    """Return number of files for the dataset."""
    number_files = get_from_deep_json(get_das_store_json(dataset), 'nfiles')
    if number_files:
        return number_files
    return 0


def get_size(dataset):
    """Return size of the dataset."""
    size = get_from_deep_json(get_das_store_json(dataset), 'size')
    if size:
        return size
    return 0


def get_file_size(afile):
    "Return file size of a file."
    return os.path.getsize(afile)


def get_file_checksum(afile):
    """Return the SHA1 checksum of a file."""
    return hashlib.sha1(open(afile, 'rb').read()).hexdigest()


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
        if afile.endswith('.txt'):
            # take only TXT files
            afile_uri = XROOTD_URI_BASE + get_dataset_location(dataset_full_name) + '/file-indexes/' + afile
            afile_size = get_file_size('./inputs/eos-file-indexes/' + afile)
            afile_checksum = get_file_checksum('./inputs/eos-file-indexes/' + afile)
            files.append((afile_uri, afile_size, afile_checksum))
    return files


def create_record(dataset_full_name):
    """Create record for the given dataset."""

    rec = {}

    dataset = get_dataset(dataset_full_name)
    year_created = '2012'
    year_published = '2017'
    run_period = '2012A-2012D'
    global_tag = 'START53_V27'
    release = 'CMSSW_5_3_32'

    rec['abstract'] = {}
    rec['abstract']['description'] = '<p>Simulated dataset ' + dataset + ' in AODSIM format for 2012 collision data.</p>' + \
                                     '<p>See the description of the simulated dataset names in: <a href="/about/CMS-Simulated-Dataset-Names">About CMS simulated dataset names</a>.</p>'

    rec['accelerator'] = "CERN-LHC"

    rec['collaboration'] = {}
    rec['collaboration']['name'] = 'CMS collaboration'
    rec['collaboration']['recid'] = '451'

    rec['collections'] = ['CMS-Simulated-Datasets', ]

    rec['collision_information'] = {}
    rec['collision_information']['energy'] = '8TeV'
    rec['collision_information']['type'] = 'pp'

    rec['date_created'] = year_created
    rec['date_published'] = year_published
    rec['date_reprocessed'] = year_created

    rec['distribution'] = {}
    rec['distribution']['formats'] = ['aodsim', 'root']
    rec['distribution']['number_events'] = get_number_events(dataset_full_name)
    rec['distribution']['number_files'] = get_number_files(dataset_full_name)
    rec['distribution']['size'] = get_size(dataset_full_name)

    # rec['doi'] = ''  # FIXME

    rec['experiment'] = 'CMS'

    rec['files'] = []
    rec_files = get_dataset_index_files(dataset_full_name)
    number_index_files = sum([1 for f in rec_files if f[0].endswith('.txt')])
    number_index_file = 1
    for file_uri, file_size, file_checksum in rec_files:
        if file_uri.endswith('.txt'):
            rec['files'].append({
                'checksum': 'sha1:' + file_checksum,
                'description': dataset + ' AOD dataset file index (' + str(number_index_file) + ' of ' + str(number_index_files) + ') for access to data via CMS virtual machine',

                'size': file_size,
                'type': 'index',
                'uri': file_uri
            })
            number_index_file += 1
        else:
            rec['files'].append({
                'checksum': 'sha1:0000000000000000000000000000000000000000',
                'size': file_size,
                'uri': file_uri
            })

    rec['generator'] = {}
    rec['generator']['global_tag'] = ''  # FIXME
    rec['generator']['names'] = []  # FIXME

    rec['license'] = {}
    rec['license']['attribution'] = 'CC0'

    rec['methodology'] = {}
    rec['methodology']['description'] = ''  # FIXME

    rec['note'] = {}
    rec['note']['description'] = 'These simulated datasets correspond to the collision data collected by the CMS experiment in 2012.'

    rec['pileup'] = {}
    rec['pileup']['description'] = '<p>To make these simulated data comparable with the collision data, <a href="/about/CMS-Pileup-Simulation">pile-up events</a> are added to the simulated event in this step.</p>'

    rec['publisher'] = 'CERN Open Data Portal'

    rec['recid'] = str(RECID_INFO[dataset_full_name])

    rec['relations'] = []
    # rec['relations']['title'] = ''  # FIXME
    # rec['relations']['type'] = 'isChildOf'

    rec['run_period'] = run_period

    rec['system_details'] = {}
    rec['system_details']['global_tag'] = global_tag
    rec['system_details']['release'] = release

    rec['title'] = dataset_full_name

    rec['title_additional'] = 'Simulated dataset ' + dataset + ' in AODSIM format for 2012 collision data'

    rec['topic'] = {}
    rec['topic']['category'] = ''  # FIXME
    rec['topic']['source'] = 'CMS collaboration'

    rec['type'] = {}
    rec['type']['primary'] = 'Dataset'
    rec['type']['secondary'] = ['Simulated', ]

    rec['usage'] = {}
    rec['usage']['description'] = 'You can access these data through the CMS Virtual Machine. See the instructions for setting up the Virtual Machine and getting started in'
    rec['usage']['links'] = [
        {
            "description": "How to install the CMS Virtual Machine",
            "url": "/vm/cms/2011"
        },
        {
            "description": "Getting started with CMS open data",
            "url": "/getting-started/cms/2011"
        }
    ]

    rec['validation'] = {}
    rec['validation']['description'] = "The generation and simulation of simulated Monte Carlo data has been validated through general CMS validation procedures."

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
    for line in open('./inputs/mc-datasets.txt', 'r').readlines():
        dataset_full_name = line.strip()
        dataset_index_file_base = get_dataset_index_file_base(dataset_full_name)
        if subprocess.call('ls ./inputs/eos-file-indexes/ | grep -q ' + dataset_index_file_base, shell=True):
            print('[ERROR] Missing EOS information, ignoring dataset ' + dataset_full_name,
                  file=sys.stderr)
        else:
            dataset_full_names.append(dataset_full_name)
    records = create_records(dataset_full_names)
    print_records(records)


if __name__ == '__main__':
    #print(print_records(create_records(['/BBH_HToTauTau_M_125_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'])))
    main()
