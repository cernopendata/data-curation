#!/usr/bin/env python
# noqa: E501


"""
Create CMS 2015 open data release collision datasets.
"""

import click
import csv
import json
import os
import re
import subprocess
import zlib

from create_eos_file_indexes import (
    XROOTD_URI_BASE,
    get_dataset_index_file_base,
    get_dataset_location,
)

FWYZARD = {}

SELECTION_DESCRIPTIONS = {}

LINK_INFO = {}
exec(open("./outputs/reco_config_files_link_info.py", "r").read())

DOI_INFO = {}

RECID_START = 24100


def get_from_deep_json(data, akey):
    "Traverse DATA and return first value matching AKEY."
    if type(data) is dict:
        if akey in data.keys():
            return data[akey]
        else:
            for val in data.values():
                if type(val) is dict:
                    aval = get_from_deep_json(val, akey)
                    if aval:
                        return aval
                if type(val) is list:
                    for elem in val:
                        aval = get_from_deep_json(elem, akey)
                        if aval:
                            return aval
    if type(data) is list:
        for elem in data:
            aval = get_from_deep_json(elem, akey)
            if aval:
                return aval
    return None


def get_das_store_json(dataset):
    "Return DAS JSON from the DAS JSON Store for the given dataset."
    filepath = "./inputs/das-json-store/" + dataset.replace("/", "@") + ".json"
    with open(filepath, "r") as filestream:
        return json.load(filestream)


def get_number_events(dataset):
    """Return number of events for the dataset."""
    number_events = get_from_deep_json(get_das_store_json(dataset), "nevents")
    if number_events:
        return number_events
    return 0


def get_number_files(dataset):
    """Return number of files for the dataset."""
    number_files = get_from_deep_json(get_das_store_json(dataset), "nfiles")
    if number_files:
        return number_files
    return 0


def get_size(dataset):
    """Return size of the dataset."""
    size = get_from_deep_json(get_das_store_json(dataset), "size")
    if size:
        return size
    return 0


def get_file_size(afile):
    "Return file size of a file."
    return os.path.getsize(afile)


def get_file_checksum(afile):
    """Return the ADLER32 checksum of a file."""
    return hex(zlib.adler32(open(afile, "rb").read(), 1) & 0xFFFFFFFF)[2:]


def populate_fwyzard():
    """Populate FWYZARD dictionary (dataset -> trigger list)."""
    for line in open("./inputs/hlt-2015-dataset.txt", "r").readlines():
        line = line.strip()
        dataset, trigger = line.split(",")
        if trigger.endswith("_v"):
            trigger = trigger[:-2]
        if dataset in FWYZARD.keys():
            FWYZARD[dataset].append(trigger)
        else:
            FWYZARD[dataset] = [
                trigger,
            ]


def populate_doiinfo():
    """Populate DOI_INFO dictionary (dataset -> doi)."""
    for line in open("./inputs/doi-col.txt", "r").readlines():
        dataset, doi = line.split()
        DOI_INFO[dataset] = doi


def populate_selection_descriptions():
    """Populate SELECTION_DESCRIPTIONS dictionary (dataset -> selection description)."""
    for input_file in ["./inputs/CMSDatasetDescription_Run2015D.csv"]:
        with open(input_file, "r") as csvfile:
            for line_values in csv.reader(csvfile, delimiter=":"):
                dataset, description = line_values
                SELECTION_DESCRIPTIONS[dataset] = description


def get_release_for_processing(dataset_full_name):
    """Return CMSSW release info for the given dataset for the processing step."""
    if "16Dec2015" in dataset_full_name:
        return "CMSSW_7_6_3"
    if "08Jun2016" in dataset_full_name:
        return "CMSSW_7_6_5_patch1"
    return "FIXME"


def get_release_for_system_details(dataset_full_name):
    """Return CMSSW release info for the given dataset for the system details."""
    return "CMSSW_7_6_7"


def get_global_tag_for_processing(dataset_full_name):
    """Return global tag info for the given dataset for the processing steps."""
    return "76X_dataRun2_v15"


def get_global_tag_for_system_details(dataset_full_name):
    """Return global tag info for the given dataset for the system details."""
    return "76X_dataRun2_16Dec2015_v0"


def create_selection_information(dataset, dataset_full_name):
    """Create box with selection information."""
    if "MINIAOD" in dataset_full_name:
        aodformat = "MINIAOD"
    else:
        aodformat = "AOD"
    out = ""
    # description:
    out += "<p>"
    out += SELECTION_DESCRIPTIONS[dataset_full_name]
    out += "</p>"
    # data taking / HLT:
    out += "<p><strong>Data taking / HLT</strong>"
    out += '<br/>The collision data were assigned to different RAW datasets using the following <a href="/record/23900">HLT configuration</a>.</p>'
    # data processing / RECO:
    run_period = re.search(r"(Run[0-9]+.)", dataset_full_name).groups()[0]
    afile = "reco_" + run_period[3:] + "_" + dataset
    process = "RECO"
    generator_text = "Configuration file for " + process + " step " + afile
    release = get_release_for_processing(dataset_full_name)
    global_tag = get_global_tag_for_processing(dataset_full_name)
    out += "<p><strong>Data processing / RECO</strong>"
    out += (
        "<br/>This primary %s dataset was processed from the RAW dataset by the following step: "
        % aodformat
    )
    out += "<br/>Step: %s" % process
    out += "<br/>Release: %s" % release
    out += "<br/>Global tag: %s" % global_tag
    out += '\n        <br/><a href="/record/%s">%s</a>' % (
        LINK_INFO.get(afile, ""),
        generator_text,
    )
    out += "\n        </p>"
    # HLT trigger paths:
    out += "<p><strong>HLT trigger paths</strong>"
    out += "<br/>The possible HLT trigger paths in this dataset are:"
    trigger_paths = get_trigger_paths_for_dataset(dataset)
    for trigger_path in trigger_paths:
        out += '<br/><a href="/search?q=%s">%s</a>' % (trigger_path, trigger_path)
    out += "</p>"
    return out


def get_trigger_paths_for_dataset(dataset):
    """Return list of trigger paths for given dataset."""
    return FWYZARD.get(dataset, [])


def get_dataset_index_files(dataset_full_name):
    """Return list of dataset file information {path,size} for the given dataset."""
    files = []
    dataset_index_file_base = get_dataset_index_file_base(dataset_full_name)
    output = subprocess.getoutput(
        "ls ./inputs/eos-file-indexes/ | grep " + dataset_index_file_base
    )
    for line in output.split("\n"):
        afile = line.strip()
        if afile.endswith(".txt") or afile.endswith(".json"):
            # take only TXT files
            afile_uri = (
                XROOTD_URI_BASE
                + get_dataset_location(dataset_full_name)
                + "/file-indexes/"
                + afile
            )
            afile_size = get_file_size("./inputs/eos-file-indexes/" + afile)
            afile_checksum = get_file_checksum("./inputs/eos-file-indexes/" + afile)
            files.append((afile_uri, afile_size, afile_checksum))
    return files


def get_doi(dataset_full_name):
    "Return DOI for the given dataset."
    return DOI_INFO.get(dataset_full_name, "")


def create_record(recid, run_period, version, dataset, aodformat):
    """Create record for the given dataset."""

    rec = {}

    recid_validated_runs = "14210"
    dataset_full_name = (
        "/" + dataset + "/" + run_period + "-" + version + "/" + aodformat
    )
    year_created = run_period[3:7]
    year_published = "2021"

    rec["abstract"] = {}
    if run_period == "Run2015D":
        rec["abstract"]["description"] = (
            "<p>"
            + dataset
            + " primary dataset in %s format from RunD of 2015. Run period from run number 256630 to 260627."
            % aodformat
            + "</p><p>The list of validated runs, which must be applied to all analyses, either with the full validation or for an analysis requiring only muons, can be found in:</p>"
        )

        rec["abstract"]["links"] = [
            {"description": "Validated runs, full validation", "recid": "14210"},
            {"description": "Validated runs, muons only", "recid": "14211"},
        ]

    rec["accelerator"] = "CERN-LHC"

    rec["collaboration"] = {}
    rec["collaboration"]["name"] = "CMS collaboration"

    rec["collections"] = [
        "CMS-Primary-Datasets",
    ]

    rec["collision_information"] = {}
    rec["collision_information"]["energy"] = "13TeV"
    rec["collision_information"]["type"] = "pp"

    rec["date_created"] = [
        year_created,
    ]
    rec["date_published"] = year_published

    if "08Jun2016" in dataset_full_name:
        rec["date_reprocessed"] = "2016"
    else:
        rec["date_reprocessed"] = year_created

    rec["distribution"] = {}
    rec["distribution"]["formats"] = [aodformat.lower(), "root"]
    rec["distribution"]["number_events"] = get_number_events(dataset_full_name)
    rec["distribution"]["number_files"] = get_number_files(dataset_full_name)
    rec["distribution"]["size"] = get_size(dataset_full_name)

    rec["doi"] = get_doi(dataset_full_name)

    rec["experiment"] = "CMS"

    rec["files"] = []
    rec_files = get_dataset_index_files(dataset_full_name)
    for index_type in [".json", ".txt"]:
        index_files = [f for f in rec_files if f[0].endswith(index_type)]
        for file_number, (file_uri, file_size, file_checksum) in enumerate(index_files):
            rec["files"].append(
                {
                    "checksum": "adler32:" + file_checksum,
                    "description": dataset
                    + " %s dataset file index (" % aodformat
                    + str(file_number + 1)
                    + " of "
                    + str(len(index_files))
                    + ") for access to data via CMS virtual machine",
                    "size": file_size,
                    "type": "index" + index_type,
                    "uri": file_uri,
                }
            )

    rec["license"] = {}
    rec["license"]["attribution"] = "CC0"

    rec["methodology"] = {}
    rec["methodology"]["description"] = create_selection_information(
        dataset, dataset_full_name
    )

    rec["note"] = {}
    if run_period == "Run2015D":
        rec["note"][
            "description"
        ] = "This dataset contains all runs from 2015 RunD. The list of validated runs, which must be applied to all analyses, can be found in"
    rec["note"]["links"] = [
        {"recid": recid_validated_runs},
    ]

    rec["publisher"] = "CERN Open Data Portal"

    rec["recid"] = str(recid)

    rec["run_period"] = [
        run_period,
    ]

    rec["system_details"] = {}
    rec["system_details"]["global_tag"] = get_global_tag_for_system_details(
        dataset_full_name
    )
    rec["system_details"]["release"] = get_release_for_system_details(dataset_full_name)

    rec["title"] = dataset_full_name

    rec["title_additional"] = (
        dataset
        + " primary dataset in %s format from " % aodformat
        + run_period.replace(year_created, "")
        + " of "
        + year_created
        + " ("
        + dataset_full_name
        + ")"
    )

    rec["type"] = {}
    rec["type"]["primary"] = "Dataset"
    rec["type"]["secondary"] = [
        "Collision",
    ]

    rec["usage"] = {}
    rec["usage"][
        "description"
    ] = "You can access these data through the CMS Open Data container or the CMS Virtual Machine. See the instructions for setting up one of the two alternative environments and getting started in"
    rec["usage"]["links"] = [
        {
            "description": "Running CMS analysis code using Docker",
            "url": "/docs/cms-guide-docker",
        },
        {
            "description": "How to install the CMS Virtual Machine",
            "url": "/docs/cms-virtual-machine-2015",
        },
        {
            "description": "Getting started with CMS open data",
            "url": "/docs/cms-getting-started-2015",
        },
    ]

    rec["validation"] = {}
    rec["validation"][
        "description"
    ] = "During data taking all the runs recorded by CMS are certified as good for physics analysis if all subdetectors, trigger, lumi and physics objects (tracking, electron, muon, photon, jet and MET) show the expected performance. Certification is based first on the offline shifters evaluation and later on the feedback provided by detector and Physics Object Group experts. Based on the above information, which is stored in a specific database called Run Registry, the Data Quality Monitoring group verifies the consistency of the certification and prepares a json file of certified runs to be used for physics analysis. For each reprocessing of the raw data, the above mentioned steps are repeated. For more information see:"
    rec["validation"]["links"] = [
        {
            "description": "The Data Quality Monitoring Software for the CMS experiment at the LHC: past, present and future",
            "url": "https://www.epj-conferences.org/articles/epjconf/pdf/2019/19/epjconf_chep2018_02003.pdf",
        },
    ]

    return rec


def print_records(records):
    """Print records."""
    print("[")
    for (idx, rec) in enumerate(records):
        print(json.dumps(rec, indent=2, sort_keys=True))
        if idx == len(records) - 1:
            pass
        else:
            print(",")
    print("]")


@click.command()
def main():
    "Do the job."
    populate_fwyzard()
    populate_doiinfo()
    populate_selection_descriptions()

    records = []
    recid = RECID_START
    with open("./inputs/cms-2015-collision-datasets.txt", "r") as fdesc:
        for dataset_full_name in fdesc.readlines():
            dataset_full_name = dataset_full_name.strip()
            dataset = dataset_full_name.split("/")[1]
            run_period = dataset_full_name.split("/")[2].split("-", 1)[0]
            version = dataset_full_name.split("/")[2].split("-", 1)[1]
            aodformat = dataset_full_name.split("/")[3]
            records.append(
                create_record(recid, run_period, version, dataset, aodformat)
            )
            recid += 1

    # Enrich created records with AOD <-> MINIAOD links
    for record in records:
        if record["title"].endswith("/MINIAOD"):
            this_format = "MINIAOD"
            other_format = "AOD"
        elif record["title"].endswith("/AOD"):
            this_format = "AOD"
            other_format = "MINIAOD"
        else:
            continue
        related_record_title = record["title"].replace(
            f"/{this_format}", f"/{other_format}"
        )
        for other_record in records:
            if other_record["title"] == related_record_title:
                record["relations"] = [
                    {
                        "description": f"The corresponding {other_format} dataset:",
                        "recid": other_record["recid"],
                        "type": "isSiblingOf",
                    }
                ]

    print(
        json.dumps(
            records,
            indent=2,
            sort_keys=True,
            ensure_ascii=False,
            separators=(",", ": "),
        )
    )


if __name__ == "__main__":
    main()
