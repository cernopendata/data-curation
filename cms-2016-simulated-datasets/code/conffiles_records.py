#!/usr/bin/env python


"""
Create MC 2016 records.
"""

import hashlib
import json
import re
import os
import subprocess
import sys
from urllib.request import urlopen

from utils import get_from_deep_json, \
                  populate_doiinfo, \
                  get_dataset_format, \
                  get_dataset_year, \
                  get_author_list_recid, \
                  get_doi
from das_json_store import get_das_store_json, \
                           get_parent_dataset
from eos_store import XROOTD_URI_BASE, \
                      get_dataset_index_file_base, \
                      get_dataset_location
from mcm_store import get_mcm_dict, \
                      get_global_tag, \
                      get_genfragment_url, \
                      get_generator_name, \
                      get_dataset_energy, \
                      get_cmsDriver_script
from config_store import get_conffile_ids_all_chain_steps
from categorisation import guess_title_category
from dataset_records import get_dataset, \
                            newer_dataset_version_exists


def create_record(conf_id, conffiles_dir):
    """Create record for the given dataset."""

    rec = {}

    with open(conffiles_dir + '/' + conf_id + '.configFile') as myfile:
        rec['cms_confdb_id'] = conf_id
        rec['script'] = myfile.read()

    return rec


def create_records(conf_ids, conffiles_dir):
    """Create records."""

    records = []
    for conf_id in conf_ids:
        records.append(create_record(conf_id, conffiles_dir))
    return records


def main(datasets, eos_dir, das_dir, mcm_dir, conffiles_dir):
    "Do the job."

    dataset_full_names = []
    for dataset_full_name in datasets:
        if newer_dataset_version_exists(dataset_full_name, datasets):
            print('[ERROR] Ignoring older dataset version ' + dataset_full_name,
                  file=sys.stderr)
        else:
            dataset_full_names.append(dataset_full_name)

    conffiles = []
    for ds in dataset_full_names:
        # this returns config_ids for all steps in the processing chain of the dataset
        config_ids = get_conffile_ids_all_chain_steps(ds, mcm_dir)
        if config_ids:
            for config_id in config_ids:
                if config_id not in conffiles:
                    conffiles.append(config_id)

    records = create_records(conffiles, conffiles_dir)
    json.dump(records, indent=2, sort_keys=True, ensure_ascii=True, fp=sys.stdout)
