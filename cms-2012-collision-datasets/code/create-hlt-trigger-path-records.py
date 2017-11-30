#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create CMS Trigger Information records.
"""

LINK_INFO = {}
# read LINK_INFO dictionary created by a friendly program ahead of this one:
exec(open('./outputs/hlt_config_files_link_info.py', 'r').read())

RECID_START = 6200

RECORD_TEMPLATE = """\
  <record>
    <controlfield tag="001">%(recid)s</controlfield>
    <datafield tag="110" ind1=" " ind2=" ">
        <subfield code="a">CMS collaboration</subfield>
    </datafield>
    <datafield tag="245" ind1=" " ind2=" ">
        <subfield code="a">High-Level Trigger path information %(title)s</subfield>
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
   </record>"""


def expand_links(atext):
    "Take text and expand links based on LINK_INFO."
    btext = atext
    for key in LINK_INFO.keys():
        if key in btext:
            btext = btext.replace(key, '<a href="/record/%d">%s</a>' % (LINK_INFO[key], key))
    return btext


def create_rich_abstract(title, info):
    """Create rich abstract out of info items."""
    out = '<![CDATA[ '
    out += '<p>High-Level Trigger path information %s.</p>' % title
    if info:
        out += '<blockquote>'
        for item in info:
            out += '<p>' + expand_links(item) + '</p>'
        out += '</blockquote>'
    out += '<p>See also the full list of triggers for CMS 2011 open data:'
    out += '<a href="/record/1700">Trigger information for 2011 CMS open data</a></p>'
    return out + ']]>'


def main():
    """Do the main job."""

    recid = RECID_START
    title = None
    info = []
    for line in open('./inputs/hlt-trigger-path.txt', 'r').readlines():
        if line.startswith('Path'):
            if title:
                print(RECORD_TEMPLATE %
                      {'recid': recid,
                       'title': title,
                       'info': create_rich_abstract(title, info)})
                recid += 1
                info = []
            title = line.split(' ', 1)[1].strip()
            if title.endswith(':'):
                title = title[:-1]
        elif line.startswith(' - '):
            info.append(line[2:].strip())
        else:
            pass


if __name__ == '__main__':
    main()
