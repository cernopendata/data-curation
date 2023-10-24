import json
import os
import subprocess
import sys
import threading
from time import sleep

from eos_store import check_datasets_in_eos_dir
from utils import get_dataset_name, get_from_deep_json


def get_parent_dataset(dataset, das_dir):
    "Return parent dataset to the given dataset or an empty string if no parent found."
    parent_dataset = ''

    filepath = das_dir + '/parent/' + dataset.replace('/', '@') + '.json'

    if os.path.exists(filepath) and os.stat(filepath).st_size != 0:
        parent_dataset = get_from_deep_json(get_das_store_json(dataset, 'parent', das_dir), 'parent_dataset')
    return parent_dataset


def get_das_store_json(dataset, query='dataset', das_dir=''):
    "Return DAS JSON from the DAS JSON Store for the given dataset and given query."

    if not dataset:
        print('[ERROR] There is no DAS JSON store', query, 'for dataset', dataset,
              file=sys.stderr)
        return json.loads('{}')

    filepath = das_dir + '/' + query + '/' + dataset.replace('/', '@') + '.json'
    if os.path.exists(filepath) and os.stat(filepath).st_size != 0:
        with open(filepath, 'r') as filestream:
            return json.load(filestream)
    else:
        print('[ERROR] There is no DAS JSON store ' + query + ' for dataset ' + dataset,
              file=sys.stderr)
        return json.loads('{}')


def mydasgoclient(dataset, query, out_dir, out_file):
    "Interface to dasgoclient"
   
    out = out_dir + '/' + query + '/' + out_file
    if  os.path.exists(out) and os.stat(out).st_size != 0:
        print('==> {:<9} {}'.format(query, dataset) +
            '\n==> File already exist, skipping...\n')
        return
   
    print('\t{:<9} {}'.format(query, dataset))

    cmd = 'dasgoclient -query "'
    if query != "dataset":
        cmd += query + ' '
    cmd += 'dataset=' + dataset + '" -json'


    das = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if das.returncode == 16:  # ????
        print("[Error] in ", cmd, file=sys.stderr)
        print(das.stderr.decode("utf-8"), "\n", file=sys.stderr)
    else:
        das_out = das.stdout.decode("utf-8")
        if das_out:
            with open(out, 'w') as dasfile:
                dasfile.write(das_out)
        else:
            print("[ERROR] Empty DAS {query} for {ds}".format(query=query, ds=dataset),
                  file=sys.stderr)


def create(dataset, das_dir):

    result_file = dataset.replace('/', '@') + ".json"
    mydasgoclient(dataset, "dataset", das_dir, result_file)
    mydasgoclient(dataset, "parent",  das_dir, result_file)
    mydasgoclient(dataset, "config",  das_dir, result_file)
    mydasgoclient(dataset, "release", das_dir, result_file)


def main(das_dir,
         eos_dir,
         datasets,
         ignore_eos_store):
    "Do the job."

    # create dirs for dataset and release
    for path in [das_dir + '/dataset',
                 das_dir + '/parent',
                 das_dir + '/config',
                 das_dir + '/release']:
        if not os.path.exists(path):
            os.makedirs(path)

    # only for the datasets with EOS file information
    if ignore_eos_store:
        eos_datasets = datasets.copy()
    else:
        eos_datasets = check_datasets_in_eos_dir(datasets, eos_dir)

    total = len(eos_datasets)
    i = 1
    for dataset in eos_datasets:
        print("dasgoclienting ({}/{})".format(i, total), dataset)
        t = threading.Thread(target=create, args=(dataset, das_dir))
        t.start()
        while threading.activeCount() >= 100 :
            sleep(0.5)  # run 100 dasgoclient commands in parallel 
        i += 1


def get_generator_parameters(dataset, das_dir):
    """Return generator parameters dictionary for given dataset. Not used in 2016"""
    # TODO get from mcm store instead?
    # and/or from xsecDB
    out = get_from_deep_json(get_das_store_json(dataset, 'mcm', das_dir),
                             'generator_parameters')
    if out:
        return out[0]
    else:
        return {}


def get_cmssw_version_from_das(dataset, das_dir):
    """Return CMSSW release version from DAS JSON. Not used in 2016"""
    out = get_from_deep_json(get_das_store_json(dataset, 'release', das_dir),
                             'name')
    if out:
        return out[0]
    else:
        return {}
