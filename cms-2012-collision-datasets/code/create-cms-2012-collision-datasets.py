#!/usr/bin/env python
# noqa: E501


"""
Create CMS 2012 open data release collision datasets.
"""

import json


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


def get_das_store_json(dataset):
    "Return DAS JSON from the DAS JSON Store for the given dataset."
    filepath = './inputs/das-json-store/' + dataset.replace('/', '@') + '.json'
    with open(filepath, 'r') as filestream:
        return json.load(filestream)


def get_number_events(dataset):
    """Return number of events for the dataset."""
    return get_from_deep_json(get_das_store_json(dataset), 'nevents')


def get_number_files(dataset):
    """Return number of files for the dataset."""
    return get_from_deep_json(get_das_store_json(dataset), 'nfiles')


def get_size(dataset):
    """Return size of the dataset."""
    return get_from_deep_json(get_das_store_json(dataset), 'size')


def create_record(recid, run_period, dataset):
    """Create record for the given dataset."""

    rec = {}

    recid_validated_runs = '1002'
    global_tag = 'FT_53_LV5_AN1'
    release = 'CMSSW_5_3_32'
    version = '22Jan2013-v1'
    dataset_full_name = '/' + dataset + '/' + run_period + '-' + version + '/' + 'AOD'
    year_created = run_period[3:7]
    year_published = '2017'

    rec['abstract'] = {}
    if run_period == 'Run2012B':
        rec['abstract']['description'] = dataset + ' primary dataset in AOD format from RunB of 2012. Run period from run number 193833 to 196531.'
    if run_period == 'Run2012C':
        rec['abstract']['description'] = dataset + ' primary dataset in AOD format from RunC of 2012. Run period from run number 198022 to 203742.'

    rec['accelerator'] = "CERN-LHC"

    rec['collaboration'] = {}
    rec['collaboration']['name'] = 'CMS collaboration'
    rec['collaboration']['recid'] = '451'

    rec['collections'] = ['CMS-Primary-Datasets', ]

    rec['collision_information'] = {}
    rec['collision_information']['energy'] = '8TeV'
    rec['collision_information']['type'] = 'pp'

    rec['date_created'] = year_created
    rec['date_published'] = year_published
    rec['date_reprocessed'] = year_created

    rec['distribution'] = {}
    rec['distribution']['formats'] = ['aod', 'root']
    rec['distribution']['number_events'] = get_number_events(dataset_full_name)
    rec['distribution']['number_files'] = get_number_files(dataset_full_name)
    rec['distribution']['size'] = get_size(dataset_full_name)

    rec['doi'] = ''  # FIXME

    rec['experiments'] = 'CMS'

    rec['files'] = []  # FIXME

    rec['license'] = {}
    rec['license']['attribution'] = 'CC0'

    rec['methodology'] = ''  # FIXME

    rec['note'] = {}
    rec['note']['description'] = 'This dataset contains all runs from 2012 RunB/RunC. The list of validated runs, which must be applied to all analyses, can be found in'
    rec['note']['links'] = [{'recid': recid_validated_runs}, ]

    rec['publisher'] = 'CERN Open Data Portal'

    rec['recid'] = recid

    rec['run_period'] = run_period

    rec['system_details'] = {}
    rec['system_details']['global_tag'] = global_tag
    rec['system_details']['release'] = release

    rec['title'] = dataset_full_name

    rec['title_additional'] = dataset + ' primary dataset in AOD format from ' + run_period[0:3] + ' of ' + year_created + ' (' + dataset_full_name + ')'

    rec['type'] = {}
    rec['type']['primary'] = 'Dataset'
    rec['type']['secondary'] = ['Collision', ]

    rec['usage'] = {}
    rec['usage']['description'] = 'You can access these data through the CMS Virtual Machine. See the instructions for setting up the Virtual Machine and getting started in'
    rec['usage']['links'] = [
        {
            "description": "How to install the CMS Virtual Machine",
            "url": "http://opendata.cern.ch/VM/CMS#2011"
        },
        {
            "description": "Getting started with CMS open data",
            "url": "http://opendata.cern.ch/getting-started/CMS#2011"
        }
    ]

    rec['validation'] = {}
    rec['validation']['description'] = "During data taking all the runs recorded by CMS are certified as good for physics analysis if all subdetectors, trigger, lumi and physics objects (tracking, electron, muon, photon, jet and MET) show the expected performance. Certification is based first on the offline shifters evaluation and later on the feedback provided by detector and Physics Object Group experts. Based on the above information, which is stored in a specific database called Run Registry, the Data Quality Monitoring group verifies the consistency of the certification and prepares a json file of certified runs to be used for physics analysis. For each reprocessing of the raw data, the above mentioned steps are repeated. For more information see:",
    rec['validation']['links'] = [
        {
            "description": "CMS data quality monitoring: Systems and experiences",
            "url": "http://iopscience.iop.org/1742-6596/219/7/072020/pdf/1742-6596_219_7_072020.pdf"
        },
        {
            "description": "The CMS Data Quality Monitoring software experience and future improvements",
            "url": "http://cds.cern.ch/record/1631039/files/CR2013_418.pdf"
        },
        {
            "description": "The CMS data quality monitoring software: experience and future prospects",
            "url": "http://iopscience.iop.org/1742-6596/513/3/032024/pdf/1742-6596_513_3_032024.pdf"
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
    records = create_records(6000, 'Run2012B', [
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
        'MuOniaParked',
        'NoBPTX',
        'PhotonHad',
        'SingleElectron',
        'SingleMu',
        'SinglePhoton',
        'TauParked',
        'TauPlusX',
        'VBF1Parked',
    ])
    records.extend(create_records(6026, 'Run2012C', [
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
        'MuOniaParked',
        'NoBPTX',
        'PhotonHad',
        'SingleElectron',
        'SingleMu',
        'SinglePhoton',
        'TauParked',
        'TauPlusX',
        'VBF1Parked',
    ]))
    print_records(records)


if __name__ == '__main__':
    main()
