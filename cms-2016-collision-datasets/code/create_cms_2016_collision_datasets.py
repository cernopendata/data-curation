#!/usr/bin/env python
# noqa: E501


"""
Create CMS 2016 open data release collision datasets.
"""

import click
import csv
import datetime
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

DATASET_TRIGGER_LIST = {}

SELECTION_DESCRIPTIONS = {}

LINK_INFO = {}
exec(open("./outputs/reco_config_files_link_info.py", "r").read())

DOI_INFO = {}

CONTAINERIMAGES_CACHE = {}

RECID_START = 30500
RECID_VALIDATED_RUNS = "14220"
YEAR_PUBLISHED = "2024"
YEAR_CREATED = "2016"
COLLISION_TYPE = "pp"
COLLISION_ENERGY = "13TeV"

RECOMMENDED_IMAGES_FOR_NANOAOD_DESCRIPTION = """<p>NANOAOD datasets are in the <a href="https://root.cern.ch/">ROOT</a> tree format and their analysis does not require the use of CMSSW or CMS open data environments. They can be analysed with common ROOT and Python tools.<p>"""
RECOMMENDED_IMAGES_FOR_NANOAOD = [
    {
        "name": "gitlab-registry.cern.ch/cms-cloud/root-vnc",
        "registry": "gitlab",
    },
    {
        "name": "gitlab-registry.cern.ch/cms-cloud/python-vnc",
        "registry": "gitlab",
    },
]

USAGE_FOR_NANOAOD_DESCRIPTION = """You can access these data through XRootD protocol or direct download, and they can be analysed with common ROOT and Python tools. See the instructions for getting started in"""
USAGE_FOR_NANOAOD_LINKS = [
    {
        "description": "Using Docker containers",
        "url": "/docs/cms-guide-docker#nanoaod",
    },
    {
        "description": "Getting started with CMS NanoAOD",
        "url": "/docs/cms-getting-started-nanoaod",
    },
]


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


def populate_dataset_trigger_list():
    """Populate DATASET_TRIGGER_LIST dictionary (dataset -> trigger list)."""
    for line in open("./inputs/hlt-2016-dataset.txt", "r").readlines():
        line = line.strip()
        dataset, trigger = line.split(",")
        if trigger.endswith("_v"):
            trigger = trigger[:-2]
        if dataset in DATASET_TRIGGER_LIST.keys():
            DATASET_TRIGGER_LIST[dataset].append(trigger)
        else:
            DATASET_TRIGGER_LIST[dataset] = [
                trigger,
            ]


def populate_doiinfo():
    """Populate DOI_INFO dictionary (dataset -> doi)."""
    for line in open("./inputs/doi-col.txt", "r").readlines():
        dataset, doi = line.split()
        DOI_INFO[dataset] = doi


def populate_containerimages_cache():
    """Populate CONTAINERIMAGES cache (dataset -> system_details.container_images)"""
    with open("../cms-release-info/cms_release_container_images_info.json") as f:
        content = json.loads(f.read())
        for key in content.keys():
            CONTAINERIMAGES_CACHE[key] = content[key]


def populate_selection_descriptions():
    """Populate SELECTION_DESCRIPTIONS dictionary (dataset -> selection description)."""
    for input_file in ["./inputs/CMSDatasetDescription_Run2016.csv"]:
        with open(input_file, "r") as csvfile:
            for line_values in csv.reader(csvfile, delimiter=":"):
                dataset, description = line_values
                SELECTION_DESCRIPTIONS[dataset] = description


def get_release_for_processing(dataset_full_name):
    """Return CMSSW release info for the given dataset for the processing step."""
    p = subprocess.run(
        ["dasgoclient", "-query", f"release dataset={dataset_full_name}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    release = p.stdout.decode().strip()
    return release


def get_release_for_system_details(dataset_full_name):
    """Return CMSSW release info for the given dataset for the system details."""
    return "CMSSW_10_6_30"


def get_global_tag_for_processing(dataset_full_name):
    """Return global tag info for the given dataset for the processing steps."""
    config_file_name = get_dataset_config_file_name(dataset_full_name)
    content = open("./outputs/" + f"{config_file_name}.py", "r").read()
    processing_global_tag = ""
    pattern = r"process\.GlobalTag = GlobalTag\(process\.GlobalTag, '([^']*)'"
    m = re.search(pattern, content)
    if m:
        processing_global_tag = m.group(1)
    processing_global_tag = processing_global_tag.strip()
    return processing_global_tag


def get_global_tag_for_system_details(dataset_full_name):
    """Return global tag info for the given dataset for the system details."""
    return "106X_dataRun2_v37"


def get_date_reprocessed(dataset_full_name):
    """Return the reprocessing date for the given dataset."""
    p = subprocess.run(
        ["dasgoclient", "-query", f"dataset={dataset_full_name}", "-json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    json_object = json.loads(p.stdout.decode())
    all_creation_dates = []
    for obj in json_object:
        dataset = obj["dataset"][0]
        if "creation_date" in dataset.keys():
            date = dataset["creation_date"]
            all_creation_dates.append(date)
    date_reprocessed_timestamp = all_creation_dates[0]
    isUnique = len(set(all_creation_dates)) == 1
    if not isUnique:
        print(
            f"{dataset_full_name} has multiple reprocessing dates associated with it!"
        )
    date_reprocessed = datetime.date.fromtimestamp(date_reprocessed_timestamp).year
    return str(date_reprocessed)


def get_run_numbers(dataset_full_name):
    """Return the run numbers for the given dataset."""
    p = subprocess.run(
        ["dasgoclient", "-query", f"run dataset={dataset_full_name}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    run_numbers = p.stdout.decode().strip().split("\n")
    run_numbers.sort()
    return run_numbers


def get_dataset_config_file_name(dataset_full_name):
    dataset = dataset_full_name.split("/")[1]    
    run_period = dataset_full_name.split("/")[2].split("-", 1)[0]
    version = dataset_full_name.split("/")[2].split("-")[1]
    config_file = f"ReReco-{run_period}-{dataset}-{version}"
    if "/AOD" in dataset_full_name:
        config_file = f"recoskim_{run_period}_{dataset}"
        if "DoubleMuonLowMass" in dataset_full_name:
            config_file = f"ReReco-{run_period}-{dataset}-{version}"
    return config_file


def get_parent_dataset(dataset_full_name):
    """Return the parent dataset for the given dataset."""
    p = subprocess.run(
        ["dasgoclient", "-query", f"parent dataset={dataset_full_name}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    parent = p.stdout.decode().strip()
    return parent


def create_selection_information(dataset, dataset_full_name):
    """Create box with selection information."""
    if "/MINIAOD" in dataset_full_name:
        aodformat = "MINIAOD"
    else:
        aodformat = "NANOAOD"
    out = ""
    # description:
    out += "<p>"
    out += SELECTION_DESCRIPTIONS.get(dataset_full_name, "")
    out += "</p>"
    # data taking / HLT:
    out += "<p><strong>Data taking / HLT</strong>"
    out += '<br/>The collision data were assigned to different RAW datasets using the following <a href="/record/30300">HLT configuration</a>.</p>'
    # data processing / NANO/PAT/RECO:
    run_period = re.search(r"(Run[0-9]+.)", dataset_full_name).groups()[0]
    aodformat = dataset_full_name.split("/")[3]
    step_dataset = dataset_full_name
    steps = []
    if aodformat == "NANOAOD":
        steps = [
            {"process": "NANO"},
            {"process": "PAT"},
            {"process": "RECO"}
        ]
    else:
        steps = [
            {"process": "PAT"},
            {"process": "RECO"}
        ]
    
    out += f"<p><strong>Data processing </strong>"
    out += (
        "<br/>This %s dataset was processed from the RAW dataset by the following steps: "
        % (aodformat)
    )
    out += "<br/>"

    afile = get_dataset_config_file_name(dataset_full_name)
    step_dataset = dataset_full_name
    for i in range(len(steps)):
        generator_text = "Configuration file for " + steps[i]['process'] + " step " + afile
        release = get_release_for_processing(step_dataset)
        global_tag = get_global_tag_for_processing(step_dataset)
    
        out += "<br/><strong>Step %s </strong>" % steps[i]['process']
        out += "<br/>Release: %s" % release
        out += "<br/>Global tag: %s" % global_tag
        out += '\n        <br/><a href="/record/%s">%s</a>' % (
            LINK_INFO.get(afile, ""),
            generator_text,
        )
        out += "<br/>Output dataset: %s" % step_dataset
        out += "\n        </p>"
        if steps[i]['process'] != "RECO":
            step_dataset = get_parent_dataset(step_dataset)
            afile = get_dataset_config_file_name(step_dataset)

    # HLT trigger paths:
    out += "<p><strong>HLT trigger paths</strong>"
    out += '<br/>The possible <a href="/docs/cms-guide-trigger-system#hlt-trigger-path-definitions">HLT trigger paths</a> in this dataset are:'
    trigger_paths = get_trigger_paths_for_dataset(dataset)
    for trigger_path in trigger_paths:
        out += (
            '<br/><a href="/search?q=%s&subtype=Trigger&type=Supplementaries&year=%s">%s</a>'
            % (trigger_path, YEAR_CREATED, trigger_path)
        )
    out += "</p>"
    return out


def get_trigger_paths_for_dataset(dataset):
    """Return list of trigger paths for given dataset."""
    return DATASET_TRIGGER_LIST.get(dataset, [])


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

    dataset_full_name = (
        "/" + dataset + "/" + run_period + "-" + version + "/" + aodformat
    )

    run_numbers = get_run_numbers(dataset_full_name)

    rec["abstract"] = {}
    rec["abstract"]["description"] = (
        "<p>"
        + dataset
        + f" primary dataset in %s format from Run{run_period[-1]} of {YEAR_CREATED}. Run period from run number {run_numbers[0]} to {run_numbers[-1]}."
        % aodformat
        + "</p><p>The list of validated runs, which must be applied to all analyses, either with the full validation or for an analysis requiring only muons, can be found in:</p>"
    )
    rec["abstract"]["links"] = [
        {"description": "Validated runs, full validation", "recid": "14220"},
        {"description": "Validated runs, muons only", "recid": "14221"},
    ]

    rec["accelerator"] = "CERN-LHC"

    rec["collaboration"] = {}
    rec["collaboration"]["name"] = "CMS Collaboration"
    rec["collaboration"]["recid"] = ""

    rec["collections"] = [
        "CMS-Primary-Datasets",
    ]

    rec["collision_information"] = {}
    rec["collision_information"]["energy"] = COLLISION_ENERGY
    rec["collision_information"]["type"] = COLLISION_TYPE

    rec["date_created"] = [
        YEAR_CREATED,
    ]
    rec["date_published"] = YEAR_PUBLISHED

    rec["date_reprocessed"] = get_date_reprocessed(dataset_full_name)

    rec["distribution"] = {}
    rec["distribution"]["formats"] = [aodformat.lower(), "root"]
    rec["distribution"]["number_events"] = get_number_events(dataset_full_name)
    rec["distribution"]["number_files"] = get_number_files(dataset_full_name)
    rec["distribution"]["size"] = get_size(dataset_full_name)

    rec["doi"] = get_doi(dataset_full_name)

    rec["experiment"] = [
        "CMS"
    ]

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
    rec["note"][
        "description"
    ] = "The list of validated runs, which must be applied to all analyses, can be found in"
    rec["note"]["links"] = [
        {"recid": RECID_VALIDATED_RUNS},
    ]

    rec["publisher"] = "CERN Open Data Portal"

    rec["recid"] = str(recid)

    rec["run_numbers"] = run_numbers

    rec["run_period"] = [
        run_period,
    ]

    rec["system_details"] = {}
    global_tag = get_global_tag_for_system_details(dataset_full_name)
    cmssw_release = get_release_for_system_details(dataset_full_name)
    if aodformat == "NANOAOD":
        rec["system_details"][
            "description"
        ] = RECOMMENDED_IMAGES_FOR_NANOAOD_DESCRIPTION
        rec["system_details"]["container_images"] = RECOMMENDED_IMAGES_FOR_NANOAOD
    else:
        rec["system_details"]["global_tag"] = global_tag
        rec["system_details"]["release"] = cmssw_release
        if cmssw_release in CONTAINERIMAGES_CACHE.keys():
            rec["system_details"]["container_images"] = CONTAINERIMAGES_CACHE[
                cmssw_release
            ]

    rec["title"] = dataset_full_name

    rec["title_additional"] = (
        dataset
        + " primary dataset in %s format from " % aodformat
        + run_period.replace(YEAR_CREATED, "")
        + " of "
        + YEAR_CREATED
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
    if aodformat == "NANOAOD":
        rec["usage"]["description"] = USAGE_FOR_NANOAOD_DESCRIPTION
        rec["usage"]["links"] = USAGE_FOR_NANOAOD_LINKS
    else:
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
                "url": "/docs/cms-virtual-machine-2016-2018",
            },
            {
                "description": "Getting started with CMS open data",
                "url": "/docs/cms-getting-started-miniaod",
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
    for idx, rec in enumerate(records):
        print(json.dumps(rec, indent=2, sort_keys=True))
        if idx == len(records) - 1:
            pass
        else:
            print(",")
    print("]")


@click.command()
def main():
    "Do the job."
    populate_dataset_trigger_list()
    populate_doiinfo()
    populate_containerimages_cache()
    populate_selection_descriptions()

    records = []
    recid = RECID_START
    with open("./inputs/cms-2016-collision-datasets.txt", "r") as fdesc:
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

    # Enrich created records with MINIAOD <-> NANOAOD links
    for record in records:
        if record["title"].endswith("/MINIAOD"):
            other_format = "NANOAOD"
            related_type = "isChildOf"
            org_title = record["title"].rsplit("-", 1)[0]
        elif record["title"].endswith("/NANOAOD"):
            other_format = "MINIAOD"
            related_type = "isParentOf"
            org_title = record["title"].rsplit("_", 1)[0]
        else:
            continue
        for other_record in records:
            if (
                org_title in other_record["title"]
                and record["title"] != other_record["title"]
            ):
                record["relations"] = [
                    {
                        "description": f"The corresponding {other_format} dataset:",
                        "recid": other_record["recid"],
                        "type": related_type,
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
