#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create RECO CMS Configuration Files records.
"""

import hashlib
import json
import re
import os


NOTE = 'This file describes the exact setup for the CMS software executable which ' \
       'was used in a data-processing step. It is provided only <i>for information ' \
       'purposes</i>. Although all the components required to <i>analyse</i> the public ' \
       'primary datasets - such as corresponding input data, condition data, software ' \
       'version - are provided on this portal, it is not necessarily possible to ' \
       '<i>reproduce</i> all the described data-processing steps.'


RECID_START = 7000


def get_content(afile):
    "Return full content of the configuration file."
    return open('./inputs/reco-config-files/' + afile, 'r').read()


def get_run_period(afile):
    "Return run period for configuration file."
    if '2012A' in afile:
        return 'Run2012A'
    if '2012B' in afile:
        return 'Run2012B'
    if '2012C' in afile:
        return 'Run2012C'
    if '2012D' in afile:
        return 'Run2012D'
    return 'FIXME'


def get_abstract(afile):
    "Return abstract for configuration file."
    process = get_process(afile)
    annotation = get_annotation(afile)
    abstract = 'The configuration file used in ' + process + ' data processing step'
    if 'nevts' in annotation:
        return abstract + "."
    else:
        return abstract + " for " + annotation + "."


def get_title(afile):
    "Return suitable title of configuration file."
    process = get_process(afile)
    return 'Configuration file for ' + process + ' step ' + get_python_filename(afile)


def get_python_filename(afile):
    "Return python_filename from configuration file."
    content = get_content(afile)
    python_filename = ''
    m = re.search(r"--python (.*)\.py", content)
    if m:
        python_filename = m.groups(1)[0]
    return os.path.basename(python_filename)


def get_annotation(afile):
    "Return annotation from configuration file."
    content = get_content(afile)
    annotation = ''
    m = re.search(r"annotation = cms.untracked.string\('(.*)'\)", content)
    if m:
        annotation = m.groups(1)[0]
    return annotation


def get_process(afile):
    "Return suitable title of configuration file."
    content = get_content(afile)
    process = 'UNKNOWN'
    m = re.search(r"process = cms.Process\(\s?['\"]([A-Z]+)['\"]\s?\)", content)
    if m:
        process = m.groups(1)[0]
    return process


def get_size(afile):
    """Return the size of the configuration file."""
    file_path = './inputs/reco-config-files/' + afile
    return os.path.getsize(file_path)


def get_checksum(afile):
    """Return the SHA1 checksum of the configuration file."""
    file_path = './inputs/reco-config-files/' + afile
    return hashlib.sha1(open(file_path, 'rb').read()).hexdigest()


def main():
    """Do the main job."""

    year_created = '2012'
    year_published = '2017'

    recid = RECID_START
    fdesc = open('./outputs/reco_config_files_link_info.py', 'w')
    fdesc.write('LINK_INFO = {\n')

    records = []

    for root, dirs, files in os.walk('./inputs/reco-config-files'):
        for afile in files:

            rec = {}

            rec['abstract'] = {}
            rec['abstract']['description'] = get_abstract(afile)

            rec['accelerator'] = "CERN-LHC"

            rec['collaboration'] = {}
            rec['collaboration']['name'] = 'CMS collaboration'
            rec['collaboration']['recid'] = '451'

            rec['collections'] = ['CMS-Configuration-Files', ]

            rec['collision_information'] = {}
            rec['collision_information']['energy'] = '8TeV'
            rec['collision_information']['type'] = 'pp'

            rec['date_created'] = year_created
            rec['date_published'] = year_published

            rec['distribution'] = {}
            rec['distribution']['formats'] = ['py', ]
            rec['distribution']['number_files'] = 1
            rec['distribution']['size'] = get_size(afile)

            rec['experiment'] = 'CMS'

            rec['files'] = [
                {
                    'checksum': get_checksum(afile),
                    'size': get_size(afile),
                    'uri': 'root://eospublic.cern.ch//eos/opendata/cms/configuration-files/2012/' + afile

                }
            ]

            rec['note'] = {}
            rec['note']['description'] = NOTE

            rec['publisher'] = 'CERN Open Data Portal'

            rec['recid'] = str(recid)

            rec['run_period'] = get_run_period(os.path.splitext(os.path.basename(afile))[0])

            rec['title'] = get_title(afile)

            rec['type'] = {}
            rec['type']['primary'] = 'Supplementaries'
            rec['type']['secondary'] = ['Configuration', ]

            records.append(rec)

            fdesc.write("  '%s': %d,\n" % (os.path.basename(afile).split('.', 1)[0], recid))
            recid += 1

    fdesc.write('}\n')
    fdesc.close()

    print(json.dumps(records, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
