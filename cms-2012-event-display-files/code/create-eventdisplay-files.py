#!/usr/bin/env python
# noqa: E501


"""
Create CMS 2012 event display files.
"""

import click
import hashlib
import json
import os

RECID_START = 7100


def get_size(afile):
    """Return the size of the configuration file."""
    file_path = './inputs/ig/' + afile
    return os.path.getsize(file_path)


def get_checksum(afile):
    """Return the SHA1 checksum of the configuration file."""
    file_path = './inputs/ig/' + afile
    return hashlib.sha1(open(file_path, 'rb').read()).hexdigest()


def get_recid(dataset_full_name):
    "Return recid of the dataset."
    for afile in ['../cms-2012-collision-datasets/outputs/cms-primary-datasets-Run2012B.json',
                  '../cms-2012-collision-datasets/outputs/cms-primary-datasets-Run2012C.json']:
        records_str = open(afile, 'r').read()
        records = json.loads(records_str)
        for record in records:
            if record['title'] == dataset_full_name:
                return record['recid']
    return ''


def create_record(recid, run_period, dataset):
    """Create record for the given dataset."""

    rec = {}

    global_tag = 'FT_53_LV5_AN1'
    release = 'CMSSW_5_3_32'
    version = '22Jan2013-v1'
    if dataset == 'DoublePhoton' and run_period == 'Run2012C':
        version = '22Jan2013-v2'  # quick fix; should be read from the input file
    dataset_full_name = '/' + dataset + '/' + run_period + '-' + version + '/' + 'AOD'
    year_created = run_period[3:7]
    year_published = '2017'

    rec['abstract'] = {}
    rec['abstract']['description'] = 'Sample event set from ' + dataset_full_name + ' primary dataset in json format readable from the browser-based 3d event display'

    rec['accelerator'] = "CERN-LHC"

    rec['authors'] = []
    rec['authors'].append({
        'name': 'McCauley, Thomas'
    })

    rec['collections'] = ['CMS-Derived-Datasets', ]

    rec['collision_information'] = {}
    rec['collision_information']['energy'] = '8TeV'
    rec['collision_information']['type'] = 'pp'

    rec['date_created'] = year_created
    rec['date_published'] = year_published
    rec['date_reprocessed'] = year_created

    afile = dataset + '_' + run_period + '_0.ig'

    rec['distribution'] = {}
    rec['distribution']['formats'] = ['ig', ]
    rec['distribution']['number_events'] = 25
    rec['distribution']['number_files'] = 1
    rec['distribution']['size'] = get_size(afile)

    # rec['doi'] = ''  # FIXME

    rec['experiment'] = 'CMS'

    rec['files'] = []
    rec['files'].append({
        'checksum': 'sha1:' + get_checksum(afile),
        'size': get_size(afile),
        'uri': 'root://eospublic.cern.ch//eos/opendata/cms/' + run_period + '/' + dataset + '/IG/' + version + '/' + afile
    })

    rec['license'] = {}
    rec['license']['attribution'] = 'CC0'

    rec['methodology'] = {}
    rec['methodology']['description'] = 'These files contain the objects to be displayed with the online event display. No event selection, apart accepting only the validated runs, is applied.'

    rec['note'] = {}
    rec['note']['description'] = 'No selection or quality criteria have been applied on the individual physics objects, apart from accepting only the validated runs.'

    rec['publisher'] = 'CERN Open Data Portal'

    rec['recid'] = str(recid)

    rec['relations'] = []
    rec['relations'].append({
        "recid": get_recid(dataset_full_name),
        "title": dataset_full_name,
        "type": "isChildOf"
    })

    rec['run_period'] = run_period

    rec['system_details'] = {}
    rec['system_details']['global_tag'] = global_tag
    rec['system_details']['release'] = release

    rec['title'] = 'Event display file derived from ' + dataset_full_name

    rec['type'] = {}
    rec['type']['primary'] = 'Dataset'
    rec['type']['secondary'] = ['Derived', ]

    rec['usage'] = {}
    rec['usage']['description'] = 'The data can be accessed from the file menu of the online event display'
    rec['usage']['links'] = [
        {
            "description": "Explore and visualise events",
            "url": "/visualise/events/CMS"
        }
    ]

    return rec


def create_records(recid_start, run_period, datasets):
    """Create records."""
    records = []
    recid = recid_start
    for dataset in datasets:
        records.append(create_record(recid, run_period, dataset))
        recid += 1
    return records


def print_records(records):
    """Print records."""
    for line in json.dumps(records, indent=2, sort_keys=True).split('\n'):
        line = line.rstrip()
        print(line)


@click.command()
@click.option('--run-period',
              required=True,
              help='Run period (Run2012B, Run2012C).')
def main(run_period):
    "Do the job."
    datasets = [
        'BJetPlusX',
        'BTag',
        'Commissioning',
        'DoubleElectron',
        'DoubleMuParked',
        'DoublePhoton',
        'DoublePhotonHighPt',
        'ElectronHad',
        'HTMHTParked',
        'HcalNZS',
        'JetHT',
        'JetMon',
        'MET',
        'MinimumBias',
        'MuEG',
        'MuHad',
        'MuOnia',
        'NoBPTX',
        'PhotonHad',
        'SingleElectron',
        'SingleMu',
        'SinglePhoton',
        'TauParked',
        'TauPlusX',
        'VBF1Parked',
    ]
    if run_period == 'Run2012B':
        records = create_records(RECID_START, run_period, datasets)
        print_records(records)
    elif run_period == 'Run2012C':
        records = create_records(RECID_START + len(datasets), run_period, datasets)
        print_records(records)
    else:
        raise Exception('Run period value %s invalid.' % run_period)


if __name__ == '__main__':
    main()
