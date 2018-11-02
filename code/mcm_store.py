import os
import sys
import subprocess
import json
from utils import check_datasets_in_eos_dir, \
                  get_from_deep_json
from das_json_store import get_das_store_json


def mcm_downloader(prepid, dataset, mcm_dir, das_dir):
    "Query dictionary and setup script from McM database"
    # TODO this function is so ugly... refactor it, please

    cmd = "curl -s -k https://cms-pdmv.cern.ch/mcm/public/restapi/requests/{query}/{prepId}"

    mcm_dict = subprocess.run(cmd.format(query="get", prepId=prepid),
                              shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    mcm_script = subprocess.run(cmd.format(query="get_setup", prepId=prepid),
                                shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # check if results are not empty
    if str(mcm_dict.stdout.decode("utf-8")) == '{"results": {}}\n':
        print("[ERROR] Empty McM dict (get) for {ds}".format(ds=dataset),
              file=sys.stderr)
    else:
        outfile = mcm_dir + "/dict/" + dataset.replace('/', '@') + ".json"
        with open(outfile, 'w') as dict_file:
                dict_file.write(mcm_dict.stdout.decode("utf-8"))

    if mcm_script.stdout.decode("utf-8")[0] == '{':
        print("[ERROR] Empty McM script (get_setup) for {ds}".format(ds=dataset),
              file=sys.stderr)
    else:
        outfile = mcm_dir + "/scripts/" + dataset.replace('/', '@') + ".sh"
        with open(outfile, 'w') as dict_file:
                dict_file.write(mcm_script.stdout.decode("utf-8"))

    # same thing for "input_dataset": hopefully the GEN-SIM step
    dataset_json = get_das_store_json(dataset, 'mcm', das_dir)
    input_dataset = get_from_deep_json(dataset_json, 'input_dataset')  # /bla/ble/GEN-SIM
    if input_dataset:
        mcm_dict = subprocess.run(cmd.format(query="produces", prepId=input_dataset[1:]),
                                 shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        mcm_out = str(mcm_dict.stdout.decode("utf-8"))
        # check if results are not empty
        if mcm_out == '{"results": {}}' or mcm_out == '{"results": {}}\n':
            print("[ERROR] Empty McM dict (get) for {ds}".format(ds=input_dataset),
                  file=sys.stderr)
        else:
            outfile = mcm_dir + "/dict/" + input_dataset.replace('/', '@') + ".json"
            with open(outfile, 'w') as dict_file:
                    dict_file.write(mcm_out)

            prepid = get_from_deep_json(mcm_out, "prepid")
            if prepid != None:
                mcm_script = subprocess.run(cmd.format(query="get_setup", prepId=prepid),
                                            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if mcm_script.stdout.decode("utf-8")[0] == '{':
                    print("[ERROR] Empty McM script (get_setup) for {ds}".format(ds=input_dataset),
                          file=sys.stderr)
                else:
                    outfile = mcm_dir + "/scripts/" + input_dataset.replace('/', '@') + ".sh"
                    with open(outfile, 'w') as dict_file:
                            dict_file.write(mcm_script.stdout.decode("utf-8"))
            else:
                print("[ERROR] No prep_id in McM Store for record {ds}".format(ds=input_dataset),
                      file=sys.stderr)
    else:
        print("[ERROR] No input_dataset in das_store/mcm for record {ds}".format(ds=dataset),
              file=sys.stderr)


def create(datasets, mcm_dir, das_dir, eos_dir):
    "Get information from McM about each dataset"

    # create dirs
    for path in [mcm_dir + "/dict", mcm_dir + "/scripts"]:
        if not os.path.exists(path):
            os.makedirs(path)

    # only for datasets with EOS file information
    eos_datasets = check_datasets_in_eos_dir(datasets, eos_dir)
    #eos_datasets = datasets.copy()

    total = len(eos_datasets)
    i = 1
    for dataset in eos_datasets:
        print("({i}/{N}) {ds}".format(i=i, N=total, ds=dataset))

        # get prepid from das
        dataset_json = get_das_store_json(dataset, 'dataset', das_dir)
        prepid = get_from_deep_json(dataset_json, 'prep_id')
        if prepid == None:
            # try to get from das/mcm:
            prepid = get_from_deep_json(get_das_store_json(dataset, 'mcm', das_dir), 'prepid')

        if prepid != None:
            # query McM rest API for dictionary and setup script
            mcm_downloader(prepid, dataset, mcm_dir, das_dir)
        else:
            print("[ERROR] No prep_id for record {ds}".format(ds=dataset),
                  file=sys.stderr)

        i += 1


def get_mcm_dict(dataset, mcm_dir):
    """Return cached McM dictionary of dataset in json format"""

    filepath = mcm_dir + '/dict/' + dataset.replace('/', '@') + '.json'
    if os.path.exists(filepath) and os.stat(filepath).st_size != 0:
        with open(filepath, 'r') as filestream:
            return json.load(filestream)
    else:
        print('[ERROR] There is no McM JSON store dict for dataset ' + dataset,
              file=sys.stderr)
        return json.loads('{}')