#!/usr/bin/env python3
# noqa: E501

import ROOT
import os
import subprocess
import yaml
import json
import click
import math
import re


"""
Create CMS derived datasets.
"""


XROOTD_URI_BASE = "root://eospublic.cern.ch/"

def get_number_events(file_path, data_type):
    """Return number of events in root file."""
    myfile = ROOT.TFile.Open(file_path)
    number_events = 0
    if data_type == "NanoAODRun1" or data_type == "PFNano":
        number_events = myfile.Events.GetEntries()
    elif data_type == "POET":
        number_events = myfile.events.GetEntries()
    return number_events


def get_parent_recid(parent_title):
    """Return parent dataset recid."""   
    cmd = f"cernopendata-client get-metadata --title={parent_title} --output-value recid"
    recid = subprocess.getoutput(cmd)
    return recid


def get_file_size(file_path):
    """Return file size."""
    file_size = os.path.getsize(file_path)/1024.0
    return math.ceil(file_size)

def get_collision_information(parent_title):
    """Return collision information.""" 
    cmd = f"cernopendata-client get-metadata --title={parent_title} --output-value collision_information"
    collision_information = subprocess.getoutput(cmd)
    return collision_information

        
def get_files(dataset_location):
    "Return file list with information about name, size, location for the given dataset and volume."
    files = []
    output = subprocess.check_output(
        "eos find --size --checksum " + dataset_location, shell=True
    )
    for line in output.decode().split('\n'):
        if line and line != "file-indexes":
            match = re.match(r"^path=(.*) size=(.*) checksum=(.*)$", line)
            if match:
                path, size, checksum = match.groups()
                filename = os.path.basename(path)
                if filename != "file_index.txt" and filename != "metadata.yaml":
                    files.append(
                        {
                            "filename": filename,
                            "size": int(size),
                            "checksum": "adler32:" + checksum,
                            "uri": XROOTD_URI_BASE + path,
                        }
                    )
    return files


def get_dataset_semantics_doc(dataset_name, sample_file_path, data_type):
    """Return the paths to the html doc and json doc of the given dataset."""
    output_dir = "outputs/docs"
    script = "documentation.py" # for NanoAODRun1 
    if data_type == "PFNano":
        script = "inspectNanoFile.py"

    html_doc_path = f"{output_dir}/{dataset_name}_doc.html"
    cmd = f"python3 external-scripts/{script} --doc {html_doc_path} {sample_file_path}"
    output = subprocess.getoutput(cmd)

    json_doc_path = f"{output_dir}/{dataset_name}_doc.json"
    cmd = f"python3 external-scripts/{script} --json {json_doc_path} {sample_file_path}"
    output = subprocess.getoutput(cmd)

    return {"html_doc": html_doc_path, "json_doc": json_doc_path}


def create_record(metadata, data_type):
    """Create record using the given metadata."""
    
    config_file = open("config.yaml", 'r')
    config = yaml.safe_load(config_file)

    rec = {}

    rec["abstract"] = {}
    rec["abstract"]["description"] = config[data_type]["abstract"]["description"].replace("<dataset-title>", metadata["dataset-title"]).replace("<dataset>", metadata["dataset"]).replace("<parent_dataset>", metadata["parent"])
    if data_type == "PFNano":
        rec["abstract"]["links"] = []
        for i in metadata["valid_recids"]:
            rec["abstract"]["links"].append({
                "recid": str(i)
            })

    rec["accelerator"] = config["common_values"]["accelerator"]
    
    rec["authors"] = []
    rec["authors"].append({
        "name": config["common_values"]["authors"]
    })
    
    rec["collision_information"] = json.loads(metadata["collision_information"])
    rec["collections"] = config["common_values"]["collections"]

    if data_type != "POET":
        rec["dataset_semantics_files"] = {}
        rec["dataset_semantics_files"]["html_doc"] =  metadata["dataset_semantics_files"]["html_doc"].rsplit('/',1)[1]
        rec["dataset_semantics_files"]["json_doc"] =  metadata["dataset_semantics_files"]["json_doc"].rsplit('/',1)[1]
        
    rec["date_published"] = config["common_values"]["date_published"]
    
    rec["distribution"] = {}
    # changes format to nanoaodsim-NNN for MC - to be modified for PFNano sim if we make some (PFNano names dataset names do not have Run2016 in them...)
    if "Run201" not in metadata["dataset"] and data_type != "PFNano":
        substr = "nanoaod"
        repl = "nanoaodsim"
        config[data_type]["distribution"]["formats"][0] = config[data_type]["distribution"]["formats"][0].replace(substr,repl)
    config[data_type]["distribution"]["formats"].append("root")

    rec["distribution"]["formats"] = config[data_type]["distribution"]["formats"]
    rec["distribution"]["number_events"] = metadata["number_events"] 
    rec["distribution"]["number_files"] = metadata["number_files"]
    rec["distribution"]["size"] = metadata["size"]

    # uniqely generated for each record (?)
    rec["doi"] = ""
    
    rec["experiment"] = [
        config["common_values"]["experiment"]
    ]

    rec["files"] = metadata["files"]
    
    #rec["index_files"] = []
    
    rec["license"] = config["common_values"]["license"]

    rec["methodology"] = config[data_type]["methodology"]
    
    rec["publisher"] = config["common_values"]["publisher"]
    
    rec["recid"] = str(metadata["recid"])
    
    rec["relations"] = []
    rec["relations"].append({
        "description": "This dataset was derived from:",
        "recid":str(metadata["parent_recid"]),
        "type": "isChildOf"
    })

    rec["title"] =  config[data_type]["title"].replace("<dataset-title>", metadata["dataset-title"])

    rec["type"] = config["common_values"]["type"]

    rec["use_with"] = config[data_type]["use_with"]

    rec["validation"] = {}
    rec["validation"]["description"] = config[data_type]["validation"]["description"]
    if data_type == "PFNano":
        rec["validation"]["links"] = []
        rec["validation"]["links"].append({
                "url": "link to processedLumis.json"
            })

    return rec


def print_records(records):
    """Print records."""
    for line in json.dumps(records, indent=2, sort_keys=True).split('\n'):
        line = line.rstrip()
        print(line)


@click.command()
@click.option('--data-type',
              '-t',
              required=True,
              help='Data Type (NanoAODRun1, POET, PFNano)')
def main(data_type):
    "Do the job."

    config_file = open("config.yaml", 'r')
    config = yaml.safe_load(config_file)

    # initialize variables based on data type
    recid_start = 0
    date = ""
    if data_type == "NanoAODRun1":
        date = "01-Jul-22"
        recid_start = config["NanoAODRun1"]["recid_start"]
    elif data_type == "POET":
        date = "23-Jul-22"
        recid_start = config["POET"]["recid_start"]
    elif data_type == "PFNano":
        date = "29-Feb-24"
        recid_start = config["PFNano"]["recid_start"]
        parent_recid = 30500
        valid_recids = [14220,14221]
        process_path = "Run2016G-UL2016_MiniAODv2_PFNanoAODv1"
    
    records = []
    datasets_path = f"/eos/opendata/cms/derived-data/{data_type}/{date}"
    datasets = os.listdir(datasets_path)
    # iterate over each dataset
    for dataset in datasets:
        if dataset.endswith("root") or dataset.endswith("flat"):
            continue
        
        dataset_dir_path = f"{datasets_path}/{dataset}"
        metadata_yaml_file = open(f"{dataset_dir_path}/metadata.yaml", 'r')
        metadata = yaml.safe_load(metadata_yaml_file)
        
        if data_type == "PFNano":
            dataset_dir_path = f"{dataset_dir_path}/{process_path}"
            next = os.listdir(dataset_dir_path)[0]
            dataset_dir_path = f"{dataset_dir_path}/{next}/0000"

        dataset_files = os.listdir(dataset_dir_path)

        files = get_files(dataset_dir_path)
        number_events = 0
        number_files = 0
        size = 0
        # POET datasets
        if data_type == "POET":
            # for all root files under <dataset> directory
            for file in dataset_files:
                if file.endswith("root"):
                    number_files += 1
            # for all root files under <dataset>_flat directory
            flat_files_dir_path = f"{datasets_path}/{dataset}_flat"
            dataset_flat_files = os.listdir(flat_files_dir_path)
            files.extend(get_files(flat_files_dir_path)) # adds the flat files to the list of dataset files
            for file in dataset_flat_files:
                if file.endswith("root"):
                    flat_file_path = f"{flat_files_dir_path}/{file}"
                    # assuming the number of events is the same in the flat and normal dataset versions
                    number_events += get_number_events(flat_file_path, data_type)
                    number_files += 1
                    file_size = get_file_size(flat_file_path)
                    size += file_size
            dataset_all_flattened_file_path = dataset_dir_path + "_flat.root"
            files.extend(get_files(dataset_all_flattened_file_path))
            number_files += 1 # for _flat.root in POET 
        # NanoAODRun1 datasets
        elif data_type == "NanoAODRun1":
            # for all root files under <dataset> directory
            for file in dataset_files:
                if file.endswith("root"):
                    file_path = f"{dataset_dir_path}/{file}"
                    number_events += get_number_events(file_path, data_type)
                    number_files += 1
                    file_size = get_file_size(file_path)
                    size += file_size
            dataset_all_merged_path = dataset_dir_path + "_merged.root"
            files.extend(get_files(dataset_all_merged_path))  # adds the merged file to the list of dataset files
            sample_file_path = f"{dataset_dir_path}/{dataset_files[0]}"
            metadata["dataset_semantics_files"] = get_dataset_semantics_doc(dataset, sample_file_path, data_type)
            number_files += 1 # for _merged.root in NanoAODRun1
        elif data_type == "PFNano":
            for file in dataset_files:
                if file.endswith("root"):
                    file_path = f"{dataset_dir_path}/{file}"
                    number_events += get_number_events(file_path, data_type)
                    number_files += 1
                    file_size = get_file_size(file_path)
                    size += file_size
            files.extend(get_files(dataset_dir_path))
            sample_file_path = f"{dataset_dir_path}/{dataset_files[0]}"
            metadata["dataset_semantics_files"] = get_dataset_semantics_doc(dataset, sample_file_path, data_type)
        
        # prepare metadata for creating the record, for PFNano differently as cernopendata-client does not reach datasets that are not yet released
        if data_type == "PFNano":
            metadata["parent_recid"] = str(parent_recid)
            parent_recid += 1 # this assumes loop in aplhabetical order
            metadata["collision_information"] = '{"energy": "13TeV","type": "pp"}'
            metadata["valid_recids"] = []
            metadata["valid_recids"] = valid_recids
        else:
            metadata["parent_recid"] = get_parent_recid(metadata["parent"])
            metadata["collision_information"] = get_collision_information(metadata["parent"])
    
        # For MC, remove the processing string from the name for the title
        metadata["dataset-title"] = metadata["dataset"]
        if "Run201" not in metadata["dataset"]:
            if data_type == "NanoAODRun1":
                metadata["dataset-title"] = metadata["dataset"].split('DR',1)[1].split('_',1)[1]
            elif data_type == "POET":
                metadata["dataset-title"] = metadata["dataset"].split('_',1)[1]
        metadata["number_events"] = number_events
        metadata["number_files"] = number_files
        metadata["size"] = size
        metadata["recid"] = recid_start
        metadata["files"] = files
        recid_start += 1
        
        record = create_record(metadata, data_type)
        records.append(record)
    
    print_records(records)

if __name__ == '__main__':
    main()


