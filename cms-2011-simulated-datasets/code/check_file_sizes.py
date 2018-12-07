#!/usr/bin/env python2

"""Check file sizes via various methods. Assumes some hard-coded paths."""

import re
from create_das_json_store import get_from_deep_json, get_das_json


MARC_FILE = '../../opendata.cern.ch/invenio_opendata/testsuite/data/cms/cms-simulated-datasets-Run2011A.xml'

def main():
    "Do the job."

    print "%10s | %10s | %10s | %10s | %10s | %15s | %15s | %15s" % ('RECORD_ID', 'DATASET', '#FILES/256', '#FILES/856', '#FILES/DAS', '#BYTES/256', '#BYTES/856', '#BYTES/DAS')
    print "%10s | %10s | %10s | %10s | %10s | %15s | %15s | %15s" % ('-' * 10, '-' * 10, '-' * 10, '-' * 10, '-' * 10, '-' * 15, '-' * 15, '-' * 15)

    record_id = 'UNKNOWN'
    bytes_via_256 = 0
    bytes_via_856 = 0
    files_via_256 = 0
    files_via_856 = 0
    title = 'UNKNOWN'
    total_titles = 0
    total_files_via_256 = 0
    total_files_via_856 = 0
    total_files_via_das = 0
    total_bytes_via_256 = 0
    total_bytes_via_856 = 0
    total_bytes_via_das = 0
    for line in open(MARC_FILE, 'r').readlines():
        if '</record>' in line:
            files_via_das = get_from_deep_json(get_das_json(title), 'nfiles')
            bytes_via_das = get_from_deep_json(get_das_json(title), 'size')
            total_files_via_das += files_via_das
            total_bytes_via_das += bytes_via_das
            total_files_via_256 += files_via_256
            total_bytes_via_256 += bytes_via_256
            total_files_via_856 += files_via_856
            total_bytes_via_856 += bytes_via_856
            print "%10s | %10s | %10s | %10s | %10s | %15s | %15s | %15s" % (record_id, title[:10], files_via_256, files_via_856, files_via_das, bytes_via_256, bytes_via_856, bytes_via_das)
            if files_via_856 != files_via_256:
                print 'Whoops!'
            if bytes_via_856 != bytes_via_256:
                print 'Whoops!'
            if files_via_856 != files_via_das:
                print 'Whoops!'
            if bytes_via_856 != bytes_via_das:
                print 'Whoops!'
            record_id = 'UNKNOWN'
            bytes_via_256 = 0
            bytes_via_856 = 0
            files_via_256 = 0
            files_via_856 = 0
            title = 'UNKNOWN'
        else:
            match = re.match(r'^\s+<controlfield tag="001">([0-9]+)</controlfield>\s+$', line)
            if match:
                record_id = match.groups()[0]
            match = re.match(r'^\s+<subfield code="s">([0-9]+)</subfield>\s+$', line)
            if match:
                bytes_via_856 += int(match.groups()[0])
                files_via_856 += 1
            match = re.match(r'^\s+<subfield code="b">([0-9]+)</subfield>\s+$', line)
            if match:
                bytes_via_256 = int(match.groups()[0])
            match = re.match(r'^\s+<subfield code="f">([0-9]+)</subfield>\s+$', line)
            if match:
                files_via_256 = int(match.groups()[0])
            match = re.match(r'^\s+<subfield code="a">(/.*AODSIM)</subfield>\s+$', line)
            if match:
                title = match.groups()[0]

    print "%10s | %10s | %10s | %10s | %10s | %15s | %15s | %15s" % ('TOTAL', '', total_files_via_256, total_files_via_856, total_files_via_das, total_bytes_via_256, total_bytes_via_856, total_bytes_via_das)

if __name__ == '__main__':
    main()
