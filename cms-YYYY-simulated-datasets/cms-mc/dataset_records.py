#!/usr/bin/env python


"""
Create MC 2012 records.
"""

import hashlib
import zlib
import json
import re
import os
import subprocess
import sys
from urllib.request import urlopen

from utils import get_from_deep_json, \
                  populate_doiinfo, \
                  get_dataset_format, \
                  get_dataset_year, \
                  get_author_list_recid, \
                  get_recommended_global_tag_for_analysis, \
                  get_recommended_cmssw_for_analysis, \
                  get_doi
from das_json_store import get_das_store_json, \
                           get_generator_parameters, \
                           get_parent_dataset
from eos_store import XROOTD_URI_BASE, \
                      get_dataset_index_file_base, \
                      get_dataset_location
from mcm_store import get_mcm_dict, \
                      get_global_tag, \
                      get_genfragment_url, \
                      get_generator_name, \
                      get_dataset_energy, \
                      get_cmsDriver_script, \
                      get_cmssw_version
from categorisation import guess_title_category


# Hi Tibor, I commented these `exec` below to not screw the code.
# I also moved some functions from this code to utils.py and das_json_store.py
# this code is not in the interface yet

LINK_INFO = {}
# read LINK_INFO dictionary created by a friendly program ahead of this one:
#exec(open('./outputs/config_files_link_info.py', 'r').read())


def get_number_events(dataset, das_dir):
    """Return number of events for the dataset."""
    number_events = get_from_deep_json(get_das_store_json(dataset, 'dataset', das_dir), 'nevents')
    if number_events:
        return number_events
    return 0


def get_number_files(dataset, das_dir):
    """Return number of files for the dataset."""
    number_files = get_from_deep_json(get_das_store_json(dataset, 'dataset', das_dir), 'nfiles')
    if number_files:
        return number_files
    return 0


def get_size(dataset, das_dir):
    """Return size of the dataset."""
    size = get_from_deep_json(get_das_store_json(dataset, 'dataset', das_dir), 'size')
    if size:
        return size
    return 0


def get_file_size(afile):
    "Return file size of a file."
    return os.path.getsize(afile)


def get_file_checksum(afile):
    """Return the ADLER32 checksum of a file."""
    return zlib.adler32(open(afile, 'rb').read(), 1) & 0xffffffff


def get_dataset(dataset_full_name):
    "Return short dataset name from dataset full name."
    return re.search(r'^/(.*?)/', dataset_full_name).groups()[0]


def get_dataset_version(dataset_full_name):
    "Return dataset version from dataset full name."
    return re.search(r'^.*Summer12_DR53X-(.*)/AODSIM$', dataset_full_name).groups()[0]


def get_dataset_index_files(dataset_full_name, eos_dir):
    """Return list of dataset file information {path,size} for the given dataset."""
    files = []
    dataset_index_file_base = get_dataset_index_file_base(dataset_full_name)
    output = subprocess.getoutput('ls ' + eos_dir + ' | grep ' + dataset_index_file_base)
    for line in output.split('\n'):
        afile = line.strip()
        if afile.endswith('.txt') or afile.endswith('.json'):
            # take only TXT files
            afile_uri = XROOTD_URI_BASE + get_dataset_location(dataset_full_name) + '/file-indexes/' + afile
            afile_size = get_file_size(eos_dir  + afile)
            # FIXME CHANGE THIS checksum TO READ FROM SOMETHING SOMWEHERE
            afile_checksum = '{:#010x}'.format(get_file_checksum(eos_dir + afile)).split('0x')[1]
            files.append((afile_uri, afile_size, afile_checksum))
    return files


def newer_dataset_version_exists(dataset_full_name, all_datasets):
    "Return whether the newer version of dataset exists."

    dataset_full_name_until_version = dataset_full_name[0:dataset_full_name.rfind('-')]
    similar_datasets = []

    for dataset in all_datasets:
        if dataset_full_name_until_version in dataset:
            similar_datasets.append(dataset_full_name_until_version)
    return len(similar_datasets) > 1


def get_conffile_ids(dataset, das_dir):
    """Return location of the configuration files for the dataset."""
    ids = {}
    output = get_from_deep_json(get_das_store_json(dataset, 'config', das_dir),
                                'byoutputdataset')
    if output:
        for someid in output:
            ids[someid] = 1
    return list(ids.keys())


def get_process(afile, conf_dir):
    "Return suitable title of configuration file."
    content = ''
    with open(conf_dir + afile, 'r') as myfile:
        content = myfile.read()
    process = ''
    m = re.search(r"process = cms.Process\(\s?['\"]([A-Z]+)['\"]\s?\)", content)
    if m:
        process = m.groups(1)[0]
    return process


def get_generator_title(afile):
    "Return suitable title of configuration file."
    process = get_process(afile)
    return 'Configuration file for ' + process + ' step ' + get_python_filename(afile)


def get_generator_text(dataset, das_dir, mcm_dir):
    """Return generator text for given dataset."""
    config_ids = get_conffile_ids(dataset, das_dir)
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
    out += '<strong>Step {}</strong>'.format(process)
    out += '<br>Release: {}'.format(get_cmssw_version(dataset, mcm_dir))
    out += '<br>Global tag: {}'.format(get_global_tag(dataset, mcm_dir))
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


def get_all_generator_text(dataset, das_dir, mcm_dir, conf_dir):
    """Return DICT with all information about the generator steps."""
    # FIXME OMG this function is ugly...

    info = {}
    info["description"] = "<p>These data were generated in several steps:</p>"
    info["description"] += """<p><strong>Note</strong><br>
                              To get the exact LHE and generator's parameters, see <a href=\"/docs/cms-mc-production-overview\">CMS Monte Carlo production Overview</a></p>
                           """
    info["steps"] = []

    step = {}

    process = 'RECO-HLT'
    step['type'] = process  # LHE, GEN, SIM, HLT, RECO or any combination of those
    release = get_cmssw_version(dataset, mcm_dir)
    if release:
        step['release'] = release
    global_tag = get_global_tag(dataset, mcm_dir)
    if global_tag:
        step['global_tag'] = global_tag

    cmsdriver_reco_path = get_cmsDriver_script(dataset, mcm_dir)
    step['configuration_files'] = []
    if cmsdriver_reco_path:
        with open(cmsdriver_reco_path) as myfile:
            configuration_files = {}
            configuration_files['type'] = 'cmsDriver script'
            configuration_files['script'] = myfile.read()
            step['configuration_files'].append(configuration_files)

    config_ids = get_conffile_ids(dataset, das_dir)
    # FIXME there's no failure check here... no idea what to do
    if config_ids:
        for config_id in config_ids:
            afile = config_id + '.configFile'
            generator_text = ''
            proc = get_process(afile, conf_dir)
            configuration_files = {}
            configuration_files['title'] = 'conffile'
            configuration_files['process'] = proc
            configuration_files['cms_confdb_id'] = config_id

            step['configuration_files'].append(configuration_files)

    info["steps"].append(step)
    input_dataset = get_parent_dataset(dataset, das_dir)

    if input_dataset:
        step = {}

        process = 'GEN-SIM'
        step['type'] = process
        release = get_cmssw_version(input_dataset, mcm_dir)
        if release:
            step['release'] = release
        global_tag = get_global_tag(input_dataset, mcm_dir)
        if global_tag:
            step['global_tag'] = global_tag

        generator_names = get_generator_name(dataset, das_dir, mcm_dir)
        if generator_names:
            step['generators'] = generator_names

        cmsdriver_path = get_cmsDriver_script(input_dataset, mcm_dir)
        step['configuration_files'] = []
        if cmsdriver_path:
            with open(cmsdriver_path) as myfile:
                configuration_files = {}
                configuration_files['title'] = 'cmsDriver script'
                configuration_files['script'] = myfile.read()
                step['configuration_files'].append(configuration_files)

        gen_fragment = get_genfragment_url(dataset, mcm_dir, das_dir)  # FIXME genfragment store would be better
        if gen_fragment:
            for url in gen_fragment:
                configuration_files = {}
                configuration_files['title'] = 'Genfragment'
                configuration_files['url'] = url
                try:
                    script = urlopen(url).read()  # FIXME get rid of error on 404
                    configuration_files['script'] = script.decode("utf-8")
                except:
                    pass
                step['configuration_files'].append(configuration_files)

        config_ids = get_conffile_ids(input_dataset, das_dir)
        # FIXME there's no failure check here... no idea what to do
        if config_ids:
            for config_id in config_ids:
                afile = config_id + '.configFile'
                generator_text = ''
                proc = get_process(afile, conf_dir)
                configuration_files = {}
                configuration_files['title'] = 'Configuration file'
                configuration_files['process'] = proc
                configuration_files['cms_confdb_id'] = config_id

                step['configuration_files'].append(configuration_files)
        info["steps"].append(step)

    # TODO check for LHE input

    return info


def create_record(dataset_full_name, doi_info, recid_info, eos_dir, das_dir, mcm_dir, conffiles_dir):
    """Create record for the given dataset."""

    rec = {}

    dataset = get_dataset(dataset_full_name)
    dataset_format = get_dataset_format(dataset_full_name)
    year_created   = str(get_dataset_year(dataset_full_name))
    year_published = '2018'  # FIXME get from somewhere, do not hardcode it!
    run_period = ['Run' + year_created + 'A', 'Run' + year_created + 'B']  # FIXME remove the 'A'!!
    global_tag = get_global_tag(dataset_full_name, mcm_dir)
    release    = get_cmssw_version(dataset_full_name, mcm_dir)

    additional_title = 'Simulated dataset ' + dataset + ' in ' + dataset_format + ' format for ' + year_created + ' collision data'

    rec['abstract'] = {}
    rec['abstract']['description'] = '<p>' + additional_title + '.</p>' + \
                                     '<p>See the description of the simulated dataset names in: <a href="/about/CMS-Simulated-Dataset-Names">About CMS simulated dataset names</a>.</p>'

    rec['accelerator'] = "CERN-LHC"

    rec['collaboration'] = {}
    rec['collaboration']['name'] = 'CMS Collaboration'
    rec['collaboration']['recid'] = get_author_list_recid(dataset_full_name)

    rec['collections'] = ['CMS-Simulated-Datasets', ]

    rec['collision_information'] = {}
    rec['collision_information']['energy'] = get_dataset_energy(dataset_full_name, mcm_dir)
    rec['collision_information']['type'] = 'pp'  # FIXME do not hardcode

    # FIXME cross section not working
    # we should try to get the cross section from the parent, and the parent-parent, and so on...
    generator_parameters = get_generator_parameters(dataset_full_name, das_dir)
    if generator_parameters:
        rec['cross_section'] = {}
        rec['cross_section']['value'] = generator_parameters.get('cross_section', None)
        rec['cross_section']['filter_efficiency:'] = generator_parameters.get('filter_efficiency', None)
        rec['cross_section']['filter_efficiency_error:'] = generator_parameters.get('filter_efficiency_error', None)
        rec['cross_section']['match_efficiency:'] = generator_parameters.get('match_efficiency', None)
        rec['cross_section']['match_efficiency error:'] = generator_parameters.get('match_efficiency_error', None)

    rec['date_created'] = year_created
    rec['date_published'] = year_published
    rec['date_reprocessed'] = year_created

    rec['distribution'] = {}
    rec['distribution']['formats'] = [dataset_format.lower(), 'root']
    rec['distribution']['number_events'] = get_number_events(dataset_full_name, das_dir)
    rec['distribution']['number_files'] = get_number_files(dataset_full_name, das_dir)
    rec['distribution']['size'] = get_size(dataset_full_name, das_dir)

    doi = get_doi(dataset_full_name, doi_info)
    if doi:
        rec['doi'] = doi

    rec['experiment'] = 'CMS'

    rec_files = get_dataset_index_files(dataset_full_name, eos_dir)
    if rec_files:
        rec['files'] = []  #TODO if no files: "Dataset available under request"
        for index_type in ['.json', '.txt']:
            index_files = [f for f in rec_files if f[0].endswith(index_type)]
            for file_number, (file_uri, file_size, file_checksum) in enumerate(index_files):
                rec['files'].append({
                    'checksum': 'adler32:' + file_checksum,
                    'description': dataset + dataset_format + ' dataset file index (' + str(file_number + 1) + ' of ' + str(len(index_files)) + ') for access to data via CMS virtual machine',

                    'size': file_size,
                    'type': 'index' + index_type,
                    'uri': file_uri
                })

    rec['license'] = {}
    rec['license']['attribution'] = 'CC0'

    rec['generation'] = get_all_generator_text(dataset_full_name, das_dir, mcm_dir, conffiles_dir)

    rec['note'] = {}
    rec['note']['description'] = 'These simulated datasets correspond to the collision data collected by the CMS experiment in ' + year_created + '.'

    mcm_dict = get_mcm_dict(dataset_full_name, mcm_dir)
    pileup = get_from_deep_json(mcm_dict, 'pileup')  # this is some notes about it.
    pileup_recid = {'2010': None,  # FIXME
                    '2011': 36,
                    '2012': 37}.get(year_created, 0)  # FIXME
    pileup_dataset = get_from_deep_json(mcm_dict, 'pileup_dataset_name')
    if pileup_dataset:
        rec['pileup'] = {}
        rec['pileup']['description'] = '<p>To make these simulated data comparable with the collision data, <a href="/about/CMS-Pileup-Simulation">pile-up events</a> are added to the simulated event in this step.</p>'
        if pileup_recid:
            rec['pileup']['description'] += '<p>The pile-up dataset used is <a href="/record/{recid}">{dataset}</a>.</p>'.format(recid=pileup_recid, dataset=pileup_dataset)
        if pileup:
            rec['pileup']['description'] += '<p>{}</p>'.format(pileup)


    rec['publisher'] = 'CERN Open Data Portal'

    rec['recid'] = str(recid_info[dataset_full_name])

    # rec['relations'] = []
    # rec['relations']['title'] = ''  # FIXME
    # rec['relations']['type'] = 'isChildOf'

    rec['run_period'] = run_period

    # recomended global tag and cmssw release recommended for analysis
    recommended_gt = get_recommended_global_tag_for_analysis(dataset_full_name)
    recommended_cmssw = get_recommended_cmssw_for_analysis(dataset_full_name)
    rec['system_details'] = {}
    rec['system_details']['global_tag'] = recommended_gt
    rec['system_details']['release'] = recommended_cmssw

    rec['title'] = dataset_full_name

    rec['title_additional'] = additional_title

    topic = guess_title_category(dataset_full_name)
    category = topic.split('/')[0]
    subcategory = None
    if len(topic.split('/')) == 2:
        subcategory = topic.split('/')[1]
    rec['categories'] = {}
    rec['categories']['primary'] = category
    if subcategory:
        rec['categories']['secondary'] = [subcategory]
    rec['categories']['source'] = 'CMS Collaboration'

    rec['type'] = {}
    rec['type']['primary'] = 'Dataset'
    rec['type']['secondary'] = ['Simulated', ]

    year_getting_started = {'2010': 2010,
                            '2011': 2011,
                            '2012': 2011}.get(year_created, 2011)
    rec['usage'] = {}
    rec['usage']['description'] = 'You can access these data through the CMS Virtual Machine. See the instructions for setting up the Virtual Machine and getting started in'
    rec['usage']['links'] = [
        {
            "description": "How to install the CMS Virtual Machine",
            "url": "/docs/cms-virtual-machine-{}".format(year_created)
        },
        {
            "description": "Getting started with CMS open data",
            "url": "/docs/cms-getting-started-{}".format(year_getting_started)
        }
    ]

    rec['validation'] = {}
    rec['validation']['description'] = "The generation and simulation of Monte Carlo data has been validated through general CMS validation procedures."
    #rec['validation']['links'] = 'FIXME'

    return rec


def create_records(dataset_full_names, doi_file, recid_file, eos_dir, das_dir, mcm_dir, conffiles_dir):
    """Create records."""

    recid_info = {}
    _locals = locals()
    exec(open(recid_file, 'r').read(), globals(), _locals)
    recid_info = _locals['RECID_INFO']

    doi_info = populate_doiinfo(doi_file)

    records = []
    for dataset_full_name in dataset_full_names:
        records.append(create_record(dataset_full_name, doi_info, recid_info, eos_dir, das_dir, mcm_dir, conffiles_dir))
    return records


def print_records(records):
    """Print records."""
    print('[')
    for (idx, rec) in enumerate(records):
        #print(json.dumps(rec, indent=2, sort_keys=True, ensure_ascii=True))
        print(rec)
        if idx == len(records) - 1:
            pass
        else:
            print(',')
    print(']')


def main(datasets, eos_dir, das_dir, mcm_dir, conffiles_dir, doi_file, recid_file):
    "Do the job."

    #dataset_full_names = []
    #for dataset_full_name in datasets:
    #    if newer_dataset_version_exists(dataset_full_name, datasets):
    #        print('[ERROR] Ignoring older dataset version ' + dataset_full_name,
    #              file=sys.stderr)
    #    else:
    #        dataset_full_names.append(dataset_full_name)

    records = create_records(datasets, doi_file, recid_file, eos_dir, das_dir, mcm_dir, conffiles_dir)
    json.dump(records, indent=2, sort_keys=True, ensure_ascii=True, fp=sys.stdout)
