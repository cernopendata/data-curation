#!/usr/bin/env python


"""
Create MC 2016 records.
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
from das_json_store import (get_das_store_json, get_parent_dataset)
from eos_store import (XROOTD_URI_BASE, get_dataset_index_file_base,
                       get_dataset_location)
from mcm_store import (get_cmsDriver_script, get_cmssw_version_from_mcm,
                       get_conffile_ids_from_mcm, get_dataset_energy,
                       get_data_processing_year,
                       get_generator_name, get_generator_parameters_from_mcm,
                       get_genfragment_url, get_global_tag, get_mcm_dict,
                       get_parent_dataset_from_mcm, get_pileup_from_mcm,
                       get_output_dataset_from_mcm)
from utils import (get_author_list_recid, get_dataset_format, get_dataset_year,
                   get_dataset_runperiod, get_doi, get_from_deep_json,
                   get_recommended_cmssw_for_analysis,
                   get_recommended_global_tag_for_analysis, populate_doiinfo)

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

recid_freerange_start = 30000 #FIXME not in use, using inputs/recid_info.py for now
recommended_gt = "106X_mcRun2_asymptotic_v17"
recommended_cmssw = "CMSSW_10_6_30"
collision_energy = "13TeV"
collision_type = "pp"
year_published = "2024"

RECOMMENDED_IMAGES_FOR_NANOAOD_DESCRIPTION = """<p>NANOAODSIM datasets are in the <a href="https://root.cern.ch/">ROOT</a> tree format and their analysis does not require the use of CMSSW or CMS open data environments. They can be analysed with common ROOT and Python tools.<p>"""
RECOMMENDED_IMAGES_FOR_NANOAOD = [
    {
        "name": "gitlab-registry.cern.ch/cms-cloud/root-vnc",
        "registry": "gitlab",
    },
    {
        "name": "gitlab-registry.cern.ch/cms-cloud/python-vnc",
        "registry": "gitlab",
    },
]

USAGE_FOR_NANOAOD_DESCRIPTION = """You can access these data through XRootD protocol or direct download, and they can be analysed with common ROOT and Python tools. See the instructions for getting started in"""
USAGE_FOR_NANOAOD_LINKS = [
    {
        "description": "Using Docker containers",
        "url": "/docs/cms-guide-docker#nanoaod",
    },
    {
        "description": "Getting started with CMS NanoAOD",
        "url": "/docs/cms-getting-started-nanoaod",
    },
]

LINK_INFO = {}

CONTAINERIMAGES_CACHE = {}

MININANORELATION_CACHE = {}

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
    return re.search(r'^.*RunIISummer20UL16.*?-(.*)/(MINI|NANO)AODSIM$', dataset_full_name).groups()[0]


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
    #if process == 'PAT':
    #    process = "MINIAODSIM"
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

# TODO when we are doing MINI, then exclude the NANO step so that it does not appear
# TODO move generator cards to the root and exclude LOG.txt when assembling list

def get_all_generator_text(dataset, das_dir, mcm_dir, conf_dir, recid_info):
    """Return DICT with all information about the generator steps."""

    # For MiniAODSIM, find the corresponding Nano and use that information
    if dataset.endswith('MINIAODSIM'):
        dataset = MININANORELATION_CACHE[dataset]

    recid = recid_info[dataset]
    info = {}
    info["description"] = "<p>These data were generated in several steps (see also <a href=\"/docs/cms-mc-production-overview\">CMS Monte Carlo production overview</a>):</p>"
    info["steps"] = []
    path = mcm_dir + '/chain/' + dataset.replace('/', '@')
    step_dirs = os.listdir(path)
    for step_dir in step_dirs:
        mcm_step_dir = path + '/' + step_dir
        input_dataset = dataset
        step = {}
        process = ''
        output_dataset = get_output_dataset_from_mcm(dataset, mcm_step_dir)
        if output_dataset:
            step['output_dataset'] = output_dataset[0]
        release = get_cmssw_version_from_mcm(dataset, mcm_step_dir)
        if release:
            step['release'] = release
        global_tag = get_global_tag(dataset, mcm_step_dir)
        if global_tag:
            step['global_tag'] = global_tag

        cmsdriver_path = get_cmsDriver_script(dataset, mcm_step_dir)
        step['configuration_files'] = []
        if cmsdriver_path:
            with open(cmsdriver_path) as myfile:
                configuration_files = {}
                configuration_files['title'] = 'Production script'
                configuration_files['script'] = myfile.read()
                if configuration_files:
                    step['configuration_files'].append(configuration_files)

        generator_names = get_generator_name(dataset, mcm_step_dir)
        if generator_names:
            step['generators'] = generator_names

        m = re.search('-(.+?)-', step_dir)
        if m:
            step_name = m.group(1)
        if step_name.endswith('GEN'): # get generator parameters for LHEGEN and GEN datasets
            step_generator_parameters= get_step_generator_parameters(dataset, mcm_step_dir, recid)
            if step_generator_parameters:
                step['configuration_files'].extend(step_generator_parameters)

        config_ids = get_conffile_ids_from_mcm(dataset, mcm_step_dir)
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

        step['type'] = process

        # Extend LHE steps
        if step_name.endswith('LHEGEN'):
            step['type'] = "LHE GEN"
            for i, configuration_files in enumerate(step['configuration_files']):
                if configuration_files['title'] == 'Generator parameters':
                    step['configuration_files'][i]['title']='Hadronizer parameters'
            # extend its LHE generator parameters
            step_generator_parameters= get_step_generator_parameters(dataset, mcm_step_dir, recid, 1) # Force LHE
            if step_generator_parameters:
               step['configuration_files'].extend(step_generator_parameters)

        info["steps"].append(step)

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

def populate_containerimages_cache():
    """Populate CONTAINERIMAGES cache (dataset -> system_details.container_images)"""
    with open("../cms-release-info/cms_release_container_images_info.json") as f:
        content = json.loads(f.read())
        for key in content.keys():
            CONTAINERIMAGES_CACHE[key] = content[key]

def populate_mininanorelation_cache(dataset_full_names, mcm_dir):
    """Populate MININANORELATION cache (to find the corresponding NANO for provenance, and for dataset -> relations)"""
    for dataset_full_name in dataset_full_names:
        if dataset_full_name.endswith('MINIAODSIM'):
            nano_found = 0
            dataset_first_name = get_from_deep_json(get_mcm_dict(dataset_full_name, mcm_dir), 'dataset_name')
            if dataset_first_name:
                for x in os.listdir(mcm_dir + '/chain'):
                    if x and x.startswith('@'+dataset_first_name):
                        dataset_name_for_nano = x.replace('@', '/')
                        nano_found = 1
                        MININANORELATION_CACHE[dataset_full_name] = dataset_name_for_nano
            if nano_found==0:
                print("A corresponding NANOAODSIM was not found for dataset: " + dataset_full_name)


def get_dataset_semantics_doc(dataset_name, sample_file_path, recid):
    """Produce the dataset semantics files and return their data-curation paths for the given dataset."""
    output_dir = f"outputs/docs/NanoAODSIM/{recid}"
    eos_dir = f"/eos/opendata/cms/dataset-semantics/NanoAODSIM/{recid}"
    isExist = os.path.exists(output_dir)
    if not isExist:
        os.makedirs(output_dir)

    script = "inspectNanoFile.py"

    html_doc_path = f"{output_dir}/{dataset_name}_doc.html"
    cmd = f"python3 external-scripts/{script} --doc {html_doc_path} {sample_file_path}"
    output = subprocess.getoutput(cmd)
    html_eos_path = f"{eos_dir}/{dataset_name}_doc.html"

    json_doc_path = f"{output_dir}/{dataset_name}_doc.json"
    cmd = f"python3 external-scripts/{script} --json {json_doc_path} {sample_file_path}"
    output = subprocess.getoutput(cmd)
    json_eos_path = f"{eos_dir}/{dataset_name}_doc.json"

    return {"url": html_eos_path, "json": json_eos_path}


def create_record(dataset_full_name, doi_info, recid_info, eos_dir, das_dir, mcm_dir, conffiles_dir):
    """Create record for the given dataset."""

    rec = {}

    dataset = get_dataset(dataset_full_name)
    dataset_format = get_dataset_format(dataset_full_name)
    dataset_runperiod = get_dataset_runperiod(dataset_full_name)
    dataset_version = get_dataset_version(dataset_full_name)

    year_created = '2016'
    year_published = '2024'
    run_period = ['Run2016G', 'Run2016H']

    additional_title = 'Simulated dataset ' + dataset + ' in ' + dataset_format + ' format for ' + year_created + ' collision data'

    rec['abstract'] = {}
    rec['abstract']['description'] = '<p>' + additional_title + '.</p>' + \
                                     '<p>See the description of the simulated dataset names in: <a href="/about/CMS-Simulated-Dataset-Names">About CMS simulated dataset names</a>.</p>' + \
                                     '<p>These simulated datasets correspond to the collision data collected by the CMS experiment in ' + year_created + '.</p>'

    rec['accelerator'] = "CERN-LHC"

    rec['collaboration'] = {}
    rec['collaboration']['name'] = 'CMS Collaboration'
    # rec['collaboration']['recid'] = get_author_list_recid(dataset_full_name)

    rec['collections'] = ['CMS-Simulated-Datasets', ]

    rec['collision_information'] = {}
    rec['collision_information']['energy'] = collision_energy
    rec['collision_information']['type'] = collision_type

    if dataset_format == "NANOAODSIM":
        dataset_path = f"/eos/opendata/cms/mc/{dataset_runperiod}/{dataset}/NANOAODSIM/{dataset_version}"
        intermediate_dir = os.listdir(dataset_path)
        sample_file_path = f"{dataset_path}/{intermediate_dir[0]}"
        sample_file_with_path = f"{sample_file_path}/{os.listdir(sample_file_path)[0]}"
        rec["dataset_semantics_files"] = get_dataset_semantics_doc(dataset, sample_file_with_path, str(recid_info[dataset_full_name]))

    rec['date_created'] = [year_created]
    rec['date_published'] = year_published
    rec['date_reprocessed'] = get_data_processing_year(dataset_full_name, mcm_dir)
    rec['distribution'] = {}
    rec['distribution']['formats'] = [dataset_format.lower(), 'root']
    rec['distribution']['number_events'] = get_number_events(dataset_full_name, das_dir)
    rec['distribution']['number_files'] = get_number_files(dataset_full_name, das_dir)
    rec['distribution']['size'] = get_size(dataset_full_name, das_dir)

    doi = get_doi(dataset_full_name, doi_info)
    if doi:
        rec['doi'] = doi

    rec['experiment'] = ['CMS', ]

    rec_files = get_dataset_index_files(dataset_full_name, eos_dir)
    if rec_files:
        rec['files'] = [] 
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

    rec['methodology'] = get_all_generator_text(dataset_full_name, das_dir, mcm_dir, conffiles_dir, recid_info)

    # For Mini, get the pileup from the corresponding Nano
    dataset_name_for_nano = dataset_full_name
    if dataset_full_name.endswith('MINIAODSIM'):
        dataset_name_for_nano = MININANORELATION_CACHE[dataset_full_name]

    pileup_dataset_name= ''
    pileup_dataset_name= get_pileup_from_mcm(dataset_name_for_nano, mcm_dir)

    pileup_dataset_recid = {
        '/MinBias_TuneZ2_7TeV-pythia6/Summer11Leg-START53_LV4-v1/GEN-SIM': 36, # 2011
        '/MinBias_TuneZ2star_8TeV-pythia6/Summer12-START50_V13-v3/GEN-SIM': 37, # 2012
        '/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIISummer15GS-MCRUN2_71_V1-v2/GEN-SIM': 22314, # 2015
        #'/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIISummer15GS-magnetOffBS0T_MCRUN2_71_V1-v1/GEN-SIM': {recid}, # 2015
        '/Neutrino_E-10_gun/RunIISummer20ULPrePremix-UL16_106X_mcRun2_asymptotic_v13-v1/PREMIX': 30595, # 2016
        '/MinBias_TuneCP5_13TeV-pythia8/RunIIFall18GS-IdealGeometry_102X_upgrade2018_design_v9-v1/GEN-SIM': 12302 # 2018
    }.get(pileup_dataset_name, 0)


    if pileup_dataset_name:
        rec['pileup'] = {}
        if pileup_dataset_recid:
            rec['pileup']['description'] = "<p>To make these simulated data comparable with the collision data, <a href=\"/docs/cms-guide-pileup-simulation\">pile-up events</a> are added to the simulated event in the DIGI2RAW step.</p>"
            rec['pileup']['links'] = [
                {
                    "recid": str(pileup_dataset_recid),
                    "title": pileup_dataset_name
                }
            ]
        else:
            rec['pileup']['description'] = "<p>To make these simulated data comparable with the collision data, <a href=\"/docs/cms-guide-pileup-simulation\">pile-up events</a> from the dataset <code>"\
                                            + pileup_dataset_name\
                                            + "</code> are added to the simulated event in the DIGI2RAW step.</p>"

    rec['publisher'] = 'CERN Open Data Portal'

    rec['recid'] = str(recid_info[dataset_full_name])

    if dataset_full_name.endswith('NANOAODSIM'):
        # Query from mcm dict fails for an example dataset because Mini is v1 in mcm and v2 in dataset list
        # Get it from das instead
        #dataset_name_for_mini = get_from_deep_json(get_mcm_dict(dataset_full_name, mcm_dir), 'input_dataset')
        dataset_name_for_mini = get_parent_dataset(dataset_full_name, das_dir)
        relations_description = 'The corresponding MINIAODSIM dataset:'
        relations_recid = str(recid_info[dataset_name_for_mini])
        relations_type = 'isParentOf'
    else:
        relations_description = 'The corresponding NANOAODSIM dataset:'
        relations_recid = str(recid_info[dataset_name_for_nano])
        relations_type = 'isChildOf'

    rec['relations'] = [
        {
            'description': relations_description,
            'recid': relations_recid,
            'type': relations_type
        }
    ]

    rec['run_period'] = run_period

    # recomended global tag and cmssw release recommended for analysis
    rec['system_details'] = {}
    if dataset_full_name.endswith("NANOAODSIM"):
        rec["system_details"][
            "description"
        ] = RECOMMENDED_IMAGES_FOR_NANOAOD_DESCRIPTION
        rec["system_details"]["container_images"] = RECOMMENDED_IMAGES_FOR_NANOAOD
    else:
        rec['system_details']['global_tag'] = recommended_gt
        rec['system_details']['release'] = recommended_cmssw
        if recommended_cmssw in CONTAINERIMAGES_CACHE.keys():
            rec["system_details"]["container_images"] = CONTAINERIMAGES_CACHE[recommended_cmssw]

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
    if dataset_full_name.endswith('NANOAODSIM'):
        rec["usage"]["description"] = USAGE_FOR_NANOAOD_DESCRIPTION
        rec["usage"]["links"] = USAGE_FOR_NANOAOD_LINKS
    else:
        rec['usage']['description'] = "You can access these data through the CMS Open Data container or the CMS Virtual Machine. See the instructions for setting up one of the two alternative environments and getting started in"
        rec['usage']['links'] = [
            {
              "description": "Running CMS analysis code using Docker",
              "url": "/docs/cms-guide-docker#images"
            },
            {
              "description": "How to install the CMS Virtual Machine",
              "url": "/docs/cms-virtual-machine-cc7"
            },
            {
              "description": "Getting started with CMS open data",
              "url": "/docs/cms-getting-started-miniaod"
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
        #2016: comment out threading for debugging
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

    populate_containerimages_cache()
    populate_mininanorelation_cache(datasets, mcm_dir)

    records_dir= "./outputs/records-" + dt.now().strftime("%Y-%m")
    os.makedirs(records_dir, exist_ok=True)

    create_records(datasets, doi_file, recid_file, eos_dir, das_dir, mcm_dir, conffiles_dir, records_dir)

    #records = create_records(datasets, doi_file, recid_file, eos_dir, das_dir, mcm_dir, conffiles_dir)
    #json.dump(records, indent=2, sort_keys=True, ensure_ascii=True, fp=sys.stdout)


def get_step_generator_parameters(dataset, mcm_dir, recid, force_lhe=0):
    configuration_files = {}
    if force_lhe:
        mcdb_id= get_from_deep_json(get_mcm_dict(dataset,mcm_dir), "mcdb_id") or 0
        if mcdb_id > 1:
            print("Got mcdb > 1: " + str(mcdb_id))
            configuration_files['title'] = 'Generator parameters'
            configuration_files['url'] = "/eos/opendata/cms/lhe_generators/2015-sim/mcdb/{mcdb_id}_header.txt".format(mcdb_id=mcdb_id)
            return [configuration_files]
        else:
            dir='./lhe_generators/2016-sim/gridpacks/' + str(recid) + '/'
            files = []
            files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
            confarr=[]
            for f in files:
                if f != 'LOG.txt':
                    configuration_files['title'] = 'Generator parameters: ' + f
                    configuration_files['url'] = '/eos/opendata/cms/lhe_generators/2016-sim/gridpacks/' + str(recid) + '/'  + f
                    confarr.append(configuration_files.copy())
            return confarr
    else:
        gen_fragment = get_genfragment_url(dataset, mcm_dir)
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
