#!/usr/bin/python3

import click
import json
import os
import re


def parse_dataset_title(title):
    """Return tuple (dataset, release, version, format) from the CMS dataset title.

    Example title:

       /TTJets_MSDecays_scaleup_mt172_5_7TeV-madgraph-tauola/Summer11LegDR-PU_S13_START53_LV6-v1/AODSIM

    Exmaple output:

       ('TTJets_MSDecays_scaleup_mt172_5_7TeV-madgraph-tauola',
        'Summer11LegDR',
        'PU_S13_START53_LV6-v1',
        'AODSIM')
    """
    dummy, title_dataset, title_release_and_version, title_format = title.split('/')
    title_release, title_version = title_release_and_version.split('-', 1)
    return (title_dataset, title_release, title_version, title_format)


def get_file_information(rootfilepath, eoslsfile):
    """Return file information for given rootfilepath.

    Example input rootfilepath:

       /Summer11LegDR/Vector1MToZZTo4L_M-125p6_7TeV-JHUGenV3-pythia6/AODSIM/PU_S13_START53_LV6-v1/

    Example input eoslsfile:

       path=root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/Vector1MToZZTo4L_M-125p6_7TeV-JHUGenV3-pythia6/AODSIM/PU_S13_START53_LV6-v1/file-indexes/CMS_MonteCarlo2011_Summer11LegDR_Vector1MToZZTo4L_M-125p6_7TeV-JHUGenV3-pythia6_AODSIM_PU_S13_START53_LV6-v1_20000_file_index.json size=7203 checksum=1915b96e
path=root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/Vector1MToZZTo4L_M-125p6_7TeV-JHUGenV3-pythia6/AODSIM/PU_S13_START53_LV6-v1/file-indexes/CMS_MonteCarlo2011_Summer11LegDR_Vector1MToZZTo4L_M-125p6_7TeV-JHUGenV3-pythia6_AODSIM_PU_S13_START53_LV6-v1_20000_file_index.txt size=4116 checksum=f8b8e698

    Example output:

        [
            {
                "checksum": "adler32:1915b96e",
                "size": 7203,
                "type": "index.json",
                "uri": "root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/Vector1MToZZTo4L_M-125p6_7TeV-JHUGenV3-pythia6/AODSIM/PU_S13_START53_LV6-v1/file-indexes/CMS_MonteCarlo2011_Summer11LegDR_Vector1MToZZTo4L_M-125p6_7TeV-JHUGenV3-pythia6_AODSIM_PU_S13_START53_LV6-v1_20000_file_index.json"
            },
            {
                "checksum": "adler32:f8b8e698",
                "size": 4116,
                "type": "index.txt",
                "uri": "root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/Vector1MToZZTo4L_M-125p6_7TeV-JHUGenV3-pythia6/AODSIM/PU_S13_START53_LV6-v1/file-indexes/CMS_MonteCarlo2011_Summer11LegDR_Vector1MToZZTo4L_M-125p6_7TeV-JHUGenV3-pythia6_AODSIM_PU_S13_START53_LV6-v1_20000_file_index.txt"
            }
        ]


    """
    found_p = False
    files = []
    for line in open(eoslsfile, 'r').readlines():
        if rootfilepath + 'file-indexes/' in line:
            match = re.match(r'^path=(.*) size=(.*) checksum=(.*)$', line)
            if match:
                path, size, checksum = match.groups()
                if path.endswith('_file_index.txt'):
                    found_p = True
                    files.append({'checksum': 'adler32:' + checksum,
                                'size': int(size),
                                'type': 'index.txt',
                                'uri': path})
                elif path.endswith('_file_index.json'):
                    found_p = True
                    files.append({'checksum': 'adler32:' + checksum,
                                'size': int(size),
                                'type': 'index.json',
                                'uri': path})
                else:
                    raise Exception('This should not happen :)')
    if not found_p:
        raise Exception('Cannot find index files for dataset ' + rootfilepath)
    return files


@click.command()
@click.argument('recordfile', type=click.Path(exists=True))
@click.argument('eoslsfile', type=click.Path(exists=True))
def main(recordfile, eoslsfile):
    "Alter record file to include EOS file information."

    # read records
    recordfile_content = open(recordfile, 'r').read()
    records = json.loads(recordfile_content)

    # amend records
    for record in records:
        title_dataset, title_release, title_version, title_format = parse_dataset_title(record['title'])
        rootfilepath = '/' + title_release + '/' + title_dataset + '/' + title_format + '/' + title_version + '/'
        record['files'] = get_file_information(rootfilepath, eoslsfile)

    # print records
    new_content = json.dumps(records, indent=2, sort_keys=records)
    for line in new_content.split('\n'):
        line = line.rstrip()
        print(line)


if __name__ == '__main__':
    #print(json.dumps(get_file_information('/Summer11LegDR/Vector1MToZZTo4L_M-125p6_7TeV-JHUGenV3-pythia6/AODSIM/PU_S13_START53_LV6-v1/', '/home/simko/z.txt')))
    main()
