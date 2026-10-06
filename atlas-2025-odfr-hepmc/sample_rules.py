# This file just includes the rules for sorting records

'''
Categories currently allowed in the Open Data Portal:
https://github.com/cernopendata/cernopendata-portal/blob/eaae90860185a947622d331a6bfcda33b383ea42/cernopendata/modules/fixtures/data/docs/simulated-dataset-categories/simulated-dataset-categories.md?plain=1#L8

- B Physics and Quarkonia
- Higgs Physics
    - Standard Model
    - Beyond Standard Model
- Standard Model
    - Drell-Yan
    - ElectroWeak
    - Forward and Small-x QCD Physics
    - Minimum Bias
    - QCD
    - Top physics
    - Miscalleneous
- Heavy-Ion Physics
- Beyond 2 Generations
- Exotica
    - Colorons, Axigluons, Diquarks
    - Contact Interaction
    - Dark Matter
    - Excited Fermions
    - Extra Dimensions
    - Gravitons
    - Heavy Fermions, Heavy Right-Handed Neutrinos
    - Heavy Gauge Bosons
    - Leptoquarks
    - Resonances
    - Miscalleneous
- Supersymmetry
- Physics Modelling
'''

# Set up the record map. This map contains several items:
#  Names. Not necessarily unique; non-unique collections will be added into the same Open Data Record.
#  KWL. A keyword list to select samples. All keywords in the list are required (AND). For OR, use a second record.
#  Not KWL. A keyword list to reject samples. Any keyword in the list will reject a sample.
#  Open Data KWL. A list of keywords to be used in the CERN Open Data Portal (see comment above)
record_map = [
               # Exotic / BSM signal records
               # RS gravitons
               {'name':'BSM RS Graviton','kwl':['graviton'],'not_kwl':[], 'ODkwl':['Exotica','Gravitons']},

               # BSM Gauge bosons
               {'name':'BSM Z prime','kwl':['zprime'],'not_kwl':[], 'ODkwl':['Exotica','Heavy Gauge Bosons']},
               {'name':'BSM W prime','kwl':['wprime'],'not_kwl':[], 'ODkwl':['Exotica','Heavy Gauge Bosons']},

               # Dark matter and axion models
               {'name':'BSM Dark Matter Simplified Model','kwl':['wimp'],'not_kwl':[], 'ODkwl':['Exotica','Dark Matter']},
               {'name':'BSM Dark Matter S>bb','kwl':['monoSbbRelic'],'not_kwl':[], 'ODkwl':['Exotica','Dark Matter']},
               {'name':'BSM Axion-like Particles','kwl':['wz','exotic'],'not_kwl':[], 'ODkwl':['Exotica','Dark Matter']},
               {'name':'BSM Axion-like Particles','kwl':['ALP'],'not_kwl':[], 'ODkwl':['Exotica','Dark Matter']},

               # Heavy neutral leptons, 4th generation, etc all go together
               {'name':'BSM Heavy Neutral Lepton','kwl':['exotic','neutrino'],'not_kwl':[], 'ODkwl':['Exotica','Heavy Fermions, Heavy Right-Handed Neutrinos']},
               {'name':'BSM Other Seesaw','kwl':['seesaw'],'not_kwl':['chargedhiggs'], 'ODkwl':['Exotica','Heavy Fermions, Heavy Right-Handed Neutrinos']},

               # Leptoquark models
               {'name':'BSM Leptoquark','kwl':['leptoquark'],'not_kwl':[], 'ODkwl':['Exotica','Leptoquarks']},

               # Vector-like leptons
               {'name':'BSM Vector-like leptons','kwl':['exotic','multilepton'],'not_kwl':['chargedhiggs'], 'ODkwl':['Exotica']},

               # Hidden valley / semi-visible jet models
               {'name':'BSM 4-jet Hidden Valley','kwl':['hiddenvalley','4jet'],'not_kwl':[], 'ODkwl':['Exotica','Miscalleneous']},
               {'name':'BSM 2-jet Hidden Valley','kwl':['hiddenvalley','2jet'],'not_kwl':[], 'ODkwl':['Exotica','Miscalleneous']},
               {'name':'BSM Semi-visible jets','kwl':['bsm','SVJ'],'not_kwl':[], 'ODkwl':['Exotica']},

               # Supersymmetry - currently only a small set from the exotics group
               {'name':'BSM Other SUSY Signals','kwl':['susy'],'not_kwl':[], 'ODkwl':['Supersymmetry']},

               # BSM Higgs models. Mix of providing additional Higgses and modifying Higgs decays
               {'name':'BSM Higgs Dark Photon','kwl':['darkphoton'],'not_kwl':[], 'ODkwl':['Higgs Physics','Beyond Standard Model']},
               {'name':'BSM Higgs LLP','kwl':['bsmhiggs','longlived'],'not_kwl':['darkphoton'], 'ODkwl':['Higgs Physics','Beyond Standard Model']},
               {'name':'BSM Charged Higgs Seesaw','kwl':['chargedhiggs'],'not_kwl':[], 'ODkwl':['Higgs Physics','Beyond Standard Model']},

               # Catch-alls to have other records. These should stay light if possible, and not be lists of a bajillion samples.
               {'name':'Other BSM Higgs samples','kwl':['bsmhiggs'],'not_kwl':['samesign','darkphoton','longlived'], 'ODkwl':['Higgs Physics','Beyond Standard Model']},
               {'name':'Other BSM Higgs samples','kwl':['bsm','higgs','gluonfusionhiggs'],'not_kwl':['samesign','darkphoton','longlived'], 'ODkwl':['Higgs Physics','Beyond Standard Model']},
               {'name':'Other BSM samples','kwl':['bsm','tau','muon'],'not_kwl':[], 'ODkwl':['Exotica','Miscalleneous']},
               {'name':'Other BSM samples','kwl':['exotic','egamma'],'not_kwl':[], 'ODkwl':['Exotica','Miscalleneous']},

               # These are simple SM extensions where we generate SM processes with BSM couplings / decays
               {'name':'Top Flavor-changing Neutral Currents','kwl':['fcnc'],'not_kwl':[], 'ODkwl':['Exotica','Miscalleneous']},
               {'name':'Single Top CKM','kwl':['ckm'],'not_kwl':[], 'ODkwl':['Exotica','Miscalleneous']},

               # Higgs samples, SM production, gathered by type
               {'name':'SM W+Higgs','kwl':['whiggs'],'not_kwl':[], 'ODkwl':['Higgs Physics','Standard Model']},
               {'name':'SM Z+Higgs','kwl':['zhiggs'],'not_kwl':[], 'ODkwl':['Higgs Physics','Standard Model']},
               {'name':'SM ttbar+Higgs','kwl':['higgs','top'],'not_kwl':[], 'ODkwl':['Higgs Physics','Standard Model']},
               {'name':'SM ttbar+Higgs','kwl':['higgs','ttbar'],'not_kwl':[], 'ODkwl':['Higgs Physics','Standard Model']},
               {'name':'SM single top+Higgs','kwl':['higgs','thiggs'],'not_kwl':[], 'ODkwl':['Higgs Physics','Standard Model']},
               {'name':'SM single top+Higgs','kwl':['Higgs','thiggs'],'not_kwl':[], 'ODkwl':['Higgs Physics','Standard Model']},
               {'name':'SM single top+Higgs','kwl':['Higgs','tHiggs'],'not_kwl':[], 'ODkwl':['Higgs Physics','Standard Model']},
               {'name':'SM Other Higgs','kwl':['higgs'],'not_kwl':['whiggs','zhiggs','thiggs','bsm','top','ttbar','bsmhiggs'], 'ODkwl':['Higgs Physics','Standard Model']},
               {'name':'SM Other Higgs','kwl':['zz','higgs','resonance'],'not_kwl':['whiggs','zhiggs','thiggs','bsm','top','ttbar','bsmhiggs'], 'ODkwl':['Higgs Physics','Standard Model']},
               {'name':'SM Other Higgs','kwl':['smhiggs'],'not_kwl':['higgs','whiggs','zhiggs','thiggs','bsm','top','ttbar','bsmhiggs'], 'ODkwl':['Higgs Physics','Standard Model']},

               # SM Diboson production
               {'name':'SM WW Diboson','kwl':['ww'],'not_kwl':['higgs','smhiggs'], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'SM WZ Diboson','kwl':['wz'],'not_kwl':['bsm'], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'SM ZZ Diboson','kwl':['zz'],'not_kwl':['smhiggs','bsm'], 'ODkwl':['Standard Model','ElectroWeak']},

               # SM Diboson VV production (for generators that don't distinguish based on intermediate states, but only final states)
               {'name':'SM VV (Diboson) Nominal','kwl':['diboson','Baseline'],'not_kwl':['photon','vbs','ww','wz','zz'], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'SM VV (Diboson) Systematic Variation','kwl':['diboson','Systematic'],'not_kwl':['photon','ww','wz','zz','vbs'], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'SM VV (Diboson) Other','kwl':['diboson'],'not_kwl':['Systematic','Baseline','photon','ww','wz','zz','vbs'], 'ODkwl':['Standard Model','ElectroWeak']},

               # Diboson production where at least one boson is a photon
               {'name':'SM Di-photon','kwl':['diphoton','sm'],'not_kwl':['higgs','exotic','triboson','2photon'], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'SM Vector-boson Scattering','kwl':['vbs'],'not_kwl':['ww','wz','zz','triboson','diphoton','2photon'], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'SM V+di-photon','kwl':['2photon'],'not_kwl':[], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'SM V(->qq)+photon','kwl':['diboson','photon'],'not_kwl':['lepton'], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'SM V(->qq)+photon','kwl':['allhadronic','photon'],'not_kwl':[], 'ODkwl':['Standard Model','ElectroWeak']},

               # Exclusive production samples usually have a photon-photon initial state as well
               {'name':'Exclusive Production','kwl':['exclusive'],'not_kwl':[], 'ODkwl':['Standard Model','ElectroWeak','Forward and Small-x QCD Physics']},

               # Diboson photon+V production (again for generators that don't distinguish based on intermediate states, but only final states)
               {'name':'SM Photon+di-electron','kwl':['2electron','photon'],'not_kwl':['2muon'], 'ODkwl':['Standard Model','ElectroWeak','Drell-Yan']},
               {'name':'SM Photon+di-muon','kwl':['2muon','photon'],'not_kwl':['2electron'], 'ODkwl':['Standard Model','ElectroWeak','Drell-Yan']},
               {'name':'SM Photon+di-tau','kwl':['2tau','photon'],'not_kwl':[], 'ODkwl':['Standard Model','ElectroWeak','Drell-Yan']},
               {'name':'SM Photon+electron','kwl':['electron','photon'],'not_kwl':['2muon'], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'SM Photon+muon','kwl':['muon','photon'],'not_kwl':['2electron'], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'SM Photon+tau','kwl':['tau','photon'],'not_kwl':[], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'SM Photon+di-neutrino','kwl':['neutrino','photon'],'not_kwl':['muon','electron','tau'], 'ODkwl':['Standard Model','ElectroWeak']},

               # Individual Z* / gamma production
               {'name':'Specialised Drell-Yan','kwl':['drellyan','Specialised'],'not_kwl':['w','z'], 'ODkwl':['Standard Model','ElectroWeak','Drell-Yan']},
               {'name':'SM Photon Nominal','kwl':['photon','Baseline'],'not_kwl':['2electron','2muon','2tau','neutrino','top','vbs','higgs','z','w'], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'SM Photon Systematic Variations','kwl':['photon','Systematic'],'not_kwl':['top','neutrino','lepton','muon','tau','electron'], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'SM Photon Alternative','kwl':['photon','Alternative'],'not_kwl':['neutrino','muon','2tau','electron','2muon','2electron','w','diboson','z','tau'], 'ODkwl':['Standard Model','ElectroWeak']},

               {'name':'Nominal SM W-boson','kwl':['w','Baseline'],'not_kwl':['jpsi'], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'Systematic Variation SM W-boson','kwl':['w','Systematic'],'not_kwl':[], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'Alternative SM W-boson','kwl':['w','Alternative'],'not_kwl':['top','2photon','photon'], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'Specialised SM W-boson','kwl':['w','Specialised'],'not_kwl':['bsm'], 'ODkwl':['Standard Model','ElectroWeak']},

               {'name':'Nominal SM Z-boson','kwl':['z','Baseline'],'not_kwl':['monojet'], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'Systematic Variation SM Z-boson','kwl':['z','Systematic'],'not_kwl':[], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'Alternative SM Z-boson','kwl':['z','Alternative'],'not_kwl':['monojet','2photon','allhadronic'], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'Specialised SM Z-boson','kwl':['z','Specialised'],'not_kwl':[], 'ODkwl':['Standard Model','ElectroWeak']},
               {'name':'SM Z to neutrinos','kwl':['monojet'],'not_kwl':[], 'ODkwl':['Standard Model','ElectroWeak']},
               # Add special non-resonance Z->bb+photon samples
               {'name':'Specialised SM Z-boson','kwl':['bottom','photon','Specialised'],'not_kwl':['z'], 'ODkwl':['Standard Model','ElectroWeak']},

               # Top physics samples. cutting things up as best we can, but in some cases it's rather difficult
               {'name':'Special ttbar J/Psi','kwl':['jpsi','ttbar'],'not_kwl':[], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM Tri-boson','kwl':['triboson'],'not_kwl':[], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM ttZ','kwl':['ttz'],'not_kwl':[], 'ODkwl':['Standard Model','Top physics','ElectroWeak']},
               {'name':'SM ttW','kwl':['ttw'],'not_kwl':[], 'ODkwl':['Standard Model','Top physics','ElectroWeak']},
               {'name':'SM 4-top','kwl':['4top'],'not_kwl':[], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM tZ','kwl':['tz'],'not_kwl':['bsmtop'], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM ttbar + diboson','kwl':['ttvv'],'not_kwl':[], 'ODkwl':['Standard Model','Top physics','ElectroWeak']},
               {'name':'SM Wt Nominal','kwl':['wt','Baseline'],'not_kwl':[], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM Wt Systematic Variations','kwl':['wt','Systematic'],'not_kwl':[], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM Wt Others','kwl':['wt'],'not_kwl':['Baseline','Systematic'], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM t-channel Single Top','kwl':['tchannel'],'not_kwl':['ckm','exotic'], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM s-channel Single Top','kwl':['schannel'],'not_kwl':['bsm'], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM Wt Sherpa','kwl':['w','Alternative','top'],'not_kwl':[], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM ttbar + bbbar','kwl':['ttbar','bbbar'],'not_kwl':[], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM ttbar + di-photon','kwl':['ttgammagamma'],'not_kwl':[], 'ODkwl':['Standard Model','Top physics','ElectroWeak']},
               {'name':'SM ttbar Nominal','kwl':['ttbar','Baseline'],'not_kwl':['bbbar'], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM ttbar Systematic Variations','kwl':['ttbar','Systematic'],'not_kwl':['higgs','tthiggs','bbbar'], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM ttbar Alternative','kwl':['ttbar','Alternative'],'not_kwl':[], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM ttbar Specialised','kwl':['ttbar','Specialised'],'not_kwl':['jpsi','fcnc','higgs'], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM tWZ','kwl':['singletop'],'not_kwl':['top','lepton'], 'ODkwl':['Standard Model','Top physics']},

               # Catch-all for any other top physics samples
               {'name':'SM Other Top+X Nominal','kwl':['top','Baseline'],'not_kwl':['bbbar','ttbar','higgs','wt','ttbar','tchannel','ttvv','tz','schannel','4top','ttgammagamma'], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM Other Top+X Systematic Variations','kwl':['top','Systematic'],'not_kwl':['4top','higgs','tthiggs','bbbar','wt','ttbar','tz','schannel','tchannel','ttw','ttgammagamma'], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM Other Top+X Alternative','kwl':['top','Alternative'],'not_kwl':['ttbar','w','wt','4top'], 'ODkwl':['Standard Model','Top physics']},
               {'name':'SM Other Top+X Specialised','kwl':['top','Specialised'],'not_kwl':['jpsi','fcnc','ttbar','tchannel','schannel','ckm','wt','ttvv','higgs','4top'], 'ODkwl':['Standard Model','Top physics']},

               # QCD jet production
               {'name':'SM Di-jet Nominal','kwl':['qcd','jets','Baseline'],'not_kwl':['photon'], 'ODkwl':['Standard Model','QCD']},
               {'name':'SM Di-jet Systematic Variation','kwl':['qcd','jets','Systematic'],'not_kwl':['photon'], 'ODkwl':['Standard Model','QCD']},
               {'name':'SM Di-jet Alternative','kwl':['qcd','jets','Alternative'],'not_kwl':['photon'], 'ODkwl':['Standard Model','QCD']},
               {'name':'SM Di-jet Specialised','kwl':['qcd','jets','Specialised'],'not_kwl':[], 'ODkwl':['Standard Model','QCD']},
               {'name':'SM Di-jet Systematic Variation','kwl':['2jet','Systematic'],'not_kwl':['1lepton','wz','diboson','hiddenvalley','zz','ww','z','vbs','jets'], 'ODkwl':['Standard Model','QCD']},
               {'name':'SM Di-jet Alternative','kwl':['2jet','Alternative'],'not_kwl':['1lepton','wz','diboson','hiddenvalley','zz','ww','z','vbs','jets'], 'ODkwl':['Standard Model','QCD']},

               # Simple minbias production
               {'name':'Minimum Bias','kwl':['minbias'],'not_kwl':[], 'ODkwl':['Standard Model','QCD','Minimum Bias','Forward and Small-x QCD Physics']},

               # Catch-all for other SM processes
               {'name':'Other SM','kwl':['3photon'],'not_kwl':[], 'ODkwl':['Standard Model','Miscalleneous']},
               {'name':'Other SM','kwl':['jpsi'],'not_kwl':['ttbar'], 'ODkwl':['Standard Model','Miscalleneous']},
               {'name':'Other SM','kwl':['4photon'],'not_kwl':[], 'ODkwl':['Standard Model','Miscalleneous']},
             ]

