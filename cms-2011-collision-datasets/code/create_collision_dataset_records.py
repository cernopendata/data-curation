#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
To be run after EOS file specs are gathered via:
source ./eos-get-listings.sh
"""

import glob
import re
import sys

from create_das_json_store import get_das_json, get_from_deep_json
from create_reco_config_file_records import get_title
from create_reco_config_file_records import get_process

LINK_INFO = {}
exec(open('./outputs/reco_config_files_link_info.py', 'r').read())

RECORD_TEMPLATE = """
  <record>
    <controlfield tag="001">%(recid)s</controlfield>
    <datafield tag="024" ind1="7" ind2=" ">
      <subfield code="2">DOI</subfield>
      <subfield code="a">%(doi)s</subfield>
    </datafield>
    <datafield tag="110" ind1=" " ind2=" ">
      <subfield code="a">CMS collaboration</subfield>
    </datafield>
    <datafield tag="245" ind1=" " ind2=" ">
      <subfield code="a">%(title)s</subfield>
    </datafield>
    <datafield tag="246" ind1=" " ind2=" ">
      <subfield code="a">%(dataset)s primary dataset in AOD format from RunA of 2011 (%(title)s)</subfield>
    </datafield>
    <datafield tag="538" ind1=" " ind2=" ">
      <subfield code="a">Recommended release for analysis: CMSSW_5_3_32</subfield>
      <subfield code="b">Global tag: FT_53_LV5_AN1</subfield>
    </datafield>
    <datafield tag="256" ind1=" " ind2=" ">
      <subfield code="a">Dataset</subfield>
      <subfield code="e">FIXME</subfield>
      <subfield code="t">events</subfield>
    </datafield>
    <datafield tag="256" ind1=" " ind2=" ">
      <subfield code="f">%(nb_files)s</subfield>
      <subfield code="t">files</subfield>
    </datafield>
    <datafield tag="256" ind1=" " ind2=" ">
      <subfield code="b">%(nb_bytes)s</subfield>
      <subfield code="t">bytes in total</subfield>
    </datafield>
    <datafield tag="260" ind1=" " ind2=" ">
      <subfield code="b">CERN Open Data Portal</subfield>
      <subfield code="c">2016</subfield>
    </datafield>
    <datafield tag="264" ind1=" " ind2="0">
      <subfield code="c">2011</subfield>
    </datafield>
    <datafield tag="520" ind1=" " ind2=" ">
      <subfield code="a">%(dataset)s primary dataset in AOD format from RunA of 2011.%(run_number_information)s</subfield>
    </datafield>
    <datafield tag="540" ind1=" " ind2=" ">
      <subfield code="a">CC0</subfield>
    </datafield>
    <datafield tag="556" ind1=" " ind2=" ">
      <subfield code="a">This dataset contains all runs from 2011 RunA. The list of validated runs, which must be applied to all analyses, can be found in</subfield>
      <subfield code="w">1001</subfield>
    </datafield>
    <datafield tag="567" ind1=" " ind2=" ">
      <subfield code="a"><![CDATA[ %(selection_information)s ]]></subfield>
    </datafield>
    <datafield tag="583" ind1=" " ind2=" ">
      <subfield code="a">During data taking all the runs recorded by CMS are certified as good for physics analysis if all subdetectors, trigger, lumi and physics objects (tracking, electron, muon, gamma, jet and MET) show the expected performance. Certification is based first on the offline shifters evaluation and later on the feedback provided by detector and Physics Object Group experts. Based on the above information, which is stored in a specific database called Run Registry, the Data Quality Monitoring group verifies the consistency of the certification and prepares a json file of certified runs to be used for physics analysis. For each reprocessing of the raw data, the above mentioned steps are repeated. For more information see:</subfield>
      <subfield code="u">http://iopscience.iop.org/1742-6596/219/7/072020/pdf/1742-6596_219_7_072020.pdf</subfield>
      <subfield code="y">CMS data quality monitoring: Systems and experiences</subfield>
    </datafield>
    <datafield tag="583" ind1=" " ind2=" ">
      <subfield code="u">http://cds.cern.ch/record/1631039/files/CR2013_418.pdf</subfield>
      <subfield code="y">The CMS Data Quality Monitoring software experience and future improvements</subfield>
    </datafield>
    <datafield tag="583" ind1=" " ind2=" ">
      <subfield code="u">http://iopscience.iop.org/1742-6596/513/3/032024/pdf/1742-6596_513_3_032024.pdf</subfield>
      <subfield code="y">The CMS data quality monitoring software: experience and future prospects</subfield>
    </datafield>
    <datafield tag="581" ind1=" " ind2=" ">
      <subfield code="a">You can access these data through the CMS Virtual Machine. See the instructions for setting up the Virtual Machine and getting started in</subfield>
      <subfield code="u">http://opendata.cern.ch/VM/CMS#2011</subfield>
      <subfield code="y">How to install the CMS Virtual Machine</subfield>
    </datafield>
    <datafield tag="581" ind1=" " ind2=" ">
      <subfield code="u">http://opendata.cern.ch/getting-started/CMS#2011</subfield>
      <subfield code="y">Getting started with CMS open data</subfield>
    </datafield>
    <datafield tag="693" ind1=" " ind2=" ">
      <subfield code="a">CERN-LHC</subfield>
      <subfield code="e">CMS</subfield>
    </datafield>
    <datafield tag="772" ind1=" " ind2=" ">
      <subfield code="a">%(raw)s</subfield>
    </datafield>
%(8567s)s
    <datafield tag="942" ind1=" " ind2=" ">
      <subfield code="e">Collision energy: 7TeV</subfield>
    </datafield>
    <datafield tag="960" ind1=" " ind2=" ">
      <subfield code="c">2011</subfield>
    </datafield>
    <datafield tag="980" ind1=" " ind2=" ">
      <subfield code="a">CMS-Primary-Datasets</subfield>
    </datafield>
    <datafield tag="980" ind1=" " ind2=" ">
      <subfield code="b">Research</subfield>
    </datafield>
%(FFTs)s
  </record>
"""

TEMPLATE_FFT = """\
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">/tmp/opendata.cern.ch-fft-file-cache/cms-eos-file-indexes/%(filename)s</subfield>
      <subfield code="z">%(dataset)s AOD dataset file index (%(nb_dataset)s of %(nb_total)s) for access to data via CMS virtual machine</subfield>
    </datafield>
"""

def create_8567s(dataset):
    out = ''
    filenames = glob.glob('./inputs/eos-file-indexes/*_%s_*xml' % dataset)
    filenames.sort()
    for filename in filenames:
        out += open(filename, 'r').read()
    return out


def create_FFTs(dataset):
    out = ''
    filenames = glob.glob('./inputs/eos-file-indexes/*_%s_*txt' % dataset)
    filenames.sort()
    nb_total = len(filenames)
    for nb_dataset, filename in enumerate(filenames):
        out += TEMPLATE_FFT % {
            'dataset': dataset,
            'filename': filename.replace('inputs/eos-file-indexes/', ''),
            'nb_dataset': str(nb_dataset + 1),
            'nb_total': str(nb_total)
        }
    return out


def get_version(dataset):
    if dataset in ['ForwardTriggers',]:
        return '2'
    else:
        return '1'


def get_nb_files(dataset):
    out = 0
    filenames = glob.glob('./inputs/eos-file-indexes/*_%s_*xml' % dataset)
    filenames.sort()
    for filename in filenames:
        for line in open(filename, 'r').readlines():
            match = re.search(r'<subfield code="s">([0-9]+)</subfield>', line)
            if match:
               out += 1
    return out


def get_nb_bytes(dataset):
    out = 0
    filenames = glob.glob('./inputs/eos-file-indexes/*_%s_*xml' % dataset)
    filenames.sort()
    for filename in filenames:
        for line in open(filename, 'r').readlines():
            match = re.search(r'<subfield code="s">([0-9]+)</subfield>', line)
            if match:
               out += int(match.groups()[0])
    return out


def get_doi(recid):
    dois = {15: '10.7483/OPENDATA.CMS.N372.QF6S',
            16: '10.7483/OPENDATA.CMS.MQXP.QNMB',
            17: '10.7483/OPENDATA.CMS.RZ34.QR6N',
            18: '10.7483/OPENDATA.CMS.Q4HH.6V7K',
            19: '10.7483/OPENDATA.CMS.UJBP.7D8Z',
            20: '10.7483/OPENDATA.CMS.28VG.KY9R',
            21: '10.7483/OPENDATA.CMS.UP77.P6PQ',
            22: '10.7483/OPENDATA.CMS.GTVX.CSFF',
            23: '10.7483/OPENDATA.CMS.E82B.SU5C',
            24: '10.7483/OPENDATA.CMS.QSPG.CCQ4',
            25: '10.7483/OPENDATA.CMS.X7AM.49VT',
            26: '10.7483/OPENDATA.CMS.B57J.DPSR',
            27: '10.7483/OPENDATA.CMS.FZ5U.TTXP',
            28: '10.7483/OPENDATA.CMS.8N95.GCTN',
            29: '10.7483/OPENDATA.CMS.K3YX.WNFA',
            30: '10.7483/OPENDATA.CMS.YQDZ.PDQA',
            31: '10.7483/OPENDATA.CMS.P87Z.TXTV',
            32: '10.7483/OPENDATA.CMS.UY8U.9XJ3',
            33: '10.7483/OPENDATA.CMS.9Y97.SG5C',
            34: '10.7483/OPENDATA.CMS.9SYW.PU3F'}
    return dois[recid]


FWYZARD = {}


def populate_fwyzard():
    """Populate FWYZARD dictionary (dataset -> trigger list)."""
    for line in open('./inputs/fwyzard-hlt-2011-dataset.txt', 'r').readlines():
        dataset, trigger = line.split()
        if dataset in FWYZARD.keys():
            FWYZARD[dataset].append(trigger)
        else:
            FWYZARD[dataset] = [trigger, ]


def get_trigger_paths_for_dataset(dataset):
    """Return list of trigger paths for given dataset."""
    return FWYZARD.get(dataset, [])


def create_selection_information(dataset):
    """Create box with selection information."""
    out = ''
    # generation steps
    out += '\n'
    out += '\n        <p><strong>Data taking / HLT</strong>'
    out += '\n        <br/>The collision data were assigned to different RAW datasets using the following <a href="/record/1700">HLT configuration</a>.</p>'
    process = 'FIXME'
    generator_text = 'FIXME'
    fulldataset = '/%s/Run2011A-12Oct2013-v%s/AOD' % (dataset, get_version(dataset))
    config_id = get_from_deep_json(get_das_json(fulldataset), 'ConfigCacheID')
    if config_id:
        afile = config_id + '.configFile'
        process = get_process(afile)
        generator_text = get_title(afile)
    out += '\n        <p><strong>Data processing / RECO</strong>'
    out += '\n        <br/>This primary AOD dataset was processed from the RAW dataset by the following step:'
    out += '\n        <br/>Step: %s' % process
    out += '\n        <br/>Release: %s' % get_from_deep_json(get_das_json(fulldataset), 'CMSSWVersion')
    out += '\n        <br/>Global tag: %s' % get_from_deep_json(get_das_json(fulldataset), 'GlobalTag')
    if config_id:
        out += '\n        <br/><a href="/record/%s">%s</a>' % (LINK_INFO[config_id], generator_text)
    out += '\n        </p>'
    # HLT trigger paths:
    out += '\n     <p><strong>HLT trigger paths</strong>'
    out += '\n     <br/>The possible HLT trigger paths in this dataset are:'
    trigger_paths = get_trigger_paths_for_dataset(dataset)
    for trigger_path in trigger_paths:
        out += '\n      <br/><a href="/search?p=%s>%s</a>' % (trigger_path,
                                                      trigger_path)
    out += '</p>'
    return out


def get_min_run_number(fulldataset):
    """Return minimum run number whitelisted for the given dataset."""
    runwhitelist = get_from_deep_json(get_das_json(fulldataset), 'RunWhitelist')
    if runwhitelist:
        return min(runwhitelist)
    else:
        return None


def get_max_run_number(fulldataset):
    """Return maximum run number whitelisted for the given dataset."""
    runwhitelist = get_from_deep_json(get_das_json(fulldataset), 'RunWhitelist')
    if runwhitelist:
        return max(runwhitelist)
    else:
        return None


def get_run_number_information(fulldataset):
    "Return textual information suitable for run number information."
    min_run_number = get_min_run_number(fulldataset)
    max_run_number = get_max_run_number(fulldataset)
    if min_run_number and max_run_number:
        return ' Run period from run number %s to %s.' % \
            (min_run_number, max_run_number)
    else:
        return ''


def main():
    """Do the main job."""

    populate_fwyzard()

    print "<collection>"
    recid = 15
    for dataset in ['BTag', 'DoubleElectron', 'DoubleMu', 'ElectronHad',
                    'ForwardTriggers', 'HT', 'Jet', 'MET', 'METBTag', 'MinimumBias', 'MuEG',
                    'MuHad', 'MuOnia', 'MultiJet', 'Photon', 'PhotonHad', 'SingleElectron',
                    'SingleMu', 'Tau', 'TauPlusX']:
        fulldataset = '/%s/Run2011A-12Oct2013-v%s/AOD' % (dataset, get_version(dataset))
        print RECORD_TEMPLATE % \
            {
                'recid': str(recid),
                'doi': get_doi(recid),
                'dataset': dataset,
                'nb_files': get_nb_files(dataset),
                'nb_bytes': get_nb_bytes(dataset),
                'title': fulldataset,
                'raw': '/%s/Run2011A-v%s/RAW' % (dataset, get_version(dataset)),
                '8567s': create_8567s(dataset),
                'FFTs': create_FFTs(dataset),
                'selection_information': create_selection_information(dataset),
                'run_number_information': get_run_number_information(fulldataset)
            }
        recid += 1
    print "</collection>"


if __name__ == '__main__':
    main()
