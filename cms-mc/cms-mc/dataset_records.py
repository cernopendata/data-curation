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

from utils import get_from_deep_json, \
                  populate_doiinfo, \
                  get_doi
from das_json_store import get_das_store_json, \
                           get_parent_dataset
from eos_store import XROOTD_URI_BASE, \
                      get_dataset_index_file_base, \
                      get_dataset_location
from mcm_store import get_mcm_dict, \
                      get_global_tag, \
                      get_cmssw_version

# Hi Tibor, I commented these `exec` below to not screw the code.
# I also moved some functions from this code to utils.py and das_json_store.py
# this code is not in the interface yet

LINK_INFO = {}
# read LINK_INFO dictionary created by a friendly program ahead of this one:
#exec(open('./outputs/config_files_link_info.py', 'r').read())

DOI_INFO = {}


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
    output = subprocess.getoutput('grep ' + dataset_full_name_until_version + ' ./inputs/mc-datasets.txt')
    similar_datasets = output.split('\n')
    similar_datasets.sort()
    return similar_datasets[-1] != dataset_full_name


def get_conffile_ids(dataset):
    """Return location of the configuration files for the dataset."""
    ids = {}
    output = get_from_deep_json(get_das_store_json(dataset, 'config'),
                                'byoutputdataset')
    if output:
        for someid in output:
            ids[someid] = 1
    return list(ids.keys())


def get_generator_text(dataset):
    """Return generator text for given dataset."""
    from create_configfile_records import get_title as get_generator_title
    from create_configfile_records import get_process
    config_ids = get_conffile_ids(dataset)
    process = ''
    if config_ids:
        for config_id in config_ids:
            afile = config_id + '.configFile'
            if process:
                process += ' '
            try:
                process += get_process(afile)
            except:
                print('[ERROR] Missing configuration file ' + config_id, file=sys.stderr)
    if not process:
        return ''
    lhe_info_needed = False
    out = '<p>'
    out += '<strong>Step %s</strong>' % process
    # out += '<br>Release: %s' % 'FIXME'
    # out += '<br>Global tag: %s' % 'FIXME'
    if config_ids:
        for config_id in config_ids:
            afile = config_id + '.configFile'
            generator_text = ''
            try:
                generator_text = get_generator_title(afile)
                out += '<br><a href="/record/%s">%s</a>' % (LINK_INFO[config_id], generator_text)
            except:
                print('[ERROR] Missing configuration file ' + config_id, file=sys.stderr)
            if 'LHE' in generator_text:
                lhe_info_needed = True
    out += '<br>Output dataset: %s' % dataset
    out += '</p>'
    if lhe_info_needed and False:  # FIXME
        out += """
        <p><strong>Note</strong>
        <br>
To get the exact LHE and generator's parameters, see <a href=\"/docs/cms-mc-production-overview\">CMS Monte Carlo production Overview</a>
        </p>
        """
    return """
%s
""" % out


def get_all_generator_text(dataset):
    """Return generator text for given dataset and all its parents."""
    out = '<p>These data were processed in several steps:</p>'
    input_dataset = dataset
    out_blocks = []
    while input_dataset:
        out_blocks.append(get_generator_text(input_dataset))
        input_dataset = get_parent_dataset(input_dataset)
    out_blocks.reverse()
    return out + "".join(out_blocks)


def create_record(dataset_full_name, mcm_dir):
    """Create record for the given dataset."""

    rec = {}

    dataset = get_dataset(dataset_full_name)
    year_created = '2012'  # FIXME get from some database, do not hardcode it!
    year_published = '2017'  # FIXME get from some database, do not hardcode it!
    run_period = '2012A-2012D'  # FIXME get from some database, do not hardcode it!
    global_tag = get_global_tag(dataset_full_name, mcm_dir) or 'START53'
    release = get_cmssw_version or 'CMSSW_5_3_X'

    RECID_INFO = {}
    _locals = locals()
    exec(open(recid_file, 'r').read(), globals(), _locals)
    RECID_INFO = _locals['RECID_INFO']

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

    rec['doi'] = get_doi(dataset_full_name)

    rec['experiment'] = 'CMS'

    rec['files'] = []
    rec_files = get_dataset_index_files(dataset_full_name)
    for index_type in ['.json', '.txt']:
        index_files = [f for f in rec_files if f[0].endswith(index_type)]
        for file_number, (file_uri, file_size, file_checksum) in enumerate(index_files):
            rec['files'].append({
                'checksum': 'sha1:' + file_checksum,
                'description': dataset + ' AOD dataset file index (' + str(file_number + 1) + ' of ' + str(len(index_files)) + ') for access to data via CMS virtual machine',

                'size': file_size,
                'type': 'index' + index_type,
                'uri': file_uri
            })

    rec['generator'] = {}
    rec['generator']['global_tag'] = ''  # FIXME
    rec['generator']['names'] = []  # FIXME

    rec['license'] = {}
    rec['license']['attribution'] = 'CC0'

    rec['methodology'] = {}
    rec['methodology']['description'] = get_all_generator_text(dataset_full_name)

    rec['note'] = {}
    rec['note']['description'] = 'These simulated datasets correspond to the collision data collected by the CMS experiment in 2012.'  # FIXME

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

    #rec['topic'] = {}
    #rec['topic']['category'] = ''  # FIXME
    #rec['topic']['source'] = 'CMS collaboration'

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


def create_records(dataset_full_names, mcm_dir):
    """Create records."""
    records = []
    for dataset_full_name in dataset_full_names:
        records.append(create_record(dataset_full_name, mcm_dir))
    return records


def print_records(records):
    """Print records."""
    print('[')
    for (idx, rec) in enumerate(records):
        #print(json.dumps(rec, indent=2, sort_keys=True))
        print(rec)
        if idx == len(records) - 1:
            pass
        else:
            print(',')
    print(']')


def main(datasets = [], mcm_dir = './inputs/mcm-store' , doi_file = './inputs/doi-sim.txt'):
    "Do the job."
    populate_doiinfo(doi_file)
    #dataset_full_names = []
    #for line in open('./inputs/mc-datasets.txt', 'r').readlines():
    #    dataset_full_name = line.strip()
    #    dataset_index_file_base = get_dataset_index_file_base(dataset_full_name)
    #    if subprocess.call('ls ./inputs/eos-file-indexes/ | grep -q ' + dataset_index_file_base, shell=True):
    #        print('[ERROR] Missing EOS information, ignoring dataset ' + dataset_full_name,
    #              file=sys.stderr)
    #    elif newer_dataset_version_exists(dataset_full_name):
    #        print('[ERROR] Ignoring older dataset version ' + dataset_full_name,
    #              file=sys.stderr)
    #    else:
    #        dataset_full_names.append(dataset_full_name)
    #records = create_records(dataset_full_names, mcm_dir)
    #print_records(records)
    print(print_records(create_records(['/BBH_HToTauTau_M_125_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM'], mcm_dir)))


if __name__ == '__main__':
    main([], mcm_dir, doi_file)
