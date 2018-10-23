import os
import subprocess
from utils import get_dataset_name


def mydasgoclient(dataset, query, out_dir, out_file):
    "Interface to dasgoclient"

    cmd = 'dasgoclient -query "'
    if query != "dataset":
        cmd += query + ' '
    cmd += 'dataset=' + dataset + '" -json'

    out = out_dir + '/' + query + '/' + out_file

    das = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if das.returncode == 16:  # ????
        print("Error with ", cmd)
        print(das.stderr.decode("utf-8"), "\n")
    else:
        with open(out, 'w') as dasfile:
            dasfile.write(str(das.stdout.decode("utf-8")))  # FIXME this can be empty?


def main(das_dir="./inputs/das-json-store",
         eos_dir="./inputs/eos-file-indexes",
         datasets=[]):
    "Do the job."

    # create dirs for dataset, parent and config
    for path in [das_dir + "/dataset", das_dir + "/parent", das_dir + "/config", das_dir + "/mcm"]:
        if not os.path.exists(path):
            os.makedirs(path)

    eos_files = os.listdir(eos_dir)
    for dataset in datasets:
        primary_dataset = get_dataset_name(dataset)

        # only for the datasets with EOS file information
        # is it necessary to only get the ones with eos information?
        # is this really working? FIXME
        if any(primary_dataset in s for s in eos_files):
            print("dasgoclienting ", dataset)
            result_file = dataset.replace('/', '@') + ".json"
            mydasgoclient(dataset, "dataset", das_dir, result_file)
            mydasgoclient(dataset, "parent",  das_dir, result_file)
            mydasgoclient(dataset, "config",  das_dir, result_file)
            mydasgoclient(dataset, "mcm",     das_dir, result_file)


if __name__ == '__main__':
    main()
