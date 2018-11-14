#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Create CMS Trigger Information records.
"""

import glob
import os


TEMPLATE_FFT = """\
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">/tmp/opendata.cern.ch-fft-file-cache/cms-trigger-information/%(filename)s</subfield>
    </datafield>"""

TEMPLATE_TOC = """\
      <tr><td>%(runs)s</td><td><a href="https://github.com/cms-sw/cmssw/tree/%(cmssw)s">%(cmssw)s</a></td><td><a href="files/%(filename)s">%(title)s</a></td></tr>"""


def main():
    """Do the main job."""

    for line in open('./inputs/trigger-information.txt', 'r').readlines():
        cmssw, title, runs = line.split(' ', 2)
        runs = runs.strip()
        runs = runs.replace('(run ', '')
        runs = runs.replace('(runs ', '')
        runs = runs.replace(')', '')
        filename = title.replace('/', '_')[1:] + '.py'
        if os.path.exists('../../opendata.cern.ch/invenio_opendata/testsuite/data/cms/cms-hlt-2011-configuration-files' + os.sep + filename):
            if True:
                print TEMPLATE_TOC % {
                    'filename': filename,
                    'cmssw': cmssw,
                    'title': title,
                    'runs': runs,
                }
            else:
                print TEMPLATE_FFT % {
                    'filename': filename,
                    'cmssw': cmssw,
                    'title': title,
                    'runs': runs,
                }


if __name__ == '__main__':
    main()
