#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
Create CMS L1 trigger Information records.
"""

import os
import re


TOC_RECORD_TEMPLATE = """\
  <record>
    <controlfield tag="001">%(recid)s</controlfield>
    <datafield tag="110" ind1=" " ind2=" ">
        <subfield code="a">CMS collaboration</subfield>
        <subfield code="w">451</subfield>
    </datafield>
    <datafield tag="245" ind1=" " ind2=" ">
        <subfield code="a">L1 trigger information for 2011 CMS open data</subfield>
    </datafield>
    <datafield tag="260" ind1=" " ind2=" ">
        <subfield code="b">CERN Open Data Portal</subfield>
        <subfield code="c">2016</subfield>
    </datafield>
    <datafield tag="264" ind1=" " ind2="0">
        <subfield code="c">2011</subfield>
    </datafield>
    <datafield tag="520" ind1=" " ind2=" ">
        <subfield code="a"><![CDATA[
        <table class="table">
        <thead>
        <tr><th>Starting from run</th><th>L1 trigger information</th></tr>
        </thead>
        <tbody>
        <tr><td>157942</td><td><a href="/record/3701">L1Menu_Collisions2011_v0_L1T_Scales_20101224_Imp0_0x101e</td></tr>
        <tr><td>161205</td><td><a href="/record/3702">L1Menu_Collisions2011_v1_L1T_Scales_20101224_Imp0_0x101f</td></tr>
        <tr><td>161568</td><td><a href="/record/3703">L1Menu_Collisions2011_v2_L1T_Scales_20101224_Imp0_0x1020</td></tr>
        <tr><td>165897</td><td><a href="/record/3704">L1Menu_Collisions2011_v3_L1T_Scales_20101224_Imp0_0x1021</td></tr>
        <tr><td>170065</td><td><a href="/record/3705">L1Menu_Collisions2011_v4_L1T_Scales_20101224_Imp0_0x1022</td></tr>
        <tr><td>173212</td><td><a href="/record/3706">L1Menu_Collisions2011_v5_L1T_Scales_20101224_Imp0_0x1023</td></tr>
        <tr><td>176725</td><td><a href="/record/3707">L1Menu_Collisions2011_v6_L1T_Scales_20101224_Imp0_0x1024</td></tr>
        </tbody>
        </table>
        ]]></subfield>
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
        <subfield code="a">CMS-Trigger-Information</subfield>
    </datafield>
    <datafield tag="980" ind1=" " ind2=" ">
        <subfield code="b">Research</subfield>
    </datafield>
  </record>"""


RECORD_TEMPLATE = """\
  <record>
    <controlfield tag="001">%(recid)s</controlfield>
    <datafield tag="110" ind1=" " ind2=" ">
        <subfield code="a">CMS collaboration</subfield>
        <subfield code="w">451</subfield>
    </datafield>
    <datafield tag="245" ind1=" " ind2=" ">
        <subfield code="a">L1 trigger menu information %(title)s</subfield>
    </datafield>
    <datafield tag="260" ind1=" " ind2=" ">
        <subfield code="b">CERN Open Data Portal</subfield>
        <subfield code="c">2016</subfield>
    </datafield>
    <datafield tag="264" ind1=" " ind2="0">
        <subfield code="c">2011</subfield>
    </datafield>
    <datafield tag="520" ind1=" " ind2=" ">
        <subfield code="a">%(info)s</subfield>
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
        <subfield code="a">CMS-Trigger-Information</subfield>
    </datafield>
    <datafield tag="980" ind1=" " ind2=" ">
        <subfield code="b">Research</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
        <subfield code="a">/tmp/opendata.cern.ch-fft-file-cache/cms-l1-trigger-information-Run2011A/%(filename)s</subfield>
    </datafield>
  </record>"""


def create_rich_abstract(recid, afile):
    """Create rich abstract out of info items."""
    out = '\n          <![CDATA['
    out += '\n           <p>L1 trigger menu information for CMS Run2011A collision data.</p>'
    out += '\n           <p>%s:' % os.path.basename(afile).split('.', 1)[0]
    for line in open('./inputs/' + afile, 'r').readlines():
        match = re.match(r'<a href=#(.*)>.*</a><BR>$', line)
        if match:
            label = match.groups()[0]
            link = '/record/%s/files/%s#%s' % (recid, afile, label)
            out += '\n           </br><a href="%s">%s</a>' % (link, label)
    out += '\n           </p>'
    out += '\n         ]]>'
    return out


def main():
    """Do the main job."""

    # begin stream
    print '<collection>'

    # generate table-of-contents record:
    recid = 3700
    print TOC_RECORD_TEMPLATE % \
        {'recid': recid,}

    # generate 7 other records:
    recid += 1
    title = None
    info = []
    for root, dirs, files in os.walk('./inputs'):
        files.sort()
        for afile in files:
            print RECORD_TEMPLATE % \
                {'recid': recid,
                 'title': os.path.basename(afile).split('.', 1)[0],
                 'info': create_rich_abstract(recid, afile),
                 'filename': afile}
            recid += 1

    # end stream
    print '</collection>'


if __name__ == '__main__':
    main()
