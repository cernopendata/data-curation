import os
import sys
import subprocess
import json
from utils import get_dataset_name, \
                  get_from_deep_json
from eos_store import  check_datasets_in_eos_dir


def get_parent_dataset(dataset, das_dir='./inputs/das-json-store'):
    "Return parent dataset to the given dataset or an empty string if no parent found."
    parent_dataset = ''
    try:
        parent_dataset = get_from_deep_json(get_das_store_json(dataset, 'parent', das_dir), 'parent_dataset')
    except:
        # troubles getting information about parent
        pass
    return parent_dataset


def get_das_store_json(dataset, query='dataset', das_dir='./inputs/das-json-store'):
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

    print('\t{:<9} {}'.format(query, dataset))

    cmd = 'dasgoclient -query "'
    if query != "dataset":
        cmd += query + ' '
    cmd += 'dataset=' + dataset + '" -json'

    out = out_dir + '/' + query + '/' + out_file

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


def main(das_dir="./inputs/das-json-store",
         eos_dir="./inputs/eos-file-indexes",
         datasets=[], ignore_eos_store=False):
    "Do the job."

    # create dirs for dataset, parent and config
    for path in [das_dir + "/dataset", das_dir + "/parent", das_dir + "/config", das_dir + "/mcm"]:
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
        # is it necessary to only get the ones with eos information?
        print("dasgoclienting ({}/{})".format(i, total), dataset)

        result_file = dataset.replace('/', '@') + ".json"
        mydasgoclient(dataset, "dataset", das_dir, result_file)
        mydasgoclient(dataset, "parent",  das_dir, result_file)
        mydasgoclient(dataset, "config",  das_dir, result_file)
        mydasgoclient(dataset, "mcm",     das_dir, result_file)

        parent = get_parent_dataset(dataset, das_dir)
        while parent != '' and parent:
            #mydasgoclient(parent, "dataset",  das_dir, parent.replace('/', '@') + ".json")
            mydasgoclient(parent, "config",   das_dir, parent.replace('/', '@') + ".json")
            mydasgoclient(parent, "parent",   das_dir, parent.replace('/', '@') + ".json")
            parent = get_parent_dataset(parent, das_dir)

        i += 1


if __name__ == '__main__':
    main()
