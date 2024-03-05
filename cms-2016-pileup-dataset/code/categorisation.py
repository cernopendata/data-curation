#!/usr/bin/env python

"""Classify CMS MonteCarlo datasets into topical categories."""

import datetime
import os
import re
import sys

from urllib.parse import quote
from utils import read_titles, \
                  get_datasets_from_dir


def categorise_titles(titles):
    """Categorise titles.

    Receives a list of datasets and outputs a dictionary: {category: [datasets]}.

    CMS categories as in https://cms-results.web.cern.ch/cms-results/public-results/publications/"""
    categories = {
        'B physics and Quarkonia': [],
        'Higgs Physics/Standard Model': [],
        'Higgs Physics/Beyond Standard Model': [],
        'Standard Model Physics/Drell-Yan': [],
        'Standard Model Physics/ElectroWeak': [],
        'Standard Model Physics/Forward and Small-x QCD Physics': [],
        'Standard Model Physics/Minimum Bias': [],
        'Standard Model Physics/QCD': [],
        'Standard Model Physics/Top physics': [],
        'Standard Model Physics/Miscellaneous': [],
        'Heavy-Ion Physics': [],
        'Beyond 2 Generations': [],
        'Exotica/Colorons, Axigluons, Diquarks': [],
        'Exotica/Contact Interaction': [],
        'Exotica/Dark Matter': [],
        'Exotica/Excited Fermions': [],
        'Exotica/Extra Dimensions': [],
        'Exotica/Gravitons': [],
        'Exotica/Heavy Fermions, Heavy Righ-Handed Neutrinos': [],
        'Exotica/Heavy Gauge Bosons': [],
        'Exotica/Leptoquarks': [],
        'Exotica/Resonances': [],
        'Exotica/Miscellaneous': [],
        'Supersymmetry': [],
        'Physics Modelling': [],
        'Miscellaneous': [],
    }
    for title in titles:
        categories[guess_title_category(title)].append(title)
    return categories


def guess_title_category(title):
    """Guess category for the dataset.

    Only information to guess the category is the dataset name. Some "notes"
    about the dataset are available in the McM dictionary store:
    for f in *json; do cat $f | json_reformat | grep notes; done > notes

    returns a string with the category of the dataset."""
    # title is /PrimaryDataset/ProcessedDataset/Tier1-Tier-2-
    title = '/' + title.split('/')[1]  # get only the primary dataset name
    title_lower = title.lower()

    # be careful with the sequence of the of the `if`s bellow
    # first we check for exotic/susy datasets, then SM.

    # Be careful with regular expressions. They are nice and evil.
    # They make this code unreadable. And might match more things than you
    # expect. Been there, done that...

    if (re.search(r'/add', title_lower) or  # Arkani-Hamed, Dimopoulos and Dvali model
        re.search(r'/branon', title_lower) or  # extra-dimensions, brane models
        re.search(r'/stringball', title_lower) or
        re.search(r'/qbh', title_lower) or  # Quantum Black Hole
        re.search(r'/unpart', title_lower) or
        re.search(r'blackhole', title_lower)):  # Quantum Black Hole also??
        return 'Exotica/Extra Dimensions'

    elif (re.search(r'darkmatter', title_lower) or
          re.search(r'/nonthdm', title_lower) or  # non thermal dark matter
          re.search(r'/dmsimp', title_lower) or  # darkmatter SIMP: Strongly interacting massive particle
          re.search(r'/dmz', title_lower) or  # darkmatter Z?
          re.search(r'/dms', title_lower) or  # darkmatter scalar
          re.search(r'/dmv', title_lower) or  # darkmatter vector
          re.search(r'/(Axial|Pseudo|Vector|Scalar|SMM)[_]?Mono',title) or
          re.search(r'/DM_',title) or
          re.search(r'/Mono',title) or
          re.search(r'DMMono',title) or
          re.search(r'/VBFDM',title) or
          #re.search(r'/Monotop', title) or
          #re.search(r'/MonoPhoton',title) or
          re.search(r'/ALP',title) or
          re.search(r'/tphito2chi',title_lower) or
          re.search(r'/SingletTripletHDM',title) or
          re.search(r'SUEP',title) or
          re.search(r'DMJets', title)):       # darkmatter Jets?
        return 'Exotica/Dark Matter'

    elif (re.search(r'/lqto', title_lower) or   # leptoquark to
          re.search(r'/slq', title_lower) or    # single leptoquark
          re.search(r'/SingleLQ',title) or
          re.search(r'/SingleVectorLQ',title) or
          re.search(r'/PairVectorLQ',title) or
          re.search(r'/lqlqto', title_lower)):  # leptoquark leptoquark to
        return 'Exotica/Leptoquarks'

    elif (re.search(r'graviton', title_lower) or
          re.search(r'bulkgrav', title_lower) or  # bulk (?) gravitons
          re.search(r'/rsgravto', title_lower) or  # RS Graviton to
          re.search(r'/rsgluon', title_lower) or  # RS Gluon
          re.search(r'radion', title_lower)):  # a.k.a. graviscalar
        return 'Exotica/Gravitons'

    elif (re.search(r'/bstar', title_lower) or
          re.search(r'/tstar', title_lower) or
          re.search(r'/estar', title_lower) or
          re.search(r'/qstar', title_lower) or
          re.search(r'/mustar', title_lower) or
          re.search(r'/ExcitedLepton',title) or
          re.search(r'/taustar', title_lower)):
        return 'Exotica/Excited Fermions'

    elif (re.search(r'/cit', title_lower) or
          re.search(r'4fermionci',title_lower)):  # Contact Interactions to
        return 'Exotica/Contact Interaction'

    elif (re.search(r'/wprime', title_lower) or  # Heavy Gauge bosons: Wprime (but not from Tprime)
          re.search(r'/heavygluon', title_lower) or  # gluon is a boson
          re.search(r'/ZpToH',title) or
          re.search(r'/WpTo(BpT|TpB)',title) or
          re.search(r'/zzprime', title_lower) or
          re.search(r'/test_zprime',title_lower) or
          re.search(r'/vectorzprime',title_lower) or 
          re.search(r'/zptotptp',title_lower) or
          re.search(r'/btWprime',title) or
          re.search(r'/bff_zprimeto',title_lower) or
          re.search(r'/zprime', title_lower)):  # Heavy Gauge bosons: Zprime (but not from Hplus with low mass)
        return 'Exotica/Heavy Gauge Bosons'

    elif (re.search(r'majorana', title_lower) or  # Heavy Fermions, Heavy Righ-Handed Neutrinos
          re.search(r'/majoron', title_lower) or  # predicted by seesaw mechanism
          re.search(r'/HeavyNeutrino',title) or # heavy neutrino
          re.search(r'HeavyN',title) or
          re.search(r'/WRtoTauN',title) or
          re.search(r'/SSWWType',title) or # seesaw type-1 (1 or I...)
          re.search(r'/VLL',title) or # vector-like leptons
          re.search(r'/seesaw', title_lower)):    # Seesaw mechanism
        return 'Exotica/Heavy Fermions, Heavy Righ-Handed Neutrinos'
      
    elif (re.search(r'xtoyy', title_lower) or
          re.search(r'/xtoaa',title_lower) or
          re.search(r'/ytohh',title_lower) or
          re.search(r'/ZpToMuMu_M',title) or
          re.search(r'chargedresonance',title_lower) or
          re.search(r'res1tores2',title_lower)): 
        return 'Exotica/Resonances'

    elif (('bsm' in title_lower and not re.search('bsm[0-9]*h', title_lower)) or  # FIXME no idea what are those things, i just put them in the limbo
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
          re.search(r'/vectordijet1',  title_lower) or
          re.search(r'/wrto',       title_lower) or
          re.search(r'/zrto',       title_lower) or
          re.search(r'/monolepton', title_lower) or
          re.search(r'/spin0plus',  title_lower) or
          re.search(r'/spin2ph',    title_lower) or
          re.search(r'/ZD', title) or
          re.search(r'/LFV',title) or
          re.search(r'/extendedweakisospin',    title_lower) or
          re.search(r'/vectorlikelepton',    title_lower) or
          re.search(r'/emergingjets',  title_lower) or
          re.search(r'/sphaleron',  title_lower) or
          re.search(r'/(Z|W|tt)Phi_(H|PS|S)', title) or
          re.search(r'/ttPhi_withOffShellPhi',title) or
          re.search(r'/hscp',    title_lower)):
        return 'Exotica/Miscellaneous'

    elif ('susy' in title_lower or
          re.search(r'gstar', title_lower) or
          re.search(r'/rpvresonant', title_lower) or  # R-Parity Violation? FIXME
          re.search(r'mssm', title_lower) or  # Minimal Supersymmetric Standard Model
          re.search(r'/sms', title_lower) or  # Simplified Model Spectra FIXME right category?
          re.search(r'/gmsb', title_lower) or  # Gauge mediated supersymmetry breaking
          (re.search(r'stop', title_lower) and 'ToPsi' not in title and 'ToPi' not in title) or  # sTop --> grabbing BsToP* from Bphysics
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
          re.search(r'/x53', title_lower) or  # vector-like quarks
          re.search(r'/y43', title_lower) or  # vector-like quarks
          re.search(r'/pairvlq',title_lower) or
          re.search(r'x53x53',title_lower) or
          re.search(r'bprime', title_lower) or  # vector-like quarks
          re.search(r'tprime', title_lower)):   # vector-like quarks
        return 'Beyond 2 Generations'

    elif ('higgs0' in title_lower or
          'higgs2p' in title_lower or
          re.search('^/h0', title_lower) or
          re.search('bsm[0-9]*h', title_lower) or  # BSM Higgs
          'chargedhiggs' in title_lower or
          re.search(r'/ATo', title) or
          re.search(r'/atozh', title_lower) or
          re.search(r'/GluGluToA', title) or
          #re.search(r'susybbh', title_lower) or # superseded by 'susy' search above for supersymmetry (which seems better)
          re.search(r'HTohh', title) or  # H to hh
          #re.search(r'primetoth', title_lower) or  # TprimeToTH FIXME: SM Higgs from T' is here? No --> B2G, fixed.
          #re.search(r'primejettoth', title_lower) or  # TprimeJetToTH FIXME: SM Higgs from T' is here? No --> B2G, fixed.
          re.search(r'hminus', title_lower) or
          re.search(r'sms[-]?higgs', title_lower) or  # sms higgs
          re.search(r'spin0to', title_lower) or
          re.search(r'/spin0_',title_lower) or
          re.search(r'xxto', title_lower) or
          re.search(r'/Hpseudo',title) or
          re.search(r'/Hscalar',title) or
          re.search(r'/(T|BB)ATo',title) or
          re.search(r'/TS0To',title) or
          re.search(r'HToZA',title) or
          re.search(r'HToAA',title) or
          re.search(r'/HZaTo',title) or
          re.search(r'hto(2|four|zand)darkphoton',title_lower) or
          re.search(r'_LFV_',title) or
          re.search(r'_htoss',title_lower) or
          re.search(r'/h1h(1|2)',title_lower) or
          re.search(r'/twohdm',title_lower) or
          re.search(r'2HDM',title) or 
          re.search(r'/idm_',title_lower) or
          re.search(r'hto2longlived',title_lower) or
          re.search(r'0(M|P)Dec',title) or
          re.search(r'Dec0(M|P)',title) or
          re.search(r'hplus', title_lower)):
        return 'Higgs Physics/Beyond Standard Model'

    elif (('higgs' in title_lower and not 'nohiggs' in title_lower) or  # higgsino is above, ok to be here
          'hto' in title_lower or
          'bbh_m' in title_lower or
          re.search('/bbHWW',title) or
          re.search('/bbH_inclusive',title) or
          re.search('/ggH_HToUps',title) or
          re.search('/ggZH_',title) or
          re.search('/tqH_',title) or
          re.search('/ttH(_|To)',title) or
          '_hcontin' in title_lower or
          '_smhcontin' in title_lower or
          'vbf_hwwto' in title_lower or
          re.search(r'htohh', title_lower) or
          re.search(r'smh_', title_lower) or  # SM triggers BSM: 'bsmh' is above, should be safe
          re.search(r'/glugluto', title_lower)):
        #'h_m' in title_lower): testing removing this, it's catching too much dark matter and "Madgraph_madspin"...
        #if ('prime' in title_lower or  # Tprime To Higgs
            #'susy' in title_lower):
            #return 'Higgs Physics/Beyond Standard Model'  -- These are both fixed above now
        if('FCNC' in title):  # ST or TT with FCNC that specify a decay with higgs -- seems better with other FCNC in Top Physics
            return 'Standard Model Physics/Top physics'
        else:
            return 'Higgs Physics/Standard Model'

    elif ('_HInt_' in title   or
          'ttHJetTo' in title or
          'ttH_' in title or
          'Hincl' in title or
          'GluGluH' in title):   
        return 'Higgs Physics/Standard Model'

    elif (re.search('GammaGammaTo(E|Mu|Tau)*_(Inel|Elastic|SingleDiss)', title) or  # gamma gamma -> mu+ mu- etc reactions which involve elastically scattered protons
                                                                                    # SingleDiss, means Single Diffractive Dissociation
          re.search('/singlediffractive[zw]?', title_lower) or
          re.search('/cepdijets', title_lower) or  # Central Exclusive Production of dijets
          re.search('/dpedijets', title_lower) or  # ???
          re.search('/cs_', title_lower)):  # Color Singlet exchange (BFKL pomeron)
        return 'Standard Model Physics/Forward and Small-x QCD Physics'

    elif (re.search('/minbias', title_lower)):
        return 'Standard Model Physics/Minimum Bias'

    elif (re.search(r'/dy', title_lower) or
          re.search(r'/mumujet_',title_lower)):
        return 'Standard Model Physics/Drell-Yan'

    elif (re.search(r'/qcd', title_lower) or
          re.search(r'/dijet',title_lower)):
        return 'Standard Model Physics/QCD'

    elif (re.search(r'/ewk', title_lower) or  # electroweak
          re.search(r'/diphoton', title_lower) or  # G = Gamma
          re.search(r'/gjet', title_lower) or
          re.search(r'/g[1-9]jet', title_lower) or  # Photon nJet
          re.search(r'/g*jets', title_lower) or
          re.search(r'/gg4j', title_lower) or
          re.search(r'/gammagammato', title_lower) or
          re.search(r'/gg_m', title_lower) or
          re.search(r'/g_pt', title_lower) or
          re.search(r'/doublephoton', title_lower) or
          re.search(r'/lnugg', title_lower) or
          re.search(r'/w*l*nub*', title_lower) or
          re.search(r'/w*[b]?j*to', title_lower) or
          re.search(r'/wwjj',title_lower) or
          re.search(r'/ll[a]?[g]?jj', title_lower) or
          re.search(r'/llwa_', title_lower) or
          re.search(r'/[lminusplus]*nu.*vbf', title_lower) or  # L+- Nu bla VBF
          re.search(r'/[wz]*vbf', title_lower) or
          re.search(r'/zb*_[1-9]*f', title_lower) or
          re.search(r'/[WmpJ]*To[QLNuBar]*_', title) or  # Wp Wm J To Q L NuBar
          re.search(r'/[wzg]*to[nug]*', title_lower) or  # W/Z/G To Nu/G
          re.search(r'/[WZGam]*_', title) or  # W/Z/G_*
          re.search(r'/zjetto', title_lower) or  # Zjet to
          re.search(r'/wjetto', title_lower) or  # Wjet to
          re.search(r'/[wzg]*[0-9]?jet', title_lower) or  # any number of W/Z/gamma, n Jets
          #re.search(r'/wplusto', title_lower) or   # W+ to
          re.search(r'/w(p|m)to', title_lower) or      # W+ to  (Wprime -> TprimeB, BprimeT caught above)
          re.search(r'/w(minus|plus)to', title_lower) or  # W- to
          re.search(r'/w(minus|plus)lnu', title_lower) or  # W- to
          re.search(r'/wplusminus', title_lower) or # W+/W- to
          #re.search(r'/wmto', title_lower) or      # W- to
          re.search(r'/w(minus|plus)j', title_lower) or
          re.search(r'/z*to', title_lower) or      # ZZ To
          re.search(r'/eeg', title_lower) or
          re.search(r'/photonindbkg', title_lower) or
          re.search(r'/wgjjto', title_lower) or
          re.search(r'/wzjto', title_lower) or
          re.search(r'/w(w|z)(a|2j)',title_lower) or
          re.search(r'/zz[2]?j', title_lower) or
          re.search(r'/wlljjto', title_lower) or
          re.search(r'/wz(jj|2j)', title_lower) or
          re.search(r'/glugluwwto', title_lower) or
          re.search(r'/mumug', title_lower) or
          re.search(r'/vvto', title_lower) or
          re.search(r'/wpwp', title_lower) or
          re.search(r'/wmwm', title_lower) or
          re.search(r'/wbjets', title_lower) or
          re.search(r'/zllg', title_lower) or
          re.search(r'/wll',title_lower) or
          re.search(r'/znunug', title_lower) or
          re.search(r'/zbjet',title_lower) or
          re.search(r'/wc[c]?jet',title_lower) or
          re.search(r'/Z[G]?J[J]?To',title) or
          re.search(r'/(W|Z)Gamma(To|2)',title) or
          re.search(r'/VBS', title) or
          re.search(r'/Wplus2JWminus2J', title) or
          re.search(r'/z2(b|nu|j)[j]?w',title_lower) or
          re.search(r'/SSWW',title) or # same-sign? Separate from Type1HeavyN above...
          re.search(r'/[wz]to[emunu]*', title_lower)):  #  W/Z to E,Mu,Nu
        return 'Standard Model Physics/ElectroWeak'

    elif (re.search(r'/t+bar', title_lower) or
          re.search(r'/t[tgz]*jets(_|to)', title_lower) or  # TTZJetsTo, TTGJetsTo, TZJetsTo
          re.search(r'/t*gamma_', title_lower) or  # TGamma, TTGamma, TTTGamma, etc with a photon in the final state
          re.search(r'FCNC', title) or  # FCNC: Flavour Change Neutral Current
          re.search(r'/tt_weights', title) or
          re.search(r'/ttoleptons_[t,s]', title_lower) or
          re.search(r'/tbarto', title_lower) or
          re.search(r'/t4qz', title_lower) or
          re.search(r'/tbz', title_lower) or
          re.search(r'/t+g+', title_lower) or  # any number of T Gamma
          re.search(r'/t+to[2lnub]*_', title_lower) or
          'tt_mt1000' in title_lower or
          'tt_mt800' in title_lower or
          'tt_mtt-1000' in title_lower or
          'tt_mtt-700' in title_lower or
          re.search(r'/[tbar]*_.+_[stuw]+-channel', title_lower) or  # T_bla_s/t/u/w-channel
          re.search(r'/ST_', title) or
          re.search(r'/TTZTo', title) or
          re.search(r'/TT[WZH][WZH]', title) or
          re.search(r'/T[TT]?[TWJ]', title) or
          re.search(r'/TT4b', title) or
          re.search(r'/tZq', title) or
          re.search(r'/TTTo', title) or
          re.search(r'/ttwjets', title_lower) or
          re.search(r'/TWZ', title) or
          re.search(r'/ttbb', title_lower) or
          re.search(r'/t+_', title_lower)):
        return 'Standard Model Physics/Top physics'

    elif ('Heavy-Ion Physics' in title or
          re.search('reggegribov_', title_lower)):
        return 'Heavy-Ion Physics'

    elif ('lambda' in title_lower or
          'Bu' in title or  # Bu stands for B+
          'Bd' in title or
          'Bc' in title or
          'Xib' in title or 
          'jpsi' in title_lower or
          'upsilon' in title_lower or
          re.search('/Y(1|2|3|n)STo',title) or
          'bctobspi' in title_lower or
          'bstokstar' in title_lower or
          re.search(r'/bsto', title_lower) or
          re.search(r'/bsstarto', title_lower) or
          re.search(r'/b0to', title_lower) or
          re.search(r'/b0sto', title_lower) or
          re.search(r'/chib0', title_lower) or
          'etabto' in title_lower or  # Eta_b To
          'InclusivebtoMu' in title or
          'InclusivectoMu' in title or
          'InclusiveMu' in title or
          'bbbarToMuMu' in title or
          'b_bbar' in title or
          'DsToTau' in title or
          'DStar' in title or
          re.search('/DPS_',title) or
          re.search('/SPS_',title)):
        return 'B physics and Quarkonia'

    # moving lower -- single and double are very generic and might be more specified above
    elif (re.search(r'gun', title_lower) or # particle gun
          re.search(r'/single', title_lower) or
          re.search(r'/double', title_lower) or
          re.search(r'/muminus', title_lower) or
          re.search(r'/muplus', title_lower) or
          re.search(r'/doubleelectron', title_lower) or  # Is this an electron gun?
          re.search(r'/singlepi', title_lower)): 
        return 'Physics Modelling'

    return 'Miscellaneous'
    # FIXME: ISR - Initial State Radiation
    # FIXME: FSR - Final State Radiation


def main():
    """Do the main job."""
    from printer import print_results

    # detect input directory with filenames containing dataset titles:
    try:
        inputdir = sys.argv[1]
    except IndexError:
        print('Usage: %s <input>' % sys.argv[0])
        print('<input> can be a text file with one entry per line or a',
              'directory with text files.')
        sys.exit(1)

    # read dataset titles
    inputdatasets = get_datasets_from_dir(inputdir)

    # categorise datasets
    categorised = categorise_titles(inputdatasets)

    # print results
    print_results(categorised)


if __name__ == '__main__':
    main()
