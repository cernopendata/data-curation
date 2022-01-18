#!/usr/bin/env python


"""
Create MC YYYY records.
"""

import hashlib
import json
import os
import re
import subprocess
import sys
import threading
import zlib
from datetime import datetime as dt
from time import sleep

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from categorisation import guess_title_category
from das_json_store import (get_cmssw_version_from_das, get_das_store_json,
                            get_generator_parameters, get_parent_dataset)
from eos_store import (XROOTD_URI_BASE, get_dataset_index_file_base,
                       get_dataset_location)
from mcm_store import (get_cmsDriver_script, get_cmssw_version_from_mcm,
                       get_conffile_ids_from_mcm, get_dataset_energy,
                       get_generator_name, get_generator_parameters_from_mcm,
                       get_genfragment_url, get_global_tag, get_mcm_dict,
                       get_parent_dataset_from_mcm, get_pileup_from_mcm)
from utils import (get_author_list_recid, get_dataset_format, get_dataset_year,
                   get_doi, get_from_deep_json,
                   get_recommended_cmssw_for_analysis,
                   get_recommended_global_tag_for_analysis, populate_doiinfo)

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

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


def get_conffile_ids(dataset, das_dir, mcm_dir):
    """Return location of the configuration files for the dataset from either McM or DAS."""
    ids = get_conffile_ids_from_mcm(dataset, mcm_dir)
    if not ids:
        ids = get_conffile_ids_from_das(dataset, das_dir, mcm_dir)
    if ids:
        ids.sort()
    return ids


def get_conffile_ids_from_das(dataset, das_dir, mcm_dir):
    """Return location of the configuration files for the dataset from DAS."""
    ids = {}
    output = get_from_deep_json(get_das_store_json(dataset, 'config', das_dir),
                                'byoutputdataset')
    if output:
        for someid in output:
            ids[someid] = 1
    else:
        print("Error: No config id found from DAS config for " +dataset, file=sys.stderr )
    return list(ids.keys())


def get_process(afile, conf_dir):
    "Return suitable title of configuration file."
    content = ''
    try:
        with open(conf_dir  + '/' + afile, 'r') as myfile:
            content = myfile.read()
    except FileNotFoundError:
        print ( "Error: '" + conf_dir  + '/' + afile + "' No such file")
    process = ''
    m = re.search(r"process = cms.Process\(\s?['\"]([A-Z0-9]+)['\"]\s?(\)|,)", content)
    if m:
        process = m.groups(1)[0]
    if process == 'PAT':
        process = "MINIAODSIM"
    return process


def get_cmssw_version(dataset, das_dir, mcm_dir):
    """Return CMSSW version either from McM or from DAS."""
    release = get_cmssw_version_from_mcm(dataset, mcm_dir)
    if not release:
        release = get_cmssw_version_from_das(dataset, das_dir)
    return release


def get_globaltag_from_conffile(afile, conf_dir):
    "Return global tag information from the configuration file."
    content = ''
    try:
        with open(conf_dir + '/' + afile, 'r') as myfile:
            content = myfile.read()
    except FileNotFoundError:
        print ( "Error: '" + conf_dir  + '/' + afile + "' No such file")
    globaltag = ''
    m = re.search(r"globaltag = cms.string\(\s?['\"](.+)['\"]\s?\)", content)
    if m:
        globaltag = m.groups(1)[0]
    else:
        m = re.search(r"process.GlobalTag.globaltag\s?=\s?['\"](.+)['\"]", content)
        if m:
            globaltag = m.groups(1)[0]
    return globaltag


def get_all_generator_text(dataset, das_dir, mcm_dir, conf_dir, recid):
    """Return DICT with all information about the generator steps."""

    info = {}
    info["description"] = "<p>These data were generated in several steps (see also <a href=\"/docs/cms-mc-production-overview\">CMS Monte Carlo production overview</a>):</p>"
    info["steps"] = []
    input_dataset = dataset
    while input_dataset:
        step = {}
        process = ''
        step['output_dataset'] = input_dataset
        release = get_cmssw_version(input_dataset, das_dir, mcm_dir)
        if release:
            step['release'] = release
        global_tag = get_global_tag(input_dataset, mcm_dir)
        if global_tag:
            step['global_tag'] = global_tag

        cmsdriver_path = get_cmsDriver_script(input_dataset, mcm_dir)
        step['configuration_files'] = []
        if cmsdriver_path:
            with open(cmsdriver_path) as myfile:
                configuration_files = {}
                configuration_files['title'] = 'Production script'
                configuration_files['script'] = myfile.read()
                if configuration_files:
                    step['configuration_files'].append(configuration_files)

        generator_names = get_generator_name(input_dataset, das_dir, mcm_dir)
        if generator_names:
            step['generators'] = generator_names
        
        if input_dataset.endswith('/LHE') or input_dataset.endswith('/SIM') or input_dataset.endswith('RAW') or input_dataset.endswith('/GEN-SIM'): # we get generator parameters for LHE and SIM datasets
            step_generator_parameters= get_step_generator_parameters(input_dataset, das_dir, mcm_dir, recid)
            if step_generator_parameters:
                step['configuration_files'].extend(step_generator_parameters)

        config_ids = get_conffile_ids(input_dataset, das_dir, mcm_dir)
        if config_ids:
            for config_id in config_ids:
                afile = config_id + '.configFile'
                proc = get_process(afile, conf_dir)
                if process:
                    process += " " + proc
                else:
                    process += proc
                configuration_files = {}
                configuration_files['title'] = 'Configuration file'
                configuration_files['process'] = proc
                configuration_files['cms_confdb_id'] = config_id
                globaltag = get_globaltag_from_conffile(afile, conf_dir)
                if not 'global_tag' in step:
                    step['global_tag'] = globaltag

                step['configuration_files'].append(configuration_files)

        # if we couldn't detect process type from config files, try guessing
        # via extension:
        if not process:
            if input_dataset.endswith('/LHE'):
                process = 'LHE'
            elif input_dataset.endswith('/SIM'):
                process = 'SIM'
            elif input_dataset.endswith('/GEN-SIM'):
                process = 'SIM'
        #if process == 'LHE':
        #    step['note'] = "To get the exact generator parameters, please see <a href=\"/docs/cms-mc-production-overview#finding-the-generator-parameters\">Finding the generator parameters</a>."
        step['type'] = process

        # For cases where SIM and LHE steps are done together
        datatier = get_from_deep_json(get_mcm_dict(input_dataset,mcm_dir),'datatier')
        if datatier ==  ["GEN-SIM", "LHE"]:
            step['type'] = "LHE SIM"
            for i, configuration_files in enumerate(step['configuration_files']):
                if configuration_files['title'] == 'Generator parameters':
                    step['configuration_files'][i]['title']='Hadronizer parameters'
            # extend its LHE generator paramters
            step_generator_parameters= get_step_generator_parameters(input_dataset, das_dir, mcm_dir, recid, 1) # Force LHE
            if step_generator_parameters:
                step['configuration_files'].extend(step_generator_parameters)
                
        info["steps"].append(step)

        # find parent dataset, first via DAS, then via McM
        input_dataset_das = get_parent_dataset(input_dataset, das_dir)
        input_dataset_mcm = get_parent_dataset_from_mcm(input_dataset, das_dir, mcm_dir)
        if input_dataset_mcm == 'Default':  # workaround McM bugs
            input_dataset_mcm = ''
        if input_dataset_das:
            input_dataset = input_dataset_das
        else:
            input_dataset = input_dataset_mcm

    # reverse order of steps for provenance
    info['steps'].reverse()

    # post-generation fix: if we have LHE step, let's modify the configuration file titles for other steps:
    lhe_present = False
    for step in info['steps']:
        if lhe_present:
            for configuration_file in step.get('configuration_files'):
                if configuration_file['title'] == 'Generator parameters':
                    configuration_file['title'] = 'Hadronizer parameters'
        if 'LHE' in step['type']:
            lhe_present = True

    # post-generation fix: keep generators only for the first step, remove from others:
    generators_present = False
    for step in info['steps']:
        if generators_present:
            if 'generators' in step:
                del(step['generators'])
        else:
            if 'generators' in step:
                generators_present = True
                    
    return info


def create_record(dataset_full_name, doi_info, recid_info, eos_dir, das_dir, mcm_dir, conffiles_dir):
    """Create record for the given dataset."""

    rec = {}

    dataset = get_dataset(dataset_full_name)
    dataset_format = get_dataset_format(dataset_full_name)
    year_created   = str(get_dataset_year(dataset_full_name))
    year_published = '2021'  # FIXME get from somewhere, do not hardcode it!
    run_period = ['Run2015C', 'Run2015D']  # FIXME Hardcoded!!
    global_tag = get_global_tag(dataset_full_name, mcm_dir)
    release    = get_cmssw_version(dataset_full_name, das_dir, mcm_dir)

    additional_title = 'Simulated dataset ' + dataset + ' in ' + dataset_format + ' format for ' + year_created + ' collision data'

    rec['abstract'] = {}
    rec['abstract']['description'] = '<p>' + additional_title + '.</p>' + \
                                     '<p>See the description of the simulated dataset names in: <a href="/about/CMS-Simulated-Dataset-Names">About CMS simulated dataset names</a>.</p>' + \
                                     '<p>These simulated datasets correspond to the collision data collected by the CMS experiment in ' + year_created + '.</p>'

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
    generator_parameters = get_generator_parameters_from_mcm(dataset_full_name, mcm_dir)
    if generator_parameters:
        rec['cross_section'] = {}
        rec['cross_section']['value'] = generator_parameters.get('cross_section', None)
        rec['cross_section']['filter_efficiency:'] = generator_parameters.get('filter_efficiency', None)
        rec['cross_section']['filter_efficiency_error:'] = generator_parameters.get('filter_efficiency_error', None)
        rec['cross_section']['match_efficiency:'] = generator_parameters.get('match_efficiency', None)
        rec['cross_section']['match_efficiency error:'] = generator_parameters.get('match_efficiency_error', None)

    rec['date_created'] = [year_created]
    rec['date_published'] = year_published
    rec['date_reprocessed'] = year_created

    rec['distribution'] = {}
    rec['distribution']['formats'] = [dataset_format.lower(), 'root']
    rec['distribution']['number_events'] = get_number_events(dataset_full_name, das_dir)
    rec['distribution']['number_files'] = get_number_files(dataset_full_name, das_dir)
    rec['distribution']['size'] = get_size(dataset_full_name, das_dir)

    #if not dataset_full_name in doi_info: FIXME
    #    rec['distribution']['availability'] = 'ondemand'

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

    rec['methodology'] = get_all_generator_text(dataset_full_name, das_dir, mcm_dir, conffiles_dir, recid_info[dataset_full_name])


    pileup_dataset_name= ''
    parent= dataset_full_name
    while parent != '' and parent and not pileup_dataset_name:
        pileup_dataset_name= get_pileup_from_mcm(parent, mcm_dir)
        parent= get_parent_dataset(parent, das_dir) or get_parent_dataset_from_mcm(parent, das_dir, mcm_dir)
    
    pileup_dataset_recid = {
        '/MinBias_TuneZ2_7TeV-pythia6/Summer11Leg-START53_LV4-v1/GEN-SIM': 36, # 2011
        '/MinBias_TuneZ2star_8TeV-pythia6/Summer12-START50_V13-v3/GEN-SIM': 37, # 2012
        '/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIISummer15GS-MCRUN2_71_V1-v2/GEN-SIM': 22314, # 2015
        #'/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIISummer15GS-magnetOffBS0T_MCRUN2_71_V1-v1/GEN-SIM': {recid}, # 2015 TODO
        '/MinBias_TuneCP5_13TeV-pythia8/RunIIFall18GS-IdealGeometry_102X_upgrade2018_design_v9-v1/GEN-SIM': 12302 # 2018
    }.get(pileup_dataset_name, 0)


    if pileup_dataset_name:
        rec['pileup'] = {}
        if pileup_dataset_recid:
            rec['pileup']['description'] = "<p>To make these simulated data comparable with the collision data, <a href=\"/docs/cms-guide-pileup-simulation\">pile-up events</a> are added to the simulated event in this step.</p>"
            rec['pileup']['links'] = [ 
                {
                    "recid": str(pileup_dataset_recid),
                    "title": pileup_dataset_name
                }
            ]
        else:
            rec['pileup']['description'] = "<p>To make these simulated data comparable with the collision data, <a href=\"/docs/cms-guide-pileup-simulation\">pile-up events</a> from the dataset <code>"\
                                            + pileup_dataset_name\
                                            + "</code> are added to the simulated event in this step.</p>"

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
    rec['system_details']['global_tag'] = "76X_mcRun2_asymptotic_RunIIFall15DR76_v1" # FIXME
    rec['system_details']['release'] = "CMSSW_7_6_7" # FIXME

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
    rec['usage']['description'] = "You can access these data through the CMS Open Data container or the CMS Virtual Machine. See the instructions for setting up one of the two alternative environments and getting started in" # FIXME
    rec['usage']['links'] = [  # FIXME
        {
          "description": "Running CMS analysis code using Docker", 
          "url": "/docs/cms-guide-docker"
        }, 
        {
          "description": "How to install the CMS Virtual Machine", 
          "url": "/docs/cms-virtual-machine-2015"
        }, 
        {
          "description": "Getting started with CMS open data", 
          "url": "/docs/cms-getting-started-2015"
        }
    ]

    rec['validation'] = {}
    rec['validation']['description'] = "The generation and simulation of Monte Carlo data has been validated through general CMS validation procedures."
    #rec['validation']['links'] = 'FIXME'

    return rec

def create(dataset, doi_info, recid_info, eos_dir, das_dir, mcm_dir, conffiles_dir, records_dir):
    filepath= records_dir  + "/" + dataset.replace('/', '@') + '.json'
    if os.path.exists(filepath) and os.stat(filepath).st_size != 0:
        print("==> " + dataset + "\n==> Already exist. Skipping...\n")
        return
        
    Record= create_record(dataset, doi_info, recid_info, eos_dir, das_dir, mcm_dir, conffiles_dir)

    with open(filepath, 'w') as file:
        json.dump(Record, indent=2, sort_keys=True, ensure_ascii=True, fp=file)



def create_records(dataset_full_names, doi_file, recid_file, eos_dir, das_dir, mcm_dir, conffiles_dir, records_dir):
    """Create records."""

    recid_info = {}
    _locals = locals()
    exec(open(recid_file, 'r').read(), globals(), _locals)
    recid_info = _locals['RECID_INFO']

    doi_info = populate_doiinfo(doi_file)

    records = []
    for dataset_full_name in dataset_full_names:
        t= threading.Thread(target=create, args=(dataset_full_name, doi_info, recid_info, eos_dir, das_dir, mcm_dir, conffiles_dir, records_dir))
        t.start()
        while threading.activeCount() >= 20 :
            sleep(0.5)  # run 20 parallel 
            
        #records.append(create_record(dataset_full_name, doi_info, recid_info, eos_dir, das_dir, mcm_dir, conffiles_dir))
    #return records


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

    records_dir= "./outputs/records-" + dt.now().strftime("%Y-%m")
    os.makedirs(records_dir, exist_ok=True)

    create_records(datasets, doi_file, recid_file, eos_dir, das_dir, mcm_dir, conffiles_dir, records_dir)

    #records = create_records(datasets, doi_file, recid_file, eos_dir, das_dir, mcm_dir, conffiles_dir)
    #json.dump(records, indent=2, sort_keys=True, ensure_ascii=True, fp=sys.stdout)


def get_step_generator_parameters(dataset, das_dir, mcm_dir, recid, force_lhe=0):
    configuration_files = {}
    if dataset[-4:] == '/LHE' or force_lhe:
        mcdb_id= get_from_deep_json(get_mcm_dict(dataset,mcm_dir), "mcdb_id") or 0
        if mcdb_id > 1:
            configuration_files['title'] = 'Generator parameters'
            configuration_files['url'] = "/eos/opendata/cms/lhe_generators/2015-sim/mcdb/{mcdb_id}_header.txt".format(mcdb_id=mcdb_id)    
            return [configuration_files]        
        else:       
            dir='./lhe_generators/2015-sim/gridpacks/' + str(recid) + '/'  # FIXME localy
            files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
            confarr=[]
            for f in files:
                configuration_files['title'] = 'Generator parameters: ' + f
                configuration_files['url'] = '/eos/opendata/cms/lhe_generators/2015-sim/gridpacks/' + str(recid) + '/'  + f
                confarr.append(configuration_files.copy())
            return confarr
    else:
        gen_fragment = get_genfragment_url(dataset, mcm_dir, das_dir)
        if gen_fragment:
            for url in gen_fragment:
                configuration_files = {}
                configuration_files['title'] = 'Generator parameters'
                configuration_files['url'] = url
                try:
                    script = requests.get(url, verify=False).text
                    configuration_files['script'] = script
                    if configuration_files:
                        return [configuration_files]
                except:
                    pass

