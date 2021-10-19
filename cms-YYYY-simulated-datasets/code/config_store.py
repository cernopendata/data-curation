import os
import subprocess
import sys

from das_json_store import get_das_store_json, get_parent_dataset
from eos_store import check_datasets_in_eos_dir
from mcm_store import get_conffile_ids_from_mcm
from utils import get_from_deep_json


def get_conffile_ids(dataset, das_dir, mcm_dir):
    """Return location of the configuration files for the dataset."""
    ids = {}
    byoutput = get_from_deep_json(get_das_store_json(dataset, 'config', das_dir),
                                'byoutputdataset')
    byinput = get_from_deep_json(get_das_store_json(dataset, 'config', das_dir),
                                'byinputdataset')
    mcm_config_ids = get_conffile_ids_from_mcm(dataset, mcm_dir)
    
    if byoutput:
        for someid in byoutput:
            ids[someid] = 1
    if byinput:
        for someid in byinput:
            ids[someid] = 1
    if mcm_config_ids:
        for someid in mcm_config_ids:
            ids[someid] = 1

    return list(ids.keys())


def main(eos_dir,
         das_dir,
         mcm_dir,
         conf_dir,
         datasets,
         ignore_eos_store):
    "Do the job"

    # only for the datasets with EOS file information
    if ignore_eos_store:
        eos_datasets = datasets.copy()
    else:
        eos_datasets = check_datasets_in_eos_dir(datasets, eos_dir)

    # add parents of the parents to the eos_datasets list!
    for dataset in eos_datasets:
        parent = get_parent_dataset(dataset, das_dir)
        while parent:
            if parent not in eos_datasets: 
                eos_datasets.append(parent)
            parent = get_parent_dataset(parent, das_dir)

    conffile_ids = []
    for dataset_full_name in eos_datasets:
        for conffile_id in get_conffile_ids(dataset_full_name, das_dir, mcm_dir):
            if conffile_id not in conffile_ids:
                conffile_ids.append(conffile_id)

    if not os.path.exists(conf_dir):
        os.makedirs(conf_dir, exist_ok=True)

    key_nodes = "~/.globus/userkey.nodes.pem"
    cert = "~/.globus/usercert.pem"

    total = len(conffile_ids)
    i = 1
    for conffile_id in conffile_ids:
        filepath="{}/{}.configFile".format(conf_dir, conffile_id)
        if os.path.exists(filepath) and os.stat(filepath).st_size != 0:
            print("==> " + conffile_id + ".configFile\n==> Already exist. Skipping...")
            i += 1
            continue

        print("Getting ({}/{}) {}/{}.configFile".format(i, total, conf_dir, conffile_id))

        cmd = "curl -s -k --key {key} --cert {cert} https://cmsweb.cern.ch/couchdb/reqmgr_config_cache/{conffile_id}/configFile".format(conffile_id=conffile_id, key=key_nodes, cert=cert)
        conffile = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        confs = conffile.stdout.decode("utf-8")
        if confs:
            with open(filepath, 'w') as outfile:
                outfile.write(confs)
        else:
            print("[ERROR] Empty conf file for {ds}".format(ds=conffile_id), file=sys.stderr)

        i += 1
