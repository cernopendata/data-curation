import json
import os
import re
import subprocess
import sys
import threading
from time import sleep

from das_json_store import get_das_store_json, get_parent_dataset
from eos_store import check_datasets_in_eos_dir
from utils import get_dataset_format, get_dataset_year, get_from_deep_json


def mcm_downloader(dataset, mcm_dir):
    "Query dictionary and setup script from McM database"

    filepath = mcm_dir + "/dict/" + dataset.replace('/', '@') + ".json"
    if os.path.exists(filepath) and os.stat(filepath).st_size != 0:
        print("==> " + dataset + "\n==> Already exist. Skipping...")
        return

    cmd = "curl -s -k https://cms-pdmv-prod.web.cern.ch/mcm/public/restapi/requests/"

    mcm_dict = subprocess.run(cmd + "produces" + dataset,
                              shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    mcm_dict_out = str(mcm_dict.stdout.decode("utf-8"))
    prepid = None
    if mcm_dict_out != '{"results": {}}\n' or mcm_dict_out != '{"results": {}}':
        # get prepid from mcm/dataset
        prepid= get_from_deep_json(json.loads(mcm_dict_out), "prepid")

    if not prepid:
        print("Error: prepid not found in mcm for " + dataset + "\n==> Skipping dataset McM dict and script",file=sys.stderr )
        return

    outfile = mcm_dir + "/dict/" + dataset.replace('/', '@') + ".json"
    with open(outfile, 'w') as dict_file:
           dict_file.write(mcm_dict_out)

    mcm_script = subprocess.run(cmd + "get_test/" + prepid ,
                                shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    mcm_script_out = str(mcm_script.stdout.decode("utf-8"))

    if mcm_script_out == '' or mcm_script_out[0] == '{':
        print("[ERROR] Empty McM script (get_test) for {ds}".format(ds=dataset),
            file=sys.stderr)
    else:
        outfile = mcm_dir + "/scripts/" + dataset.replace('/', '@') + ".sh"
        with open(outfile, 'w') as dict_file:
                dict_file.write(mcm_script_out)

    ### New 2016
    # create a directory with the dataset name under mcm_dir + "/chain"
    # create dirs
    if dataset.endswith('MINIAODSIM'):
        return
    path = mcm_dir + "/chain/" + dataset.replace('/', '@')
    os.makedirs(path, exist_ok=True)

    # FIXME: change shell jq to deep json query
    mcm_chain_prepid = subprocess.run(cmd + "get/" + prepid  + " | jq .results.member_of_chain",
                                shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    mcm_chain_prepid_out = str(mcm_chain_prepid.stdout.decode("utf-8"))
    chain_prepid = re.sub(r"[\[\]]", "", mcm_chain_prepid_out).strip()

    # now query for the full chain
    # FIXME: change shell jq to deep json query
    chaincmd = "curl -L -s -b cookies.txt https://cms-pdmv-prod.web.cern.ch/mcm/restapi/chained_requests/"
    mcm_chain_prepids = subprocess.run(chaincmd + "get/" + chain_prepid  + " | jq .results.chain",
                                shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    mcm_chain_prepids_out = str(mcm_chain_prepids.stdout.decode("utf-8"))
    json_object = json.loads(mcm_chain_prepids_out)
    for idx,step in enumerate(json_object):
        step_path = mcm_dir + "/chain/" + dataset.replace('/', '@') + "/" + str(idx) + step
        for path in [step_path, step_path + "/dict", step_path + "/scripts"]:
            os.makedirs(path, exist_ok=True)
        
        mcm_step_dict = subprocess.run(cmd + "get/" + step,
                                shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        mcm_step_dict_out = str(mcm_step_dict.stdout.decode("utf-8"))

        # check if it is empty (then there is no way to get dataset McM dict)
        if mcm_step_dict_out == '{"results": {}}\n' or mcm_step_dict_out == '{"results": {}}':
            print(step + "[ERROR] Empty McM dict (get) for {ds} \n with prepid {pd}".format(ds=dataset,pd=prepid),
                  file=sys.stderr)
        else:
            outfile = step_path + "/dict/" + dataset.replace('/', '@') + ".json"
            with open(outfile, 'w') as dict_file:
                    dict_file.write(mcm_step_dict_out)

        mcm_step_script = subprocess.run(cmd + "get_test/" + step ,
                                shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        mcm_step_script_out = str(mcm_step_script.stdout.decode("utf-8"))

        if mcm_step_script_out == '' or mcm_step_script_out[0] == '{':
            print(step + " [ERROR] Empty McM script (get_test) for {ds}".format(ds=dataset),
                file=sys.stderr)
        else:
            outfile = step_path + "/scripts/" + dataset.replace('/', '@') + ".sh"
            with open(outfile, 'w') as dict_file:
                    dict_file.write(mcm_step_script_out)



def create(datasets, mcm_dir, eos_dir, ignore_eos_store=False):
    "Get information from McM about each dataset"

    # create dirs
    for path in [mcm_dir + "/dict", mcm_dir + "/scripts", mcm_dir + "/chain"]:
        os.makedirs(path, exist_ok=True)

    # only for datasets with EOS file information
    if ignore_eos_store:
        eos_datasets = datasets.copy()
    else:
        eos_datasets = check_datasets_in_eos_dir(datasets, eos_dir)

    total = len(eos_datasets)
    i = 1
    for dataset in eos_datasets:
        print("McM Storing ({i}/{N}) {ds}".format(i=i, N=total, ds=dataset))
        t = threading.Thread(target=mcm_downloader, args=(dataset, mcm_dir))
        t.start()
        while threading.activeCount() >= 100 :
            sleep(0.5)  # run 100 curl commands in parallel
        i += 1


def get_mcm_dict(dataset, mcm_dir):
    """Return cached McM dictionary of dataset in json format"""

    filepath = mcm_dir + '/dict/' + dataset.replace('/', '@') + '.json'
    if os.path.exists(filepath) and os.stat(filepath).st_size != 0:
        with open(filepath, 'r') as filestream:
            try:
                return json.load(filestream)
            except:
                return json.loads('{}')
    else:
        print(f'[ERROR] There is no McM JSON store dict for dataset {dataset} in directory {mcm_dir}',
              file=sys.stderr)
        return json.loads('{}')


def get_prepId_from_das(dataset, das_dir):
    "get prepid for dataset"

    # get prepid from das/dataset
    prepid = get_from_deep_json(get_das_store_json(dataset, 'dataset', das_dir), 'prep_id')

    if not prepid:
        # try to get from das/mcm:
        prepid = get_from_deep_json(get_das_store_json(dataset, 'mcm', das_dir), 'prepid')

    return prepid


def get_prepid_from_mcm(dataset, mcm_dir):
    "get prepid for dataset from McM store. Not used in 2016"

    # get prepid from das/dataset
    prepid = get_from_deep_json(get_mcm_dict(dataset, mcm_dir), 'prep_id')

    if not prepid:
        # try different queries from the json. prep_id?
        prepid = get_from_deep_json(get_mcm_dict(dataset, mcm_dir), 'prepid')

    return prepid


def get_global_tag(dataset, mcm_dir):
    "Get global tag from McM dictionary"
    mcm_dict = get_mcm_dict(dataset, mcm_dir)
    global_tag = get_from_deep_json(mcm_dict, 'conditions')

    if not global_tag:
        global_tag = ''

    return global_tag


def get_cmssw_version_from_mcm(dataset, mcm_dir):
    "Get CMSSW version from McM dictionary"
    mcm_dict = get_mcm_dict(dataset, mcm_dir)
    cmssw = get_from_deep_json(mcm_dict, 'cmssw_release')

    if not cmssw:
        cmssw = ''

    return cmssw


def get_cmsDriver_script(dataset, mcm_dir):
    """Return path to cmsDriver script for that dataset"""
    if not dataset:
        return None

    script = mcm_dir + '/scripts/' + dataset.replace('/', '@') + '.sh'
    if os.path.exists(script):
        return script
    else:
        return None


def get_genfragment_url(dataset, mcm_dir):
    "return list of url's of the genfragments used"
    url = []
    script_path = get_cmsDriver_script(dataset, mcm_dir)
    if script_path == None:
        return None

    with open(script_path, 'r') as script:
        for line in script:
            if 'curl' in line:
                curl = re.search('(?P<url>https?://[^\s]+)', line)
                if curl:
                    url.append(curl.group('url'))
    return url


def get_dataset_energy(dataset, mcm_dir):
    "Return energy of that dataset in TeV"
    mcm_dict = get_mcm_dict(dataset, mcm_dir)
    if mcm_dict:
        energy = get_from_deep_json(mcm_dict, 'energy')
        if isinstance(energy, str):
            return energy
        else:
            return str(energy).replace('.0', '') + 'TeV'

    else:
        year = get_dataset_year(dataset)
        return {
               2010:  '7TeV',
               2011:  '7TeV',
               2012:  '8TeV',
               2015: '13TeV',
               2016: '13TeV',
               }.get(year, 0)

def get_data_processing_year(dataset, mcm_dir):
    "Return year of the processing from McM"
    mcm_dict = get_mcm_dict(dataset, mcm_dir)
    date = get_from_deep_json(mcm_dict, 'pdmv_submission_date')
    if len(date) == 6:
        year='20' + date[:2]
        return year
    else:
        print("In get_data_processing_year, unexpected format for date: expecting yymmdd, got :" + date)
        return '0000'
 

def get_generator_name(dataset, mcm_dir):
    "Return list of generators used for that dataset"
    generator_names = []
    mcm_dict = get_mcm_dict(dataset, mcm_dir)
    generators = get_from_deep_json(mcm_dict, 'generators')

    if generators:
        for item in generators:
            for char in ['"', '\\', '[', ']']:  # remove ", \, [, ]
                item = item.replace(char, '')
            generator = item
            if generator not in generator_names:
                generator_names.append(item)

    return generator_names


def get_parent_dataset_from_mcm(dataset, mcm_dir):
    "Return parent dataset to given DATASET from McM."
    parent_dataset = ''
    mcm_dict = get_mcm_dict(dataset, mcm_dir)
    parent_dataset = get_from_deep_json(mcm_dict, 'input_dataset')
    return parent_dataset

def get_output_dataset_from_mcm(dataset, mcm_dir):
    "Return output dataset to given production step of a DATASET from McM."
    mcm_dict = get_mcm_dict(dataset, mcm_dir)
    output_dataset = get_from_deep_json(mcm_dict, 'output_dataset')
    return output_dataset

def get_conffile_ids_from_mcm(dataset, mcm_dir):
    """Return location of the configuration files for the dataset from McM."""
    config_ids = []
    mcm_dict = get_mcm_dict(dataset, mcm_dir)
    config_ids = get_from_deep_json(mcm_dict, 'config_id')
    return config_ids


def get_generator_parameters_from_mcm(dataset, mcm_dir):
    """Return generator parameters dictionary for given dataset."""
    mcm_dict = get_mcm_dict(dataset, mcm_dir)
    out = get_from_deep_json(mcm_dict, 'generator_parameters')
    if out:
        return out[0]
    else:
        return {}


def get_pileup_from_mcm(dataset, mcm_dir):
    """Return pileup_dataset_name from the DIGIPremix step of a given dataset."""
    pileup=''
    path = mcm_dir + '/chain/' + dataset.replace('/', '@')
    step_dirs = os.listdir(path)
    for step_dir in step_dirs:
        m = re.search('-(.+?)-', step_dir)
        if m:
            step_name = m.group(1)
            if step_name.endswith('DIGIPremix'):
                mcm_step_dir = path + '/' + step_dir
                mcm_dict = get_mcm_dict(dataset, mcm_step_dir)
                pileup = get_from_deep_json(mcm_dict, 'pileup_dataset_name')
    return pileup
