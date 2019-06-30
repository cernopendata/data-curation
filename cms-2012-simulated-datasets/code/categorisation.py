#!/usr/bin/env python

"""Classify CMS Run2012 datasets into topical categories."""

import datetime
import json
import os
import re
import subprocess
import sys

from urllib.parse import quote


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


def download_config_file(conffile_id):
    """Download config file into config-store."""
    conffile_location = get_conffile_location_from_conffile_id(conffile_id)
    subprocess.check_output([
        'curl',
        '-s',
        '-o',
        'config-store/%s.configFile' % conffile_id,
        '-k',
        '--key',
        'x509up_u102955',
        '--cert',
        'x509up_u102955',
        conffile_location])


def get_from_das(query):
    "Get results from CMS DAS."
    try:
        return json.loads(subprocess.check_output(["dasgoclient",
                                                   "--query",
                                                   query,
                                                   "--json"]))
    except subprocess.CalledProcessError:
        if 'config dataset' in query:
            return json.loads('[]')
        else:
            raise


def get_parent_dataset(dataset):
    """Return parent dataset of the current dataset."""
    return get_from_deep_json(get_from_das('parent dataset=' + dataset),
                              'parent_dataset')


def get_generator_parameters(dataset):
    """Return generator parameters dictionary for given dataset."""
    out = get_from_deep_json(get_from_das('mcm dataset=' + dataset),
                             'generator_parameters')
    if out:
        return out[0]
    else:
        return {}


def get_conffile_ids(dataset):
    """Return location of the configuration files for the dataset."""
    ids = {}
    output = get_from_deep_json(get_from_das('config dataset=' +
                                             dataset),
                                'byoutputdataset')
    if output:
        for someid in output:
            ids[someid] = 1
    return list(ids.keys())


def get_conffile_location_from_conffile_id(conffile_id):
    """Return configuration file location configuration ID."""
    return 'https://cmsweb.cern.ch/couchdb/reqmgr_config_cache/%s/configFile' % conffile_id


def get_conffile_content(conffile_id):
    "Return full content of the configuration file."
    try:
        return open('config-store/' + conffile_id + '.configFile', 'r').read()
    except:
        return ""


def get_conffile_process(conffile_id):
    "Return suitable title of configuration file."
    content = get_conffile_content(conffile_id)
    process = 'UNKNOWN'
    m = re.search(r"""process = cms.Process\(['"]([A-Z]+)['"]\)""", content)
    if m:
        process = m.groups(1)[0]
    return process


def get_conffile_python_filename(conffile_id):
    "Return python_filename from configuration file."
    content = get_conffile_content(conffile_id)
    python_filename = ''
    m = re.search(r"--python_filename (.*?) ", content)
    if m:
        python_filename = m.groups(1)[0]
    return os.path.basename(python_filename)


def get_oldest_ancestor_dataset(dataset):
    """Find oldest ancestor of the dataset."""
    output = dataset
    parent_dataset = get_parent_dataset(output)
    while parent_dataset:
        output = parent_dataset
        print('    - Parent dataset: [%s](%s)' %
              (output,
               'https://cmsweb.cern.ch/das/request?view=list&limit=5&instance=prod%2Fglobal&input=' + quote(output, safe='')))
        generator_parameters = get_generator_parameters(output)
        if generator_parameters:
            print('        - Generator parameters:')
            print('            - Cross section:', generator_parameters.get('cross_section', None))
            print('            - Filter efficiency:', generator_parameters.get('filter_efficiency', None))
            print('            - Filter efficiency error:', generator_parameters.get('filter_efficiency_error', None))
            print('            - Match efficiency:', generator_parameters.get('match_efficiency', None))
            print('            - Match efficiency error:', generator_parameters.get('match_efficiency_error', None))
        for conffile_id in get_conffile_ids(output):
            conffile_location = get_conffile_location_from_conffile_id(conffile_id)
            if not get_conffile_content(conffile_id):
                download_config_file(conffile_id)
            print('        - Configuration file: [%s](%s)' % (conffile_id,
                                                              conffile_location))
            print('            - Process: %s' % get_conffile_process(conffile_id))
            print('            - Python filename: %s' % get_conffile_python_filename(conffile_id))
        parent_dataset = get_parent_dataset(output)
    return output


def read_titles(filename):
    """Read dataset titles from filename."""
    titles = {}
    for line in open(filename).readlines():
        line = line.strip()
        if line:
            titles[line] = 1
    return list(titles.keys())


def categorise_titles(titles):
    """Categorise titles."""
    categories = {
        'B-physics': [],
        'BSM': [],
        'SM Systematic Variations': [],
        'SM Higgs': [],
        'SM Exclusive': [],
        'SM Inclusive': [],
    }
    for title in titles:
        categories[guess_title_category(title)].append(title)
    return categories


def guess_title_category(title):
    """Guess category for the title."""
    title_lower = title.lower()

    if 'lambda' in title_lower or \
       'Bu' in title or \
       'Bd' in title or \
       'jpsi' in title_lower or \
       'upsilon' in title_lower or \
       'bctobspi' in title_lower or \
       'bstokstar' in title_lower or \
       'xibstar0' in title_lower:
        return 'B-physics'

    elif 'higgs2p' in title_lower or \
         'bsm' in title_lower or \
         'graviton2' in title_lower or \
         'higgs0' in title_lower or \
         re.search(r'/add', title_lower) or \
         re.search(r'/cit', title_lower) or \
         re.search(r'/qbh', title_lower) or \
         re.search(r'prime', title_lower) or \
         re.search(r'/gmsb', title_lower) or \
         re.search(r'/atozh', title_lower) or \
         re.search(r'/gluglutoa', title_lower) or \
         re.search(r'graviton', title_lower) or \
         re.search(r'gravitino', title_lower) or \
         re.search(r'htohh', title_lower) or \
         re.search(r'mssm', title_lower) or \
         re.search(r'/qdqd', title_lower) or \
         re.search(r'/qdto', title_lower) or \
         re.search(r'/quto', title_lower) or \
         re.search(r'sms', title_lower) or \
         re.search(r'susy', title_lower) or \
         re.search(r'/axito', title_lower) or \
         re.search(r'/branon', title_lower) or \
         re.search(r'/bstar', title_lower) or \
         re.search(r'/dmz', title_lower) or \
         re.search(r'/darkmatter', title_lower) or \
         re.search(r'/heavygluon', title_lower) or \
         re.search(r'hplus', title_lower) or \
         re.search(r'/lqto', title_lower) or \
         re.search(r'/majorana', title_lower) or \
         re.search(r'/qstar', title_lower) or \
         re.search(r'/radion', title_lower) or \
         re.search(r'/seesaw', title_lower) or \
         re.search(r'/thmtto', title_lower) or \
         re.search(r'/thptto', title_lower) or \
         re.search(r'/ttchichi', title_lower) or \
         re.search(r'anomwtb', title_lower) or \
         re.search(r'/vector1', title_lower) or \
         re.search(r'/vectormix', title_lower) or \
         re.search(r'/wrto', title_lower) or \
         re.search(r'chargino', title_lower) or \
         re.search(r'/monolepton', title_lower) or \
         re.search(r'/spin0plus', title_lower) or \
         re.search(r'/spin2ph', title_lower):
        return 'BSM'

    elif 'matchingup' in title_lower or \
         'matchingdown' in title_lower or \
         'scaleup' in title_lower or \
         'scaledown' in title_lower or \
         re.search(r'tt_weights.*auet2', title_lower) or \
         '_mt' in title_lower or \
         '_mass' in title_lower:
        return 'SM Systematic Variations'

    elif 'higgs' in title_lower or \
         'hto' in title_lower or \
         '_hcontin' in title_lower or \
         '_smhcontin' in title_lower or \
         'vbf_hwwto' in title_lower or \
         'h_m' in title_lower:
        return 'SM Higgs'

    elif 'HT' in title or \
         'Pt' in title or \
         'enriched' in title_lower or \
         'tt_mt1000' in title_lower or \
         'tt_mt800' in title_lower or \
         'tt_mtt-1000' in title_lower or \
         'tt_mtt-700' in title_lower or \
         re.search(r'[0-9]jet', title_lower):
        return 'SM Exclusive'

    return 'SM Inclusive'


def print_results(categories):
    """Print category statistics."""
    for category, titles in categories.items():
        print('')
        print("# %s (%d)" % (category, len(titles)))
        print('')
        titles.sort()
        if titles:
            for title in titles:
                print('')
                print('- Dataset: [%s](%s)' %
                      (title,
                       'https://cmsweb.cern.ch/das/request?view=list&limit=5&instance=prod%2Fglobal&input=' + quote(title, safe='')))
                get_oldest_ancestor_dataset(title)


def main():
    """Do the main job."""

    # detect input directory with filenames containing dataset titles:
    try:
        inputdir = sys.argv[1]
    except IndexError:
        print('Usage: %s <inputdir>' % sys.argv[0])
        sys.exit(1)

    # print About information:
    print('# About')
    print('')
    print('This page is automatically generated from a categorisation script'
          ' that studies CMS MC 2012 datasets. If a dataset is mis-categorised,'
          ' the rules in the categorisation script should be adjusted and'
          ' the script rerun.')
    print('')
    print('See [#1229](https://github.com/cernopendata/opendata.cern.ch/issues/1229)'
          ' for more context.')
    print('')
    print('Generated by @tiborsimko on', datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print('')

    # read dataset titles
    inputdatasets = []
    for dirpath, dummy, inputfilenames in os.walk(inputdir):
        for inputfilename in inputfilenames:
            for datasettitle in read_titles(os.path.join(inputdir,
                                                         inputfilename)):
                if datasettitle not in inputdatasets:
                    inputdatasets.append(datasettitle)

    # categorise datasets and print results:
    print_results(categorise_titles(inputdatasets))


if __name__ == '__main__':
    main()
