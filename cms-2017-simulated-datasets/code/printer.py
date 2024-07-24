#!/usr/bin/env python

"""Print results of the scripts in markdown format"""

from urllib.parse import quote
import datetime
import os

from utils import get_from_deep_json, \
                  populate_doiinfo, \
                  get_doi
from das_json_store import get_das_store_json, \
                           get_generator_parameters, \
                           get_parent_dataset
from mcm_store import get_mcm_dict, \
                      get_global_tag, \
                      get_generator_name, \
                      get_cmsDriver_script, \
                      get_genfragment_url, \
                      get_dataset_energy, \
                      get_prepId_from_das, \
                      get_prepid_from_mcm
from dataset_records import get_conffile_ids, \
    get_cmssw_version


DATASETS_WITH_BOTH_CMSDRIVER = 0
DATASETS_WITH_CMSDRIVER1 = 0
DATASETS_WITH_CMSDRIVER2 = 0
DATASETS_WITH_3CONFFILES = 0
DATASETS_WITH_FULL_PROVENANCE = 0


def print_results(categories,
                  das_dir='./inputs/das-json-store/',
                  mcm_dir='./inputs/mcm-store/',
                  recid_file='./outputs/recid_info.py',
                  doi_file='./outputs/doi-sim.txt',
                  all_information=False):
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
    print('See [#157](https://github.com/cernopendata/data-curation/issues/157) for more context.')
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
                    doi_info = populate_doiinfo(doi_file)
                    print_ancestor_information(title, das_dir, mcm_dir, recid_file, doi_info)

    if all_information:
        print('## Summary')
        print('- datasets with both cmsDriver scripts: {}/{}'.format(DATASETS_WITH_BOTH_CMSDRIVER , total_datasets))
        print('- datasets with 3+ config files: {}/{}'.format(DATASETS_WITH_3CONFFILES, total_datasets))
        print('- datasets with 2 cmsDriver scripts and/or 3+ conffiles: {}/{}'.format(DATASETS_WITH_FULL_PROVENANCE , total_datasets))


def print_ancestor_information(dataset, das_dir, mcm_dir, recid_file, doi_info):
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
    # - LHE stuff?
    # - Data popularity from github.com/katilp/cms-data-popularity
    #   ideally we should make a local cache of that.
    # it would be very nice if this printer script needed not external (non cached) information

    # record ID as in OpenData portal
# TODO move this code to other place, no need to open a file everytime
    RECID_INFO = {}
    _locals = locals()
    exec(open(recid_file, 'r').read(), globals(), _locals)
    RECID_INFO = _locals['RECID_INFO']

    try:
        recid = RECID_INFO[dataset]
        print("    - Record ID: [{recid}]({url})".format(recid=recid, url='http://opendata.cern.ch/record/' + str(recid)))
    except:
        pass

    # DOI
    doi = get_doi(dataset, doi_info)
    if doi:
        print("    - DOI: [{doi}]({url})".format(doi=doi, url='https://doi.org/' + str(doi)))

    # PrepId
    prepid = get_prepId_from_das(dataset, das_dir)
    if not prepid:
        prepid = get_prepid_from_mcm(dataset, mcm_dir)
    if prepid:
            print("    - PrepId: [{prepid}]({url})".format(prepid=prepid, url='https://cms-pdmv.cern.ch/mcm/requests?prepid=' + str(prepid)))

    # global tag & cmssw version
    global_tag = get_global_tag(dataset, mcm_dir)
    cmssw_ver = get_cmssw_version(dataset, das_dir, mcm_dir)
    if global_tag:
        print("    - Global Tag:", global_tag)
    if cmssw_ver:
        print("    - CMSSW version:", cmssw_ver)

    # Energy
    print("    - Collision Energy: ", get_dataset_energy(dataset, mcm_dir), "TeV")

    # Generators
    generators = get_generator_name(dataset, das_dir, mcm_dir)
    if generators:
         print("    - Generators: ", generators)

    # GEN-SIM dataset used to produce the AODSIM
    dataset_json = get_das_store_json(dataset, 'mcm', das_dir)
    input_dataset = get_from_deep_json(dataset_json, 'input_dataset')
    if input_dataset:
        print("    - Input Dataset:", input_dataset)

        input_global_tag = get_global_tag(input_dataset, mcm_dir)
        input_cmssw_ver = get_cmssw_version(input_dataset, das_dir, mcm_dir)
        if input_global_tag:
            print("        - Global Tag:", input_global_tag)
        if input_cmssw_ver:
            print("        - CMSSW version:", input_cmssw_ver)

        gen_fragment = get_genfragment_url(dataset, mcm_dir, das_dir)
        if gen_fragment:
            for url in gen_fragment:
                    print("        - Gen Fragment: [{url}]({url})".format(url=url))


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
    global DATASETS_WITH_BOTH_CMSDRIVER
    global DATASETS_WITH_CMSDRIVER1
    global DATASETS_WITH_CMSDRIVER2

    if cmsDriver1 or cmsDriver2:
        print("    - cmsDriver scripts:")
        if cmsDriver1:
            print('        - GEN-SIM:',  cmsDriver1)
            DATASETS_WITH_CMSDRIVER1 += 1
        if cmsDriver2:
            print('        - RECO-HLT:', cmsDriver2)
            DATASETS_WITH_CMSDRIVER2 += 1

        if cmsDriver1 and cmsDriver2:
            DATASETS_WITH_BOTH_CMSDRIVER += 1

    # python config files
    conffile_ids = get_conffile_ids(dataset, das_dir, mcm_dir)
    parent = get_parent_dataset(dataset, das_dir)
    while parent != '' and parent:
        conffile_ids += get_conffile_ids(parent, das_dir, mcm_dir)
        parent = get_parent_dataset(parent, das_dir)
    global DATASETS_WITH_3CONFFILES
    if conffile_ids:
        print("    - python config scripts: ", conffile_ids)
        if len(conffile_ids) > 2:
            DATASETS_WITH_3CONFFILES += 1

    global DATASETS_WITH_FULL_PROVENANCE
    if (cmsDriver1 and cmsDriver2) or len(conffile_ids) > 2:
        DATASETS_WITH_FULL_PROVENANCE += 1

    # pile up information
    mcm_dict = get_mcm_dict(dataset, mcm_dir)
    if mcm_dict:
        pileup = get_from_deep_json(mcm_dict, 'pileup')
        pileup_dataset = get_from_deep_json(mcm_dict, 'pileup_dataset_name')
        if pileup or pileup_dataset:
            print('    - pile-up:')
            if pileup:
                print('        -', pileup)
            if pileup_dataset:
                print('        -', pileup_dataset)

        notes = get_from_deep_json(mcm_dict, 'notes')
        if notes != None:
            print('    - notes:', notes.replace('\n', '\n        '))  # some notes have several lines, this makes the markdown use them in the same item list
