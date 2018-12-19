#!/usr/bin/env python3

"""
Take EOS find command output and create JSON file list snippet.

Example command:

$ eos find --xurl --size --checksum /eos/opendata/cms/software/HiggsExample20112012

Example input:

$ head -3 ../inputs/HiggsExample20112012-file-list.txt
path=root://eospublic.cern.ch//eos/opendata/cms/software/HiggsExample20112012/BuildFile.xml size=305 checksum=ff63668a
path=root://eospublic.cern.ch//eos/opendata/cms/software/HiggsExample20112012/DY1011.root size=66215 checksum=90cb6b24
path=root://eospublic.cern.ch//eos/opendata/cms/software/HiggsExample20112012/DY1012.root size=67648 checksum=a55fe748

Example output:

$ python code/create_json_file_list_snippet.py ./inputs/HiggsExample20112012-file-list.txt
{
  "files": [
    {
      "checksum": "adler32:ff63668a",
      "size": "305",
      "uri": "root://eospublic.cern.ch//eos/opendata/cms/software/HiggsExample20112012/BuildFile.xml"
    },
    {
      "checksum": "adler32:90cb6b24",
      "size": "66215",
      "uri": "root://eospublic.cern.ch//eos/opendata/cms/software/HiggsExample20112012/DY1011.root"
    },
    {
      "checksum": "adler32:a55fe748",
      "size": "67648",
      "uri": "root://eospublic.cern.ch//eos/opendata/cms/software/HiggsExample20112012/DY1012.root"
    },
  ]
}
"""

import click
import json
import re


@click.command()
@click.argument('filename', type=click.Path(exists=True))
def main(filename):
    "Do the job."
    rec = {}
    files = []
    for line in open(filename, 'r').readlines():
        line = line.strip()
        match = re.search(r'^path=(.*) size=(.*) checksum=(.*)', line)
        if match:
            path, size, checksum = match.groups()
            if True:  # and not path.endswith('.root'):
                if path.endswith('_file_index.txt'):
                    files.append({
                        'checksum': 'adler32:' + checksum,
                        'size': int(size),
                        'type': 'index.txt',
                        'uri': path
                    })
                elif path.endswith('_file_index.json'):
                    files.append({
                        'checksum': 'adler32:' + checksum,
                        'size': int(size),
                        'type': 'index.json',
                        'uri': path
                    })
                else:
                    files.append({
                        'checksum': 'adler32:' + checksum,
                        'size': int(size),
                        'uri': path
                    })
    rec['files'] = files
    print(json.dumps(rec, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
