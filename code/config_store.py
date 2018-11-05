import os
import sys
import subprocess
from das_json_store import get_das_store_json
from utils import check_datasets_in_eos_dir, \
                  get_from_deep_json


def get_conffile_ids(dataset):
    """Return location of the configuration files for the dataset."""
    ids = {}
    output = get_from_deep_json(get_das_store_json(dataset, 'config'),
                                'byoutputdataset')
    if output:
        for someid in output:
            ids[someid] = 1
    return list(ids.keys())


def main(eos_dir="./inputs/eos-file-indexes",
         das_dir="./inputs/das-json-store",
         conf_dir="./inputs/config-store",
         datasets=[], ignore_eos_store=False):
    "Do the job"

    # only for the datasets with EOS file information
    if ignore_eos_store:
        eos_datasets = datasets.copy()
    else:
        eos_datasets = check_datasets_in_eos_dir(datasets, eos_dir)

    conffile_ids = []
    for dataset_full_name in eos_datasets:
        for conffile_id in get_conffile_ids(dataset_full_name):
            if conffile_id not in conffile_ids:
                conffile_ids.append(conffile_id)

    if not os.path.exists(conf_dir):
        os.makedirs(conf_dir)

    voms = subprocess.run("voms-proxy-info -p", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    voms_key = voms.stdout.decode("utf-8").strip()

    total = len(conffile_ids)
    i = 1
    for conffile_id in conffile_ids:
        print("Getting ({}/{}) {}/{}.configFile".format(i, total, conf_dir, conffile_id))

        cmd = "curl -s -k --key {key} --cert {key} https://cmsweb.cern.ch/couchdb/reqmgr_config_cache/{conffile_id}/configFile".format(dir=conf_dir, conffile_id=conffile_id, key=voms_key)
        conffile = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        confs = conffile.stdout.decode("utf-8")
        if confs:
            with open("{}/{}.configFile".format(conf_dir, conffile_id), 'w') as outfile:
                outfile.write(confs)
        else:
            print("[ERROR] Empty conf file for {ds}".format(ds=conffile_id),
                  file=sys.stderr)

        i += 1