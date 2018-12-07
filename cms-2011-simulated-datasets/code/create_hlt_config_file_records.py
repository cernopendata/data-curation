#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Create HLT CMS Configuration Files records.
"""

import re
import os
import sys

RECORD_TEMPLATE = """\
  <record>
    <controlfield tag="001">%(recid)s</controlfield>
    <datafield tag="110" ind1=" " ind2=" ">
      <subfield code="a">CMS collaboration</subfield>
      <subfield code="w">451</subfield>
    </datafield>
    <datafield tag="245" ind1=" " ind2=" ">
      <subfield code="a">%(title)s</subfield>
    </datafield>
    <datafield tag="260" ind1=" " ind2=" ">
      <subfield code="b">CERN Open Data Portal</subfield>
      <subfield code="c">2016</subfield>
    </datafield>
    <datafield tag="264" ind1=" " ind2="0">
      <subfield code="c">2011</subfield>
    </datafield>
    <datafield tag="520" ind1=" " ind2=" ">
      <subfield code="a">%(description)s</subfield>
    </datafield>
    <datafield tag="556" ind1=" " ind2=" ">
      <subfield code="a"><![CDATA[ This file describes the exact setup for the
      CMS software executable which was used in a data-processing step. It is
      provided only <i>for information purposes</i>. Although all the components
      required to <i>analyse</i> the public primary datasets - such as
      corresponding input data, condition data, software version - are provided
      on this portal, it is not necessarily possible to <i>reproduce</i> all the
      described data-processing steps. ]]></subfield>
    </datafield>
    <datafield tag="693" ind1=" " ind2=" ">
      <subfield code="a">CERN-LHC</subfield>
      <subfield code="e">CMS</subfield>
    </datafield>
    <datafield tag="942" ind1=" " ind2=" ">
      <subfield code="e">7TeV</subfield>
    </datafield>
    <datafield tag="964" ind1=" " ind2="0">
      <subfield code="c">Run2011A</subfield>
    </datafield>
    <datafield tag="980" ind1=" " ind2=" ">
      <subfield code="a">CMS-Configuration-Files</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">/tmp/opendata.cern.ch-fft-file-cache/cms-hlt-2011-configuration-files/%(afile)s</subfield>
    </datafield>
  </record>"""


def get_content(afile):
    "Return full content of the configuration file."
    return open('./inputs/hlt-2011-configuration-files/' + afile, 'r').read()


def get_title(afile):
    "Return suitable title of configuration file."
    process = get_process(afile)
    tablename = get_tablename(afile)
    return 'Configuration file for ' + process + ' step ' + tablename


def get_tablename(afile):
    "Return tableName for configuration file."
    content = get_content(afile)
    tablename = ''
    m = re.search(r"tableName = cms.string\(\s?'(.*)'\s?\)", content)
    if m:
        tablename = m.groups(1)[0]
    return tablename


def get_process(afile):
    "Return suitable title of configuration file."
    content = get_content(afile)
    process = 'UNKNOWN'
    m = re.search(r"process = cms.Process\( \"([A-Z]+)\" \)", content)
    if m:
        process = m.groups(1)[0]
    return process


def get_run_numbers_and_software(tablename):
    "Return run numbers and software for given configuration."
    for line in open('./inputs/trigger-information.txt', 'r').readlines():
        cmssw, title, runs = line.split(' ', 2)
        runs = runs.strip()
        runs = runs.replace('(run ', '')
        runs = runs.replace('(runs ', '')
        runs = runs.replace(')', '')
        if title == tablename:
            return (runs, cmssw)
    return None


def create_rich_description(afile):
    "Return suitable description text for the configuration file."
    out = ''
    process = get_process(afile)
    tablename = get_tablename(afile)
    more_info = get_run_numbers_and_software(tablename)
    if more_info:
        out += '<![CDATA[ '
    out += 'The configuration file used in data taking and %(process)s data processing step.' % {
        'process': process
    }
    if more_info:
        run_number = more_info[0]
        cmssw = more_info[1]
        out += '<p>Run number %(run_number)s, software version <a href="https://github.com/cms-sw/cmssw/tree/%(cmssw)s">%(cmssw)s</a>.</p>' % {
            'run_number': run_number,
            'cmssw': cmssw
        }
        out += ']]>'
    return out


def main():
    """Do the main job."""

    print "<collection>"
    recid = 3500
    for root, dirs, files in os.walk('./inputs/hlt-2011-configuration-files'):
        for afile in files:
            print RECORD_TEMPLATE % \
                {
                    'recid': str(recid),
                    'afile': afile,
                    'title': get_title(afile),
                    'process': get_process(afile),
                    'description': create_rich_description(afile),
                }
            sys.stderr.write("  '%s': %d,\n" % (get_tablename(afile), recid))
            recid += 1
    print "</collection>"


if __name__ == '__main__':
    main()
