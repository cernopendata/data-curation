#!/usr/bin/env python

"""Print results of the scripts in markdown format"""

from urllib.parse import quote
import datetime
import os

from utils import get_from_deep_json
from das_json_store import get_das_store_json
from mcm_store import get_mcm_dict, \
                      get_global_tag, \
                      get_cmssw_version


def print_results(categories, das_dir='./inputs/das-json-store/', mcm_dir='./inputs/mcm-store/', all_information=False):
    """Print category statistics."""

    # print About information:
    print('# Categorisation for MC datasets')
    print('')
    print('## About')
    print('')
    print('This page is automatically generated from a categorisation script'
          ' that studies CMS MC datasets. If a dataset is mis-categorised,'
          ' the rules in the categorisation script should be adjusted and'
          ' the script rerun.')
    print('')
    print('See [#1229](https://github.com/cernopendata/opendata.cern.ch/issues/1229)'
          ' and [this page](https://demo.codimd.org/s/BkoBknkqQ#)'
          ' for more context.')
    print('')
    print('Generated on', datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print('')

    # print overview of results
    total_datasets = 0
    for items in categories.values():
        total_datasets += len(items)
    print('{} datasets in total:\n'.format(total_datasets))
    print('| # | Category |')
    print('|--:|:---------|')
    for category, titles in categories.items():
        print("| {}\t| `{}` |".format(len(titles), category))

    # print everything in their respective category
    print('')
    print('## Categories and Datasets')
    for category, titles in categories.items():
        print('')
        print("### %s (%d)" % (category, len(titles)))
        titles.sort()
        if titles:
            for title in titles:
                print('')
                print('- Dataset: [%s](%s)' %
                      (title,
                       'https://cmsweb.cern.ch/das/request?view=list&limit=5&instance=prod%2Fglobal&input=' + quote(title, safe='')))
                if all_information:
                    print_ancestor_information(title, das_dir, mcm_dir)


def print_ancestor_information(dataset, das_dir, mcm_dir):
    "All the information we have so far"
    # everything should be a sublist item (4 spaces of indentation):
    # - dataset_name
    #     - info

    # TODO add to this function:
    # - config files present
    #   - step GEN
    #   - step RECO
    #   - step HLT
    # - gen_parameters:
    #   - cross section from XSECDB.
    #     see github issue opendata.cern.ch#1137
    #     ideally we should make a local cache of that.
    #   - genfragment
    # - LHE stuff?
    # - Data popularity from github.com/katilp/cms-data-popularity
    #   ideally we should make a local cache of that.
    # it would be very nice if this printer script needed not external (non cached) information

    # global tag & cmssw version
    global_tag = get_global_tag(dataset, mcm_dir)
    cmssw_ver = get_cmssw_version(dataset, mcm_dir)
    if global_tag:
    print("    - Global Tag:", global_tag)
    if cmssw_ver:
    print("    - CMSSW version:", cmssw_ver)

    # GEN-SIM dataset used to produce the AODSIM
    dataset_json = get_das_store_json(dataset, 'mcm', das_dir)
    input_dataset = get_from_deep_json(dataset_json, 'input_dataset')
    if input_dataset:
        print("    - Input Dataset:", input_dataset)

        input_global_tag = get_global_tag(input_dataset, mcm_dir)
        input_cmssw_ver = get_cmssw_version(input_dataset, mcm_dir)
        if input_global_tag:
        print("        - Global Tag:", input_global_tag)
        if input_cmssw_ver:
        print("        - CMSSW version:", input_cmssw_ver)

    # gen parameters of input dataset
    generator_parameters = get_generator_parameters(dataset, das_dir)
    if generator_parameters:
        print('        - Generator parameters:')
        print('            - Cross section:', generator_parameters.get('cross_section', None))
        print('            - Filter efficiency:', generator_parameters.get('filter_efficiency', None))
        print('            - Filter efficiency error:', generator_parameters.get('filter_efficiency_error', None))
        print('            - Match efficiency:', generator_parameters.get('match_efficiency', None))
        print('            - Match efficiency error:', generator_parameters.get('match_efficiency_error', None))

    # mcm scripts with cmsDriver instructions
    cmsDriver1 = get_cmsDriver_script(input_dataset, mcm_dir)
    cmsDriver2 = get_cmsDriver_script(dataset, mcm_dir)
    if cmsDriver1 or cmsDriver2:
        print("    - cmsDriver scripts:")
        if cmsDriver1:
            print('        - GEN-SIM:',  cmsDriver1)
        if cmsDriver2:
            print('        - RECO-HLT:', cmsDriver2)

    # pile up information
    mcm_dict = get_mcm_dict(dataset, mcm_dir)
    if mcm_dict:
        print('    - pile-up:')
        print('        -', get_from_deep_json(mcm_dict, 'pileup'))
        print('        -', get_from_deep_json(mcm_dict, 'pileup_dataset_name'))

        notes = get_from_deep_json(mcm_dict, 'notes')
        if notes != None:
            print('    - notes:', notes.replace('\n', '\n        '))  # some notes have several lines, this makes the markdown use them in the same item list


def get_generator_parameters(dataset, das_dir):
    """Return generator parameters dictionary for given dataset."""
    # TODO get from mcm store instead?
    # and/or from xsecDB
    out = get_from_deep_json(get_das_store_json(dataset, 'mcm', das_dir),
                             'generator_parameters')
    if out:
        return out[0]
    else:
        return {}


def get_cmsDriver_script(dataset, mcm_dir):
    """Return path to cmsDriver script for that dataset"""
    if dataset == None:
        return None

    script = mcm_dir + '/scripts/' + dataset.replace('/', '@') + '.sh'
    if os.path.exists(script):
        return script
    else:
        return None
