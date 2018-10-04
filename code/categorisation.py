#!/usr/bin/env python

"""Classify CMS MonteCarlo datasets into topical categories."""

import datetime
import os
import re
import sys

from urllib.parse import quote


def read_titles(filename):
    """Read dataset titles from filename."""
    titles = {}
    for line in open(filename).readlines():
        line = line.strip()
        if line:
            titles[line] = 1
    return list(titles.keys())


def categorise_titles(titles):
    """Categorise titles.

    Receives a list of datasets and outputs a dicttionary: {category: [datasets]}.

    CMS categories as in https://cms-results.web.cern.ch/cms-results/public-results/publications/"""
    categories = {
        'B physics and Quarkonia': [],
        'Top Physics': [],
        'Higgs Physics/SM': [],
        'Higgs Physics/BSM': [],
        'Forward and Small-x QCD Physics': [],
        'Standard Model Physics/DY': [],
        'Standard Model Physics/ElectroWeak': [],
        'Standard Model Physics/QCD': [],
        'Standard Model Physics/T': [],
        'Standard Model Physics/Others': [],
        'Heavy-Ion Physics': [],
        'Beyond 2 Generations': [],
        'Exotica/Colorons, Axigluons, Diquarks': [],
        'Exotica/Contact Interaction': [],
        'Exotica/Dark Matter': [],
        'Exotica/Excited Fermions': [],
        'Exotica/Extra Dimensions': [],
        'Exotica/Graviton': [],
        'Exotica/Heavy Fermions, Heavy Righ-Handed Neutrinos': [],
        'Exotica/Heavy Gauge Bosons': [],
        'Exotica/Leptoquark': [],
        'Exotica/Resonances': [],
        'Exotica/others': [],
        'Supersymmetry': [],
        'Physics Modelling': [],
        'Categorisation failure': [],
    }
    for title in titles:
        categories[guess_title_category(title)].append(title)
    return categories


def guess_title_category(title):
    """Guess category for the dataset.

    returns a string with the category of the dataset."""
    # title is /PrimaryDataset/ProcessedDataset/Tier1-Tier-2-
    title = '/' + title.split('/')[1] # get only the primary dataset name
    title_lower = title.lower()

    # be careful with the sequence of the of the `if`s bellow
    # first we check for exotic/susy datasets, then SM.

    if (re.search(r'/add', title_lower) or # Arkani-Hamed, Dimopoulos and Dvali model
        re.search(r'/branon', title_lower) or # extra-dimensions, brane models
        re.search(r'/stringball', title_lower) or
        re.search(r'/qbh', title_lower) or # Quantum Black Hole
        re.search(r'blackhole', title_lower)): # Quantum Black Hole also??
        return 'Exotica/Extra Dimensions'

    elif (re.search(r'darkmatter', title_lower) or
          re.search(r'/dmsimp', title_lower) or # darkmatter SIMP: Strongly interacting massive particle
          re.search(r'/dmz', title_lower) or    # darkmatter Z? FIXME
          re.search(r'DMJets', title)):         # darkmatter Jets? FIXME
        return 'Exotica/Dark Matter'

    elif (re.search(r'/lqto', title_lower) or  # leptoquark to
          re.search(r'/slq', title_lower) or   # single leptoquark
          re.search(r'/lqlqto', title_lower)): # leptoquark leptoquark to
        return 'Exotica/Leptoquark'

    elif (re.search(r'graviton', title_lower) or
          re.search(r'/rsgravto', title_lower) or # RS Graviton to
          re.search(r'radion', title_lower)):     # a.k.a. graviscalar
        return 'Exotica/Graviton'

    elif (re.search(r'/bstar', title_lower) or
          re.search(r'/estar', title_lower) or
          re.search(r'/qstar', title_lower) or
          re.search(r'/mustar', title_lower) or
          re.search(r'/taustar', title_lower)):
        return 'Exotica/Excited Fermions'

    elif (re.search(r'/cit', title_lower)):  # Contact Interactions to
        return 'Exotica/Contact Interaction'

    elif (re.search(r'wprime', title_lower) or # Heavy Gauge bosons: Wprime
          re.search(r'/heavygluon', title_lower) or # gluon is a boson
          re.search(r'zprime', title_lower)): # Heavy Gauge bosons: Zprime
        return 'Exotica/Heavy Gauge Bosons'

    elif (re.search(r'majorana', title_lower) or # Heavy Fermions, Heavy Righ-Handed Neutrinos
          re.search(r'/majoron', title_lower) or # predicted by seesaw mechanism
          re.search(r'/seesaw', title_lower)):   # Seesaw mechanism
        return 'Exotica/Heavy Fermions, Heavy Righ-Handed Neutrinos'

    elif ('bsm' in title_lower or
          re.search(r'/x53',        title_lower) or
          re.search(r'/atozh',      title_lower) or
          re.search(r'htohh',       title_lower) or
          re.search(r'/qdqd',       title_lower) or
          re.search(r'/qdto',       title_lower) or
          re.search(r'/quto',       title_lower) or
          re.search(r'/axito',      title_lower) or
          re.search(r'/thmtto',     title_lower) or
          re.search(r'/thptto',     title_lower) or
          re.search(r'/ttchichi',   title_lower) or
          re.search(r'anomwtb',     title_lower) or
          re.search(r'/vector1',    title_lower) or
          re.search(r'/vectormix',  title_lower) or
          re.search(r'/wrto',       title_lower) or
          re.search(r'/monolepton', title_lower) or
          re.search(r'/spin0plus',  title_lower) or
          re.search(r'/spin2ph',    title_lower)):
        return 'Exotica/others'

    elif ('susy' in title_lower or
          re.search(r'mssm', title_lower) or # Minimal Supersymmetric Standard Model
          re.search(r'/sms', title_lower) or # Simplified Model Spectra FIXME right category?
          re.search(r'/gmsb', title_lower) or # Gauge mediated supersymmetry breaking
          re.search(r'stop', title_lower) or # sTop
          re.search(r'sbottom', title_lower) or
          re.search(r'squark', title_lower) or
          re.search(r'slepton', title_lower) or
          re.search(r'selectron', title_lower) or
          re.search(r'smuon', title_lower) or
          re.search(r'neutralino', title_lower) or
          re.search(r'chargino', title_lower) or
          re.search(r'higgsino', title_lower) or
          re.search(r'gluino', title_lower) or
          re.search(r'gravitino', title_lower)):
        return 'Supersymmetry'

    elif ('Beyond 2 Generations' in title or
          re.search(r'bprime', title_lower) or # 4th gen of quarks
          re.search(r'tprime', title_lower)):  # 4th gen of quarks
        return 'Beyond 2 Generations'

    elif ('higgs0' in title_lower or
          'higgs2p' in title_lower or
          'bsmh' in title_lower or # BSM Higgs
          'chargedhiggs' in title_lower or
          re.search(r'/ATo', title) or
          re.search(r'/GluGluToA', title) or
          re.search(r'susybbh', title_lower) or
          re.search(r'primetoth', title_lower) or # TprimeToTH FIXME: SM Higgs from T' is here?
          re.search(r'primejettoth', title_lower) or # TprimeJetToTH FIXME: SM Higgs from T' is here?
          re.search(r'hminus', title_lower) or
          re.search(r'sms[-]?higgs', title_lower) or # sms higgs
          re.search(r'hplus', title_lower)):
        return 'Higgs Physics/BSM'

    elif ('higgs' in title_lower or # this also triggers higgsino FIXME
           'hto' in title_lower or
           '_hcontin' in title_lower or
           '_smhcontin' in title_lower or
           'vbf_hwwto' in title_lower or
           re.search(r'smh_', title_lower) or # SM triggers BSM: 'bsmh' is above, should be safe
           re.search(r'/glugluto', title_lower) or
           'h_m' in title_lower):
        if ('prime' in title_lower): # Tprime To Higgs
            return 'Higgs Physics/BSM'
        else:
            return 'Higgs Physics/SM'
            # FIXME gravitino going to SM Higgs ctegory.

    elif (re.search('GammaGammaTo(E|Mu|Tau)*_(Inel|Elastic|SingleDiss)', title)): # gamma gamma -> mu+ mu- etc reactions which involve elastically scattered protons
        return 'Forward and Small-x QCD Physics'

    elif ('matchingup' in title_lower or
          'matchingdown' in title_lower or
          'scaleup' in title_lower or
          'scaledown' in title_lower or
          re.search(r'tt_weights.*auet2', title_lower) or # FIXME ???
          re.search(r'pt[\w-]*gun', title_lower) or # neutrino, etc gun: ...Pt..gun
          '_mt' in title_lower or
          'signal_' in title_lower or # FIXME ???
          'signalplusbkgd' in title_lower or # FIXME ???
          '_mass' in title_lower):
        return 'Physics Modelling'

    elif re.search(r'/dy', title_lower):
        return 'Standard Model Physics/DY'

    elif re.search(r'/qcd', title_lower):
        return 'Standard Model Physics/QCD'

    elif (re.search(r'/ewk', title_lower) or # electroweak
          re.search(r'/diphoton', title_lower) or # G = Gamma
          re.search(r'/gjet', title_lower) or
          re.search(r'/g[1-9]jet', title_lower) or# Photon nJet ?? FIXME
          re.search(r'/ggjets', title_lower) or
          re.search(r'/gg4j', title_lower) or
          re.search(r'/gammagammato', title_lower) or
          re.search(r'/gg_m', title_lower) or
          re.search(r'/g_pt', title_lower) or
          re.search(r'/doublephoton', title_lower) or
          re.search(r'/zjetto', title_lower) or   # Zjet to
          re.search(r'/wjetto', title_lower) or   # Wjet to
          re.search(r'/w*[0-9]?jets', title_lower) or # any number of Wi, n Jets
          re.search(r'/z*[0-9]?jets', title_lower) or
          re.search(r'/zw[0-9]?jets', title_lower) or
          re.search(r'/wz[0-9]?jets', title_lower) or
          re.search(r'/wplusto', title_lower) or  # W+ to
          re.search(r'/wpto', title_lower) or     # W+ to
          re.search(r'/wminusto', title_lower) or # W- to
          re.search(r'/wmto', title_lower) or     # W- to
          re.search(r'/zzto', title_lower)):      # ZZ To
        return 'Standard Model Physics/ElectroWeak'


    elif (re.search(r'/ttbar', title_lower) or
          re.search(r'/tbarto', title_lower) or
          re.search(r'/tt_', title_lower)):
        return 'Standard Model Physics/T'

    elif (re.search(r'/muminus', title_lower) or
          re.search(r'/muplus', title_lower) or
          re.search(r'/doubleelectron', title_lower) or
          re.search(r'/singlepi', title_lower) or # is this right? FIXME
          'HT' in title or # from this line to end was SM Exclusive
          'Pt' in title or
          'enriched' in title_lower or
          'tt_mt1000' in title_lower or
          'tt_mt800' in title_lower or
          'tt_mtt-1000' in title_lower or
          'tt_mtt-700' in title_lower or
          re.search(r'[0-9]jet', title_lower)):
        return 'Standard Model Physics/Others'

    elif 'Heavy-Ion Physics' in title:
        return 'Heavy-Ion Physics'

    elif ('lambda' in title_lower or
          'Bu' in title or
          'Bd' in title or
          'jpsi' in title_lower or
          'upsilon' in title_lower or
          'bctobspi' in title_lower or
          'bstokstar' in title_lower or
          'etabto' in title_lower or # Eta_b To
          'xibstar0' in title_lower):
        return 'B physics and Quarkonia'

    elif ('Top Physics' in title_lower or
          re.search(r'/t[tgz]*jets(_|to)', title_lower) or # TTZJetsTo, TTGJetsTo, TZJetsTo
          re.search(r'/t*gamma_', title_lower) or # TGamma, TTGamma, TTTGamma, etc
          re.search(r'FCNC', title) or # FCNC: Flavour Change Neutral Current
          re.search(r'/ttoleptons_[t,s]', title_lower)):
        return 'Top Physics'

    return 'Categorisation failure'
    # FIXME: ISR - Initial State Radiation
    # FIXME: FSR - Final State Radiation


def print_results(categories):
    """Print category statistics."""
    for category, titles in categories.items():
        print('')
        print("### %s (%d)" % (category, len(titles)))
        print('')
        titles.sort()
        if titles:
            for title in titles:
                print('')
                print('- Dataset: [%s](%s)' %
                      (title,
                       'https://cmsweb.cern.ch/das/request?view=list&limit=5&instance=prod%2Fglobal&input=' + quote(title, safe='')))

def get_datasets_from_dir(inputdir):
    inputdatasets = []

    if re.search(r'.txt$', inputdir):
        for datasettitle in read_titles(inputdir):
            if datasettitle not in inputdatasets:
                inputdatasets.append(datasettitle)
        return inputdatasets

    for dirpath, dummy, inputfilenames in os.walk(inputdir):
        for inputfilename in inputfilenames:
            for datasettitle in read_titles(os.path.join(inputdir,
                                                         inputfilename)):
                if datasettitle not in inputdatasets:
                    inputdatasets.append(datasettitle)

    return inputdatasets


def main():
    """Do the main job."""

    # detect input directory with filenames containing dataset titles:
    try:
        inputdir = sys.argv[1]
    except IndexError:
        print('Usage: %s <input>' % sys.argv[0])
        print('<input> can be a text file with one entry per line or a',
              'directory with text files.')
        sys.exit(1)

    # print About information:
    print('# Categorisation for MC datasets')
    print('')
    print('## About')
    print('')
    print('This page is automatically generated from a categorisation script'
          ' that studies CMS MC 2012 datasets. If a dataset is mis-categorised,'
          ' the rules in the categorisation script should be adjusted and'
          ' the script rerun.')
    print('')
    print('See [#1229](https://github.com/cernopendata/opendata.cern.ch/issues/1229)'
          ' and [this page](https://demo.codimd.org/s/BkoBknkqQ#)'
          ' for more context.')
    print('')
    print('Generated on', datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print('')

    # read dataset titles
    inputdatasets = get_datasets_from_dir(inputdir)

    # categorise datasets:
    categorised = categorise_titles(inputdatasets)

    # print overview of results
    print('{} datasets in total:\n'.format(len(inputdatasets)))
    print('| # | Category |')
    print('|--:|:---------|')
    for category, titles in categorised.items():
        print("| {}\t| `{}` |".format(len(titles), category))
    print('')
    print('## Categories and Datasets')

    # print results
    print_results(categorised)


if __name__ == '__main__':
    main()
