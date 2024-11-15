#!/usr/bin/env python3

"""
Create EOS rich index files for CMS 2017 collision datasets.

Creates files in the OUTPUTDIR (see below) but also copies them onto EOS final
destination (unless DEBUG is set).

To be run on LXPLUS:

$ export EOS_MGM_URL=root://eospublic.cern.ch
$ python ./code/create_eos_file_indexes.py

"""

import json
import os
import re
import subprocess

XROOTD_URI_BASE = "root://eospublic.cern.ch/"

XROOTD_DIR_BASE = "/eos/opendata/"

EXPERIMENT = "cms"

INPUT = "./inputs/cms-2017-collision-datasets.txt"

OUTPUTDIR = "./inputs/eos-file-indexes"


def get_dataset_name(dataset):
    "Return dataset name without version information."
    return dataset.split("/")[1]


def get_dataset_runperiod(dataset):
    "Return dataset run period."
    return dataset.split("/")[2].split("-")[0]


def get_dataset_version(dataset):
    "Return dataset run period."
    return dataset.split("/")[2].split("-", 1)[1]


def get_dataset_format(dataset):
    "Return dataset format."
    return dataset.split("/")[-1]


def get_dataset_location(dataset):
    "Return EOS location of the dataset."
    return (
        XROOTD_DIR_BASE
        + EXPERIMENT
        + "/"
        + get_dataset_runperiod(dataset)
        + "/"
        + get_dataset_name(dataset)
        + "/"
        + get_dataset_format(dataset)
        + "/"
        + get_dataset_version(dataset)
    )


def get_dataset_index_file_base(dataset):
    "Return index file base for given dataset."
    filebase = (
        EXPERIMENT.upper()
        + "_"
        + get_dataset_runperiod(dataset)
        + "_"
        + get_dataset_name(dataset)
        + "_"
        + get_dataset_format(dataset)
        + "_"
        + get_dataset_version(dataset)
    )
    return filebase


def get_volumes(dataset):
    "Return list of volumes for the given dataset."
    volumes = []
    dataset_location = get_dataset_location(dataset)
    output = subprocess.check_output("eos ls -1 " + dataset_location, shell=True)
    output = output.decode('utf-8')
    for line in output.split("\n"):
        if line and line != "file-indexes":
            volumes.append(line)
    return volumes


def get_files(dataset, volume):
    "Return file list with information about name, size, location for the given dataset and volume."
    files = []
    dataset_location = get_dataset_location(dataset)


    # TPM: note that the eos find --xurl option returns the full eos location so
    # a lot of this code could be simplified
    output = subprocess.check_output(
        "eos find --size --checksum " + dataset_location + "/" + volume, shell=True
    )
    output = output.decode('utf-8')

    for line in output.split("\n"):
        if line and line != "file-indexes":

            # TPM: eos doesn't return path= anymore? 
            #match = re.match(r"^path=(.*) size=(.*) checksum=(.*)$", line)
            match = re.match(r"^(.*) size=(.*) checksum=(.*)$", line)
            
            if match:
                path, size, checksum = match.groups()
                files.append(
                    {
                        "filename": os.path.basename(path),
                        "size": int(size),
                        "checksum": "adler32:" + checksum,
                        "uri": XROOTD_URI_BASE + path,
                    }
                )
    return files


def create_index_file(dataset, volume, files, style="txt"):
    "Create index file in the given style format (text, json)."
    filebase = (
        EXPERIMENT.upper()
        + "_"
        + get_dataset_runperiod(dataset)
        + "_"
        + get_dataset_name(dataset)
        + "_"
        + get_dataset_format(dataset)
        + "_"
        + get_dataset_version(dataset)
        + "_"
        + volume
        + "_"
        + "file_index"
    )
    filename = filebase + "." + style
    fdesc = open(OUTPUTDIR + "/" + filename, "w")
    if style == "txt":
        for afile in files:
            fdesc.write(afile["uri"])
            fdesc.write("\n")
    elif style == "json":
        fdesc.write(json.dumps(files, indent=2, sort_keys=True, separators=(",", ": ")))
        fdesc.write("\n")
    fdesc.close()
    return filename


def create_copy_command(dataset, volume, filename):
    "Create shell command to copy index file filename to its final destination on EOS."
    dataset_location = get_dataset_location(dataset)
    cmd = (
        "eos cp "
        + "./"
        + filename
        + " "
        + dataset_location
        + "/file-indexes/"
        + filename
    )
    fdesc = open(OUTPUTDIR + "/" + filename + ".sh", "w")
    fdesc.write(cmd + '\n')
    fdesc.close()


def create_index_files(dataset, volume):
    "Create index files for the given dataset and volumes."
    files = get_files(dataset, volume)
    filename = create_index_file(dataset, volume, files, "txt")
    # TPM: don't do this now
    #create_copy_command(dataset, volume, filename)
    filename = create_index_file(dataset, volume, files, "json")
    # TPM: don't do this now
    #create_copy_command(dataset, volume, filename)


def main():
    "Do the job."

    os.makedirs(OUTPUTDIR, exist_ok=True)
    for line in open(INPUT, "r").readlines():
        dataset = line.strip()
        volumes = get_volumes(dataset)

        print(f'dataset: {dataset}')
        
        for volume in volumes:
            create_index_files(dataset, volume)


if __name__ == "__main__":
    main()
