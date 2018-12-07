#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Download JSON from CMS DAS.
"""

import json
import os
import subprocess


def get_from_deep_json(data, akey):
    "Traverse DATA and return first value matching AKEY."
    if type(data) is dict:
        if data.has_key(akey):
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


def get_das_json(dataset):
    "Get JSON from CMS DAS for the given dataset."
    filepath = './inputs/das-json-store/%s.json' % escape_for_filename(dataset)
    if os.path.isfile(filepath):
        with open(filepath, 'r') as filestream:
            return json.load(filestream)
    else:
        return json.loads(subprocess.check_output(["python", "../cms-2011-collision-datasets/das.py",
                                                   "--query",
                                                   "dataset="+dataset,
                                                   "--format=json"]))


def get_input_dataset(das):
    """Return input dataset for the current dataset."""
    return get_from_deep_json(das, 'input_dataset')


def escape_for_filename(dataset):
    """Escape dataset title so that it's suitable to be used as filename."""
    return dataset.replace('/', '@')


def store_das_json(dataset, das):
    """Store DAS json for dataset."""
    filepath = './inputs/das-json-store/%s.json' % escape_for_filename(dataset)
    if os.path.isfile(filepath):
        print "Whoops! File %s exists already. Skipping." % filepath
        # sys.exit(1)
    with open(filepath, 'w') as filestream:
        json.dump(das, filestream)


def process_dataset(dataset):
    """Process this dataset and return its parent."""
    das = get_das_json(dataset)
    store_das_json(dataset, das)
    return get_input_dataset(das)


def main():
    """Do the job."""
    for title in open('./inputs/cms-mc-nov-2015.txt', 'rb').readlines():
        input_dataset = title.strip()
        while input_dataset:
            input_dataset = process_dataset(input_dataset)


if __name__ == '__main__':
    main()
