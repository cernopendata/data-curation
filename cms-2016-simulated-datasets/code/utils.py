#!/usr/bin/env python

import re
import os
import sys
import subprocess


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
    "Return dataset version."
    return dataset.split('/')[2].split('-', 1)[1]


def get_dataset_format(dataset):
    "Return dataset format."
    return dataset.split('/')[-1]


def get_dataset_year(dataset):
    "Return the data-taking year related to the dataset."
    # cat CMS-2012-mc-datasets.txt | sed -r 's|^/.*/(.*)/.*|\1|g' | cut -d _ -f 1 | sort | uniq
    # FIXME some datasets are getting weird year from this function
    second_name = dataset.split('/')[2].split('_')[0]
    return {
           'Summer12-LowPU2010' : 2010,
           'Fall11-PU' : 2011,
           'Summer11LegDR-PU' : 2011,
           'Summer12' : 2012,
           'RunIIFall15MiniAODv2-PU25nsData2015v1' : 2015,
           'RunIIFall15MiniAODv2-PU25nsData2015v1FSQ' : 2015,
           'RunIIFall15MiniAODv2-PU25nsData2015v1Raw' : 2015,
           'RunIISummer16MiniAODv2-PUMoriond17' : 2016,
           'RunIISummer20UL16NanoAODv9' : 2016,
           'RunIISummer20UL16MiniAODv2' : 2016
           }.get(second_name, 0)


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


def populate_doiinfo(doi_file):
    """Populate DOI_INFO dictionary (dataset -> doi)."""
    doi_info = {}
    for line in open(doi_file, 'r').readlines():
        dataset, doi = line.split()
        doi_info[dataset] = doi

    return doi_info


def get_doi(dataset_full_name, doi_info):
    "Return DOI for the given dataset."
    if dataset_full_name in doi_info.keys():
        return doi_info[dataset_full_name]
    else:
        return None


def get_author_list_recid(dataset):
    "Return recid for author list"
    year = get_dataset_year(dataset)
    return {
           2010: '450',  # FIXME
           2011: '451',
           2012: '453',
           2015: '',  # FIXME
           2016: '',  # FIXME
           }.get(year, '')


def get_recommended_global_tag_for_analysis(dataset):
    "Return recommended global tag for analysis."
    year = get_dataset_year(dataset)
    return {
           2010: 'START42_V17B::All',
           2011: 'START53_LV6A1::All',
           2012: 'START53_V27::All',
           2015: '76X_mcRun2_asymptotic_RunIIFall15DR76_v1',
           2016: '106X_mcRun2_asymptotic_v17',
           }.get(year, '')


def get_recommended_cmssw_for_analysis(dataset):
    "Return recommended CMSSW release for analysis for the main pp data."
    year = get_dataset_year(dataset)
    return {
           2010: 'CMSSW_4_2_8',
           2011: 'CMSSW_5_3_32',
           2012: 'CMSSW_5_3_32',
           2015: 'CMSSW_7_6_7',  
           2016: 'CMSSW_10_6_30',  
           }.get(year, '')
