#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Create CMS Configuration Files records found in primary datasets.
"""

import re
import os
import sys

RECORD_TEMPLATE = """\
  <record>
    <controlfield tag="001">%(recid)s</controlfield>
    <datafield tag="035" ind1=" " ind2=" ">
      <subfield code="a">%(sha1)s</subfield>
      <subfield code="9">CMS-ConfDB</subfield>
    </datafield>
    <datafield tag="110" ind1=" " ind2=" ">
      <subfield code="a">CMS collaboration</subfield>
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
      <subfield code="a">%(abstract)s</subfield>
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
    <datafield tag="980" ind1=" " ind2=" ">
      <subfield code="b">Research</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">/tmp/opendata.cern.ch-fft-file-cache/cms-configuration-files/%(afile)s</subfield>
      <subfield code="n">configFile</subfield>
      <subfield code="f">py</subfield>
    </datafield>
  </record>"""


def get_content(afile):
    "Return full content of the configuration file."
    try:
        return open('./inputs/config-store/' + afile, 'r').read()
    except:
        return ""


def get_title(afile):
    "Return suitable title of configuration file."
    return 'Configuration file for ' + get_process(afile) + ' step ' + get_python_filename(afile)


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


def get_abstract(afile):
    "Return abstract for configuration file."
    process = get_process(afile)
    annotation = get_annotation(afile)
    abstract = 'The configuration file used in ' + process + ' data processing step'
    if 'nevts' in annotation:
        return abstract + "."
    else:
        return abstract + " for " + annotation + "."


def get_process(afile):
    "Return suitable title of configuration file."
    content = get_content(afile)
    process = 'UNKNOWN'
    m = re.search(r"process = cms.Process\('([A-Z]+)'\)", content)
    if m:
        process = m.groups(1)[0]
    return process


def main():
    """Do the main job."""

    print "<collection>"
    sys.stderr.write("LINK_INFO = {\n")
    recid = 3601
    for root, dirs, files in os.walk('./inputs/config-store'):
        for afile in files:
            print RECORD_TEMPLATE % \
                {
                    'recid': str(recid),
                    'afile': afile,
                    'title': get_title(afile),
                    'sha1': os.path.basename(afile).split('.', 1)[0],
                    'process': get_process(afile),
                    'abstract': get_abstract(afile),
                }
            sys.stderr.write("  '%s': %d,\n" % (os.path.basename(afile).split('.', 1)[0], recid))
            recid += 1
    sys.stderr.write("}\n")
    print "</collection>"


if __name__ == '__main__':
    main()
