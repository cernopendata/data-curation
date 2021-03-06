# /cdaq/physics/Run2011/5e32/v5.3/HLT/V1 (CMSSW_3_11_0_HLT12)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "HLT" )

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/cdaq/physics/Run2011/5e32/v5.3/HLT/V1')
)

process.streams = cms.PSet(
  A = cms.vstring( 'Commissioning',
    'Cosmics',
    'DoubleElectron',
    'DoubleMu',
    'ElectronHad',
    'HT',
    'HcalHPDNoise',
    'HcalNZS',
    'Jet',
    'METBTag',
    'MinimumBias',
    'MuEG',
    'MuHad',
    'MuOnia',
    'MultiJet',
    'Photon',
    'PhotonHad',
    'SingleElectron',
    'SingleMu',
    'Tau',
    'TauPlusX' ),
  ALCAP0 = cms.vstring( 'AlCaP0' ),
  ALCAPHISYM = cms.vstring( 'AlCaPhiSym' ),
  Calibration = cms.vstring( 'TestEnables' ),
  DQM = cms.vstring( 'OnlineMonitor' ),
  EcalCalibration = cms.vstring( 'EcalLaser' ),
  Express = cms.vstring( 'ExpressPhysics' ),
  HLTDQM = cms.vstring( 'OnlineHltMonitor' ),
  HLTDQMResults = cms.vstring( 'OnlineHltResults' ),
  HLTMON = cms.vstring( 'OfflineMonitor' ),
  NanoDST = cms.vstring( 'L1Accept' ),
  OnlineErrors = cms.vstring( 'FEDMonitor',
    'LogMonitor' ),
  RPCMON = cms.vstring( 'RPCMonitor' )
)

process.datasets = cms.PSet(
  AlCaP0 = cms.vstring( 'AlCa_EcalEta_v2',
    'AlCa_EcalPi0_v3' ),
  AlCaPhiSym = cms.vstring( 'AlCa_EcalPhiSym_v2' ),
  Commissioning = cms.vstring( 'HLT_BeamGas_BSC_v1',
    'HLT_BeamGas_HF_v1',
    'HLT_IsoTrackHB_v2',
    'HLT_IsoTrackHE_v3',
    'HLT_L1SingleEG5_v1',
    'HLT_L1SingleJet36_v1',
    'HLT_L1SingleMuOpen_DT_v1',
    'HLT_L1SingleMuOpen_v1',
    'HLT_L1_Interbunch_BSC_v1',
    'HLT_L1_PreCollisions_v1',
    'HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1',
    'HLT_Photon20_EBOnly_NoSpikeFilter_v1',
    'HLT_Photon20_NoSpikeFilter_v1',
    'HLT_Spike20_v1' ),
  Cosmics = cms.vstring( 'HLT_L1MuOpen_AntiBPTX_v2',
    'HLT_L1Tech_BSC_halo_v1',
    'HLT_L1TrackerCosmics_v2',
    'HLT_L1_BeamHalo_v1',
    'HLT_L2MuOpen_NoVertex_v1',
    'HLT_L3MuonsCosmicTracking_v1',
    'HLT_RegionalCosmicTracking_v1' ),
  DoubleElectron = cms.vstring( 'HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_v1',
    'HLT_Ele17_CaloIdL_CaloIsoVL_Ele15_HFL_v1',
    'HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1',
    'HLT_Ele17_CaloIdL_CaloIsoVL_v1',
    'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v2',
    'HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v1',
    'HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v1',
    'HLT_Ele8_CaloIdL_CaloIsoVL_v1',
    'HLT_Ele8_CaloIdL_TrkIdVL_v1',
    'HLT_Ele8_v1',
    'HLT_Photon20_CaloIdVT_IsoT_Ele8_CaloIdL_CaloIsoVL_v1',
    'HLT_TripleEle10_CaloIdL_TrkIdVL_v1' ),
  DoubleMu = cms.vstring( 'HLT_DoubleMu3_v3',
    'HLT_DoubleMu4_Acoplanarity03_v1',
    'HLT_DoubleMu6_v1',
    'HLT_DoubleMu7_v1',
    'HLT_L1DoubleMu0_v1',
    'HLT_L2DoubleMu0_v2',
    'HLT_L2DoubleMu35_NoVertex_v1',
    'HLT_Mu8_Jet40_v2',
    'HLT_TripleMu5_v2' ),
  EcalLaser = cms.vstring( 'HLT_EcalCalibration_v1' ),
  ElectronHad = cms.vstring( 'HLT_DoubleEle8_CaloIdL_TrkIdVL_HT160_v2',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_HT160_v2',
    'HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v2',
    'HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v2',
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralDiJet30_v1',
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralJet30_v1',
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralJet40_BTagIP_v1',
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralTriJet30_v1' ),
  ExpressPhysics = cms.vstring( 'HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1',
    'HLT_L1Tech_BSC_minBias_threshold1_v2',
    'HLT_Mu15_v2',
    'HLT_ZeroBias_v1' ),
  FEDMonitor = cms.vstring( 'HLT_DTErrors_v1' ),
  HT = cms.vstring( 'HLT_DiJet100_PT100_v1',
    'HLT_DiJet130_PT130_v1',
    'HLT_DiJet70_PT70_v1',
    'HLT_HT160_v2',
    'HLT_HT240_v2',
    'HLT_HT260_MHT60_v2',
    'HLT_HT260_v2',
    'HLT_HT300_MHT75_v2',
    'HLT_HT300_v2',
    'HLT_HT360_v2',
    'HLT_HT440_v2',
    'HLT_HT520_v2',
    'HLT_MR100_v1',
    'HLT_Meff440_v2',
    'HLT_Meff520_v2',
    'HLT_Meff640_v2',
    'HLT_R032_MR100_v1',
    'HLT_R032_v1',
    'HLT_R035_MR100_v1' ),
  HcalHPDNoise = cms.vstring( 'HLT_GlobalRunHPDNoise_v2',
    'HLT_L1Tech_HBHEHO_totalOR_v1' ),
  HcalNZS = cms.vstring( 'HLT_HcalNZS_v2',
    'HLT_HcalPhiSym_v2' ),
  Jet = cms.vstring( 'HLT_DiJetAve100U_v4',
    'HLT_DiJetAve140U_v4',
    'HLT_DiJetAve15U_v4',
    'HLT_DiJetAve180U_v4',
    'HLT_DiJetAve300U_v4',
    'HLT_DiJetAve30U_v4',
    'HLT_DiJetAve50U_v4',
    'HLT_DiJetAve70U_v4',
    'HLT_Jet110_v1',
    'HLT_Jet150_v1',
    'HLT_Jet190_v1',
    'HLT_Jet240_v1',
    'HLT_Jet30_v1',
    'HLT_Jet370_NoJetID_v1',
    'HLT_Jet370_v1',
    'HLT_Jet60_v1',
    'HLT_Jet80_v1' ),
  L1Accept = cms.vstring( 'HLT_Physics_NanoDST_v1' ),
  LogMonitor = cms.vstring( 'HLT_LogMonitor_v1' ),
  METBTag = cms.vstring( 'HLT_BTagMu_DiJet20_Mu5_v1',
    'HLT_BTagMu_DiJet60_Mu7_v1',
    'HLT_BTagMu_DiJet80_Mu9_v1',
    'HLT_CentralJet80_MET100_v1',
    'HLT_CentralJet80_MET160_v1',
    'HLT_CentralJet80_MET65_v1',
    'HLT_CentralJet80_MET80_v1',
    'HLT_DiJet60_MET45_v1',
    'HLT_MET100_v1',
    'HLT_MET120_v1',
    'HLT_MET200_v1',
    'HLT_PFMHT150_v1' ),
  MinimumBias = cms.vstring( 'HLT_JetE30_NoBPTX3BX_NoHalo_v2',
    'HLT_JetE30_NoBPTX_NoHalo_v2',
    'HLT_JetE30_NoBPTX_v1',
    'HLT_L1Tech_BSC_minBias_threshold1_v2',
    'HLT_Physics_v1',
    'HLT_PixelTracks_Multiplicity110_v1',
    'HLT_PixelTracks_Multiplicity125_v1',
    'HLT_Random_v1',
    'HLT_ZeroBias_v1' ),
  MuEG = cms.vstring( 'HLT_DoubleMu5_Ele8_CaloIdL_TrkIdVL_v2',
    'HLT_DoubleMu5_Ele8_v2',
    'HLT_Mu10_Ele10_CaloIdL_v2',
    'HLT_Mu15_DoublePhoton15_CaloIdL_v2',
    'HLT_Mu15_Photon20_CaloIdL_v2',
    'HLT_Mu17_Ele8_CaloIdL_v1',
    'HLT_Mu5_DoubleEle8_v2',
    'HLT_Mu5_Ele8_CaloIdL_TrkIdVL_Ele8_v2',
    'HLT_Mu8_Ele17_CaloIdL_v1',
    'HLT_Mu8_Photon20_CaloIdVT_IsoT_v2' ),
  MuHad = cms.vstring( 'HLT_DoubleMu3_HT160_v2',
    'HLT_DoubleMu3_HT200_v2',
    'HLT_IsoMu17_CentralJet40_BTagIP_v1',
    'HLT_Mu17_CentralJet30_v1',
    'HLT_Mu17_CentralJet40_BTagIP_v1',
    'HLT_Mu17_DiCentralJet30_v1',
    'HLT_Mu17_TriCentralJet30_v1',
    'HLT_Mu3_Ele8_CaloIdL_TrkIdVL_HT160_v2',
    'HLT_Mu3_Ele8_CaloIdT_TrkIdVL_HT160_v2',
    'HLT_Mu5_HT200_v3',
    'HLT_Mu8_HT200_v2' ),
  MuOnia = cms.vstring( 'HLT_DoubleMu3_Bs_v1',
    'HLT_DoubleMu3_Jpsi_v1',
    'HLT_DoubleMu3_Quarkonium_v1',
    'HLT_Mu3_Track3_Jpsi_v4',
    'HLT_Mu5_L2Mu2_Jpsi_v1',
    'HLT_Mu5_L2Mu2_v1',
    'HLT_Mu7_Track5_Jpsi_v1',
    'HLT_Mu7_Track7_Jpsi_v1' ),
  MultiJet = cms.vstring( 'HLT_DoubleJet30_ForwardBackward_v1',
    'HLT_DoubleJet60_ForwardBackward_v1',
    'HLT_DoubleJet70_ForwardBackward_v1',
    'HLT_DoubleJet80_ForwardBackward_v1',
    'HLT_ExclDiJet60_HFAND_v1',
    'HLT_ExclDiJet60_HFOR_v1',
    'HLT_QuadJet40_IsoPFTau40_v1',
    'HLT_QuadJet40_v1',
    'HLT_QuadJet50_BTagIP_v1',
    'HLT_QuadJet50_Jet40_v1',
    'HLT_QuadJet60_v1',
    'HLT_QuadJet70_v1' ),
  OfflineMonitor = cms.vstring( 'AlCa_EcalEta_v2',
    'AlCa_EcalPhiSym_v2',
    'AlCa_EcalPi0_v3',
    'AlCa_RPCMuonNoHits_v2',
    'AlCa_RPCMuonNoTriggers_v2',
    'AlCa_RPCMuonNormalisation_v2',
    'HLT_BTagMu_DiJet20_Mu5_v1',
    'HLT_BTagMu_DiJet60_Mu7_v1',
    'HLT_BTagMu_DiJet80_Mu9_v1',
    'HLT_BeamGas_BSC_v1',
    'HLT_BeamGas_HF_v1',
    'HLT_CentralJet80_MET100_v1',
    'HLT_CentralJet80_MET160_v1',
    'HLT_CentralJet80_MET65_v1',
    'HLT_CentralJet80_MET80_v1',
    'HLT_DTErrors_v1',
    'HLT_DiJet100_PT100_v1',
    'HLT_DiJet130_PT130_v1',
    'HLT_DiJet60_MET45_v1',
    'HLT_DiJet70_PT70_v1',
    'HLT_DiJetAve100U_v4',
    'HLT_DiJetAve140U_v4',
    'HLT_DiJetAve15U_v4',
    'HLT_DiJetAve180U_v4',
    'HLT_DiJetAve300U_v4',
    'HLT_DiJetAve30U_v4',
    'HLT_DiJetAve50U_v4',
    'HLT_DiJetAve70U_v4',
    'HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_v1',
    'HLT_DoubleEle8_CaloIdL_TrkIdVL_HT160_v2',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_HT160_v2',
    'HLT_DoubleIsoPFTau20_Trk5_v1',
    'HLT_DoubleJet30_ForwardBackward_v1',
    'HLT_DoubleJet60_ForwardBackward_v1',
    'HLT_DoubleJet70_ForwardBackward_v1',
    'HLT_DoubleJet80_ForwardBackward_v1',
    'HLT_DoubleMu3_Bs_v1',
    'HLT_DoubleMu3_HT160_v2',
    'HLT_DoubleMu3_HT200_v2',
    'HLT_DoubleMu3_Jpsi_v1',
    'HLT_DoubleMu3_Quarkonium_v1',
    'HLT_DoubleMu3_v3',
    'HLT_DoubleMu4_Acoplanarity03_v1',
    'HLT_DoubleMu5_Ele8_CaloIdL_TrkIdVL_v2',
    'HLT_DoubleMu5_Ele8_v2',
    'HLT_DoubleMu6_v1',
    'HLT_DoubleMu7_v1',
    'HLT_DoublePhoton33_v1',
    'HLT_DoublePhoton5_IsoVL_CEP_v1',
    'HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v2',
    'HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v2',
    'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1',
    'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1',
    'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1',
    'HLT_Ele15_CaloIdVT_TrkIdT_LooseIsoPFTau15_v1',
    'HLT_Ele17_CaloIdL_CaloIsoVL_Ele15_HFL_v1',
    'HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1',
    'HLT_Ele17_CaloIdL_CaloIsoVL_v1',
    'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v2',
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralDiJet30_v1',
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralJet30_v1',
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralJet40_BTagIP_v1',
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralTriJet30_v1',
    'HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1',
    'HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v1',
    'HLT_Ele45_CaloIdVT_TrkIdT_v1',
    'HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v1',
    'HLT_Ele8_CaloIdL_CaloIsoVL_v1',
    'HLT_Ele8_CaloIdL_TrkIdVL_v1',
    'HLT_Ele8_v1',
    'HLT_Ele90_NoSpikeFilter_v1',
    'HLT_ExclDiJet60_HFAND_v1',
    'HLT_ExclDiJet60_HFOR_v1',
    'HLT_GlobalRunHPDNoise_v2',
    'HLT_HT160_v2',
    'HLT_HT240_v2',
    'HLT_HT260_MHT60_v2',
    'HLT_HT260_v2',
    'HLT_HT300_MHT75_v2',
    'HLT_HT300_v2',
    'HLT_HT360_v2',
    'HLT_HT440_v2',
    'HLT_HT520_v2',
    'HLT_HcalNZS_v2',
    'HLT_HcalPhiSym_v2',
    'HLT_IsoMu12_LooseIsoPFTau10_v1',
    'HLT_IsoMu12_v1',
    'HLT_IsoMu15_v5',
    'HLT_IsoMu17_CentralJet40_BTagIP_v1',
    'HLT_IsoMu17_v5',
    'HLT_IsoMu30_v1',
    'HLT_IsoPFTau35_Trk20_MET45_v1',
    'HLT_IsoTrackHB_v2',
    'HLT_IsoTrackHE_v3',
    'HLT_Jet110_v1',
    'HLT_Jet150_v1',
    'HLT_Jet190_v1',
    'HLT_Jet240_v1',
    'HLT_Jet30_v1',
    'HLT_Jet370_NoJetID_v1',
    'HLT_Jet370_v1',
    'HLT_Jet60_v1',
    'HLT_Jet80_v1',
    'HLT_JetE30_NoBPTX3BX_NoHalo_v2',
    'HLT_JetE30_NoBPTX_NoHalo_v2',
    'HLT_JetE30_NoBPTX_v1',
    'HLT_L1DoubleMu0_v1',
    'HLT_L1MuOpen_AntiBPTX_v2',
    'HLT_L1SingleEG5_v1',
    'HLT_L1SingleJet36_v1',
    'HLT_L1SingleMu10_v1',
    'HLT_L1SingleMu20_v1',
    'HLT_L1SingleMuOpen_DT_v1',
    'HLT_L1SingleMuOpen_v1',
    'HLT_L1Tech_BSC_halo_v1',
    'HLT_L1Tech_HBHEHO_totalOR_v1',
    'HLT_L1TrackerCosmics_v2',
    'HLT_L1_BeamHalo_v1',
    'HLT_L1_Interbunch_BSC_v1',
    'HLT_L1_PreCollisions_v1',
    'HLT_L2DoubleMu0_v2',
    'HLT_L2DoubleMu35_NoVertex_v1',
    'HLT_L2Mu10_v1',
    'HLT_L2Mu20_v1',
    'HLT_L2MuOpen_NoVertex_v1',
    'HLT_L3MuonsCosmicTracking_v1',
    'HLT_LogMonitor_v1',
    'HLT_MET100_v1',
    'HLT_MET120_v1',
    'HLT_MET200_v1',
    'HLT_MR100_v1',
    'HLT_Meff440_v2',
    'HLT_Meff520_v2',
    'HLT_Meff640_v2',
    'HLT_Mu10_Ele10_CaloIdL_v2',
    'HLT_Mu12_v1',
    'HLT_Mu15_DoublePhoton15_CaloIdL_v2',
    'HLT_Mu15_LooseIsoPFTau20_v1',
    'HLT_Mu15_Photon20_CaloIdL_v2',
    'HLT_Mu15_v2',
    'HLT_Mu17_CentralJet30_v1',
    'HLT_Mu17_CentralJet40_BTagIP_v1',
    'HLT_Mu17_DiCentralJet30_v1',
    'HLT_Mu17_Ele8_CaloIdL_v1',
    'HLT_Mu17_TriCentralJet30_v1',
    'HLT_Mu20_v1',
    'HLT_Mu24_v1',
    'HLT_Mu30_v1',
    'HLT_Mu3_Ele8_CaloIdL_TrkIdVL_HT160_v2',
    'HLT_Mu3_Ele8_CaloIdT_TrkIdVL_HT160_v2',
    'HLT_Mu3_Track3_Jpsi_v4',
    'HLT_Mu3_v3',
    'HLT_Mu5_DoubleEle8_v2',
    'HLT_Mu5_Ele8_CaloIdL_TrkIdVL_Ele8_v2',
    'HLT_Mu5_HT200_v3',
    'HLT_Mu5_L2Mu2_Jpsi_v1',
    'HLT_Mu5_L2Mu2_v1',
    'HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1',
    'HLT_Mu5_v3',
    'HLT_Mu7_Track5_Jpsi_v1',
    'HLT_Mu7_Track7_Jpsi_v1',
    'HLT_Mu8_Ele17_CaloIdL_v1',
    'HLT_Mu8_HT200_v2',
    'HLT_Mu8_Jet40_v2',
    'HLT_Mu8_Photon20_CaloIdVT_IsoT_v2',
    'HLT_Mu8_v1',
    'HLT_PFMHT150_v1',
    'HLT_Photon125_NoSpikeFilter_v1',
    'HLT_Photon20_CaloIdVT_IsoT_Ele8_CaloIdL_CaloIsoVL_v1',
    'HLT_Photon20_R9Id_Photon18_R9Id_v1',
    'HLT_Photon26_CaloIdL_IsoVL_Photon18_CaloIdL_IsoVL_v1',
    'HLT_Photon26_CaloIdL_IsoVL_Photon18_v1',
    'HLT_Photon26_IsoVL_Photon18_IsoVL_v1',
    'HLT_Photon26_IsoVL_Photon18_v1',
    'HLT_Photon26_Photon18_v1',
    'HLT_Photon30_CaloIdVL_IsoL_v1',
    'HLT_Photon30_CaloIdVL_v1',
    'HLT_Photon32_CaloIdL_Photon26_CaloIdL_v1',
    'HLT_Photon60_CaloIdL_HT200_v1',
    'HLT_Photon70_CaloIdL_HT200_v1',
    'HLT_Photon70_CaloIdL_HT300_v1',
    'HLT_Photon70_CaloIdL_MHT30_v1',
    'HLT_Photon70_CaloIdL_MHT50_v1',
    'HLT_Photon75_CaloIdVL_IsoL_v1',
    'HLT_Photon75_CaloIdVL_v1',
    'HLT_Physics_v1',
    'HLT_PixelTracks_Multiplicity110_v1',
    'HLT_PixelTracks_Multiplicity125_v1',
    'HLT_QuadJet40_IsoPFTau40_v1',
    'HLT_QuadJet40_v1',
    'HLT_QuadJet50_BTagIP_v1',
    'HLT_QuadJet50_Jet40_v1',
    'HLT_QuadJet60_v1',
    'HLT_QuadJet70_v1',
    'HLT_R032_MR100_v1',
    'HLT_R032_v1',
    'HLT_R035_MR100_v1',
    'HLT_Random_v1',
    'HLT_RegionalCosmicTracking_v1',
    'HLT_TripleEle10_CaloIdL_TrkIdVL_v1',
    'HLT_TripleMu5_v2',
    'HLT_ZeroBias_v1' ),
  OnlineHltMonitor = cms.vstring( 'AlCa_EcalEta_v2',
    'AlCa_EcalPhiSym_v2',
    'AlCa_EcalPi0_v3',
    'AlCa_RPCMuonNoHits_v2',
    'AlCa_RPCMuonNoTriggers_v2',
    'AlCa_RPCMuonNormalisation_v2',
    'HLT_BTagMu_DiJet20_Mu5_v1',
    'HLT_BTagMu_DiJet60_Mu7_v1',
    'HLT_BTagMu_DiJet80_Mu9_v1',
    'HLT_BeamGas_BSC_v1',
    'HLT_BeamGas_HF_v1',
    'HLT_CentralJet80_MET100_v1',
    'HLT_CentralJet80_MET160_v1',
    'HLT_CentralJet80_MET65_v1',
    'HLT_CentralJet80_MET80_v1',
    'HLT_DTErrors_v1',
    'HLT_DiJet100_PT100_v1',
    'HLT_DiJet130_PT130_v1',
    'HLT_DiJet60_MET45_v1',
    'HLT_DiJet70_PT70_v1',
    'HLT_DiJetAve100U_v4',
    'HLT_DiJetAve140U_v4',
    'HLT_DiJetAve15U_v4',
    'HLT_DiJetAve180U_v4',
    'HLT_DiJetAve300U_v4',
    'HLT_DiJetAve30U_v4',
    'HLT_DiJetAve50U_v4',
    'HLT_DiJetAve70U_v4',
    'HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_v1',
    'HLT_DoubleEle8_CaloIdL_TrkIdVL_HT160_v2',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_HT160_v2',
    'HLT_DoubleIsoPFTau20_Trk5_v1',
    'HLT_DoubleJet30_ForwardBackward_v1',
    'HLT_DoubleJet60_ForwardBackward_v1',
    'HLT_DoubleJet70_ForwardBackward_v1',
    'HLT_DoubleJet80_ForwardBackward_v1',
    'HLT_DoubleMu3_Bs_v1',
    'HLT_DoubleMu3_HT160_v2',
    'HLT_DoubleMu3_HT200_v2',
    'HLT_DoubleMu3_Jpsi_v1',
    'HLT_DoubleMu3_Quarkonium_v1',
    'HLT_DoubleMu3_v3',
    'HLT_DoubleMu4_Acoplanarity03_v1',
    'HLT_DoubleMu5_Ele8_CaloIdL_TrkIdVL_v2',
    'HLT_DoubleMu5_Ele8_v2',
    'HLT_DoubleMu6_v1',
    'HLT_DoubleMu7_v1',
    'HLT_DoublePhoton33_v1',
    'HLT_DoublePhoton5_IsoVL_CEP_v1',
    'HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v2',
    'HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v2',
    'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1',
    'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1',
    'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1',
    'HLT_Ele15_CaloIdVT_TrkIdT_LooseIsoPFTau15_v1',
    'HLT_Ele17_CaloIdL_CaloIsoVL_Ele15_HFL_v1',
    'HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1',
    'HLT_Ele17_CaloIdL_CaloIsoVL_v1',
    'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v2',
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralDiJet30_v1',
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralJet30_v1',
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralJet40_BTagIP_v1',
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralTriJet30_v1',
    'HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1',
    'HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v1',
    'HLT_Ele45_CaloIdVT_TrkIdT_v1',
    'HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v1',
    'HLT_Ele8_CaloIdL_CaloIsoVL_v1',
    'HLT_Ele8_CaloIdL_TrkIdVL_v1',
    'HLT_Ele8_v1',
    'HLT_Ele90_NoSpikeFilter_v1',
    'HLT_ExclDiJet60_HFAND_v1',
    'HLT_ExclDiJet60_HFOR_v1',
    'HLT_GlobalRunHPDNoise_v2',
    'HLT_HT160_v2',
    'HLT_HT240_v2',
    'HLT_HT260_MHT60_v2',
    'HLT_HT260_v2',
    'HLT_HT300_MHT75_v2',
    'HLT_HT300_v2',
    'HLT_HT360_v2',
    'HLT_HT440_v2',
    'HLT_HT520_v2',
    'HLT_HcalNZS_v2',
    'HLT_HcalPhiSym_v2',
    'HLT_IsoMu12_LooseIsoPFTau10_v1',
    'HLT_IsoMu12_v1',
    'HLT_IsoMu15_v5',
    'HLT_IsoMu17_CentralJet40_BTagIP_v1',
    'HLT_IsoMu17_v5',
    'HLT_IsoMu30_v1',
    'HLT_IsoPFTau35_Trk20_MET45_v1',
    'HLT_IsoTrackHB_v2',
    'HLT_IsoTrackHE_v3',
    'HLT_Jet110_v1',
    'HLT_Jet150_v1',
    'HLT_Jet190_v1',
    'HLT_Jet240_v1',
    'HLT_Jet30_v1',
    'HLT_Jet370_NoJetID_v1',
    'HLT_Jet370_v1',
    'HLT_Jet60_v1',
    'HLT_Jet80_v1',
    'HLT_JetE30_NoBPTX3BX_NoHalo_v2',
    'HLT_JetE30_NoBPTX_NoHalo_v2',
    'HLT_JetE30_NoBPTX_v1',
    'HLT_L1DoubleMu0_v1',
    'HLT_L1MuOpen_AntiBPTX_v2',
    'HLT_L1SingleEG5_v1',
    'HLT_L1SingleJet36_v1',
    'HLT_L1SingleMu10_v1',
    'HLT_L1SingleMu20_v1',
    'HLT_L1SingleMuOpen_DT_v1',
    'HLT_L1SingleMuOpen_v1',
    'HLT_L1Tech_BSC_halo_v1',
    'HLT_L1Tech_HBHEHO_totalOR_v1',
    'HLT_L1TrackerCosmics_v2',
    'HLT_L1_BeamHalo_v1',
    'HLT_L1_Interbunch_BSC_v1',
    'HLT_L1_PreCollisions_v1',
    'HLT_L2DoubleMu0_v2',
    'HLT_L2DoubleMu35_NoVertex_v1',
    'HLT_L2Mu10_v1',
    'HLT_L2Mu20_v1',
    'HLT_L2MuOpen_NoVertex_v1',
    'HLT_L3MuonsCosmicTracking_v1',
    'HLT_LogMonitor_v1',
    'HLT_MET100_v1',
    'HLT_MET120_v1',
    'HLT_MET200_v1',
    'HLT_MR100_v1',
    'HLT_Meff440_v2',
    'HLT_Meff520_v2',
    'HLT_Meff640_v2',
    'HLT_Mu10_Ele10_CaloIdL_v2',
    'HLT_Mu12_v1',
    'HLT_Mu15_DoublePhoton15_CaloIdL_v2',
    'HLT_Mu15_LooseIsoPFTau20_v1',
    'HLT_Mu15_Photon20_CaloIdL_v2',
    'HLT_Mu15_v2',
    'HLT_Mu17_CentralJet30_v1',
    'HLT_Mu17_CentralJet40_BTagIP_v1',
    'HLT_Mu17_DiCentralJet30_v1',
    'HLT_Mu17_Ele8_CaloIdL_v1',
    'HLT_Mu17_TriCentralJet30_v1',
    'HLT_Mu20_v1',
    'HLT_Mu24_v1',
    'HLT_Mu30_v1',
    'HLT_Mu3_Ele8_CaloIdL_TrkIdVL_HT160_v2',
    'HLT_Mu3_Ele8_CaloIdT_TrkIdVL_HT160_v2',
    'HLT_Mu3_Track3_Jpsi_v4',
    'HLT_Mu3_v3',
    'HLT_Mu5_DoubleEle8_v2',
    'HLT_Mu5_Ele8_CaloIdL_TrkIdVL_Ele8_v2',
    'HLT_Mu5_HT200_v3',
    'HLT_Mu5_L2Mu2_Jpsi_v1',
    'HLT_Mu5_L2Mu2_v1',
    'HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1',
    'HLT_Mu5_v3',
    'HLT_Mu7_Track5_Jpsi_v1',
    'HLT_Mu7_Track7_Jpsi_v1',
    'HLT_Mu8_Ele17_CaloIdL_v1',
    'HLT_Mu8_HT200_v2',
    'HLT_Mu8_Jet40_v2',
    'HLT_Mu8_Photon20_CaloIdVT_IsoT_v2',
    'HLT_Mu8_v1',
    'HLT_PFMHT150_v1',
    'HLT_Photon125_NoSpikeFilter_v1',
    'HLT_Photon20_CaloIdVT_IsoT_Ele8_CaloIdL_CaloIsoVL_v1',
    'HLT_Photon20_R9Id_Photon18_R9Id_v1',
    'HLT_Photon26_CaloIdL_IsoVL_Photon18_CaloIdL_IsoVL_v1',
    'HLT_Photon26_CaloIdL_IsoVL_Photon18_v1',
    'HLT_Photon26_IsoVL_Photon18_IsoVL_v1',
    'HLT_Photon26_IsoVL_Photon18_v1',
    'HLT_Photon26_Photon18_v1',
    'HLT_Photon30_CaloIdVL_IsoL_v1',
    'HLT_Photon30_CaloIdVL_v1',
    'HLT_Photon32_CaloIdL_Photon26_CaloIdL_v1',
    'HLT_Photon60_CaloIdL_HT200_v1',
    'HLT_Photon70_CaloIdL_HT200_v1',
    'HLT_Photon70_CaloIdL_HT300_v1',
    'HLT_Photon70_CaloIdL_MHT30_v1',
    'HLT_Photon70_CaloIdL_MHT50_v1',
    'HLT_Photon75_CaloIdVL_IsoL_v1',
    'HLT_Photon75_CaloIdVL_v1',
    'HLT_Physics_v1',
    'HLT_PixelTracks_Multiplicity110_v1',
    'HLT_PixelTracks_Multiplicity125_v1',
    'HLT_QuadJet40_IsoPFTau40_v1',
    'HLT_QuadJet40_v1',
    'HLT_QuadJet50_BTagIP_v1',
    'HLT_QuadJet50_Jet40_v1',
    'HLT_QuadJet60_v1',
    'HLT_QuadJet70_v1',
    'HLT_R032_MR100_v1',
    'HLT_R032_v1',
    'HLT_R035_MR100_v1',
    'HLT_Random_v1',
    'HLT_RegionalCosmicTracking_v1',
    'HLT_TripleEle10_CaloIdL_TrkIdVL_v1',
    'HLT_TripleMu5_v2',
    'HLT_ZeroBias_v1' ),
  OnlineHltResults = cms.vstring( 'HLTriggerFinalPath' ),
  OnlineMonitor = cms.vstring( 'HLT_BTagMu_DiJet20_Mu5_v1',
    'HLT_BTagMu_DiJet60_Mu7_v1',
    'HLT_BTagMu_DiJet80_Mu9_v1',
    'HLT_BeamGas_BSC_v1',
    'HLT_BeamGas_HF_v1',
    'HLT_Calibration_v1',
    'HLT_CentralJet80_MET100_v1',
    'HLT_CentralJet80_MET160_v1',
    'HLT_CentralJet80_MET65_v1',
    'HLT_CentralJet80_MET80_v1',
    'HLT_DTErrors_v1',
    'HLT_DiJet100_PT100_v1',
    'HLT_DiJet130_PT130_v1',
    'HLT_DiJet60_MET45_v1',
    'HLT_DiJet70_PT70_v1',
    'HLT_DiJetAve100U_v4',
    'HLT_DiJetAve140U_v4',
    'HLT_DiJetAve15U_v4',
    'HLT_DiJetAve180U_v4',
    'HLT_DiJetAve300U_v4',
    'HLT_DiJetAve30U_v4',
    'HLT_DiJetAve50U_v4',
    'HLT_DiJetAve70U_v4',
    'HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_v1',
    'HLT_DoubleEle8_CaloIdL_TrkIdVL_HT160_v2',
    'HLT_DoubleEle8_CaloIdT_TrkIdVL_HT160_v2',
    'HLT_DoubleIsoPFTau20_Trk5_v1',
    'HLT_DoubleJet30_ForwardBackward_v1',
    'HLT_DoubleJet60_ForwardBackward_v1',
    'HLT_DoubleJet70_ForwardBackward_v1',
    'HLT_DoubleJet80_ForwardBackward_v1',
    'HLT_DoubleMu3_Bs_v1',
    'HLT_DoubleMu3_HT160_v2',
    'HLT_DoubleMu3_HT200_v2',
    'HLT_DoubleMu3_Jpsi_v1',
    'HLT_DoubleMu3_Quarkonium_v1',
    'HLT_DoubleMu3_v3',
    'HLT_DoubleMu4_Acoplanarity03_v1',
    'HLT_DoubleMu5_Ele8_CaloIdL_TrkIdVL_v2',
    'HLT_DoubleMu5_Ele8_v2',
    'HLT_DoubleMu6_v1',
    'HLT_DoubleMu7_v1',
    'HLT_DoublePhoton33_v1',
    'HLT_DoublePhoton5_IsoVL_CEP_v1',
    'HLT_EcalCalibration_v1',
    'HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v2',
    'HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v2',
    'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1',
    'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1',
    'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1',
    'HLT_Ele15_CaloIdVT_TrkIdT_LooseIsoPFTau15_v1',
    'HLT_Ele17_CaloIdL_CaloIsoVL_Ele15_HFL_v1',
    'HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1',
    'HLT_Ele17_CaloIdL_CaloIsoVL_v1',
    'HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v2',
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralDiJet30_v1',
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralJet30_v1',
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralJet40_BTagIP_v1',
    'HLT_Ele25_CaloIdVT_TrkIdT_CentralTriJet30_v1',
    'HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1',
    'HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v1',
    'HLT_Ele45_CaloIdVT_TrkIdT_v1',
    'HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v1',
    'HLT_Ele8_CaloIdL_CaloIsoVL_v1',
    'HLT_Ele8_CaloIdL_TrkIdVL_v1',
    'HLT_Ele8_v1',
    'HLT_Ele90_NoSpikeFilter_v1',
    'HLT_ExclDiJet60_HFAND_v1',
    'HLT_ExclDiJet60_HFOR_v1',
    'HLT_GlobalRunHPDNoise_v2',
    'HLT_HT160_v2',
    'HLT_HT240_v2',
    'HLT_HT260_MHT60_v2',
    'HLT_HT260_v2',
    'HLT_HT300_MHT75_v2',
    'HLT_HT300_v2',
    'HLT_HT360_v2',
    'HLT_HT440_v2',
    'HLT_HT520_v2',
    'HLT_HcalCalibration_v1',
    'HLT_HcalNZS_v2',
    'HLT_HcalPhiSym_v2',
    'HLT_IsoMu12_LooseIsoPFTau10_v1',
    'HLT_IsoMu12_v1',
    'HLT_IsoMu15_v5',
    'HLT_IsoMu17_CentralJet40_BTagIP_v1',
    'HLT_IsoMu17_v5',
    'HLT_IsoMu30_v1',
    'HLT_IsoPFTau35_Trk20_MET45_v1',
    'HLT_IsoTrackHB_v2',
    'HLT_IsoTrackHE_v3',
    'HLT_Jet110_v1',
    'HLT_Jet150_v1',
    'HLT_Jet190_v1',
    'HLT_Jet240_v1',
    'HLT_Jet30_v1',
    'HLT_Jet370_NoJetID_v1',
    'HLT_Jet370_v1',
    'HLT_Jet60_v1',
    'HLT_Jet80_v1',
    'HLT_JetE30_NoBPTX3BX_NoHalo_v2',
    'HLT_JetE30_NoBPTX_NoHalo_v2',
    'HLT_JetE30_NoBPTX_v1',
    'HLT_L1DoubleMu0_v1',
    'HLT_L1MuOpen_AntiBPTX_v2',
    'HLT_L1SingleEG5_v1',
    'HLT_L1SingleJet36_v1',
    'HLT_L1SingleMu10_v1',
    'HLT_L1SingleMu20_v1',
    'HLT_L1SingleMuOpen_DT_v1',
    'HLT_L1SingleMuOpen_v1',
    'HLT_L1Tech_BSC_halo_v1',
    'HLT_L1Tech_HBHEHO_totalOR_v1',
    'HLT_L1TrackerCosmics_v2',
    'HLT_L1_BeamHalo_v1',
    'HLT_L1_Interbunch_BSC_v1',
    'HLT_L1_PreCollisions_v1',
    'HLT_L2DoubleMu0_v2',
    'HLT_L2DoubleMu35_NoVertex_v1',
    'HLT_L2Mu10_v1',
    'HLT_L2Mu20_v1',
    'HLT_L2MuOpen_NoVertex_v1',
    'HLT_L3MuonsCosmicTracking_v1',
    'HLT_LogMonitor_v1',
    'HLT_MET100_v1',
    'HLT_MET120_v1',
    'HLT_MET200_v1',
    'HLT_MR100_v1',
    'HLT_Meff440_v2',
    'HLT_Meff520_v2',
    'HLT_Meff640_v2',
    'HLT_Mu10_Ele10_CaloIdL_v2',
    'HLT_Mu12_v1',
    'HLT_Mu15_DoublePhoton15_CaloIdL_v2',
    'HLT_Mu15_LooseIsoPFTau20_v1',
    'HLT_Mu15_Photon20_CaloIdL_v2',
    'HLT_Mu15_v2',
    'HLT_Mu17_CentralJet30_v1',
    'HLT_Mu17_CentralJet40_BTagIP_v1',
    'HLT_Mu17_DiCentralJet30_v1',
    'HLT_Mu17_Ele8_CaloIdL_v1',
    'HLT_Mu17_TriCentralJet30_v1',
    'HLT_Mu20_v1',
    'HLT_Mu24_v1',
    'HLT_Mu30_v1',
    'HLT_Mu3_Ele8_CaloIdL_TrkIdVL_HT160_v2',
    'HLT_Mu3_Ele8_CaloIdT_TrkIdVL_HT160_v2',
    'HLT_Mu3_Track3_Jpsi_v4',
    'HLT_Mu3_v3',
    'HLT_Mu5_DoubleEle8_v2',
    'HLT_Mu5_Ele8_CaloIdL_TrkIdVL_Ele8_v2',
    'HLT_Mu5_HT200_v3',
    'HLT_Mu5_L2Mu2_Jpsi_v1',
    'HLT_Mu5_L2Mu2_v1',
    'HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1',
    'HLT_Mu5_v3',
    'HLT_Mu7_Track5_Jpsi_v1',
    'HLT_Mu7_Track7_Jpsi_v1',
    'HLT_Mu8_Ele17_CaloIdL_v1',
    'HLT_Mu8_HT200_v2',
    'HLT_Mu8_Jet40_v2',
    'HLT_Mu8_Photon20_CaloIdVT_IsoT_v2',
    'HLT_Mu8_v1',
    'HLT_PFMHT150_v1',
    'HLT_Photon125_NoSpikeFilter_v1',
    'HLT_Photon20_CaloIdVT_IsoT_Ele8_CaloIdL_CaloIsoVL_v1',
    'HLT_Photon20_R9Id_Photon18_R9Id_v1',
    'HLT_Photon26_CaloIdL_IsoVL_Photon18_CaloIdL_IsoVL_v1',
    'HLT_Photon26_CaloIdL_IsoVL_Photon18_v1',
    'HLT_Photon26_IsoVL_Photon18_IsoVL_v1',
    'HLT_Photon26_IsoVL_Photon18_v1',
    'HLT_Photon26_Photon18_v1',
    'HLT_Photon30_CaloIdVL_IsoL_v1',
    'HLT_Photon30_CaloIdVL_v1',
    'HLT_Photon32_CaloIdL_Photon26_CaloIdL_v1',
    'HLT_Photon60_CaloIdL_HT200_v1',
    'HLT_Photon70_CaloIdL_HT200_v1',
    'HLT_Photon70_CaloIdL_HT300_v1',
    'HLT_Photon70_CaloIdL_MHT30_v1',
    'HLT_Photon70_CaloIdL_MHT50_v1',
    'HLT_Photon75_CaloIdVL_IsoL_v1',
    'HLT_Photon75_CaloIdVL_v1',
    'HLT_Physics_v1',
    'HLT_PixelTracks_Multiplicity110_v1',
    'HLT_PixelTracks_Multiplicity125_v1',
    'HLT_QuadJet40_IsoPFTau40_v1',
    'HLT_QuadJet40_v1',
    'HLT_QuadJet50_BTagIP_v1',
    'HLT_QuadJet50_Jet40_v1',
    'HLT_QuadJet60_v1',
    'HLT_QuadJet70_v1',
    'HLT_R032_MR100_v1',
    'HLT_R032_v1',
    'HLT_R035_MR100_v1',
    'HLT_Random_v1',
    'HLT_RegionalCosmicTracking_v1',
    'HLT_TrackerCalibration_v1',
    'HLT_TripleEle10_CaloIdL_TrkIdVL_v1',
    'HLT_TripleMu5_v2',
    'HLT_ZeroBias_v1' ),
  Photon = cms.vstring( 'HLT_DoublePhoton33_v1',
    'HLT_DoublePhoton5_IsoVL_CEP_v1',
    'HLT_Photon125_NoSpikeFilter_v1',
    'HLT_Photon20_R9Id_Photon18_R9Id_v1',
    'HLT_Photon26_CaloIdL_IsoVL_Photon18_CaloIdL_IsoVL_v1',
    'HLT_Photon26_CaloIdL_IsoVL_Photon18_v1',
    'HLT_Photon26_IsoVL_Photon18_IsoVL_v1',
    'HLT_Photon26_IsoVL_Photon18_v1',
    'HLT_Photon26_Photon18_v1',
    'HLT_Photon30_CaloIdVL_IsoL_v1',
    'HLT_Photon30_CaloIdVL_v1',
    'HLT_Photon32_CaloIdL_Photon26_CaloIdL_v1',
    'HLT_Photon75_CaloIdVL_IsoL_v1',
    'HLT_Photon75_CaloIdVL_v1' ),
  PhotonHad = cms.vstring( 'HLT_Photon60_CaloIdL_HT200_v1',
    'HLT_Photon70_CaloIdL_HT200_v1',
    'HLT_Photon70_CaloIdL_HT300_v1',
    'HLT_Photon70_CaloIdL_MHT30_v1',
    'HLT_Photon70_CaloIdL_MHT50_v1' ),
  RPCMonitor = cms.vstring( 'AlCa_RPCMuonNoHits_v2',
    'AlCa_RPCMuonNoTriggers_v2',
    'AlCa_RPCMuonNormalisation_v2' ),
  SingleElectron = cms.vstring( 'HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1',
    'HLT_Ele45_CaloIdVT_TrkIdT_v1',
    'HLT_Ele90_NoSpikeFilter_v1' ),
  SingleMu = cms.vstring( 'HLT_IsoMu12_v1',
    'HLT_IsoMu15_v5',
    'HLT_IsoMu17_v5',
    'HLT_IsoMu24_v1',
    'HLT_IsoMu30_v1',
    'HLT_L1SingleMu10_v1',
    'HLT_L1SingleMu20_v1',
    'HLT_L2Mu10_v1',
    'HLT_L2Mu20_v1',
    'HLT_Mu12_v1',
    'HLT_Mu15_v2',
    'HLT_Mu20_v1',
    'HLT_Mu24_v1',
    'HLT_Mu30_v1',
    'HLT_Mu3_v3',
    'HLT_Mu5_v3',
    'HLT_Mu8_v1' ),
  Tau = cms.vstring( 'HLT_DoubleIsoPFTau20_Trk5_v1',
    'HLT_IsoPFTau35_Trk20_MET45_v1' ),
  TauPlusX = cms.vstring( 'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1',
    'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1',
    'HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1',
    'HLT_Ele15_CaloIdVT_TrkIdT_LooseIsoPFTau15_v1',
    'HLT_IsoMu12_LooseIsoPFTau10_v1',
    'HLT_Mu15_LooseIsoPFTau20_v1' ),
  TestEnables = cms.vstring( 'HLT_Calibration_v1',
    'HLT_HcalCalibration_v1',
    'HLT_TrackerCalibration_v1' )
)

process.source = cms.Source( "DaqSource",
    evtsPerLS = cms.untracked.uint32( None ),
    writeStatusFile = cms.untracked.bool( False ),
    processingMode = cms.untracked.string( "defaultMode" ),
    readerPluginName = cms.untracked.string( "" ),
    readerPset = cms.untracked.PSet( None )
)

process.GlobalTag = cms.ESSource( "PoolDBESSource",
    appendToDataLabel = cms.string( "" ),
    timetype = cms.string( "runnumber" ),
    authenticationMethod = cms.untracked.uint32( None ),
    siteLocalConfig = cms.untracked.bool( None ),
    messagelevel = cms.untracked.uint32( None ),
    connect = cms.string( "frontier://(proxyurl=http://localhost:3128)(serverurl=http://localhost:8000/FrontierOnProd)(serverurl=http://localhost:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_31X_GLOBALTAG" ),
    label = cms.untracked.string( "" ),
    DumpStat = cms.untracked.bool( False ),
    BlobStreamerName = cms.untracked.string( "TBufferBlobStreamingService" ),
    globaltag = cms.string( "GR_H_V15::All" ),
    DBParameters = cms.PSet(
      authenticationPath = cms.untracked.string( "." ),
      connectionRetrialTimeOut = cms.untracked.int32( 60 ),
      idleConnectionCleanupPeriod = cms.untracked.int32( 10 ),
      messageLevel = cms.untracked.int32( 0 ),
      enablePoolAutomaticCleanUp = cms.untracked.bool( False ),
      enableConnectionSharing = cms.untracked.bool( True ),
      enableReadOnlySessionOnUpdateConnection = cms.untracked.bool( False ),
      connectionTimeOut = cms.untracked.int32( 0 ),
      connectionRetrialPeriod = cms.untracked.int32( 10 )
    ),
    toGet = cms.VPSet(
    ),
    RefreshEachRun = cms.untracked.bool( True )
)
process.HepPDTESSource = cms.ESSource( "HepPDTESSource",
    pdtFileName = cms.FileInPath( "SimGeneral/HepPDTESSource/data/pythiaparticle.tbl" ),
    appendToDataLabel = cms.string( "" )
)
process.eegeom = cms.ESSource( "EmptyESSource",
    recordName = cms.string( "EcalMappingRcd" ),
    iovIsRunNotTime = cms.bool( True ),
    appendToDataLabel = cms.string( "" ),
    firstValid = cms.vuint32( 1 )
)
process.es_hardcode = cms.ESSource( "HcalHardcodeCalibrations",
    H2Mode = cms.untracked.bool( False ),
    toGet = cms.untracked.vstring( "GainWidths" ),
    appendToDataLabel = cms.string( "" )
)
process.hltESSAK5CaloL2L3 = cms.ESSource( "JetCorrectionServiceChain",
    appendToDataLabel = cms.string( "" ),
    correctors = cms.vstring( "hltESSL2RelativeCorrectionService",
       "hltESSL3AbsoluteCorrectionService" ),
    label = cms.string( "hltESSAK5CaloL2L3" )
)
process.hltESSBTagRecord = cms.ESSource( "EmptyESSource",
    recordName = cms.string( "JetTagComputerRecord" ),
    iovIsRunNotTime = cms.bool( True ),
    appendToDataLabel = cms.string( "" ),
    firstValid = cms.vuint32( 1 )
)
process.hltESSHcalSeverityLevel = cms.ESSource( "EmptyESSource",
    recordName = cms.string( "HcalSeverityLevelComputerRcd" ),
    iovIsRunNotTime = cms.bool( True ),
    appendToDataLabel = cms.string( "" ),
    firstValid = cms.vuint32( 1 )
)
process.hltESSL2RelativeCorrectionService = cms.ESSource( "LXXXCorrectionService",
    appendToDataLabel = cms.string( "" ),
    level = cms.string( "L2Relative" ),
    algorithm = cms.string( "AK5Calo" ),
    section = cms.string( "" ),
    era = cms.string( "" ),
    useCondDB = cms.untracked.bool( True )
)
process.hltESSL3AbsoluteCorrectionService = cms.ESSource( "LXXXCorrectionService",
    appendToDataLabel = cms.string( "" ),
    level = cms.string( "L3Absolute" ),
    algorithm = cms.string( "AK5Calo" ),
    section = cms.string( "" ),
    era = cms.string( "" ),
    useCondDB = cms.untracked.bool( True )
)
process.magfield = cms.ESSource( "XMLIdealGeometryESSource",
    rootNodeName = cms.string( "cmsMagneticField:MAGF" ),
    userControlledNamespace = cms.untracked.bool( False ),
    appendToDataLabel = cms.string( "" ),
    geomXMLFiles = cms.vstring( "Geometry/CMSCommonData/data/normal/cmsextent.xml",
       "Geometry/CMSCommonData/data/cms.xml",
       "Geometry/CMSCommonData/data/cmsMagneticField.xml",
       "MagneticField/GeomBuilder/data/MagneticFieldVolumes_1103l.xml",
       "MagneticField/GeomBuilder/data/MagneticFieldParameters_07_2pi.xml" )
)

process.hltESPSmartPropagatorAnyOpposite = cms.ESProducer( "SmartPropagatorESProducer",
    ComponentName = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
    PropagationDirection = cms.string( "oppositeToMomentum" ),
    Epsilon = cms.double( 5.0 ),
    TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
    MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPSmartPropagatorOpposite = cms.ESProducer( "SmartPropagatorESProducer",
    ComponentName = cms.string( "hltESPSmartPropagatorOpposite" ),
    PropagationDirection = cms.string( "oppositeToMomentum" ),
    Epsilon = cms.double( 5.0 ),
    TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
    MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPSoftLeptonByDistance = cms.ESProducer( "LeptonTaggerByDistanceESProducer",
    appendToDataLabel = cms.string( "" ),
    distance = cms.double( 0.5 )
)
process.hltESPSoftLeptonByPt = cms.ESProducer( "LeptonTaggerByPtESProducer",
    appendToDataLabel = cms.string( "" ),
    ipSign = cms.string( "any" )
)
process.hltESPSteppingHelixPropagatorAlong = cms.ESProducer( "SteppingHelixPropagatorESProducer",
    ComponentName = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
    PropagationDirection = cms.string( "alongMomentum" ),
    useInTeslaFromMagField = cms.bool( False ),
    SetVBFPointer = cms.bool( False ),
    useMagVolumes = cms.bool( True ),
    VBFName = cms.string( "VolumeBasedMagneticField" ),
    ApplyRadX0Correction = cms.bool( True ),
    AssumeNoMaterial = cms.bool( False ),
    NoErrorPropagation = cms.bool( False ),
    debug = cms.bool( False ),
    useMatVolumes = cms.bool( True ),
    useIsYokeFlag = cms.bool( True ),
    returnTangentPlane = cms.bool( True ),
    sendLogWarning = cms.bool( False ),
    useTuningForL2Speed = cms.bool( False ),
    useEndcapShiftsInZ = cms.bool( False ),
    endcapShiftInZPos = cms.double( 0.0 ),
    endcapShiftInZNeg = cms.double( 0.0 ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
    ComponentName = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
    PropagationDirection = cms.string( "oppositeToMomentum" ),
    useInTeslaFromMagField = cms.bool( False ),
    SetVBFPointer = cms.bool( False ),
    useMagVolumes = cms.bool( True ),
    VBFName = cms.string( "VolumeBasedMagneticField" ),
    ApplyRadX0Correction = cms.bool( True ),
    AssumeNoMaterial = cms.bool( False ),
    NoErrorPropagation = cms.bool( False ),
    debug = cms.bool( False ),
    useMatVolumes = cms.bool( True ),
    useIsYokeFlag = cms.bool( True ),
    returnTangentPlane = cms.bool( True ),
    sendLogWarning = cms.bool( False ),
    useTuningForL2Speed = cms.bool( False ),
    useEndcapShiftsInZ = cms.bool( False ),
    endcapShiftInZPos = cms.double( 0.0 ),
    endcapShiftInZNeg = cms.double( 0.0 ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPStraightLinePropagator = cms.ESProducer( "StraightLinePropagatorESProducer",
    ComponentName = cms.string( "hltESPStraightLinePropagator" ),
    PropagationDirection = cms.string( "alongMomentum" ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPTTRHBWithTrackAngle = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string( "hltESPTTRHBWithTrackAngle" ),
    StripCPE = cms.string( "StripCPEfromTrackAngle" ),
    PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
    Matcher = cms.string( "StandardMatcher" ),
    ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPTTRHBuilderPixelOnly = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    StripCPE = cms.string( "Fake" ),
    PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
    Matcher = cms.string( "StandardMatcher" ),
    ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPTrackCounting3D2nd = cms.ESProducer( "TrackCountingESProducer",
    appendToDataLabel = cms.string( "" ),
    nthTrack = cms.int32( 2 ),
    impactParameterType = cms.int32( 0 ),
    deltaR = cms.double( -1.0 ),
    maximumDecayLength = cms.double( 5.0 ),
    maximumDistanceToJetAxis = cms.double( 0.07 ),
    trackQualityClass = cms.string( "any" )
)
process.hltESPTrackerRecoGeometryESProducer = cms.ESProducer( "TrackerRecoGeometryESProducer",
    trackerGeometryLabel = cms.untracked.string( "" ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPTrajectoryBuilderL3 = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
    ComponentName = cms.string( "hltESPTrajectoryBuilderL3" ),
    updator = cms.string( "hltESPKFUpdator" ),
    propagatorAlong = cms.string( "PropagatorWithMaterial" ),
    propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
    estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
    trajectoryFilterName = cms.string( "hltESPTrajectoryFilterL3" ),
    maxCand = cms.int32( 5 ),
    lostHitPenalty = cms.double( 30.0 ),
    intermediateCleaning = cms.bool( True ),
    alwaysUseInvalidHits = cms.bool( False ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
    ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
    appendToDataLabel = cms.string( "" ),
    fractionShared = cms.double( 0.5 ),
    allowSharedFirstHit = cms.bool( False )
)
process.hltESPTrajectoryFilterL3 = cms.ESProducer( "TrajectoryFilterESProducer",
    ComponentName = cms.string( "hltESPTrajectoryFilterL3" ),
    appendToDataLabel = cms.string( "" ),
    filterPset = cms.PSet(
      minPt = cms.double( 0.9 ),
      minHitsMinPt = cms.int32( 3 ),
      ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
      maxLostHits = cms.int32( 1 ),
      maxNumberOfHits = cms.int32( 7 ),
      maxConsecLostHits = cms.int32( 1 ),
      minimumNumberOfHits = cms.int32( 5 ),
      nSigmaMinPt = cms.double( 5.0 ),
      chargeSignificance = cms.double( -1.0 )
    )
)
process.hltESPTrajectoryFitterRK = cms.ESProducer( "KFTrajectoryFitterESProducer",
    ComponentName = cms.string( "hltESPTrajectoryFitterRK" ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
    Updator = cms.string( "hltESPKFUpdator" ),
    Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
    RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
    minHits = cms.int32( 3 ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPTrajectorySmootherRK = cms.ESProducer( "KFTrajectorySmootherESProducer",
    ComponentName = cms.string( "hltESPTrajectorySmootherRK" ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
    Updator = cms.string( "hltESPKFUpdator" ),
    Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
    RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
    errorRescaling = cms.double( 100.0 ),
    minHits = cms.int32( 3 ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPbJetRegionalTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
    ComponentName = cms.string( "hltESPbJetRegionalTrajectoryBuilder" ),
    updator = cms.string( "hltESPKFUpdator" ),
    propagatorAlong = cms.string( "PropagatorWithMaterial" ),
    propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
    estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
    trajectoryFilterName = cms.string( "hltESPbJetRegionalTrajectoryFilter" ),
    maxCand = cms.int32( 1 ),
    lostHitPenalty = cms.double( 30.0 ),
    intermediateCleaning = cms.bool( True ),
    alwaysUseInvalidHits = cms.bool( False ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPbJetRegionalTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
    ComponentName = cms.string( "hltESPbJetRegionalTrajectoryFilter" ),
    appendToDataLabel = cms.string( "" ),
    filterPset = cms.PSet(
      minPt = cms.double( 1.0 ),
      minHitsMinPt = cms.int32( 3 ),
      ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
      maxLostHits = cms.int32( 1 ),
      maxNumberOfHits = cms.int32( 8 ),
      maxConsecLostHits = cms.int32( 1 ),
      minimumNumberOfHits = cms.int32( 5 ),
      nSigmaMinPt = cms.double( 5.0 ),
      chargeSignificance = cms.double( -1.0 )
    )
)
process.hoDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
    ComponentName = cms.string( "HODetIdAssociator" ),
    appendToDataLabel = cms.string( "" ),
    etaBinSize = cms.double( 0.087 ),
    nEta = cms.int32( 30 ),
    nPhi = cms.int32( 72 ),
    includeBadChambers = cms.bool( False )
)
process.muonDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
    ComponentName = cms.string( "MuonDetIdAssociator" ),
    appendToDataLabel = cms.string( "" ),
    etaBinSize = cms.double( 0.125 ),
    nEta = cms.int32( 48 ),
    nPhi = cms.int32( 48 ),
    includeBadChambers = cms.bool( False )
)
process.navigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
    ComponentName = cms.string( "SimpleNavigationSchool" ),
    appendToDataLabel = cms.string( "" )
)
process.preshowerDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
    ComponentName = cms.string( "PreshowerDetIdAssociator" ),
    appendToDataLabel = cms.string( "" ),
    etaBinSize = cms.double( 0.1 ),
    nEta = cms.int32( 60 ),
    nPhi = cms.int32( 30 ),
    includeBadChambers = cms.bool( False )
)
process.siPixelTemplateDBObjectESProducer = cms.ESProducer( "SiPixelTemplateDBObjectESProducer",
    appendToDataLabel = cms.string( "" )
)
process.sistripconn = cms.ESProducer( "SiStripConnectivity" )
process.AnyDirectionAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
    ComponentName = cms.string( "AnyDirectionAnalyticalPropagator" ),
    PropagationDirection = cms.string( "anyDirection" ),
    MaxDPhi = cms.double( 1.6 ),
    appendToDataLabel = cms.string( "" )
)
process.AutoMagneticFieldESProducer = cms.ESProducer( "AutoMagneticFieldESProducer",
    label = cms.untracked.string( "" ),
    valueOverride = cms.int32( -1 ),
    appendToDataLabel = cms.string( "" ),
    nominalCurrents = cms.untracked.vint32( -1, 0, 9558, 14416, 16819, 18268, 19262 ),
    mapLabels = cms.untracked.vstring( "090322_3_8t",
       "0t",
       "071212_2t",
       "071212_3t",
       "071212_3_5t",
       "090322_3_8t",
       "071212_4t" )
)
process.CSCGeometryESModule = cms.ESProducer( "CSCGeometryESModule",
    alignmentsLabel = cms.string( "" ),
    appendToDataLabel = cms.string( "" ),
    useRealWireGeometry = cms.bool( True ),
    useOnlyWiresInME1a = cms.bool( False ),
    useGangedStripsInME1a = cms.bool( True ),
    useCentreTIOffsets = cms.bool( False ),
    debugV = cms.untracked.bool( False ),
    useDDD = cms.bool( False ),
    applyAlignment = cms.bool( True )
)
process.CaloGeometryBuilder = cms.ESProducer( "CaloGeometryBuilder",
    appendToDataLabel = cms.string( "" ),
    SelectedCalos = cms.vstring( "HCAL",
       "ZDC",
       "EcalBarrel",
       "EcalEndcap",
       "EcalPreshower",
       "TOWER" )
)
process.CaloTopologyBuilder = cms.ESProducer( "CaloTopologyBuilder",
    appendToDataLabel = cms.string( "" )
)
process.CaloTowerConstituentsMapBuilder = cms.ESProducer( "CaloTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string( "Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz" ),
    appendToDataLabel = cms.string( "" )
)
process.CaloTowerGeometryFromDBEP = cms.ESProducer( "CaloTowerGeometryFromDBEP",
    appendToDataLabel = cms.string( "" ),
    applyAlignment = cms.bool( False )
)
process.DTGeometryESModule = cms.ESProducer( "DTGeometryESModule",
    alignmentsLabel = cms.string( "" ),
    appendToDataLabel = cms.string( "" ),
    fromDDD = cms.bool( False ),
    applyAlignment = cms.bool( True )
)
process.EcalBarrelGeometryFromDBEP = cms.ESProducer( "EcalBarrelGeometryFromDBEP",
    appendToDataLabel = cms.string( "" ),
    applyAlignment = cms.bool( True )
)
process.EcalElectronicsMappingBuilder = cms.ESProducer( "EcalElectronicsMappingBuilder",
    appendToDataLabel = cms.string( "" )
)
process.EcalEndcapGeometryFromDBEP = cms.ESProducer( "EcalEndcapGeometryFromDBEP",
    appendToDataLabel = cms.string( "" ),
    applyAlignment = cms.bool( True )
)
process.EcalLaserCorrectionService = cms.ESProducer( "EcalLaserCorrectionService",
    appendToDataLabel = cms.string( "" )
)
process.EcalPreshowerGeometryFromDBEP = cms.ESProducer( "EcalPreshowerGeometryFromDBEP",
    appendToDataLabel = cms.string( "" ),
    applyAlignment = cms.bool( True )
)
process.EcalUnpackerWorkerESProducer = cms.ESProducer( "EcalUnpackerWorkerESProducer",
    ComponentName = cms.string( "" ),
    appendToDataLabel = cms.string( "" ),
    DCCDataUnpacker = cms.PSet(
      tccUnpacking = cms.bool( False ),
      orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
      srpUnpacking = cms.bool( False ),
      syncCheck = cms.bool( False ),
      feIdCheck = cms.bool( True ),
      headerUnpacking = cms.bool( True ),
      orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
      feUnpacking = cms.bool( True ),
      forceKeepFRData = cms.bool( False ),
      memUnpacking = cms.bool( True ),
      silentMode = cms.untracked.bool( None )
    ),
    ElectronicsMapper = cms.PSet(
      numbXtalTSamples = cms.uint32( 10 ),
      numbTriggerTSamples = cms.uint32( 1 )
    ),
    UncalibRHAlgo = cms.PSet(
      Type = cms.string( "EcalUncalibRecHitWorkerWeights" )
    ),
    CalibRHAlgo = cms.PSet(
      flagsMapDBReco = cms.vint32( 0, 0, 0, 0, 4, -1, -1, -1, 4, 4, 6, 6, 6, 7, 8 ),
      Type = cms.string( "EcalRecHitWorkerSimple" ),
      killDeadChannels = cms.bool( True ),
      ChannelStatusToBeExcluded = cms.vint32( 10, 11, 12, 13, 14, 78, 142 ),
      laserCorrection = cms.bool( False )
    )
)
process.HcalGeometryFromDBEP = cms.ESProducer( "HcalGeometryFromDBEP",
    appendToDataLabel = cms.string( "" ),
    applyAlignment = cms.bool( False )
)
process.HcalTopologyIdealEP = cms.ESProducer( "HcalTopologyIdealEP",
    Exclude = cms.untracked.string( "" ),
    H2Mode = cms.untracked.bool( False ),
    appendToDataLabel = cms.string( "" )
)
process.MaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
    ComponentName = cms.string( "PropagatorWithMaterial" ),
    PropagationDirection = cms.string( "alongMomentum" ),
    Mass = cms.double( 0.105 ),
    MaxDPhi = cms.double( 1.6 ),
    useRungeKutta = cms.bool( False ),
    ptMin = cms.double( -1.0 ),
    appendToDataLabel = cms.string( "" )
)
process.MuonNumberingInitialization = cms.ESProducer( "MuonNumberingInitialization",
    appendToDataLabel = cms.string( "" )
)
process.OppositeMaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
    ComponentName = cms.string( "PropagatorWithMaterialOpposite" ),
    PropagationDirection = cms.string( "oppositeToMomentum" ),
    Mass = cms.double( 0.105 ),
    MaxDPhi = cms.double( 1.6 ),
    useRungeKutta = cms.bool( False ),
    ptMin = cms.double( -1.0 ),
    appendToDataLabel = cms.string( "" )
)
process.RPCGeometryESModule = cms.ESProducer( "RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool( True ),
    useDDD = cms.untracked.bool( False ),
    appendToDataLabel = cms.string( "" )
)
process.SiStripGainESProducer = cms.ESProducer( "SiStripGainESProducer",
    AutomaticNormalization = cms.bool( False ),
    printDebug = cms.untracked.bool( False ),
    APVGain = cms.VPSet(
      cms.PSet(
        Record = cms.string( "SiStripApvGainRcd" ),
        NormalizationFactor = cms.untracked.double( 1.0 ),
        Label = cms.untracked.string( "" )
      ),
      cms.PSet(
        Record = cms.string( "SiStripApvGain2Rcd" ),
        NormalizationFactor = cms.untracked.double( 1.0 ),
        Label = cms.untracked.string( "" )
      )
    )
)
process.SiStripQualityESProducer = cms.ESProducer( "SiStripQualityESProducer",
    appendToDataLabel = cms.string( "" ),
    PrintDebugOutput = cms.bool( False ),
    ThresholdForReducedGranularity = cms.double( 0.3 ),
    UseEmptyRunInfo = cms.bool( False ),
    ReduceGranularity = cms.bool( False ),
    ListOfRecordToMerge = cms.VPSet(
      cms.PSet(
        record = cms.string( "SiStripDetVOffRcd" ),
        tag = cms.string( "" )
      ),
      cms.PSet(
        record = cms.string( "SiStripDetCablingRcd" ),
        tag = cms.string( "" )
      ),
      cms.PSet(
        record = cms.string( "SiStripBadChannelRcd" ),
        tag = cms.string( "" )
      ),
      cms.PSet(
        record = cms.string( "SiStripBadFiberRcd" ),
        tag = cms.string( "" )
      ),
      cms.PSet(
        record = cms.string( "SiStripBadModuleRcd" ),
        tag = cms.string( "" )
      ),
      cms.PSet(
        record = cms.string( "RunInfoRcd" ),
        tag = cms.string( "" )
      )
    )
)
process.SiStripRecHitMatcherESProducer = cms.ESProducer( "SiStripRecHitMatcherESProducer",
    ComponentName = cms.string( "StandardMatcher" ),
    NSigmaInside = cms.double( 3.0 ),
    appendToDataLabel = cms.string( "" )
)
process.SlaveField0 = cms.ESProducer( "UniformMagneticFieldESProducer",
    ZFieldInTesla = cms.double( 0.0 ),
    label = cms.untracked.string( "slave_0" ),
    appendToDataLabel = cms.string( "" )
)
process.SlaveField20 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
    label = cms.untracked.string( "slave_20" ),
    version = cms.string( "OAE_1103l_071212" ),
    appendToDataLabel = cms.string( "" ),
    parameters = cms.PSet(
      b0 = cms.double( None ),
      BValue = cms.string( "2_0T" ),
      l = cms.double( None ),
      a = cms.double( None )
    )
)
process.SlaveField30 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
    label = cms.untracked.string( "slave_30" ),
    version = cms.string( "OAE_1103l_071212" ),
    appendToDataLabel = cms.string( "" ),
    parameters = cms.PSet(
      b0 = cms.double( None ),
      BValue = cms.string( "3_0T" ),
      l = cms.double( None ),
      a = cms.double( None )
    )
)
process.SlaveField35 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
    label = cms.untracked.string( "slave_35" ),
    version = cms.string( "OAE_1103l_071212" ),
    appendToDataLabel = cms.string( "" ),
    parameters = cms.PSet(
      b0 = cms.double( None ),
      BValue = cms.string( "3_5T" ),
      l = cms.double( None ),
      a = cms.double( None )
    )
)
process.SlaveField38 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
    label = cms.untracked.string( "slave_38" ),
    version = cms.string( "OAE_1103l_071212" ),
    appendToDataLabel = cms.string( "" ),
    parameters = cms.PSet(
      b0 = cms.double( None ),
      BValue = cms.string( "3_8T" ),
      l = cms.double( None ),
      a = cms.double( None )
    )
)
process.SlaveField40 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
    label = cms.untracked.string( "slave_40" ),
    version = cms.string( "OAE_1103l_071212" ),
    appendToDataLabel = cms.string( "" ),
    parameters = cms.PSet(
      b0 = cms.double( None ),
      BValue = cms.string( "4_0T" ),
      l = cms.double( None ),
      a = cms.double( None )
    )
)
process.SteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
    ComponentName = cms.string( "SteppingHelixPropagatorAny" ),
    PropagationDirection = cms.string( "anyDirection" ),
    useInTeslaFromMagField = cms.bool( False ),
    SetVBFPointer = cms.bool( False ),
    useMagVolumes = cms.bool( True ),
    VBFName = cms.string( "VolumeBasedMagneticField" ),
    ApplyRadX0Correction = cms.bool( True ),
    AssumeNoMaterial = cms.bool( False ),
    NoErrorPropagation = cms.bool( False ),
    debug = cms.bool( False ),
    useMatVolumes = cms.bool( True ),
    useIsYokeFlag = cms.bool( True ),
    returnTangentPlane = cms.bool( True ),
    sendLogWarning = cms.bool( False ),
    useTuningForL2Speed = cms.bool( False ),
    useEndcapShiftsInZ = cms.bool( False ),
    endcapShiftInZPos = cms.double( 0.0 ),
    endcapShiftInZNeg = cms.double( 0.0 ),
    appendToDataLabel = cms.string( "" )
)
process.StripCPEfromTrackAngleESProducer = cms.ESProducer( "StripCPEESProducer",
    ComponentName = cms.string( "StripCPEfromTrackAngle" ),
    appendToDataLabel = cms.string( "" ),
    TanDiffusionAngle = cms.double( 0.01 ),
    ThicknessRelativeUncertainty = cms.double( 0.02 ),
    NoiseThreshold = cms.double( 2.3 ),
    MaybeNoiseThreshold = cms.double( 3.5 ),
    UncertaintyScaling = cms.double( 1.42 ),
    MinimumUncertainty = cms.double( 0.01 )
)
process.TrackerDigiGeometryESModule = cms.ESProducer( "TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string( "" ),
    appendToDataLabel = cms.string( "" ),
    applyAlignment = cms.bool( True ),
    fromDDD = cms.bool( False )
)
process.TrackerGeometricDetESModule = cms.ESProducer( "TrackerGeometricDetESModule",
    fromDDD = cms.bool( False ),
    appendToDataLabel = cms.string( "" )
)
process.TransientTrackBuilderESProducer = cms.ESProducer( "TransientTrackBuilderESProducer",
    ComponentName = cms.string( "TransientTrackBuilder" ),
    appendToDataLabel = cms.string( "" )
)
process.VBF0 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
    label = cms.untracked.string( "0t" ),
    debugBuilder = cms.untracked.bool( False ),
    version = cms.string( "grid_1103l_071212_2t" ),
    overrideMasterSector = cms.bool( True ),
    useParametrizedTrackerField = cms.bool( True ),
    paramLabel = cms.string( "slave_0" ),
    appendToDataLabel = cms.string( "" ),
    scalingVolumes = cms.vint32(  ),
    scalingFactors = cms.vdouble(    ),
    findVolumeTolerance = cms.double( 0.0 ),
    cacheLastVolume = cms.untracked.bool( True ),
    timerOn = cms.untracked.bool( None )
)
process.VBF20 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
    label = cms.untracked.string( "071212_2t" ),
    debugBuilder = cms.untracked.bool( False ),
    version = cms.string( "grid_1103l_071212_2t" ),
    overrideMasterSector = cms.bool( True ),
    useParametrizedTrackerField = cms.bool( True ),
    paramLabel = cms.string( "slave_20" ),
    appendToDataLabel = cms.string( "" ),
    scalingVolumes = cms.vint32(  ),
    scalingFactors = cms.vdouble(    ),
    findVolumeTolerance = cms.double( 0.0 ),
    cacheLastVolume = cms.untracked.bool( True ),
    timerOn = cms.untracked.bool( None )
)
process.VBF30 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
    label = cms.untracked.string( "071212_3t" ),
    debugBuilder = cms.untracked.bool( False ),
    version = cms.string( "grid_1103l_071212_3t" ),
    overrideMasterSector = cms.bool( True ),
    useParametrizedTrackerField = cms.bool( True ),
    paramLabel = cms.string( "slave_30" ),
    appendToDataLabel = cms.string( "" ),
    scalingVolumes = cms.vint32(  ),
    scalingFactors = cms.vdouble(    ),
    findVolumeTolerance = cms.double( 0.0 ),
    cacheLastVolume = cms.untracked.bool( True ),
    timerOn = cms.untracked.bool( None )
)
process.VBF35 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
    label = cms.untracked.string( "071212_3_5t" ),
    debugBuilder = cms.untracked.bool( False ),
    version = cms.string( "grid_1103l_071212_3_5t" ),
    overrideMasterSector = cms.bool( True ),
    useParametrizedTrackerField = cms.bool( True ),
    paramLabel = cms.string( "slave_35" ),
    appendToDataLabel = cms.string( "" ),
    scalingVolumes = cms.vint32(  ),
    scalingFactors = cms.vdouble(    ),
    findVolumeTolerance = cms.double( 0.0 ),
    cacheLastVolume = cms.untracked.bool( True ),
    timerOn = cms.untracked.bool( None )
)
process.VBF38 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
    label = cms.untracked.string( "090322_3_8t" ),
    debugBuilder = cms.untracked.bool( False ),
    version = cms.string( "grid_1103l_090322_3_8t" ),
    overrideMasterSector = cms.bool( False ),
    useParametrizedTrackerField = cms.bool( True ),
    paramLabel = cms.string( "slave_38" ),
    appendToDataLabel = cms.string( "" ),
    scalingVolumes = cms.vint32( 14100, 14200, 17600, 17800, 17900, 18100, 18300, 18400, 18600, 23100, 23300, 23400, 23600, 23800, 23900, 24100, 28600, 28800, 28900, 29100, 29300, 29400, 29600, 28609, 28809, 28909, 29109, 29309, 29409, 29609, 28610, 28810, 28910, 29110, 29310, 29410, 29610, 28611, 28811, 28911, 29111, 29311, 29411, 29611 ),
    scalingFactors = cms.vdouble(  1, 1, 0.994, 1.004, 1.004, 1.005, 1.004, 1.004, 0.994, 0.965, 0.958, 0.958, 0.953, 0.958, 0.958, 0.965, 0.918, 0.924, 0.924, 0.906, 0.924, 0.924, 0.918, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991  ),
    findVolumeTolerance = cms.double( 0.0 ),
    cacheLastVolume = cms.untracked.bool( True ),
    timerOn = cms.untracked.bool( None )
)
process.VBF40 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
    label = cms.untracked.string( "071212_4t" ),
    debugBuilder = cms.untracked.bool( False ),
    version = cms.string( "grid_1103l_071212_4t" ),
    overrideMasterSector = cms.bool( True ),
    useParametrizedTrackerField = cms.bool( True ),
    paramLabel = cms.string( "slave_40" ),
    appendToDataLabel = cms.string( "" ),
    scalingVolumes = cms.vint32(  ),
    scalingFactors = cms.vdouble(    ),
    findVolumeTolerance = cms.double( 0.0 ),
    cacheLastVolume = cms.untracked.bool( True ),
    timerOn = cms.untracked.bool( None )
)
process.XMLFromDBSource = cms.ESProducer( "XMLIdealGeometryESProducer",
    rootDDName = cms.string( "cms:OCMS" ),
    label = cms.string( "Extended" ),
    appendToDataLabel = cms.string( "" )
)
process.ZdcGeometryFromDBEP = cms.ESProducer( "ZdcGeometryFromDBEP",
    appendToDataLabel = cms.string( "" ),
    applyAlignment = cms.bool( False )
)
process.caloDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
    ComponentName = cms.string( "CaloDetIdAssociator" ),
    appendToDataLabel = cms.string( "" ),
    etaBinSize = cms.double( 0.087 ),
    nEta = cms.int32( 70 ),
    nPhi = cms.int32( 72 ),
    includeBadChambers = cms.bool( False )
)
process.cosmicsNavigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
    ComponentName = cms.string( "CosmicNavigationSchool" ),
    appendToDataLabel = cms.string( "" )
)
process.ecalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
    ComponentName = cms.string( "EcalDetIdAssociator" ),
    appendToDataLabel = cms.string( "" ),
    etaBinSize = cms.double( 0.02 ),
    nEta = cms.int32( 300 ),
    nPhi = cms.int32( 360 ),
    includeBadChambers = cms.bool( False )
)
process.hcalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
    ComponentName = cms.string( "HcalDetIdAssociator" ),
    appendToDataLabel = cms.string( "" ),
    etaBinSize = cms.double( 0.087 ),
    nEta = cms.int32( 70 ),
    nPhi = cms.int32( 72 ),
    includeBadChambers = cms.bool( False )
)
process.hcalRecAlgos = cms.ESProducer( "HcalRecAlgoESProducer",
    SeverityLevels = cms.VPSet(
      cms.PSet(
        RecHitFlags = cms.vstring("  "),
        ChannelStatus = cms.vstring("  "),
        Level = cms.int32( 0 )
      ),
      cms.PSet(
        RecHitFlags = cms.vstring("  "),
        ChannelStatus = cms.vstring( "HcalCellCaloTowerProb" ),
        Level = cms.int32( 1 )
      ),
      cms.PSet(
        RecHitFlags = cms.vstring( "HSCP_R1R2",
           "HSCP_FracLeader",
           "HSCP_OuterEnergy",
           "HSCP_ExpFit",
           "ADCSaturationBit" ),
        ChannelStatus = cms.vstring("  "),
        Level = cms.int32( 5 )
      ),
      cms.PSet(
        RecHitFlags = cms.vstring( "HBHEHpdHitMultiplicity",
           "HBHEPulseShape",
           "HOBit",
           "HFDigiTime",
           "HFInTimeWindow",
           "HFS8S1Ratio",
           "ZDCBit",
           "CalibrationBit",
           "TimingErrorBit" ),
        ChannelStatus = cms.vstring("  "),
        Level = cms.int32( 8 )
      ),
      cms.PSet(
        RecHitFlags = cms.vstring( "HFLongShort" ),
        ChannelStatus = cms.vstring("  "),
        Level = cms.int32( 11 )
      ),
      cms.PSet(
        RecHitFlags = cms.vstring("  "),
        ChannelStatus = cms.vstring( "HcalCellCaloTowerMask" ),
        Level = cms.int32( 12 )
      ),
      cms.PSet(
        RecHitFlags = cms.vstring("  "),
        ChannelStatus = cms.vstring( "HcalCellHot" ),
        Level = cms.int32( 15 )
      ),
      cms.PSet(
        RecHitFlags = cms.vstring("  "),
        ChannelStatus = cms.vstring( "HcalCellOff",
           "HcalCellDead" ),
        Level = cms.int32( 20 )
      )
    ),
    RecoveredRecHitBits = cms.vstring( "TimingAddedBit",
       "TimingSubtractedBit" ),
    appendToDataLabel = cms.string( "" ),
    DropChannelStatusBits = cms.vstring( "HcalCellMask",
       "HcalCellOff",
       "HcalCellDead" )
)
process.hcal_db_producer = cms.ESProducer( "HcalDbProducer",
    file = cms.untracked.string( "" ),
    appendToDataLabel = cms.string( "" ),
    dump = cms.untracked.vstring("  ")
)
process.hltESPAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
    ComponentName = cms.string( "hltESPAnalyticalPropagator" ),
    PropagationDirection = cms.string( "alongMomentum" ),
    MaxDPhi = cms.double( 1.6 ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPChi2EstimatorForRefit = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string( "hltESPChi2EstimatorForRefit" ),
    MaxChi2 = cms.double( 100000.0 ),
    nSigma = cms.double( 3.0 ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPChi2MeasurementEstimator = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
    ComponentName = cms.string( "hltESPChi2MeasurementEstimator" ),
    MaxChi2 = cms.double( 30.0 ),
    nSigma = cms.double( 3.0 ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPCkfTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
    ComponentName = cms.string( "hltESPCkfTrajectoryBuilder" ),
    updator = cms.string( "hltESPKFUpdator" ),
    propagatorAlong = cms.string( "PropagatorWithMaterial" ),
    propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
    estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
    trajectoryFilterName = cms.string( "hltESPCkfTrajectoryFilter" ),
    maxCand = cms.int32( 5 ),
    lostHitPenalty = cms.double( 30.0 ),
    intermediateCleaning = cms.bool( True ),
    alwaysUseInvalidHits = cms.bool( True ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPCkfTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
    ComponentName = cms.string( "hltESPCkfTrajectoryFilter" ),
    appendToDataLabel = cms.string( "" ),
    filterPset = cms.PSet(
      minPt = cms.double( 0.9 ),
      minHitsMinPt = cms.int32( 3 ),
      ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
      maxLostHits = cms.int32( 1 ),
      maxNumberOfHits = cms.int32( -1 ),
      maxConsecLostHits = cms.int32( 1 ),
      minimumNumberOfHits = cms.int32( 5 ),
      nSigmaMinPt = cms.double( 5.0 ),
      chargeSignificance = cms.double( -1.0 )
    )
)
process.hltESPDummyDetLayerGeometry = cms.ESProducer( "DetLayerGeometryESProducer",
    ComponentName = cms.string( "hltESPDummyDetLayerGeometry" ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPESUnpackerWorker = cms.ESProducer( "ESUnpackerWorkerESProducer",
    ComponentName = cms.string( "hltESPESUnpackerWorker" ),
    appendToDataLabel = cms.string( "" ),
    DCCDataUnpacker = cms.PSet(
      LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" )
    ),
    RHAlgo = cms.PSet(
      ESRecoAlgo = cms.int32( 0 ),
      Type = cms.string( "ESRecHitWorker" )
    )
)
process.hltESPEcalRegionCablingESProducer = cms.ESProducer( "EcalRegionCablingESProducer",
    appendToDataLabel = cms.string( "" ),
    esMapping = cms.PSet(
      LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" )
    )
)
process.hltESPEcalTrigTowerConstituentsMapBuilder = cms.ESProducer( "EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string( "Geometry/EcalMapping/data/EndCap_TTMap.txt" ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
    ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
    PropagationDirection = cms.string( "anyDirection" ),
    useInTeslaFromMagField = cms.bool( False ),
    SetVBFPointer = cms.bool( False ),
    useMagVolumes = cms.bool( True ),
    VBFName = cms.string( "VolumeBasedMagneticField" ),
    ApplyRadX0Correction = cms.bool( True ),
    AssumeNoMaterial = cms.bool( False ),
    NoErrorPropagation = cms.bool( False ),
    debug = cms.bool( False ),
    useMatVolumes = cms.bool( True ),
    useIsYokeFlag = cms.bool( True ),
    returnTangentPlane = cms.bool( True ),
    sendLogWarning = cms.bool( False ),
    useTuningForL2Speed = cms.bool( True ),
    useEndcapShiftsInZ = cms.bool( False ),
    endcapShiftInZPos = cms.double( 0.0 ),
    endcapShiftInZNeg = cms.double( 0.0 ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
    ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
    PropagationDirection = cms.string( "oppositeToMomentum" ),
    useInTeslaFromMagField = cms.bool( False ),
    SetVBFPointer = cms.bool( False ),
    useMagVolumes = cms.bool( True ),
    VBFName = cms.string( "VolumeBasedMagneticField" ),
    ApplyRadX0Correction = cms.bool( True ),
    AssumeNoMaterial = cms.bool( False ),
    NoErrorPropagation = cms.bool( False ),
    debug = cms.bool( False ),
    useMatVolumes = cms.bool( True ),
    useIsYokeFlag = cms.bool( True ),
    returnTangentPlane = cms.bool( True ),
    sendLogWarning = cms.bool( False ),
    useTuningForL2Speed = cms.bool( True ),
    useEndcapShiftsInZ = cms.bool( False ),
    endcapShiftInZPos = cms.double( 0.0 ),
    endcapShiftInZNeg = cms.double( 0.0 ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPFittingSmootherRK = cms.ESProducer( "KFFittingSmootherESProducer",
    ComponentName = cms.string( "hltESPFittingSmootherRK" ),
    Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
    Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
    EstimateCut = cms.double( -1.0 ),
    LogPixelProbabilityCut = cms.double( -16.0 ),
    MinNumberOfHits = cms.int32( 5 ),
    RejectTracks = cms.bool( True ),
    BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
    NoInvalidHitsBeginEnd = cms.bool( False ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPGlobalTrackingGeometryESProducer = cms.ESProducer( "GlobalTrackingGeometryESProducer",
    appendToDataLabel = cms.string( "" )
)
process.hltESPHIPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
    appendToDataLabel = cms.string( "" ),
    ComponentName = cms.string( "hltESPHIPixelLayerPairs" ),
    layerList = cms.vstring( "BPix1+BPix2",
       "BPix1+BPix3",
       "BPix2+BPix3",
       "BPix1+FPix1_pos",
       "BPix1+FPix1_neg",
       "BPix1+FPix2_pos",
       "BPix1+FPix2_neg",
       "BPix2+FPix1_pos",
       "BPix2+FPix1_neg",
       "BPix2+FPix2_pos",
       "BPix2+FPix2_neg",
       "FPix1_pos+FPix2_pos",
       "FPix1_neg+FPix2_neg" ),
    BPix = cms.PSet(
      hitErrorRZ = cms.double( 0.006 ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      useErrorsFromParam = cms.bool( True )
    ),
    FPix = cms.PSet(
      hitErrorRZ = cms.double( 0.0036 ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      useErrorsFromParam = cms.bool( True )
    ),
    TEC = cms.PSet(  )
)
process.hltESPHIPixelLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
    appendToDataLabel = cms.string( "" ),
    ComponentName = cms.string( "hltESPHIPixelLayerTriplets" ),
    layerList = cms.vstring( "BPix1+BPix2+BPix3",
       "BPix1+BPix2+FPix1_pos",
       "BPix1+BPix2+FPix1_neg",
       "BPix1+FPix1_pos+FPix2_pos",
       "BPix1+FPix1_neg+FPix2_neg" ),
    BPix = cms.PSet(
      hitErrorRZ = cms.double( 0.006 ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      useErrorsFromParam = cms.bool( True )
    ),
    FPix = cms.PSet(
      hitErrorRZ = cms.double( 0.0036 ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltHISiPixelRecHits" ),
      useErrorsFromParam = cms.bool( True )
    ),
    TEC = cms.PSet(  )
)
process.hltESPHITTRHBuilderWithoutRefit = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string( "hltESPHITTRHBuilderWithoutRefit" ),
    StripCPE = cms.string( "Fake" ),
    PixelCPE = cms.string( "Fake" ),
    Matcher = cms.string( "Fake" ),
    ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPKFFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
    ComponentName = cms.string( "hltESPKFFittingSmoother" ),
    Fitter = cms.string( "hltESPKFTrajectoryFitter" ),
    Smoother = cms.string( "hltESPKFTrajectorySmoother" ),
    EstimateCut = cms.double( -1.0 ),
    LogPixelProbabilityCut = cms.double( -16.0 ),
    MinNumberOfHits = cms.int32( 5 ),
    RejectTracks = cms.bool( True ),
    BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
    NoInvalidHitsBeginEnd = cms.bool( False ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPKFFittingSmootherForL2Muon = cms.ESProducer( "KFFittingSmootherESProducer",
    ComponentName = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
    Fitter = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
    Smoother = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
    EstimateCut = cms.double( -1.0 ),
    LogPixelProbabilityCut = cms.double( -16.0 ),
    MinNumberOfHits = cms.int32( 5 ),
    RejectTracks = cms.bool( True ),
    BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
    NoInvalidHitsBeginEnd = cms.bool( False ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
    ComponentName = cms.string( "hltESPKFTrajectoryFitter" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    Updator = cms.string( "hltESPKFUpdator" ),
    Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
    RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
    minHits = cms.int32( 3 ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer( "KFTrajectoryFitterESProducer",
    ComponentName = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
    Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
    Updator = cms.string( "hltESPKFUpdator" ),
    Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
    RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
    minHits = cms.int32( 3 ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPKFTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
    ComponentName = cms.string( "hltESPKFTrajectorySmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    Updator = cms.string( "hltESPKFUpdator" ),
    Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
    RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
    errorRescaling = cms.double( 100.0 ),
    minHits = cms.int32( 3 ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer( "KFTrajectorySmootherESProducer",
    ComponentName = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
    Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
    Updator = cms.string( "hltESPKFUpdator" ),
    Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
    RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
    errorRescaling = cms.double( 100.0 ),
    minHits = cms.int32( 3 ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer( "KFTrajectorySmootherESProducer",
    ComponentName = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
    Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
    Updator = cms.string( "hltESPKFUpdator" ),
    Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
    RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
    errorRescaling = cms.double( 10.0 ),
    minHits = cms.int32( 3 ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPKFUpdator = cms.ESProducer( "KFUpdatorESProducer",
    ComponentName = cms.string( "hltESPKFUpdator" ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPL3MuKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
    ComponentName = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
    Propagator = cms.string( "hltESPSmartPropagatorAny" ),
    Updator = cms.string( "hltESPKFUpdator" ),
    Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
    RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" ),
    minHits = cms.int32( 3 ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
    ComponentName = cms.string( "hltESPMeasurementTracker" ),
    PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
    StripCPE = cms.string( "StripCPEfromTrackAngle" ),
    HitMatcher = cms.string( "StandardMatcher" ),
    Regional = cms.bool( True ),
    OnDemand = cms.bool( True ),
    UsePixelModuleQualityDB = cms.bool( True ),
    DebugPixelModuleQualityDB = cms.untracked.bool( False ),
    UsePixelROCQualityDB = cms.bool( True ),
    DebugPixelROCQualityDB = cms.untracked.bool( False ),
    UseStripModuleQualityDB = cms.bool( True ),
    DebugStripModuleQualityDB = cms.untracked.bool( False ),
    UseStripAPVFiberQualityDB = cms.bool( True ),
    DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
    MaskBadAPVFibers = cms.bool( True ),
    UseStripStripQualityDB = cms.bool( True ),
    DebugStripStripQualityDB = cms.untracked.bool( False ),
    SiStripQualityLabel = cms.string( "" ),
    switchOffPixelsIfEmpty = cms.bool( True ),
    pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
    stripClusterProducer = cms.string( "hltSiStripClusters" ),
    stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
    appendToDataLabel = cms.string( "" ),
    inactivePixelDetectorLabels = cms.VInputTag(  ),
    inactiveStripDetectorLabels = cms.VInputTag(  ),
    badStripCuts = cms.PSet(
      TID = cms.PSet(
        maxConsecutiveBad = cms.uint32( 9999 ),
        maxBad = cms.uint32( 9999 )
      ),
      TOB = cms.PSet(
        maxConsecutiveBad = cms.uint32( 9999 ),
        maxBad = cms.uint32( 9999 )
      ),
      TEC = cms.PSet(
        maxConsecutiveBad = cms.uint32( 9999 ),
        maxBad = cms.uint32( 9999 )
      ),
      TIB = cms.PSet(
        maxConsecutiveBad = cms.uint32( 9999 ),
        maxBad = cms.uint32( 9999 )
      )
    )
)
process.hltESPMixedLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
    appendToDataLabel = cms.string( "" ),
    ComponentName = cms.string( "hltESPMixedLayerPairs" ),
    layerList = cms.vstring( "BPix1+BPix2",
       "BPix1+BPix3",
       "BPix2+BPix3",
       "BPix1+FPix1_pos",
       "BPix1+FPix1_neg",
       "BPix1+FPix2_pos",
       "BPix1+FPix2_neg",
       "BPix2+FPix1_pos",
       "BPix2+FPix1_neg",
       "BPix2+FPix2_pos",
       "BPix2+FPix2_neg",
       "FPix1_pos+FPix2_pos",
       "FPix1_neg+FPix2_neg",
       "FPix2_pos+TEC1_pos",
       "FPix2_pos+TEC2_pos",
       "TEC1_pos+TEC2_pos",
       "TEC2_pos+TEC3_pos",
       "FPix2_neg+TEC1_neg",
       "FPix2_neg+TEC2_neg",
       "TEC1_neg+TEC2_neg",
       "TEC2_neg+TEC3_neg" ),
    BPix = cms.PSet(
      hitErrorRZ = cms.double( 0.006 ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      useErrorsFromParam = cms.bool( True )
    ),
    FPix = cms.PSet(
      hitErrorRZ = cms.double( 0.0036 ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      useErrorsFromParam = cms.bool( True )
    ),
    TEC = cms.PSet(
      useRingSlector = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      minRing = cms.int32( 1 ),
      maxRing = cms.int32( 1 )
    )
)
process.hltESPMuTrackJpsiTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
    ComponentName = cms.string( "hltESPMuTrackJpsiTrajectoryBuilder" ),
    updator = cms.string( "hltESPKFUpdator" ),
    propagatorAlong = cms.string( "PropagatorWithMaterial" ),
    propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
    estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
    trajectoryFilterName = cms.string( "hltESPMuTrackJpsiTrajectoryFilter" ),
    maxCand = cms.int32( 1 ),
    lostHitPenalty = cms.double( 30.0 ),
    intermediateCleaning = cms.bool( True ),
    alwaysUseInvalidHits = cms.bool( False ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPMuTrackJpsiTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
    ComponentName = cms.string( "hltESPMuTrackJpsiTrajectoryFilter" ),
    appendToDataLabel = cms.string( "" ),
    filterPset = cms.PSet(
      minPt = cms.double( 1.0 ),
      minHitsMinPt = cms.int32( 3 ),
      ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
      maxLostHits = cms.int32( 1 ),
      maxNumberOfHits = cms.int32( 8 ),
      maxConsecLostHits = cms.int32( 1 ),
      minimumNumberOfHits = cms.int32( 5 ),
      nSigmaMinPt = cms.double( 5.0 ),
      chargeSignificance = cms.double( -1.0 )
    )
)
process.hltESPMuonCkfTrajectoryBuilder = cms.ESProducer( "MuonCkfTrajectoryBuilderESProducer",
    ComponentName = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
    updator = cms.string( "hltESPKFUpdator" ),
    propagatorAlong = cms.string( "PropagatorWithMaterial" ),
    propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
    propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
    estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
    trajectoryFilterName = cms.string( "hltESPMuonCkfTrajectoryFilter" ),
    useSeedLayer = cms.bool( False ),
    rescaleErrorIfFail = cms.double( 1.0 ),
    deltaEta = cms.double( 0.1 ),
    deltaPhi = cms.double( 0.1 ),
    appendToDataLabel = cms.string( "" ),
    maxCand = cms.int32( 5 ),
    lostHitPenalty = cms.double( 30.0 ),
    intermediateCleaning = cms.bool( False ),
    alwaysUseInvalidHits = cms.bool( True )
)
process.hltESPMuonCkfTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
    ComponentName = cms.string( "hltESPMuonCkfTrajectoryFilter" ),
    appendToDataLabel = cms.string( "" ),
    filterPset = cms.PSet(
      minPt = cms.double( 0.9 ),
      minHitsMinPt = cms.int32( 3 ),
      ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
      maxLostHits = cms.int32( 1 ),
      maxNumberOfHits = cms.int32( -1 ),
      maxConsecLostHits = cms.int32( 1 ),
      chargeSignificance = cms.double( -1.0 ),
      nSigmaMinPt = cms.double( 5.0 ),
      minimumNumberOfHits = cms.int32( 5 )
    )
)
process.hltESPMuonDetLayerGeometryESProducer = cms.ESProducer( "MuonDetLayerGeometryESProducer",
    appendToDataLabel = cms.string( "" )
)
process.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer( "MuonTransientTrackingRecHitBuilderESProducer",
    ComponentName = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPPixelCPEGeneric = cms.ESProducer( "PixelCPEGenericESProducer",
    ComponentName = cms.string( "hltESPPixelCPEGeneric" ),
    eff_charge_cut_lowX = cms.double( 0.0 ),
    eff_charge_cut_lowY = cms.double( 0.0 ),
    eff_charge_cut_highX = cms.double( 1.0 ),
    eff_charge_cut_highY = cms.double( 1.0 ),
    size_cutX = cms.double( 3.0 ),
    size_cutY = cms.double( 3.0 ),
    EdgeClusterErrorX = cms.double( 50.0 ),
    EdgeClusterErrorY = cms.double( 85.0 ),
    inflate_errors = cms.bool( False ),
    inflate_all_errors_no_trk_angle = cms.bool( False ),
    UseErrorsFromTemplates = cms.bool( True ),
    TruncatePixelCharge = cms.bool( True ),
    IrradiationBiasCorrection = cms.bool( False ),
    DoCosmics = cms.bool( False ),
    LoadTemplatesFromDB = cms.bool( True ),
    appendToDataLabel = cms.string( "" ),
    TanLorentzAnglePerTesla = cms.double( 0.106 ),
    PixelErrorParametrization = cms.string( "NOTcmsim" ),
    Alpha2Order = cms.bool( True ),
    ClusterProbComputationFlag = cms.int32( 0 )
)
process.hltESPPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
    appendToDataLabel = cms.string( "" ),
    ComponentName = cms.string( "hltESPPixelLayerPairs" ),
    layerList = cms.vstring( "BPix1+BPix2",
       "BPix1+BPix3",
       "BPix2+BPix3",
       "BPix1+FPix1_pos",
       "BPix1+FPix1_neg",
       "BPix1+FPix2_pos",
       "BPix1+FPix2_neg",
       "BPix2+FPix1_pos",
       "BPix2+FPix1_neg",
       "BPix2+FPix2_pos",
       "BPix2+FPix2_neg",
       "FPix1_pos+FPix2_pos",
       "FPix1_neg+FPix2_neg" ),
    BPix = cms.PSet(
      hitErrorRZ = cms.double( 0.006 ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      useErrorsFromParam = cms.bool( True )
    ),
    FPix = cms.PSet(
      hitErrorRZ = cms.double( 0.0036 ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      useErrorsFromParam = cms.bool( True )
    ),
    TEC = cms.PSet(  )
)
process.hltESPPixelLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
    appendToDataLabel = cms.string( "" ),
    ComponentName = cms.string( "hltESPPixelLayerTriplets" ),
    layerList = cms.vstring( "BPix1+BPix2+BPix3",
       "BPix1+BPix2+FPix1_pos",
       "BPix1+BPix2+FPix1_neg",
       "BPix1+FPix1_pos+FPix2_pos",
       "BPix1+FPix1_neg+FPix2_neg" ),
    BPix = cms.PSet(
      hitErrorRZ = cms.double( 0.006 ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      useErrorsFromParam = cms.bool( True )
    ),
    FPix = cms.PSet(
      hitErrorRZ = cms.double( 0.0036 ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      useErrorsFromParam = cms.bool( True )
    ),
    TEC = cms.PSet(  )
)
process.hltESPPixelLayerTripletsHITHB = cms.ESProducer( "SeedingLayersESProducer",
    appendToDataLabel = cms.string( "" ),
    ComponentName = cms.string( "hltESPPixelLayerTripletsHITHB" ),
    layerList = cms.vstring( "BPix1+BPix2+BPix3" ),
    BPix = cms.PSet(
      hitErrorRZ = cms.double( 0.006 ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      useErrorsFromParam = cms.bool( True )
    ),
    FPix = cms.PSet(
      hitErrorRZ = cms.double( 0.0036 ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      useErrorsFromParam = cms.bool( True )
    ),
    TEC = cms.PSet(  )
)
process.hltESPPixelLayerTripletsHITHE = cms.ESProducer( "SeedingLayersESProducer",
    appendToDataLabel = cms.string( "" ),
    ComponentName = cms.string( "hltESPPixelLayerTripletsHITHE" ),
    layerList = cms.vstring( "BPix1+BPix2+FPix1_pos",
       "BPix1+BPix2+FPix1_neg",
       "BPix1+FPix1_pos+FPix2_pos",
       "BPix1+FPix1_neg+FPix2_neg" ),
    BPix = cms.PSet(
      hitErrorRZ = cms.double( 0.006 ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      useErrorsFromParam = cms.bool( True )
    ),
    FPix = cms.PSet(
      hitErrorRZ = cms.double( 0.0036 ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      useErrorsFromParam = cms.bool( True )
    ),
    TEC = cms.PSet(  )
)
process.hltESPRungeKuttaTrackerPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
    ComponentName = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
    PropagationDirection = cms.string( "alongMomentum" ),
    Mass = cms.double( 0.105 ),
    MaxDPhi = cms.double( 1.6 ),
    useRungeKutta = cms.bool( True ),
    ptMin = cms.double( -1.0 ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPSiStripRegionConnectivity = cms.ESProducer( "SiStripRegionConnectivity",
    EtaDivisions = cms.untracked.uint32( 20 ),
    PhiDivisions = cms.untracked.uint32( 20 ),
    EtaMax = cms.untracked.double( 2.5 )
)
process.hltESPSmartPropagator = cms.ESProducer( "SmartPropagatorESProducer",
    ComponentName = cms.string( "hltESPSmartPropagator" ),
    PropagationDirection = cms.string( "alongMomentum" ),
    Epsilon = cms.double( 5.0 ),
    TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
    MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
    appendToDataLabel = cms.string( "" )
)
process.hltESPSmartPropagatorAny = cms.ESProducer( "SmartPropagatorESProducer",
    ComponentName = cms.string( "hltESPSmartPropagatorAny" ),
    PropagationDirection = cms.string( "alongMomentum" ),
    Epsilon = cms.double( 5.0 ),
    TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
    MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
    appendToDataLabel = cms.string( "" )
)

process.DQM = cms.Service( "DQM" )
process.DQMStore = cms.Service( "DQMStore",
    verbose = cms.untracked.int32( 0 ),
    verboseQT = cms.untracked.int32( 0 ),
    collateHistograms = cms.untracked.bool( False ),
    referenceFileName = cms.untracked.string( "" )
)
process.DTDataIntegrityTask = cms.Service( "DTDataIntegrityTask",
    getSCInfo = cms.untracked.bool( True ),
    fedIntegrityFolder = cms.untracked.string( "DT/FEDIntegrity_EvF" ),
    processingMode = cms.untracked.string( "HLT" )
)
process.FUShmDQMOutputService = cms.Service( "FUShmDQMOutputService",
    initialMessageBufferSize = cms.untracked.int32( 1000000 ),
    lumiSectionsPerUpdate = cms.double( 1.0 ),
    useCompression = cms.bool( True ),
    compressionLevel = cms.int32( 1 ),
    lumiSectionInterval = cms.untracked.int32( 0 )
)
process.MessageLogger = cms.Service( "MessageLogger",
    destinations = cms.untracked.vstring( "warnings",
       "errors",
       "infos",
       "debugs",
       "cout",
       "cerr" ),
    categories = cms.untracked.vstring( "FwkJob",
       "FwkReport",
       "FwkSummary",
       "Root_NoDictionary" ),
    statistics = cms.untracked.vstring( "cerr" ),
    cerr = cms.untracked.PSet(
      INFO = cms.PSet(
        limit = cms.untracked.int32( 0 )
      ),
      noTimeStamps = cms.untracked.bool( False ),
      FwkReport = cms.PSet(
        reportEvery = cms.untracked.int32( 1 ),
        limit = cms.untracked.int32( 0 )
      ),
      default = cms.PSet(
        limit = cms.untracked.int32( 10000000 )
      ),
      Root_NoDictionary = cms.PSet(
        limit = cms.untracked.int32( 0 )
      ),
      FwkJob = cms.PSet(
        limit = cms.untracked.int32( 0 )
      ),
      FwkSummary = cms.PSet(
        reportEvery = cms.untracked.int32( 1 ),
        limit = cms.untracked.int32( 10000000 )
      ),
      threshold = cms.untracked.string( "INFO" )
    ),
    cout = cms.untracked.PSet(
      threshold = cms.untracked.string( "ERROR" )
    ),
    errors = cms.untracked.PSet(
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True )
    ),
    warnings = cms.untracked.PSet(
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True )
    ),
    infos = cms.untracked.PSet(
      threshold = cms.untracked.string( "INFO" ),
      Root_NoDictionary = cms.PSet(
        limit = cms.untracked.int32( 0 )
      ),
      placeholder = cms.untracked.bool( True )
    ),
    debugs = cms.untracked.PSet(
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True )
    ),
    fwkJobReports = cms.untracked.vstring( "FrameworkJobReport" ),
    FrameworkJobReport = cms.untracked.PSet(
      default = cms.PSet(
        limit = cms.untracked.int32( 0 )
      ),
      FwkJob = cms.PSet(
        limit = cms.untracked.int32( 10000000 )
      )
    ),
    debugModules = cms.untracked.vstring("  "),
    suppressDebug = cms.untracked.vstring("  "),
    suppressInfo = cms.untracked.vstring("  "),
    suppressWarning = cms.untracked.vstring( "hltOnlineBeamSpot",
       "hltPixelTracksForMinBias",
       "hltPixelTracksForHighMult",
       "hltHITPixelTracksHE",
       "hltHITPixelTracksHB",
       "hltSiPixelClusters",
       "hltPixelTracks" ),
    threshold = cms.untracked.string( "INFO" )
)
process.MicroStateService = cms.Service( "MicroStateService" )
process.ModuleWebRegistry = cms.Service( "ModuleWebRegistry" )
process.PrescaleService = cms.Service( "PrescaleService",
    lvl1DefaultLabel = cms.untracked.string( "7E31" ),
    lvl1Labels = cms.vstring( "2E32",
       "14e31",
       "7E31",
       "3E31",
       "1E31",
       "1E30" ),
    prescaleTable = cms.VPSet(
      cms.PSet(
        pathName = cms.string( "HLT_L1SingleJet36_v1" ),
        prescales = cms.vuint32( 1000, 2000, 3000, 1200, 500, 50 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Jet30_v1" ),
        prescales = cms.vuint32( 10, 10, 10, 10, 10, 10 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Jet60_v1" ),
        prescales = cms.vuint32( 150, 100, 500, 250, 100, 10 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Jet80_v1" ),
        prescales = cms.vuint32( 300, 200, 100, 50, 20, 2 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Jet110_v1" ),
        prescales = cms.vuint32( 50, 50, 25, 15, 5, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Jet150_v1" ),
        prescales = cms.vuint32( 10, 10, 5, 2, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Jet190_v1" ),
        prescales = cms.vuint32( 4, 2, 1, 1, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_DiJetAve15U_v4" ),
        prescales = cms.vuint32( 5, 5, 5, 5, 5, 5 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_DiJetAve30U_v4" ),
        prescales = cms.vuint32( 75, 75, 350, 150, 50, 5 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_DiJetAve50U_v4" ),
        prescales = cms.vuint32( 150, 100, 50, 20, 10, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_DiJetAve70U_v4" ),
        prescales = cms.vuint32( 25, 25, 15, 10, 3, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_DiJetAve100U_v4" ),
        prescales = cms.vuint32( 10, 10, 5, 2, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_DiJetAve140U_v4" ),
        prescales = cms.vuint32( 2, 1, 1, 1, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_DiJet60_MET45_v1" ),
        prescales = cms.vuint32( 20, 10, 5, 2, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_QuadJet40_v1" ),
        prescales = cms.vuint32( 10, 10, 5, 2, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_ExclDiJet60_HFOR_v1" ),
        prescales = cms.vuint32( 1, 1, 5, 2, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_JetE30_NoBPTX_v1" ),
        prescales = cms.vuint32( 60, 40, 20, 8, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_JetE30_NoBPTX_NoHalo_v2" ),
        prescales = cms.vuint32( 60, 40, 20, 8, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_HT160_v2" ),
        prescales = cms.vuint32( 200, 100, 50, 20, 7, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_HT240_v2" ),
        prescales = cms.vuint32( 100, 20, 1, 1, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_HT260_v2" ),
        prescales = cms.vuint32( 25, 1, 1, 1, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_HT300_v2" ),
        prescales = cms.vuint32( 10, 1, 1, 1, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_MR100_v1" ),
        prescales = cms.vuint32( 250, 250, 100, 50, 10, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_R032_v1" ),
        prescales = cms.vuint32( 10, 1, 1, 1, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_L1SingleMuOpen_v1" ),
        prescales = cms.vuint32( 200, 200, 200, 200, 200, 20 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_L1SingleMuOpen_DT_v1" ),
        prescales = cms.vuint32( 20, 20, 20, 20, 20, 2 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_L1SingleMu10_v1" ),
        prescales = cms.vuint32( 900, 600, 300, 120, 40, 4 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_L1SingleMu20_v1" ),
        prescales = cms.vuint32( 500, 300, 150, 75, 25, 2 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_L1DoubleMu0_v1" ),
        prescales = cms.vuint32( 700, 700, 700, 300, 100, 10 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_L2MuOpen_NoVertex_v1" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_L2Mu10_v1" ),
        prescales = cms.vuint32( 200, 100, 50, 25, 10, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_L2Mu20_v1" ),
        prescales = cms.vuint32( 75, 50, 25, 10, 3, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_L2DoubleMu0_v2" ),
        prescales = cms.vuint32( 250, 125, 60, 30, 10, 2 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Mu3_v3" ),
        prescales = cms.vuint32( 100, 100, 100, 40, 15, 2 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Mu5_v3" ),
        prescales = cms.vuint32( 140, 140, 70, 30, 10, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Mu8_v1" ),
        prescales = cms.vuint32( 28, 28, 70, 30, 10, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Mu12_v1" ),
        prescales = cms.vuint32( 50, 25, 10, 5, 2, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Mu15_v2" ),
        prescales = cms.vuint32( 20, 1, 1, 1, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_DoubleMu3_v3" ),
        prescales = cms.vuint32( 25, 20, 10, 5, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Mu5_L2Mu2_v1" ),
        prescales = cms.vuint32( 30, 20, 10, 4, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Mu5_L2Mu2_Jpsi_v1" ),
        prescales = cms.vuint32( 5, 2, 1, 1, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Mu3_Track3_Jpsi_v4" ),
        prescales = cms.vuint32( 5, 5, 2, 1, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_L1SingleEG5_v1" ),
        prescales = cms.vuint32( 100, 100, 150, 150, 150, 15 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Photon30_CaloIdVL_v1" ),
        prescales = cms.vuint32( 100, 50, 25, 15, 5, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Photon30_CaloIdVL_IsoL_v1" ),
        prescales = cms.vuint32( 50, 25, 25, 5, 5, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Photon125_NoSpikeFilter_v1" ),
        prescales = cms.vuint32( 100, 50, 25, 10, 3, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Ele8_v1" ),
        prescales = cms.vuint32( 20, 20, 20, 20, 20, 2 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Ele8_CaloIdL_CaloIsoVL_v1" ),
        prescales = cms.vuint32( 50, 50, 50, 50, 50, 5 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Ele8_CaloIdL_TrkIdVL_v1" ),
        prescales = cms.vuint32( 30, 30, 30, 30, 30, 3 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1" ),
        prescales = cms.vuint32( 20, 15, 10, 5, 2, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Ele17_CaloIdL_CaloIsoVL_v1" ),
        prescales = cms.vuint32( 150, 100, 50, 20, 7, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Photon20_R9Id_Photon18_R9Id_v1" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Photon26_Photon18_v1" ),
        prescales = cms.vuint32( 10, 10, 5, 2, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_BTagMu_DiJet20_Mu5_v1" ),
        prescales = cms.vuint32( 100, 100, 50, 20, 7, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Mu8_Jet40_v2" ),
        prescales = cms.vuint32( 24, 24, 8, 3, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v1" ),
        prescales = cms.vuint32( 3, 3, 3, 3, 3, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Ele15_CaloIdVT_TrkIdT_LooseIsoPFTau15_v1" ),
        prescales = cms.vuint32( 5, 4, 2, 1, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Ele25_CaloIdVT_TrkIdT_CentralJet30_v1" ),
        prescales = cms.vuint32( 15, 10, 5, 2, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Ele25_CaloIdVT_TrkIdT_CentralDiJet30_v1" ),
        prescales = cms.vuint32( 10, 5, 3, 1, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Photon20_EBOnly_NoSpikeFilter_v1" ),
        prescales = cms.vuint32( 2000, 1400, 700, 300, 100, 10 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Photon20_NoSpikeFilter_v1" ),
        prescales = cms.vuint32( 2000, 1400, 700, 300, 100, 10 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Spike20_v1" ),
        prescales = cms.vuint32( 2000, 1400, 700, 300, 100, 10 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_BeamGas_HF_v1" ),
        prescales = cms.vuint32( 10, 10, 10, 1, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_L1_BeamHalo_v1" ),
        prescales = cms.vuint32( 1000, 1000, 1000, 1000, 1000, 1000 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_L1Tech_BSC_halo_v1" ),
        prescales = cms.vuint32( 300, 200, 100, 40, 15, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_L1_Interbunch_BSC_v1" ),
        prescales = cms.vuint32( 30, 20, 10, 4, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_GlobalRunHPDNoise_v2" ),
        prescales = cms.vuint32( 3000, 2000, 1000, 400, 150, 15 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Physics_v1" ),
        prescales = cms.vuint32( 4000, 4000, 4000, 4000, 1500, 150 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Physics_NanoDST_v1" ),
        prescales = cms.vuint32( 10, 10, 10, 10, 10, 10 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_Random_v1" ),
        prescales = cms.vuint32( 6000, 6000, 6000, 6000, 6000, 6000 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_L1MuOpen_AntiBPTX_v2" ),
        prescales = cms.vuint32( 2, 4, 5, 12, 50, 50 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_RegionalCosmicTracking_v1" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(
        pathName = cms.string( "HLT_L3MuonsCosmicTracking_v1" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(
        pathName = cms.string( "AlCa_EcalPi0_v3" ),
        prescales = cms.vuint32( 8, 6, 4, 2, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "AlCa_EcalEta_v2" ),
        prescales = cms.vuint32( 6, 5, 3, 2, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "AlCa_EcalPhiSym_v2" ),
        prescales = cms.vuint32( 2, 2, 2, 2, 2, 2 )
      ),
      cms.PSet(
        pathName = cms.string( "AlCa_RPCMuonNoTriggers_v2" ),
        prescales = cms.vuint32( 10, 6, 3, 1, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "AlCa_RPCMuonNoHits_v2" ),
        prescales = cms.vuint32( 10, 6, 3, 1, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "AlCa_RPCMuonNormalisation_v2" ),
        prescales = cms.vuint32( 30, 2, 1, 1, 1, 1 )
      ),
      cms.PSet(
        pathName = cms.string( "DQM_FEDIntegrity_v2" ),
        prescales = cms.vuint32( 10, 10, 10, 10, 10, 10 )
      ),
      cms.PSet(
        pathName = cms.string( "HLTDQMResultsOutput" ),
        prescales = cms.vuint32( 10, 10, 10, 10, 10, 10 )
      ),
      cms.PSet(
        pathName = cms.string( "HLTMONOutput" ),
        prescales = cms.vuint32( 100, 100, 100, 100, 100, 100 )
      )
    )
)
process.UpdaterService = cms.Service( "UpdaterService" )

process.hltActivityPhotonClusterShape = cms.EDProducer( "EgammaHLTClusterShapeProducer",
    recoEcalCandidateProducer = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    ecalRechitEB = cms.InputTag( 'hltEcalRecHitAll', 'EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRecHitAll', 'EcalRecHitsEE' ),
    isIeta = cms.bool( True )
)
process.hltActivityPhotonEcalIsol = cms.EDProducer( "EgammaHLTEcalRecIsolationProducer",
    recoEcalCandidateProducer = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    ecalBarrelRecHitProducer = cms.InputTag( 'hltEcalRecHitAll' ),
    ecalBarrelRecHitCollection = cms.InputTag( 'EcalRecHitsEB' ),
    ecalEndcapRecHitProducer = cms.InputTag( 'hltEcalRecHitAll' ),
    ecalEndcapRecHitCollection = cms.InputTag( 'EcalRecHitsEE' ),
    etMinBarrel = cms.double( -9999.0 ),
    eMinBarrel = cms.double( 0.08 ),
    etMinEndcap = cms.double( 0.1 ),
    eMinEndcap = cms.double( -9999.0 ),
    intRadiusBarrel = cms.double( 3.0 ),
    intRadiusEndcap = cms.double( 3.0 ),
    extRadius = cms.double( 0.3 ),
    jurassicWidth = cms.double( 3.0 ),
    useIsolEt = cms.bool( True ),
    tryBoth = cms.bool( True ),
    subtract = cms.bool( False ),
    useNumCrystals = cms.bool( True )
)
process.hltActivityPhotonHcalForHE = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    hbheRecHitProducer = cms.InputTag( 'hltHbhereco' ),
    eMinHB = cms.double( 0.7 ),
    eMinHE = cms.double( 0.8 ),
    etMinHB = cms.double( -1.0 ),
    etMinHE = cms.double( -1.0 ),
    innerCone = cms.double( 0.0 ),
    outerCone = cms.double( 0.14 ),
    depth = cms.int32( -1 ),
    doEtSum = cms.bool( False )
)
process.hltActivityPhotonHcalIsol = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    hbheRecHitProducer = cms.InputTag( 'hltHbhereco' ),
    eMinHB = cms.double( 0.7 ),
    eMinHE = cms.double( 0.8 ),
    etMinHB = cms.double( -1.0 ),
    etMinHE = cms.double( -1.0 ),
    innerCone = cms.double( 0.16 ),
    outerCone = cms.double( 0.29 ),
    depth = cms.int32( -1 ),
    doEtSum = cms.bool( True )
)
process.hltActivityPhotonHollowTrackIsol = cms.EDProducer( "EgammaHLTPhotonTrackIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    trackProducer = cms.InputTag( 'hltEcalActivityEgammaRegionalCTFFinalFitWithMaterial' ),
    countTracks = cms.bool( False ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoConeSize = cms.double( 0.29 ),
    egTrkIsoZSpan = cms.double( 999999.0 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSize = cms.double( 0.06 ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    egTrkIsoStripEndcap = cms.double( 0.03 )
)
process.hltActivityR9ID = cms.EDProducer( "EgammaHLTR9IDProducer",
    recoEcalCandidateProducer = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    ecalRechitEB = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEE' )
)
process.hltActivityStartUpElectronPixelSeeds = cms.EDProducer( "ElectronSeedProducer",
    barrelSuperClusters = cms.InputTag( 'hltCorrectedHybridSuperClustersActivity' ),
    endcapSuperClusters = cms.InputTag( 'hltCorrectedMulti5x5SuperClustersWithPreshowerActivity' ),
    SeedConfiguration = cms.PSet(
      searchInTIDTEC = cms.bool( True ),
      HighPtThreshold = cms.double( 35.0 ),
      r2MinF = cms.double( -0.15 ),
      OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32( 0 ),
        ComponentName = cms.string( "StandardHitPairGenerator" ),
        SeedingLayers = cms.string( "hltESPMixedLayerPairs" ),
        useOnDemandTracker = cms.untracked.int32( 0 )
      ),
      DeltaPhi1Low = cms.double( 0.23 ),
      DeltaPhi1High = cms.double( 0.08 ),
      ePhiMin1 = cms.double( -0.08 ),
      PhiMin2 = cms.double( -0.004 ),
      LowPtThreshold = cms.double( 3.0 ),
      hcalTowers = cms.InputTag( 'towerMaker' ),
      RegionPSet = cms.PSet(
        deltaPhiRegion = cms.double( 0.4 ),
        originHalfLength = cms.double( 15.0 ),
        useZInVertex = cms.bool( True ),
        deltaEtaRegion = cms.double( 0.1 ),
        ptMin = cms.double( 1.5 ),
        originRadius = cms.double( 0.2 ),
        VertexProducer = cms.InputTag( 'dummyVertices' )
      ),
      hOverEPtMin = cms.double( None ),
      maxHOverE = cms.double( 999999.0 ),
      maxHOverEBarrel = cms.double( None ),
      maxHOverEEndcaps = cms.double( None ),
      dynamicPhiRoad = cms.bool( False ),
      ePhiMax1 = cms.double( 0.04 ),
      maxHBarrel = cms.double( None ),
      maxHEndcaps = cms.double( None ),
      DeltaPhi2 = cms.double( 0.004 ),
      measurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      SizeWindowENeg = cms.double( 0.675 ),
      nSigmasDeltaZ1 = cms.double( 5.0 ),
      rMaxI = cms.double( 0.2 ),
      rMinI = cms.double( -0.2 ),
      preFilteredSeeds = cms.bool( True ),
      r2MaxF = cms.double( 0.15 ),
      pPhiMin1 = cms.double( -0.04 ),
      useRecoVertex = cms.bool( None ),
      initialSeeds = cms.InputTag( 'noSeedsHere' ),
      vertices = cms.InputTag( None ),
      pPhiMax1 = cms.double( 0.08 ),
      deltaZ1WithVertex = cms.double( None ),
      hbheModule = cms.string( "hbhereco" ),
      SCEtCut = cms.double( 3.0 ),
      DeltaPhi2B = cms.double( None ),
      z2MaxB = cms.double( 0.09 ),
      DeltaPhi2F = cms.double( None ),
      fromTrackerSeeds = cms.bool( True ),
      hcalRecHits = cms.InputTag( 'hltHbhereco' ),
      PhiMin2B = cms.double( None ),
      z2MinB = cms.double( -0.09 ),
      hbheInstance = cms.string( "" ),
      PhiMin2F = cms.double( None ),
      PhiMax2 = cms.double( 0.004 ),
      hOverEConeSize = cms.double( 0.0 ),
      PhiMax2B = cms.double( None ),
      PhiMax2F = cms.double( None ),
      hOverEHBMinE = cms.double( 999999.0 ),
      beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
      applyHOverECut = cms.bool( False ),
      hOverEHFMinE = cms.double( 999999.0 )
    )
)
process.hltAlCaEtaRecHitsFilter = cms.HLTFilter( "HLTEcalResonanceFilter",
    barrelHits = cms.InputTag( 'hltEcalRegionalPi0EtaRecHit', 'EcalRecHitsEB' ),
    barrelClusters = cms.InputTag( 'hltSimple3x3Clusters', 'Simple3x3ClustersBarrel' ),
    endcapHits = cms.InputTag( 'hltEcalRegionalPi0EtaRecHit', 'EcalRecHitsEE' ),
    endcapClusters = cms.InputTag( 'hltSimple3x3Clusters', 'Simple3x3ClustersEndcap' ),
    doSelBarrel = cms.bool( True ),
    doSelEndcap = cms.bool( True ),
    useRecoFlag = cms.bool( False ),
    flagLevelRecHitsToUse = cms.int32( 1 ),
    useDBStatus = cms.bool( True ),
    statusLevelRecHitsToUse = cms.int32( 1 ),
    preshRecHitProducer = cms.InputTag( 'hltESRegionalPi0EtaRecHit', 'EcalRecHitsES' ),
    storeRecHitES = cms.bool( True ),
    debugLevel = cms.int32( 0 ),
    barrelSelection = cms.PSet(
      massLowPi0Cand = cms.double( 0.084 ),
      seleIso = cms.double( 0.5 ),
      seleMinvMaxBarrel = cms.double( 0.8 ),
      selePtPair = cms.double( 4.0 ),
      seleMinvMinBarrel = cms.double( 0.3 ),
      seleS4S9Gamma = cms.double( 0.87 ),
      seleS9S25Gamma = cms.double( 0.8 ),
      selePtGamma = cms.double( 1.2 ),
      seleBeltDR = cms.double( 0.3 ),
      ptMinForIsolation = cms.double( 0.5 ),
      store5x5RecHitEB = cms.bool( True ),
      seleBeltDeta = cms.double( 0.1 ),
      removePi0CandidatesForEta = cms.bool( True ),
      barrelHitCollection = cms.string( "etaEcalRecHitsEB" ),
      massHighPi0Cand = cms.double( 0.156 )
    ),
    endcapSelection = cms.PSet(
      selePtGammaEndCap_region1 = cms.double( 1.0 ),
      selePtGammaEndCap_region3 = cms.double( 0.7 ),
      selePtGammaEndCap_region2 = cms.double( 1.0 ),
      region1_EndCap = cms.double( 2.0 ),
      seleS9S25GammaEndCap = cms.double( 0.85 ),
      selePtPairMaxEndCap_region3 = cms.double( 9999.0 ),
      seleMinvMinEndCap = cms.double( 0.2 ),
      seleS4S9GammaEndCap = cms.double( 0.9 ),
      seleMinvMaxEndCap = cms.double( 0.9 ),
      selePtPairEndCap_region1 = cms.double( 3.0 ),
      seleBeltDREndCap = cms.double( 0.3 ),
      selePtPairEndCap_region3 = cms.double( 3.0 ),
      selePtPairEndCap_region2 = cms.double( 3.0 ),
      seleIsoEndCap = cms.double( 0.5 ),
      ptMinForIsolationEndCap = cms.double( 0.5 ),
      endcapHitCollection = cms.string( "etaEcalRecHitsEE" ),
      region2_EndCap = cms.double( 2.5 ),
      seleBeltDetaEndCap = cms.double( 0.1 ),
      store5x5RecHitEE = cms.bool( True )
    ),
    preshowerSelection = cms.PSet(
      preshCalibGamma = cms.double( 0.024 ),
      preshStripEnergyCut = cms.double( 0.0 ),
      debugLevelES = cms.string( "" ),
      preshCalibPlaneY = cms.double( 0.7 ),
      preshCalibPlaneX = cms.double( 1.0 ),
      preshCalibMIP = cms.double( 9e-05 ),
      ESCollection = cms.string( "etaEcalRecHitsES" ),
      preshNclust = cms.int32( 4 ),
      preshClusterEnergyCut = cms.double( 0.0 ),
      preshSeededNstrip = cms.int32( 15 )
    )
)
process.hltAlCaPhiSymStream = cms.HLTFilter( "HLTEcalPhiSymFilter",
    barrelHitCollection = cms.InputTag( 'hltEcalRecHitAll', 'EcalRecHitsEB' ),
    endcapHitCollection = cms.InputTag( 'hltEcalRecHitAll', 'EcalRecHitsEE' ),
    phiSymBarrelHitCollection = cms.string( "phiSymEcalRecHitsEB" ),
    phiSymEndcapHitCollection = cms.string( "phiSymEcalRecHitsEE" ),
    eCut_barrel = cms.double( 0.15 ),
    eCut_endcap = cms.double( 0.75 ),
    eCut_barrel_high = cms.double( 999999.0 ),
    eCut_endcap_high = cms.double( 999999.0 ),
    statusThreshold = cms.uint32( 3 ),
    useRecoFlag = cms.bool( False )
)
process.hltAlCaPi0RecHitsFilter = cms.HLTFilter( "HLTEcalResonanceFilter",
    barrelHits = cms.InputTag( 'hltEcalRegionalPi0EtaRecHit', 'EcalRecHitsEB' ),
    barrelClusters = cms.InputTag( 'hltSimple3x3Clusters', 'Simple3x3ClustersBarrel' ),
    endcapHits = cms.InputTag( 'hltEcalRegionalPi0EtaRecHit', 'EcalRecHitsEE' ),
    endcapClusters = cms.InputTag( 'hltSimple3x3Clusters', 'Simple3x3ClustersEndcap' ),
    doSelBarrel = cms.bool( True ),
    doSelEndcap = cms.bool( True ),
    useRecoFlag = cms.bool( False ),
    flagLevelRecHitsToUse = cms.int32( 1 ),
    useDBStatus = cms.bool( True ),
    statusLevelRecHitsToUse = cms.int32( 1 ),
    preshRecHitProducer = cms.InputTag( 'hltESRegionalPi0EtaRecHit', 'EcalRecHitsES' ),
    storeRecHitES = cms.bool( True ),
    debugLevel = cms.int32( 0 ),
    barrelSelection = cms.PSet(
      massLowPi0Cand = cms.double( 0.084 ),
      seleIso = cms.double( 0.5 ),
      seleMinvMaxBarrel = cms.double( 0.23 ),
      selePtPair = cms.double( 2.6 ),
      seleMinvMinBarrel = cms.double( 0.04 ),
      seleS4S9Gamma = cms.double( 0.83 ),
      seleS9S25Gamma = cms.double( 0.0 ),
      selePtGamma = cms.double( 1.3 ),
      seleBeltDR = cms.double( 0.2 ),
      ptMinForIsolation = cms.double( 0.5 ),
      store5x5RecHitEB = cms.bool( False ),
      seleBeltDeta = cms.double( 0.05 ),
      removePi0CandidatesForEta = cms.bool( False ),
      barrelHitCollection = cms.string( "pi0EcalRecHitsEB" ),
      massHighPi0Cand = cms.double( 0.156 )
    ),
    endcapSelection = cms.PSet(
      selePtGammaEndCap_region1 = cms.double( 0.6 ),
      selePtGammaEndCap_region3 = cms.double( 0.5 ),
      selePtGammaEndCap_region2 = cms.double( 0.6 ),
      region1_EndCap = cms.double( 2.0 ),
      seleS9S25GammaEndCap = cms.double( 0.0 ),
      selePtPairMaxEndCap_region3 = cms.double( 2.5 ),
      seleMinvMinEndCap = cms.double( 0.05 ),
      seleS4S9GammaEndCap = cms.double( 0.9 ),
      seleMinvMaxEndCap = cms.double( 0.3 ),
      selePtPairEndCap_region1 = cms.double( 2.5 ),
      seleBeltDREndCap = cms.double( 0.2 ),
      selePtPairEndCap_region3 = cms.double( 1.0 ),
      selePtPairEndCap_region2 = cms.double( 2.5 ),
      seleIsoEndCap = cms.double( 0.5 ),
      ptMinForIsolationEndCap = cms.double( 0.5 ),
      endcapHitCollection = cms.string( "pi0EcalRecHitsEE" ),
      region2_EndCap = cms.double( 2.5 ),
      seleBeltDetaEndCap = cms.double( 0.05 ),
      store5x5RecHitEE = cms.bool( False )
    ),
    preshowerSelection = cms.PSet(
      preshCalibGamma = cms.double( 0.024 ),
      preshStripEnergyCut = cms.double( 0.0 ),
      debugLevelES = cms.string( "" ),
      preshCalibPlaneY = cms.double( 0.7 ),
      preshCalibPlaneX = cms.double( 1.0 ),
      preshCalibMIP = cms.double( 9e-05 ),
      ESCollection = cms.string( "pi0EcalRecHitsES" ),
      preshNclust = cms.int32( 4 ),
      preshClusterEnergyCut = cms.double( 0.0 ),
      preshSeededNstrip = cms.int32( 15 )
    )
)
process.hltAntiKT5CaloJets = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "AntiKt" ),
    rParam = cms.double( 0.5 ),
    src = cms.InputTag( 'hltTowerMakerForAll' ),
    srcPVs = cms.InputTag( 'offlinePrimaryVertices' ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
process.hltAntiKT5CaloJetsEt5 = cms.EDFilter( "EtMinCaloJetSelector",
    src = cms.InputTag( 'hltAntiKT5CaloJets' ),
    filter = cms.bool( False ),
    etMin = cms.double( 5.0 )
)
process.hltAntiKT5CaloJetsRegional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "AntiKt" ),
    rParam = cms.double( 0.5 ),
    src = cms.InputTag( 'hltTowerMakerForJets' ),
    srcPVs = cms.InputTag( 'offlinePrimaryVertices' ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
process.hltAntiKT5ConvPFJets = cms.EDProducer( "PFJetToCaloProducer",
    Source = cms.InputTag( 'hltAntiKT5PFJets' )
)
process.hltAntiKT5L2L3CaloJetsEle8CaloIdLCaloIsoVLRemoved = cms.EDProducer( "JetCollectionForEleHT",
    HltElectronTag = cms.InputTag( 'hltEle8CaloIdLCaloIsoVLPixelMatchFilter' ),
    SourceJetTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    minDeltaR = cms.double( 0.5 )
)
process.hltAntiKT5L2L3CorrCaloJets = cms.EDProducer( "CaloJetCorrectionProducer",
    src = cms.InputTag( 'hltAntiKT5CaloJets' ),
    verbose = cms.untracked.bool( False ),
    alias = cms.untracked.string( "JetCorJetAntiKT5" ),
    correctors = cms.vstring( "hltESSAK5CaloL2L3" )
)
process.hltAntiKT5L2L3CorrCaloJetsRegional = cms.EDProducer( "CaloJetCorrectionProducer",
    src = cms.InputTag( 'hltAntiKT5CaloJetsRegional' ),
    verbose = cms.untracked.bool( False ),
    alias = cms.untracked.string( "JetCorJetAntiKT5" ),
    correctors = cms.vstring( "hltESSAK5CaloL2L3" )
)
process.hltAntiKT5PFJets = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 0 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.5 ),
    src = cms.InputTag( 'hltParticleFlow' ),
    srcPVs = cms.InputTag( 'hltPixelVertices' ),
    jetType = cms.string( "PFJet" ),
    jetPtMin = cms.double( 15.0 ),
    inputEtMin = cms.double( 0.0 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
process.hltBDiJet20Central = cms.HLTFilter( "HLT1CaloBJet",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 20.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 2 )
)
process.hltBDiJet60Central = cms.HLTFilter( "HLT1CaloBJet",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 60.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 2 )
)
process.hltBDiJet80Central = cms.HLTFilter( "HLT1CaloBJet",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 80.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 2 )
)
process.hltBJet40Central = cms.HLTFilter( "HLT1CaloBJet",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 40.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 1 )
)
process.hltBLifetimeL25Associator = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( 'hltBLifetimeL25Jets' ),
    tracks = cms.InputTag( 'hltPixelTracks' ),
    coneSize = cms.double( 0.5 )
)
process.hltBLifetimeL25AssociatorEleJetSingleTop = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( 'hltBLifetimeL25JetsEleJetSingleTop' ),
    tracks = cms.InputTag( 'hltPixelTracks' ),
    coneSize = cms.double( 0.5 )
)
process.hltBLifetimeL25AssociatorSingleTop = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( 'hltBLifetimeL25JetsSingleTop' ),
    tracks = cms.InputTag( 'hltPixelTracks' ),
    coneSize = cms.double( 0.5 )
)
process.hltBLifetimeL25BJetTags = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPTrackCounting3D2nd" ),
    tagInfos = cms.VInputTag( 'hltBLifetimeL25TagInfos' )
)
process.hltBLifetimeL25BJetTagsEleJetSingleTop = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPTrackCounting3D2nd" ),
    tagInfos = cms.VInputTag( 'hltBLifetimeL25TagInfosEleJetSingleTop' )
)
process.hltBLifetimeL25BJetTagsSingleTop = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPTrackCounting3D2nd" ),
    tagInfos = cms.VInputTag( 'hltBLifetimeL25TagInfosSingleTop' )
)
process.hltBLifetimeL25Filter = cms.HLTFilter( "HLTJetTag",
    JetTag = cms.InputTag( 'hltBLifetimeL25BJetTags' ),
    MinTag = cms.double( 0.0 ),
    MaxTag = cms.double( 99999.0 ),
    MinJets = cms.int32( 1 ),
    SaveTag = cms.bool( False )
)
process.hltBLifetimeL25FilterEleJetSingleTop = cms.HLTFilter( "HLTJetTag",
    JetTag = cms.InputTag( 'hltBLifetimeL25BJetTagsEleJetSingleTop' ),
    MinTag = cms.double( 0.0 ),
    MaxTag = cms.double( 99999.0 ),
    MinJets = cms.int32( 1 ),
    SaveTag = cms.bool( False )
)
process.hltBLifetimeL25FilterSingleTop = cms.HLTFilter( "HLTJetTag",
    JetTag = cms.InputTag( 'hltBLifetimeL25BJetTagsSingleTop' ),
    MinTag = cms.double( 0.0 ),
    MaxTag = cms.double( 99999.0 ),
    MinJets = cms.int32( 1 ),
    SaveTag = cms.bool( False )
)
process.hltBLifetimeL25Jets = cms.EDFilter( "EtMinCaloJetSelector",
    src = cms.InputTag( 'hltSelector4Jets' ),
    filter = cms.bool( False ),
    etMin = cms.double( 25.0 )
)
process.hltBLifetimeL25JetsEleJetSingleTop = cms.EDFilter( "EtMinCaloJetSelector",
    src = cms.InputTag( 'hltSelectorEleJetsSingleTop' ),
    filter = cms.bool( False ),
    etMin = cms.double( 20.0 )
)
process.hltBLifetimeL25JetsSingleTop = cms.EDFilter( "EtMinCaloJetSelector",
    src = cms.InputTag( 'hltSelectorJetsSingleTop' ),
    filter = cms.bool( False ),
    etMin = cms.double( 20.0 )
)
process.hltBLifetimeL25TagInfos = cms.EDProducer( "TrackIPProducer",
    jetTracks = cms.InputTag( 'hltBLifetimeL25Associator' ),
    primaryVertex = cms.InputTag( 'hltPixelVertices' ),
    computeProbabilities = cms.bool( False ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    minimumNumberOfHits = cms.int32( 3 ),
    maximumTransverseImpactParameter = cms.double( 0.2 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    maximumChiSquared = cms.double( 5.0 ),
    maximumLongitudinalImpactParameter = cms.double( 17.0 ),
    jetDirectionUsingTracks = cms.bool( False ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    useTrackQuality = cms.bool( False )
)
process.hltBLifetimeL25TagInfosEleJetSingleTop = cms.EDProducer( "TrackIPProducer",
    jetTracks = cms.InputTag( 'hltBLifetimeL25AssociatorEleJetSingleTop' ),
    primaryVertex = cms.InputTag( 'hltPixelVertices' ),
    computeProbabilities = cms.bool( False ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    minimumNumberOfHits = cms.int32( 3 ),
    maximumTransverseImpactParameter = cms.double( 0.2 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    maximumChiSquared = cms.double( 5.0 ),
    maximumLongitudinalImpactParameter = cms.double( 17.0 ),
    jetDirectionUsingTracks = cms.bool( False ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    useTrackQuality = cms.bool( False )
)
process.hltBLifetimeL25TagInfosSingleTop = cms.EDProducer( "TrackIPProducer",
    jetTracks = cms.InputTag( 'hltBLifetimeL25AssociatorSingleTop' ),
    primaryVertex = cms.InputTag( 'hltPixelVertices' ),
    computeProbabilities = cms.bool( False ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    minimumNumberOfHits = cms.int32( 3 ),
    maximumTransverseImpactParameter = cms.double( 0.2 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    maximumChiSquared = cms.double( 5.0 ),
    maximumLongitudinalImpactParameter = cms.double( 17.0 ),
    jetDirectionUsingTracks = cms.bool( False ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    useTrackQuality = cms.bool( False )
)
process.hltBLifetimeL3Associator = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( 'hltBLifetimeL25Jets' ),
    tracks = cms.InputTag( 'hltBLifetimeRegionalCtfWithMaterialTracks' ),
    coneSize = cms.double( 0.5 )
)
process.hltBLifetimeL3AssociatorEleJetSingleTop = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( 'hltBLifetimeL3EleJetsSingleTop' ),
    tracks = cms.InputTag( 'hltBLifetimeRegionalCtfWithMaterialTracksEleJetSingleTop' ),
    coneSize = cms.double( 0.5 )
)
process.hltBLifetimeL3AssociatorSingleTop = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( 'hltBLifetimeL3JetsSingleTop' ),
    tracks = cms.InputTag( 'hltBLifetimeRegionalCtfWithMaterialTracksSingleTop' ),
    coneSize = cms.double( 0.5 )
)
process.hltBLifetimeL3BJetTags = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPTrackCounting3D2nd" ),
    tagInfos = cms.VInputTag( 'hltBLifetimeL3TagInfos' )
)
process.hltBLifetimeL3BJetTagsEleJetSingleTop = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPTrackCounting3D2nd" ),
    tagInfos = cms.VInputTag( 'hltBLifetimeL3TagInfosEleJetSingleTop' )
)
process.hltBLifetimeL3BJetTagsSingleTop = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPTrackCounting3D2nd" ),
    tagInfos = cms.VInputTag( 'hltBLifetimeL3TagInfosSingleTop' )
)
process.hltBLifetimeL3EleJetsSingleTop = cms.EDProducer( "GetJetsFromHLTobject",
    jets = cms.InputTag( 'hltBLifetimeL25FilterEleJetSingleTop' )
)
process.hltBLifetimeL3Filter = cms.HLTFilter( "HLTJetTag",
    JetTag = cms.InputTag( 'hltBLifetimeL3BJetTags' ),
    MinTag = cms.double( 2.0 ),
    MaxTag = cms.double( 99999.0 ),
    MinJets = cms.int32( 1 ),
    SaveTag = cms.bool( True )
)
process.hltBLifetimeL3FilterEleJetSingleTop = cms.HLTFilter( "HLTJetTag",
    JetTag = cms.InputTag( 'hltBLifetimeL3BJetTagsEleJetSingleTop' ),
    MinTag = cms.double( 2.0 ),
    MaxTag = cms.double( 99999.0 ),
    MinJets = cms.int32( 1 ),
    SaveTag = cms.bool( True )
)
process.hltBLifetimeL3FilterSingleTop = cms.HLTFilter( "HLTJetTag",
    JetTag = cms.InputTag( 'hltBLifetimeL3BJetTagsSingleTop' ),
    MinTag = cms.double( 2.0 ),
    MaxTag = cms.double( 99999.0 ),
    MinJets = cms.int32( 1 ),
    SaveTag = cms.bool( True )
)
process.hltBLifetimeL3JetsSingleTop = cms.EDProducer( "GetJetsFromHLTobject",
    jets = cms.InputTag( 'hltBLifetimeL25FilterSingleTop' )
)
process.hltBLifetimeL3TagInfos = cms.EDProducer( "TrackIPProducer",
    jetTracks = cms.InputTag( 'hltBLifetimeL3Associator' ),
    primaryVertex = cms.InputTag( 'hltPixelVertices' ),
    computeProbabilities = cms.bool( False ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    minimumNumberOfHits = cms.int32( 8 ),
    maximumTransverseImpactParameter = cms.double( 0.2 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    maximumChiSquared = cms.double( 20.0 ),
    maximumLongitudinalImpactParameter = cms.double( 17.0 ),
    jetDirectionUsingTracks = cms.bool( False ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    useTrackQuality = cms.bool( False )
)
process.hltBLifetimeL3TagInfosEleJetSingleTop = cms.EDProducer( "TrackIPProducer",
    jetTracks = cms.InputTag( 'hltBLifetimeL3AssociatorEleJetSingleTop' ),
    primaryVertex = cms.InputTag( 'hltPixelVertices' ),
    computeProbabilities = cms.bool( False ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    minimumNumberOfHits = cms.int32( 8 ),
    maximumTransverseImpactParameter = cms.double( 0.2 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    maximumChiSquared = cms.double( 20.0 ),
    maximumLongitudinalImpactParameter = cms.double( 17.0 ),
    jetDirectionUsingTracks = cms.bool( False ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    useTrackQuality = cms.bool( False )
)
process.hltBLifetimeL3TagInfosSingleTop = cms.EDProducer( "TrackIPProducer",
    jetTracks = cms.InputTag( 'hltBLifetimeL3AssociatorSingleTop' ),
    primaryVertex = cms.InputTag( 'hltPixelVertices' ),
    computeProbabilities = cms.bool( False ),
    computeGhostTrack = cms.bool( False ),
    ghostTrackPriorDeltaR = cms.double( 0.03 ),
    minimumNumberOfPixelHits = cms.int32( 2 ),
    minimumNumberOfHits = cms.int32( 8 ),
    maximumTransverseImpactParameter = cms.double( 0.2 ),
    minimumTransverseMomentum = cms.double( 1.0 ),
    maximumChiSquared = cms.double( 20.0 ),
    maximumLongitudinalImpactParameter = cms.double( 17.0 ),
    jetDirectionUsingTracks = cms.bool( False ),
    jetDirectionUsingGhostTrack = cms.bool( False ),
    useTrackQuality = cms.bool( False )
)
process.hltBLifetimeRegionalCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( 'hltBLifetimeRegionalPixelSeedGenerator' ),
    TrajectoryBuilder = cms.string( "hltESPbJetRegionalTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltBLifetimeRegionalCkfTrackCandidatesEleJetSingleTop = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( 'hltBLifetimeRegionalPixelSeedGeneratorEleJetSingleTop' ),
    TrajectoryBuilder = cms.string( "hltESPbJetRegionalTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltBLifetimeRegionalCkfTrackCandidatesSingleTop = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( 'hltBLifetimeRegionalPixelSeedGeneratorSingleTop' ),
    TrajectoryBuilder = cms.string( "hltESPbJetRegionalTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltBLifetimeRegionalCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( True ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    Fitter = cms.string( "hltESPFittingSmootherRK" ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
    src = cms.InputTag( 'hltBLifetimeRegionalCkfTrackCandidates' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltBLifetimeRegionalCtfWithMaterialTracksEleJetSingleTop = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( True ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    Fitter = cms.string( "hltESPFittingSmootherRK" ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
    src = cms.InputTag( 'hltBLifetimeRegionalCkfTrackCandidatesEleJetSingleTop' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltBLifetimeRegionalCtfWithMaterialTracksSingleTop = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( True ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    Fitter = cms.string( "hltESPFittingSmootherRK" ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
    src = cms.InputTag( 'hltBLifetimeRegionalCkfTrackCandidatesSingleTop' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltBLifetimeRegionalPixelSeedGenerator = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    ClusterCheckPSet = cms.PSet(
      PixelClusterCollectionLabel = cms.InputTag( 'hltSiPixelClusters' ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
      doClusterCheck = cms.bool( False ),
      ClusterCollectionLabel = cms.InputTag( 'hltSiStripClusters' ),
      MaxNumberOfPixelClusters = cms.uint32( 10000 )
    ),
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "TauRegionalPixelSeedGenerator" ),
      RegionPSet = cms.PSet(
        precise = cms.bool( True ),
        deltaPhiRegion = cms.double( 0.5 ),
        originHalfLength = cms.double( 0.2 ),
        originRadius = cms.double( 0.2 ),
        deltaEtaRegion = cms.double( 0.5 ),
        ptMin = cms.double( 1.0 ),
        JetSrc = cms.InputTag( 'hltBLifetimeL25Jets' ),
        originZPos = cms.double( 0.0 ),
        vertexSrc = cms.InputTag( 'hltPixelVertices' )
      )
    ),
    OrderedHitsFactoryPSet = cms.PSet(
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltESPPixelLayerPairs" )
    ),
    SeedComparitorPSet = cms.PSet(
      ComponentName = cms.string( "none" )
    ),
    SeedCreatorPSet = cms.PSet(
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      propagator = cms.string( "PropagatorWithMaterial" )
    ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltBLifetimeRegionalPixelSeedGeneratorEleJetSingleTop = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    ClusterCheckPSet = cms.PSet(
      PixelClusterCollectionLabel = cms.InputTag( 'hltSiPixelClusters' ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
      doClusterCheck = cms.bool( False ),
      ClusterCollectionLabel = cms.InputTag( 'hltSiStripClusters' ),
      MaxNumberOfPixelClusters = cms.uint32( 10000 )
    ),
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "TauRegionalPixelSeedGenerator" ),
      RegionPSet = cms.PSet(
        precise = cms.bool( True ),
        deltaPhiRegion = cms.double( 0.5 ),
        originHalfLength = cms.double( 0.2 ),
        originRadius = cms.double( 0.2 ),
        deltaEtaRegion = cms.double( 0.5 ),
        ptMin = cms.double( 1.0 ),
        JetSrc = cms.InputTag( 'hltBLifetimeL3EleJetsSingleTop' ),
        originZPos = cms.double( 0.0 ),
        vertexSrc = cms.InputTag( 'hltPixelVertices' )
      )
    ),
    OrderedHitsFactoryPSet = cms.PSet(
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltESPPixelLayerPairs" )
    ),
    SeedComparitorPSet = cms.PSet(
      ComponentName = cms.string( "none" )
    ),
    SeedCreatorPSet = cms.PSet(
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      propagator = cms.string( "PropagatorWithMaterial" )
    ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltBLifetimeRegionalPixelSeedGeneratorSingleTop = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    ClusterCheckPSet = cms.PSet(
      PixelClusterCollectionLabel = cms.InputTag( 'hltSiPixelClusters' ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
      doClusterCheck = cms.bool( False ),
      ClusterCollectionLabel = cms.InputTag( 'hltSiStripClusters' ),
      MaxNumberOfPixelClusters = cms.uint32( 10000 )
    ),
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "TauRegionalPixelSeedGenerator" ),
      RegionPSet = cms.PSet(
        precise = cms.bool( True ),
        deltaPhiRegion = cms.double( 0.5 ),
        originHalfLength = cms.double( 0.2 ),
        originRadius = cms.double( 0.2 ),
        deltaEtaRegion = cms.double( 0.5 ),
        ptMin = cms.double( 1.0 ),
        JetSrc = cms.InputTag( 'hltBLifetimeL3JetsSingleTop' ),
        originZPos = cms.double( 0.0 ),
        vertexSrc = cms.InputTag( 'hltPixelVertices' )
      )
    ),
    OrderedHitsFactoryPSet = cms.PSet(
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltESPPixelLayerPairs" )
    ),
    SeedComparitorPSet = cms.PSet(
      ComponentName = cms.string( "none" )
    ),
    SeedCreatorPSet = cms.PSet(
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      propagator = cms.string( "PropagatorWithMaterial" )
    ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltBPTXAntiCoincidence = cms.HLTFilter( "HLTLevel1Activity",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    daqPartitions = cms.uint32( 1 ),
    ignoreL1Mask = cms.bool( True ),
    invert = cms.bool( True ),
    physicsLoBits = cms.uint64( 0x1 ),
    physicsHiBits = cms.uint64( 0x0 ),
    technicalBits = cms.uint64( 0x11 ),
    bunchCrossings = cms.vint32( 0, 1, -1 )
)
process.hltBPTXCoincidence = cms.HLTFilter( "HLTLevel1Activity",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    daqPartitions = cms.uint32( 1 ),
    ignoreL1Mask = cms.bool( True ),
    invert = cms.bool( False ),
    physicsLoBits = cms.uint64( 0x1 ),
    physicsHiBits = cms.uint64( 0x0 ),
    technicalBits = cms.uint64( 0x7f ),
    bunchCrossings = cms.vint32( 0, -1, 1 )
)
process.hltBSoftMuon5L3 = cms.EDFilter( "RecoTrackRefSelector",
    src = cms.InputTag( 'hltL3Muons' ),
    maxChi2 = cms.double( 10000.0 ),
    tip = cms.double( 120.0 ),
    minRapidity = cms.double( -5.0 ),
    lip = cms.double( 300.0 ),
    ptMin = cms.double( 5.0 ),
    maxRapidity = cms.double( 5.0 ),
    quality = cms.vstring("  "),
    algorithm = cms.vstring("  "),
    minHit = cms.int32( 0 ),
    min3DHit = cms.int32( 0 ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' )
)
process.hltBSoftMuon5SelL3BJetTagsByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuon5SelL3TagInfos' )
)
process.hltBSoftMuon5SelL3BJetTagsByPt = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByPt" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuon5SelL3TagInfos' )
)
process.hltBSoftMuon5SelL3FilterByDR = cms.HLTFilter( "HLTJetTag",
    JetTag = cms.InputTag( 'hltBSoftMuon5SelL3BJetTagsByDR' ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 ),
    MinJets = cms.int32( 1 ),
    SaveTag = cms.bool( True )
)
process.hltBSoftMuon5SelL3TagInfos = cms.EDProducer( "SoftLepton",
    jets = cms.InputTag( 'hltBSoftMuonL25Jets' ),
    primaryVertex = cms.InputTag( 'nominal' ),
    leptons = cms.InputTag( 'hltBSoftMuon5L3' ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 ),
    muonSelection = cms.uint32( 0 )
)
process.hltBSoftMuon7L3 = cms.EDFilter( "RecoTrackRefSelector",
    src = cms.InputTag( 'hltL3Muons' ),
    maxChi2 = cms.double( 10000.0 ),
    tip = cms.double( 120.0 ),
    minRapidity = cms.double( -5.0 ),
    lip = cms.double( 300.0 ),
    ptMin = cms.double( 7.0 ),
    maxRapidity = cms.double( 5.0 ),
    quality = cms.vstring("  "),
    algorithm = cms.vstring("  "),
    minHit = cms.int32( 0 ),
    min3DHit = cms.int32( 0 ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' )
)
process.hltBSoftMuon7SelL3BJetTagsByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuon7SelL3TagInfos' )
)
process.hltBSoftMuon7SelL3BJetTagsByPt = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByPt" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuon7SelL3TagInfos' )
)
process.hltBSoftMuon7SelL3FilterByDR = cms.HLTFilter( "HLTJetTag",
    JetTag = cms.InputTag( 'hltBSoftMuon7SelL3BJetTagsByDR' ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 ),
    MinJets = cms.int32( 1 ),
    SaveTag = cms.bool( True )
)
process.hltBSoftMuon7SelL3TagInfos = cms.EDProducer( "SoftLepton",
    jets = cms.InputTag( 'hltBSoftMuonL25Jets' ),
    primaryVertex = cms.InputTag( 'nominal' ),
    leptons = cms.InputTag( 'hltBSoftMuon7L3' ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 ),
    muonSelection = cms.uint32( 0 )
)
process.hltBSoftMuon9L3 = cms.EDFilter( "RecoTrackRefSelector",
    src = cms.InputTag( 'hltL3Muons' ),
    maxChi2 = cms.double( 10000.0 ),
    tip = cms.double( 120.0 ),
    minRapidity = cms.double( -5.0 ),
    lip = cms.double( 300.0 ),
    ptMin = cms.double( 9.0 ),
    maxRapidity = cms.double( 5.0 ),
    quality = cms.vstring("  "),
    algorithm = cms.vstring("  "),
    minHit = cms.int32( 0 ),
    min3DHit = cms.int32( 0 ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' )
)
process.hltBSoftMuon9SelL3BJetTagsByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuon9SelL3TagInfos' )
)
process.hltBSoftMuon9SelL3BJetTagsByPt = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByPt" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuon9SelL3TagInfos' )
)
process.hltBSoftMuon9SelL3FilterByDR = cms.HLTFilter( "HLTJetTag",
    JetTag = cms.InputTag( 'hltBSoftMuon9SelL3BJetTagsByDR' ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 ),
    MinJets = cms.int32( 1 ),
    SaveTag = cms.bool( True )
)
process.hltBSoftMuon9SelL3TagInfos = cms.EDProducer( "SoftLepton",
    jets = cms.InputTag( 'hltBSoftMuonL25Jets' ),
    primaryVertex = cms.InputTag( 'nominal' ),
    leptons = cms.InputTag( 'hltBSoftMuon9L3' ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 ),
    muonSelection = cms.uint32( 0 )
)
process.hltBSoftMuonL25BJetTagsByDR = cms.EDProducer( "JetTagProducer",
    jetTagComputer = cms.string( "hltESPSoftLeptonByDistance" ),
    tagInfos = cms.VInputTag( 'hltBSoftMuonL25TagInfos' )
)
process.hltBSoftMuonL25FilterByDR = cms.HLTFilter( "HLTJetTag",
    JetTag = cms.InputTag( 'hltBSoftMuonL25BJetTagsByDR' ),
    MinTag = cms.double( 0.5 ),
    MaxTag = cms.double( 99999.0 ),
    MinJets = cms.int32( 1 ),
    SaveTag = cms.bool( False )
)
process.hltBSoftMuonL25Jets = cms.EDFilter( "EtMinCaloJetSelector",
    src = cms.InputTag( 'hltSelector4Jets' ),
    filter = cms.bool( False ),
    etMin = cms.double( 20.0 )
)
process.hltBSoftMuonL25TagInfos = cms.EDProducer( "SoftLepton",
    jets = cms.InputTag( 'hltBSoftMuonL25Jets' ),
    primaryVertex = cms.InputTag( 'nominal' ),
    leptons = cms.InputTag( 'hltL2Muons' ),
    leptonCands = cms.InputTag( "" ),
    leptonId = cms.InputTag( "" ),
    refineJetAxis = cms.uint32( 0 ),
    leptonDeltaRCut = cms.double( 0.4 ),
    leptonChi2Cut = cms.double( 0.0 ),
    muonSelection = cms.uint32( 0 )
)
process.hltBoolEnd = cms.HLTFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltBoolFalse = cms.HLTFilter( "HLTBool",
    result = cms.bool( False )
)
process.hltBoolTrue = cms.HLTFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltCSCMonitorModule = cms.EDAnalyzer( "CSCMonitorModule",
    InputObjects = cms.untracked.InputTag( 'source' ),
    PREBOOK_EFF_PARAMS = cms.untracked.bool( False ),
    PROCESS_DCS_SCALERS = cms.untracked.bool( True ),
    BOOKING_XML_FILE = cms.FileInPath( "DQM/CSCMonitorModule/data/emuDQMBooking.xml" ),
    MASKEDHW = cms.untracked.vstring("  "),
    EventProcessor = cms.untracked.PSet(
      EFF_ERR_SIGFAIL = cms.untracked.double( 5.0 ),
      FRAEFF_AUTO_UPDATE = cms.untracked.bool( False ),
      EFF_NODATA_THRESHOLD = cms.untracked.double( 0.1 ),
      FRAEFF_AUTO_UPDATE_START = cms.untracked.uint32( 5 ),
      BINCHECK_MASK = cms.untracked.uint32( 384563190 ),
      BINCHECKER_CRC_CLCT = cms.untracked.bool( True ),
      EFF_COLD_SIGFAIL = cms.untracked.double( 5.0 ),
      PROCESS_DDU = cms.untracked.bool( False ),
      EFF_NODATA_SIGFAIL = cms.untracked.double( 5.0 ),
      BINCHECKER_MODE_DDU = cms.untracked.bool( False ),
      BINCHECKER_CRC_ALCT = cms.untracked.bool( True ),
      EFF_HOT_THRESHOLD = cms.untracked.double( 0.1 ),
      FOLDER_DDU = cms.untracked.string( "" ),
      BINCHECKER_CRC_CFEB = cms.untracked.bool( True ),
      EVENTS_ECHO = cms.untracked.uint32( 1000 ),
      DDU_CHECK_MASK = cms.untracked.uint32( 4294959103 ),
      FRAEFF_SEPARATE_THREAD = cms.untracked.bool( False ),
      PROCESS_EFF_PARAMETERS = cms.untracked.bool( False ),
      EFF_HOT_SIGFAIL = cms.untracked.double( 5.0 ),
      FOLDER_PAR = cms.untracked.string( "" ),
      FRAEFF_AUTO_UPDATE_FREQ = cms.untracked.uint32( 200 ),
      EFF_COLD_THRESHOLD = cms.untracked.double( 0.1 ),
      FOLDER_EMU = cms.untracked.string( "CSC/FEDIntegrity_EvF" ),
      DDU_BINCHECK_MASK = cms.untracked.uint32( 384563190 ),
      PROCESS_CSC = cms.untracked.bool( False ),
      PROCESS_EFF_HISTOS = cms.untracked.bool( False ),
      MO_FILTER = cms.untracked.vstring( "-/^.*$/",
         "+/FEDEntries/",
         "+/FEDFatal/",
         "+/FEDFormatFatal/",
         "+/FEDNonFatal/",
         "+/^CSC_Reporting$/",
         "+/^CSC_Format_Errors$/",
         "+/^CSC_Format_Warnings$/",
         "+/^CSC_L1A_out_of_sync$/",
         "+/^CSC_wo_ALCT$/",
         "+/^CSC_wo_CFEB$/",
         "+/^CSC_wo_CLCT$/" ),
      FOLDER_CSC = cms.untracked.string( "" ),
      EFF_ERR_THRESHOLD = cms.untracked.double( 0.1 ),
      BINCHECKER_OUTPUT = cms.untracked.bool( False )
    )
)
process.hltCalibrationEventsFilter = cms.HLTFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 2 )
)
process.hltCaloTowersCentral1Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    verbose = cms.untracked.int32( 0 ),
    towers = cms.InputTag( 'hltTowerMakerForJets' ),
    UseTowersInCone = cms.double( 0.8 ),
    TauTrigger = cms.InputTag( 'hltL1extraParticles', 'Central' ),
    minimumEt = cms.double( 0.5 ),
    minimumE = cms.double( 0.8 ),
    TauId = cms.int32( 0 )
)
process.hltCaloTowersCentral2Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    verbose = cms.untracked.int32( 0 ),
    towers = cms.InputTag( 'hltTowerMakerForJets' ),
    UseTowersInCone = cms.double( 0.8 ),
    TauTrigger = cms.InputTag( 'hltL1extraParticles', 'Central' ),
    minimumEt = cms.double( 0.5 ),
    minimumE = cms.double( 0.8 ),
    TauId = cms.int32( 1 )
)
process.hltCaloTowersCentral3Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    verbose = cms.untracked.int32( 0 ),
    towers = cms.InputTag( 'hltTowerMakerForJets' ),
    UseTowersInCone = cms.double( 0.8 ),
    TauTrigger = cms.InputTag( 'hltL1extraParticles', 'Central' ),
    minimumEt = cms.double( 0.5 ),
    minimumE = cms.double( 0.8 ),
    TauId = cms.int32( 2 )
)
process.hltCaloTowersCentral4Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    verbose = cms.untracked.int32( 0 ),
    towers = cms.InputTag( 'hltTowerMakerForJets' ),
    UseTowersInCone = cms.double( 0.8 ),
    TauTrigger = cms.InputTag( 'hltL1extraParticles', 'Central' ),
    minimumEt = cms.double( 0.5 ),
    minimumE = cms.double( 0.8 ),
    TauId = cms.int32( 3 )
)
process.hltCaloTowersTau1Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    verbose = cms.untracked.int32( 0 ),
    towers = cms.InputTag( 'hltTowerMakerForJets' ),
    UseTowersInCone = cms.double( 0.8 ),
    TauTrigger = cms.InputTag( 'hltL1extraParticles', 'Tau' ),
    minimumEt = cms.double( 0.5 ),
    minimumE = cms.double( 0.8 ),
    TauId = cms.int32( 0 )
)
process.hltCaloTowersTau2Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    verbose = cms.untracked.int32( 0 ),
    towers = cms.InputTag( 'hltTowerMakerForJets' ),
    UseTowersInCone = cms.double( 0.8 ),
    TauTrigger = cms.InputTag( 'hltL1extraParticles', 'Tau' ),
    minimumEt = cms.double( 0.5 ),
    minimumE = cms.double( 0.8 ),
    TauId = cms.int32( 1 )
)
process.hltCaloTowersTau3Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    verbose = cms.untracked.int32( 0 ),
    towers = cms.InputTag( 'hltTowerMakerForJets' ),
    UseTowersInCone = cms.double( 0.8 ),
    TauTrigger = cms.InputTag( 'hltL1extraParticles', 'Tau' ),
    minimumEt = cms.double( 0.5 ),
    minimumE = cms.double( 0.8 ),
    TauId = cms.int32( 2 )
)
process.hltCaloTowersTau4Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
    verbose = cms.untracked.int32( 0 ),
    towers = cms.InputTag( 'hltTowerMakerForJets' ),
    UseTowersInCone = cms.double( 0.8 ),
    TauTrigger = cms.InputTag( 'hltL1extraParticles', 'Tau' ),
    minimumEt = cms.double( 0.5 ),
    minimumE = cms.double( 0.8 ),
    TauId = cms.int32( 3 )
)
process.hltCenJet80CentralRegional = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltJetIDPassedJetsRegional' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 80.0 ),
    MaxEta = cms.double( 2.6 ),
    MinN = cms.int32( 1 )
)
process.hltCkfActivityTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( 'hltActivityStartUpElectronPixelSeeds' ),
    TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltCkfL1IsoTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltCkfL1NonIsoTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltCleanEle25CaloIdVTTrkIdTFromAK5CorrJets = cms.EDProducer( "JetCollectionForEleHT",
    HltElectronTag = cms.InputTag( 'hltEle25CaloIdVTTrkIdTDphiFilter' ),
    SourceJetTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    minDeltaR = cms.double( 0.3 )
)
process.hltConvPFTauTightIsoTrackPt20 = cms.EDProducer( "PFTauToJetProducer",
    Source = cms.InputTag( 'hltSelectedPFTauTightIsoTrackPt20' )
)
process.hltConvPFTauTightIsoTrackPt20Isolation = cms.EDProducer( "PFTauToJetProducer",
    Source = cms.InputTag( 'hltSelectedPFTauTightIsoTrackPt20Isolation' )
)
process.hltConvPFTaus = cms.EDProducer( "PFTauToJetProducer",
    Source = cms.InputTag( 'hltPFTaus' )
)
process.hltConvPFTausTightIso = cms.EDProducer( "PFTauToJetProducer",
    Source = cms.InputTag( 'hltPFTausTightIso' )
)
process.hltConvPFTausTightIsoTrackFinding = cms.EDProducer( "PFTauToJetProducer",
    Source = cms.InputTag( 'hltSelectedPFTausTightIsoTrackFinding' )
)
process.hltConvPFTausTightIsoTrackFindingIsolation = cms.EDProducer( "PFTauToJetProducer",
    Source = cms.InputTag( 'hltSelectedPFTausTightIsoTrackFindingIsolation' )
)
process.hltConvPFTausTightIsoTrackPt5 = cms.EDProducer( "PFTauToJetProducer",
    Source = cms.InputTag( 'hltSelectedPFTausTightIsoTrackPt5' )
)
process.hltConvPFTausTightIsoTrackPt5Isolation = cms.EDProducer( "PFTauToJetProducer",
    Source = cms.InputTag( 'hltSelectedPFTausTightIsoTrackPt5Isolation' )
)
process.hltConvPFTausTrackFinding = cms.EDProducer( "PFTauToJetProducer",
    Source = cms.InputTag( 'hltSelectedPFTausTrackFinding' )
)
process.hltConvPFTausTrackFindingIsolation = cms.EDProducer( "PFTauToJetProducer",
    Source = cms.InputTag( 'hltSelectedPFTausTrackFindingIsolation' )
)
process.hltConvPFTausTrackFindingLooseIsolation = cms.EDProducer( "PFTauToJetProducer",
    Source = cms.InputTag( 'hltSelectedPFTausTrackFindingLooseIsolation' )
)
process.hltConvPFTausTrackPt5 = cms.EDProducer( "PFTauToJetProducer",
    Source = cms.InputTag( 'hltSelectedPFTausTrackPt5' )
)
process.hltConvPFTausTrackPt5Isolation = cms.EDProducer( "PFTauToJetProducer",
    Source = cms.InputTag( 'hltSelectedPFTausTrackPt5Isolation' )
)
process.hltCorrectedHybridSuperClustersActivity = cms.EDProducer( "EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRecHitAll', 'EcalRecHitsEB' ),
    rawSuperClusterProducer = cms.InputTag( 'hltHybridSuperClustersActivity' ),
    superClusterAlgo = cms.string( "Hybrid" ),
    applyEnergyCorrection = cms.bool( True ),
    applyCrackCorrection = cms.bool( False ),
    sigmaElectronicNoise = cms.double( 0.15 ),
    etThresh = cms.double( 0.0 ),
    corectedSuperClusterCollection = cms.string( "" ),
    hyb_fCorrPset = cms.PSet(
      brLinearLowThr = cms.double( 1.1 ),
      fEtEtaVec = cms.vdouble(  0, 1.00121, -0.63672, 0, 0, 0, 0.5655, 6.457, 0.5081, 8, 1.023, -0.00181  ),
      brLinearHighThr = cms.double( 8.0 ),
      fBremVec = cms.vdouble(  -0.04382, 0.1169, 0.9267, -0.0009413, 1.419  )
    ),
    isl_fCorrPset = cms.PSet(  ),
    dyn_fCorrPset = cms.PSet(  ),
    fix_fCorrPset = cms.PSet(  )
)
process.hltCorrectedHybridSuperClustersL1Isolated = cms.EDProducer( "EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEB' ),
    rawSuperClusterProducer = cms.InputTag( 'hltHybridSuperClustersL1Isolated' ),
    superClusterAlgo = cms.string( "Hybrid" ),
    applyEnergyCorrection = cms.bool( True ),
    applyCrackCorrection = cms.bool( False ),
    sigmaElectronicNoise = cms.double( 0.03 ),
    etThresh = cms.double( 1.0 ),
    corectedSuperClusterCollection = cms.string( "" ),
    hyb_fCorrPset = cms.PSet(
      brLinearLowThr = cms.double( 1.1 ),
      fBremVec = cms.vdouble(  -0.05208, 0.1331, 0.9196, -0.0005735, 1.343  ),
      brLinearHighThr = cms.double( 8.0 ),
      fEtEtaVec = cms.vdouble(  1.0012, -0.5714, 0, 0, 0, 0.5549, 12.74, 1.0448, 0, 0, 0, 0, 8, 1.023, -0.00181, 0, 0  )
    ),
    isl_fCorrPset = cms.PSet(  ),
    dyn_fCorrPset = cms.PSet(  ),
    fix_fCorrPset = cms.PSet(  )
)
process.hltCorrectedHybridSuperClustersL1NonIsolated = cms.EDProducer( "EgammaHLTRemoveDuplicatedSC",
    L1NonIsoUskimmedSC = cms.InputTag( 'hltCorrectedHybridSuperClustersL1NonIsolatedTemp' ),
    L1IsoSC = cms.InputTag( 'hltCorrectedHybridSuperClustersL1Isolated' ),
    L1NonIsoSkimmedCollection = cms.string( "" )
)
process.hltCorrectedHybridSuperClustersL1NonIsolatedTemp = cms.EDProducer( "EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEB' ),
    rawSuperClusterProducer = cms.InputTag( 'hltHybridSuperClustersL1NonIsolated' ),
    superClusterAlgo = cms.string( "Hybrid" ),
    applyEnergyCorrection = cms.bool( True ),
    applyCrackCorrection = cms.bool( False ),
    sigmaElectronicNoise = cms.double( 0.03 ),
    etThresh = cms.double( 1.0 ),
    corectedSuperClusterCollection = cms.string( "" ),
    hyb_fCorrPset = cms.PSet(
      brLinearLowThr = cms.double( 1.1 ),
      fBremVec = cms.vdouble(  -0.05208, 0.1331, 0.9196, -0.0005735, 1.343  ),
      brLinearHighThr = cms.double( 8.0 ),
      fEtEtaVec = cms.vdouble(  1.0012, -0.5714, 0, 0, 0, 0.5549, 12.74, 1.0448, 0, 0, 0, 0, 8, 1.023, -0.00181, 0, 0  )
    ),
    isl_fCorrPset = cms.PSet(  ),
    dyn_fCorrPset = cms.PSet(  ),
    fix_fCorrPset = cms.PSet(  )
)
process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated = cms.EDProducer( "EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEE' ),
    rawSuperClusterProducer = cms.InputTag( 'hltMulti5x5EndcapSuperClustersWithPreshowerL1Isolated' ),
    superClusterAlgo = cms.string( "Multi5x5" ),
    applyEnergyCorrection = cms.bool( True ),
    applyCrackCorrection = cms.bool( False ),
    sigmaElectronicNoise = cms.double( 0.15 ),
    etThresh = cms.double( 1.0 ),
    corectedSuperClusterCollection = cms.string( "" ),
    hyb_fCorrPset = cms.PSet(  ),
    isl_fCorrPset = cms.PSet(  ),
    dyn_fCorrPset = cms.PSet(  ),
    fix_fCorrPset = cms.PSet(
      brLinearLowThr = cms.double( 0.6 ),
      fBremVec = cms.vdouble(  -0.04163, 0.08552, 0.95048, -0.002308, 1.077  ),
      brLinearHighThr = cms.double( 6.0 ),
      fEtEtaVec = cms.vdouble(  0.9746, -6.512, 0, 0, 0.02771, 4.983, 0, 0, -0.007288, -0.9446, 0, 0, 0, 0, 0, 1, 1  )
    )
)
process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated = cms.EDProducer( "EgammaHLTRemoveDuplicatedSC",
    L1NonIsoUskimmedSC = cms.InputTag( 'hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedTemp' ),
    L1IsoSC = cms.InputTag( 'hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated' ),
    L1NonIsoSkimmedCollection = cms.string( "" )
)
process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedTemp = cms.EDProducer( "EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEE' ),
    rawSuperClusterProducer = cms.InputTag( 'hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated' ),
    superClusterAlgo = cms.string( "Multi5x5" ),
    applyEnergyCorrection = cms.bool( True ),
    applyCrackCorrection = cms.bool( False ),
    sigmaElectronicNoise = cms.double( 0.15 ),
    etThresh = cms.double( 1.0 ),
    corectedSuperClusterCollection = cms.string( "" ),
    hyb_fCorrPset = cms.PSet(  ),
    isl_fCorrPset = cms.PSet(  ),
    dyn_fCorrPset = cms.PSet(  ),
    fix_fCorrPset = cms.PSet(
      brLinearLowThr = cms.double( 0.6 ),
      fBremVec = cms.vdouble(  -0.04163, 0.08552, 0.95048, -0.002308, 1.077  ),
      brLinearHighThr = cms.double( 6.0 ),
      fEtEtaVec = cms.vdouble(  0.9746, -6.512, 0, 0, 0.02771, 4.983, 0, 0, -0.007288, -0.9446, 0, 0, 0, 0, 0, 1, 1  )
    )
)
process.hltCorrectedMulti5x5SuperClustersWithPreshowerActivity = cms.EDProducer( "EgammaSCCorrectionMaker",
    VerbosityLevel = cms.string( "ERROR" ),
    recHitProducer = cms.InputTag( 'hltEcalRecHitAll', 'EcalRecHitsEE' ),
    rawSuperClusterProducer = cms.InputTag( 'hltMulti5x5SuperClustersWithPreshowerActivity' ),
    superClusterAlgo = cms.string( "Multi5x5" ),
    applyEnergyCorrection = cms.bool( True ),
    applyCrackCorrection = cms.bool( False ),
    sigmaElectronicNoise = cms.double( 0.15 ),
    etThresh = cms.double( 0.0 ),
    corectedSuperClusterCollection = cms.string( "" ),
    hyb_fCorrPset = cms.PSet(  ),
    isl_fCorrPset = cms.PSet(  ),
    dyn_fCorrPset = cms.PSet(  ),
    fix_fCorrPset = cms.PSet(
      brLinearLowThr = cms.double( 0.9 ),
      fEtEtaVec = cms.vdouble(  1, -0.4386, -32.38, 0.6372, 15.67, -0.0928, -2.462, 1.138, 20.93  ),
      brLinearHighThr = cms.double( 6.0 ),
      fBremVec = cms.vdouble(  -0.05228, 0.08738, 0.9508, 0.002677, 1.221  )
    )
)
process.hltCosmicTrackSelector = cms.EDProducer( "CosmicTrackSelector",
    src = cms.InputTag( 'hltRegionalCosmicTracks' ),
    beamspot = cms.InputTag( 'hltOnlineBeamSpot' ),
    copyExtras = cms.untracked.bool( False ),
    copyTrajectories = cms.untracked.bool( False ),
    keepAllTracks = cms.bool( False ),
    chi2n_par = cms.double( 10.0 ),
    max_d0 = cms.double( 999.0 ),
    max_z0 = cms.double( 999.0 ),
    min_pt = cms.double( 5.0 ),
    max_eta = cms.double( 2.0 ),
    min_nHit = cms.uint32( 6 ),
    min_nPixelHit = cms.uint32( 0 ),
    minNumberLayers = cms.uint32( 0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    maxNumberLostLayers = cms.uint32( 999 ),
    qualityBit = cms.string( "" )
)
process.hltCsc2DRecHits = cms.EDProducer( "CSCRecHitDProducer",
    CSCUseCalibrations = cms.bool( True ),
    CSCUseStaticPedestals = cms.bool( False ),
    CSCUseTimingCorrections = cms.bool( True ),
    stripDigiTag = cms.InputTag( 'hltMuonCSCDigis', 'MuonCSCStripDigi' ),
    wireDigiTag = cms.InputTag( 'hltMuonCSCDigis', 'MuonCSCWireDigi' ),
    CSCstripWireDeltaTime = cms.int32( 8 ),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32( 2 ),
    CSCStripPeakThreshold = cms.double( 10.0 ),
    CSCStripClusterChargeCut = cms.double( 25.0 ),
    CSCWireClusterDeltaT = cms.int32( 1 ),
    CSCStripxtalksOffset = cms.double( 0.03 ),
    NoiseLevel_ME1a = cms.double( 7.0 ),
    XTasymmetry_ME1a = cms.double( 0.0 ),
    ConstSyst_ME1a = cms.double( 0.022 ),
    NoiseLevel_ME1b = cms.double( 8.0 ),
    XTasymmetry_ME1b = cms.double( 0.0 ),
    ConstSyst_ME1b = cms.double( 0.007 ),
    NoiseLevel_ME12 = cms.double( 9.0 ),
    XTasymmetry_ME12 = cms.double( 0.0 ),
    ConstSyst_ME12 = cms.double( 0.0 ),
    NoiseLevel_ME13 = cms.double( 8.0 ),
    XTasymmetry_ME13 = cms.double( 0.0 ),
    ConstSyst_ME13 = cms.double( 0.0 ),
    NoiseLevel_ME21 = cms.double( 9.0 ),
    XTasymmetry_ME21 = cms.double( 0.0 ),
    ConstSyst_ME21 = cms.double( 0.0 ),
    NoiseLevel_ME22 = cms.double( 9.0 ),
    XTasymmetry_ME22 = cms.double( 0.0 ),
    ConstSyst_ME22 = cms.double( 0.0 ),
    NoiseLevel_ME31 = cms.double( 9.0 ),
    XTasymmetry_ME31 = cms.double( 0.0 ),
    ConstSyst_ME31 = cms.double( 0.0 ),
    NoiseLevel_ME32 = cms.double( 9.0 ),
    XTasymmetry_ME32 = cms.double( 0.0 ),
    ConstSyst_ME32 = cms.double( 0.0 ),
    NoiseLevel_ME41 = cms.double( 9.0 ),
    XTasymmetry_ME41 = cms.double( 0.0 ),
    ConstSyst_ME41 = cms.double( 0.0 ),
    readBadChannels = cms.bool( True ),
    readBadChambers = cms.bool( True ),
    UseAverageTime = cms.bool( False ),
    UseParabolaFit = cms.bool( False ),
    UseFivePoleFit = cms.bool( True )
)
process.hltCscSegments = cms.EDProducer( "CSCSegmentProducer",
    inputObjects = cms.InputTag( 'hltCsc2DRecHits' ),
    algo_type = cms.int32( 1 ),
    algo_psets = cms.VPSet(
      cms.PSet(
        chamber_types = cms.vstring( "ME1/a",
           "ME1/b",
           "ME1/2",
           "ME1/3",
           "ME2/1",
           "ME2/2",
           "ME3/1",
           "ME3/2",
           "ME4/1",
           "ME4/2" ),
        algo_name = cms.string( "CSCSegAlgoST" ),
        parameters_per_chamber_type = cms.vint32( 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 )
      )
    )
)
process.hltCtfActivityWithMaterialTracks = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( True ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    src = cms.InputTag( 'hltCkfActivityTrackCandidates' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltCtfL1IsoWithMaterialTracks = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( True ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    src = cms.InputTag( 'hltCkfL1IsoTrackCandidates' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltCtfL1NonIsoWithMaterialTracks = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    src = cms.InputTag( 'hltCkfL1NonIsoTrackCandidates' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltDQMHLTScalers = cms.EDAnalyzer( "HLTScalers",
    dqmFolder = cms.untracked.string( "HLT/HLTScalers_EvF" ),
    triggerResults = cms.InputTag( 'TriggerResults', '', 'HLT' ),
    MonitorDaemon = cms.untracked.bool( False )
)
process.hltDQML1Scalers = cms.EDAnalyzer( "L1Scalers",
    verbose = cms.untracked.bool( False ),
    l1GtData = cms.InputTag( 'hltGtDigis' ),
    denomIsTech = cms.untracked.bool( True ),
    denomBit = cms.untracked.uint32( 40 ),
    tfIsTech = cms.untracked.bool( True ),
    tfBit = cms.untracked.uint32( 41 ),
    dqmFolder = cms.untracked.string( "L1T/L1Scalers_EvF" ),
    firstFED = cms.untracked.uint32( 0 ),
    lastFED = cms.untracked.uint32( 931 ),
    fedRawData = cms.InputTag( 'source' ),
    HFRecHitCollection = cms.InputTag( 'hltHfreco' ),
    algoMonitorBits = cms.untracked.vuint32(  ),
    techMonitorBits = cms.untracked.vuint32(  ),
    maskedChannels = cms.untracked.vint32( 8137, 8141, 8146, 8149, 8150, 8153 )
)
process.hltDQML1SeedLogicScalers = cms.EDAnalyzer( "HLTSeedL1LogicScalers",
    l1BeforeMask = cms.bool( False ),
    processname = cms.string( "HLT" ),
    L1GtDaqReadoutRecordInputTag = cms.InputTag( 'hltGtDigis' ),
    L1GtRecordInputTag = cms.InputTag( 'unused' ),
    DQMFolder = cms.untracked.string( "HLT/HLTSeedL1LogicScalers_EvF" ),
    monitorPaths = cms.untracked.vstring( "HLT_L1MuOpen",
       "HLT_L1Mu",
       "HLT_Mu3",
       "HLT_L1SingleForJet",
       "HLT_SingleLooseIsoTau20",
       "HLT_MinBiasEcal" )
)
process.hltDTDQMEvF = cms.EDProducer( "DTUnpackingModule",
    dataType = cms.string( "DDU" ),
    fedbyType = cms.bool( False ),
    inputLabel = cms.InputTag( 'source' ),
    useStandardFEDid = cms.bool( True ),
    minFEDid = cms.untracked.int32( 770 ),
    maxFEDid = cms.untracked.int32( 779 ),
    dqmOnly = cms.bool( True ),
    rosParameters = cms.PSet(  ),
    readOutParameters = cms.PSet(
      debug = cms.untracked.bool( False ),
      rosParameters = cms.PSet(
        writeSC = cms.untracked.bool( True ),
        readingDDU = cms.untracked.bool( True ),
        dduID = cms.untracked.int32( None ),
        performDataIntegrityMonitor = cms.untracked.bool( True ),
        readDDUIDfromDDU = cms.untracked.bool( True ),
        debug = cms.untracked.bool( False ),
        localDAQ = cms.untracked.bool( False )
      ),
      performDataIntegrityMonitor = cms.untracked.bool( True ),
      localDAQ = cms.untracked.bool( False ),
      debugMode = cms.untracked.bool( None )
    )
)
process.hltDTROMonitorFilter = cms.HLTFilter( "HLTDTROMonitorFilter",
    inputLabel = cms.InputTag( 'source' )
)
process.hltDiJet30Central = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 30.0 ),
    MaxEta = cms.double( 2.6 ),
    MinN = cms.int32( 2 )
)
process.hltDiJet60 = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 60.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 2 )
)
process.hltDiJetAve100U = cms.HLTFilter( "HLTDiJetAveFilter",
    inputJetTag = cms.InputTag( 'hltJetIDPassedAK5Jets' ),
    saveTag = cms.untracked.bool( False ),
    minPtAve = cms.double( 100.0 ),
    minPtJet3 = cms.double( 99999.0 ),
    minDphi = cms.double( 0.0 )
)
process.hltDiJetAve140U = cms.HLTFilter( "HLTDiJetAveFilter",
    inputJetTag = cms.InputTag( 'hltJetIDPassedAK5Jets' ),
    saveTag = cms.untracked.bool( False ),
    minPtAve = cms.double( 140.0 ),
    minPtJet3 = cms.double( 99999.0 ),
    minDphi = cms.double( 0.0 )
)
process.hltDiJetAve15U = cms.HLTFilter( "HLTDiJetAveFilter",
    inputJetTag = cms.InputTag( 'hltJetIDPassedAK5Jets' ),
    saveTag = cms.untracked.bool( False ),
    minPtAve = cms.double( 15.0 ),
    minPtJet3 = cms.double( 99999.0 ),
    minDphi = cms.double( 0.0 )
)
process.hltDiJetAve180U = cms.HLTFilter( "HLTDiJetAveFilter",
    inputJetTag = cms.InputTag( 'hltJetIDPassedAK5Jets' ),
    saveTag = cms.untracked.bool( False ),
    minPtAve = cms.double( 180.0 ),
    minPtJet3 = cms.double( 99999.0 ),
    minDphi = cms.double( 0.0 )
)
process.hltDiJetAve300U = cms.HLTFilter( "HLTDiJetAveFilter",
    inputJetTag = cms.InputTag( 'hltJetIDPassedAK5Jets' ),
    saveTag = cms.untracked.bool( False ),
    minPtAve = cms.double( 300.0 ),
    minPtJet3 = cms.double( 99999.0 ),
    minDphi = cms.double( 0.0 )
)
process.hltDiJetAve30U = cms.HLTFilter( "HLTDiJetAveFilter",
    inputJetTag = cms.InputTag( 'hltJetIDPassedAK5Jets' ),
    saveTag = cms.untracked.bool( False ),
    minPtAve = cms.double( 30.0 ),
    minPtJet3 = cms.double( 99999.0 ),
    minDphi = cms.double( 0.0 )
)
process.hltDiJetAve50U = cms.HLTFilter( "HLTDiJetAveFilter",
    inputJetTag = cms.InputTag( 'hltJetIDPassedAK5Jets' ),
    saveTag = cms.untracked.bool( False ),
    minPtAve = cms.double( 50.0 ),
    minPtJet3 = cms.double( 99999.0 ),
    minDphi = cms.double( 0.0 )
)
process.hltDiJetAve70U = cms.HLTFilter( "HLTDiJetAveFilter",
    inputJetTag = cms.InputTag( 'hltJetIDPassedAK5Jets' ),
    saveTag = cms.untracked.bool( False ),
    minPtAve = cms.double( 70.0 ),
    minPtJet3 = cms.double( 99999.0 ),
    minDphi = cms.double( 0.0 )
)
process.hltDiMuon3L2PreFiltered0 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1DoubleMuon3L1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 0.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltDiMuonL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1DoubleMu0' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltDiMuonL2PreFiltered0 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltDiMuonL1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 0.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltDiMuonL2PreFiltered2 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltDiMuonL1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 2.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltDiMuonL3PreFiltered3 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltDiMuonL2PreFiltered0' ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltDiMuonL3PreFiltered3Onia = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltDiMuonL2PreFiltered2' ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltDiMuonL3PreFiltered4 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL2DoubleMu3L2Filtered' ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 4.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltDiMuonL3PreFiltered6 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltDiMuon3L2PreFiltered0' ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 6.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltDiMuonL3PreFiltered7 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltDiMuon3L2PreFiltered0' ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 7.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltDijet100PT100 = cms.HLTFilter( "HLTMhtHtFilter",
    inputJetTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    minMht = cms.double( 0.0 ),
    minNJet = cms.int32( 0 ),
    mode = cms.int32( 3 ),
    usePt = cms.bool( False ),
    minPT12 = cms.double( 100.0 ),
    minMeff = cms.double( 0.0 ),
    minHt = cms.double( 0.0 ),
    minMht2Ht = cms.double( 0.0 ),
    minPtJet = cms.vdouble(  100, 100  ),
    etaJet = cms.vdouble(  9999, 9999  )
)
process.hltDijet130PT130 = cms.HLTFilter( "HLTMhtHtFilter",
    inputJetTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    minMht = cms.double( 0.0 ),
    minNJet = cms.int32( 0 ),
    mode = cms.int32( 3 ),
    usePt = cms.bool( False ),
    minPT12 = cms.double( 130.0 ),
    minMeff = cms.double( 0.0 ),
    minHt = cms.double( 0.0 ),
    minMht2Ht = cms.double( 0.0 ),
    minPtJet = cms.vdouble(  130, 130  ),
    etaJet = cms.vdouble(  9999, 9999  )
)
process.hltDijet70PT70 = cms.HLTFilter( "HLTMhtHtFilter",
    inputJetTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    minMht = cms.double( 0.0 ),
    minNJet = cms.int32( 0 ),
    mode = cms.int32( 3 ),
    usePt = cms.bool( False ),
    minPT12 = cms.double( 70.0 ),
    minMeff = cms.double( 0.0 ),
    minHt = cms.double( 0.0 ),
    minMht2Ht = cms.double( 0.0 ),
    minPtJet = cms.vdouble(  70, 70  ),
    etaJet = cms.vdouble(  9999, 9999  )
)
process.hltDoubleEG15EtFilterL1Mu3EG5 = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1Mu3EG5' ),
    etcutEB = cms.double( 15.0 ),
    etcutEE = cms.double( 15.0 ),
    ncandcut = cms.int32( 2 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltDoubleEG8EtFilterL1DoubleEG5HTT50 = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1DoubleEG5HTT50' ),
    etcutEB = cms.double( 8.0 ),
    etcutEE = cms.double( 8.0 ),
    ncandcut = cms.int32( 2 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltDoubleEG8EtFilterUnseeded = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEcalActivitySuperClusterWrapper' ),
    etcutEB = cms.double( 8.0 ),
    etcutEE = cms.double( 8.0 ),
    ncandcut = cms.int32( 2 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltDoubleEG8NoCandPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTNonIsoMu5DoubleEle8NoCandHEFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltActivityStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltDoubleIsoEG17EtFilterUnseeded = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEcalActivitySuperClusterWrapper' ),
    etcutEB = cms.double( 17.0 ),
    etcutEE = cms.double( 17.0 ),
    ncandcut = cms.int32( 2 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltDoubleIsoEG18EtFilterUnseeded = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEcalActivitySuperClusterWrapper' ),
    etcutEB = cms.double( 18.0 ),
    etcutEE = cms.double( 18.0 ),
    ncandcut = cms.int32( 2 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltDoubleIsoEG18HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoubleIsoEG18R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltDoubleIsoEG18HELastFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoubleIsoEG18R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltDoubleIsoEG18R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoubleIsoEG18EtFilterUnseeded' ),
    isoTag = cms.InputTag( 'hltUnseededR9shape' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltDoubleIsoEG26EtFilterUnseeded = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEcalActivitySuperClusterWrapper' ),
    etcutEB = cms.double( 26.0 ),
    etcutEE = cms.double( 26.0 ),
    ncandcut = cms.int32( 2 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltDoubleIsoEG26R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoubleIsoEG26EtFilterUnseeded' ),
    isoTag = cms.InputTag( 'hltUnseededR9shape' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltDoubleIsoEG33EtFilterUnseededTight = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEcalActivitySuperClusterWrapper' ),
    etcutEB = cms.double( 33.0 ),
    etcutEE = cms.double( 33.0 ),
    ncandcut = cms.int32( 2 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltDoubleJet30ForwardBackward = cms.HLTFilter( "HLTForwardBackwardJetsFilter",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( False ),
    minPt = cms.double( 30.0 ),
    minEta = cms.double( 3.0 ),
    maxEta = cms.double( 5.1 )
)
process.hltDoubleJet60ForwardBackward = cms.HLTFilter( "HLTForwardBackwardJetsFilter",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( False ),
    minPt = cms.double( 60.0 ),
    minEta = cms.double( 3.0 ),
    maxEta = cms.double( 5.1 )
)
process.hltDoubleJet70ForwardBackward = cms.HLTFilter( "HLTForwardBackwardJetsFilter",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( False ),
    minPt = cms.double( 70.0 ),
    minEta = cms.double( 3.0 ),
    maxEta = cms.double( 5.1 )
)
process.hltDoubleJet80ForwardBackward = cms.HLTFilter( "HLTForwardBackwardJetsFilter",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( False ),
    minPt = cms.double( 80.0 ),
    minEta = cms.double( 3.0 ),
    maxEta = cms.double( 5.1 )
)
process.hltDoubleMu3BsL3Filtered = cms.HLTFilter( "HLTMuonDimuonL3Filter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltDiMuonL2PreFiltered2' ),
    FastAccept = cms.bool( False ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    ChargeOpt = cms.int32( -1 ),
    MinPtPair = cms.double( 0.0 ),
    MinPtMax = cms.double( 0.0 ),
    MinPtMin = cms.double( 0.0 ),
    MinInvMass = cms.double( 4.8 ),
    MaxInvMass = cms.double( 6.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxPtBalance = cms.double( 999999.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDzMuMu = cms.double( 999999.0 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltDoubleMu3JpsiL3Filtered = cms.HLTFilter( "HLTMuonDimuonL3Filter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltDiMuonL2PreFiltered2' ),
    FastAccept = cms.bool( False ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    ChargeOpt = cms.int32( -1 ),
    MinPtPair = cms.double( 0.0 ),
    MinPtMax = cms.double( 0.0 ),
    MinPtMin = cms.double( 0.0 ),
    MinInvMass = cms.double( 2.5 ),
    MaxInvMass = cms.double( 4.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxPtBalance = cms.double( 999999.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDzMuMu = cms.double( 999999.0 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltDoubleMu3QuarkoniumL3Filtered = cms.HLTFilter( "HLTMuonDimuonL3Filter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltDiMuonL2PreFiltered2' ),
    FastAccept = cms.bool( False ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    ChargeOpt = cms.int32( -1 ),
    MinPtPair = cms.double( 0.0 ),
    MinPtMax = cms.double( 0.0 ),
    MinPtMin = cms.double( 0.0 ),
    MinInvMass = cms.double( 1.5 ),
    MaxInvMass = cms.double( 14.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxAcop = cms.double( 999.0 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxPtBalance = cms.double( 999999.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDzMuMu = cms.double( 999999.0 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltDoubleMu4ExclL3PreFiltered = cms.HLTFilter( "HLTMuonDimuonL3Filter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL2DoubleMu3L2Filtered' ),
    FastAccept = cms.bool( False ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    ChargeOpt = cms.int32( -1 ),
    MinPtPair = cms.double( 0.0 ),
    MinPtMax = cms.double( 0.0 ),
    MinPtMin = cms.double( 0.0 ),
    MinInvMass = cms.double( 0.0 ),
    MaxInvMass = cms.double( 9999.0 ),
    MinAcop = cms.double( -999.0 ),
    MaxAcop = cms.double( 0.3 ),
    MinPtBalance = cms.double( -1.0 ),
    MaxPtBalance = cms.double( 999999.0 ),
    NSigmaPt = cms.double( 0.0 ),
    MaxDzMuMu = cms.double( 999999.0 ),
    MaxRapidityPair = cms.double( 999999.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltDoublePFTauTightIso20Track = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltConvPFTausTightIsoTrackFinding' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 20.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 2 )
)
process.hltDoublePFTauTightIso20Track5 = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltConvPFTausTightIsoTrackPt5' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 20.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 2 )
)
process.hltDoublePhoton33EgammaLHEDoubleFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoublePhoton33EgammaR9ShapeDoubleFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltDoublePhoton33EgammaR9ShapeDoubleFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoubleIsoEG33EtFilterUnseededTight' ),
    isoTag = cms.InputTag( 'hltUnseededR9shape' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltDoublePhoton5IsoVLEgammaEcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltDoublePhoton5IsoVLEgammaHEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonEcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 6.0 ),
    thrRegularEE = cms.double( 6.0 ),
    thrOverEEB = cms.double( 0.012 ),
    thrOverEEE = cms.double( 0.012 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltDoublePhoton5IsoVLEgammaHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoublePhoton5IsoVLEtPhiFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.15 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltDoublePhoton5IsoVLEgammaHcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltDoublePhoton5IsoVLEgammaEcalIsolFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 4.0 ),
    thrRegularEE = cms.double( 4.0 ),
    thrOverEEB = cms.double( 0.005 ),
    thrOverEEE = cms.double( 0.005 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltDoublePhoton5IsoVLEgammaTrackIsolFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltDoublePhoton5IsoVLEgammaHcalIsolFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHollowTrackIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHollowTrackIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 4.0 ),
    thrRegularEE = cms.double( 4.0 ),
    thrOverEEB = cms.double( 0.002 ),
    thrOverEEE = cms.double( 0.002 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltDoublePhoton5IsoVLEtPhiFilter = cms.HLTFilter( "HLTEgammaDoubleEtDeltaPhiFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1DoubleEG2FwdVeto' ),
    etcut = cms.double( 5.0 ),
    minDeltaPhi = cms.double( 2.5 ),
    saveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltDt1DRecHits = cms.EDProducer( "DTRecHitProducer",
    debug = cms.untracked.bool( False ),
    dtDigiLabel = cms.InputTag( 'hltMuonDTDigis' ),
    recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
    recAlgoConfig = cms.PSet(
      minTime = cms.double( -3.0 ),
      debug = cms.untracked.bool( False ),
      tTrigModeConfig = cms.PSet(
        vPropWire = cms.double( 24.4 ),
        doTOFCorrection = cms.bool( True ),
        tofCorrType = cms.int32( 0 ),
        wirePropCorrType = cms.int32( 0 ),
        tTrigLabel = cms.string( "" ),
        doWirePropCorrection = cms.bool( True ),
        doT0Correction = cms.bool( True ),
        debug = cms.untracked.bool( False )
      ),
      maxTime = cms.double( 420.0 ),
      tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
      stepTwoFromDigi = cms.bool( False ),
      doVdriftCorr = cms.bool( False )
    )
)
process.hltDt4DSegments = cms.EDProducer( "DTRecSegment4DProducer",
    debug = cms.untracked.bool( False ),
    recHits1DLabel = cms.InputTag( 'hltDt1DRecHits' ),
    recHits2DLabel = cms.InputTag( 'dt2DSegments' ),
    Reco4DAlgoName = cms.string( "DTCombinatorialPatternReco4D" ),
    Reco4DAlgoConfig = cms.PSet(
      segmCleanerMode = cms.int32( 2 ),
      Reco2DAlgoName = cms.string( "DTCombinatorialPatternReco" ),
      recAlgoConfig = cms.PSet(
        minTime = cms.double( -3.0 ),
        debug = cms.untracked.bool( False ),
        tTrigModeConfig = cms.PSet(
          vPropWire = cms.double( 24.4 ),
          doTOFCorrection = cms.bool( True ),
          tofCorrType = cms.int32( 0 ),
          wirePropCorrType = cms.int32( 0 ),
          tTrigLabel = cms.string( "" ),
          doWirePropCorrection = cms.bool( True ),
          doT0Correction = cms.bool( True ),
          debug = cms.untracked.bool( False )
        ),
        maxTime = cms.double( 420.0 ),
        tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
        stepTwoFromDigi = cms.bool( False ),
        doVdriftCorr = cms.bool( False )
      ),
      nSharedHitsMax = cms.int32( 2 ),
      hit_afterT0_resolution = cms.double( 0.03 ),
      Reco2DAlgoConfig = cms.PSet(
        segmCleanerMode = cms.int32( 2 ),
        recAlgoConfig = cms.PSet(
          minTime = cms.double( -3.0 ),
          debug = cms.untracked.bool( False ),
          tTrigModeConfig = cms.PSet(
            vPropWire = cms.double( 24.4 ),
            doTOFCorrection = cms.bool( True ),
            tofCorrType = cms.int32( 0 ),
            wirePropCorrType = cms.int32( 0 ),
            tTrigLabel = cms.string( "" ),
            doWirePropCorrection = cms.bool( True ),
            doT0Correction = cms.bool( True ),
            debug = cms.untracked.bool( False )
          ),
          maxTime = cms.double( 420.0 ),
          tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
          stepTwoFromDigi = cms.bool( False ),
          doVdriftCorr = cms.bool( False )
        ),
        nSharedHitsMax = cms.int32( 2 ),
        AlphaMaxPhi = cms.double( 1.0 ),
        hit_afterT0_resolution = cms.double( 0.03 ),
        MaxAllowedHits = cms.uint32( 50 ),
        performT0_vdriftSegCorrection = cms.bool( False ),
        AlphaMaxTheta = cms.double( 0.9 ),
        debug = cms.untracked.bool( False ),
        recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
        nUnSharedHitsMin = cms.int32( 2 ),
        performT0SegCorrection = cms.bool( False )
      ),
      performT0_vdriftSegCorrection = cms.bool( False ),
      debug = cms.untracked.bool( False ),
      recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
      nUnSharedHitsMin = cms.int32( 2 ),
      AllDTRecHits = cms.bool( True ),
      performT0SegCorrection = cms.bool( False )
    )
)
process.hltDynAlCaDTErrors = cms.HLTFilter( "HLTDynamicPrescaler" )
process.hltEBHltTask = cms.EDAnalyzer( "EBHltTask",
    prefixME = cms.untracked.string( "EcalBarrel" ),
    folderName = cms.untracked.string( "FEDIntegrity_EvF" ),
    enableCleanup = cms.untracked.bool( False ),
    mergeRuns = cms.untracked.bool( False ),
    EBDetIdCollection0 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityDCCSizeErrors' ),
    EBDetIdCollection1 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityGainErrors' ),
    EBDetIdCollection2 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityChIdErrors' ),
    EBDetIdCollection3 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityGainSwitchErrors' ),
    EcalElectronicsIdCollection1 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityTTIdErrors' ),
    EcalElectronicsIdCollection2 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityBlockSizeErrors' ),
    EcalElectronicsIdCollection3 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityMemTtIdErrors' ),
    EcalElectronicsIdCollection4 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityMemBlockSizeErrors' ),
    EcalElectronicsIdCollection5 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityMemChIdErrors' ),
    EcalElectronicsIdCollection6 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityMemGainErrors' ),
    FEDRawDataCollection = cms.InputTag( 'source' )
)
process.hltEEHltTask = cms.EDAnalyzer( "EEHltTask",
    prefixME = cms.untracked.string( "EcalEndcap" ),
    folderName = cms.untracked.string( "FEDIntegrity_EvF" ),
    enableCleanup = cms.untracked.bool( False ),
    mergeRuns = cms.untracked.bool( False ),
    EEDetIdCollection0 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityDCCSizeErrors' ),
    EEDetIdCollection1 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityGainErrors' ),
    EEDetIdCollection2 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityChIdErrors' ),
    EEDetIdCollection3 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityGainSwitchErrors' ),
    EcalElectronicsIdCollection1 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityTTIdErrors' ),
    EcalElectronicsIdCollection2 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityBlockSizeErrors' ),
    EcalElectronicsIdCollection3 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityMemTtIdErrors' ),
    EcalElectronicsIdCollection4 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityMemBlockSizeErrors' ),
    EcalElectronicsIdCollection5 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityMemChIdErrors' ),
    EcalElectronicsIdCollection6 = cms.InputTag( 'hltEcalRawToRecHitByproductProducer', 'EcalIntegrityMemGainErrors' ),
    FEDRawDataCollection = cms.InputTag( 'source' )
)
process.hltEG10CaloIdLClusterShapeFilterEG5HTT75 = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG10R9ShapeFilterEG5HTT75' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG10CaloIdTCaloIsoVLEcalIsolFilterEG5HTT75 = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG10CaloIdLClusterShapeFilterEG5HTT75' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonEcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG10CaloIdTCaloIsoVLHEFilterEG5HTT75 = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG10CaloIdTCaloIsoVLEcalIsolFilterEG5HTT75' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.1 ),
    thrOverEEE = cms.double( 0.075 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG10CaloIdTCaloIsoVLHcalIsolFilterEG5HTT75 = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG10CaloIdTCaloIsoVLHEFilterEG5HTT75' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG10CaloIdTCaloIsoVLPixelMatchFilterEG5HTT75 = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEG10CaloIdTCaloIsoVLHcalIsolFilterEG5HTT75' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG10CaloIdTClusterShapeFilterEG5HTT75 = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG10R9ShapeFilterEG5HTT75' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.011 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG10EtFilterL1EG5HTT75 = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1EG5HTT75' ),
    etcutEB = cms.double( 10.0 ),
    etcutEE = cms.double( 10.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG10EtFilterL1Mu3EG5 = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1Mu3EG5' ),
    etcutEB = cms.double( 10.0 ),
    etcutEE = cms.double( 10.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG10R9ShapeFilterEG5HTT75 = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG10EtFilterL1EG5HTT75' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG125EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1SingleEG20' ),
    etcutEB = cms.double( 125.0 ),
    etcutEE = cms.double( 125.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG15CaloIdTClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG15R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.011 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG15EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1SingleEG12' ),
    etcutEB = cms.double( 15.0 ),
    etcutEE = cms.double( 15.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG15R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG15EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG17CaloIdLCaloIsoVLEcalIsoFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG17CaloIdLClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonEcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG17CaloIdLCaloIsoVLHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG17CaloIdLCaloIsoVLEcalIsoFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG17CaloIdLCaloIsoVLHcalIsoFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG17CaloIdLCaloIsoVLHEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG17CaloIdLClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG17R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG17EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1SingleEG12' ),
    etcutEB = cms.double( 17.0 ),
    etcutEE = cms.double( 17.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG17EtFilterL1Mu3EG5 = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1Mu3EG5' ),
    etcutEB = cms.double( 17.0 ),
    etcutEE = cms.double( 17.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG17R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG17EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG20EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1SingleEG12' ),
    etcutEB = cms.double( 20.0 ),
    etcutEE = cms.double( 20.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG20EtFilterMu3EG5 = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1Mu3EG5' ),
    etcutEB = cms.double( 20.0 ),
    etcutEE = cms.double( 20.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG20R9ShapeAntiFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG20EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( False ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.95 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG20R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG20EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG20R9ShapeFilterMu3EG5 = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG20EtFilterMu3EG5' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG25EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1SingleEG12' ),
    etcutEB = cms.double( 25.0 ),
    etcutEE = cms.double( 25.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG26CaloIdLClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG26HEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG26CaloIdLIsoVLEcalIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltEG26CaloIdLClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonEcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 6.0 ),
    thrRegularEE = cms.double( 6.0 ),
    thrOverEEB = cms.double( 0.012 ),
    thrOverEEE = cms.double( 0.012 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG26CaloIdLIsoVLHcalIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltEG26CaloIdLIsoVLEcalIsoFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 4.0 ),
    thrRegularEE = cms.double( 4.0 ),
    thrOverEEB = cms.double( 0.005 ),
    thrOverEEE = cms.double( 0.005 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG26CaloIdLIsoVLTrackIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltEG26CaloIdLIsoVLHcalIsoFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHollowTrackIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHollowTrackIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 4.0 ),
    thrRegularEE = cms.double( 4.0 ),
    thrOverEEB = cms.double( 0.002 ),
    thrOverEEE = cms.double( 0.002 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG26EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1SingleEG12' ),
    etcutEB = cms.double( 26.0 ),
    etcutEE = cms.double( 26.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG26HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG26R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG26R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG26EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG27EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1SingleEG15' ),
    etcutEB = cms.double( 27.0 ),
    etcutEE = cms.double( 27.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG30CaloIdVLClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG30R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.024 ),
    thrRegularEE = cms.double( 0.04 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG30CaloIdVLHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG30CaloIdVLClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG30EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1SingleEG15' ),
    etcutEB = cms.double( 30.0 ),
    etcutEE = cms.double( 30.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG30R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG30EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG32CaloIdLClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG32CaloIdLHEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG32CaloIdLHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG32R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG32EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1SingleEG20' ),
    etcutEB = cms.double( 32.0 ),
    etcutEE = cms.double( 32.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG32R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG32EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG33EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1SingleEG20' ),
    etcutEB = cms.double( 33.0 ),
    etcutEE = cms.double( 33.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG33HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG33R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG33R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG33EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG45EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1SingleEG20' ),
    etcutEB = cms.double( 45.0 ),
    etcutEE = cms.double( 45.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG60CaloIdLClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG60R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG60CaloIdLHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG60CaloIdLClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG60EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1SingleEG20' ),
    etcutEB = cms.double( 60.0 ),
    etcutEE = cms.double( 60.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG60R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG60EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG70CaloIdLClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG70R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG70CaloIdLHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG70CaloIdLClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG70EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1SingleEG20' ),
    etcutEB = cms.double( 70.0 ),
    etcutEE = cms.double( 70.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG70R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG70EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG75CaloIdVLClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG75R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.024 ),
    thrRegularEE = cms.double( 0.04 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG75EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1SingleEG20' ),
    etcutEB = cms.double( 75.0 ),
    etcutEE = cms.double( 75.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG75R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG75EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG8CaloIdLClusterShapeFilterMu3EG5 = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG8EtFilterMu3EG5' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG8CaloIdLHEFilterMu3EG5 = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG8CaloIdLR9ShapeFilterMu3EG5' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG8CaloIdLPixelMatchFilterMu3EG5 = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEG8CaloIdLHEFilterMu3EG5' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG8CaloIdLR9ShapeFilterMu3EG5 = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG8CaloIdLClusterShapeFilterMu3EG5' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG8EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1SingleEG5' ),
    etcutEB = cms.double( 8.0 ),
    etcutEE = cms.double( 8.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG8EtFilterMu3EG5 = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1Mu3EG5' ),
    etcutEB = cms.double( 8.0 ),
    etcutEE = cms.double( 8.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG8EtFilterUnseeded = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEcalActivitySuperClusterWrapper' ),
    etcutEB = cms.double( 8.0 ),
    etcutEE = cms.double( 8.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltEG8HEFilterMu3EG5 = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG8R9ShapeFilterMu3EG5' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG8PixelMatchFilterMu3EG5 = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEG8HEFilterMu3EG5' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG8R9ShapeFilterMu3EG5 = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG8EtFilterMu3EG5' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEG90EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1SingleEG20' ),
    etcutEB = cms.double( 90.0 ),
    etcutEE = cms.double( 90.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEGRegionalL1DoubleEG2FwdVeto = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles', 'Isolated' ),
    candNonIsolatedTag = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles', 'NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( 'hltL1sL1DoubleEG2FwdVeto' ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
process.hltEGRegionalL1DoubleEG5HTT50 = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles', 'Isolated' ),
    candNonIsolatedTag = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles', 'NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( 'hltL1sL1DoubleEG5HTT50' ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
process.hltEGRegionalL1EG5HTT75 = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles', 'Isolated' ),
    candNonIsolatedTag = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles', 'NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( 'hltL1sL1EG5HTT75' ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
process.hltEGRegionalL1Mu3EG5 = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles', 'Isolated' ),
    candNonIsolatedTag = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles', 'NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( 'hltL1sL1Mu3EG5' ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
process.hltEGRegionalL1SingleEG12 = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles', 'Isolated' ),
    candNonIsolatedTag = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles', 'NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( 'hltL1sL1SingleEG12' ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
process.hltEGRegionalL1SingleEG15 = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles', 'Isolated' ),
    candNonIsolatedTag = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles', 'NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( 'hltL1sL1SingleEG15' ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
process.hltEGRegionalL1SingleEG20 = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles', 'Isolated' ),
    candNonIsolatedTag = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles', 'NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( 'hltL1sL1SingleEG20' ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
process.hltEGRegionalL1SingleEG5 = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles', 'Isolated' ),
    candNonIsolatedTag = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles', 'NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( 'hltL1sL1SingleEG5' ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
process.hltEGRegionalL1TripleEG5 = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
    candIsolatedTag = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles', 'Isolated' ),
    candNonIsolatedTag = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles', 'NonIsolated' ),
    L1SeedFilterTag = cms.InputTag( 'hltL1sL1TripleEG5' ),
    ncandcut = cms.int32( 3 ),
    doIsolated = cms.bool( False ),
    region_eta_size = cms.double( 0.522 ),
    region_eta_size_ecap = cms.double( 1.0 ),
    region_phi_size = cms.double( 1.044 ),
    barrel_end = cms.double( 1.4791 ),
    endcap_end = cms.double( 2.65 )
)
process.hltESFEDIntegrityTask = cms.EDAnalyzer( "ESFEDIntegrityTask",
    prefixME = cms.untracked.string( "EcalPreshower" ),
    FEDDirName = cms.untracked.string( "FEDIntegrity_EvF" ),
    enableCleanup = cms.untracked.bool( False ),
    mergeRuns = cms.untracked.bool( False ),
    debug = cms.untracked.bool( False ),
    ESDCCCollections = cms.InputTag( 'NotUsed' ),
    ESKChipCollections = cms.InputTag( 'NotUsed' ),
    FEDRawDataCollection = cms.InputTag( 'source' )
)
process.hltESRawToRecHitFacility = cms.EDProducer( "EcalRawToRecHitFacility",
    sourceTag = cms.InputTag( 'source' ),
    workerName = cms.string( "hltESPESUnpackerWorker" )
)
process.hltESRecHitAll = cms.EDProducer( "EcalRawToRecHitProducer",
    lazyGetterTag = cms.InputTag( 'hltESRawToRecHitFacility' ),
    sourceTag = cms.InputTag( 'hltEcalRegionalESRestFEDs', 'es' ),
    splitOutput = cms.bool( False ),
    EBrechitCollection = cms.string( "" ),
    EErechitCollection = cms.string( "" ),
    rechitCollection = cms.string( "EcalRecHitsES" )
)
process.hltESRegionalEgammaRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
    lazyGetterTag = cms.InputTag( 'hltESRawToRecHitFacility' ),
    sourceTag = cms.InputTag( 'hltEcalRegionalEgammaFEDs', 'es' ),
    splitOutput = cms.bool( False ),
    EBrechitCollection = cms.string( "" ),
    EErechitCollection = cms.string( "" ),
    rechitCollection = cms.string( "EcalRecHitsES" )
)
process.hltESRegionalPi0EtaRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
    lazyGetterTag = cms.InputTag( 'hltESRawToRecHitFacility' ),
    sourceTag = cms.InputTag( 'hltEcalRegionalPi0EtaFEDs', 'es' ),
    splitOutput = cms.bool( False ),
    EBrechitCollection = cms.string( "" ),
    EErechitCollection = cms.string( "" ),
    rechitCollection = cms.string( "EcalRecHitsES" )
)
process.hltEcalActivityEgammaRegionalCTFFinalFitWithMaterial = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "hltEcalActivityEgammaRegionalCTFFinalFitWithMaterial" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    src = cms.InputTag( 'hltEcalActivityEgammaRegionalCkfTrackCandidates' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltEcalActivityEgammaRegionalCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( 'hltEcalActivityEgammaRegionalPixelSeedGenerator' ),
    TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltEcalActivityEgammaRegionalPixelSeedGenerator = cms.EDProducer( "EgammaHLTRegionalPixelSeedGeneratorProducers",
    ptMin = cms.double( 1.5 ),
    vertexZ = cms.double( 0.0 ),
    originRadius = cms.double( 0.02 ),
    originHalfLength = cms.double( 15.0 ),
    deltaEtaRegion = cms.double( 0.3 ),
    deltaPhiRegion = cms.double( 0.3 ),
    candTag = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    candTagEle = cms.InputTag( 'pixelMatchElectrons' ),
    UseZInVertex = cms.bool( False ),
    BSProducer = cms.InputTag( 'hltOnlineBeamSpot' ),
    OrderedHitsFactoryPSet = cms.PSet(
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltESPPixelLayerPairs" )
    )
)
process.hltEcalActivitySuperClusterWrapper = cms.HLTFilter( "HLTEgammaTriggerFilterObjectWrapper",
    candIsolatedTag = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    candNonIsolatedTag = cms.InputTag( 'none' ),
    doIsolated = cms.bool( True )
)
process.hltEcalCalibrationRaw = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( 'source' ),
    fedList = cms.vuint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 )
)
process.hltEcalRawToRecHitByproductProducer = cms.EDProducer( "EcalRawToRecHitByproductProducer",
    workerName = cms.string( "" )
)
process.hltEcalRawToRecHitFacility = cms.EDProducer( "EcalRawToRecHitFacility",
    sourceTag = cms.InputTag( 'source' ),
    workerName = cms.string( "" )
)
process.hltEcalRecHitAll = cms.EDProducer( "EcalRawToRecHitProducer",
    lazyGetterTag = cms.InputTag( 'hltEcalRawToRecHitFacility' ),
    sourceTag = cms.InputTag( 'hltEcalRegionalRestFEDs' ),
    splitOutput = cms.bool( True ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    rechitCollection = cms.string( "NotNeededsplitOutputTrue" )
)
process.hltEcalRegionalESRestFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
    sourceTag = cms.InputTag( 'hltEcalRawToRecHitFacility' ),
    type = cms.string( "all" ),
    doES = cms.bool( True ),
    sourceTag_es = cms.InputTag( 'hltESRawToRecHitFacility' ),
    esInstance = cms.untracked.string( "es" ),
    MuJobPSet = cms.PSet(  ),
    JetJobPSet = cms.VPSet(
    ),
    EmJobPSet = cms.VPSet(
    ),
    CandJobPSet = cms.VPSet(
    )
)
process.hltEcalRegionalEgammaFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
    sourceTag = cms.InputTag( 'hltEcalRawToRecHitFacility' ),
    type = cms.string( "egamma" ),
    doES = cms.bool( True ),
    sourceTag_es = cms.InputTag( 'hltESRawToRecHitFacility' ),
    esInstance = cms.untracked.string( "es" ),
    MuJobPSet = cms.PSet(  ),
    JetJobPSet = cms.VPSet(
    ),
    EmJobPSet = cms.VPSet(
      cms.PSet(
        regionEtaMargin = cms.double( 0.25 ),
        regionPhiMargin = cms.double( 0.4 ),
        Ptmin = cms.double( 5.0 ),
        Source = cms.InputTag( 'hltL1extraParticles', 'Isolated' )
      ),
      cms.PSet(
        regionEtaMargin = cms.double( 0.25 ),
        regionPhiMargin = cms.double( 0.4 ),
        Ptmin = cms.double( 5.0 ),
        Source = cms.InputTag( 'hltL1extraParticles', 'NonIsolated' )
      )
    ),
    CandJobPSet = cms.VPSet(
    )
)
process.hltEcalRegionalEgammaRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
    lazyGetterTag = cms.InputTag( 'hltEcalRawToRecHitFacility' ),
    sourceTag = cms.InputTag( 'hltEcalRegionalEgammaFEDs' ),
    splitOutput = cms.bool( True ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    rechitCollection = cms.string( "NotNeededsplitOutputTrue" )
)
process.hltEcalRegionalJetsFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
    sourceTag = cms.InputTag( 'hltEcalRawToRecHitFacility' ),
    type = cms.string( "jet" ),
    doES = cms.bool( False ),
    sourceTag_es = cms.InputTag( 'NotNeededoESfalse' ),
    esInstance = cms.untracked.string( "es" ),
    MuJobPSet = cms.PSet(  ),
    JetJobPSet = cms.VPSet(
      cms.PSet(
        regionEtaMargin = cms.double( 1.0 ),
        regionPhiMargin = cms.double( 1.0 ),
        Ptmin = cms.double( 14.0 ),
        Source = cms.InputTag( 'hltL1extraParticles', 'Central' )
      ),
      cms.PSet(
        regionEtaMargin = cms.double( 1.0 ),
        regionPhiMargin = cms.double( 1.0 ),
        Ptmin = cms.double( 20.0 ),
        Source = cms.InputTag( 'hltL1extraParticles', 'Forward' )
      ),
      cms.PSet(
        regionEtaMargin = cms.double( 1.0 ),
        regionPhiMargin = cms.double( 1.0 ),
        Ptmin = cms.double( 14.0 ),
        Source = cms.InputTag( 'hltL1extraParticles', 'Tau' )
      )
    ),
    EmJobPSet = cms.VPSet(
    ),
    CandJobPSet = cms.VPSet(
    )
)
process.hltEcalRegionalJetsRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
    lazyGetterTag = cms.InputTag( 'hltEcalRawToRecHitFacility' ),
    sourceTag = cms.InputTag( 'hltEcalRegionalJetsFEDs' ),
    splitOutput = cms.bool( True ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    rechitCollection = cms.string( "NotNeededsplitOutputTrue" )
)
process.hltEcalRegionalMuonsFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
    sourceTag = cms.InputTag( 'hltEcalRawToRecHitFacility' ),
    type = cms.string( "candidate" ),
    doES = cms.bool( False ),
    sourceTag_es = cms.InputTag( 'NotNeededoESfalse' ),
    esInstance = cms.untracked.string( "es" ),
    MuJobPSet = cms.PSet(  ),
    JetJobPSet = cms.VPSet(
    ),
    EmJobPSet = cms.VPSet(
    ),
    CandJobPSet = cms.VPSet(
      cms.PSet(
        bePrecise = cms.bool( False ),
        propagatorNameToBePrecise = cms.string( "" ),
        epsilon = cms.double( 0.01 ),
        regionPhiMargin = cms.double( 0.3 ),
        cType = cms.string( "chargedcandidate" ),
        Source = cms.InputTag( 'hltL2MuonCandidates' ),
        Ptmin = cms.double( 0.0 ),
        regionEtaMargin = cms.double( 0.3 )
      )
    )
)
process.hltEcalRegionalMuonsRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
    lazyGetterTag = cms.InputTag( 'hltEcalRawToRecHitFacility' ),
    sourceTag = cms.InputTag( 'hltEcalRegionalMuonsFEDs' ),
    splitOutput = cms.bool( True ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    rechitCollection = cms.string( "NotNeededsplitOutputTrue" )
)
process.hltEcalRegionalPi0EtaFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
    sourceTag = cms.InputTag( 'hltEcalRawToRecHitFacility' ),
    type = cms.string( "egamma" ),
    doES = cms.bool( True ),
    sourceTag_es = cms.InputTag( 'hltESRawToRecHitFacility' ),
    esInstance = cms.untracked.string( "es" ),
    MuJobPSet = cms.PSet(  ),
    JetJobPSet = cms.VPSet(
    ),
    EmJobPSet = cms.VPSet(
      cms.PSet(
        regionEtaMargin = cms.double( 0.25 ),
        regionPhiMargin = cms.double( 0.4 ),
        Ptmin = cms.double( 2.0 ),
        Source = cms.InputTag( 'hltL1extraParticles', 'Isolated' )
      ),
      cms.PSet(
        regionEtaMargin = cms.double( 0.25 ),
        regionPhiMargin = cms.double( 0.4 ),
        Ptmin = cms.double( 2.0 ),
        Source = cms.InputTag( 'hltL1extraParticles', 'NonIsolated' )
      )
    ),
    CandJobPSet = cms.VPSet(
    )
)
process.hltEcalRegionalPi0EtaRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
    lazyGetterTag = cms.InputTag( 'hltEcalRawToRecHitFacility' ),
    sourceTag = cms.InputTag( 'hltEcalRegionalPi0EtaFEDs' ),
    splitOutput = cms.bool( True ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    rechitCollection = cms.string( "" )
)
process.hltEcalRegionalRestFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
    sourceTag = cms.InputTag( 'hltEcalRawToRecHitFacility' ),
    type = cms.string( "all" ),
    doES = cms.bool( False ),
    sourceTag_es = cms.InputTag( 'NotNeededoESfalse' ),
    esInstance = cms.untracked.string( "es" ),
    MuJobPSet = cms.PSet(  ),
    JetJobPSet = cms.VPSet(
    ),
    EmJobPSet = cms.VPSet(
    ),
    CandJobPSet = cms.VPSet(
    )
)
process.hltEle10CaloIdTTrkIdTCaloIsoVLTrkIsoVLDetaFilterEG5HTT75 = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle10CaloIdTTrkIdTCaloIsoVLTrkIsoVLOneOEMinusOneOPFilterEG5HTT75' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.008 ),
    thrRegularEE = cms.double( 0.008 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle10CaloIdTTrkIdTCaloIsoVLTrkIsoVLDphiFilterEG5HTT75 = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle10CaloIdTTrkIdTCaloIsoVLTrkIsoVLDetaFilterEG5HTT75' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.07 ),
    thrRegularEE = cms.double( 0.05 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle10CaloIdTTrkIdTCaloIsoVLTrkIsoVLOneOEMinusOneOPFilterEG5HTT75 = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( 'hltEG10CaloIdTCaloIsoVLPixelMatchFilterEG5HTT75' ),
    electronIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    electronNonIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False )
)
process.hltEle10CaloIdTTrkIdTCaloIsoVLTrkIsoVLTrackIsolFilterEG5HTT75 = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle10CaloIdTTrkIdTCaloIsoVLTrkIsoVLDphiFilterEG5HTT75' ),
    isoTag = cms.InputTag( 'hltL1IsoElectronTrackIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoElectronTrackIsol' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( 0.2 ),
    thrOverPtEE = cms.double( 0.2 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTOneOEMinusOneOPFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.008 ),
    thrRegularEE = cms.double( 0.008 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTDetaFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.07 ),
    thrRegularEE = cms.double( 0.05 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTEcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG15CaloIdTClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonEcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.125 ),
    thrOverEEE = cms.double( 0.075 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTEcalIsolFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTHcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTHEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.125 ),
    thrOverEEE = cms.double( 0.075 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( 'hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTPixelMatchFilter' ),
    electronIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    electronNonIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False )
)
process.hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTHcalIsolFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTTrackIsolFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTDphiFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoElectronTrackIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoElectronTrackIsol' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( 0.125 ),
    thrOverPtEE = cms.double( 0.075 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle15CaloIdVTTrkIdTDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle15CaloIdVTTrkIdTOneOEMinusOneOPFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.008 ),
    thrRegularEE = cms.double( 0.008 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle15CaloIdVTTrkIdTDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle15CaloIdVTTrkIdTDetaFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.07 ),
    thrRegularEE = cms.double( 0.05 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle15CaloIdVTTrkIdTHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG15CaloIdTClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle15CaloIdVTTrkIdTOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( 'hltEle15CaloIdVTTrkIdTPixelMatchFilter' ),
    electronIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    electronNonIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False )
)
process.hltEle15CaloIdVTTrkIdTPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEle15CaloIdVTTrkIdTHEFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle17CaloIdIsoEle8CaloIdIsoClusterShapeDoubleFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoubleEG8EtFilterUnseeded' ),
    isoTag = cms.InputTag( 'hltActivityPhotonClusterShape' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltEle17CaloIdIsoEle8CaloIdIsoEcalIsolDoubleFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle17CaloIdIsoEle8CaloIdIsoClusterShapeDoubleFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltEle17CaloIdIsoEle8CaloIdIsoHEDoubleFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle17CaloIdIsoEle8CaloIdIsoEcalIsolDoubleFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltEle17CaloIdIsoEle8CaloIdIsoHcalIsolDoubleFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle17CaloIdIsoEle8CaloIdIsoHEDoubleFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltEle17CaloIdIsoEle8CaloIdIsoPixelMatchDoubleFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEle17CaloIdIsoEle8CaloIdIsoHcalIsolDoubleFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltActivityStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltEle17CaloIdLCaloIsoVLPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEG17CaloIdLCaloIsoVLHcalIsoFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8ClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG17R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.011 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8DetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8OneOEMinusOneOPFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.008 ),
    thrRegularEE = cms.double( 0.008 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8DphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8DetaFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.07 ),
    thrRegularEE = cms.double( 0.05 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8EcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8ClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonEcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8HEDoubleFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoubleEG8EtFilterUnseeded' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8EcalIsolFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8HcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8HEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8OneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( 'hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8PixelMatchFilter' ),
    electronIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    electronNonIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False )
)
process.hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8PMMassFilter = cms.HLTFilter( "HLTPMMassFilter",
    candTag = cms.InputTag( 'hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8HEDoubleFilter' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    lowerMassCut = cms.double( 30.0 ),
    upperMassCut = cms.double( 999999.0 ),
    nZcandcut = cms.int32( 1 ),
    reqOppCharge = cms.untracked.bool( False ),
    isElectron1 = cms.untracked.bool( False ),
    isElectron2 = cms.untracked.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8HcalIsolFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8TrackIsolFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8DphiFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoElectronTrackIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoElectronTrackIsol' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( 0.05 ),
    thrOverPtEE = cms.double( 0.05 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle25CaloIdVTTrkIdTCentralDiJet30Cleaned = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltCleanEle25CaloIdVTTrkIdTFromAK5CorrJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 30.0 ),
    MaxEta = cms.double( 2.6 ),
    MinN = cms.int32( 2 )
)
process.hltEle25CaloIdVTTrkIdTCentralJet30Cleaned = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltCleanEle25CaloIdVTTrkIdTFromAK5CorrJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 30.0 ),
    MaxEta = cms.double( 2.6 ),
    MinN = cms.int32( 1 )
)
process.hltEle25CaloIdVTTrkIdTCentralTriJet30Cleaned = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltCleanEle25CaloIdVTTrkIdTFromAK5CorrJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 30.0 ),
    MaxEta = cms.double( 2.6 ),
    MinN = cms.int32( 3 )
)
process.hltEle25CaloIdVTTrkIdTClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle25CaloIdVTTrkIdTR9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.011 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle25CaloIdVTTrkIdTDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle25CaloIdVTTrkIdTOneOEMinusOneOPFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.008 ),
    thrRegularEE = cms.double( 0.008 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle25CaloIdVTTrkIdTDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle25CaloIdVTTrkIdTDetaFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.07 ),
    thrRegularEE = cms.double( 0.05 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle25CaloIdVTTrkIdTHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle25CaloIdVTTrkIdTClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle25CaloIdVTTrkIdTOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( 'hltEle25CaloIdVTTrkIdTPixelMatchFilter' ),
    electronIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    electronNonIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False )
)
process.hltEle25CaloIdVTTrkIdTPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEle25CaloIdVTTrkIdTHEFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle25CaloIdVTTrkIdTR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG25EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTR9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.011 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTOneOEMinusOneOPFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.008 ),
    thrRegularEE = cms.double( 0.008 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTDetaFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.07 ),
    thrRegularEE = cms.double( 0.05 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTEcalIsoFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonEcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.125 ),
    thrOverEEE = cms.double( 0.075 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTEcalIsoFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTHcalIsoFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTHEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 999999.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.125 ),
    thrOverEEE = cms.double( 0.075 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( 'hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTPixelMatchFilter' ),
    electronIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    electronNonIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False )
)
process.hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTHcalIsoFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG27EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTTrackIsoFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle27CaloIdTCaloIsoTTrkIdTTrkIsoTDphiFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoElectronTrackIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoElectronTrackIsol' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( 0.125 ),
    thrOverPtEE = cms.double( 0.075 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle32CaloIdLCaloIsoVLSC17ClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG32EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle32CaloIdLCaloIsoVLSC17EcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle32CaloIdLCaloIsoVLSC17ClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonEcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle32CaloIdLCaloIsoVLSC17HEDoubleFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoubleIsoEG17EtFilterUnseeded' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltEle32CaloIdLCaloIsoVLSC17HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle32CaloIdLCaloIsoVLSC17EcalIsolFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle32CaloIdLCaloIsoVLSC17HcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle32CaloIdLCaloIsoVLSC17HEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle32CaloIdLCaloIsoVLSC17PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEle32CaloIdLCaloIsoVLSC17HcalIsolFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle45CaloIdTTrkIdTDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle45CaloIdVTTrkIdTOneOEMinusOneOPFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.008 ),
    thrRegularEE = cms.double( 0.008 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle45CaloIdVTTrkIdTClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle45CaloIdVTTrkIdTR9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.011 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle45CaloIdVTTrkIdTDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle45CaloIdTTrkIdTDetaFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.07 ),
    thrRegularEE = cms.double( 0.05 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle45CaloIdVTTrkIdTHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle45CaloIdVTTrkIdTClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle45CaloIdVTTrkIdTOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( 'hltEle45CaloIdVTTrkIdTPixelMatchFilter' ),
    electronIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    electronNonIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False )
)
process.hltEle45CaloIdVTTrkIdTPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEle45CaloIdVTTrkIdTHEFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle45CaloIdVTTrkIdTR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG45EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle8CaloIdLCaloIsoVLClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle8R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle8CaloIdLCaloIsoVLEcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle8CaloIdLCaloIsoVLClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonEcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle8CaloIdLCaloIsoVLHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle8CaloIdLCaloIsoVLEcalIsolFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle8CaloIdLCaloIsoVLHcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle8CaloIdLCaloIsoVLHEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle8CaloIdLCaloIsoVLNoL1SeedClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle8CaloIdLCaloIsoVLNoL1SeedR9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonClusterShape' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltEle8CaloIdLCaloIsoVLNoL1SeedEcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle8CaloIdLCaloIsoVLNoL1SeedClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltEle8CaloIdLCaloIsoVLNoL1SeedHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle8CaloIdLCaloIsoVLNoL1SeedEcalIsolFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltEle8CaloIdLCaloIsoVLNoL1SeedHcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle8CaloIdLCaloIsoVLNoL1SeedHEFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltEle8CaloIdLCaloIsoVLNoL1SeedPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEle8CaloIdLCaloIsoVLNoL1SeedHcalIsolFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltActivityStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltEle8CaloIdLCaloIsoVLNoL1SeedR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG8EtFilterUnseeded' ),
    isoTag = cms.InputTag( 'hltUnseededR9shape' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.0 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltEle8CaloIdLCaloIsoVLPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEle8CaloIdLCaloIsoVLHcalIsolFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle8CaloIdLTrkIdVLDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle8CaloIdLTrkIdVLOneOEMinusOneOPFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.01 ),
    thrRegularEE = cms.double( 0.01 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle8CaloIdLTrkIdVLDetaFilterMu3EG5 = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle8CaloIdLTrkIdVLOneOEMinusOneOPFilterRegionalMu3EG5' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.01 ),
    thrRegularEE = cms.double( 0.01 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle8CaloIdLTrkIdVLDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle8CaloIdLTrkIdVLDetaFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.15 ),
    thrRegularEE = cms.double( 0.1 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle8CaloIdLTrkIdVLDphiFilterMu3EG5 = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltEle8CaloIdLTrkIdVLDetaFilterMu3EG5' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.15 ),
    thrRegularEE = cms.double( 0.1 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltEle8CaloIdLTrkIdVLHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle8CaloIdLCaloIsoVLClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle8CaloIdLTrkIdVLOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( 'hltEle8CaloIdLTrkIdVLPixelMatchFilter' ),
    electronIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    electronNonIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False )
)
process.hltEle8CaloIdLTrkIdVLOneOEMinusOneOPFilterRegionalMu3EG5 = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( 'hltEG8CaloIdLPixelMatchFilterMu3EG5' ),
    electronIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    electronNonIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False )
)
process.hltEle8CaloIdLTrkIdVLPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEle8CaloIdLTrkIdVLHEFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle8HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle8R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle8PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEle8HEFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle8R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG8EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle90NoSpikeFilterClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle90NoSpikeFilterR9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 999.0 ),
    thrRegularEE = cms.double( 999.0 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle90NoSpikeFilterHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEle90NoSpikeFilterClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle90NoSpikeFilterPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltEle90NoSpikeFilterHEFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltEle90NoSpikeFilterR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG90EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 999999.9 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltElectronActivityDetaDphi = cms.EDProducer( "EgammaHLTElectronDetaDphiProducer",
    electronProducer = cms.InputTag( 'hltPixelMatchElectronsActivity' ),
    BSProducer = cms.InputTag( 'hltOnlineBeamSpot' ),
    useTrackProjectionToEcal = cms.untracked.bool( False )
)
process.hltElectronL1IsoDetaDphi = cms.EDProducer( "EgammaHLTElectronDetaDphiProducer",
    electronProducer = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    BSProducer = cms.InputTag( 'hltOnlineBeamSpot' ),
    useTrackProjectionToEcal = cms.untracked.bool( False )
)
process.hltElectronL1NonIsoDetaDphi = cms.EDProducer( "EgammaHLTElectronDetaDphiProducer",
    electronProducer = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' ),
    BSProducer = cms.InputTag( 'hltOnlineBeamSpot' ),
    useTrackProjectionToEcal = cms.untracked.bool( False )
)
process.hltExclDiJet60HFAND = cms.HLTFilter( "HLTExclDiJetFilter",
    inputJetTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    minPtJet = cms.double( 60.0 ),
    minHFe = cms.double( 70.0 ),
    HF_OR = cms.bool( False )
)
process.hltExclDiJet60HFOR = cms.HLTFilter( "HLTExclDiJetFilter",
    inputJetTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    minPtJet = cms.double( 60.0 ),
    minHFe = cms.double( 70.0 ),
    HF_OR = cms.bool( True )
)
process.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( 'source' ),
    fedList = cms.vuint32( 1023 )
)
process.hltFilterDoubleIsoPFTau20Trk5LeadTrack5IsolationL1HLTMatched = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltL1HLTDoubleIsoPFTau20Trk5JetsMatch' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 20.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 2 )
)
process.hltFilterIsoMu12IsoPFTau10LooseIsolation = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltConvPFTausTrackFindingLooseIsolation' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 10.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltFilterL2EtCutDoublePFIsoTau20Trk5 = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltL2TauJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 20.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 2 )
)
process.hltFilterL2EtCutSingleIsoPFTau35Trk20MET45 = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltL2TauJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 35.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 1 )
)
process.hltFilterPFTauTrack5TightIsoL1QuadJet20Central = cms.EDProducer( "L1HLTJetsMatching",
    JetSrc = cms.InputTag( 'hltConvPFTausTightIsoTrackPt5Isolation' ),
    L1TauTrigger = cms.InputTag( 'hltL1sL1QuadJet20Central' ),
    EtMin = cms.double( 0.0 )
)
process.hltFilterPFTauTrack5TightIsoL1QuadJet20CentralPFTau40 = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltFilterPFTauTrack5TightIsoL1QuadJet20Central' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 40.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltFilterSingleIsoPFTau35Trk20LeadTrackPt20 = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltConvPFTauTightIsoTrackPt20' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 35.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltFilterSingleIsoPFTau35Trk20MET45LeadTrack20MET45IsolationL1HLTMatched = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltL1HLTSingleIsoPFTau35Trk20Met45JetsMatch' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 35.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltGctDigis = cms.EDProducer( "GctRawToDigi",
    inputLabel = cms.InputTag( 'source' ),
    gctFedId = cms.untracked.int32( 745 ),
    hltMode = cms.bool( True ),
    numberOfGctSamplesToUnpack = cms.uint32( 1 ),
    numberOfRctSamplesToUnpack = cms.uint32( 1 ),
    unpackSharedRegions = cms.bool( False ),
    unpackerVersion = cms.uint32( 0 ),
    checkHeaders = cms.untracked.bool( False ),
    verbose = cms.untracked.bool( False )
)
process.hltGetJetsfrom1EleCleanBJet40Central = cms.EDProducer( "GetJetsFromHLTobject",
    jets = cms.InputTag( 'hltSingleEleCleanBJet40Central' )
)
process.hltGetJetsfromBJet40Central = cms.EDProducer( "GetJetsFromHLTobject",
    jets = cms.InputTag( 'hltBJet40Central' )
)
process.hltGtDigis = cms.EDProducer( "L1GlobalTriggerRawToDigi",
    DaqGtInputTag = cms.InputTag( 'source' ),
    DaqGtFedId = cms.untracked.int32( 813 ),
    ActiveBoardsMask = cms.uint32( 65535 ),
    UnpackBxInEvent = cms.int32( 5 ),
    Verbosity = cms.untracked.int32( 0 )
)
process.hltHFAsymmetryFilter = cms.HLTFilter( "HLTHFAsymmetryFilter",
    HFHitCollection = cms.InputTag( 'hltHfreco' ),
    ECut_HF = cms.double( 3.0 ),
    OS_Asym_max = cms.double( 0.2 ),
    SS_Asym_min = cms.double( 0.8 )
)
process.hltHFEMClusters = cms.EDProducer( "HFEMClusterProducer",
    hits = cms.InputTag( 'hltHfreco' ),
    minTowerEnergy = cms.double( 4.0 ),
    seedThresholdET = cms.double( 5.0 ),
    maximumSL = cms.double( 0.98 ),
    maximumRenergy = cms.double( 50.0 ),
    usePMTFlag = cms.bool( True ),
    usePulseFlag = cms.bool( True ),
    forcePulseFlagMC = cms.bool( False ),
    correctionType = cms.int32( 1 )
)
process.hltHFEMFilter = cms.HLTFilter( "HLT1Photon",
    inputTag = cms.InputTag( 'hltHFRecoEcalCandidate' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
process.hltHFRecoEcalCandidate = cms.EDProducer( "HFRecoEcalCandidateProducer",
    hfclusters = cms.InputTag( 'hltHFEMClusters' ),
    e9e25Cut = cms.double( 0.9 ),
    intercept2DCut = cms.double( 0.2 ),
    Correct = cms.bool( True )
)
process.hltHITCkfTrackCandidatesHB = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( 'hltHITPixelTripletSeedGeneratorHB' ),
    TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltHITCkfTrackCandidatesHE = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( 'hltHITPixelTripletSeedGeneratorHE' ),
    TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltHITCtfWithMaterialTracksHB = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "hltHITCtfWithMaterialTracksHB8E29" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    src = cms.InputTag( 'hltHITCkfTrackCandidatesHB' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltHITCtfWithMaterialTracksHE = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "hltHITCtfWithMaterialTracksHE8E29" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    src = cms.InputTag( 'hltHITCkfTrackCandidatesHE' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltHITIPTCorrectorHB = cms.EDProducer( "IPTCorrector",
    corTracksLabel = cms.InputTag( 'hltHITCtfWithMaterialTracksHB' ),
    filterLabel = cms.InputTag( 'hltIsolPixelTrackL2FilterHB' ),
    associationCone = cms.double( 0.2 )
)
process.hltHITIPTCorrectorHE = cms.EDProducer( "IPTCorrector",
    corTracksLabel = cms.InputTag( 'hltHITCtfWithMaterialTracksHE' ),
    filterLabel = cms.InputTag( 'hltIsolPixelTrackL2FilterHE' ),
    associationCone = cms.double( 0.2 )
)
process.hltHITPixelTracksHB = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( False ),
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
      RegionPSet = cms.PSet(
        precise = cms.bool( True ),
        originRadius = cms.double( 0.0015 ),
        nSigmaZ = cms.double( 3.0 ),
        ptMin = cms.double( 0.7 ),
        beamSpot = cms.InputTag( 'hltOnlineBeamSpot' )
      )
    ),
    OrderedHitsFactoryPSet = cms.PSet(
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      SeedingLayers = cms.string( "hltESPPixelLayerTripletsHITHB" ),
      GeneratorPSet = cms.PSet(
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 10000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" ),
        extraHitRZtolerance = cms.double( 0.06 )
      )
    ),
    FitterPSet = cms.PSet(
      ComponentName = cms.string( "PixelFitterByConformalMappingAndLine" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      fixImpactParameter = cms.double( 0.0 )
    ),
    FilterPSet = cms.PSet(
      chi2 = cms.double( 1000.0 ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
      nSigmaInvPtTolerance = cms.double( 0.0 ),
      ptMin = cms.double( 0.7 ),
      tipMax = cms.double( 1.0 )
    ),
    CleanerPSet = cms.PSet(
      ComponentName = cms.string( "PixelTrackCleanerBySharedHits" )
    )
)
process.hltHITPixelTracksHE = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( False ),
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
      RegionPSet = cms.PSet(
        precise = cms.bool( True ),
        originRadius = cms.double( 0.0015 ),
        nSigmaZ = cms.double( 3.0 ),
        ptMin = cms.double( 0.35 ),
        beamSpot = cms.InputTag( 'hltOnlineBeamSpot' )
      )
    ),
    OrderedHitsFactoryPSet = cms.PSet(
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      SeedingLayers = cms.string( "hltESPPixelLayerTripletsHITHE" ),
      GeneratorPSet = cms.PSet(
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 10000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" ),
        extraHitRZtolerance = cms.double( 0.06 )
      )
    ),
    FitterPSet = cms.PSet(
      ComponentName = cms.string( "PixelFitterByConformalMappingAndLine" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      fixImpactParameter = cms.double( 0.0 )
    ),
    FilterPSet = cms.PSet(
      chi2 = cms.double( 1000.0 ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
      nSigmaInvPtTolerance = cms.double( 0.0 ),
      ptMin = cms.double( 0.35 ),
      tipMax = cms.double( 1.0 )
    ),
    CleanerPSet = cms.PSet(
      ComponentName = cms.string( "PixelTrackCleanerBySharedHits" )
    )
)
process.hltHITPixelTripletSeedGeneratorHB = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    ClusterCheckPSet = cms.PSet(
      PixelClusterCollectionLabel = cms.InputTag( 'hltSiPixelClusters' ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
      doClusterCheck = cms.bool( False ),
      ClusterCollectionLabel = cms.InputTag( 'hltSiStripClusters' ),
      MaxNumberOfPixelClusters = cms.uint32( 10000 )
    ),
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "HITRegionalPixelSeedGenerator" ),
      RegionPSet = cms.PSet(
        deltaEtaTrackRegion = cms.double( 0.05 ),
        useL1Jets = cms.bool( False ),
        deltaPhiTrackRegion = cms.double( 0.05 ),
        originHalfLength = cms.double( 15.0 ),
        precise = cms.bool( True ),
        deltaEtaL1JetRegion = cms.double( 0.3 ),
        useTracks = cms.bool( False ),
        originRadius = cms.double( 0.6 ),
        isoTrackSrc = cms.InputTag( 'hltIsolPixelTrackL2FilterHB' ),
        trackSrc = cms.InputTag( 'hltHITPixelTracksHB' ),
        useIsoTracks = cms.bool( True ),
        l1tjetSrc = cms.InputTag( 'hltL1extraParticles', 'Tau' ),
        deltaPhiL1JetRegion = cms.double( 0.3 ),
        ptMin = cms.double( 1.0 ),
        fixedReg = cms.bool( False ),
        etaCenter = cms.double( 0.0 ),
        phiCenter = cms.double( 0.0 ),
        originZPos = cms.double( 0.0 ),
        vertexSrc = cms.string( "hltHITPixelVerticesHB" )
      )
    ),
    OrderedHitsFactoryPSet = cms.PSet(
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      SeedingLayers = cms.string( "hltESPPixelLayerTriplets" ),
      GeneratorPSet = cms.PSet(
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 10000 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRZtolerance = cms.double( 0.06 )
      )
    ),
    SeedComparitorPSet = cms.PSet(
      ComponentName = cms.string( "none" )
    ),
    SeedCreatorPSet = cms.PSet(
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      propagator = cms.string( "PropagatorWithMaterial" )
    ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltHITPixelTripletSeedGeneratorHE = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    ClusterCheckPSet = cms.PSet(
      PixelClusterCollectionLabel = cms.InputTag( 'hltSiPixelClusters' ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
      doClusterCheck = cms.bool( False ),
      ClusterCollectionLabel = cms.InputTag( 'hltSiStripClusters' ),
      MaxNumberOfPixelClusters = cms.uint32( 10000 )
    ),
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "HITRegionalPixelSeedGenerator" ),
      RegionPSet = cms.PSet(
        deltaEtaTrackRegion = cms.double( 0.05 ),
        useL1Jets = cms.bool( False ),
        deltaPhiTrackRegion = cms.double( 0.05 ),
        originHalfLength = cms.double( 15.0 ),
        precise = cms.bool( True ),
        deltaEtaL1JetRegion = cms.double( 0.3 ),
        useTracks = cms.bool( False ),
        originRadius = cms.double( 0.6 ),
        isoTrackSrc = cms.InputTag( 'hltIsolPixelTrackL2FilterHE' ),
        trackSrc = cms.InputTag( 'hltHITPixelTracksHE' ),
        useIsoTracks = cms.bool( True ),
        l1tjetSrc = cms.InputTag( 'hltL1extraParticles', 'Tau' ),
        deltaPhiL1JetRegion = cms.double( 0.3 ),
        ptMin = cms.double( 0.5 ),
        fixedReg = cms.bool( False ),
        etaCenter = cms.double( 0.0 ),
        phiCenter = cms.double( 0.0 ),
        originZPos = cms.double( 0.0 ),
        vertexSrc = cms.string( "hltHITPixelVerticesHE" )
      )
    ),
    OrderedHitsFactoryPSet = cms.PSet(
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      SeedingLayers = cms.string( "hltESPPixelLayerTriplets" ),
      GeneratorPSet = cms.PSet(
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 10000 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRZtolerance = cms.double( 0.06 )
      )
    ),
    SeedComparitorPSet = cms.PSet(
      ComponentName = cms.string( "none" )
    ),
    SeedCreatorPSet = cms.PSet(
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      propagator = cms.string( "PropagatorWithMaterial" )
    ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltHITPixelVerticesHB = cms.EDProducer( "PixelVertexProducer",
    Verbosity = cms.int32( 0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    UseError = cms.bool( True ),
    WtAverage = cms.bool( True ),
    ZOffset = cms.double( 5.0 ),
    ZSeparation = cms.double( 0.05 ),
    NTrkMin = cms.int32( 2 ),
    PtMin = cms.double( 1.0 ),
    TrackCollection = cms.InputTag( 'hltHITPixelTracksHB' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    Method2 = cms.bool( True )
)
process.hltHITPixelVerticesHE = cms.EDProducer( "PixelVertexProducer",
    Verbosity = cms.int32( 0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    UseError = cms.bool( True ),
    WtAverage = cms.bool( True ),
    ZOffset = cms.double( 5.0 ),
    ZSeparation = cms.double( 0.05 ),
    NTrkMin = cms.int32( 2 ),
    PtMin = cms.double( 1.0 ),
    TrackCollection = cms.InputTag( 'hltHITPixelTracksHE' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    Method2 = cms.bool( True )
)
process.hltHT160 = cms.HLTFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( 'hltJet40Ht' ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 160.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
process.hltHT200 = cms.HLTFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( 'hltJet40Ht' ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 200.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
process.hltHT240 = cms.HLTFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( 'hltJet40Ht' ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 240.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
process.hltHT260 = cms.HLTFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( 'hltJet40Ht' ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 260.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
process.hltHT300 = cms.HLTFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( 'hltJet40Ht' ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 300.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
process.hltHT360 = cms.HLTFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( 'hltJet40Ht' ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 360.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
process.hltHT440 = cms.HLTFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( 'hltJet40Ht' ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 440.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
process.hltHT520 = cms.HLTFilter( "HLTGlobalSumsMET",
    inputTag = cms.InputTag( 'hltJet40Ht' ),
    saveTag = cms.untracked.bool( True ),
    observable = cms.string( "sumEt" ),
    Min = cms.double( 520.0 ),
    Max = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
process.hltHbhereco = cms.EDProducer( "HcalHitReconstructor",
    firstSample = cms.int32( 4 ),
    samplesToAdd = cms.int32( 4 ),
    correctForTimeslew = cms.bool( True ),
    correctForPhaseContainment = cms.bool( True ),
    correctionPhaseNS = cms.double( 13.0 ),
    digiLabel = cms.InputTag( 'hltHcalDigis' ),
    correctTiming = cms.bool( False ),
    setNoiseFlags = cms.bool( False ),
    setHSCPFlags = cms.bool( False ),
    setSaturationFlags = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    dropZSmarkedPassed = cms.bool( True ),
    Subdetector = cms.string( "HBHE" ),
    setTimingShapedCutsFlags = cms.bool( False ),
    digistat = cms.PSet(  ),
    HFInWindowStat = cms.PSet(  ),
    S8S1stat = cms.PSet(
      longETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      shortEnergyParams = cms.vdouble(  40, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100  ),
      flagsToSkip = cms.int32( 16 ),
      shortETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      short_optimumSlope = cms.vdouble(  0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1  ),
      longEnergyParams = cms.vdouble(  40, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100  ),
      long_optimumSlope = cms.vdouble(  0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1  ),
      isS8S1 = cms.bool( True )
    ),
    PETstat = cms.PSet(
      longETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      short_R_29 = cms.vdouble(  0.8  ),
      shortEnergyParams = cms.vdouble(  35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093  ),
      flagsToSkip = cms.int32( 0 ),
      short_R = cms.vdouble(  0.8  ),
      shortETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      long_R_29 = cms.vdouble(  0.8  ),
      longEnergyParams = cms.vdouble(  43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62  ),
      long_R = cms.vdouble(  0.98  )
    ),
    saturationParameters = cms.PSet(
      maxADCvalue = cms.int32( 127 )
    ),
    timingshapedcutsParameters = cms.PSet(
      ignorelowest = cms.bool( True ),
      win_offset = cms.double( 0.0 ),
      ignorehighest = cms.bool( False ),
      win_gain = cms.double( 1.0 ),
      tfilterEnvelope = cms.vdouble(  4, 12.04, 13, 10.56, 23.5, 8.82, 37, 7.38, 56, 6.3, 81, 5.64, 114.5, 5.44, 175.5, 5.38, 350.5, 5.14  )
    ),
    flagParameters = cms.PSet(
      nominalPedestal = cms.double( 3.0 ),
      hitMultiplicityThreshold = cms.int32( 17 ),
      hitEnergyMinimum = cms.double( 1.0 )
    ),
    hscpParameters = cms.PSet(
      slopeMax = cms.double( -0.6 ),
      r1Max = cms.double( 1.0 ),
      r1Min = cms.double( 0.15 ),
      TimingEnergyThreshold = cms.double( 30.0 ),
      slopeMin = cms.double( -1.5 ),
      outerMin = cms.double( 0.0 ),
      outerMax = cms.double( 0.1 ),
      fracLeaderMin = cms.double( 0.4 ),
      r2Min = cms.double( 0.1 ),
      r2Max = cms.double( 0.5 ),
      fracLeaderMax = cms.double( 0.7 )
    ),
    pulseShapeParameters = cms.PSet(
      MinimumChargeThreshold = cms.double( None ),
      TrianglePeakTS = cms.uint32( 4 ),
      RMS8MaxThreshold = cms.vdouble(    ),
      LinearThreshold = cms.vdouble(    ),
      LeftSlopeCut = cms.vdouble(    ),
      LinearCut = cms.vdouble(    ),
      LeftSlopeThreshold = cms.vdouble(    ),
      RightSlopeThreshold = cms.vdouble(    ),
      RightSlopeCut = cms.vdouble(    ),
      RMS8MaxCut = cms.vdouble(    ),
      RightSlopeSmallThreshold = cms.vdouble(    ),
      UseDualFit = cms.bool( None ),
      RightSlopeSmallCut = cms.vdouble(    ),
      TriangleIgnoreSlow = cms.bool( None )
    ),
    hfTimingTrustParameters = cms.PSet(
      hfTimingTrustLevel2 = cms.int32( 4 ),
      hfTimingTrustLevel1 = cms.int32( 1 )
    ),
    S9S1stat = cms.PSet(
      longETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      shortEnergyParams = cms.vdouble(  35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093  ),
      flagsToSkip = cms.int32( 24 ),
      shortETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      short_optimumSlope = cms.vdouble(  -99999, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927  ),
      longEnergyParams = cms.vdouble(  43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62  ),
      long_optimumSlope = cms.vdouble(  -99999, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927  ),
      isS8S1 = cms.bool( False )
    ),
    firstAuxOffset = cms.int32( 0 ),
    firstAuxTS = cms.int32( 4 ),
    tsFromDB = cms.bool( True )
)
process.hltHcalCalibTypeFilter = cms.HLTFilter( "HLTHcalCalibTypeFilter",
    InputTag = cms.InputTag( 'source' ),
    FilterSummary = cms.untracked.bool( False ),
    CalibTypes = cms.vint32( 1, 2, 3, 4, 5, 6 )
)
process.hltHcalDigis = cms.EDProducer( "HcalRawToDigi",
    InputLabel = cms.InputTag( 'source' ),
    HcalFirstFED = cms.untracked.int32( None ),
    UnpackCalib = cms.untracked.bool( True ),
    UnpackZDC = cms.untracked.bool( True ),
    UnpackTTP = cms.untracked.bool( False ),
    silent = cms.untracked.bool( True ),
    ComplainEmptyData = cms.untracked.bool( False ),
    ExpectedOrbitMessageTime = cms.untracked.int32( None ),
    FEDs = cms.untracked.vint32(  ),
    firstSample = cms.int32( 0 ),
    lastSample = cms.int32( 9 ),
    FilterDataQuality = cms.bool( True )
)
process.hltHcalTowerFilter = cms.HLTFilter( "HLTHcalTowerFilter",
    inputTag = cms.InputTag( 'hltTowerMakerForHcal' ),
    saveTag = cms.untracked.bool( False ),
    MinE_HB = cms.double( 1.5 ),
    MinE_HE = cms.double( 2.5 ),
    MinE_HF = cms.double( 9.0 ),
    MaxN_HB = cms.int32( 2 ),
    MaxN_HE = cms.int32( 2 ),
    MaxN_HF = cms.int32( 8 )
)
process.hltHfreco = cms.EDProducer( "HcalHitReconstructor",
    firstSample = cms.int32( 4 ),
    samplesToAdd = cms.int32( 2 ),
    correctForTimeslew = cms.bool( False ),
    correctForPhaseContainment = cms.bool( False ),
    correctionPhaseNS = cms.double( 0.0 ),
    digiLabel = cms.InputTag( 'hltHcalDigis' ),
    correctTiming = cms.bool( False ),
    setNoiseFlags = cms.bool( False ),
    setHSCPFlags = cms.bool( False ),
    setSaturationFlags = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    dropZSmarkedPassed = cms.bool( True ),
    Subdetector = cms.string( "HF" ),
    setTimingShapedCutsFlags = cms.bool( False ),
    digistat = cms.PSet(
      HFdigiflagFirstSample = cms.int32( 3 ),
      HFdigiflagMinEthreshold = cms.double( 40.0 ),
      HFdigiflagSamplesToAdd = cms.int32( 4 ),
      HFdigiflagCoef0 = cms.double( 0.93 ),
      HFdigiflagCoef2 = cms.double( -0.012667 ),
      HFdigiflagCoef1 = cms.double( -0.38275 ),
      HFdigiflagExpectedPeak = cms.int32( 4 )
    ),
    HFInWindowStat = cms.PSet(
      hflongEthresh = cms.double( 40.0 ),
      hflongMinWindowTime = cms.vdouble(  -10  ),
      hfshortEthresh = cms.double( 40.0 ),
      hflongMaxWindowTime = cms.vdouble(  10  ),
      hfshortMaxWindowTime = cms.vdouble(  10  ),
      hfshortMinWindowTime = cms.vdouble(  -12  )
    ),
    S8S1stat = cms.PSet(
      longETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      shortEnergyParams = cms.vdouble(  40, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100  ),
      flagsToSkip = cms.int32( 16 ),
      shortETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      short_optimumSlope = cms.vdouble(  0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1  ),
      longEnergyParams = cms.vdouble(  40, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100  ),
      long_optimumSlope = cms.vdouble(  0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1  ),
      isS8S1 = cms.bool( True )
    ),
    PETstat = cms.PSet(
      longETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      short_R_29 = cms.vdouble(  0.8  ),
      shortEnergyParams = cms.vdouble(  35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093  ),
      flagsToSkip = cms.int32( 0 ),
      short_R = cms.vdouble(  0.8  ),
      shortETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      long_R_29 = cms.vdouble(  0.8  ),
      longEnergyParams = cms.vdouble(  43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62  ),
      long_R = cms.vdouble(  0.98  )
    ),
    saturationParameters = cms.PSet(
      maxADCvalue = cms.int32( 127 )
    ),
    timingshapedcutsParameters = cms.PSet(
      ignorelowest = cms.bool( True ),
      win_offset = cms.double( 0.0 ),
      ignorehighest = cms.bool( False ),
      win_gain = cms.double( 1.0 ),
      tfilterEnvelope = cms.vdouble(  4, 12.04, 13, 10.56, 23.5, 8.82, 37, 7.38, 56, 6.3, 81, 5.64, 114.5, 5.44, 175.5, 5.38, 350.5, 5.14  )
    ),
    flagParameters = cms.PSet(
      nominalPedestal = cms.double( 3.0 ),
      hitMultiplicityThreshold = cms.int32( 17 ),
      hitEnergyMinimum = cms.double( 1.0 )
    ),
    hscpParameters = cms.PSet(
      slopeMax = cms.double( -0.6 ),
      r1Max = cms.double( 1.0 ),
      r1Min = cms.double( 0.15 ),
      TimingEnergyThreshold = cms.double( 30.0 ),
      slopeMin = cms.double( -1.5 ),
      outerMin = cms.double( 0.0 ),
      outerMax = cms.double( 0.1 ),
      fracLeaderMin = cms.double( 0.4 ),
      r2Min = cms.double( 0.1 ),
      r2Max = cms.double( 0.5 ),
      fracLeaderMax = cms.double( 0.7 )
    ),
    pulseShapeParameters = cms.PSet(
      MinimumChargeThreshold = cms.double( None ),
      TrianglePeakTS = cms.uint32( 4 ),
      RMS8MaxThreshold = cms.vdouble(    ),
      LinearThreshold = cms.vdouble(    ),
      LeftSlopeCut = cms.vdouble(    ),
      LinearCut = cms.vdouble(    ),
      LeftSlopeThreshold = cms.vdouble(    ),
      RightSlopeThreshold = cms.vdouble(    ),
      RightSlopeCut = cms.vdouble(    ),
      RMS8MaxCut = cms.vdouble(    ),
      RightSlopeSmallThreshold = cms.vdouble(    ),
      UseDualFit = cms.bool( None ),
      RightSlopeSmallCut = cms.vdouble(    ),
      TriangleIgnoreSlow = cms.bool( None )
    ),
    hfTimingTrustParameters = cms.PSet(
      hfTimingTrustLevel2 = cms.int32( 4 ),
      hfTimingTrustLevel1 = cms.int32( 1 )
    ),
    S9S1stat = cms.PSet(
      longETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      shortEnergyParams = cms.vdouble(  35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093  ),
      flagsToSkip = cms.int32( 24 ),
      shortETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      short_optimumSlope = cms.vdouble(  -99999, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927  ),
      longEnergyParams = cms.vdouble(  43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62  ),
      long_optimumSlope = cms.vdouble(  -99999, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927  ),
      isS8S1 = cms.bool( False )
    ),
    firstAuxOffset = cms.int32( 0 ),
    firstAuxTS = cms.int32( 4 ),
    tsFromDB = cms.bool( True )
)
process.hltHoreco = cms.EDProducer( "HcalHitReconstructor",
    firstSample = cms.int32( 4 ),
    samplesToAdd = cms.int32( 4 ),
    correctForTimeslew = cms.bool( True ),
    correctForPhaseContainment = cms.bool( True ),
    correctionPhaseNS = cms.double( 13.0 ),
    digiLabel = cms.InputTag( 'hltHcalDigis' ),
    correctTiming = cms.bool( False ),
    setNoiseFlags = cms.bool( False ),
    setHSCPFlags = cms.bool( False ),
    setSaturationFlags = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    setPulseShapeFlags = cms.bool( False ),
    dropZSmarkedPassed = cms.bool( True ),
    Subdetector = cms.string( "HO" ),
    setTimingShapedCutsFlags = cms.bool( False ),
    digistat = cms.PSet(  ),
    HFInWindowStat = cms.PSet(  ),
    S8S1stat = cms.PSet(
      longETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      shortEnergyParams = cms.vdouble(  40, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100  ),
      flagsToSkip = cms.int32( 16 ),
      shortETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      short_optimumSlope = cms.vdouble(  0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1  ),
      longEnergyParams = cms.vdouble(  40, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100  ),
      long_optimumSlope = cms.vdouble(  0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1  ),
      isS8S1 = cms.bool( True )
    ),
    PETstat = cms.PSet(
      longETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      short_R_29 = cms.vdouble(  0.8  ),
      shortEnergyParams = cms.vdouble(  35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093  ),
      flagsToSkip = cms.int32( 0 ),
      short_R = cms.vdouble(  0.8  ),
      shortETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      long_R_29 = cms.vdouble(  0.8  ),
      longEnergyParams = cms.vdouble(  43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62  ),
      long_R = cms.vdouble(  0.98  )
    ),
    saturationParameters = cms.PSet(
      maxADCvalue = cms.int32( 127 )
    ),
    timingshapedcutsParameters = cms.PSet(
      ignorelowest = cms.bool( True ),
      win_offset = cms.double( 0.0 ),
      ignorehighest = cms.bool( False ),
      win_gain = cms.double( 1.0 ),
      tfilterEnvelope = cms.vdouble(  4, 12.04, 13, 10.56, 23.5, 8.82, 37, 7.38, 56, 6.3, 81, 5.64, 114.5, 5.44, 175.5, 5.38, 350.5, 5.14  )
    ),
    flagParameters = cms.PSet(
      nominalPedestal = cms.double( 3.0 ),
      hitMultiplicityThreshold = cms.int32( 17 ),
      hitEnergyMinimum = cms.double( 1.0 )
    ),
    hscpParameters = cms.PSet(
      slopeMax = cms.double( -0.6 ),
      r1Max = cms.double( 1.0 ),
      r1Min = cms.double( 0.15 ),
      TimingEnergyThreshold = cms.double( 30.0 ),
      slopeMin = cms.double( -1.5 ),
      outerMin = cms.double( 0.0 ),
      outerMax = cms.double( 0.1 ),
      fracLeaderMin = cms.double( 0.4 ),
      r2Min = cms.double( 0.1 ),
      r2Max = cms.double( 0.5 ),
      fracLeaderMax = cms.double( 0.7 )
    ),
    pulseShapeParameters = cms.PSet(
      MinimumChargeThreshold = cms.double( None ),
      TrianglePeakTS = cms.uint32( 4 ),
      RMS8MaxThreshold = cms.vdouble(    ),
      LinearThreshold = cms.vdouble(    ),
      LeftSlopeCut = cms.vdouble(    ),
      LinearCut = cms.vdouble(    ),
      LeftSlopeThreshold = cms.vdouble(    ),
      RightSlopeThreshold = cms.vdouble(    ),
      RightSlopeCut = cms.vdouble(    ),
      RMS8MaxCut = cms.vdouble(    ),
      RightSlopeSmallThreshold = cms.vdouble(    ),
      UseDualFit = cms.bool( None ),
      RightSlopeSmallCut = cms.vdouble(    ),
      TriangleIgnoreSlow = cms.bool( None )
    ),
    hfTimingTrustParameters = cms.PSet(
      hfTimingTrustLevel2 = cms.int32( 4 ),
      hfTimingTrustLevel1 = cms.int32( 1 )
    ),
    S9S1stat = cms.PSet(
      longETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      shortEnergyParams = cms.vdouble(  35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093  ),
      flagsToSkip = cms.int32( 24 ),
      shortETParams = cms.vdouble(  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ),
      short_optimumSlope = cms.vdouble(  -99999, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927  ),
      longEnergyParams = cms.vdouble(  43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62  ),
      long_optimumSlope = cms.vdouble(  -99999, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927  ),
      isS8S1 = cms.bool( False )
    ),
    firstAuxOffset = cms.int32( 0 ),
    firstAuxTS = cms.int32( 4 ),
    tsFromDB = cms.bool( True )
)
process.hltHybridSuperClustersActivity = cms.EDProducer( "HybridClusterProducer",
    debugLevel = cms.string( "ERROR" ),
    basicclusterCollection = cms.string( "hybridBarrelBasicClusters" ),
    superclusterCollection = cms.string( "" ),
    ecalhitproducer = cms.string( "hltEcalRecHitAll" ),
    ecalhitcollection = cms.string( "EcalRecHitsEB" ),
    HybridBarrelSeedThr = cms.double( 1.0 ),
    step = cms.int32( 17 ),
    ethresh = cms.double( 0.1 ),
    eseed = cms.double( 0.35 ),
    ewing = cms.double( 0.0 ),
    dynamicEThresh = cms.bool( False ),
    eThreshA = cms.double( 0.003 ),
    eThreshB = cms.double( 0.1 ),
    excludeFlagged = cms.bool( False ),
    dynamicPhiRoad = cms.bool( False ),
    RecHitFlagToBeExcluded = cms.vint32(  ),
    RecHitSeverityToBeExcluded = cms.vint32( 999 ),
    posCalcParameters = cms.PSet(
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    bremRecoveryPset = cms.PSet(  ),
    severitySpikeId = cms.int32( 2 ),
    severitySpikeThreshold = cms.double( 0.95 ),
    severityRecHitThreshold = cms.double( 4.0 )
)
process.hltHybridSuperClustersL1Isolated = cms.EDProducer( "EgammaHLTHybridClusterProducer",
    debugLevel = cms.string( "INFO" ),
    basicclusterCollection = cms.string( "" ),
    superclusterCollection = cms.string( "" ),
    ecalhitproducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit' ),
    ecalhitcollection = cms.string( "EcalRecHitsEB" ),
    l1TagIsolated = cms.InputTag( 'hltL1extraParticles', 'Isolated' ),
    l1TagNonIsolated = cms.InputTag( 'hltL1extraParticles', 'NonIsolated' ),
    doIsolated = cms.bool( True ),
    l1LowerThr = cms.double( 5.0 ),
    l1UpperThr = cms.double( 999.0 ),
    l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
    regionEtaMargin = cms.double( 0.14 ),
    regionPhiMargin = cms.double( 0.4 ),
    HybridBarrelSeedThr = cms.double( 1.5 ),
    step = cms.int32( 17 ),
    ethresh = cms.double( 0.1 ),
    eseed = cms.double( 0.35 ),
    ewing = cms.double( 0.0 ),
    dynamicEThresh = cms.bool( False ),
    eThreshA = cms.double( 0.003 ),
    eThreshB = cms.double( 0.1 ),
    severityRecHitThreshold = cms.double( 4.0 ),
    severitySpikeId = cms.int32( 2 ),
    severitySpikeThreshold = cms.double( 0.95 ),
    excludeFlagged = cms.bool( False ),
    dynamicPhiRoad = cms.bool( False ),
    RecHitFlagToBeExcluded = cms.vint32(  ),
    RecHitSeverityToBeExcluded = cms.vint32( 999 ),
    posCalcParameters = cms.PSet(
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    bremRecoveryPset = cms.PSet(  )
)
process.hltHybridSuperClustersL1NonIsolated = cms.EDProducer( "EgammaHLTHybridClusterProducer",
    debugLevel = cms.string( "INFO" ),
    basicclusterCollection = cms.string( "" ),
    superclusterCollection = cms.string( "" ),
    ecalhitproducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit' ),
    ecalhitcollection = cms.string( "EcalRecHitsEB" ),
    l1TagIsolated = cms.InputTag( 'hltL1extraParticles', 'Isolated' ),
    l1TagNonIsolated = cms.InputTag( 'hltL1extraParticles', 'NonIsolated' ),
    doIsolated = cms.bool( False ),
    l1LowerThr = cms.double( 5.0 ),
    l1UpperThr = cms.double( 999.0 ),
    l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
    regionEtaMargin = cms.double( 0.14 ),
    regionPhiMargin = cms.double( 0.4 ),
    HybridBarrelSeedThr = cms.double( 1.5 ),
    step = cms.int32( 17 ),
    ethresh = cms.double( 0.1 ),
    eseed = cms.double( 0.35 ),
    ewing = cms.double( 0.0 ),
    dynamicEThresh = cms.bool( False ),
    eThreshA = cms.double( 0.003 ),
    eThreshB = cms.double( 0.1 ),
    severityRecHitThreshold = cms.double( 4.0 ),
    severitySpikeId = cms.int32( 2 ),
    severitySpikeThreshold = cms.double( 0.95 ),
    excludeFlagged = cms.bool( False ),
    dynamicPhiRoad = cms.bool( False ),
    RecHitFlagToBeExcluded = cms.vint32(  ),
    RecHitSeverityToBeExcluded = cms.vint32( 999 ),
    posCalcParameters = cms.PSet(
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    ),
    bremRecoveryPset = cms.PSet(  )
)
process.hltIconeCentral1Regional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.2 ),
    src = cms.InputTag( 'hltCaloTowersCentral1Regional' ),
    srcPVs = cms.InputTag( 'offlinePrimaryVertices' ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
process.hltIconeCentral2Regional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.2 ),
    src = cms.InputTag( 'hltCaloTowersCentral2Regional' ),
    srcPVs = cms.InputTag( 'offlinePrimaryVertices' ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
process.hltIconeCentral3Regional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.2 ),
    src = cms.InputTag( 'hltCaloTowersCentral3Regional' ),
    srcPVs = cms.InputTag( 'offlinePrimaryVertices' ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
process.hltIconeCentral4Regional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.2 ),
    src = cms.InputTag( 'hltCaloTowersCentral4Regional' ),
    srcPVs = cms.InputTag( 'offlinePrimaryVertices' ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
process.hltIconeTau1Regional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.2 ),
    src = cms.InputTag( 'hltCaloTowersTau1Regional' ),
    srcPVs = cms.InputTag( 'offlinePrimaryVertices' ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
process.hltIconeTau2Regional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.2 ),
    src = cms.InputTag( 'hltCaloTowersTau2Regional' ),
    srcPVs = cms.InputTag( 'offlinePrimaryVertices' ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
process.hltIconeTau3Regional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.2 ),
    src = cms.InputTag( 'hltCaloTowersTau3Regional' ),
    srcPVs = cms.InputTag( 'offlinePrimaryVertices' ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
process.hltIconeTau4Regional = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.2 ),
    src = cms.InputTag( 'hltCaloTowersTau4Regional' ),
    srcPVs = cms.InputTag( 'offlinePrimaryVertices' ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
process.hltIsoMu17CenJet40L3Filtered17 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltIsoMu7CenJet40L2IsoFiltered7' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 17.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( False )
)
process.hltIsoMu17CenJet40L3IsoFiltered17 = cms.HLTFilter( "HLTMuonIsoFilter",
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltIsoMu17CenJet40L3Filtered17' ),
    MinN = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( True ),
    DepTag = cms.VInputTag( 'hltL3MuonIsolations' ),
    IsolatorPSet = cms.PSet(
      ComponentName = cms.string( "" )
    )
)
process.hltIsoMu7CenJet40L2IsoFiltered7 = cms.HLTFilter( "HLTMuonIsoFilter",
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL2Muon7' ),
    MinN = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    DepTag = cms.VInputTag( 'hltL2MuonIsolations' ),
    IsolatorPSet = cms.PSet(
      ComponentName = cms.string( "" )
    )
)
process.hltIsolPixelTrackL2FilterHB = cms.HLTFilter( "HLTPixelIsolTrackFilter",
    candTag = cms.InputTag( 'hltIsolPixelTrackProdHB' ),
    L1GTSeedLabel = cms.InputTag( 'hltL1sL1SingleJet52' ),
    MinDeltaPtL1Jet = cms.double( -40000.0 ),
    MinPtTrack = cms.double( 3.5 ),
    MaxPtNearby = cms.double( 2.0 ),
    MaxEtaTrack = cms.double( 1.15 ),
    MinEtaTrack = cms.double( 0.0 ),
    filterTrackEnergy = cms.bool( True ),
    MinEnergyTrack = cms.double( 8.0 ),
    NMaxTrackCandidates = cms.int32( 10 ),
    DropMultiL2Event = cms.bool( False )
)
process.hltIsolPixelTrackL2FilterHE = cms.HLTFilter( "HLTPixelIsolTrackFilter",
    candTag = cms.InputTag( 'hltIsolPixelTrackProdHE' ),
    L1GTSeedLabel = cms.InputTag( 'hltL1sL1SingleJet52' ),
    MinDeltaPtL1Jet = cms.double( -40000.0 ),
    MinPtTrack = cms.double( 3.5 ),
    MaxPtNearby = cms.double( 2.0 ),
    MaxEtaTrack = cms.double( 2.2 ),
    MinEtaTrack = cms.double( 1.1 ),
    filterTrackEnergy = cms.bool( True ),
    MinEnergyTrack = cms.double( 12.0 ),
    NMaxTrackCandidates = cms.int32( 5 ),
    DropMultiL2Event = cms.bool( False )
)
process.hltIsolPixelTrackL3FilterHB = cms.HLTFilter( "HLTPixelIsolTrackFilter",
    candTag = cms.InputTag( 'hltHITIPTCorrectorHB' ),
    L1GTSeedLabel = cms.InputTag( 'hltL1sL1SingleJet52' ),
    MinDeltaPtL1Jet = cms.double( 4.0 ),
    MinPtTrack = cms.double( 20.0 ),
    MaxPtNearby = cms.double( 2.0 ),
    MaxEtaTrack = cms.double( 1.15 ),
    MinEtaTrack = cms.double( 0.0 ),
    filterTrackEnergy = cms.bool( True ),
    MinEnergyTrack = cms.double( 38.0 ),
    NMaxTrackCandidates = cms.int32( 999 ),
    DropMultiL2Event = cms.bool( False )
)
process.hltIsolPixelTrackL3FilterHE = cms.HLTFilter( "HLTPixelIsolTrackFilter",
    candTag = cms.InputTag( 'hltHITIPTCorrectorHE' ),
    L1GTSeedLabel = cms.InputTag( 'hltL1sL1SingleJet52' ),
    MinDeltaPtL1Jet = cms.double( 4.0 ),
    MinPtTrack = cms.double( 20.0 ),
    MaxPtNearby = cms.double( 2.0 ),
    MaxEtaTrack = cms.double( 2.2 ),
    MinEtaTrack = cms.double( 1.1 ),
    filterTrackEnergy = cms.bool( True ),
    MinEnergyTrack = cms.double( 38.0 ),
    NMaxTrackCandidates = cms.int32( 999 ),
    DropMultiL2Event = cms.bool( False )
)
process.hltIsolPixelTrackProdHB = cms.EDProducer( "IsolatedPixelTrackCandidateProducer",
    L1eTauJetsSource = cms.InputTag( 'hltL1extraParticles', 'Tau' ),
    tauAssociationCone = cms.double( 0.0 ),
    tauUnbiasCone = cms.double( 1.2 ),
    ExtrapolationConeSize = cms.double( 1.0 ),
    PixelIsolationConeSizeAtEC = cms.double( 40.0 ),
    L1GTSeedLabel = cms.InputTag( 'hltL1sL1SingleJet52' ),
    MaxVtxDXYSeed = cms.double( 101.0 ),
    MaxVtxDXYIsol = cms.double( 101.0 ),
    VertexLabel = cms.InputTag( 'hltHITPixelVerticesHB' ),
    MagFieldRecordName = cms.string( "VolumeBasedMagneticField" ),
    minPTrack = cms.double( 5.0 ),
    maxPTrackForIsolation = cms.double( 3.0 ),
    EBEtaBoundary = cms.double( 1.479 ),
    PixelTracksSources = cms.VInputTag( 'hltHITPixelTracksHB' )
)
process.hltIsolPixelTrackProdHE = cms.EDProducer( "IsolatedPixelTrackCandidateProducer",
    L1eTauJetsSource = cms.InputTag( 'hltL1extraParticles', 'Tau' ),
    tauAssociationCone = cms.double( 0.0 ),
    tauUnbiasCone = cms.double( 1.2 ),
    ExtrapolationConeSize = cms.double( 1.0 ),
    PixelIsolationConeSizeAtEC = cms.double( 40.0 ),
    L1GTSeedLabel = cms.InputTag( 'hltL1sL1SingleJet52' ),
    MaxVtxDXYSeed = cms.double( 101.0 ),
    MaxVtxDXYIsol = cms.double( 101.0 ),
    VertexLabel = cms.InputTag( 'hltHITPixelVerticesHE' ),
    MagFieldRecordName = cms.string( "VolumeBasedMagneticField" ),
    minPTrack = cms.double( 5.0 ),
    maxPTrackForIsolation = cms.double( 3.0 ),
    EBEtaBoundary = cms.double( 1.479 ),
    PixelTracksSources = cms.VInputTag( 'hltHITPixelTracksHB, hltHITPixelTracksHE' )
)
process.hltJet30Central = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 30.0 ),
    MaxEta = cms.double( 2.6 ),
    MinN = cms.int32( 1 )
)
process.hltJet40 = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( False ),
    MinPt = cms.double( 40.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
process.hltJet40Ele8CaloIdLCaloIsoVLRemoved = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CaloJetsEle8CaloIdLCaloIsoVLRemoved' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 40.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
process.hltJet40Ht = cms.EDProducer( "METProducer",
    src = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    InputType = cms.string( "CaloJetCollection" ),
    METType = cms.string( "MET" ),
    alias = cms.string( "HTMET" ),
    globalThreshold = cms.double( 40.0 ),
    noHF = cms.bool( True ),
    calculateSignificance = cms.bool( False ),
    onlyFiducialParticles = cms.bool( False ),
    usePt = cms.untracked.bool( False ),
    jets = cms.InputTag( 'unused' ),
    rf_type = cms.int32( 0 ),
    correctShowerTracks = cms.bool( False ),
    HO_EtResPar = cms.vdouble(  0, 1.3, 0.005  ),
    HF_EtResPar = cms.vdouble(  0, 1.82, 0.09  ),
    HB_PhiResPar = cms.vdouble(  0.02511  ),
    HE_PhiResPar = cms.vdouble(  0.02511  ),
    EE_EtResPar = cms.vdouble(  0.2, 0.03, 0.005  ),
    EB_PhiResPar = cms.vdouble(  0.00502  ),
    EE_PhiResPar = cms.vdouble(  0.02511  ),
    HB_EtResPar = cms.vdouble(  0, 1.22, 0.05  ),
    EB_EtResPar = cms.vdouble(  0.2, 0.03, 0.005  ),
    HF_PhiResPar = cms.vdouble(  0.05022  ),
    HE_EtResPar = cms.vdouble(  0, 1.3, 0.05  ),
    HO_PhiResPar = cms.vdouble(  0.02511  )
)
process.hltJetIDPassedAK5Jets = cms.EDProducer( "HLTJetIDProducer",
    jetsInput = cms.InputTag( 'hltAntiKT5CaloJets' ),
    min_EMF = cms.double( 1e-06 ),
    max_EMF = cms.double( 999.0 ),
    min_N90 = cms.int32( 2 )
)
process.hltJetIDPassedCorrJets = cms.EDProducer( "HLTJetIDProducer",
    jetsInput = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    min_EMF = cms.double( 1e-06 ),
    max_EMF = cms.double( 999.0 ),
    min_N90 = cms.int32( 2 )
)
process.hltJetIDPassedJetsRegional = cms.EDProducer( "HLTJetIDProducer",
    jetsInput = cms.InputTag( 'hltL1MatchedJetsRegional' ),
    min_EMF = cms.double( 1e-06 ),
    max_EMF = cms.double( 999.0 ),
    min_N90 = cms.int32( 2 )
)
process.hltL1BeamHaloAntiCoincidence3BX = cms.HLTFilter( "HLTLevel1Activity",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    daqPartitions = cms.uint32( 1 ),
    ignoreL1Mask = cms.bool( True ),
    invert = cms.bool( True ),
    physicsLoBits = cms.uint64( 0x40000000000000 ),
    physicsHiBits = cms.uint64( 0x0 ),
    technicalBits = cms.uint64( 0x0 ),
    bunchCrossings = cms.vint32( 0, 1, -1 )
)
process.hltL1DoubleMu3L1TriMuFiltered3 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1DoubleMu3' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 3.0 ),
    MinN = cms.int32( 3 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1DoubleMu3L2TriMuFiltered3 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1DoubleMu3L1TriMuFiltered3' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 3 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1DoubleMu3L3TriMuFiltered5 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1DoubleMu3L2TriMuFiltered3' ),
    MinN = cms.int32( 3 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1DoubleMuon3L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1DoubleMu3' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1DoubleMuon3L1Filtered3 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1DoubleMu3' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 3.0 ),
    MinN = cms.int32( 2 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( True ),
    SelectQualities = cms.vint32(  )
)
process.hltL1EventNumberNZS = cms.HLTFilter( "HLTL1NumberFilter",
    rawInput = cms.InputTag( 'source' ),
    period = cms.uint32( 4096 ),
    invert = cms.bool( False )
)
process.hltL1GtObjectMap = cms.EDProducer( "L1GlobalTrigger",
    GmtInputTag = cms.InputTag( 'hltGtDigis' ),
    GctInputTag = cms.InputTag( 'hltGctDigis' ),
    CastorInputTag = cms.InputTag( 'castorL1Digis' ),
    ProduceL1GtDaqRecord = cms.bool( False ),
    ProduceL1GtEvmRecord = cms.bool( False ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    WritePsbL1GtDaqRecord = cms.bool( False ),
    ReadTechnicalTriggerRecords = cms.bool( True ),
    EmulateBxInEvent = cms.int32( 1 ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    AlternativeNrBxBoardEvm = cms.uint32( 0 ),
    BstLengthBytes = cms.int32( -1 ),
    Verbosity = cms.untracked.int32( 0 ),
    TechnicalTriggersInputTags = cms.VInputTag( 'simBscDigis' ),
    RecordLength = cms.vint32( 3, 0 )
)
process.hltL1HLTDoubleIsoPFTau20Trk5JetsMatch = cms.EDProducer( "L1HLTJetsMatching",
    JetSrc = cms.InputTag( 'hltConvPFTausTightIsoTrackPt5Isolation' ),
    L1TauTrigger = cms.InputTag( 'hltL1sDoubleIsoTau20Trk5' ),
    EtMin = cms.double( 0.0 )
)
process.hltL1HLTSingleIsoPFTau35Trk20Met45JetsMatch = cms.EDProducer( "L1HLTJetsMatching",
    JetSrc = cms.InputTag( 'hltConvPFTauTightIsoTrackPt20Isolation' ),
    L1TauTrigger = cms.InputTag( 'hltL1sSingleIsoTau35Trk20MET45' ),
    EtMin = cms.double( 0.0 )
)
process.hltL1IsoEgammaRegionalCTFFinalFitWithMaterial = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "hltEgammaRegionalCTFFinalFitWithMaterial" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    src = cms.InputTag( 'hltL1IsoEgammaRegionalCkfTrackCandidates' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltL1IsoEgammaRegionalCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( 'hltL1IsoEgammaRegionalPixelSeedGenerator' ),
    TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltL1IsoEgammaRegionalPixelSeedGenerator = cms.EDProducer( "EgammaHLTRegionalPixelSeedGeneratorProducers",
    ptMin = cms.double( 1.5 ),
    vertexZ = cms.double( 0.0 ),
    originRadius = cms.double( 0.02 ),
    originHalfLength = cms.double( 15.0 ),
    deltaEtaRegion = cms.double( 0.3 ),
    deltaPhiRegion = cms.double( 0.3 ),
    candTag = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    candTagEle = cms.InputTag( 'pixelMatchElectrons' ),
    UseZInVertex = cms.bool( False ),
    BSProducer = cms.InputTag( 'hltOnlineBeamSpot' ),
    OrderedHitsFactoryPSet = cms.PSet(
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltESPPixelLayerPairs" )
    )
)
process.hltL1IsoElectronTrackIsol = cms.EDProducer( "EgammaHLTElectronTrackIsolationProducers",
    electronProducer = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    trackProducer = cms.InputTag( 'hltL1IsoEgammaRegionalCTFFinalFitWithMaterial' ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoConeSize = cms.double( 0.3 ),
    egTrkIsoZSpan = cms.double( 0.15 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSize = cms.double( 0.03 ),
    egCheckForOtherEleInCone = cms.untracked.bool( False ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    egTrkIsoStripEndcap = cms.double( 0.03 )
)
process.hltL1IsoHLTClusterShape = cms.EDProducer( "EgammaHLTClusterShapeProducer",
    recoEcalCandidateProducer = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    ecalRechitEB = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEE' ),
    isIeta = cms.bool( True )
)
process.hltL1IsoR9ID = cms.EDProducer( "EgammaHLTR9IDProducer",
    recoEcalCandidateProducer = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    ecalRechitEB = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEE' )
)
process.hltL1IsoR9shape = cms.EDProducer( "EgammaHLTR9Producer",
    recoEcalCandidateProducer = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    ecalRechitEB = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEE' ),
    useSwissCross = cms.bool( False )
)
process.hltL1IsoRecoEcalCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scHybridBarrelProducer = cms.InputTag( 'hltCorrectedHybridSuperClustersL1Isolated' ),
    scIslandEndcapProducer = cms.InputTag( 'hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated' ),
    recoEcalCandidateCollection = cms.string( "" )
)
process.hltL1IsoStartUpElectronPixelSeeds = cms.EDProducer( "ElectronSeedProducer",
    barrelSuperClusters = cms.InputTag( 'hltCorrectedHybridSuperClustersL1Isolated' ),
    endcapSuperClusters = cms.InputTag( 'hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated' ),
    SeedConfiguration = cms.PSet(
      searchInTIDTEC = cms.bool( True ),
      HighPtThreshold = cms.double( 35.0 ),
      r2MinF = cms.double( -0.15 ),
      OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32( 0 ),
        ComponentName = cms.string( "StandardHitPairGenerator" ),
        SeedingLayers = cms.string( "hltESPMixedLayerPairs" ),
        useOnDemandTracker = cms.untracked.int32( 0 )
      ),
      DeltaPhi1Low = cms.double( 0.23 ),
      DeltaPhi1High = cms.double( 0.08 ),
      ePhiMin1 = cms.double( -0.08 ),
      PhiMin2 = cms.double( -0.004 ),
      LowPtThreshold = cms.double( 3.0 ),
      hcalTowers = cms.InputTag( 'towerMaker' ),
      RegionPSet = cms.PSet(
        deltaPhiRegion = cms.double( 0.4 ),
        originHalfLength = cms.double( 15.0 ),
        useZInVertex = cms.bool( True ),
        deltaEtaRegion = cms.double( 0.1 ),
        ptMin = cms.double( 1.5 ),
        originRadius = cms.double( 0.2 ),
        VertexProducer = cms.InputTag( 'dummyVertices' )
      ),
      hOverEPtMin = cms.double( None ),
      maxHOverE = cms.double( 999999.0 ),
      maxHOverEBarrel = cms.double( None ),
      maxHOverEEndcaps = cms.double( None ),
      dynamicPhiRoad = cms.bool( False ),
      ePhiMax1 = cms.double( 0.04 ),
      maxHBarrel = cms.double( None ),
      maxHEndcaps = cms.double( None ),
      DeltaPhi2 = cms.double( 0.004 ),
      measurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      SizeWindowENeg = cms.double( 0.675 ),
      nSigmasDeltaZ1 = cms.double( 5.0 ),
      rMaxI = cms.double( 0.2 ),
      PhiMax2 = cms.double( 0.004 ),
      preFilteredSeeds = cms.bool( True ),
      r2MaxF = cms.double( 0.15 ),
      pPhiMin1 = cms.double( -0.04 ),
      useRecoVertex = cms.bool( None ),
      initialSeeds = cms.InputTag( 'noSeedsHere' ),
      vertices = cms.InputTag( None ),
      pPhiMax1 = cms.double( 0.08 ),
      deltaZ1WithVertex = cms.double( None ),
      hbheModule = cms.string( "hbhereco" ),
      SCEtCut = cms.double( 3.0 ),
      DeltaPhi2B = cms.double( None ),
      z2MaxB = cms.double( 0.09 ),
      DeltaPhi2F = cms.double( None ),
      fromTrackerSeeds = cms.bool( True ),
      hcalRecHits = cms.InputTag( 'hltHbhereco' ),
      PhiMin2B = cms.double( None ),
      z2MinB = cms.double( -0.09 ),
      hbheInstance = cms.string( "" ),
      PhiMin2F = cms.double( None ),
      rMinI = cms.double( -0.2 ),
      hOverEConeSize = cms.double( 0.0 ),
      PhiMax2B = cms.double( None ),
      PhiMax2F = cms.double( None ),
      hOverEHBMinE = cms.double( 999999.0 ),
      beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
      applyHOverECut = cms.bool( False ),
      hOverEHFMinE = cms.double( 999999.0 )
    )
)
process.hltL1IsolatedPhotonEcalIsol = cms.EDProducer( "EgammaHLTEcalRecIsolationProducer",
    recoEcalCandidateProducer = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    ecalBarrelRecHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit' ),
    ecalBarrelRecHitCollection = cms.InputTag( 'EcalRecHitsEB' ),
    ecalEndcapRecHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit' ),
    ecalEndcapRecHitCollection = cms.InputTag( 'EcalRecHitsEE' ),
    etMinBarrel = cms.double( -9999.0 ),
    eMinBarrel = cms.double( 0.08 ),
    etMinEndcap = cms.double( 0.1 ),
    eMinEndcap = cms.double( -9999.0 ),
    intRadiusBarrel = cms.double( 3.0 ),
    intRadiusEndcap = cms.double( 3.0 ),
    extRadius = cms.double( 0.3 ),
    jurassicWidth = cms.double( 3.0 ),
    useIsolEt = cms.bool( True ),
    tryBoth = cms.bool( True ),
    subtract = cms.bool( False ),
    useNumCrystals = cms.bool( True )
)
process.hltL1IsolatedPhotonHcalForHE = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    hbheRecHitProducer = cms.InputTag( 'hltHbhereco' ),
    eMinHB = cms.double( 0.7 ),
    eMinHE = cms.double( 0.8 ),
    etMinHB = cms.double( -1.0 ),
    etMinHE = cms.double( -1.0 ),
    innerCone = cms.double( 0.0 ),
    outerCone = cms.double( 0.14 ),
    depth = cms.int32( -1 ),
    doEtSum = cms.bool( False )
)
process.hltL1IsolatedPhotonHcalIsol = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    hbheRecHitProducer = cms.InputTag( 'hltHbhereco' ),
    eMinHB = cms.double( 0.7 ),
    eMinHE = cms.double( 0.8 ),
    etMinHB = cms.double( -1.0 ),
    etMinHE = cms.double( -1.0 ),
    innerCone = cms.double( 0.16 ),
    outerCone = cms.double( 0.29 ),
    depth = cms.int32( -1 ),
    doEtSum = cms.bool( True )
)
process.hltL1IsolatedPhotonHollowTrackIsol = cms.EDProducer( "EgammaHLTPhotonTrackIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    trackProducer = cms.InputTag( 'hltL1IsoEgammaRegionalCTFFinalFitWithMaterial' ),
    countTracks = cms.bool( False ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoConeSize = cms.double( 0.29 ),
    egTrkIsoZSpan = cms.double( 999999.0 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSize = cms.double( 0.06 ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    egTrkIsoStripEndcap = cms.double( 0.03 )
)
process.hltL1MatchedJetsRegional = cms.EDProducer( "HLTJetL1MatchProducer",
    jetsInput = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJetsRegional' ),
    L1TauJets = cms.InputTag( 'hltL1extraParticles', 'Tau' ),
    L1CenJets = cms.InputTag( 'hltL1extraParticles', 'Central' ),
    L1ForJets = cms.InputTag( 'hltL1extraParticles', 'Forward' ),
    DeltaR = cms.double( 0.5 )
)
process.hltL1Mu0HTT50L1DiMuFiltered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1Mu0HTT50' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1Mu0HTT50L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1Mu0HTT50' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1Mu0HTT50L1MuFiltered3 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1Mu0HTT50' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 3.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1Mu0HTT50L1MuFiltered5 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1Mu0HTT50' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 5.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1Mu0HTT50L2DiMuFiltered0 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu0HTT50L1DiMuFiltered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 0.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1Mu0HTT50L2Filtered0 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu0HTT50L1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 0.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1Mu0HTT50L2MuFiltered3 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu0HTT50L1MuFiltered3' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1Mu0HTT50L2MuFiltered5 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu0HTT50L1MuFiltered5' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1Mu0HTT50L3DiMuFiltered3 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu0HTT50L2DiMuFiltered0' ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1Mu0HTT50L3Filtered3 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu0HTT50L2Filtered0' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1Mu0HTT50L3MuFiltered5 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu0HTT50L2MuFiltered3' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1Mu0HTT50L3MuFiltered8 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu0HTT50L2MuFiltered5' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 8.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1Mu3EG5L1DiMuFiltered3 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1Mu3EG5' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 3.0 ),
    MinN = cms.int32( 2 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1Mu3EG5L1Filtered12 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1Mu3EG5' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 12.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1Mu3EG5L1Filtered3 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1Mu3EG5' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 3.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1Mu3EG5L1Filtered5 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1Mu3EG5' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 5.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1Mu3EG5L2DiMuFiltered3 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu3EG5L1DiMuFiltered3' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1Mu3EG5L2Filtered12 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu3EG5L1Filtered12' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 12.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1Mu3EG5L2Filtered5 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu3EG5L1Filtered5' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1Mu3EG5L3DiMuFiltered5 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu3EG5L2DiMuFiltered3' ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1Mu3EG5L3Filtered10 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu3EG5L2Filtered5' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 10.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1Mu3EG5L3Filtered15 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu3EG5L2Filtered5' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 15.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1Mu3EG5L3Filtered17 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu3EG5L2Filtered12' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 17.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1Mu3EG5L3Filtered8 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu3EG5L2Filtered5' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 8.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL1Mu3Jet20L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1Mu3Jet20' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1Mu7CenJet20L1MuFiltered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1Mu7Jet20Central' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1MuORL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1SingleMuOpenCandidate' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( True ),
    SelectQualities = cms.vint32(  )
)
process.hltL1MuOpenL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1SingleMuOpen' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( True ),
    SelectQualities = cms.vint32(  )
)
process.hltL1MuOpenL1FilteredDT = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1SingleMuOpen' ),
    MaxEta = cms.double( 1.25 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( True ),
    SelectQualities = cms.vint32(  )
)
process.hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "hltEgammaRegionalCTFFinalFitWithMaterial" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    src = cms.InputTag( 'hltL1NonIsoEgammaRegionalCkfTrackCandidates' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltL1NonIsoEgammaRegionalCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( 'hltL1NonIsoEgammaRegionalPixelSeedGenerator' ),
    TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltL1NonIsoEgammaRegionalPixelSeedGenerator = cms.EDProducer( "EgammaHLTRegionalPixelSeedGeneratorProducers",
    ptMin = cms.double( 1.5 ),
    vertexZ = cms.double( 0.0 ),
    originRadius = cms.double( 0.02 ),
    originHalfLength = cms.double( 15.0 ),
    deltaEtaRegion = cms.double( 0.3 ),
    deltaPhiRegion = cms.double( 0.3 ),
    candTag = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    candTagEle = cms.InputTag( 'pixelMatchElectrons' ),
    UseZInVertex = cms.bool( False ),
    BSProducer = cms.InputTag( 'hltOnlineBeamSpot' ),
    OrderedHitsFactoryPSet = cms.PSet(
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltESPPixelLayerPairs" )
    )
)
process.hltL1NonIsoElectronTrackIsol = cms.EDProducer( "EgammaHLTElectronTrackIsolationProducers",
    electronProducer = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' ),
    trackProducer = cms.InputTag( 'hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial' ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoConeSize = cms.double( 0.3 ),
    egTrkIsoZSpan = cms.double( 0.15 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSize = cms.double( 0.03 ),
    egCheckForOtherEleInCone = cms.untracked.bool( False ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    egTrkIsoStripEndcap = cms.double( 0.03 )
)
process.hltL1NonIsoHLT2CaloIdLTripleElectronEt10HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTNonIsoTripleElectronEt10PixelMatchFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLT2LegEleIdTripleElectronEt10ClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLT2CaloIdLTripleElectronEt10HEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLT2LegEleIdTripleElectronEt10EleIdDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLT2LegEleIdTripleElectronEt10OneOEMinusOneOPFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.01 ),
    thrRegularEE = cms.double( 0.01 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltL1NonIsoHLT2LegEleIdTripleElectronEt10EleIdDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLT2LegEleIdTripleElectronEt10EleIdDetaFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.15 ),
    thrRegularEE = cms.double( 0.1 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltL1NonIsoHLT2LegEleIdTripleElectronEt10OneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( 'hltL1NonIsoHLT2LegEleIdTripleElectronEt10ClusterShapeFilter' ),
    electronIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    electronNonIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False )
)
process.hltL1NonIsoHLT3LegEleIdTripleElectronEt10ClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTNonIsoTripleElectronEt10PixelMatchFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 3 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLT3LegEleIdTripleElectronEt10EleIdDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLT3LegEleIdTripleElectronEt10OneOEMinusOneOPFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.01 ),
    thrRegularEE = cms.double( 0.01 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 3 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltL1NonIsoHLT3LegEleIdTripleElectronEt10EleIdDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLT3LegEleIdTripleElectronEt10EleIdDetaFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.15 ),
    thrRegularEE = cms.double( 0.1 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 3 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltL1NonIsoHLT3LegEleIdTripleElectronEt10OneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( 'hltL1NonIsoHLT3LegEleIdTripleElectronEt10ClusterShapeFilter' ),
    electronIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    electronNonIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 3 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False )
)
process.hltL1NonIsoHLTCaloIdLDoubleEle8HTT50ClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoubleEG8EtFilterL1DoubleEG5HTT50' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTCaloIdLDoubleEle8HTT50HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdLDoubleEle8HTT50R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTCaloIdLDoubleEle8HTT50PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdLDoubleEle8HTT50HEFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTCaloIdLDoubleEle8HTT50R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdLDoubleEle8HTT50ClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTCaloIdLMu10Ele10ClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTNonIsoMu10Ele10R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTCaloIdLMu17Ele8ClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG8R9ShapeFilterMu3EG5' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTCaloIdLMu8Ele17ClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTNonIsoMu8Ele17R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTCaloIdLSingleEle8NoCandClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTNonIsoSingleEle8NoCandR9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonClusterShape' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTCaloIdLSingleEle8NoCandHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdLSingleEle8NoCandClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltActivityPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' )
)
process.hltL1NonIsoHLTCaloIdLSingleEle8NoCandPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdLSingleEle8NoCandHEFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltActivityStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTCaloIdLTrkIdVLDoubleEle8HTT50DetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdLTrkIdVLDoubleEle8HTT50OneOEMinusOneOPFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.01 ),
    thrRegularEE = cms.double( 0.01 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltL1NonIsoHLTCaloIdLTrkIdVLDoubleEle8HTT50DphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdLTrkIdVLDoubleEle8HTT50DetaFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.15 ),
    thrRegularEE = cms.double( 0.1 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltL1NonIsoHLTCaloIdLTrkIdVLDoubleEle8HTT50OneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdLDoubleEle8HTT50PixelMatchFilter' ),
    electronIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    electronNonIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False )
)
process.hltL1NonIsoHLTCaloIdLTrkIdVLSingleElectronEt8NoCandDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdLTrkIdVLSingleElectronEt8NoCandOneOEMinusOneOPFilter' ),
    isoTag = cms.InputTag( 'hltElectronActivityDetaDphi', 'Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronActivityDetaDphi', 'Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.01 ),
    thrRegularEE = cms.double( 0.01 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsActivity' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsActivity' )
)
process.hltL1NonIsoHLTCaloIdLTrkIdVLSingleElectronEt8NoCandDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdLTrkIdVLSingleElectronEt8NoCandDetaFilter' ),
    isoTag = cms.InputTag( 'hltElectronActivityDetaDphi', 'Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronActivityDetaDphi', 'Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.15 ),
    thrRegularEE = cms.double( 0.1 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsActivity' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsActivity' )
)
process.hltL1NonIsoHLTCaloIdLTrkIdVLSingleElectronEt8NoCandOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdLSingleEle8NoCandPixelMatchFilter' ),
    electronIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsActivity' ),
    electronNonIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsActivity' ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False )
)
process.hltL1NonIsoHLTCaloIdTDoubleEle8HTT50ClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoubleEG8EtFilterL1DoubleEG5HTT50' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.011 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTCaloIdTDoubleEle8HTT50HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdTDoubleEle8HTT50R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.1 ),
    thrOverEEE = cms.double( 0.075 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTCaloIdTDoubleEle8HTT50PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdTDoubleEle8HTT50HEFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTCaloIdTDoubleEle8HTT50R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdTDoubleEle8HTT50ClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTCaloIdTSingleEle8NoCandClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTNonIsoSingleEle8NoCandR9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonClusterShape' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.011 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTCaloIdTSingleEle8NoCandHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdTSingleEle8NoCandClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltActivityPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.1 ),
    thrOverEEE = cms.double( 0.075 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' )
)
process.hltL1NonIsoHLTCaloIdTSingleEle8NoCandPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdTSingleEle8NoCandHEFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltActivityStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTCaloIdTTrkIdVLDoubleEle8HTT50DetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdTTrkIdVLDoubleEle8HTT50OneOEMinusOneOPFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.01 ),
    thrRegularEE = cms.double( 0.01 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltL1NonIsoHLTCaloIdTTrkIdVLDoubleEle8HTT50DphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdTTrkIdVLDoubleEle8HTT50DetaFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.15 ),
    thrRegularEE = cms.double( 0.1 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltL1NonIsoHLTCaloIdTTrkIdVLDoubleEle8HTT50OneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdTDoubleEle8HTT50PixelMatchFilter' ),
    electronIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    electronNonIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False )
)
process.hltL1NonIsoHLTCaloIdTTrkIdVLSingleElectronEt8NoCandDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdTTrkIdVLSingleElectronEt8NoCandOneOEMinusOneOPFilter' ),
    isoTag = cms.InputTag( 'hltElectronActivityDetaDphi', 'Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronActivityDetaDphi', 'Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.01 ),
    thrRegularEE = cms.double( 0.01 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsActivity' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsActivity' )
)
process.hltL1NonIsoHLTCaloIdTTrkIdVLSingleElectronEt8NoCandDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdTTrkIdVLSingleElectronEt8NoCandDetaFilter' ),
    isoTag = cms.InputTag( 'hltElectronActivityDetaDphi', 'Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronActivityDetaDphi', 'Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.15 ),
    thrRegularEE = cms.double( 0.1 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsActivity' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsActivity' )
)
process.hltL1NonIsoHLTCaloIdTTrkIdVLSingleElectronEt8NoCandOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdTSingleEle8NoCandPixelMatchFilter' ),
    electronIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsActivity' ),
    electronNonIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsActivity' ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False )
)
process.hltL1NonIsoHLTCaloIsolLSingleElectronEt10HT200HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG10CaloIdTCaloIsoVLEcalIsolFilterEG5HTT75' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTCaloIsolLSingleElectronEt10HT200HcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIsolLSingleElectronEt10HT200HEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.2 ),
    thrOverEEE = cms.double( 0.2 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTCaloIsolLSingleElectronEt10HT200PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIsolLSingleElectronEt10HT200HcalIsolFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTCaloIsolLTrkIsolLCaloIdLSingleElectronEt10HT200OneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIsolLSingleElectronEt10HT200PixelMatchFilter' ),
    electronIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    electronNonIsolatedProducer = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' ),
    barrelcut = cms.double( 999.9 ),
    endcapcut = cms.double( 999.9 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False )
)
process.hltL1NonIsoHLTCaloIsolLTrkIsolLCaloIdLTrkIdLSingleElectronEt10HT200DetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIsolLTrkIsolLCaloIdLSingleElectronEt10HT200OneOEMinusOneOPFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Deta' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Deta' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.01 ),
    thrRegularEE = cms.double( 0.01 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltL1NonIsoHLTCaloIsolLTrkIsolLCaloIdLTrkIdLSingleElectronEt10HT200DphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIsolLTrkIsolLCaloIdLTrkIdLSingleElectronEt10HT200DetaFilter' ),
    isoTag = cms.InputTag( 'hltElectronL1IsoDetaDphi', 'Dphi' ),
    nonIsoTag = cms.InputTag( 'hltElectronL1NonIsoDetaDphi', 'Dphi' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( 0.15 ),
    thrRegularEE = cms.double( 0.1 ),
    thrOverPtEB = cms.double( -1.0 ),
    thrOverPtEE = cms.double( -1.0 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltL1NonIsoHLTCaloIsolLTrkIsolLSingleElectronEt10HT200TrackIsolFilter = cms.HLTFilter( "HLTElectronGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIsolLTrkIsolLCaloIdLTrkIdLSingleElectronEt10HT200DphiFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoElectronTrackIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoElectronTrackIsol' ),
    lessThan = cms.bool( True ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverPtEB = cms.double( 0.2 ),
    thrOverPtEE = cms.double( 0.2 ),
    thrTimesPtEB = cms.double( -1.0 ),
    thrTimesPtEE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltPixelMatchElectronsL1Iso' ),
    L1NonIsoCand = cms.InputTag( 'hltPixelMatchElectronsL1NonIso' )
)
process.hltL1NonIsoHLTClusterShape = cms.EDProducer( "EgammaHLTClusterShapeProducer",
    recoEcalCandidateProducer = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    ecalRechitEB = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEE' ),
    isIeta = cms.bool( True )
)
process.hltL1NonIsoHLTNonIsoMu10Ele10HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdLMu10Ele10ClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTNonIsoMu10Ele10PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTNonIsoMu10Ele10HEFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTNonIsoMu10Ele10R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG10EtFilterL1Mu3EG5' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTNonIsoMu17Ele8HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdLMu17Ele8ClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTNonIsoMu17Ele8PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTNonIsoMu17Ele8HEFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTNonIsoMu5DoubleEle8NoCandHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTNonIsoMu5DoubleEle8NoCandR9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( True ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoMu5DoubleEle8NoCandR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoubleEG8EtFilterUnseeded' ),
    isoTag = cms.InputTag( 'hltUnseededR9shape' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoMu8Ele17HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTCaloIdLMu8Ele17ClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTNonIsoMu8Ele17PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTNonIsoMu8Ele17HEFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTNonIsoMu8Ele17R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG17EtFilterL1Mu3EG5' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTNonIsoSingleEle8NoCandEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEcalActivitySuperClusterWrapper' ),
    etcutEB = cms.double( 8.0 ),
    etcutEE = cms.double( 8.0 ),
    ncandcut = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' )
)
process.hltL1NonIsoHLTNonIsoSingleEle8NoCandR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTNonIsoSingleEle8NoCandEtFilter' ),
    isoTag = cms.InputTag( 'hltUnseededR9shape' ),
    nonIsoTag = cms.InputTag( 'hltUnseededR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' )
)
process.hltL1NonIsoHLTNonIsoTripleElectronEt10HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTNonIsoTripleElectronEt10R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 3 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTNonIsoTripleElectronEt10PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
    candTag = cms.InputTag( 'hltL1NonIsoHLTNonIsoTripleElectronEt10HEFilter' ),
    L1IsoPixelSeedsTag = cms.InputTag( 'hltL1IsoStartUpElectronPixelSeeds' ),
    L1NonIsoPixelSeedsTag = cms.InputTag( 'hltL1NonIsoStartUpElectronPixelSeeds' ),
    npixelmatchcut = cms.double( 1.0 ),
    ncandcut = cms.int32( 3 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoHLTNonIsoTripleElectronEt10R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltTripleEG10EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 3 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltL1NonIsoR9ID = cms.EDProducer( "EgammaHLTR9IDProducer",
    recoEcalCandidateProducer = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    ecalRechitEB = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEE' )
)
process.hltL1NonIsoR9shape = cms.EDProducer( "EgammaHLTR9Producer",
    recoEcalCandidateProducer = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    ecalRechitEB = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRegionalEgammaRecHit', 'EcalRecHitsEE' ),
    useSwissCross = cms.bool( False )
)
process.hltL1NonIsoRecoEcalCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scHybridBarrelProducer = cms.InputTag( 'hltCorrectedHybridSuperClustersL1NonIsolated' ),
    scIslandEndcapProducer = cms.InputTag( 'hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated' ),
    recoEcalCandidateCollection = cms.string( "" )
)
process.hltL1NonIsoStartUpElectronPixelSeeds = cms.EDProducer( "ElectronSeedProducer",
    barrelSuperClusters = cms.InputTag( 'hltCorrectedHybridSuperClustersL1NonIsolated' ),
    endcapSuperClusters = cms.InputTag( 'hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated' ),
    SeedConfiguration = cms.PSet(
      searchInTIDTEC = cms.bool( True ),
      HighPtThreshold = cms.double( 35.0 ),
      r2MinF = cms.double( -0.15 ),
      OrderedHitsFactoryPSet = cms.PSet(
        maxElement = cms.uint32( 0 ),
        ComponentName = cms.string( "StandardHitPairGenerator" ),
        SeedingLayers = cms.string( "hltESPMixedLayerPairs" ),
        useOnDemandTracker = cms.untracked.int32( 0 )
      ),
      DeltaPhi1Low = cms.double( 0.23 ),
      DeltaPhi1High = cms.double( 0.08 ),
      ePhiMin1 = cms.double( -0.08 ),
      PhiMin2 = cms.double( -0.004 ),
      LowPtThreshold = cms.double( 3.0 ),
      hcalTowers = cms.InputTag( 'towerMaker' ),
      RegionPSet = cms.PSet(
        deltaPhiRegion = cms.double( 0.4 ),
        originHalfLength = cms.double( 15.0 ),
        useZInVertex = cms.bool( True ),
        deltaEtaRegion = cms.double( 0.1 ),
        ptMin = cms.double( 1.5 ),
        originRadius = cms.double( 0.2 ),
        VertexProducer = cms.InputTag( 'dummyVertices' )
      ),
      hOverEPtMin = cms.double( None ),
      maxHOverE = cms.double( 999999.0 ),
      maxHOverEBarrel = cms.double( None ),
      maxHOverEEndcaps = cms.double( None ),
      dynamicPhiRoad = cms.bool( False ),
      ePhiMax1 = cms.double( 0.04 ),
      maxHBarrel = cms.double( None ),
      maxHEndcaps = cms.double( None ),
      DeltaPhi2 = cms.double( 0.004 ),
      measurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      SizeWindowENeg = cms.double( 0.675 ),
      nSigmasDeltaZ1 = cms.double( 5.0 ),
      rMaxI = cms.double( 0.2 ),
      PhiMax2 = cms.double( 0.004 ),
      preFilteredSeeds = cms.bool( True ),
      r2MaxF = cms.double( 0.15 ),
      pPhiMin1 = cms.double( -0.04 ),
      useRecoVertex = cms.bool( None ),
      initialSeeds = cms.InputTag( 'noSeedsHere' ),
      vertices = cms.InputTag( None ),
      pPhiMax1 = cms.double( 0.08 ),
      deltaZ1WithVertex = cms.double( None ),
      hbheModule = cms.string( "hbhereco" ),
      SCEtCut = cms.double( 3.0 ),
      DeltaPhi2B = cms.double( None ),
      z2MaxB = cms.double( 0.09 ),
      DeltaPhi2F = cms.double( None ),
      fromTrackerSeeds = cms.bool( True ),
      hcalRecHits = cms.InputTag( 'hltHbhereco' ),
      PhiMin2B = cms.double( None ),
      z2MinB = cms.double( -0.09 ),
      hbheInstance = cms.string( "" ),
      PhiMin2F = cms.double( None ),
      rMinI = cms.double( -0.2 ),
      hOverEConeSize = cms.double( 0.0 ),
      PhiMax2B = cms.double( None ),
      PhiMax2F = cms.double( None ),
      hOverEHBMinE = cms.double( 999999.0 ),
      beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
      applyHOverECut = cms.bool( False ),
      hOverEHFMinE = cms.double( 999999.0 )
    )
)
process.hltL1NonIsolatedPhotonEcalIsol = cms.EDProducer( "EgammaHLTEcalRecIsolationProducer",
    recoEcalCandidateProducer = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    ecalBarrelRecHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit' ),
    ecalBarrelRecHitCollection = cms.InputTag( 'EcalRecHitsEB' ),
    ecalEndcapRecHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit' ),
    ecalEndcapRecHitCollection = cms.InputTag( 'EcalRecHitsEE' ),
    etMinBarrel = cms.double( -9999.0 ),
    eMinBarrel = cms.double( 0.08 ),
    etMinEndcap = cms.double( 0.1 ),
    eMinEndcap = cms.double( -9999.0 ),
    intRadiusBarrel = cms.double( 3.0 ),
    intRadiusEndcap = cms.double( 3.0 ),
    extRadius = cms.double( 0.3 ),
    jurassicWidth = cms.double( 3.0 ),
    useIsolEt = cms.bool( True ),
    tryBoth = cms.bool( True ),
    subtract = cms.bool( False ),
    useNumCrystals = cms.bool( True )
)
process.hltL1NonIsolatedPhotonHcalForHE = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    hbheRecHitProducer = cms.InputTag( 'hltHbhereco' ),
    eMinHB = cms.double( 0.7 ),
    eMinHE = cms.double( 0.8 ),
    etMinHB = cms.double( -1.0 ),
    etMinHE = cms.double( -1.0 ),
    innerCone = cms.double( 0.0 ),
    outerCone = cms.double( 0.14 ),
    depth = cms.int32( -1 ),
    doEtSum = cms.bool( False )
)
process.hltL1NonIsolatedPhotonHcalIsol = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    hbheRecHitProducer = cms.InputTag( 'hltHbhereco' ),
    eMinHB = cms.double( 0.7 ),
    eMinHE = cms.double( 0.8 ),
    etMinHB = cms.double( -1.0 ),
    etMinHE = cms.double( -1.0 ),
    innerCone = cms.double( 0.16 ),
    outerCone = cms.double( 0.29 ),
    depth = cms.int32( -1 ),
    doEtSum = cms.bool( True )
)
process.hltL1NonIsolatedPhotonHollowTrackIsol = cms.EDProducer( "EgammaHLTPhotonTrackIsolationProducersRegional",
    recoEcalCandidateProducer = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' ),
    trackProducer = cms.InputTag( 'hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial' ),
    countTracks = cms.bool( False ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoConeSize = cms.double( 0.29 ),
    egTrkIsoZSpan = cms.double( 999999.0 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSize = cms.double( 0.06 ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    egTrkIsoStripEndcap = cms.double( 0.03 )
)
process.hltL1SingleMu10L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1SingleMu10' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1SingleMu12L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1SingleMu12' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1SingleMu20L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1SingleMu20' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1SingleMu3EG5L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1Mu3EG5' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1SingleMu3L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1SingleMu3' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1SingleMu7L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1SingleMu7' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltL1TechBSChalo = cms.HLTFilter( "TriggerResultsFilter",
    triggerConditions = cms.vstring( "L1Tech_BSC_halo_beam2_inner",
       "L1Tech_BSC_halo_beam2_outer",
       "L1Tech_BSC_halo_beam1_inner",
       "L1Tech_BSC_halo_beam1_outer" ),
    hltResults = cms.InputTag( "" ),
    l1tResults = cms.InputTag( 'hltGtDigis' ),
    l1tIgnoreMask = cms.bool( False ),
    daqPartitions = cms.uint32( 1 ),
    throw = cms.bool( True ),
    l1techIgnorePrescales = cms.bool( True )
)
process.hltL1TechBSCminBiasthreshold1 = cms.HLTFilter( "TriggerResultsFilter",
    triggerConditions = cms.vstring( "L1Tech_BSC_minBias_threshold1" ),
    hltResults = cms.InputTag( "" ),
    l1tResults = cms.InputTag( 'hltGtDigis' ),
    l1tIgnoreMask = cms.bool( False ),
    daqPartitions = cms.uint32( 1 ),
    throw = cms.bool( True ),
    l1techIgnorePrescales = cms.bool( True )
)
process.hltL1extraParticles = cms.EDProducer( "L1ExtraParticlesProd",
    produceMuonParticles = cms.bool( True ),
    muonSource = cms.InputTag( 'hltGtDigis' ),
    produceCaloParticles = cms.bool( True ),
    isolatedEmSource = cms.InputTag( 'hltGctDigis', 'isoEm' ),
    nonIsolatedEmSource = cms.InputTag( 'hltGctDigis', 'nonIsoEm' ),
    centralJetSource = cms.InputTag( 'hltGctDigis', 'cenJets' ),
    forwardJetSource = cms.InputTag( 'hltGctDigis', 'forJets' ),
    tauJetSource = cms.InputTag( 'hltGctDigis', 'tauJets' ),
    etTotalSource = cms.InputTag( 'hltGctDigis' ),
    etHadSource = cms.InputTag( 'hltGctDigis' ),
    etMissSource = cms.InputTag( 'hltGctDigis' ),
    htMissSource = cms.InputTag( 'hltGctDigis' ),
    hfRingEtSumsSource = cms.InputTag( 'hltGctDigis' ),
    hfRingBitCountsSource = cms.InputTag( 'hltGctDigis' ),
    centralBxOnly = cms.bool( True ),
    ignoreHtMiss = cms.bool( False )
)
process.hltL1sAlCaEcalPi0Eta = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleEG10 OR L1_DoubleEG2_FwdVeto OR L1_DoubleEG3 OR L1_DoubleEG5 OR L1_DoubleEG5_HTT50 OR L1_DoubleEG5_HTT75 OR L1_DoubleEG8 OR L1_DoubleEG_12_5 OR L1_DoubleForJet20_EtaOpp OR L1_DoubleForJet36_EtaOpp OR L1_DoubleIsoEG10 OR L1_DoubleIsoEG5 OR L1_DoubleIsoEG8 OR L1_DoubleJet36_Central OR L1_DoubleJet52 OR L1_EG5_HTT100 OR L1_EG5_HTT125 OR L1_EG5_HTT75 OR L1_SingleEG12 OR L1_SingleEG12_Eta2p17 OR L1_SingleEG15 OR L1_SingleEG20 OR L1_SingleEG30 OR L1_SingleEG5 OR L1_SingleIsoEG10 OR L1_SingleIsoEG12 OR L1_SingleIsoEG12_Eta2p17 OR L1_SingleIsoEG15 OR L1_SingleJet128 OR L1_SingleJet16 OR L1_SingleJet36 OR L1_SingleJet36_FwdVeto OR L1_SingleJet52 OR L1_SingleJet68 OR L1_SingleJet80_Central OR L1_SingleJet92 OR L1_TripleEG5 OR L1_TripleEG7 OR L1_TripleJet28" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sAlCaRPC = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu7 OR L1_SingleMu10 OR L1_SingleMu12 OR L1_SingleMu16 OR L1_SingleMu20" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sDoubleIsoTau20Trk5 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleTauJet28 OR L1_DoubleJet52" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sETT180 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_ETT180" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sGlobalRunHPDNoise = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet20_NotBptxOR_NotMuBeamHalo" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sHcalNZS = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet16 OR L1_SingleJet36 OR L1_SingleJet52 OR L1_SingleJet68 OR L1_SingleJet92 OR L1_SingleJet128 OR L1_SingleTauJet52 OR L1_SingleTauJet68 OR L1_SingleMu3 OR L1_SingleMu7 OR L1_SingleMu10 OR L1_SingleMu12 OR L1_SingleMu16 OR L1_SingleMu20 OR L1_SingleIsoEG5 OR L1_SingleIsoEG10 OR L1_SingleIsoEG12 OR L1_SingleIsoEG15 OR L1_SingleEG5 OR L1_SingleEG12 OR L1_SingleEG15 OR L1_SingleEG20 OR L1_SingleEG30 OR L1_ZeroBias" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sHcalPhiSym = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleEG10 OR L1_DoubleEG2_FwdVeto OR L1_DoubleEG3 OR L1_DoubleEG5 OR L1_DoubleEG8 OR L1_DoubleEG_12_5 OR L1_DoubleIsoEG10 OR L1_DoubleIsoEG5 OR L1_DoubleIsoEG8 OR L1_SingleEG12 OR L1_SingleEG12_Eta2p17 OR L1_SingleEG15 OR L1_SingleEG20 OR L1_SingleEG30 OR L1_SingleEG5 OR L1_SingleIsoEG10 OR L1_SingleIsoEG12 OR L1_SingleIsoEG12_Eta2p17 OR L1_SingleIsoEG15 OR L1_SingleIsoEG5 OR L1_SingleMu7 OR L1_SingleMu10 OR L1_SingleMu12 OR L1_SingleMu16 OR L1_SingleMu20 OR L1_SingleMu3 OR L1_SingleMu25 OR L1_DoubleMu0 OR L1_DoubleMu3 OR L1_DoubleMu5 OR L1_Mu3_EG8 OR L1_Mu5_EG8" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1BeamGasBsc = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_BeamGas_Bsc" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1BeamGasHf = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_BeamGas_Hf" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1BeamHalo = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_BeamHalo" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1BscMinBiasORBptxPlusANDMinus = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_BscMinBiasOR_BptxPlusANDMinus" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1DoubleEG2FwdVeto = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleEG2_FwdVeto" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1DoubleEG5HTT50 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleEG5_HTT50" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1DoubleForJet20EtaOpp = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleForJet20_EtaOpp" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1DoubleForJet36EtaOpp = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleForJet36_EtaOpp" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1DoubleJet36Central = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleJet36_Central" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1DoubleMu0 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu0" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1DoubleMu05 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu_0_5" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1DoubleMu3 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu3" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1EG5HTT75 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_EG5_HTT75" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1ETM20 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_ETM20" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1ETM30 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_ETM30" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1HTT100 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_HTT100" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1HTT50 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_HTT50" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1InterbunchBsc = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_InterBunch_Bsc" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1Mu0HTT50 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_Mu0_HTT50" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1Mu3EG5 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_Mu3_EG5" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1Mu3Jet16 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_Mu3_Jet16" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1Mu3Jet20 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_Mu3_Jet20" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1Mu7Jet20Central = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_Mu7_Jet20_Central" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1PreCollisions = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_PreCollisions" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1QuadJet20Central = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_QuadJet20_Central" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleEG12 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG12" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleEG15 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG15" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleEG20 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG20" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleEG5 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG5" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleJet16 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet16" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleJet20NoBPTX = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet20_NotBptxOR" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( False )
)
process.hltL1sL1SingleJet20NoBPTXNoHalo = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet20_NotBptxOR_NotMuBeamHalo" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( False )
)
process.hltL1sL1SingleJet36 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet36" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleJet36FwdVeto = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet36_FwdVeto" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleJet52 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet52" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleJet68 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet68" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleJet92 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleJet92" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMu10 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu10" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMu12 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu12" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMu20 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu20" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMu3 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu3" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMu5BQ7 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu5_Eta1p5_Q80" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMu7 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu7" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMuOpen = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMuOpen" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMuOpenCandidate = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( False ),
    L1NrBxInEvent = cms.int32( 1 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleMuOpen" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sL1TripleEG5 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_TripleEG5" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sSingleIsoTau35Trk20MET45 = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( False ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleTauJet52 OR L1_SingleJet68" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sTechTrigHCALNoise = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "11 OR 12" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sTrackerCosmics = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "25" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1sZeroBias = cms.HLTFilter( "HLTLevel1GTSeed",
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1TechTriggerSeeding = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1SeedsLogicalExpression = cms.string( "4" ),
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    L1GtObjectMapTag = cms.InputTag( 'hltL1GtObjectMap' ),
    L1CollectionsTag = cms.InputTag( 'hltL1extraParticles' ),
    L1MuonCollectionTag = cms.InputTag( 'hltL1extraParticles' ),
    saveTags = cms.untracked.bool( True )
)
process.hltL1tfed = cms.EDAnalyzer( "L1TFED",
    verbose = cms.untracked.bool( False ),
    rawTag = cms.InputTag( 'source' ),
    DQMStore = cms.untracked.bool( True ),
    outputFile = cms.untracked.string( "" ),
    disableROOToutput = cms.untracked.bool( True ),
    FEDDirName = cms.untracked.string( "L1T/FEDIntegrity_EvF" ),
    stableROConfig = cms.untracked.bool( True ),
    L1FEDS = cms.vint32( 745, 760, 780, 812, 813 )
)
process.hltL2DoubleMu35NoVertexL2PreFiltered = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidatesNoVtx' ),
    PreviousCandTag = cms.InputTag( 'hltL1DoubleMuon3L1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 3.0 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 35.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL2DoubleMu3L2Filtered = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1DoubleMuon3L1Filtered3' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 3.0 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL2Mu10L2Filtered10 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1SingleMu10L1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 10.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL2Mu12L2Filtered12 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1SingleMu12L1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 12.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL2Mu20L2Filtered20 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1SingleMu12L1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 20.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL2Mu3EG5L2Filtered3 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu3EG5L1Filtered3' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL2Mu3L2Filtered3 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1SingleMu3L1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL2Mu7L2Filtered7 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1SingleMu7L1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 7.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL2Mu8Jet20L2Filtered3 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu3Jet20L1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( False )
)
process.hltL2Muon7 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1Mu7CenJet20L1MuFiltered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 7.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL2MuonCandidates = cms.EDProducer( "L2MuonCandidateProducer",
    InputObjects = cms.InputTag( 'hltL2Muons', 'UpdatedAtVtx' )
)
process.hltL2MuonCandidatesNoVtx = cms.EDProducer( "L2MuonCandidateProducer",
    InputObjects = cms.InputTag( 'hltL2Muons' )
)
process.hltL2MuonIsolations = cms.EDProducer( "L2MuonIsolationProducer",
    StandAloneCollectionLabel = cms.InputTag( 'hltL2Muons', 'UpdatedAtVtx' ),
    ExtractorPSet = cms.PSet(
      DR_Veto_H = cms.double( 0.1 ),
      Vertex_Constraint_Z = cms.bool( False ),
      Threshold_H = cms.double( 0.5 ),
      ComponentName = cms.string( "CaloExtractor" ),
      Threshold_E = cms.double( 0.2 ),
      DR_Max = cms.double( 0.24 ),
      DR_Veto_E = cms.double( 0.07 ),
      Weight_E = cms.double( 1.5 ),
      Vertex_Constraint_XY = cms.bool( False ),
      DepositLabel = cms.untracked.string( "EcalPlusHcal" ),
      CaloTowerCollectionLabel = cms.InputTag( 'hltTowerMakerForMuons' ),
      Weight_H = cms.double( 1.0 )
    ),
    IsolatorPSet = cms.PSet(
      ConeSizes = cms.vdouble(  0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24  ),
      ComponentName = cms.string( "SimpleCutsIsolator" ),
      EtaBounds = cms.vdouble(  0.0435, 0.1305, 0.2175, 0.3045, 0.3915, 0.4785, 0.5655, 0.6525, 0.7395, 0.8265, 0.9135, 1.0005, 1.0875, 1.1745, 1.2615, 1.3485, 1.4355, 1.5225, 1.6095, 1.6965, 1.785, 1.88, 1.9865, 2.1075, 2.247, 2.411  ),
      Thresholds = cms.vdouble(  4, 3.7, 4, 3.5, 3.4, 3.4, 3.2, 3.4, 3.1, 2.9, 2.9, 2.7, 3.1, 3, 2.4, 2.1, 2, 2.3, 2.2, 2.4, 2.5, 2.5, 2.6, 2.9, 3.1, 2.9  )
    )
)
process.hltL2MuonSeeds = cms.EDProducer( "L2MuonSeedGenerator",
    InputObjects = cms.InputTag( 'hltL1extraParticles' ),
    GMTReadoutCollection = cms.InputTag( 'hltGtDigis' ),
    Propagator = cms.string( "SteppingHelixPropagatorAny" ),
    L1MinPt = cms.double( 0.0 ),
    L1MaxEta = cms.double( 2.5 ),
    L1MinQuality = cms.uint32( 1 ),
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( "SteppingHelixPropagatorAny" ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    )
)
process.hltL2Muons = cms.EDProducer( "L2MuonProducer",
    InputObjects = cms.InputTag( 'hltL2MuonSeeds' ),
    L2TrajBuilderParameters = cms.PSet(
      DoRefit = cms.bool( False ),
      SeedPropagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      FilterParameters = cms.PSet(
        NumberOfSigma = cms.double( 3.0 ),
        FitDirection = cms.string( "insideOut" ),
        DTRecSegmentLabel = cms.InputTag( 'hltDt4DSegments' ),
        MaxChi2 = cms.double( 1000.0 ),
        MuonTrajectoryUpdatorParameters = cms.PSet(
          MaxChi2 = cms.double( 25.0 ),
          RescaleErrorFactor = cms.double( 100.0 ),
          Granularity = cms.int32( 0 ),
          ExcludeRPCFromFit = cms.bool( False ),
          UseInvalidHits = cms.bool( True ),
          RescaleError = cms.bool( False )
        ),
        EnableRPCMeasurement = cms.bool( True ),
        CSCRecSegmentLabel = cms.InputTag( 'hltCscSegments' ),
        EnableDTMeasurement = cms.bool( True ),
        RPCRecSegmentLabel = cms.InputTag( 'hltRpcRecHits' ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        EnableCSCMeasurement = cms.bool( True )
      ),
      NavigationType = cms.string( "Standard" ),
      SeedTransformerParameters = cms.PSet(
        Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        NMinRecHits = cms.uint32( 2 ),
        UseSubRecHits = cms.bool( False ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        RescaleError = cms.double( 100.0 )
      ),
      DoBackwardFilter = cms.bool( True ),
      SeedPosition = cms.string( "in" ),
      BWFilterParameters = cms.PSet(
        NumberOfSigma = cms.double( 3.0 ),
        CSCRecSegmentLabel = cms.InputTag( 'hltCscSegments' ),
        FitDirection = cms.string( "outsideIn" ),
        DTRecSegmentLabel = cms.InputTag( 'hltDt4DSegments' ),
        MaxChi2 = cms.double( 100.0 ),
        MuonTrajectoryUpdatorParameters = cms.PSet(
          MaxChi2 = cms.double( 25.0 ),
          RescaleErrorFactor = cms.double( 100.0 ),
          Granularity = cms.int32( 2 ),
          ExcludeRPCFromFit = cms.bool( False ),
          UseInvalidHits = cms.bool( True ),
          RescaleError = cms.bool( False )
        ),
        EnableRPCMeasurement = cms.bool( True ),
        BWSeedType = cms.string( "fromGenerator" ),
        EnableDTMeasurement = cms.bool( True ),
        RPCRecSegmentLabel = cms.InputTag( 'hltRpcRecHits' ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        EnableCSCMeasurement = cms.bool( True )
      ),
      DoSeedRefit = cms.bool( False )
    ),
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( "hltESPFastSteppingHelixPropagatorAny",
         "hltESPFastSteppingHelixPropagatorOpposite" ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    TrackLoaderParameters = cms.PSet(
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      DoSmoothing = cms.bool( False ),
      beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
      MuonUpdatorAtVertexParameters = cms.PSet(
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPosition = cms.vdouble(  0, 0, 0  ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble(  0.1, 0.1, 5.3  )
      ),
      VertexConstraint = cms.bool( True ),
      PutTrajectoryIntoEvent = cms.untracked.bool( None ),
      MuonSeededTracksInstance = cms.untracked.string( "" ),
      PutTkTrackIntoEvent = cms.untracked.bool( None ),
      SmoothTkTrack = cms.untracked.bool( None ),
      AllowNoVertex = cms.untracked.bool( None )
    )
)
process.hltL2TauJets = cms.EDProducer( "L2TauJetsMerger",
    EtMin = cms.double( 20.0 ),
    JetSrc = cms.VInputTag( 'hltIconeTau1Regional, hltIconeTau2Regional, hltIconeTau3Regional, hltIconeTau4Regional, hltIconeCentral1Regional, hltIconeCentral2Regional, hltIconeCentral3Regional, hltIconeCentral4Regional' )
)
process.hltL3Mu8Jet20L3Filtered8 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL2Mu8Jet20L2Filtered3' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 8.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL3Muon15 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL2Mu10L2Filtered10' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 15.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL3Muon17 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL2Muon7' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 17.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltL3MuonCandidates = cms.EDProducer( "L3MuonCandidateProducer",
    InputObjects = cms.InputTag( 'hltL3Muons' )
)
process.hltL3MuonCandidatesNoVtx = cms.EDProducer( "L3MuonCandidateProducer",
    InputObjects = cms.InputTag( 'hltL3MuonsNoVtx' )
)
process.hltL3MuonIsolations = cms.EDProducer( "L3MuonIsolationProducer",
    inputMuonCollection = cms.InputTag( 'hltL3Muons' ),
    OutputMuIsoDeposits = cms.bool( True ),
    TrackPt_Min = cms.double( -1.0 ),
    CutsPSet = cms.PSet(
      ConeSizes = cms.vdouble(  0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24  ),
      ComponentName = cms.string( "SimpleCuts" ),
      Thresholds = cms.vdouble(  1.1, 1.1, 1.1, 1.1, 1.2, 1.1, 1.2, 1.1, 1.2, 1, 1.1, 1, 1, 1.1, 1, 1, 1.1, 0.9, 1.1, 0.9, 1.1, 1, 1, 0.9, 0.8, 0.1  ),
      maxNTracks = cms.int32( -1 ),
      EtaBounds = cms.vdouble(  0.0435, 0.1305, 0.2175, 0.3045, 0.3915, 0.4785, 0.5655, 0.6525, 0.7395, 0.8265, 0.9135, 1.0005, 1.0875, 1.1745, 1.2615, 1.3485, 1.4355, 1.5225, 1.6095, 1.6965, 1.785, 1.88, 1.9865, 2.1075, 2.247, 2.411  ),
      applyCutsORmaxNTracks = cms.bool( False )
    ),
    ExtractorPSet = cms.PSet(
      Chi2Prob_Min = cms.double( -1.0 ),
      Diff_z = cms.double( 0.2 ),
      inputTrackCollection = cms.InputTag( 'hltPixelTracks' ),
      ReferenceRadius = cms.double( 6.0 ),
      BeamSpotLabel = cms.InputTag( 'hltOnlineBeamSpot' ),
      ComponentName = cms.string( "PixelTrackExtractor" ),
      DR_Max = cms.double( 0.24 ),
      Diff_r = cms.double( 0.1 ),
      VetoLeadingTrack = cms.bool( True ),
      DR_VetoPt = cms.double( 0.025 ),
      DR_Veto = cms.double( 0.01 ),
      NHits_Min = cms.uint32( 0 ),
      Chi2Ndof_Max = cms.double( 1e+64 ),
      Pt_Min = cms.double( -1.0 ),
      DepositLabel = cms.untracked.string( "PXLS" ),
      BeamlineOption = cms.string( "BeamSpotFromEvent" ),
      PropagateTracksToRadius = cms.bool( True ),
      PtVeto_Min = cms.double( 2.0 )
    )
)
process.hltL3Muons = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState, hltL3MuonsOIHit, hltL3MuonsIOHit' )
)
process.hltL3MuonsIOHit = cms.EDProducer( "L3MuonProducer",
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons', 'UpdatedAtVtx' ),
    L3TrajBuilderParameters = cms.PSet(
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet(
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( 'hltDt4DSegments' ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( 'hltCscSegments' ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet(
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        Eta_min = cms.double( 0.05 ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        vertexCollection = cms.InputTag( 'pixelVertices' ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( 'hltOnlineBeamSpot' )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet(
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet(
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 999999999.0 ),
        LocChi2Cut = cms.double( 0.001 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( 'hltL3TkTracksFromL2IOHit' )
    ),
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( "hltESPSmartPropagatorAny",
         "SteppingHelixPropagatorAny",
         "hltESPSmartPropagator",
         "hltESPSteppingHelixPropagatorOpposite" ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    TrackLoaderParameters = cms.PSet(
      PutTkTrackIntoEvent = cms.untracked.bool( True ),
      beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet(
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble(  0.1, 0.1, 5.3  )
      ),
      PutTrajectoryIntoEvent = cms.untracked.bool( None ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True ),
      AllowNoVertex = cms.untracked.bool( None )
    )
)
process.hltL3MuonsLinksCombination = cms.EDProducer( "L3TrackLinksCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState, hltL3MuonsOIHit, hltL3MuonsIOHit' )
)
process.hltL3MuonsNoVtx = cms.EDProducer( "L3TkMuonProducer",
    InputObjects = cms.InputTag( 'hltL3TkTracksFromL2NoVtx' )
)
process.hltL3MuonsOIHit = cms.EDProducer( "L3MuonProducer",
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons', 'UpdatedAtVtx' ),
    L3TrajBuilderParameters = cms.PSet(
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet(
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( 'hltDt4DSegments' ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( 'hltCscSegments' ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet(
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        Eta_min = cms.double( 0.05 ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        vertexCollection = cms.InputTag( 'pixelVertices' ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( 'hltOnlineBeamSpot' )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet(
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet(
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 999999999.0 ),
        LocChi2Cut = cms.double( 0.001 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( 'hltL3TkTracksFromL2OIHit' )
    ),
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( "hltESPSmartPropagatorAny",
         "SteppingHelixPropagatorAny",
         "hltESPSmartPropagator",
         "hltESPSteppingHelixPropagatorOpposite" ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    TrackLoaderParameters = cms.PSet(
      PutTkTrackIntoEvent = cms.untracked.bool( True ),
      beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet(
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble(  0.1, 0.1, 5.3  )
      ),
      PutTrajectoryIntoEvent = cms.untracked.bool( None ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True ),
      AllowNoVertex = cms.untracked.bool( None )
    )
)
process.hltL3MuonsOIState = cms.EDProducer( "L3MuonProducer",
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons', 'UpdatedAtVtx' ),
    L3TrajBuilderParameters = cms.PSet(
      ScaleTECyFactor = cms.double( -1.0 ),
      GlbRefitterParameters = cms.PSet(
        TrackerSkipSection = cms.int32( -1 ),
        DoPredictionsOnly = cms.bool( False ),
        PropDirForCosmics = cms.bool( False ),
        HitThreshold = cms.int32( 1 ),
        MuonHitsOption = cms.int32( 1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( 'hltDt4DSegments' ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        CSCRecSegmentLabel = cms.InputTag( 'hltCscSegments' ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        TrackerSkipSystem = cms.int32( -1 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      MuonTrackingRegionBuilder = cms.PSet(
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        OnDemand = cms.double( -1.0 ),
        Rescale_Dz = cms.double( 3.0 ),
        Eta_min = cms.double( 0.05 ),
        Rescale_phi = cms.double( 3.0 ),
        Eta_fixed = cms.double( 0.2 ),
        DeltaZ_Region = cms.double( 15.9 ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        vertexCollection = cms.InputTag( 'pixelVertices' ),
        Phi_fixed = cms.double( 0.2 ),
        DeltaR = cms.double( 0.2 ),
        EscapePt = cms.double( 1.5 ),
        UseFixedRegion = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        Rescale_eta = cms.double( 3.0 ),
        Phi_min = cms.double( 0.05 ),
        UseVertex = cms.bool( False ),
        beamSpot = cms.InputTag( 'hltOnlineBeamSpot' )
      ),
      RefitRPCHits = cms.bool( True ),
      PCut = cms.double( 2.5 ),
      TrackTransformer = cms.PSet(
        DoPredictionsOnly = cms.bool( False ),
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" )
      ),
      GlobalMuonTrackMatcher = cms.PSet(
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        MinP = cms.double( 2.5 ),
        MinPt = cms.double( 1.0 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Pt_threshold2 = cms.double( 999999999.0 ),
        LocChi2Cut = cms.double( 0.001 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_3 = cms.double( 7.0 ),
        Quality_2 = cms.double( 15.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        Quality_1 = cms.double( 20.0 )
      ),
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      tkTrajLabel = cms.InputTag( 'hltL3TkTracksFromL2OIState' )
    ),
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( "hltESPSmartPropagatorAny",
         "SteppingHelixPropagatorAny",
         "hltESPSmartPropagator",
         "hltESPSteppingHelixPropagatorOpposite" ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    TrackLoaderParameters = cms.PSet(
      PutTkTrackIntoEvent = cms.untracked.bool( True ),
      beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
      SmoothTkTrack = cms.untracked.bool( False ),
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
      MuonUpdatorAtVertexParameters = cms.PSet(
        MaxChi2 = cms.double( 1000000.0 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
        BeamSpotPositionErrors = cms.vdouble(  0.1, 0.1, 5.3  )
      ),
      PutTrajectoryIntoEvent = cms.untracked.bool( None ),
      VertexConstraint = cms.bool( False ),
      DoSmoothing = cms.bool( True ),
      AllowNoVertex = cms.untracked.bool( None )
    )
)
process.hltL3TkFromL2OICombination = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3MuonsOIState, hltL3MuonsOIHit' )
)
process.hltL3TkTracksFromL2 = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3TkTracksFromL2IOHit, hltL3TkTracksFromL2OIHit, hltL3TkTracksFromL2OIState' )
)
process.hltL3TkTracksFromL2IOHit = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( True ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    src = cms.InputTag( 'hltL3TrackCandidateFromL2IOHit' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltL3TkTracksFromL2NoVtx = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    src = cms.InputTag( 'hltL3TrackCandidateFromL2NoVtx' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltL3TkTracksFromL2OIHit = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( True ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    src = cms.InputTag( 'hltL3TrackCandidateFromL2OIHit' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltL3TkTracksFromL2OIState = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( True ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "PropagatorWithMaterial" ),
    src = cms.InputTag( 'hltL3TrackCandidateFromL2OIState' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltL3TrackCandidateFromL2 = cms.EDProducer( "L3TrackCandCombiner",
    labels = cms.VInputTag( 'hltL3TrackCandidateFromL2IOHit, hltL3TrackCandidateFromL2OIHit, hltL3TrackCandidateFromL2OIState' )
)
process.hltL3TrackCandidateFromL2IOHit = cms.EDProducer( "CkfTrajectoryMaker",
    trackCandidateAlso = cms.bool( True ),
    src = cms.InputTag( 'hltL3TrajSeedIOHit' ),
    TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    doSeedingRegionRebuilding = cms.bool( False ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TrackCandidateFromL2NoVtx = cms.EDProducer( "CkfTrajectoryMaker",
    trackCandidateAlso = cms.bool( True ),
    src = cms.InputTag( 'hltL3TrajectorySeedNoVtx' ),
    TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "CosmicNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    doSeedingRegionRebuilding = cms.bool( False ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TrackCandidateFromL2OIHit = cms.EDProducer( "CkfTrajectoryMaker",
    trackCandidateAlso = cms.bool( True ),
    src = cms.InputTag( 'hltL3TrajSeedOIHit' ),
    TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    doSeedingRegionRebuilding = cms.bool( False ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TrackCandidateFromL2OIState = cms.EDProducer( "CkfTrajectoryMaker",
    trackCandidateAlso = cms.bool( True ),
    src = cms.InputTag( 'hltL3TrajSeedOIState' ),
    TrajectoryBuilder = cms.string( "hltESPMuonCkfTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    doSeedingRegionRebuilding = cms.bool( False ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TrajSeedIOHit = cms.EDProducer( "TSGFromL2Muon",
    PtCut = cms.double( 1.0 ),
    PCut = cms.double( 2.5 ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons', 'UpdatedAtVtx' ),
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( "PropagatorWithMaterial" ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonTrackingRegionBuilder = cms.PSet(
      EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
      EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
      OnDemand = cms.double( -1.0 ),
      Rescale_Dz = cms.double( 3.0 ),
      Eta_min = cms.double( 0.1 ),
      Rescale_phi = cms.double( 3.0 ),
      Eta_fixed = cms.double( 0.2 ),
      DeltaZ_Region = cms.double( 15.9 ),
      MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
      vertexCollection = cms.InputTag( 'pixelVertices' ),
      Phi_fixed = cms.double( 0.2 ),
      DeltaR = cms.double( 0.2 ),
      EscapePt = cms.double( 1.5 ),
      UseFixedRegion = cms.bool( False ),
      PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
      Rescale_eta = cms.double( 3.0 ),
      Phi_min = cms.double( 0.1 ),
      UseVertex = cms.bool( False ),
      beamSpot = cms.InputTag( 'hltOnlineBeamSpot' )
    ),
    TkSeedGenerator = cms.PSet(
      PSetNames = cms.vstring( "skipTSG",
         "iterativeTSG" ),
      L3TkCollectionA = cms.InputTag( 'hltL3TkFromL2OICombination' ),
      iterativeTSG = cms.PSet(
        firstTSG = cms.PSet(
          ComponentName = cms.string( "TSGFromOrderedHits" ),
          OrderedHitsFactoryPSet = cms.PSet(
            ComponentName = cms.string( "StandardHitTripletGenerator" ),
            GeneratorPSet = cms.PSet(
              useBending = cms.bool( True ),
              useFixedPreFiltering = cms.bool( False ),
              maxElement = cms.uint32( 10000 ),
              phiPreFiltering = cms.double( 0.3 ),
              extraHitRPhitolerance = cms.double( 0.06 ),
              useMultScattering = cms.bool( True ),
              ComponentName = cms.string( "PixelTripletHLTGenerator" ),
              extraHitRZtolerance = cms.double( 0.06 )
            ),
            SeedingLayers = cms.string( "hltESPPixelLayerTriplets" )
          ),
          TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
        ),
        PSetNames = cms.vstring( "firstTSG",
           "secondTSG" ),
        ComponentName = cms.string( "CombinedTSG" ),
        thirdTSG = cms.PSet(
          PSetNames = cms.vstring( "endcapTSG",
             "barrelTSG" ),
          barrelTSG = cms.PSet(  ),
          endcapTSG = cms.PSet(
            ComponentName = cms.string( "TSGFromOrderedHits" ),
            OrderedHitsFactoryPSet = cms.PSet(
              maxElement = cms.uint32( 0 ),
              ComponentName = cms.string( "StandardHitPairGenerator" ),
              SeedingLayers = cms.string( "hltESPMixedLayerPairs" ),
              useOnDemandTracker = cms.untracked.int32( 0 )
            ),
            TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
          ),
          etaSeparation = cms.double( 2.0 ),
          ComponentName = cms.string( "DualByEtaTSG" )
        ),
        secondTSG = cms.PSet(
          ComponentName = cms.string( "TSGFromOrderedHits" ),
          OrderedHitsFactoryPSet = cms.PSet(
            maxElement = cms.uint32( 0 ),
            ComponentName = cms.string( "StandardHitPairGenerator" ),
            SeedingLayers = cms.string( "hltESPPixelLayerPairs" ),
            useOnDemandTracker = cms.untracked.int32( 0 )
          ),
          TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
        )
      ),
      skipTSG = cms.PSet(  ),
      ComponentName = cms.string( "DualByL2TSG" )
    ),
    TrackerSeedCleaner = cms.PSet(
      cleanerFromSharedHits = cms.bool( True ),
      ptCleaner = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
      directionCleaner = cms.bool( True )
    ),
    TSGFromMixedPairs = cms.PSet(  ),
    TSGFromPixelTriplets = cms.PSet(  ),
    TSGFromPixelPairs = cms.PSet(  ),
    TSGForRoadSearchOI = cms.PSet(  ),
    TSGForRoadSearchIOpxl = cms.PSet(  ),
    TSGFromPropagation = cms.PSet(  ),
    TSGFromCombinedHits = cms.PSet(  )
)
process.hltL3TrajSeedOIHit = cms.EDProducer( "TSGFromL2Muon",
    PtCut = cms.double( 1.0 ),
    PCut = cms.double( 2.5 ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons', 'UpdatedAtVtx' ),
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( "PropagatorWithMaterial",
         "hltESPSmartPropagatorAnyOpposite" ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonTrackingRegionBuilder = cms.PSet(
      Eta_fixed = cms.double( None ),
      vertexCollection = cms.InputTag( None ),
      Rescale_eta = cms.double( None ),
      Eta_min = cms.double( None ),
      Rescale_Dz = cms.double( None ),
      EscapePt = cms.double( None ),
      Rescale_phi = cms.double( None ),
      EtaR_UpperLimit_Par1 = cms.double( None ),
      EtaR_UpperLimit_Par2 = cms.double( None ),
      DeltaZ_Region = cms.double( None ),
      PhiR_UpperLimit_Par2 = cms.double( None ),
      Phi_fixed = cms.double( None ),
      PhiR_UpperLimit_Par1 = cms.double( None ),
      DeltaR = cms.double( None ),
      UseVertex = cms.bool( None ),
      OnDemand = cms.double( None ),
      UseFixedRegion = cms.bool( None ),
      Phi_min = cms.double( None )
    ),
    TkSeedGenerator = cms.PSet(
      PSetNames = cms.vstring( "skipTSG",
         "iterativeTSG" ),
      L3TkCollectionA = cms.InputTag( 'hltL3MuonsOIState' ),
      iterativeTSG = cms.PSet(
        ErrorRescaling = cms.double( 3.0 ),
        beamSpot = cms.InputTag( 'offlineBeamSpot' ),
        MaxChi2 = cms.double( 40.0 ),
        errorMatrixPset = cms.PSet(
          atIP = cms.bool( True ),
          action = cms.string( "use" ),
          errorMatrixValuesPSet = cms.PSet(
            pf3_V12 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
            ),
            pf3_V13 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
            ),
            pf3_V11 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble(  3, 3, 3, 5, 4, 5, 10, 7, 10, 10, 10, 10  )
            ),
            pf3_V14 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
            ),
            pf3_V15 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
            ),
            pf3_V34 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
            ),
            yAxis = cms.vdouble(  0, 1, 1.4, 10  ),
            pf3_V33 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble(  3, 3, 3, 5, 4, 5, 10, 7, 10, 10, 10, 10  )
            ),
            pf3_V45 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
            ),
            pf3_V44 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble(  3, 3, 3, 5, 4, 5, 10, 7, 10, 10, 10, 10  )
            ),
            xAxis = cms.vdouble(  0, 13, 30, 70, 1000  ),
            pf3_V23 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
            ),
            pf3_V22 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble(  3, 3, 3, 5, 4, 5, 10, 7, 10, 10, 10, 10  )
            ),
            pf3_V55 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble(  3, 3, 3, 5, 4, 5, 10, 7, 10, 10, 10, 10  )
            ),
            zAxis = cms.vdouble(  -3.14159, 3.14159  ),
            pf3_V35 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
            ),
            pf3_V25 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
            ),
            pf3_V24 = cms.PSet(
              action = cms.string( "scale" ),
              values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
            )
          )
        ),
        UpdateState = cms.bool( True ),
        MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        SelectState = cms.bool( False ),
        SigmaZ = cms.double( 25.0 ),
        ResetMethod = cms.string( "matrix" ),
        ComponentName = cms.string( "TSGFromPropagation" ),
        UseVertexState = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" )
      ),
      skipTSG = cms.PSet(  ),
      ComponentName = cms.string( "DualByL2TSG" )
    ),
    TrackerSeedCleaner = cms.PSet(
      cleanerFromSharedHits = cms.bool( True ),
      ptCleaner = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
      directionCleaner = cms.bool( True )
    ),
    TSGFromMixedPairs = cms.PSet(  ),
    TSGFromPixelTriplets = cms.PSet(  ),
    TSGFromPixelPairs = cms.PSet(  ),
    TSGForRoadSearchOI = cms.PSet(  ),
    TSGForRoadSearchIOpxl = cms.PSet(  ),
    TSGFromPropagation = cms.PSet(  ),
    TSGFromCombinedHits = cms.PSet(  )
)
process.hltL3TrajSeedOIState = cms.EDProducer( "TSGFromL2Muon",
    PtCut = cms.double( 1.0 ),
    PCut = cms.double( 2.5 ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons', 'UpdatedAtVtx' ),
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( "hltESPSteppingHelixPropagatorOpposite",
         "hltESPSteppingHelixPropagatorAlong" ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonTrackingRegionBuilder = cms.PSet(
      Eta_fixed = cms.double( None ),
      vertexCollection = cms.InputTag( None ),
      Rescale_eta = cms.double( None ),
      Eta_min = cms.double( None ),
      Rescale_Dz = cms.double( None ),
      EscapePt = cms.double( None ),
      Rescale_phi = cms.double( None ),
      EtaR_UpperLimit_Par1 = cms.double( None ),
      EtaR_UpperLimit_Par2 = cms.double( None ),
      DeltaZ_Region = cms.double( None ),
      MeasurementTrackerName = cms.string( "" ),
      PhiR_UpperLimit_Par2 = cms.double( None ),
      Phi_fixed = cms.double( None ),
      PhiR_UpperLimit_Par1 = cms.double( None ),
      UseVertex = cms.bool( None ),
      DeltaR = cms.double( None ),
      UseFixedRegion = cms.bool( None ),
      OnDemand = cms.double( None ),
      Phi_min = cms.double( None )
    ),
    TkSeedGenerator = cms.PSet(
      propagatorCompatibleName = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
      option = cms.uint32( 3 ),
      maxChi2 = cms.double( 40.0 ),
      errorMatrixPset = cms.PSet(
        atIP = cms.bool( True ),
        action = cms.string( "use" ),
        errorMatrixValuesPSet = cms.PSet(
          pf3_V12 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          pf3_V13 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          pf3_V11 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  3, 3, 3, 5, 4, 5, 10, 7, 10, 10, 10, 10  )
          ),
          pf3_V14 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          pf3_V15 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          pf3_V34 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          yAxis = cms.vdouble(  0, 1, 1.4, 10  ),
          pf3_V33 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  3, 3, 3, 5, 4, 5, 10, 7, 10, 10, 10, 10  )
          ),
          pf3_V45 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          pf3_V44 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  3, 3, 3, 5, 4, 5, 10, 7, 10, 10, 10, 10  )
          ),
          xAxis = cms.vdouble(  0, 13, 30, 70, 1000  ),
          pf3_V23 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          pf3_V22 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  3, 3, 3, 5, 4, 5, 10, 7, 10, 10, 10, 10  )
          ),
          pf3_V55 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  3, 3, 3, 5, 4, 5, 10, 7, 10, 10, 10, 10  )
          ),
          zAxis = cms.vdouble(  -3.14159, 3.14159  ),
          pf3_V35 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          pf3_V25 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          pf3_V24 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          )
        )
      ),
      propagatorName = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
      manySeeds = cms.bool( False ),
      copyMuonRecHit = cms.bool( False ),
      ComponentName = cms.string( "TSGForRoadSearch" )
    ),
    TrackerSeedCleaner = cms.PSet(
      TTRHBuilder = cms.string( "" ),
      beamSpot = cms.InputTag( None ),
      directionCleaner = cms.bool( None ),
      ptCleaner = cms.bool( None ),
      cleanerFromSharedHits = cms.bool( None )
    ),
    TSGFromMixedPairs = cms.PSet(  ),
    TSGFromPixelTriplets = cms.PSet(  ),
    TSGFromPixelPairs = cms.PSet(  ),
    TSGForRoadSearchOI = cms.PSet(  ),
    TSGForRoadSearchIOpxl = cms.PSet(  ),
    TSGFromPropagation = cms.PSet(  ),
    TSGFromCombinedHits = cms.PSet(  )
)
process.hltL3TrajectorySeed = cms.EDProducer( "L3MuonTrajectorySeedCombiner",
    labels = cms.VInputTag( 'hltL3TrajSeedIOHit, hltL3TrajSeedOIState, hltL3TrajSeedOIHit' )
)
process.hltL3TrajectorySeedNoVtx = cms.EDProducer( "TSGFromL2Muon",
    PtCut = cms.double( 1.0 ),
    PCut = cms.double( 2.5 ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons' ),
    ServiceParameters = cms.PSet(
      Propagators = cms.untracked.vstring( "hltESPSteppingHelixPropagatorOpposite",
         "hltESPSteppingHelixPropagatorAlong" ),
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True )
    ),
    MuonTrackingRegionBuilder = cms.PSet(
      Eta_fixed = cms.double( None ),
      vertexCollection = cms.InputTag( None ),
      Rescale_eta = cms.double( None ),
      Eta_min = cms.double( None ),
      Rescale_Dz = cms.double( None ),
      EscapePt = cms.double( None ),
      Rescale_phi = cms.double( None ),
      EtaR_UpperLimit_Par1 = cms.double( None ),
      EtaR_UpperLimit_Par2 = cms.double( None ),
      DeltaZ_Region = cms.double( None ),
      MeasurementTrackerName = cms.string( "" ),
      PhiR_UpperLimit_Par2 = cms.double( None ),
      Phi_fixed = cms.double( None ),
      PhiR_UpperLimit_Par1 = cms.double( None ),
      UseVertex = cms.bool( None ),
      DeltaR = cms.double( None ),
      UseFixedRegion = cms.bool( None ),
      OnDemand = cms.double( None ),
      Phi_min = cms.double( None )
    ),
    TkSeedGenerator = cms.PSet(
      propagatorCompatibleName = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
      option = cms.uint32( 3 ),
      maxChi2 = cms.double( 40.0 ),
      errorMatrixPset = cms.PSet(
        atIP = cms.bool( True ),
        action = cms.string( "use" ),
        errorMatrixValuesPSet = cms.PSet(
          pf3_V12 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          pf3_V13 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          pf3_V11 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  3, 3, 3, 5, 4, 5, 10, 7, 10, 10, 10, 10  )
          ),
          pf3_V14 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          yAxis = cms.vdouble(  0, 1, 1.4, 10  ),
          pf3_V34 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          pf3_V15 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          pf3_V33 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  3, 3, 3, 5, 4, 5, 10, 7, 10, 10, 10, 10  )
          ),
          pf3_V45 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          pf3_V44 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  3, 3, 3, 5, 4, 5, 10, 7, 10, 10, 10, 10  )
          ),
          xAxis = cms.vdouble(  0, 13, 30, 70, 1000  ),
          pf3_V23 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          pf3_V22 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  3, 3, 3, 5, 4, 5, 10, 7, 10, 10, 10, 10  )
          ),
          pf3_V55 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  3, 3, 3, 5, 4, 5, 10, 7, 10, 10, 10, 10  )
          ),
          zAxis = cms.vdouble(  -3.14159, 3.14159  ),
          pf3_V35 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          pf3_V25 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          ),
          pf3_V24 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble(  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  )
          )
        )
      ),
      propagatorName = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
      manySeeds = cms.bool( False ),
      copyMuonRecHit = cms.bool( False ),
      ComponentName = cms.string( "TSGForRoadSearch" )
    ),
    TrackerSeedCleaner = cms.PSet(
      TTRHBuilder = cms.string( "" ),
      beamSpot = cms.InputTag( None ),
      directionCleaner = cms.bool( None ),
      ptCleaner = cms.bool( None ),
      cleanerFromSharedHits = cms.bool( None )
    ),
    TSGFromMixedPairs = cms.PSet(  ),
    TSGFromPixelTriplets = cms.PSet(  ),
    TSGFromPixelPairs = cms.PSet(  ),
    TSGForRoadSearchOI = cms.PSet(  ),
    TSGForRoadSearchIOpxl = cms.PSet(  ),
    TSGFromPropagation = cms.PSet(  ),
    TSGFromCombinedHits = cms.PSet(  )
)
process.hltLaserAlignmentEventFilter = cms.EDFilter( "LaserAlignmentEventFilter",
    FedInputTag = cms.InputTag( 'source' ),
    SIGNAL_Filter = cms.bool( True ),
    SINGLE_CHANNEL_THRESH = cms.uint32( 11 ),
    CHANNEL_COUNT_THRESH = cms.uint32( 8 ),
    FED_IDs = cms.vint32( 260, 261, 262, 263, 264, 265, 266, 267, 269, 270, 273, 274, 277, 278, 281, 282, 284, 285, 288, 289, 292, 293, 294, 295, 300, 301, 304, 305, 308, 309, 310, 311, 316, 317, 324, 325, 329, 330, 331, 332, 339, 340, 341, 342, 349, 350, 351, 352, 164, 165, 172, 173, 177, 178, 179, 180, 187, 188, 189, 190, 197, 198, 199, 200, 204, 205, 208, 209, 212, 213, 214, 215, 220, 221, 224, 225, 228, 229, 230, 231, 236, 237, 238, 239, 240, 241, 242, 243, 245, 246, 249, 250, 253, 254, 257, 258, 478, 476, 477, 482, 484, 480, 481, 474, 459, 460, 461, 463, 485, 487, 488, 489, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 288, 289, 292, 293, 300, 301, 304, 305, 310, 311, 316, 317, 329, 330, 339, 340, 341, 342, 349, 350, 164, 165, 177, 178, 179, 180, 189, 190, 197, 198, 204, 205, 212, 213, 220, 221, 224, 225, 230, 231 ),
    SIGNAL_IDs = cms.vint32( 470389128, 470389384, 470389640, 470389896, 470390152, 470390408, 470390664, 470390920, 470389192, 470389448, 470389704, 470389960, 470390216, 470390472, 470390728, 470390984, 470126984, 470127240, 470127496, 470127752, 470128008, 470128264, 470128520, 470128776, 470127048, 470127304, 470127560, 470127816, 470128072, 470128328, 470128584, 470128840, 436232506, 436232826, 436233146, 436233466, 369174604, 369174812, 369175068, 369175292, 470307468, 470307716, 470308236, 470308748, 470308996, 470045316, 470045580, 470046084, 470046596, 470046860 )
)
process.hltLightPFTracks = cms.EDProducer( "LightPFTrackProducer",
    UseQuality = cms.bool( False ),
    TrackQuality = cms.string( "none" ),
    TkColList = cms.VInputTag( 'hltPFlowTrackSelectionHighPurity' )
)
process.hltLogMonitorFilter = cms.HLTFilter( "HLTLogMonitorFilter",
    default_threshold = cms.uint32( 10 ),
    categories = cms.VPSet(
    )
)
process.hltMET100 = cms.HLTFilter( "HLT1CaloMET",
    inputTag = cms.InputTag( 'hltMet' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 100.0 ),
    MaxEta = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
process.hltMET120 = cms.HLTFilter( "HLT1CaloMET",
    inputTag = cms.InputTag( 'hltMet' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 120.0 ),
    MaxEta = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
process.hltMET160 = cms.HLTFilter( "HLT1CaloMET",
    inputTag = cms.InputTag( 'hltMet' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 160.0 ),
    MaxEta = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
process.hltMET200 = cms.HLTFilter( "HLT1CaloMET",
    inputTag = cms.InputTag( 'hltMet' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 200.0 ),
    MaxEta = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
process.hltMET65 = cms.HLTFilter( "HLT1CaloMET",
    inputTag = cms.InputTag( 'hltMet' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 65.0 ),
    MaxEta = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
process.hltMET80 = cms.HLTFilter( "HLT1CaloMET",
    inputTag = cms.InputTag( 'hltMet' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 80.0 ),
    MaxEta = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
process.hltMHT30 = cms.HLTFilter( "HLTMhtHtFilter",
    inputJetTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    minMht = cms.double( 30.0 ),
    minNJet = cms.int32( 0 ),
    mode = cms.int32( 1 ),
    usePt = cms.bool( True ),
    minPT12 = cms.double( 0.0 ),
    minMeff = cms.double( 0.0 ),
    minHt = cms.double( 0.0 ),
    minMht2Ht = cms.double( 0.0 ),
    minPtJet = cms.vdouble(  30, 30  ),
    etaJet = cms.vdouble(  3, 3  )
)
process.hltMHT50 = cms.HLTFilter( "HLTMhtHtFilter",
    inputJetTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    minMht = cms.double( 50.0 ),
    minNJet = cms.int32( 0 ),
    mode = cms.int32( 1 ),
    usePt = cms.bool( True ),
    minPT12 = cms.double( 0.0 ),
    minMeff = cms.double( 0.0 ),
    minHt = cms.double( 0.0 ),
    minMht2Ht = cms.double( 0.0 ),
    minPtJet = cms.vdouble(  30, 30  ),
    etaJet = cms.vdouble(  3, 3  )
)
process.hltMHT60 = cms.HLTFilter( "HLTMhtHtFilter",
    inputJetTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    minMht = cms.double( 60.0 ),
    minNJet = cms.int32( 0 ),
    mode = cms.int32( 1 ),
    usePt = cms.bool( True ),
    minPT12 = cms.double( 0.0 ),
    minMeff = cms.double( 0.0 ),
    minHt = cms.double( 0.0 ),
    minMht2Ht = cms.double( 0.0 ),
    minPtJet = cms.vdouble(  30, 30  ),
    etaJet = cms.vdouble(  3, 3  )
)
process.hltMHT75 = cms.HLTFilter( "HLTMhtHtFilter",
    inputJetTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    minMht = cms.double( 75.0 ),
    minNJet = cms.int32( 0 ),
    mode = cms.int32( 1 ),
    usePt = cms.bool( True ),
    minPT12 = cms.double( 0.0 ),
    minMeff = cms.double( 0.0 ),
    minHt = cms.double( 0.0 ),
    minMht2Ht = cms.double( 0.0 ),
    minPtJet = cms.vdouble(  30, 30  ),
    etaJet = cms.vdouble(  3, 3  )
)
process.hltMR100 = cms.HLTFilter( "HLTRFilter",
    inputTag = cms.InputTag( 'hltRHemisphere' ),
    inputMetTag = cms.InputTag( 'hltMet' ),
    minR = cms.double( 0.0 ),
    minMR = cms.double( 100.0 ),
    doRPrime = cms.bool( False ),
    acceptNJ = cms.bool( True )
)
process.hltMeff440 = cms.HLTFilter( "HLTMhtHtFilter",
    inputJetTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    minMht = cms.double( 0.0 ),
    minNJet = cms.int32( 0 ),
    mode = cms.int32( 2 ),
    usePt = cms.bool( True ),
    minPT12 = cms.double( 0.0 ),
    minMeff = cms.double( 440.0 ),
    minHt = cms.double( 0.0 ),
    minMht2Ht = cms.double( 0.0 ),
    minPtJet = cms.vdouble(  40, 30  ),
    etaJet = cms.vdouble(  3, 3  )
)
process.hltMeff520 = cms.HLTFilter( "HLTMhtHtFilter",
    inputJetTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    minMht = cms.double( 0.0 ),
    minNJet = cms.int32( 0 ),
    mode = cms.int32( 2 ),
    usePt = cms.bool( True ),
    minPT12 = cms.double( 0.0 ),
    minMeff = cms.double( 520.0 ),
    minHt = cms.double( 0.0 ),
    minMht2Ht = cms.double( 0.0 ),
    minPtJet = cms.vdouble(  40, 30  ),
    etaJet = cms.vdouble(  3, 3  )
)
process.hltMeff640 = cms.HLTFilter( "HLTMhtHtFilter",
    inputJetTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    minMht = cms.double( 0.0 ),
    minNJet = cms.int32( 0 ),
    mode = cms.int32( 2 ),
    usePt = cms.bool( True ),
    minPT12 = cms.double( 0.0 ),
    minMeff = cms.double( 640.0 ),
    minHt = cms.double( 0.0 ),
    minMht2Ht = cms.double( 0.0 ),
    minPtJet = cms.vdouble(  40, 30  ),
    etaJet = cms.vdouble(  3, 3  )
)
process.hltMet = cms.EDProducer( "METProducer",
    src = cms.InputTag( 'hltTowerMakerForAll' ),
    InputType = cms.string( "CandidateCollection" ),
    METType = cms.string( "CaloMET" ),
    alias = cms.string( "RawCaloMET" ),
    globalThreshold = cms.double( 0.3 ),
    noHF = cms.bool( True ),
    calculateSignificance = cms.bool( False ),
    onlyFiducialParticles = cms.bool( False ),
    usePt = cms.untracked.bool( False ),
    jets = cms.InputTag( 'unused' ),
    rf_type = cms.int32( 0 ),
    correctShowerTracks = cms.bool( False ),
    HO_EtResPar = cms.vdouble(  0, 1.3, 0.005  ),
    HF_EtResPar = cms.vdouble(  0, 1.82, 0.09  ),
    HB_PhiResPar = cms.vdouble(  0.02511  ),
    HE_PhiResPar = cms.vdouble(  0.02511  ),
    EE_EtResPar = cms.vdouble(  0.2, 0.03, 0.005  ),
    EB_PhiResPar = cms.vdouble(  0.00502  ),
    EE_PhiResPar = cms.vdouble(  0.02511  ),
    HB_EtResPar = cms.vdouble(  0, 1.22, 0.05  ),
    EB_EtResPar = cms.vdouble(  0.2, 0.03, 0.005  ),
    HF_PhiResPar = cms.vdouble(  0.05022  ),
    HE_EtResPar = cms.vdouble(  0, 1.3, 0.05  ),
    HO_PhiResPar = cms.vdouble(  0.02511  )
)
process.hltMet45 = cms.HLTFilter( "HLT1CaloMET",
    inputTag = cms.InputTag( 'hltMet' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 45.0 ),
    MaxEta = cms.double( -1.0 ),
    MinN = cms.int32( 1 )
)
process.hltMu15DiPhoton15CaloIdLClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltMu15DiPhoton15R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltMu15DiPhoton15CaloIdLHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltMu15DiPhoton15CaloIdLClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltMu15DiPhoton15R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoubleEG15EtFilterL1Mu3EG5' ),
    isoTag = cms.InputTag( 'hltL1IsoR9shape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9shape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.98 ),
    thrRegularEE = cms.double( 999999.9 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltMu15Photon20CaloIdLClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG20R9ShapeFilterMu3EG5' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltMu15Photon20CaloIdLHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltMu15Photon20CaloIdLClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltMu3EG5L3Filtered5 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL2Mu3EG5L2Filtered3' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltMu3Track3JpsiTrackMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    TrackTag = cms.InputTag( 'hltMuTrackJpsiCtfTrackCands' ),
    PreviousCandTag = cms.InputTag( 'hltMu3TrackJpsiPixelMassFiltered' ),
    SaveTag = cms.untracked.bool( True ),
    checkCharge = cms.bool( True ),
    MinTrackPt = cms.double( 3.0 ),
    MinTrackP = cms.double( 2.7 ),
    MaxTrackEta = cms.double( 999.0 ),
    MaxTrackDxy = cms.double( 999.0 ),
    MaxTrackDz = cms.double( 999.0 ),
    MinTrackHits = cms.int32( 5 ),
    MaxTrackNormChi2 = cms.double( 10000000000.0 ),
    MaxDzMuonTrack = cms.double( 0.5 ),
    CutCowboys = cms.bool( False ),
    MinMasses = cms.vdouble(  2.7  ),
    MaxMasses = cms.vdouble(  3.5  )
)
process.hltMu3TrackJpsiL2Filtered3 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1SingleMu3L1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 2.5 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( False )
)
process.hltMu3TrackJpsiL3Filtered3 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltMu3TrackJpsiL2Filtered3' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltMu3TrackJpsiPixelMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    TrackTag = cms.InputTag( 'hltMuTrackJpsiPixelTrackCands' ),
    PreviousCandTag = cms.InputTag( 'hltMu3TrackJpsiL3Filtered3' ),
    SaveTag = cms.untracked.bool( True ),
    checkCharge = cms.bool( False ),
    MinTrackPt = cms.double( 2.5 ),
    MinTrackP = cms.double( 2.5 ),
    MaxTrackEta = cms.double( 999.0 ),
    MaxTrackDxy = cms.double( 999.0 ),
    MaxTrackDz = cms.double( 999.0 ),
    MinTrackHits = cms.int32( 3 ),
    MaxTrackNormChi2 = cms.double( 10000000000.0 ),
    MaxDzMuonTrack = cms.double( 999.0 ),
    CutCowboys = cms.bool( False ),
    MinMasses = cms.vdouble(  2.1  ),
    MaxMasses = cms.vdouble(  4.5  )
)
process.hltMu5L2Mu0L3Filtered5 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltMu5L2Mu2L2PreFiltered0' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltMu5L2Mu2JpsiTrackMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    TrackTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltMu5L2Mu0L3Filtered5' ),
    SaveTag = cms.untracked.bool( True ),
    checkCharge = cms.bool( True ),
    MinTrackPt = cms.double( 2.0 ),
    MinTrackP = cms.double( 0.0 ),
    MaxTrackEta = cms.double( 999.0 ),
    MaxTrackDxy = cms.double( 999.0 ),
    MaxTrackDz = cms.double( 999.0 ),
    MinTrackHits = cms.int32( 2 ),
    MaxTrackNormChi2 = cms.double( 999999999.0 ),
    MaxDzMuonTrack = cms.double( 99999.0 ),
    CutCowboys = cms.bool( False ),
    MinMasses = cms.vdouble(  1.8  ),
    MaxMasses = cms.vdouble(  4.5  )
)
process.hltMu5L2Mu2L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1DoubleMu05' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltMu5L2Mu2L2PreFiltered0 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltMu5L2Mu2L1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 2.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltMu5NoVertexL3PreFiltered5 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidatesNoVtx' ),
    PreviousCandTag = cms.InputTag( 'hltSingleL2MuORL2PreFilteredNoVtx' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 6 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltMu5TkMuJpsiTkMuMassFilteredTight = cms.HLTFilter( "HLTMuonTrackMassFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    TrackTag = cms.InputTag( 'hltMuTkMuJpsiTrackerMuonCands' ),
    PreviousCandTag = cms.InputTag( 'hltMu5TkMuJpsiTrackMassFiltered' ),
    SaveTag = cms.untracked.bool( True ),
    checkCharge = cms.bool( True ),
    MinTrackPt = cms.double( 0.0 ),
    MinTrackP = cms.double( 2.7 ),
    MaxTrackEta = cms.double( 999.0 ),
    MaxTrackDxy = cms.double( 999.0 ),
    MaxTrackDz = cms.double( 999.0 ),
    MinTrackHits = cms.int32( 5 ),
    MaxTrackNormChi2 = cms.double( 10000000000.0 ),
    MaxDzMuonTrack = cms.double( 0.5 ),
    CutCowboys = cms.bool( True ),
    MinMasses = cms.vdouble(  2.5  ),
    MaxMasses = cms.vdouble(  4.1  )
)
process.hltMu5TkMuJpsiTrackMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    TrackTag = cms.InputTag( 'hltMuTrackJpsiCtfTrackCands' ),
    PreviousCandTag = cms.InputTag( 'hltMu5TrackJpsiPixelMassFilteredEta15' ),
    SaveTag = cms.untracked.bool( True ),
    checkCharge = cms.bool( True ),
    MinTrackPt = cms.double( 0.0 ),
    MinTrackP = cms.double( 2.7 ),
    MaxTrackEta = cms.double( 999.0 ),
    MaxTrackDxy = cms.double( 999.0 ),
    MaxTrackDz = cms.double( 999.0 ),
    MinTrackHits = cms.int32( 5 ),
    MaxTrackNormChi2 = cms.double( 10000000000.0 ),
    MaxDzMuonTrack = cms.double( 0.5 ),
    CutCowboys = cms.bool( False ),
    MinMasses = cms.vdouble(  2.5  ),
    MaxMasses = cms.vdouble(  4.1  )
)
process.hltMu5TrackJpsiL1Filtered0Eta15 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1SingleMu5BQ7' ),
    MaxEta = cms.double( 1.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltMu5TrackJpsiL2Filtered5Eta15 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltMu5TrackJpsiL1Filtered0Eta15' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( False )
)
process.hltMu5TrackJpsiL3Filtered5Eta15 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltMu5TrackJpsiL2Filtered5Eta15' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltMu5TrackJpsiPixelMassFilteredEta15 = cms.HLTFilter( "HLTMuonTrackMassFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    TrackTag = cms.InputTag( 'hltMuTrackJpsiPixelTrackCands' ),
    PreviousCandTag = cms.InputTag( 'hltMu5TrackJpsiL3Filtered5Eta15' ),
    SaveTag = cms.untracked.bool( True ),
    checkCharge = cms.bool( False ),
    MinTrackPt = cms.double( 0.0 ),
    MinTrackP = cms.double( 2.5 ),
    MaxTrackEta = cms.double( 999.0 ),
    MaxTrackDxy = cms.double( 999.0 ),
    MaxTrackDz = cms.double( 999.0 ),
    MinTrackHits = cms.int32( 3 ),
    MaxTrackNormChi2 = cms.double( 10000000000.0 ),
    MaxDzMuonTrack = cms.double( 999.0 ),
    CutCowboys = cms.bool( False ),
    MinMasses = cms.vdouble(  2  ),
    MaxMasses = cms.vdouble(  4.6  )
)
process.hltMu7Track5JpsiTrackMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    TrackTag = cms.InputTag( 'hltMuTrackJpsiCtfTrackCands' ),
    PreviousCandTag = cms.InputTag( 'hltMu7TrackJpsiPixelMassFiltered' ),
    SaveTag = cms.untracked.bool( True ),
    checkCharge = cms.bool( True ),
    MinTrackPt = cms.double( 5.0 ),
    MinTrackP = cms.double( 2.7 ),
    MaxTrackEta = cms.double( 999.0 ),
    MaxTrackDxy = cms.double( 999.0 ),
    MaxTrackDz = cms.double( 999.0 ),
    MinTrackHits = cms.int32( 5 ),
    MaxTrackNormChi2 = cms.double( 10000000000.0 ),
    MaxDzMuonTrack = cms.double( 0.5 ),
    CutCowboys = cms.bool( False ),
    MinMasses = cms.vdouble(  2.7  ),
    MaxMasses = cms.vdouble(  3.5  )
)
process.hltMu7Track7JpsiTrackMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    TrackTag = cms.InputTag( 'hltMuTrackJpsiCtfTrackCands' ),
    PreviousCandTag = cms.InputTag( 'hltMu7TrackJpsiPixelMassFiltered' ),
    SaveTag = cms.untracked.bool( True ),
    checkCharge = cms.bool( True ),
    MinTrackPt = cms.double( 7.0 ),
    MinTrackP = cms.double( 2.7 ),
    MaxTrackEta = cms.double( 999.0 ),
    MaxTrackDxy = cms.double( 999.0 ),
    MaxTrackDz = cms.double( 999.0 ),
    MinTrackHits = cms.int32( 5 ),
    MaxTrackNormChi2 = cms.double( 10000000000.0 ),
    MaxDzMuonTrack = cms.double( 0.5 ),
    CutCowboys = cms.bool( False ),
    MinMasses = cms.vdouble(  2.7  ),
    MaxMasses = cms.vdouble(  3.5  )
)
process.hltMu7TrackJpsiL2Filtered3 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1SingleMu7L1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 6.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( False )
)
process.hltMu7TrackJpsiL3Filtered3 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltMu7TrackJpsiL2Filtered3' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 7.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltMu7TrackJpsiPixelMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    TrackTag = cms.InputTag( 'hltMuTrackJpsiPixelTrackCands' ),
    PreviousCandTag = cms.InputTag( 'hltMu7TrackJpsiL3Filtered3' ),
    SaveTag = cms.untracked.bool( True ),
    checkCharge = cms.bool( False ),
    MinTrackPt = cms.double( 4.0 ),
    MinTrackP = cms.double( 2.5 ),
    MaxTrackEta = cms.double( 999.0 ),
    MaxTrackDxy = cms.double( 999.0 ),
    MaxTrackDz = cms.double( 999.0 ),
    MinTrackHits = cms.int32( 3 ),
    MaxTrackNormChi2 = cms.double( 10000000000.0 ),
    MaxDzMuonTrack = cms.double( 999.0 ),
    CutCowboys = cms.bool( False ),
    MinMasses = cms.vdouble(  2  ),
    MaxMasses = cms.vdouble(  4.6  )
)
process.hltMuTkMuJpsiTrackerMuonCands = cms.EDProducer( "L3MuonCandidateProducerFromMuons",
    InputObjects = cms.InputTag( 'hltMuTkMuJpsiTrackerMuons' )
)
process.hltMuTkMuJpsiTrackerMuons = cms.EDProducer( "MuonIdProducer",
    minPt = cms.double( 0.0 ),
    minP = cms.double( 2.7 ),
    minPCaloMuon = cms.double( 1.0 ),
    minNumberOfMatches = cms.int32( 1 ),
    addExtraSoftMuons = cms.bool( False ),
    maxAbsEta = cms.double( 999.0 ),
    maxAbsDx = cms.double( 3.0 ),
    maxAbsPullX = cms.double( 3.0 ),
    maxAbsDy = cms.double( 3.0 ),
    maxAbsPullY = cms.double( 3.0 ),
    fillCaloCompatibility = cms.bool( False ),
    fillEnergy = cms.bool( False ),
    fillMatching = cms.bool( True ),
    fillIsolation = cms.bool( False ),
    writeIsoDeposits = cms.bool( False ),
    fillGlobalTrackQuality = cms.bool( False ),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double( 200.0 ),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double( 2.0 ),
    minCaloCompatibility = cms.double( 0.6 ),
    runArbitrationCleaner = cms.bool( False ),
    trackDepositName = cms.string( "tracker" ),
    ecalDepositName = cms.string( "ecal" ),
    hcalDepositName = cms.string( "hcal" ),
    hoDepositName = cms.string( "ho" ),
    jetDepositName = cms.string( "jets" ),
    debugWithTruthMatching = cms.bool( False ),
    globalTrackQualityInputTag = cms.InputTag( 'glbTrackQual' ),
    inputCollectionLabels = cms.VInputTag( 'hltMuTrackJpsiCtfTracks' ),
    inputCollectionTypes = cms.vstring( "inner tracks" ),
    arbitrationCleanerOptions = cms.PSet(
      Clustering = cms.bool( True ),
      ME1a = cms.bool( True ),
      ClusterDPhi = cms.double( 0.6 ),
      OverlapDTheta = cms.double( 0.02 ),
      Overlap = cms.bool( True ),
      OverlapDPhi = cms.double( 0.0786 ),
      ClusterDTheta = cms.double( 0.02 )
    ),
    TrackAssociatorParameters = cms.PSet(
      muonMaxDistanceSigmaX = cms.double( 0.0 ),
      muonMaxDistanceSigmaY = cms.double( 0.0 ),
      CSCSegmentCollectionLabel = cms.InputTag( 'hltCscSegments' ),
      dRHcal = cms.double( 9999.0 ),
      dRPreshowerPreselection = cms.double( 0.2 ),
      CaloTowerCollectionLabel = cms.InputTag( 'towerMaker' ),
      useEcal = cms.bool( False ),
      dREcal = cms.double( 9999.0 ),
      dREcalPreselection = cms.double( 0.05 ),
      HORecHitCollectionLabel = cms.InputTag( 'hltHoreco' ),
      dRMuon = cms.double( 9999.0 ),
      propagateAllDirections = cms.bool( True ),
      muonMaxDistanceX = cms.double( 5.0 ),
      muonMaxDistanceY = cms.double( 5.0 ),
      useHO = cms.bool( False ),
      trajectoryUncertaintyTolerance = cms.double( -1.0 ),
      usePreshower = cms.bool( False ),
      DTRecSegment4DCollectionLabel = cms.InputTag( 'hltDt4DSegments' ),
      EERecHitCollectionLabel = cms.InputTag( 'ecalRecHit', 'EcalRecHitsEE' ),
      dRHcalPreselection = cms.double( 0.2 ),
      useMuon = cms.bool( True ),
      useCalo = cms.bool( False ),
      accountForTrajectoryChangeCalo = cms.bool( False ),
      EBRecHitCollectionLabel = cms.InputTag( 'ecalRecHit', 'EcalRecHitsEB' ),
      dRMuonPreselection = cms.double( 0.2 ),
      truthMatch = cms.bool( False ),
      HBHERecHitCollectionLabel = cms.InputTag( 'hbhereco' ),
      useHcal = cms.bool( False )
    ),
    TimingFillerParameters = cms.PSet(
      UseDT = cms.bool( True ),
      ErrorDT = cms.double( 3.1 ),
      EcalEnergyCut = cms.double( 0.4 ),
      ErrorEB = cms.double( 2.085 ),
      ErrorCSC = cms.double( 7.0 ),
      CSCTimingParameters = cms.PSet(
        CSCsegments = cms.InputTag( 'hltCscSegments' ),
        CSCTimeOffset = cms.double( 213.0 ),
        MatchParameters = cms.PSet(
          CSCsegments = cms.InputTag( 'hltCscSegments' ),
          DTsegments = cms.InputTag( 'hltDthlt4DSegments' ),
          TightMatchDT = cms.bool( False ),
          TightMatchCSC = cms.bool( True ),
          DTradius = cms.double( 0.01 )
        ),
        ServiceParameters = cms.PSet(
          Propagators = cms.untracked.vstring( "SteppingHelixPropagatorAny",
             "PropagatorWithMaterial",
             "PropagatorWithMaterialOpposite" ),
          RPCLayers = cms.bool( True )
        ),
        debug = cms.bool( False ),
        PruneCut = cms.double( 100.0 ),
        CSCStripTimeOffset = cms.double( 0.0 ),
        CSCStripError = cms.double( 7.0 ),
        UseStripTime = cms.bool( True ),
        CSCWireError = cms.double( 8.6 ),
        CSCWireTimeOffset = cms.double( 0.0 ),
        UseWireTime = cms.bool( True )
      ),
      DTTimingParameters = cms.PSet(
        DoWireCorr = cms.bool( False ),
        PruneCut = cms.double( 1000.0 ),
        DTsegments = cms.InputTag( 'hltDthlt4DSegments' ),
        ServiceParameters = cms.PSet(
          Propagators = cms.untracked.vstring( "SteppingHelixPropagatorAny",
             "PropagatorWithMaterial",
             "PropagatorWithMaterialOpposite" ),
          RPCLayers = cms.bool( True )
        ),
        RequireBothProjections = cms.bool( False ),
        HitsMin = cms.int32( 3 ),
        DTTimeOffset = cms.double( 2.7 ),
        debug = cms.bool( False ),
        UseSegmentT0 = cms.bool( False ),
        MatchParameters = cms.PSet(
          CSCsegments = cms.InputTag( 'hltCscSegments' ),
          DTsegments = cms.InputTag( 'hltDthlt4DSegments' ),
          TightMatchDT = cms.bool( False ),
          TightMatchCSC = cms.bool( True ),
          DTradius = cms.double( 0.01 )
        ),
        HitError = cms.double( 6.0 ),
        DropTheta = cms.bool( True )
      ),
      ErrorEE = cms.double( 6.95 ),
      UseCSC = cms.bool( True ),
      UseECAL = cms.bool( False )
    ),
    JetExtractorPSet = cms.PSet(  ),
    TrackExtractorPSet = cms.PSet(  ),
    MuonCaloCompatibility = cms.PSet(  ),
    CaloExtractorPSet = cms.PSet(
      ComponentName = cms.string( "CaloExtractorByAssociator" )
    )
)
process.hltMuTrackJpsiCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( 'hltMuTrackJpsiTrackSeeds' ),
    TrajectoryBuilder = cms.string( "hltESPMuTrackJpsiTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltMuTrackJpsiCtfTrackCands = cms.EDProducer( "ConcreteChargedCandidateProducer",
    src = cms.InputTag( 'hltMuTrackJpsiCtfTracks' ),
    particleType = cms.string( "mu-" )
)
process.hltMuTrackJpsiCtfTracks = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( True ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "hltMuTrackJpsiCtfTracks" ),
    Fitter = cms.string( "hltESPFittingSmootherRK" ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
    src = cms.InputTag( 'hltMuTrackJpsiCkfTrackCandidates' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltMuTrackJpsiPixelTrackCands = cms.EDProducer( "ConcreteChargedCandidateProducer",
    src = cms.InputTag( 'hltMuTrackJpsiPixelTrackSelector' ),
    particleType = cms.string( "mu-" )
)
process.hltMuTrackJpsiPixelTrackSelector = cms.EDProducer( "QuarkoniaTrackSelector",
    muonCandidates = cms.InputTag( 'hltL3MuonCandidates' ),
    tracks = cms.InputTag( 'hltPixelTracks' ),
    checkCharge = cms.bool( False ),
    MinTrackPt = cms.double( 0.0 ),
    MinTrackP = cms.double( 2.5 ),
    MaxTrackEta = cms.double( 999.0 ),
    MinMasses = cms.vdouble(  2  ),
    MaxMasses = cms.vdouble(  4.6  )
)
process.hltMuTrackJpsiTrackSeeds = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    InputCollection = cms.InputTag( 'hltMuTrackJpsiPixelTrackSelector' ),
    useProtoTrackKinematics = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltMulti5x5BasicClustersActivity = cms.EDProducer( "Multi5x5ClusterProducer",
    VerbosityLevel = cms.string( "ERROR" ),
    barrelHitProducer = cms.string( "hltEcalRecHitAll" ),
    endcapHitProducer = cms.string( "hltEcalRecHitAll" ),
    barrelHitCollection = cms.string( "EcalRecHitsEB" ),
    endcapHitCollection = cms.string( "EcalRecHitsEE" ),
    doEndcap = cms.bool( True ),
    doBarrel = cms.bool( False ),
    barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    IslandBarrelSeedThr = cms.double( 0.5 ),
    IslandEndcapSeedThr = cms.double( 0.18 ),
    RecHitFlagToBeExcluded = cms.vint32(  ),
    posCalcParameters = cms.PSet(
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    )
)
process.hltMulti5x5BasicClustersL1Isolated = cms.EDProducer( "EgammaHLTMulti5x5ClusterProducer",
    VerbosityLevel = cms.string( "ERROR" ),
    doBarrel = cms.bool( False ),
    doEndcaps = cms.bool( True ),
    doIsolated = cms.bool( True ),
    barrelHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit' ),
    endcapHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit' ),
    barrelHitCollection = cms.string( "EcalRecHitsEB" ),
    endcapHitCollection = cms.string( "EcalRecHitsEE" ),
    barrelClusterCollection = cms.string( "notused" ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    Multi5x5BarrelSeedThr = cms.double( 0.5 ),
    Multi5x5EndcapSeedThr = cms.double( 0.18 ),
    l1TagIsolated = cms.InputTag( 'hltL1extraParticles', 'Isolated' ),
    l1TagNonIsolated = cms.InputTag( 'hltL1extraParticles', 'NonIsolated' ),
    l1LowerThr = cms.double( 5.0 ),
    l1UpperThr = cms.double( 999.0 ),
    l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
    regionEtaMargin = cms.double( 0.3 ),
    regionPhiMargin = cms.double( 0.4 ),
    RecHitFlagToBeExcluded = cms.vint32(  ),
    posCalcParameters = cms.PSet(
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    )
)
process.hltMulti5x5BasicClustersL1NonIsolated = cms.EDProducer( "EgammaHLTMulti5x5ClusterProducer",
    VerbosityLevel = cms.string( "ERROR" ),
    doBarrel = cms.bool( False ),
    doEndcaps = cms.bool( True ),
    doIsolated = cms.bool( False ),
    barrelHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit' ),
    endcapHitProducer = cms.InputTag( 'hltEcalRegionalEgammaRecHit' ),
    barrelHitCollection = cms.string( "EcalRecHitsEB" ),
    endcapHitCollection = cms.string( "EcalRecHitsEE" ),
    barrelClusterCollection = cms.string( "notused" ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    Multi5x5BarrelSeedThr = cms.double( 0.5 ),
    Multi5x5EndcapSeedThr = cms.double( 0.18 ),
    l1TagIsolated = cms.InputTag( 'hltL1extraParticles', 'Isolated' ),
    l1TagNonIsolated = cms.InputTag( 'hltL1extraParticles', 'NonIsolated' ),
    l1LowerThr = cms.double( 5.0 ),
    l1UpperThr = cms.double( 999.0 ),
    l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
    regionEtaMargin = cms.double( 0.3 ),
    regionPhiMargin = cms.double( 0.4 ),
    RecHitFlagToBeExcluded = cms.vint32(  ),
    posCalcParameters = cms.PSet(
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    )
)
process.hltMulti5x5EndcapSuperClustersWithPreshowerL1Isolated = cms.EDProducer( "PreshowerClusterProducer",
    preshRecHitProducer = cms.InputTag( 'hltESRegionalEgammaRecHit', 'EcalRecHitsES' ),
    endcapSClusterProducer = cms.InputTag( 'hltMulti5x5SuperClustersL1Isolated', 'multi5x5EndcapSuperClusters' ),
    preshClusterCollectionX = cms.string( "preshowerXClusters" ),
    preshClusterCollectionY = cms.string( "preshowerYClusters" ),
    preshNclust = cms.int32( 4 ),
    etThresh = cms.double( 5.0 ),
    assocSClusterCollection = cms.string( "" ),
    preshStripEnergyCut = cms.double( 0.0 ),
    preshSeededNstrip = cms.int32( 15 ),
    preshClusterEnergyCut = cms.double( 0.0 ),
    debugLevel = cms.string( "" )
)
process.hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated = cms.EDProducer( "PreshowerClusterProducer",
    preshRecHitProducer = cms.InputTag( 'hltESRegionalEgammaRecHit', 'EcalRecHitsES' ),
    endcapSClusterProducer = cms.InputTag( 'hltMulti5x5SuperClustersL1NonIsolated', 'multi5x5EndcapSuperClusters' ),
    preshClusterCollectionX = cms.string( "preshowerXClusters" ),
    preshClusterCollectionY = cms.string( "preshowerYClusters" ),
    preshNclust = cms.int32( 4 ),
    etThresh = cms.double( 5.0 ),
    assocSClusterCollection = cms.string( "" ),
    preshStripEnergyCut = cms.double( 0.0 ),
    preshSeededNstrip = cms.int32( 15 ),
    preshClusterEnergyCut = cms.double( 0.0 ),
    debugLevel = cms.string( "" )
)
process.hltMulti5x5SuperClustersActivity = cms.EDProducer( "Multi5x5SuperClusterProducer",
    VerbosityLevel = cms.string( "ERROR" ),
    endcapClusterProducer = cms.string( "hltMulti5x5BasicClustersActivity" ),
    barrelClusterProducer = cms.string( "hltMulti5x5BasicClustersActivity" ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
    endcapSuperclusterCollection = cms.string( "multi5x5EndcapSuperClusters" ),
    barrelSuperclusterCollection = cms.string( "multi5x5BarrelSuperClusters" ),
    doBarrel = cms.bool( False ),
    doEndcaps = cms.bool( True ),
    barrelEtaSearchRoad = cms.double( 0.06 ),
    barrelPhiSearchRoad = cms.double( 0.8 ),
    endcapEtaSearchRoad = cms.double( 0.14 ),
    endcapPhiSearchRoad = cms.double( 0.6 ),
    seedTransverseEnergyThreshold = cms.double( 1.0 ),
    dynamicPhiRoad = cms.bool( False ),
    bremRecoveryPset = cms.PSet(
      barrel = cms.PSet(
        cryVec = cms.vint32( 16, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3 ),
        cryMin = cms.int32( 2 ),
        etVec = cms.vdouble(  5, 10, 15, 20, 30, 40, 45, 55, 135, 195, 225  )
      ),
      endcap = cms.PSet(
        a = cms.double( 47.85 ),
        c = cms.double( 0.1201 ),
        b = cms.double( 108.8 )
      )
    )
)
process.hltMulti5x5SuperClustersL1Isolated = cms.EDProducer( "Multi5x5SuperClusterProducer",
    VerbosityLevel = cms.string( "ERROR" ),
    endcapClusterProducer = cms.string( "hltMulti5x5BasicClustersL1Isolated" ),
    barrelClusterProducer = cms.string( "notused" ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
    endcapSuperclusterCollection = cms.string( "multi5x5EndcapSuperClusters" ),
    barrelSuperclusterCollection = cms.string( "multi5x5BarrelSuperClusters" ),
    doBarrel = cms.bool( False ),
    doEndcaps = cms.bool( True ),
    barrelEtaSearchRoad = cms.double( 0.06 ),
    barrelPhiSearchRoad = cms.double( 0.8 ),
    endcapEtaSearchRoad = cms.double( 0.14 ),
    endcapPhiSearchRoad = cms.double( 0.6 ),
    seedTransverseEnergyThreshold = cms.double( 1.0 ),
    dynamicPhiRoad = cms.bool( False ),
    bremRecoveryPset = cms.PSet(
      barrel = cms.PSet(  ),
      endcap = cms.PSet(
        a = cms.double( 47.85 ),
        c = cms.double( 0.1201 ),
        b = cms.double( 108.8 )
      ),
      doEndcaps = cms.bool( True ),
      doBarrel = cms.bool( False )
    )
)
process.hltMulti5x5SuperClustersL1NonIsolated = cms.EDProducer( "Multi5x5SuperClusterProducer",
    VerbosityLevel = cms.string( "ERROR" ),
    endcapClusterProducer = cms.string( "hltMulti5x5BasicClustersL1NonIsolated" ),
    barrelClusterProducer = cms.string( "notused" ),
    endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
    barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
    endcapSuperclusterCollection = cms.string( "multi5x5EndcapSuperClusters" ),
    barrelSuperclusterCollection = cms.string( "multi5x5BarrelSuperClusters" ),
    doBarrel = cms.bool( False ),
    doEndcaps = cms.bool( True ),
    barrelEtaSearchRoad = cms.double( 0.06 ),
    barrelPhiSearchRoad = cms.double( 0.8 ),
    endcapEtaSearchRoad = cms.double( 0.14 ),
    endcapPhiSearchRoad = cms.double( 0.6 ),
    seedTransverseEnergyThreshold = cms.double( 1.0 ),
    dynamicPhiRoad = cms.bool( False ),
    bremRecoveryPset = cms.PSet(
      barrel = cms.PSet(  ),
      endcap = cms.PSet(
        a = cms.double( 47.85 ),
        c = cms.double( 0.1201 ),
        b = cms.double( 108.8 )
      ),
      doEndcaps = cms.bool( True ),
      doBarrel = cms.bool( False )
    )
)
process.hltMulti5x5SuperClustersWithPreshowerActivity = cms.EDProducer( "PreshowerClusterProducer",
    preshRecHitProducer = cms.InputTag( 'hltESRecHitAll', 'EcalRecHitsES' ),
    endcapSClusterProducer = cms.InputTag( 'hltMulti5x5SuperClustersActivity', 'multi5x5EndcapSuperClusters' ),
    preshClusterCollectionX = cms.string( "preshowerXClusters" ),
    preshClusterCollectionY = cms.string( "preshowerYClusters" ),
    preshNclust = cms.int32( 4 ),
    etThresh = cms.double( 0.0 ),
    assocSClusterCollection = cms.string( "" ),
    preshStripEnergyCut = cms.double( 0.0 ),
    preshSeededNstrip = cms.int32( 15 ),
    preshClusterEnergyCut = cms.double( 0.0 ),
    debugLevel = cms.string( "ERROR" )
)
process.hltMuonCSCDigis = cms.EDProducer( "CSCDCCUnpacker",
    InputObjects = cms.InputTag( 'source' ),
    UseExaminer = cms.bool( True ),
    ExaminerMask = cms.uint32( 535557110 ),
    UseSelectiveUnpacking = cms.bool( True ),
    ErrorMask = cms.uint32( 0 ),
    UnpackStatusDigis = cms.bool( False ),
    UseFormatStatus = cms.bool( True ),
    PrintEventNumber = cms.untracked.bool( False ),
    Debug = cms.untracked.bool( False ),
    runDQM = cms.untracked.bool( False ),
    VisualFEDInspect = cms.untracked.bool( False ),
    VisualFEDShort = cms.untracked.bool( False ),
    FormatedEventDump = cms.untracked.bool( False ),
    SuppressZeroLCT = cms.untracked.bool( True )
)
process.hltMuonDTDigis = cms.EDProducer( "DTUnpackingModule",
    dataType = cms.string( "DDU" ),
    fedbyType = cms.bool( False ),
    inputLabel = cms.InputTag( 'source' ),
    useStandardFEDid = cms.bool( True ),
    minFEDid = cms.untracked.int32( 770 ),
    maxFEDid = cms.untracked.int32( 779 ),
    dqmOnly = cms.bool( False ),
    rosParameters = cms.PSet(  ),
    readOutParameters = cms.PSet(
      debug = cms.untracked.bool( False ),
      rosParameters = cms.PSet(
        writeSC = cms.untracked.bool( True ),
        readingDDU = cms.untracked.bool( True ),
        dduID = cms.untracked.int32( None ),
        performDataIntegrityMonitor = cms.untracked.bool( False ),
        readDDUIDfromDDU = cms.untracked.bool( True ),
        debug = cms.untracked.bool( False ),
        localDAQ = cms.untracked.bool( False )
      ),
      localDAQ = cms.untracked.bool( False ),
      performDataIntegrityMonitor = cms.untracked.bool( False ),
      debugMode = cms.untracked.bool( None )
    )
)
process.hltMuonRPCDigis = cms.EDProducer( "RPCUnpackingModule",
    InputLabel = cms.InputTag( 'source' ),
    doSynchro = cms.bool( False )
)
process.hltOfflineBeamSpot = cms.EDProducer( "BeamSpotProducer" )
process.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    label = cms.InputTag( 'hltScalersRawToDigi' ),
    changeToCMSCoordinates = cms.bool( False ),
    maxRadius = cms.double( 2.0 ),
    maxZ = cms.double( 40.0 ),
    setSigmaZ = cms.double( 10.0 ),
    gtEvmLabel = cms.InputTag( "" )
)
process.hltOverlapFilterEle15CaloJet5 = cms.HLTFilter( "HLT2ElectronTau",
    inputTag1 = cms.InputTag( 'hltEle15CaloIdVTTrkIdTDphiFilter' ),
    inputTag2 = cms.InputTag( 'hltTauJet5' ),
    saveTags = cms.untracked.bool( False ),
    MinDphi = cms.double( 0.0 ),
    MaxDphi = cms.double( 9999.0 ),
    MinDeta = cms.double( 0.0 ),
    MaxDeta = cms.double( 9999.0 ),
    MinMinv = cms.double( 0.0 ),
    MaxMinv = cms.double( 14000.0 ),
    MinDelR = cms.double( 0.3 ),
    MaxDelR = cms.double( 99999.0 ),
    MinN = cms.int32( 1 )
)
process.hltOverlapFilterEle15IsoPFTau15 = cms.HLTFilter( "HLT2ElectronTau",
    inputTag1 = cms.InputTag( 'hltEle15CaloIdVTTrkIdTDphiFilter' ),
    inputTag2 = cms.InputTag( 'hltPFTau15TrackLooseIso' ),
    saveTags = cms.untracked.bool( True ),
    MinDphi = cms.double( 0.0 ),
    MaxDphi = cms.double( 1000.0 ),
    MinDeta = cms.double( 0.0 ),
    MaxDeta = cms.double( 1000.0 ),
    MinMinv = cms.double( 0.0 ),
    MaxMinv = cms.double( 14000.0 ),
    MinDelR = cms.double( 0.3 ),
    MaxDelR = cms.double( 1000.0 ),
    MinN = cms.int32( 1 )
)
process.hltOverlapFilterIsoEle15CaloJet5 = cms.HLTFilter( "HLT2ElectronTau",
    inputTag1 = cms.InputTag( 'hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTTrackIsolFilter' ),
    inputTag2 = cms.InputTag( 'hltTauJet5' ),
    saveTags = cms.untracked.bool( False ),
    MinDphi = cms.double( 0.0 ),
    MaxDphi = cms.double( 9999.0 ),
    MinDeta = cms.double( 0.0 ),
    MaxDeta = cms.double( 9999.0 ),
    MinMinv = cms.double( 0.0 ),
    MaxMinv = cms.double( 14000.0 ),
    MinDelR = cms.double( 0.3 ),
    MaxDelR = cms.double( 99999.0 ),
    MinN = cms.int32( 1 )
)
process.hltOverlapFilterIsoEle15IsoPFTau15 = cms.HLTFilter( "HLT2ElectronTau",
    inputTag1 = cms.InputTag( 'hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTTrackIsolFilter' ),
    inputTag2 = cms.InputTag( 'hltPFTau15TrackLooseIso' ),
    saveTags = cms.untracked.bool( True ),
    MinDphi = cms.double( 0.0 ),
    MaxDphi = cms.double( 1000.0 ),
    MinDeta = cms.double( 0.0 ),
    MaxDeta = cms.double( 1000.0 ),
    MinMinv = cms.double( 0.0 ),
    MaxMinv = cms.double( 14000.0 ),
    MinDelR = cms.double( 0.3 ),
    MaxDelR = cms.double( 1000.0 ),
    MinN = cms.int32( 1 )
)
process.hltOverlapFilterIsoEle15IsoPFTau20 = cms.HLTFilter( "HLT2ElectronTau",
    inputTag1 = cms.InputTag( 'hltEle15CaloIdVTTrkIdTCaloIsoTTrkIsoTTrackIsolFilter' ),
    inputTag2 = cms.InputTag( 'hltPFTau20TrackLooseIso' ),
    saveTags = cms.untracked.bool( True ),
    MinDphi = cms.double( 0.0 ),
    MaxDphi = cms.double( 1000.0 ),
    MinDeta = cms.double( 0.0 ),
    MaxDeta = cms.double( 1000.0 ),
    MinMinv = cms.double( 0.0 ),
    MaxMinv = cms.double( 14000.0 ),
    MinDelR = cms.double( 0.3 ),
    MaxDelR = cms.double( 1000.0 ),
    MinN = cms.int32( 1 )
)
process.hltOverlapFilterIsoMu12IsoPFTau10 = cms.HLTFilter( "HLT2MuonTau",
    inputTag1 = cms.InputTag( 'hltSingleMuIsoL3IsoFiltered12' ),
    inputTag2 = cms.InputTag( 'hltFilterIsoMu12IsoPFTau10LooseIsolation' ),
    saveTags = cms.untracked.bool( True ),
    MinDphi = cms.double( 0.0 ),
    MaxDphi = cms.double( 1000.0 ),
    MinDeta = cms.double( 0.0 ),
    MaxDeta = cms.double( 1000.0 ),
    MinMinv = cms.double( 0.0 ),
    MaxMinv = cms.double( 14000.0 ),
    MinDelR = cms.double( 0.3 ),
    MaxDelR = cms.double( 1000.0 ),
    MinN = cms.int32( 1 )
)
process.hltOverlapFilterMu15IsoPFTau20 = cms.HLTFilter( "HLT2MuonTau",
    inputTag1 = cms.InputTag( 'hltL3Muon15' ),
    inputTag2 = cms.InputTag( 'hltPFTau20TrackLooseIso' ),
    saveTags = cms.untracked.bool( True ),
    MinDphi = cms.double( 0.0 ),
    MaxDphi = cms.double( 1000.0 ),
    MinDeta = cms.double( 0.0 ),
    MaxDeta = cms.double( 1000.0 ),
    MinMinv = cms.double( 0.0 ),
    MaxMinv = cms.double( 14000.0 ),
    MinDelR = cms.double( 0.3 ),
    MaxDelR = cms.double( 1000.0 ),
    MinN = cms.int32( 1 )
)
process.hltPFJet10 = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltAntiKT5ConvPFJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 10.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltPFJet15 = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltAntiKT5ConvPFJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltPFJet20 = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltAntiKT5ConvPFJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 20.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltPFJetCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( 'hltPFJetPixelSeeds' ),
    TrajectoryBuilder = cms.string( "hltESPTrajectoryBuilderL3" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 )
)
process.hltPFJetCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( True ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    Fitter = cms.string( "hltESPFittingSmootherRK" ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
    src = cms.InputTag( 'hltPFJetCkfTrackCandidates' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "ctf" ),
    NavigationSchool = cms.string( "" )
)
process.hltPFJetPixelSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    ClusterCheckPSet = cms.PSet(
      PixelClusterCollectionLabel = cms.InputTag( 'hltSiPixelClusters' ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
      doClusterCheck = cms.bool( False ),
      ClusterCollectionLabel = cms.InputTag( 'hltSiStripClusters' ),
      MaxNumberOfPixelClusters = cms.uint32( 10000 )
    ),
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "TauRegionalPixelSeedGenerator" ),
      RegionPSet = cms.PSet(
        precise = cms.bool( True ),
        deltaPhiRegion = cms.double( 0.5 ),
        originHalfLength = cms.double( 0.3 ),
        originRadius = cms.double( 0.2 ),
        deltaEtaRegion = cms.double( 0.5 ),
        vertexSrc = cms.InputTag( 'hltPixelVertices' ),
        JetSrc = cms.InputTag( 'hltAntiKT5CaloJetsEt5' ),
        originZPos = cms.double( 0.0 ),
        ptMin = cms.double( 0.2 )
      )
    ),
    OrderedHitsFactoryPSet = cms.PSet(
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltESPPixelLayerPairs" )
    ),
    SeedComparitorPSet = cms.PSet(
      ComponentName = cms.string( "none" )
    ),
    SeedCreatorPSet = cms.PSet(
      ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
      propagator = cms.string( "PropagatorWithMaterial" )
    ),
    TTRHBuilder = cms.string( "WithTrackAngle" )
)
process.hltPFMHT150Filter = cms.HLTFilter( "HLTMhtHtFilter",
    inputJetTag = cms.InputTag( 'hltAntiKT5ConvPFJets' ),
    saveTag = cms.untracked.bool( True ),
    minMht = cms.double( 150.0 ),
    minNJet = cms.int32( 3 ),
    mode = cms.int32( 1 ),
    usePt = cms.bool( True ),
    minPT12 = cms.double( 0.0 ),
    minMeff = cms.double( 0.0 ),
    minHt = cms.double( 0.0 ),
    minMht2Ht = cms.double( 0.4 ),
    minPtJet = cms.vdouble(  5, 5  ),
    etaJet = cms.vdouble(  9999, 9999  )
)
process.hltPFTau10Track = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltConvPFTausTrackFinding' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 10.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltPFTau15 = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltConvPFTaus' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltPFTau15Track = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltConvPFTausTrackFinding' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltPFTau15TrackLooseIso = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltConvPFTausTrackFindingLooseIsolation' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 15.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltPFTau20 = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltConvPFTaus' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 20.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltPFTau20Track = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltConvPFTausTrackFinding' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 20.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltPFTau20TrackLooseIso = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltConvPFTausTrackFindingLooseIsolation' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 20.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltPFTau5Track = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltConvPFTausTightIsoTrackFinding' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 5.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltPFTau5Track5 = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltConvPFTausTightIsoTrackPt5' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 5.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltPFTauIsolationDiscriminator = cms.EDProducer( "PFRecoTauDiscriminationByIsolation",
    PFTauProducer = cms.InputTag( 'hltPFTaus' ),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string( "and" )
    ),
    maximumSumPtCut = cms.double( 6.0 ),
    maximumOccupancy = cms.uint32( 0 ),
    relativeSumPtCut = cms.double( 0.0 ),
    ApplyDiscriminationByECALIsolation = cms.bool( False ),
    PVProducer = cms.InputTag( 'hltPixelVertices' ),
    applyOccupancyCut = cms.bool( True ),
    applyRelativeSumPtCut = cms.bool( False ),
    applySumPtCut = cms.bool( False ),
    ApplyDiscriminationByTrackerIsolation = cms.bool( True ),
    qualityCuts = cms.PSet(
      isolationQualityCuts = cms.PSet(
        minTrackHits = cms.uint32( 3 ),
        minTrackPt = cms.double( 1.0 ),
        maxTrackChi2 = cms.double( 100.0 ),
        minTrackPixelHits = cms.uint32( 0 ),
        minGammaEt = cms.double( 1.5 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        maxDeltaZ = cms.double( 0.2 ),
        maxTransverseImpactParameter = cms.double( 0.05 )
      ),
      signalQualityCuts = cms.PSet(
        maxDeltaZ = cms.double( 0.5 ),
        minTrackPt = cms.double( 0.0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minGammaEt = cms.double( 0.5 ),
        minTrackPixelHits = cms.uint32( 0 ),
        minTrackHits = cms.uint32( 3 ),
        maxTransverseImpactParameter = cms.double( 0.2 )
      )
    )
)
process.hltPFTauJetTracksAssociator = cms.EDProducer( "JetTracksAssociatorAtVertex",
    jets = cms.InputTag( 'hltAntiKT5PFJets' ),
    tracks = cms.InputTag( 'hltPFJetCtfWithMaterialTracks' ),
    coneSize = cms.double( 0.5 )
)
process.hltPFTauLooseIsolationDiscriminator = cms.EDProducer( "PFRecoTauDiscriminationByIsolation",
    PFTauProducer = cms.InputTag( 'hltPFTaus' ),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string( "and" )
    ),
    maximumSumPtCut = cms.double( 6.0 ),
    maximumOccupancy = cms.uint32( 0 ),
    relativeSumPtCut = cms.double( 0.0 ),
    ApplyDiscriminationByECALIsolation = cms.bool( False ),
    PVProducer = cms.InputTag( 'hltPixelVertices' ),
    applyOccupancyCut = cms.bool( True ),
    applyRelativeSumPtCut = cms.bool( False ),
    applySumPtCut = cms.bool( False ),
    ApplyDiscriminationByTrackerIsolation = cms.bool( True ),
    qualityCuts = cms.PSet(
      isolationQualityCuts = cms.PSet(
        minTrackHits = cms.uint32( 3 ),
        minTrackPt = cms.double( 1.5 ),
        maxTrackChi2 = cms.double( 100.0 ),
        minTrackPixelHits = cms.uint32( 0 ),
        minGammaEt = cms.double( 1.5 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        maxDeltaZ = cms.double( 0.2 ),
        maxTransverseImpactParameter = cms.double( 0.05 )
      ),
      signalQualityCuts = cms.PSet(
        maxDeltaZ = cms.double( 0.5 ),
        minTrackPt = cms.double( 0.0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minGammaEt = cms.double( 0.5 ),
        minTrackPixelHits = cms.uint32( 0 ),
        minTrackHits = cms.uint32( 3 ),
        maxTransverseImpactParameter = cms.double( 0.2 )
      )
    )
)
process.hltPFTauTagInfo = cms.EDProducer( "PFRecoTauTagInfoProducer",
    PFCandidateProducer = cms.InputTag( 'hltParticleFlow' ),
    PFJetTracksAssociatorProducer = cms.InputTag( 'hltPFTauJetTracksAssociator' ),
    PVProducer = cms.InputTag( 'hltPixelVertices' ),
    smearedPVsigmaX = cms.double( 0.0015 ),
    smearedPVsigmaY = cms.double( 0.0015 ),
    smearedPVsigmaZ = cms.double( 0.005 ),
    ChargedHadrCand_AssociationCone = cms.double( 0.8 ),
    ChargedHadrCand_tkminPt = cms.double( 0.0 ),
    ChargedHadrCand_tkminPixelHitsn = cms.int32( 0 ),
    ChargedHadrCand_tkminTrackerHitsn = cms.int32( 0 ),
    ChargedHadrCand_tkmaxipt = cms.double( 0.2 ),
    ChargedHadrCand_tkmaxChi2 = cms.double( 100.0 ),
    NeutrHadrCand_HcalclusMinEt = cms.double( 0.5 ),
    GammaCand_EcalclusMinEt = cms.double( 0.5 ),
    tkminPt = cms.double( 0.0 ),
    tkminPixelHitsn = cms.int32( 2 ),
    tkminTrackerHitsn = cms.int32( 5 ),
    tkmaxipt = cms.double( 0.2 ),
    tkmaxChi2 = cms.double( 100.0 ),
    UsePVconstraint = cms.bool( True ),
    ChargedHadrCand_tkPVmaxDZ = cms.double( 0.4 ),
    tkPVmaxDZ = cms.double( 0.4 )
)
process.hltPFTauTightIso35 = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltConvPFTausTightIso' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 35.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltPFTauTightIso35Track = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltConvPFTausTightIsoTrackFinding' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 35.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltPFTauTightIsoIsolationDiscriminator = cms.EDProducer( "PFRecoTauDiscriminationByIsolation",
    PFTauProducer = cms.InputTag( 'hltPFTausTightIso' ),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string( "and" )
    ),
    maximumSumPtCut = cms.double( 6.0 ),
    maximumOccupancy = cms.uint32( 0 ),
    relativeSumPtCut = cms.double( 0.0 ),
    ApplyDiscriminationByECALIsolation = cms.bool( True ),
    PVProducer = cms.InputTag( 'hltPixelVertices' ),
    applyOccupancyCut = cms.bool( True ),
    applyRelativeSumPtCut = cms.bool( False ),
    applySumPtCut = cms.bool( False ),
    ApplyDiscriminationByTrackerIsolation = cms.bool( True ),
    qualityCuts = cms.PSet(
      isolationQualityCuts = cms.PSet(
        minTrackHits = cms.uint32( 3 ),
        minTrackPt = cms.double( 1.0 ),
        maxTrackChi2 = cms.double( 100.0 ),
        minTrackPixelHits = cms.uint32( 0 ),
        minGammaEt = cms.double( 1.5 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        maxDeltaZ = cms.double( 0.2 ),
        maxTransverseImpactParameter = cms.double( 0.05 )
      ),
      signalQualityCuts = cms.PSet(
        maxDeltaZ = cms.double( 0.5 ),
        minTrackPt = cms.double( 0.0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minGammaEt = cms.double( 0.5 ),
        minTrackPixelHits = cms.uint32( 0 ),
        minTrackHits = cms.uint32( 3 ),
        maxTransverseImpactParameter = cms.double( 0.2 )
      )
    )
)
process.hltPFTauTightIsoTrackFindingDiscriminator = cms.EDProducer( "PFRecoTauDiscriminationByLeadingObjectPtCut",
    PFTauProducer = cms.InputTag( 'hltPFTausTightIso' ),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string( "and" )
    ),
    UseOnlyChargedHadrons = cms.bool( True ),
    MinPtLeadingObject = cms.double( 0.0 )
)
process.hltPFTauTightIsoTrackPt20Discriminator = cms.EDProducer( "PFRecoTauDiscriminationByLeadingObjectPtCut",
    PFTauProducer = cms.InputTag( 'hltPFTausTightIso' ),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string( "and" )
    ),
    UseOnlyChargedHadrons = cms.bool( True ),
    MinPtLeadingObject = cms.double( 20.0 )
)
process.hltPFTauTightIsoTrackPt5Discriminator = cms.EDProducer( "PFRecoTauDiscriminationByLeadingObjectPtCut",
    PFTauProducer = cms.InputTag( 'hltPFTausTightIso' ),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string( "and" )
    ),
    UseOnlyChargedHadrons = cms.bool( True ),
    MinPtLeadingObject = cms.double( 5.0 )
)
process.hltPFTauTrackFindingDiscriminator = cms.EDProducer( "PFRecoTauDiscriminationByLeadingObjectPtCut",
    PFTauProducer = cms.InputTag( 'hltPFTaus' ),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string( "and" )
    ),
    UseOnlyChargedHadrons = cms.bool( True ),
    MinPtLeadingObject = cms.double( 0.0 )
)
process.hltPFTauTrackPt5Discriminator = cms.EDProducer( "PFRecoTauDiscriminationByLeadingObjectPtCut",
    PFTauProducer = cms.InputTag( 'hltPFTaus' ),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string( "and" )
    ),
    UseOnlyChargedHadrons = cms.bool( True ),
    MinPtLeadingObject = cms.double( 5.0 )
)
process.hltPFTaus = cms.EDProducer( "PFRecoTauProducer",
    PFTauTagInfoProducer = cms.InputTag( 'hltPFTauTagInfo' ),
    ElectronPreIDProducer = cms.InputTag( 'elecpreid' ),
    PVProducer = cms.InputTag( 'hltPixelVertices' ),
    Algorithm = cms.string( "ConeBased" ),
    smearedPVsigmaX = cms.double( 0.0015 ),
    smearedPVsigmaY = cms.double( 0.0015 ),
    smearedPVsigmaZ = cms.double( 0.005 ),
    JetPtMin = cms.double( 0.0 ),
    LeadPFCand_minPt = cms.double( 0.0 ),
    UseChargedHadrCandLeadChargedHadrCand_tksDZconstraint = cms.bool( True ),
    ChargedHadrCandLeadChargedHadrCand_tksmaxDZ = cms.double( 0.4 ),
    LeadTrack_minPt = cms.double( 0.0 ),
    UseTrackLeadTrackDZconstraint = cms.bool( False ),
    TrackLeadTrack_maxDZ = cms.double( 0.4 ),
    MatchingConeMetric = cms.string( "DR" ),
    MatchingConeSizeFormula = cms.string( "0.2" ),
    MatchingConeSize_min = cms.double( 0.0 ),
    MatchingConeSize_max = cms.double( 0.6 ),
    TrackerSignalConeMetric = cms.string( "DR" ),
    TrackerSignalConeSizeFormula = cms.string( "0.2" ),
    TrackerSignalConeSize_min = cms.double( 0.0 ),
    TrackerSignalConeSize_max = cms.double( 0.2 ),
    TrackerIsolConeMetric = cms.string( "DR" ),
    TrackerIsolConeSizeFormula = cms.string( "0.5" ),
    TrackerIsolConeSize_min = cms.double( 0.0 ),
    TrackerIsolConeSize_max = cms.double( 0.5 ),
    ECALSignalConeMetric = cms.string( "DR" ),
    ECALSignalConeSizeFormula = cms.string( "0.2" ),
    ECALSignalConeSize_min = cms.double( 0.0 ),
    ECALSignalConeSize_max = cms.double( 0.6 ),
    ECALIsolConeMetric = cms.string( "DR" ),
    ECALIsolConeSizeFormula = cms.string( "0.5" ),
    ECALIsolConeSize_min = cms.double( 0.0 ),
    ECALIsolConeSize_max = cms.double( 0.5 ),
    HCALSignalConeMetric = cms.string( "DR" ),
    HCALSignalConeSizeFormula = cms.string( "0.2" ),
    HCALSignalConeSize_min = cms.double( 0.0 ),
    HCALSignalConeSize_max = cms.double( 0.5 ),
    HCALIsolConeMetric = cms.string( "DR" ),
    HCALIsolConeSizeFormula = cms.string( "0.5" ),
    HCALIsolConeSize_min = cms.double( 0.0 ),
    HCALIsolConeSize_max = cms.double( 0.5 ),
    Rphi = cms.double( 0.2 ),
    MaxEtInEllipse = cms.double( 2.0 ),
    AddEllipseGammas = cms.bool( False ),
    AreaMetric_recoElements_maxabsEta = cms.double( 2.5 ),
    ChargedHadrCand_IsolAnnulus_minNhits = cms.uint32( 0 ),
    Track_IsolAnnulus_minNhits = cms.uint32( 0 ),
    ElecPreIDLeadTkMatch_maxDR = cms.double( 0.015 ),
    EcalStripSumE_minClusEnergy = cms.double( 0.0 ),
    EcalStripSumE_deltaEta = cms.double( 0.0 ),
    EcalStripSumE_deltaPhiOverQ_minValue = cms.double( 0.0 ),
    EcalStripSumE_deltaPhiOverQ_maxValue = cms.double( 0.0 ),
    maximumForElectrionPreIDOutput = cms.double( 0.0 ),
    DataType = cms.string( "AOD" ),
    emMergingAlgorithm = cms.string( "None" ),
    candOverlapCriterion = cms.string( "None" ),
    doOneProng = cms.bool( True ),
    doOneProngStrip = cms.bool( True ),
    doOneProngTwoStrips = cms.bool( True ),
    doThreeProng = cms.bool( True ),
    tauPtThreshold = cms.double( 0.0 ),
    leadPionThreshold = cms.double( 1.0 ),
    stripPtThreshold = cms.double( 0.5 ),
    chargeHadrIsolationConeSize = cms.double( 0.5 ),
    gammaIsolationConeSize = cms.double( 0.5 ),
    neutrHadrIsolationConeSize = cms.double( 0.5 ),
    useIsolationAnnulus = cms.bool( False ),
    matchingCone = cms.double( 0.2 ),
    coneMetric = cms.string( "DR" ),
    coneSizeFormula = cms.string( "2.8/ET" ),
    minimumSignalCone = cms.double( 0.0 ),
    maximumSignalCone = cms.double( 1.8 ),
    oneProngStripMassWindow = cms.vdouble(  0, 0  ),
    oneProngTwoStripsMassWindow = cms.vdouble(  0, 0  ),
    oneProngTwoStripsPi0MassWindow = cms.vdouble(  0, 0  ),
    threeProngMassWindow = cms.vdouble(  0, 0  )
)
process.hltPFTausTightIso = cms.EDProducer( "PFRecoTauProducer",
    PFTauTagInfoProducer = cms.InputTag( 'hltPFTauTagInfo' ),
    ElectronPreIDProducer = cms.InputTag( 'elecpreid' ),
    PVProducer = cms.InputTag( 'hltPixelVertices' ),
    Algorithm = cms.string( "ConeBased" ),
    smearedPVsigmaX = cms.double( 0.0015 ),
    smearedPVsigmaY = cms.double( 0.0015 ),
    smearedPVsigmaZ = cms.double( 0.005 ),
    JetPtMin = cms.double( 0.0 ),
    LeadPFCand_minPt = cms.double( 0.0 ),
    UseChargedHadrCandLeadChargedHadrCand_tksDZconstraint = cms.bool( True ),
    ChargedHadrCandLeadChargedHadrCand_tksmaxDZ = cms.double( 0.4 ),
    LeadTrack_minPt = cms.double( 0.0 ),
    UseTrackLeadTrackDZconstraint = cms.bool( True ),
    TrackLeadTrack_maxDZ = cms.double( 0.4 ),
    MatchingConeMetric = cms.string( "DR" ),
    MatchingConeSizeFormula = cms.string( "0.2" ),
    MatchingConeSize_min = cms.double( 0.0 ),
    MatchingConeSize_max = cms.double( 0.6 ),
    TrackerSignalConeMetric = cms.string( "DR" ),
    TrackerSignalConeSizeFormula = cms.string( "0.15" ),
    TrackerSignalConeSize_min = cms.double( 0.0 ),
    TrackerSignalConeSize_max = cms.double( 0.2 ),
    TrackerIsolConeMetric = cms.string( "DR" ),
    TrackerIsolConeSizeFormula = cms.string( "0.5" ),
    TrackerIsolConeSize_min = cms.double( 0.0 ),
    TrackerIsolConeSize_max = cms.double( 0.5 ),
    ECALSignalConeMetric = cms.string( "DR" ),
    ECALSignalConeSizeFormula = cms.string( "0.15" ),
    ECALSignalConeSize_min = cms.double( 0.0 ),
    ECALSignalConeSize_max = cms.double( 0.6 ),
    ECALIsolConeMetric = cms.string( "DR" ),
    ECALIsolConeSizeFormula = cms.string( "0.5" ),
    ECALIsolConeSize_min = cms.double( 0.0 ),
    ECALIsolConeSize_max = cms.double( 0.5 ),
    HCALSignalConeMetric = cms.string( "DR" ),
    HCALSignalConeSizeFormula = cms.string( "0.2" ),
    HCALSignalConeSize_min = cms.double( 0.0 ),
    HCALSignalConeSize_max = cms.double( 0.5 ),
    HCALIsolConeMetric = cms.string( "DR" ),
    HCALIsolConeSizeFormula = cms.string( "0.5" ),
    HCALIsolConeSize_min = cms.double( 0.0 ),
    HCALIsolConeSize_max = cms.double( 0.5 ),
    Rphi = cms.double( 0.2 ),
    MaxEtInEllipse = cms.double( 2.0 ),
    AddEllipseGammas = cms.bool( False ),
    AreaMetric_recoElements_maxabsEta = cms.double( 2.5 ),
    ChargedHadrCand_IsolAnnulus_minNhits = cms.uint32( 0 ),
    Track_IsolAnnulus_minNhits = cms.uint32( 0 ),
    ElecPreIDLeadTkMatch_maxDR = cms.double( 0.015 ),
    EcalStripSumE_minClusEnergy = cms.double( 0.0 ),
    EcalStripSumE_deltaEta = cms.double( 0.0 ),
    EcalStripSumE_deltaPhiOverQ_minValue = cms.double( 0.0 ),
    EcalStripSumE_deltaPhiOverQ_maxValue = cms.double( 0.0 ),
    maximumForElectrionPreIDOutput = cms.double( 0.0 ),
    DataType = cms.string( "AOD" ),
    emMergingAlgorithm = cms.string( "None" ),
    candOverlapCriterion = cms.string( "None" ),
    doOneProng = cms.bool( True ),
    doOneProngStrip = cms.bool( True ),
    doOneProngTwoStrips = cms.bool( True ),
    doThreeProng = cms.bool( True ),
    tauPtThreshold = cms.double( 0.0 ),
    leadPionThreshold = cms.double( 1.0 ),
    stripPtThreshold = cms.double( 0.5 ),
    chargeHadrIsolationConeSize = cms.double( 0.5 ),
    gammaIsolationConeSize = cms.double( 0.5 ),
    neutrHadrIsolationConeSize = cms.double( 0.5 ),
    useIsolationAnnulus = cms.bool( False ),
    matchingCone = cms.double( 0.2 ),
    coneMetric = cms.string( "DR" ),
    coneSizeFormula = cms.string( "2.8/ET" ),
    minimumSignalCone = cms.double( 0.0 ),
    maximumSignalCone = cms.double( 1.8 ),
    oneProngStripMassWindow = cms.vdouble(  0, 0  ),
    oneProngTwoStripsMassWindow = cms.vdouble(  0, 0  ),
    oneProngTwoStripsPi0MassWindow = cms.vdouble(  0, 0  ),
    threeProngMassWindow = cms.vdouble(  0, 0  )
)
process.hltPFlowTrackSelectionHighPurity = cms.EDProducer( "AnalyticalTrackSelector",
    src = cms.InputTag( 'hltPFJetCtfWithMaterialTracks' ),
    beamspot = cms.InputTag( 'hltOnlineBeamSpot' ),
    vertices = cms.InputTag( 'hltPixelVertices' ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( True ),
    keepAllTracks = cms.bool( False ),
    vtxNumber = cms.int32( -1 ),
    vertexCut = cms.string( "ndof>=2&!isFake" ),
    chi2n_par = cms.double( 0.6 ),
    applyAdaptedPVCuts = cms.bool( False ),
    max_d0 = cms.double( 100.0 ),
    max_z0 = cms.double( 100.0 ),
    nSigmaZ = cms.double( 3.0 ),
    minNumberLayers = cms.uint32( 3 ),
    minNumber3DLayers = cms.uint32( 3 ),
    maxNumberLostLayers = cms.uint32( 2 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    max_d0NoPV = cms.double( 100.0 ),
    max_z0NoPV = cms.double( 100.0 ),
    res_par = cms.vdouble(  0.003, 0.001  ),
    d0_par1 = cms.vdouble(  0.3, 4  ),
    dz_par1 = cms.vdouble(  0.35, 4  ),
    d0_par2 = cms.vdouble(  4, 4  ),
    dz_par2 = cms.vdouble(  4, 4  )
)
process.hltParticleFlow = cms.EDProducer( "PFProducer",
    pf_newCalib = cms.uint32( 2 ),
    pfcluster_lowEP0 = cms.double( 0.3249189 ),
    pfcluster_lowEP1 = cms.double( 0.790799 ),
    pfcluster_globalP0 = cms.double( -2.315 ),
    pfcluster_globalP1 = cms.double( 1.01 ),
    pfcluster_allowNegative = cms.uint32( 0 ),
    pfcluster_doCorrection = cms.uint32( 1 ),
    pfcluster_barrelEndcapEtaDiv = cms.double( 1.4 ),
    pfcluster_doEtaCorrection = cms.uint32( 1 ),
    calibHF_use = cms.bool( False ),
    blocks = cms.InputTag( 'hltParticleFlowBlock' ),
    muons = cms.InputTag( "" ),
    postMuonCleaning = cms.bool( False ),
    usePFElectrons = cms.bool( False ),
    useEGammaElectrons = cms.bool( False ),
    egammaElectrons = cms.InputTag( "" ),
    pf_electron_output_col = cms.string( "electrons" ),
    usePFSCEleCalib = cms.bool( True ),
    useEGammaSupercluster = cms.bool( False ),
    sumEtEcalIsoForEgammaSC_barrel = cms.double( 1.0 ),
    sumEtEcalIsoForEgammaSC_endcap = cms.double( 2.0 ),
    coneEcalIsoForEgammaSC = cms.double( 0.3 ),
    sumPtTrackIsoForEgammaSC_barrel = cms.double( 4.0 ),
    sumPtTrackIsoForEgammaSC_endcap = cms.double( 4.0 ),
    coneTrackIsoForEgammaSC = cms.double( 0.3 ),
    nTrackIsoForEgammaSC = cms.uint32( 2 ),
    pf_nsigma_ECAL = cms.double( 0.0 ),
    pf_nsigma_HCAL = cms.double( 1.0 ),
    pf_calib_ECAL_slope = cms.double( 1.0 ),
    pf_calib_ECAL_offset = cms.double( 0.0 ),
    pf_calib_ECAL_HCAL_eslope = cms.double( 1.05 ),
    pf_calib_ECAL_HCAL_hslope = cms.double( 1.06 ),
    pf_calib_ECAL_HCAL_offset = cms.double( 6.11 ),
    pf_calib_HCAL_slope = cms.double( 2.17 ),
    pf_calib_HCAL_offset = cms.double( 1.73 ),
    pf_calib_HCAL_damping = cms.double( 2.49 ),
    pf_electron_mvaCut = cms.double( -0.1 ),
    pf_electronID_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_PfElectrons23Jan_IntToFloat.txt" ),
    pf_electronID_crackCorrection = cms.bool( False ),
    rejectTracks_Bad = cms.bool( False ),
    rejectTracks_Step45 = cms.bool( False ),
    usePFNuclearInteractions = cms.bool( False ),
    usePFConversions = cms.bool( False ),
    usePFDecays = cms.bool( False ),
    dptRel_DispVtx = cms.double( 10.0 ),
    algoType = cms.uint32( 0 ),
    nsigma_TRACK = cms.double( 1.0 ),
    pt_Error = cms.double( 1.0 ),
    usePFMuonMomAssign = cms.bool( False ),
    postHFCleaning = cms.bool( False ),
    minHFCleaningPt = cms.double( 5.0 ),
    minSignificance = cms.double( 2.5 ),
    maxSignificance = cms.double( 2.5 ),
    minSignificanceReduction = cms.double( 1.4 ),
    maxDeltaPhiPt = cms.double( 7.0 ),
    minDeltaMet = cms.double( 0.4 ),
    vertexCollection = cms.InputTag( 'hltPixelVertices' ),
    useVerticesForNeutral = cms.bool( True ),
    verbose = cms.untracked.bool( False ),
    debug = cms.untracked.bool( False ),
    pfcluster_etaCorrection = cms.vdouble(  1.01, -0.0102, 0.0517, 0.563, -0.425, 0.11  ),
    calibHF_eta_step = cms.vdouble(  0, 2.9, 3, 3.2, 4.2, 4.4, 4.6, 4.8, 5.2, 5.2  ),
    calibHF_a_EMonly = cms.vdouble(  0.96945, 0.96701, 0.76309, 0.82268, 0.87583  ),
    calibHF_b_HADonly = cms.vdouble(  1.27541, 0.85361, 0.86333, 0.89091, 0.94348  ),
    calibHF_a_EMHAD = cms.vdouble(  1.42215, 1.00496, 0.68961, 0.81656, 0.98504  ),
    calibHF_b_EMHAD = cms.vdouble(  1.27541, 0.85361, 0.86333, 0.89091, 0.94348  ),
    calibPFSCEle_barrel = cms.vdouble(  1.0326, -13.71, 339.72, 0.4862, 0.00182, 0.36445, 1.411, 1.0206, 0.0059162, -5.14434E-5, 1.42516E-7  ),
    calibPFSCEle_endcap = cms.vdouble(  0.9995, -12.313, 2.8784, -0.0001057, 10.282, 3.059, 0.0013502, -2.2185, 3.4206  ),
    muon_HCAL = cms.vdouble(  3, 3  ),
    muon_ECAL = cms.vdouble(  0.5, 0.5  ),
    factors_45 = cms.vdouble(  10, 100  ),
    cleanedHF = cms.VInputTag( 'hltParticleFlowRecHitHCAL:Cleaned, hltParticleFlowClusterHFHAD:Cleaned, hltParticleFlowClusterHFEM:Cleaned' ),
    iCfgCandConnector = cms.PSet(
      bCalibSecondary = cms.bool( False ),
      bCalibPrimary = cms.bool( False ),
      bCorrect = cms.bool( False ),
      nuclCalibFactors = cms.vdouble(  0.88, 0.28, 0.04  )
    ),
    pf_clusterRecovery = cms.bool( False ),
    ecalHcalEcalEndcap = cms.vdouble(  0.46, 3, 1.1, 0.4, -0.02, 1.4  ),
    ecalHcalEcalBarrel = cms.vdouble(  0.67, 3, 1.15, 0.9, -0.06, 1.4  ),
    ecalHcalHcalBarrel = cms.vdouble(  0.46, 3, 1.15, 0.3, -0.02, 1.4  ),
    ecalHcalHcalEndcap = cms.vdouble(  0.46, 3, 1.1, 0.3, -0.02, 1.4  ),
    useCalibrationsFromDB = cms.bool( True ),
    usePFPhotons = cms.bool( False ),
    calibPFSCEle_Fbrem_barrel = cms.vdouble(  0.6, 6, -0.0255975, 0.0576727, 0.975442, -0.000546394, 1.26147, 25, -0.02025, 0.04537, 0.9728, -0.0008962, 1.172  ),
    calibPFSCEle_Fbrem_endcap = cms.vdouble(  0.9, 6.5, -0.0692932, 0.101776, 0.995338, -0.00236548, 0.874998, 1.653, -0.0750184, 0.147, 0.923165, 0.000474665, 1.10782  )
)
process.hltParticleFlowBlock = cms.EDProducer( "PFBlockProducer",
    RecTracks = cms.InputTag( 'hltLightPFTracks' ),
    GsfRecTracks = cms.InputTag( 'pfTrackElec' ),
    ConvBremGsfRecTracks = cms.InputTag( 'pfTrackElec', 'Secondary' ),
    RecMuons = cms.InputTag( 'muons' ),
    PFNuclear = cms.InputTag( 'pfDisplacedTrackerVertex' ),
    PFConversions = cms.InputTag( 'pfConversions' ),
    PFV0 = cms.InputTag( 'pfV0' ),
    PFClustersECAL = cms.InputTag( 'hltParticleFlowClusterECAL' ),
    PFClustersHCAL = cms.InputTag( 'hltParticleFlowClusterHCAL' ),
    PFClustersHFEM = cms.InputTag( 'hltParticleFlowClusterHFEM' ),
    PFClustersHFHAD = cms.InputTag( 'hltParticleFlowClusterHFHAD' ),
    PFClustersPS = cms.InputTag( 'hltParticleFlowClusterPS' ),
    verbose = cms.untracked.bool( False ),
    debug = cms.untracked.bool( False ),
    usePFatHLT = cms.bool( True ),
    useNuclear = cms.bool( False ),
    useConversions = cms.bool( False ),
    useConvBremGsfTracks = cms.bool( False ),
    useConvBremPFRecTracks = cms.bool( False ),
    useV0 = cms.bool( False ),
    useIterTracking = cms.bool( False ),
    nuclearInteractionsPurity = cms.uint32( 1 ),
    pf_DPtoverPt_Cut = cms.vdouble(  -1, -1, -1, -1  ),
    pf_NHit_Cut = cms.vuint32( 0, 0, 0, 0 ),
    useRecMuons = cms.bool( False ),
    useGsfRecTracks = cms.bool( False ),
    useEGPhotons = cms.bool( False )
)
process.hltParticleFlowClusterECAL = cms.EDProducer( "PFClusterProducer",
    verbose = cms.untracked.bool( False ),
    thresh_Barrel = cms.double( 0.8 ),
    thresh_Seed_Barrel = cms.double( 0.8 ),
    thresh_Pt_Barrel = cms.double( 0.0 ),
    thresh_Pt_Seed_Barrel = cms.double( 0.0 ),
    thresh_Clean_Barrel = cms.double( 100000.0 ),
    thresh_Endcap = cms.double( 0.8 ),
    thresh_Seed_Endcap = cms.double( 1.1 ),
    thresh_Pt_Endcap = cms.double( 0.0 ),
    thresh_Pt_Seed_Endcap = cms.double( 0.0 ),
    thresh_Clean_Endcap = cms.double( 100000.0 ),
    thresh_DoubleSpike_Barrel = cms.double( 1000000000.0 ),
    minS6S2_DoubleSpike_Barrel = cms.double( -1.0 ),
    thresh_DoubleSpike_Endcap = cms.double( 1000000000.0 ),
    minS6S2_DoubleSpike_Endcap = cms.double( -1.0 ),
    nNeighbours = cms.int32( 4 ),
    posCalcNCrystal = cms.int32( 5 ),
    showerSigma = cms.double( 10.0 ),
    useCornerCells = cms.bool( True ),
    cleanRBXandHPDs = cms.bool( False ),
    depthCor_Mode = cms.int32( 1 ),
    depthCor_A = cms.double( 0.89 ),
    depthCor_B = cms.double( 7.4 ),
    depthCor_A_preshower = cms.double( 0.89 ),
    depthCor_B_preshower = cms.double( 4.0 ),
    PFRecHits = cms.InputTag( 'hltParticleFlowRecHitECAL' ),
    minS4S1_Clean_Barrel = cms.vdouble(  0.04, -0.024  ),
    minS4S1_Clean_Endcap = cms.vdouble(  0.04, -0.025  )
)
process.hltParticleFlowClusterHCAL = cms.EDProducer( "PFClusterProducer",
    verbose = cms.untracked.bool( False ),
    thresh_Barrel = cms.double( 0.8 ),
    thresh_Seed_Barrel = cms.double( 0.8 ),
    thresh_Pt_Barrel = cms.double( 0.0 ),
    thresh_Pt_Seed_Barrel = cms.double( 0.0 ),
    thresh_Clean_Barrel = cms.double( 10000000.0 ),
    thresh_Endcap = cms.double( 0.8 ),
    thresh_Seed_Endcap = cms.double( 1.1 ),
    thresh_Pt_Endcap = cms.double( 0.0 ),
    thresh_Pt_Seed_Endcap = cms.double( 0.0 ),
    thresh_Clean_Endcap = cms.double( 1000000.0 ),
    thresh_DoubleSpike_Barrel = cms.double( 1000000000.0 ),
    minS6S2_DoubleSpike_Barrel = cms.double( -1.0 ),
    thresh_DoubleSpike_Endcap = cms.double( 1000000000.0 ),
    minS6S2_DoubleSpike_Endcap = cms.double( -1.0 ),
    nNeighbours = cms.int32( 4 ),
    posCalcNCrystal = cms.int32( 5 ),
    showerSigma = cms.double( 10.0 ),
    useCornerCells = cms.bool( True ),
    cleanRBXandHPDs = cms.bool( True ),
    depthCor_Mode = cms.int32( 2 ),
    depthCor_A = cms.double( 0.89 ),
    depthCor_B = cms.double( 7.4 ),
    depthCor_A_preshower = cms.double( 0.89 ),
    depthCor_B_preshower = cms.double( 4.0 ),
    PFRecHits = cms.InputTag( 'hltParticleFlowRecHitHCAL' ),
    minS4S1_Clean_Barrel = cms.vdouble(  0.032, -0.045  ),
    minS4S1_Clean_Endcap = cms.vdouble(  0.032, -0.045  )
)
process.hltParticleFlowClusterHFEM = cms.EDProducer( "PFClusterProducer",
    verbose = cms.untracked.bool( False ),
    thresh_Barrel = cms.double( 0.8 ),
    thresh_Seed_Barrel = cms.double( 1.4 ),
    thresh_Pt_Barrel = cms.double( 0.0 ),
    thresh_Pt_Seed_Barrel = cms.double( 0.0 ),
    thresh_Clean_Barrel = cms.double( 80.0 ),
    thresh_Endcap = cms.double( 0.8 ),
    thresh_Seed_Endcap = cms.double( 1.4 ),
    thresh_Pt_Endcap = cms.double( 0.0 ),
    thresh_Pt_Seed_Endcap = cms.double( 0.0 ),
    thresh_Clean_Endcap = cms.double( 80.0 ),
    thresh_DoubleSpike_Barrel = cms.double( 1000000000.0 ),
    minS6S2_DoubleSpike_Barrel = cms.double( -1.0 ),
    thresh_DoubleSpike_Endcap = cms.double( 1000000000.0 ),
    minS6S2_DoubleSpike_Endcap = cms.double( -1.0 ),
    nNeighbours = cms.int32( 0 ),
    posCalcNCrystal = cms.int32( 5 ),
    showerSigma = cms.double( 10.0 ),
    useCornerCells = cms.bool( False ),
    cleanRBXandHPDs = cms.bool( False ),
    depthCor_Mode = cms.int32( 1 ),
    depthCor_A = cms.double( 0.89 ),
    depthCor_B = cms.double( 7.4 ),
    depthCor_A_preshower = cms.double( 0.89 ),
    depthCor_B_preshower = cms.double( 4.0 ),
    PFRecHits = cms.InputTag( 'hltParticleFlowRecHitHCAL', 'HFEM' ),
    minS4S1_Clean_Barrel = cms.vdouble(  0.11, -0.19  ),
    minS4S1_Clean_Endcap = cms.vdouble(  0.11, -0.19  )
)
process.hltParticleFlowClusterHFHAD = cms.EDProducer( "PFClusterProducer",
    verbose = cms.untracked.bool( False ),
    thresh_Barrel = cms.double( 0.8 ),
    thresh_Seed_Barrel = cms.double( 1.4 ),
    thresh_Pt_Barrel = cms.double( 0.0 ),
    thresh_Pt_Seed_Barrel = cms.double( 0.0 ),
    thresh_Clean_Barrel = cms.double( 120.0 ),
    thresh_Endcap = cms.double( 0.8 ),
    thresh_Seed_Endcap = cms.double( 1.4 ),
    thresh_Pt_Endcap = cms.double( 0.0 ),
    thresh_Pt_Seed_Endcap = cms.double( 0.0 ),
    thresh_Clean_Endcap = cms.double( 120.0 ),
    thresh_DoubleSpike_Barrel = cms.double( 1000000000.0 ),
    minS6S2_DoubleSpike_Barrel = cms.double( -1.0 ),
    thresh_DoubleSpike_Endcap = cms.double( 1000000000.0 ),
    minS6S2_DoubleSpike_Endcap = cms.double( -1.0 ),
    nNeighbours = cms.int32( 0 ),
    posCalcNCrystal = cms.int32( 5 ),
    showerSigma = cms.double( 10.0 ),
    useCornerCells = cms.bool( False ),
    cleanRBXandHPDs = cms.bool( False ),
    depthCor_Mode = cms.int32( 2 ),
    depthCor_A = cms.double( 0.89 ),
    depthCor_B = cms.double( 7.4 ),
    depthCor_A_preshower = cms.double( 0.89 ),
    depthCor_B_preshower = cms.double( 4.0 ),
    PFRecHits = cms.InputTag( 'hltParticleFlowRecHitHCAL', 'HFHAD' ),
    minS4S1_Clean_Barrel = cms.vdouble(  0.045, -0.08  ),
    minS4S1_Clean_Endcap = cms.vdouble(  0.045, -0.08  )
)
process.hltParticleFlowClusterPS = cms.EDProducer( "PFClusterProducer",
    verbose = cms.untracked.bool( False ),
    thresh_Barrel = cms.double( 6e-05 ),
    thresh_Seed_Barrel = cms.double( 0.00012 ),
    thresh_Pt_Barrel = cms.double( 0.0 ),
    thresh_Pt_Seed_Barrel = cms.double( 0.0 ),
    thresh_Clean_Barrel = cms.double( 100000.0 ),
    thresh_Endcap = cms.double( 6e-05 ),
    thresh_Seed_Endcap = cms.double( 0.00012 ),
    thresh_Pt_Endcap = cms.double( 0.0 ),
    thresh_Pt_Seed_Endcap = cms.double( 0.0 ),
    thresh_Clean_Endcap = cms.double( 100000.0 ),
    thresh_DoubleSpike_Barrel = cms.double( 1000000000.0 ),
    minS6S2_DoubleSpike_Barrel = cms.double( -1.0 ),
    thresh_DoubleSpike_Endcap = cms.double( 1000000000.0 ),
    minS6S2_DoubleSpike_Endcap = cms.double( -1.0 ),
    nNeighbours = cms.int32( 4 ),
    posCalcNCrystal = cms.int32( -1 ),
    showerSigma = cms.double( 0.2 ),
    useCornerCells = cms.bool( False ),
    cleanRBXandHPDs = cms.bool( False ),
    depthCor_Mode = cms.int32( 1 ),
    depthCor_A = cms.double( 0.89 ),
    depthCor_B = cms.double( 7.4 ),
    depthCor_A_preshower = cms.double( 0.89 ),
    depthCor_B_preshower = cms.double( 4.0 ),
    PFRecHits = cms.InputTag( 'hltParticleFlowRecHitPS' ),
    minS4S1_Clean_Barrel = cms.vdouble(  0, 0  ),
    minS4S1_Clean_Endcap = cms.vdouble(  0, 0  )
)
process.hltParticleFlowRecHitECAL = cms.EDProducer( "PFRecHitProducerECAL",
    ecalRecHitsEB = cms.InputTag( 'hltEcalRecHitAll', 'EcalRecHitsEB' ),
    ecalRecHitsEE = cms.InputTag( 'hltEcalRecHitAll', 'EcalRecHitsEE' ),
    crossBarrelEndcapBorder = cms.bool( False ),
    timing_Cleaning = cms.bool( False ),
    thresh_Cleaning = cms.double( 2.0 ),
    verbose = cms.untracked.bool( False ),
    thresh_Barrel = cms.double( 0.08 ),
    thresh_Endcap = cms.double( 0.3 ),
    topological_Cleaning = cms.bool( True )
)
process.hltParticleFlowRecHitHCAL = cms.EDProducer( "PFRecHitProducerHCAL",
    hcalRecHitsHBHE = cms.InputTag( 'hltHbhereco' ),
    hcalRecHitsHF = cms.InputTag( 'hltHfreco' ),
    caloTowers = cms.InputTag( 'hltTowerMakerForAll' ),
    thresh_HF = cms.double( 0.4 ),
    navigation_HF = cms.bool( True ),
    weight_HFem = cms.double( 1.0 ),
    weight_HFhad = cms.double( 1.0 ),
    HCAL_Calib = cms.bool( True ),
    HF_Calib = cms.bool( False ),
    Max_Calib = cms.double( 5.0 ),
    ShortFibre_Cut = cms.double( 60.0 ),
    LongFibre_Fraction = cms.double( 0.05 ),
    LongFibre_Cut = cms.double( 120.0 ),
    ShortFibre_Fraction = cms.double( 0.01 ),
    ApplyLongShortDPG = cms.bool( False ),
    LongShortFibre_Cut = cms.double( 1000000000.0 ),
    MinShortTiming_Cut = cms.double( -5.0 ),
    MaxShortTiming_Cut = cms.double( 5.0 ),
    MinLongTiming_Cut = cms.double( -5.0 ),
    MaxLongTiming_Cut = cms.double( 5.0 ),
    ApplyTimeDPG = cms.bool( False ),
    ApplyPulseDPG = cms.bool( False ),
    ECAL_Compensate = cms.bool( False ),
    ECAL_Threshold = cms.double( 10.0 ),
    ECAL_Compensation = cms.double( 0.5 ),
    ECAL_Dead_Code = cms.uint32( 10 ),
    EM_Depth = cms.double( 22.0 ),
    HAD_Depth = cms.double( 47.0 ),
    verbose = cms.untracked.bool( False ),
    thresh_Barrel = cms.double( 0.4 ),
    thresh_Endcap = cms.double( 0.4 ),
    HCAL_Calib_29 = cms.double( 1.35 ),
    HF_Calib_29 = cms.double( 1.07 )
)
process.hltParticleFlowRecHitPS = cms.EDProducer( "PFRecHitProducerPS",
    ecalRecHitsES = cms.InputTag( 'hltESRecHitAll', 'EcalRecHitsES' ),
    verbose = cms.untracked.bool( False ),
    thresh_Barrel = cms.double( 7e-06 ),
    thresh_Endcap = cms.double( 7e-06 )
)
process.hltPentaJet40Central = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 40.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 5 )
)
process.hltPhoton125HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG125EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 999999.9 ),
    thrOverEEE = cms.double( 999999.9 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton20CaloIdVTIsoTClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG20R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.011 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton20CaloIdVTIsoTEcalIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton20CaloIdVTIsoTClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonEcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 5.0 ),
    thrRegularEE = cms.double( 5.0 ),
    thrOverEEB = cms.double( 0.012 ),
    thrOverEEE = cms.double( 0.012 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton20CaloIdVTIsoTEle8CaloIdLCaloIsoVLDoubleLegCombFilter = cms.HLTFilter( "HLTEgammaDoubleLegCombFilter",
    firstLegLastFilter = cms.InputTag( 'hltPhoton20CaloIdVTIsoTTrackIsoFilter' ),
    secondLegLastFilter = cms.InputTag( 'hltEle8CaloIdLCaloIsoVLNoL1SeedPixelMatchFilter' ),
    nrRequiredFirstLeg = cms.int32( 1 ),
    nrRequiredSecondLeg = cms.int32( 1 ),
    maxMatchDR = cms.double( 0.3 )
)
process.hltPhoton20CaloIdVTIsoTHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltPhoton20CaloIdVTIsoTEcalIsoFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton20CaloIdVTIsoTHcalIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton20CaloIdVTIsoTHEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 3.0 ),
    thrRegularEE = cms.double( 3.0 ),
    thrOverEEB = cms.double( 0.005 ),
    thrOverEEE = cms.double( 0.005 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton20CaloIdVTIsoTMu8ClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG20R9ShapeFilterMu3EG5' ),
    isoTag = cms.InputTag( 'hltL1IsoHLTClusterShape' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoHLTClusterShape' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.011 ),
    thrRegularEE = cms.double( 0.031 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton20CaloIdVTIsoTMu8EcalIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton20CaloIdVTIsoTMu8ClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonEcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 5.0 ),
    thrRegularEE = cms.double( 5.0 ),
    thrOverEEB = cms.double( 0.012 ),
    thrOverEEE = cms.double( 0.012 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton20CaloIdVTIsoTMu8HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltPhoton20CaloIdVTIsoTMu8EcalIsoFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.05 ),
    thrOverEEE = cms.double( 0.05 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton20CaloIdVTIsoTMu8HcalIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton20CaloIdVTIsoTMu8HEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 3.0 ),
    thrRegularEE = cms.double( 3.0 ),
    thrOverEEB = cms.double( 0.005 ),
    thrOverEEE = cms.double( 0.005 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton20CaloIdVTIsoTMu8TrackIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton20CaloIdVTIsoTMu8HcalIsoFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHollowTrackIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHollowTrackIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 3.0 ),
    thrRegularEE = cms.double( 3.0 ),
    thrOverEEB = cms.double( 0.002 ),
    thrOverEEE = cms.double( 0.002 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton20CaloIdVTIsoTTrackIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton20CaloIdVTIsoTHcalIsoFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHollowTrackIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHollowTrackIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 3.0 ),
    thrRegularEE = cms.double( 3.0 ),
    thrOverEEB = cms.double( 0.002 ),
    thrOverEEE = cms.double( 0.002 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton20EBOnlyNoSpikeFilterHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG20EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton20NoSpikeFilterHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG20EtFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton20R9IdPhoton18R9IdEgammaLHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG20R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton20R9IdPhoton18R9IdEgammaR9IDDoubleFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoubleIsoEG18HEFilter' ),
    isoTag = cms.InputTag( 'hltActivityR9ID' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( False ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.8 ),
    thrRegularEE = cms.double( 0.8 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltPhoton20R9IdPhoton18R9IdEgammaR9IDFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltPhoton20R9IdPhoton18R9IdEgammaLHEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsoR9ID' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsoR9ID' ),
    lessThan = cms.bool( False ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.8 ),
    thrRegularEE = cms.double( 0.8 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton26CaloIdLIsoVLPhoton18CaloIdLIsoVLEgammaClusterShapeDoubleFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoubleIsoEG18HEFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonClusterShape' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltPhoton26CaloIdLIsoVLPhoton18CaloIdLIsoVLEgammaEcalIsolDoubleFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton26CaloIdLIsoVLPhoton18CaloIdLIsoVLEgammaClusterShapeDoubleFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 6.0 ),
    thrRegularEE = cms.double( 6.0 ),
    thrOverEEB = cms.double( 0.012 ),
    thrOverEEE = cms.double( 0.012 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltPhoton26CaloIdLIsoVLPhoton18CaloIdLIsoVLEgammaHcalIsolDoubleFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton26CaloIdLIsoVLPhoton18CaloIdLIsoVLEgammaEcalIsolDoubleFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 4.0 ),
    thrRegularEE = cms.double( 4.0 ),
    thrOverEEB = cms.double( 0.005 ),
    thrOverEEE = cms.double( 0.005 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltPhoton26CaloIdLIsoVLPhoton18CaloIdLIsoVLEgammaTrackIsolDoubleFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton26CaloIdLIsoVLPhoton18CaloIdLIsoVLEgammaHcalIsolDoubleFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHollowTrackIsol' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 4.0 ),
    thrRegularEE = cms.double( 4.0 ),
    thrOverEEB = cms.double( 0.002 ),
    thrOverEEE = cms.double( 0.002 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltPhoton26IsoVLEcalIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltEG26HEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonEcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 6.0 ),
    thrRegularEE = cms.double( 6.0 ),
    thrOverEEB = cms.double( 0.012 ),
    thrOverEEE = cms.double( 0.012 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton26IsoVLHcalIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton26IsoVLEcalIsoFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 4.0 ),
    thrRegularEE = cms.double( 4.0 ),
    thrOverEEB = cms.double( 0.005 ),
    thrOverEEE = cms.double( 0.005 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton26IsoVLPhoton18IsoVLEgammaEcalIsolDoubleFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltDoubleIsoEG18HEFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 6.0 ),
    thrRegularEE = cms.double( 6.0 ),
    thrOverEEB = cms.double( 0.012 ),
    thrOverEEE = cms.double( 0.012 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltPhoton26IsoVLPhoton18IsoVLEgammaHcalIsolDoubleFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton26IsoVLPhoton18IsoVLEgammaEcalIsolDoubleFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 4.0 ),
    thrRegularEE = cms.double( 4.0 ),
    thrOverEEB = cms.double( 0.005 ),
    thrOverEEE = cms.double( 0.005 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltPhoton26IsoVLPhoton18IsoVLEgammaTrackIsolDoubleFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton26IsoVLPhoton18IsoVLEgammaHcalIsolDoubleFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHollowTrackIsol' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 4.0 ),
    thrRegularEE = cms.double( 4.0 ),
    thrOverEEB = cms.double( 0.002 ),
    thrOverEEE = cms.double( 0.002 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltPhoton26IsoVLTrackIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton26IsoVLHcalIsoFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHollowTrackIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHollowTrackIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 4.0 ),
    thrRegularEE = cms.double( 4.0 ),
    thrOverEEB = cms.double( 0.002 ),
    thrOverEEE = cms.double( 0.002 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton26Photon18EgammaLHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG26R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton30CaloIdVLIsoLEcalIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltEG30CaloIdVLClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonEcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 5.5 ),
    thrRegularEE = cms.double( 5.5 ),
    thrOverEEB = cms.double( 0.012 ),
    thrOverEEE = cms.double( 0.012 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton30CaloIdVLIsoLHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltPhoton30CaloIdVLIsoLEcalIsoFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton30CaloIdVLIsoLHcalIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton30CaloIdVLIsoLHEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 3.5 ),
    thrRegularEE = cms.double( 3.5 ),
    thrOverEEB = cms.double( 0.005 ),
    thrOverEEE = cms.double( 0.005 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton30CaloIdVLIsoLTrackIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton30CaloIdVLIsoLHcalIsoFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHollowTrackIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHollowTrackIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 3.5 ),
    thrRegularEE = cms.double( 3.5 ),
    thrOverEEB = cms.double( 0.002 ),
    thrOverEEE = cms.double( 0.002 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton32CaloIdLPhoton26CaloIdLEgammaClusterShapeDoubleFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltPhoton32CaloIdLPhoton26CaloIdLEgammaLHEDoubleFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonClusterShape' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( 0.014 ),
    thrRegularEE = cms.double( 0.035 ),
    thrOverEEB = cms.double( -1.0 ),
    thrOverEEE = cms.double( -1.0 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltPhoton32CaloIdLPhoton26CaloIdLEgammaLHEDoubleFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltDoubleIsoEG26R9ShapeFilter' ),
    isoTag = cms.InputTag( 'hltActivityPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( "" ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 2 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    L1NonIsoCand = cms.InputTag( "" )
)
process.hltPhoton75CaloIdVLHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG75CaloIdVLClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton75CaloIdVLIsoLEcalIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltEG75CaloIdVLClusterShapeFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonEcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonEcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 5.5 ),
    thrRegularEE = cms.double( 5.5 ),
    thrOverEEB = cms.double( 0.012 ),
    thrOverEEE = cms.double( 0.012 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton75CaloIdVLIsoLHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltPhoton75CaloIdVLIsoLEcalIsoFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton75CaloIdVLIsoLHcalIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton75CaloIdVLIsoLHEFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 3.5 ),
    thrRegularEE = cms.double( 3.5 ),
    thrOverEEB = cms.double( 0.005 ),
    thrOverEEE = cms.double( 0.005 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPhoton75CaloIdVLIsoLTrackIsoFilter = cms.HLTFilter( "HLTEgammaGenericQuadraticFilter",
    candTag = cms.InputTag( 'hltPhoton75CaloIdVLIsoLHcalIsoFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHollowTrackIsol' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHollowTrackIsol' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    thrRegularEB = cms.double( 3.5 ),
    thrRegularEE = cms.double( 3.5 ),
    thrOverEEB = cms.double( 0.002 ),
    thrOverEEE = cms.double( 0.002 ),
    thrOverE2EB = cms.double( 0.0 ),
    thrOverE2EE = cms.double( 0.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltPixelActivityFilter = cms.HLTFilter( "HLTPixelActivityFilter",
    inputTag = cms.InputTag( 'hltSiPixelClusters' ),
    saveTag = cms.untracked.bool( False ),
    minClusters = cms.uint32( 3 ),
    maxClusters = cms.uint32( 0 )
)
process.hltPixelAsymmetryFilter = cms.HLTFilter( "HLTPixelAsymmetryFilter",
    inputTag = cms.InputTag( 'hltSiPixelClusters' ),
    saveTag = cms.untracked.bool( False ),
    MinAsym = cms.double( 0.0 ),
    MaxAsym = cms.double( 1.0 ),
    MinCharge = cms.double( 4000.0 ),
    MinBarrel = cms.double( 10000.0 )
)
process.hltPixelCandsForHighMult = cms.EDProducer( "ConcreteChargedCandidateProducer",
    src = cms.InputTag( 'hltPixelTracksForHighMult' ),
    particleType = cms.string( "pi+" )
)
process.hltPixelClusterShapeFilter = cms.HLTFilter( "HLTPixelClusterShapeFilter",
    inputTag = cms.InputTag( 'hltSiPixelRecHits' ),
    saveTag = cms.untracked.bool( False ),
    minZ = cms.double( -10.1 ),
    maxZ = cms.double( 10.1 ),
    zStep = cms.double( 0.2 ),
    nhitsTrunc = cms.int32( 150 ),
    clusterTrunc = cms.double( 3.0 ),
    clusterPars = cms.vdouble(  0, 0.0045  )
)
process.hltPixelMatchElectronsActivity = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    TrackProducer = cms.InputTag( 'hltCtfActivityWithMaterialTracks' ),
    BSProducer = cms.InputTag( 'hltOnlineBeamSpot' )
)
process.hltPixelMatchElectronsL1Iso = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    TrackProducer = cms.InputTag( 'hltCtfL1IsoWithMaterialTracks' ),
    BSProducer = cms.InputTag( 'hltOnlineBeamSpot' )
)
process.hltPixelMatchElectronsL1NonIso = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    TrackProducer = cms.InputTag( 'hltCtfL1NonIsoWithMaterialTracks' ),
    BSProducer = cms.InputTag( 'hltOnlineBeamSpot' )
)
process.hltPixelTracks = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( False ),
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
      RegionPSet = cms.PSet(
        precise = cms.bool( True ),
        ptMin = cms.double( 0.9 ),
        originRadius = cms.double( 0.2 ),
        beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
        originHalfLength = cms.double( 15.9 )
      )
    ),
    OrderedHitsFactoryPSet = cms.PSet(
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      SeedingLayers = cms.string( "hltESPPixelLayerTriplets" ),
      GeneratorPSet = cms.PSet(
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 10000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" ),
        extraHitRZtolerance = cms.double( 0.06 )
      )
    ),
    FitterPSet = cms.PSet(
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" )
    ),
    FilterPSet = cms.PSet(
      chi2 = cms.double( 1000.0 ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
      nSigmaInvPtTolerance = cms.double( 0.0 ),
      ptMin = cms.double( 0.1 ),
      tipMax = cms.double( 1.0 )
    ),
    CleanerPSet = cms.PSet(
      ComponentName = cms.string( "PixelTrackCleanerBySharedHits" )
    )
)
process.hltPixelTracksForHighMult = cms.EDProducer( "PixelTrackProducer",
    useFilterWithES = cms.bool( False ),
    RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
      RegionPSet = cms.PSet(
        precise = cms.bool( True ),
        ptMin = cms.double( 0.6 ),
        originRadius = cms.double( 0.0015 ),
        beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
        originHalfLength = cms.double( 10.1 )
      )
    ),
    OrderedHitsFactoryPSet = cms.PSet(
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet(
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 10000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" ),
        extraHitRZtolerance = cms.double( 0.06 )
      ),
      SeedingLayers = cms.string( "hltESPPixelLayerTriplets" )
    ),
    FitterPSet = cms.PSet(
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" )
    ),
    FilterPSet = cms.PSet(
      chi2 = cms.double( 1000.0 ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
      nSigmaInvPtTolerance = cms.double( 0.0 ),
      ptMin = cms.double( 0.6 ),
      tipMax = cms.double( 1.0 )
    ),
    CleanerPSet = cms.PSet(
      ComponentName = cms.string( "PixelTrackCleanerBySharedHits" )
    )
)
process.hltPixelVertices = cms.EDProducer( "PixelVertexProducer",
    Verbosity = cms.int32( 0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    UseError = cms.bool( True ),
    WtAverage = cms.bool( True ),
    ZOffset = cms.double( 5.0 ),
    ZSeparation = cms.double( 0.05 ),
    NTrkMin = cms.int32( 2 ),
    PtMin = cms.double( 1.0 ),
    TrackCollection = cms.InputTag( 'hltPixelTracks' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    Method2 = cms.bool( True )
)
process.hltPixelVerticesForHighMult = cms.EDProducer( "PixelVertexProducer",
    Verbosity = cms.int32( 0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    UseError = cms.bool( True ),
    WtAverage = cms.bool( True ),
    ZOffset = cms.double( 5.0 ),
    ZSeparation = cms.double( 0.05 ),
    NTrkMin = cms.int32( 50 ),
    PtMin = cms.double( 0.6 ),
    TrackCollection = cms.InputTag( 'hltPixelTracksForHighMult' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    Method2 = cms.bool( True )
)
process.hltPreALCAP0Output = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreALCAPHISYMOutput = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreAlCaDTErrors = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreAlCaEcalEta = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreAlCaEcalPhiSym = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreAlCaEcalPi0 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreBTagMuDiJet20Mu5 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreBTagMuDiJet60Mu7 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreBTagMuDiJet80Mu9 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreCalibration = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreCalibrationOutput = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreCenJet80MET100 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreCenJet80MET160 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreCenJet80MET65 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreCenJet80MET80 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDQMOutput = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDQMOutputSmart = cms.HLTFilter( "TriggerResultsFilter",
    triggerConditions = cms.vstring( "HLT_BTagMu_DiJet20_Mu5_v1",
       "HLT_BTagMu_DiJet60_Mu7_v1",
       "HLT_BTagMu_DiJet80_Mu9_v1",
       "HLT_BeamGas_BSC_v1",
       "HLT_BeamGas_HF_v1",
       "HLT_Calibration_v1 / 10",
       "HLT_CentralJet80_MET100_v1",
       "HLT_CentralJet80_MET160_v1",
       "HLT_CentralJet80_MET65_v1",
       "HLT_CentralJet80_MET80_v1",
       "HLT_DTErrors_v1",
       "HLT_DiJet100_PT100_v1",
       "HLT_DiJet130_PT130_v1",
       "HLT_DiJet60_MET45_v1",
       "HLT_DiJet70_PT70_v1",
       "HLT_DiJetAve100U_v4",
       "HLT_DiJetAve140U_v4",
       "HLT_DiJetAve15U_v4",
       "HLT_DiJetAve180U_v4",
       "HLT_DiJetAve300U_v4",
       "HLT_DiJetAve30U_v4",
       "HLT_DiJetAve50U_v4",
       "HLT_DiJetAve70U_v4",
       "HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_v1",
       "HLT_DoubleEle8_CaloIdL_TrkIdVL_HT160_v2",
       "HLT_DoubleEle8_CaloIdT_TrkIdVL_HT160_v2",
       "HLT_DoubleIsoPFTau20_Trk5_v1",
       "HLT_DoubleJet30_ForwardBackward_v1",
       "HLT_DoubleJet60_ForwardBackward_v1",
       "HLT_DoubleJet70_ForwardBackward_v1",
       "HLT_DoubleJet80_ForwardBackward_v1",
       "HLT_DoubleMu3_Bs_v1",
       "HLT_DoubleMu3_HT160_v2",
       "HLT_DoubleMu3_HT200_v2",
       "HLT_DoubleMu3_Jpsi_v1",
       "HLT_DoubleMu3_Quarkonium_v1",
       "HLT_DoubleMu3_v3",
       "HLT_DoubleMu4_Acoplanarity03_v1",
       "HLT_DoubleMu5_Ele8_CaloIdL_TrkIdVL_v2",
       "HLT_DoubleMu5_Ele8_v2",
       "HLT_DoubleMu6_v1",
       "HLT_DoubleMu7_v1",
       "HLT_DoublePhoton33_v1",
       "HLT_DoublePhoton5_IsoVL_CEP_v1",
       "HLT_EcalCalibration_v1 / 10",
       "HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v2",
       "HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v2",
       "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1",
       "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1",
       "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1",
       "HLT_Ele15_CaloIdVT_TrkIdT_LooseIsoPFTau15_v1",
       "HLT_Ele17_CaloIdL_CaloIsoVL_Ele15_HFL_v1",
       "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1",
       "HLT_Ele17_CaloIdL_CaloIsoVL_v1",
       "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v2",
       "HLT_Ele25_CaloIdVT_TrkIdT_CentralDiJet30_v1",
       "HLT_Ele25_CaloIdVT_TrkIdT_CentralJet30_v1",
       "HLT_Ele25_CaloIdVT_TrkIdT_CentralJet40_BTagIP_v1",
       "HLT_Ele25_CaloIdVT_TrkIdT_CentralTriJet30_v1",
       "HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1",
       "HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v1",
       "HLT_Ele45_CaloIdVT_TrkIdT_v1",
       "HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v1",
       "HLT_Ele8_CaloIdL_CaloIsoVL_v1",
       "HLT_Ele8_CaloIdL_TrkIdVL_v1",
       "HLT_Ele8_v1",
       "HLT_Ele90_NoSpikeFilter_v1",
       "HLT_ExclDiJet60_HFAND_v1",
       "HLT_ExclDiJet60_HFOR_v1",
       "HLT_GlobalRunHPDNoise_v2",
       "HLT_HT160_v2",
       "HLT_HT240_v2",
       "HLT_HT260_MHT60_v2",
       "HLT_HT260_v2",
       "HLT_HT300_MHT75_v2",
       "HLT_HT300_v2",
       "HLT_HT360_v2",
       "HLT_HT440_v2",
       "HLT_HT520_v2",
       "HLT_HcalCalibration_v1",
       "HLT_HcalNZS_v2",
       "HLT_HcalPhiSym_v2",
       "HLT_IsoMu12_LooseIsoPFTau10_v1",
       "HLT_IsoMu12_v1",
       "HLT_IsoMu15_v5",
       "HLT_IsoMu17_CentralJet40_BTagIP_v1",
       "HLT_IsoMu17_v5",
       "HLT_IsoMu30_v1",
       "HLT_IsoPFTau35_Trk20_MET45_v1",
       "HLT_IsoTrackHB_v2",
       "HLT_IsoTrackHE_v3",
       "HLT_Jet110_v1",
       "HLT_Jet150_v1",
       "HLT_Jet190_v1",
       "HLT_Jet240_v1",
       "HLT_Jet30_v1",
       "HLT_Jet370_NoJetID_v1",
       "HLT_Jet370_v1",
       "HLT_Jet60_v1",
       "HLT_Jet80_v1",
       "HLT_JetE30_NoBPTX3BX_NoHalo_v2",
       "HLT_JetE30_NoBPTX_NoHalo_v2",
       "HLT_JetE30_NoBPTX_v1",
       "HLT_L1DoubleMu0_v1",
       "HLT_L1MuOpen_AntiBPTX_v2",
       "HLT_L1SingleEG5_v1",
       "HLT_L1SingleJet36_v1",
       "HLT_L1SingleMu10_v1",
       "HLT_L1SingleMu20_v1",
       "HLT_L1SingleMuOpen_DT_v1",
       "HLT_L1SingleMuOpen_v1",
       "HLT_L1Tech_BSC_halo_v1",
       "HLT_L1Tech_BSC_minBias_threshold1_v2/10",
       "HLT_L1Tech_HBHEHO_totalOR_v1",
       "HLT_L1TrackerCosmics_v2",
       "HLT_L1_BeamHalo_v1",
       "HLT_L1_Interbunch_BSC_v1",
       "HLT_L1_PreCollisions_v1",
       "HLT_L2DoubleMu0_v2",
       "HLT_L2DoubleMu35_NoVertex_v1",
       "HLT_L2Mu10_v1",
       "HLT_L2Mu20_v1",
       "HLT_L2MuOpen_NoVertex_v1",
       "HLT_L3MuonsCosmicTracking_v1",
       "HLT_LogMonitor_v1",
       "HLT_MET100_v1",
       "HLT_MET120_v1",
       "HLT_MET200_v1",
       "HLT_MR100_v1",
       "HLT_Meff440_v2",
       "HLT_Meff520_v2",
       "HLT_Meff640_v2",
       "HLT_Mu10_Ele10_CaloIdL_v2",
       "HLT_Mu12_v1",
       "HLT_Mu15_DoublePhoton15_CaloIdL_v2",
       "HLT_Mu15_LooseIsoPFTau20_v1",
       "HLT_Mu15_Photon20_CaloIdL_v2",
       "HLT_Mu15_v2",
       "HLT_Mu17_CentralJet30_v1",
       "HLT_Mu17_CentralJet40_BTagIP_v1",
       "HLT_Mu17_DiCentralJet30_v1",
       "HLT_Mu17_Ele8_CaloIdL_v1",
       "HLT_Mu17_TriCentralJet30_v1",
       "HLT_Mu20_v1",
       "HLT_Mu24_v1",
       "HLT_Mu30_v1",
       "HLT_Mu3_Ele8_CaloIdL_TrkIdVL_HT160_v2",
       "HLT_Mu3_Ele8_CaloIdT_TrkIdVL_HT160_v2",
       "HLT_Mu3_Track3_Jpsi_v4",
       "HLT_Mu3_v3",
       "HLT_Mu5_DoubleEle8_v2",
       "HLT_Mu5_Ele8_CaloIdL_TrkIdVL_Ele8_v2",
       "HLT_Mu5_HT200_v3",
       "HLT_Mu5_L2Mu2_Jpsi_v1",
       "HLT_Mu5_L2Mu2_v1",
       "HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1",
       "HLT_Mu5_v3",
       "HLT_Mu7_Track5_Jpsi_v1",
       "HLT_Mu7_Track7_Jpsi_v1",
       "HLT_Mu8_Ele17_CaloIdL_v1",
       "HLT_Mu8_HT200_v2",
       "HLT_Mu8_Jet40_v2",
       "HLT_Mu8_Photon20_CaloIdVT_IsoT_v2",
       "HLT_Mu8_v1",
       "HLT_PFMHT150_v1",
       "HLT_Photon125_NoSpikeFilter_v1",
       "HLT_Photon20_CaloIdVT_IsoT_Ele8_CaloIdL_CaloIsoVL_v1",
       "HLT_Photon20_R9Id_Photon18_R9Id_v1",
       "HLT_Photon26_CaloIdL_IsoVL_Photon18_CaloIdL_IsoVL_v1",
       "HLT_Photon26_CaloIdL_IsoVL_Photon18_v1",
       "HLT_Photon26_IsoVL_Photon18_IsoVL_v1",
       "HLT_Photon26_IsoVL_Photon18_v1",
       "HLT_Photon26_Photon18_v1",
       "HLT_Photon30_CaloIdVL_IsoL_v1",
       "HLT_Photon30_CaloIdVL_v1",
       "HLT_Photon32_CaloIdL_Photon26_CaloIdL_v1",
       "HLT_Photon60_CaloIdL_HT200_v1",
       "HLT_Photon70_CaloIdL_HT200_v1",
       "HLT_Photon70_CaloIdL_HT300_v1",
       "HLT_Photon70_CaloIdL_MHT30_v1",
       "HLT_Photon70_CaloIdL_MHT50_v1",
       "HLT_Photon75_CaloIdVL_IsoL_v1",
       "HLT_Photon75_CaloIdVL_v1",
       "HLT_Physics_v1 / 500",
       "HLT_PixelTracks_Multiplicity110_v1",
       "HLT_PixelTracks_Multiplicity125_v1",
       "HLT_QuadJet40_IsoPFTau40_v1",
       "HLT_QuadJet40_v1",
       "HLT_QuadJet50_BTagIP_v1",
       "HLT_QuadJet50_Jet40_v1",
       "HLT_QuadJet60_v1",
       "HLT_QuadJet70_v1",
       "HLT_R032_MR100_v1",
       "HLT_R032_v1",
       "HLT_R035_MR100_v1",
       "HLT_Random_v1",
       "HLT_RegionalCosmicTracking_v1",
       "HLT_TrackerCalibration_v1 ",
       "HLT_TripleEle10_CaloIdL_TrkIdVL_v1",
       "HLT_TripleMu5_v2",
       "HLT_ZeroBias_v1" ),
    hltResults = cms.InputTag( 'TriggerResults' ),
    l1tResults = cms.InputTag( 'hltGtDigis' ),
    l1tIgnoreMask = cms.bool( False ),
    daqPartitions = cms.uint32( 1 ),
    throw = cms.bool( True ),
    l1techIgnorePrescales = cms.bool( False )
)
process.hltPreDiJet100PT100 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDiJet130PT130 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDiJet60MET45 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDiJet70PT70 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDiJetAve100U = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDiJetAve140U = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDiJetAve15U = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDiJetAve180U = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDiJetAve300U = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDiJetAve30U = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDiJetAve50U = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDiJetAve70U = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleEle10CaloIdLTrkIdVLEle10 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleEle8CaloIdLTrkIdVLHT160 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleEle8CaloIdTTrkIdVLHT160 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleIsoTau20Trk5 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleJet30ForwardBackward = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleJet60ForwardBackward = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleJet70ForwardBackward = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleJet80ForwardBackward = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleMu0Bs = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleMu0Jpsi = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleMu0Quarkonium = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleMu3 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleMu3HT160 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleMu4Excl = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleMu5Ele8 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleMu5Ele8CaloIdLTrkIdVL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleMu6 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoubleMu7 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoublePhoton33 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreDoublePhoton5IsoVLCEP = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEcalCalibration = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEcalCalibrationOutput = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle10CaloIdLCaloIsoVLTrkIdVLTrkIsoVLHT200 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle10CaloIdTCaloIsoVLTrkIdTTrkIsoVLHT200 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle15CaloIdVTCaloIsoTTrkIdTTrkIsoT = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTLooseIsoPFTau15 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTLooseIsoPFTau20 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle15CaloIdVTTrkIdTLooseIsoPFTau15 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle17CaloIdLCaloIsoVL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle17CaloIdLCaloIsoVLEle15HFL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle17CaloIdLCaloIsoVLEle8CaloIdLCaloIsoVL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8Mass30 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle25CaloIdVTTrkIdTCentralDiJet30 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle25CaloIdVTTrkIdTCentralJet30 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle25CaloIdVTTrkIdTCentralJet40BTagIP = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle25CaloIdVTTrkIdTCentralTriJet30 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle27CaloIdVTCaloIsoTTrkIdTTrkIsoT = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle32CaloIdLCaloIsoVLSC17 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle45CaloIdVTTrkIdT = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle8 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle8CaloIdLCaloIsoVL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle8CaloIdLCaloIsoVLJet40 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle8CaloIdLTrkIdVL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreEle90NoSpikeFilter = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreExclDiJet60HFAND = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreExclDiJet60HFOR = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreExpressOutput = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreExpressOutputSmart = cms.HLTFilter( "TriggerResultsFilter",
    triggerConditions = cms.vstring( "HLT_L1Tech_BSC_minBias_threshold1_v2 / 10",
       "HLT_Mu15_v2",
       "HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1",
       "HLT_ZeroBias_v1 / 8" ),
    hltResults = cms.InputTag( 'TriggerResults' ),
    l1tResults = cms.InputTag( 'hltGtDigis' ),
    l1tIgnoreMask = cms.bool( False ),
    daqPartitions = cms.uint32( 1 ),
    throw = cms.bool( True ),
    l1techIgnorePrescales = cms.bool( False )
)
process.hltPreFEDIntegrity = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreGlobalRunHPDNoise = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreHLTDQMOutput = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreHLTDQMOutputSmart = cms.HLTFilter( "TriggerResultsFilter",
    triggerConditions = cms.vstring( "AlCa_EcalEta_v2 / 100",
       "AlCa_EcalPhiSym_v2 / 100",
       "AlCa_EcalPi0_v3 / 100",
       "AlCa_RPCMuonNoHits_v2 / 100",
       "AlCa_RPCMuonNoTriggers_v2 / 100",
       "AlCa_RPCMuonNormalisation_v2 / 100",
       "HLT_BTagMu_DiJet20_Mu5_v1",
       "HLT_BTagMu_DiJet60_Mu7_v1",
       "HLT_BTagMu_DiJet80_Mu9_v1",
       "HLT_BeamGas_BSC_v1",
       "HLT_BeamGas_HF_v1",
       "HLT_CentralJet80_MET100_v1",
       "HLT_CentralJet80_MET160_v1",
       "HLT_CentralJet80_MET65_v1",
       "HLT_CentralJet80_MET80_v1",
       "HLT_DTErrors_v1",
       "HLT_DiJet100_PT100_v1",
       "HLT_DiJet130_PT130_v1",
       "HLT_DiJet60_MET45_v1",
       "HLT_DiJet70_PT70_v1",
       "HLT_DiJetAve100U_v4",
       "HLT_DiJetAve140U_v4",
       "HLT_DiJetAve15U_v4",
       "HLT_DiJetAve180U_v4",
       "HLT_DiJetAve300U_v4",
       "HLT_DiJetAve30U_v4",
       "HLT_DiJetAve50U_v4",
       "HLT_DiJetAve70U_v4",
       "HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_v1",
       "HLT_DoubleEle8_CaloIdL_TrkIdVL_HT160_v2",
       "HLT_DoubleEle8_CaloIdT_TrkIdVL_HT160_v2",
       "HLT_DoubleIsoPFTau20_Trk5_v1",
       "HLT_DoubleJet30_ForwardBackward_v1",
       "HLT_DoubleJet60_ForwardBackward_v1",
       "HLT_DoubleJet70_ForwardBackward_v1",
       "HLT_DoubleJet80_ForwardBackward_v1",
       "HLT_DoubleMu3_Bs_v1",
       "HLT_DoubleMu3_HT160_v2",
       "HLT_DoubleMu3_HT200_v2",
       "HLT_DoubleMu3_Jpsi_v1",
       "HLT_DoubleMu3_Quarkonium_v1",
       "HLT_DoubleMu3_v3",
       "HLT_DoubleMu4_Acoplanarity03_v1",
       "HLT_DoubleMu5_Ele8_CaloIdL_TrkIdVL_v2",
       "HLT_DoubleMu5_Ele8_v2",
       "HLT_DoubleMu6_v1",
       "HLT_DoubleMu7_v1",
       "HLT_DoublePhoton33_v1",
       "HLT_DoublePhoton5_IsoVL_CEP_v1",
       "HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v2",
       "HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v2",
       "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1",
       "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1",
       "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1",
       "HLT_Ele15_CaloIdVT_TrkIdT_LooseIsoPFTau15_v1",
       "HLT_Ele17_CaloIdL_CaloIsoVL_Ele15_HFL_v1",
       "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1",
       "HLT_Ele17_CaloIdL_CaloIsoVL_v1",
       "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v2",
       "HLT_Ele25_CaloIdVT_TrkIdT_CentralDiJet30_v1",
       "HLT_Ele25_CaloIdVT_TrkIdT_CentralJet30_v1",
       "HLT_Ele25_CaloIdVT_TrkIdT_CentralJet40_BTagIP_v1",
       "HLT_Ele25_CaloIdVT_TrkIdT_CentralTriJet30_v1",
       "HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1",
       "HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v1",
       "HLT_Ele45_CaloIdVT_TrkIdT_v1",
       "HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v1",
       "HLT_Ele8_CaloIdL_CaloIsoVL_v1",
       "HLT_Ele8_CaloIdL_TrkIdVL_v1",
       "HLT_Ele8_v1",
       "HLT_Ele90_NoSpikeFilter_v1",
       "HLT_ExclDiJet60_HFAND_v1",
       "HLT_ExclDiJet60_HFOR_v1",
       "HLT_GlobalRunHPDNoise_v2",
       "HLT_HT160_v2",
       "HLT_HT240_v2",
       "HLT_HT260_MHT60_v2",
       "HLT_HT260_v2",
       "HLT_HT300_MHT75_v2",
       "HLT_HT300_v2",
       "HLT_HT360_v2",
       "HLT_HT440_v2",
       "HLT_HT520_v2",
       "HLT_HcalNZS_v2",
       "HLT_HcalPhiSym_v2",
       "HLT_IsoMu12_LooseIsoPFTau10_v1",
       "HLT_IsoMu12_v1",
       "HLT_IsoMu15_v5",
       "HLT_IsoMu17_CentralJet40_BTagIP_v1",
       "HLT_IsoMu17_v5",
       "HLT_IsoMu30_v1",
       "HLT_IsoPFTau35_Trk20_MET45_v1",
       "HLT_IsoTrackHB_v2",
       "HLT_IsoTrackHE_v3",
       "HLT_Jet110_v1",
       "HLT_Jet150_v1",
       "HLT_Jet190_v1",
       "HLT_Jet240_v1",
       "HLT_Jet30_v1",
       "HLT_Jet370_NoJetID_v1",
       "HLT_Jet370_v1",
       "HLT_Jet60_v1",
       "HLT_Jet80_v1",
       "HLT_JetE30_NoBPTX3BX_NoHalo_v2",
       "HLT_JetE30_NoBPTX_NoHalo_v2",
       "HLT_JetE30_NoBPTX_v1",
       "HLT_L1DoubleMu0_v1",
       "HLT_L1MuOpen_AntiBPTX_v2",
       "HLT_L1SingleEG5_v1",
       "HLT_L1SingleJet36_v1",
       "HLT_L1SingleMu10_v1",
       "HLT_L1SingleMu20_v1",
       "HLT_L1SingleMuOpen_DT_v1",
       "HLT_L1SingleMuOpen_v1",
       "HLT_L1Tech_BSC_halo_v1",
       "HLT_L1Tech_BSC_minBias_threshold1_v2",
       "HLT_L1Tech_HBHEHO_totalOR_v1",
       "HLT_L1TrackerCosmics_v2",
       "HLT_L1_BeamHalo_v1",
       "HLT_L1_Interbunch_BSC_v1",
       "HLT_L1_PreCollisions_v1",
       "HLT_L2DoubleMu0_v2",
       "HLT_L2DoubleMu35_NoVertex_v1",
       "HLT_L2Mu10_v1",
       "HLT_L2Mu20_v1",
       "HLT_L2MuOpen_NoVertex_v1",
       "HLT_L3MuonsCosmicTracking_v1",
       "HLT_LogMonitor_v1",
       "HLT_MET100_v1",
       "HLT_MET120_v1",
       "HLT_MET200_v1",
       "HLT_MR100_v1",
       "HLT_Meff440_v2",
       "HLT_Meff520_v2",
       "HLT_Meff640_v2",
       "HLT_Mu10_Ele10_CaloIdL_v2",
       "HLT_Mu12_v1",
       "HLT_Mu15_DoublePhoton15_CaloIdL_v2",
       "HLT_Mu15_LooseIsoPFTau20_v1",
       "HLT_Mu15_Photon20_CaloIdL_v2",
       "HLT_Mu15_v2",
       "HLT_Mu17_CentralJet30_v1",
       "HLT_Mu17_CentralJet40_BTagIP_v1",
       "HLT_Mu17_DiCentralJet30_v1",
       "HLT_Mu17_Ele8_CaloIdL_v1",
       "HLT_Mu17_TriCentralJet30_v1",
       "HLT_Mu20_v1",
       "HLT_Mu24_v1",
       "HLT_Mu30_v1",
       "HLT_Mu3_Ele8_CaloIdL_TrkIdVL_HT160_v2",
       "HLT_Mu3_Ele8_CaloIdT_TrkIdVL_HT160_v2",
       "HLT_Mu3_Track3_Jpsi_v4",
       "HLT_Mu3_v3",
       "HLT_Mu5_DoubleEle8_v2",
       "HLT_Mu5_Ele8_CaloIdL_TrkIdVL_Ele8_v2",
       "HLT_Mu5_HT200_v3",
       "HLT_Mu5_L2Mu2_Jpsi_v1",
       "HLT_Mu5_L2Mu2_v1",
       "HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1",
       "HLT_Mu5_v3",
       "HLT_Mu7_Track5_Jpsi_v1",
       "HLT_Mu7_Track7_Jpsi_v1",
       "HLT_Mu8_Ele17_CaloIdL_v1",
       "HLT_Mu8_HT200_v2",
       "HLT_Mu8_Jet40_v2",
       "HLT_Mu8_Photon20_CaloIdVT_IsoT_v2",
       "HLT_Mu8_v1",
       "HLT_PFMHT150_v1",
       "HLT_Photon125_NoSpikeFilter_v1",
       "HLT_Photon20_CaloIdVT_IsoT_Ele8_CaloIdL_CaloIsoVL_v1",
       "HLT_Photon20_R9Id_Photon18_R9Id_v1",
       "HLT_Photon26_CaloIdL_IsoVL_Photon18_CaloIdL_IsoVL_v1",
       "HLT_Photon26_CaloIdL_IsoVL_Photon18_v1",
       "HLT_Photon26_IsoVL_Photon18_IsoVL_v1",
       "HLT_Photon26_IsoVL_Photon18_v1",
       "HLT_Photon26_Photon18_v1",
       "HLT_Photon30_CaloIdVL_IsoL_v1",
       "HLT_Photon30_CaloIdVL_v1",
       "HLT_Photon32_CaloIdL_Photon26_CaloIdL_v1",
       "HLT_Photon60_CaloIdL_HT200_v1",
       "HLT_Photon70_CaloIdL_HT200_v1",
       "HLT_Photon70_CaloIdL_HT300_v1",
       "HLT_Photon70_CaloIdL_MHT30_v1",
       "HLT_Photon70_CaloIdL_MHT50_v1",
       "HLT_Photon75_CaloIdVL_IsoL_v1",
       "HLT_Photon75_CaloIdVL_v1",
       "HLT_Physics_v1 / 500",
       "HLT_PixelTracks_Multiplicity110_v1",
       "HLT_PixelTracks_Multiplicity125_v1",
       "HLT_QuadJet40_IsoPFTau40_v1",
       "HLT_QuadJet40_v1",
       "HLT_QuadJet50_BTagIP_v1",
       "HLT_QuadJet50_Jet40_v1",
       "HLT_QuadJet60_v1",
       "HLT_QuadJet70_v1",
       "HLT_R032_MR100_v1",
       "HLT_R032_v1",
       "HLT_R035_MR100_v1",
       "HLT_Random_v1",
       "HLT_RegionalCosmicTracking_v1",
       "HLT_TripleEle10_CaloIdL_TrkIdVL_v1",
       "HLT_TripleMu5_v2",
       "HLT_ZeroBias_v1" ),
    hltResults = cms.InputTag( 'TriggerResults' ),
    l1tResults = cms.InputTag( 'hltGtDigis' ),
    l1tIgnoreMask = cms.bool( False ),
    daqPartitions = cms.uint32( 1 ),
    throw = cms.bool( True ),
    l1techIgnorePrescales = cms.bool( False )
)
process.hltPreHLTDQMResultsOutput = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreHLTMONOutput = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreHLTMONOutputSmart = cms.HLTFilter( "TriggerResultsFilter",
    triggerConditions = cms.vstring( "AlCa_EcalEta_v2 / 100",
       "AlCa_EcalPhiSym_v2 / 100",
       "AlCa_EcalPi0_v3 / 100",
       "AlCa_RPCMuonNoHits_v2 / 100",
       "AlCa_RPCMuonNoTriggers_v2 / 100",
       "AlCa_RPCMuonNormalisation_v2 / 100",
       "HLT_BTagMu_DiJet20_Mu5_v1",
       "HLT_BTagMu_DiJet60_Mu7_v1",
       "HLT_BTagMu_DiJet80_Mu9_v1",
       "HLT_BeamGas_BSC_v1",
       "HLT_BeamGas_HF_v1",
       "HLT_CentralJet80_MET100_v1",
       "HLT_CentralJet80_MET160_v1",
       "HLT_CentralJet80_MET65_v1",
       "HLT_CentralJet80_MET80_v1",
       "HLT_DTErrors_v1",
       "HLT_DiJet100_PT100_v1",
       "HLT_DiJet130_PT130_v1",
       "HLT_DiJet60_MET45_v1",
       "HLT_DiJet70_PT70_v1",
       "HLT_DiJetAve100U_v4",
       "HLT_DiJetAve140U_v4",
       "HLT_DiJetAve15U_v4",
       "HLT_DiJetAve180U_v4",
       "HLT_DiJetAve300U_v4",
       "HLT_DiJetAve30U_v4",
       "HLT_DiJetAve50U_v4",
       "HLT_DiJetAve70U_v4",
       "HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_v1",
       "HLT_DoubleEle8_CaloIdL_TrkIdVL_HT160_v2",
       "HLT_DoubleEle8_CaloIdT_TrkIdVL_HT160_v2",
       "HLT_DoubleIsoPFTau20_Trk5_v1",
       "HLT_DoubleJet30_ForwardBackward_v1",
       "HLT_DoubleJet60_ForwardBackward_v1",
       "HLT_DoubleJet70_ForwardBackward_v1",
       "HLT_DoubleJet80_ForwardBackward_v1",
       "HLT_DoubleMu3_Bs_v1",
       "HLT_DoubleMu3_HT160_v2",
       "HLT_DoubleMu3_HT200_v2",
       "HLT_DoubleMu3_Jpsi_v1",
       "HLT_DoubleMu3_Quarkonium_v1",
       "HLT_DoubleMu3_v3",
       "HLT_DoubleMu4_Acoplanarity03_v1",
       "HLT_DoubleMu5_Ele8_CaloIdL_TrkIdVL_v2",
       "HLT_DoubleMu5_Ele8_v2",
       "HLT_DoubleMu6_v1",
       "HLT_DoubleMu7_v1",
       "HLT_DoublePhoton33_v1",
       "HLT_DoublePhoton5_IsoVL_CEP_v1",
       "HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v2",
       "HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v2",
       "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1",
       "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1",
       "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1",
       "HLT_Ele15_CaloIdVT_TrkIdT_LooseIsoPFTau15_v1",
       "HLT_Ele17_CaloIdL_CaloIsoVL_Ele15_HFL_v1",
       "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1",
       "HLT_Ele17_CaloIdL_CaloIsoVL_v1",
       "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v2",
       "HLT_Ele25_CaloIdVT_TrkIdT_CentralDiJet30_v1",
       "HLT_Ele25_CaloIdVT_TrkIdT_CentralJet30_v1",
       "HLT_Ele25_CaloIdVT_TrkIdT_CentralJet40_BTagIP_v1",
       "HLT_Ele25_CaloIdVT_TrkIdT_CentralTriJet30_v1",
       "HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1",
       "HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v1",
       "HLT_Ele45_CaloIdVT_TrkIdT_v1",
       "HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v1",
       "HLT_Ele8_CaloIdL_CaloIsoVL_v1",
       "HLT_Ele8_CaloIdL_TrkIdVL_v1",
       "HLT_Ele8_v1",
       "HLT_Ele90_NoSpikeFilter_v1",
       "HLT_ExclDiJet60_HFAND_v1",
       "HLT_ExclDiJet60_HFOR_v1",
       "HLT_GlobalRunHPDNoise_v2",
       "HLT_HT160_v2",
       "HLT_HT240_v2",
       "HLT_HT260_MHT60_v2",
       "HLT_HT260_v2",
       "HLT_HT300_MHT75_v2",
       "HLT_HT300_v2",
       "HLT_HT360_v2",
       "HLT_HT440_v2",
       "HLT_HT520_v2",
       "HLT_HcalNZS_v2",
       "HLT_HcalPhiSym_v2",
       "HLT_IsoMu12_LooseIsoPFTau10_v1",
       "HLT_IsoMu12_v1",
       "HLT_IsoMu15_v5",
       "HLT_IsoMu17_CentralJet40_BTagIP_v1",
       "HLT_IsoMu17_v5",
       "HLT_IsoMu30_v1",
       "HLT_IsoPFTau35_Trk20_MET45_v1",
       "HLT_IsoTrackHB_v2",
       "HLT_IsoTrackHE_v3",
       "HLT_Jet110_v1",
       "HLT_Jet150_v1",
       "HLT_Jet190_v1",
       "HLT_Jet240_v1",
       "HLT_Jet30_v1",
       "HLT_Jet370_NoJetID_v1",
       "HLT_Jet370_v1",
       "HLT_Jet60_v1",
       "HLT_Jet80_v1",
       "HLT_JetE30_NoBPTX3BX_NoHalo_v2",
       "HLT_JetE30_NoBPTX_NoHalo_v2",
       "HLT_JetE30_NoBPTX_v1",
       "HLT_L1DoubleMu0_v1",
       "HLT_L1MuOpen_AntiBPTX_v2",
       "HLT_L1SingleEG5_v1",
       "HLT_L1SingleJet36_v1",
       "HLT_L1SingleMu10_v1",
       "HLT_L1SingleMu20_v1",
       "HLT_L1SingleMuOpen_DT_v1",
       "HLT_L1SingleMuOpen_v1",
       "HLT_L1Tech_BSC_halo_v1",
       "HLT_L1Tech_BSC_minBias_threshold1_v2",
       "HLT_L1Tech_HBHEHO_totalOR_v1",
       "HLT_L1TrackerCosmics_v2",
       "HLT_L1_BeamHalo_v1",
       "HLT_L1_Interbunch_BSC_v1",
       "HLT_L1_PreCollisions_v1",
       "HLT_L2DoubleMu0_v2",
       "HLT_L2DoubleMu35_NoVertex_v1",
       "HLT_L2Mu10_v1",
       "HLT_L2Mu20_v1",
       "HLT_L2MuOpen_NoVertex_v1",
       "HLT_L3MuonsCosmicTracking_v1",
       "HLT_LogMonitor_v1",
       "HLT_MET100_v1",
       "HLT_MET120_v1",
       "HLT_MET200_v1",
       "HLT_MR100_v1",
       "HLT_Meff440_v2",
       "HLT_Meff520_v2",
       "HLT_Meff640_v2",
       "HLT_Mu10_Ele10_CaloIdL_v2",
       "HLT_Mu12_v1",
       "HLT_Mu15_DoublePhoton15_CaloIdL_v2",
       "HLT_Mu15_LooseIsoPFTau20_v1",
       "HLT_Mu15_Photon20_CaloIdL_v2",
       "HLT_Mu15_v2",
       "HLT_Mu17_CentralJet30_v1",
       "HLT_Mu17_CentralJet40_BTagIP_v1",
       "HLT_Mu17_DiCentralJet30_v1",
       "HLT_Mu17_Ele8_CaloIdL_v1",
       "HLT_Mu17_TriCentralJet30_v1",
       "HLT_Mu20_v1",
       "HLT_Mu24_v1",
       "HLT_Mu30_v1",
       "HLT_Mu3_Ele8_CaloIdL_TrkIdVL_HT160_v2",
       "HLT_Mu3_Ele8_CaloIdT_TrkIdVL_HT160_v2",
       "HLT_Mu3_Track3_Jpsi_v4",
       "HLT_Mu3_v3",
       "HLT_Mu5_DoubleEle8_v2",
       "HLT_Mu5_Ele8_CaloIdL_TrkIdVL_Ele8_v2",
       "HLT_Mu5_HT200_v3",
       "HLT_Mu5_L2Mu2_Jpsi_v1",
       "HLT_Mu5_L2Mu2_v1",
       "HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1",
       "HLT_Mu5_v3",
       "HLT_Mu7_Track5_Jpsi_v1",
       "HLT_Mu7_Track7_Jpsi_v1",
       "HLT_Mu8_Ele17_CaloIdL_v1",
       "HLT_Mu8_HT200_v2",
       "HLT_Mu8_Jet40_v2",
       "HLT_Mu8_Photon20_CaloIdVT_IsoT_v2",
       "HLT_Mu8_v1",
       "HLT_PFMHT150_v1",
       "HLT_Photon125_NoSpikeFilter_v1",
       "HLT_Photon20_CaloIdVT_IsoT_Ele8_CaloIdL_CaloIsoVL_v1",
       "HLT_Photon20_R9Id_Photon18_R9Id_v1",
       "HLT_Photon26_CaloIdL_IsoVL_Photon18_CaloIdL_IsoVL_v1",
       "HLT_Photon26_CaloIdL_IsoVL_Photon18_v1",
       "HLT_Photon26_IsoVL_Photon18_IsoVL_v1",
       "HLT_Photon26_IsoVL_Photon18_v1",
       "HLT_Photon26_Photon18_v1",
       "HLT_Photon30_CaloIdVL_IsoL_v1",
       "HLT_Photon30_CaloIdVL_v1",
       "HLT_Photon32_CaloIdL_Photon26_CaloIdL_v1",
       "HLT_Photon60_CaloIdL_HT200_v1",
       "HLT_Photon70_CaloIdL_HT200_v1",
       "HLT_Photon70_CaloIdL_HT300_v1",
       "HLT_Photon70_CaloIdL_MHT30_v1",
       "HLT_Photon70_CaloIdL_MHT50_v1",
       "HLT_Photon75_CaloIdVL_IsoL_v1",
       "HLT_Photon75_CaloIdVL_v1",
       "HLT_Physics_v1 / 500",
       "HLT_PixelTracks_Multiplicity110_v1",
       "HLT_PixelTracks_Multiplicity125_v1",
       "HLT_QuadJet40_IsoPFTau40_v1",
       "HLT_QuadJet40_v1",
       "HLT_QuadJet50_BTagIP_v1",
       "HLT_QuadJet50_Jet40_v1",
       "HLT_QuadJet60_v1",
       "HLT_QuadJet70_v1",
       "HLT_R032_MR100_v1",
       "HLT_R032_v1",
       "HLT_R035_MR100_v1",
       "HLT_Random_v1",
       "HLT_RegionalCosmicTracking_v1",
       "HLT_TripleEle10_CaloIdL_TrkIdVL_v1",
       "HLT_TripleMu5_v2",
       "HLT_ZeroBias_v1" ),
    hltResults = cms.InputTag( 'TriggerResults' ),
    l1tResults = cms.InputTag( 'hltGtDigis' ),
    l1tIgnoreMask = cms.bool( False ),
    daqPartitions = cms.uint32( 1 ),
    throw = cms.bool( True ),
    l1techIgnorePrescales = cms.bool( False )
)
process.hltPreHT160 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreHT240 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreHT260 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreHT260MHT60 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreHT300 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreHT300MHT75 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreHT360 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreHT440 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreHT520 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreHcalCalibration = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreHcalNZS = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreHcalPhiSym = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreIsoMu12 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreIsoMu12IsoPFTau10 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreIsoMu15 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreIsoMu17 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreIsoMu17BTagIPCentJet40 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreIsoMu24 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreIsoMu30 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreIsoTrackHB = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreIsoTrackHE = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreJet110 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreJet150 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreJet190 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreJet240 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreJet30 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreJet370 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreJet370NoJetID = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreJet60 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreJet80 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreJetE30NoBPTX = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreJetE30NoBPTX3BXNoHalo = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreJetE30NoBPTXNoHalo = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL1BeamGasBsc = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL1BeamGasHf = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL1BeamHalo = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL1DoubleMu0 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL1Interbunch1 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL1Mu10 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL1Mu20 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL1MuOpenAntiBPTX = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL1PreCollisions = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL1SingleEG5 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL1SingleJet36 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL1SingleMuOpen = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL1SingleMuOpenDT = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL1TechBSChalo = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL1TechBSCminBiasthreshold1 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL2DoubleMu0 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL2DoubleMu35NoVertex = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL2Mu10 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL2Mu20 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL2MuOpenNoVertex = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreL3MuonsCosmicTracking = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreLogMonitor = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMET100 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMET120 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMET200 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMR100 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMeff440 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMeff520 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMeff640 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu10Ele10CaloIdL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu12 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu15 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu15DoublePhoton15CaloIdL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu15IsoPFTau20 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu15Photon20CaloIdL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu17BTagIPCenJet40 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu17Ele8CaloIdL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu17TriCenJet30 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu20 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu24 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu3 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu30 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu3Ele8CaloIdLTrkIdVLHT160 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu3Ele8CaloIdTTrkIdVLHT160 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu3Track3Jpsi = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu5 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu5DoubleEle8 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu5Ele8CaloIdLTrkIdVLEle8 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu5HT200 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu5L2Mu0 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu5L2Mu2Jpsi = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu5TkMu0JpsiTightB5Q7 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu7Track5Jpsi = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu7Track7Jpsi = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu8 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu8Ele17CaloIdL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu8HT200 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu8Jet40 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreMu8Photon20CaloIdVTIsoT = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreNanoDSTOutput = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreOnlineErrorsOutput = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePFMHT150 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton125NoSpikeFilter = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton20CaloIdVTIsoTEle8CaloIdLCaloIsoVL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton20EBOnlyNoSpikeFilter = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton20NoSpikeFilter = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton20R9IdPhoton18R9Id = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton26CaloIdLIsoVLPhoton18 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton26CaloIdLIsoVLPhoton18CaloIdLIsoVL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton26IsoVLPhoton18 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton26IsoVLPhoton18IsoVL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton26Photon18 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton30CaloIdVL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton30CaloIdVLIsoL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton32CaloIdLPhoton26CaloIdL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton60CaloIdLHT200 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton70CaloIdLHT200 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton70CaloIdLHT300 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton70CaloIdLMHT30 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton70CaloIdLMHT50 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton75CaloIdVL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhoton75CaloIdVLIsoL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhysics = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePhysicsNanoDST = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePixelTracksMultiplicity110 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPrePixelTracksMultiplicity125 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreQuadJet40 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreQuadJet40IsoPFTau40 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreQuadJet50 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreQuadJet50Jet40 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreQuadJet60 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreQuadJet70 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreR032 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreR032MR100 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreR035MR100 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreRPCMONOutput = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreRPCMuonNoHits = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreRPCMuonNoTriggers = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreRPCMuonNorma = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreRandom = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreRegionalCosmicTracking = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreSingleIsoTau35Trk20MET45 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreSpike20 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreTechTrigHCALNoise = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreTrackerCalibration = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreTrackerCosmics = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreTripleEle10CaloIdLTrkIdVL = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreTripleMu3 = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltPreZeroBias = cms.HLTFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' )
)
process.hltQuadJet40Central = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 40.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 4 )
)
process.hltQuadJet40IsoPFTau40 = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 40.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 4 )
)
process.hltQuadJet50Central = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 50.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 4 )
)
process.hltQuadJet60 = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 60.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 4 )
)
process.hltQuadJet70 = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 70.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 4 )
)
process.hltR032 = cms.HLTFilter( "HLTRFilter",
    inputTag = cms.InputTag( 'hltRHemisphere' ),
    inputMetTag = cms.InputTag( 'hltMet' ),
    minR = cms.double( 0.32 ),
    minMR = cms.double( 0.0 ),
    doRPrime = cms.bool( False ),
    acceptNJ = cms.bool( True )
)
process.hltR032MR100 = cms.HLTFilter( "HLTRFilter",
    inputTag = cms.InputTag( 'hltRHemisphere' ),
    inputMetTag = cms.InputTag( 'hltMet' ),
    minR = cms.double( 0.32 ),
    minMR = cms.double( 100.0 ),
    doRPrime = cms.bool( False ),
    acceptNJ = cms.bool( True )
)
process.hltR035MR100 = cms.HLTFilter( "HLTRFilter",
    inputTag = cms.InputTag( 'hltRHemisphere' ),
    inputMetTag = cms.InputTag( 'hltMet' ),
    minR = cms.double( 0.35 ),
    minMR = cms.double( 100.0 ),
    doRPrime = cms.bool( False ),
    acceptNJ = cms.bool( True )
)
process.hltRHemisphere = cms.HLTFilter( "HLTRHemisphere",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    minJetPt = cms.double( 56.0 ),
    maxEta = cms.double( 3.0 ),
    maxNJ = cms.int32( 7 ),
    acceptNJ = cms.bool( True )
)
process.hltRPCFEDIntegrity = cms.EDAnalyzer( "RPCFEDIntegrity",
    RPCRawCountsInputTag = cms.untracked.InputTag( 'hltMuonRPCDigis' ),
    RPCPrefixDir = cms.untracked.string( "RPC/FEDIntegrity_EvF" ),
    MergeRuns = cms.untracked.bool( False ),
    MinimumFEDID = cms.untracked.int32( 790 ),
    MaximumFEDID = cms.untracked.int32( 792 )
)
process.hltRPCFilter = cms.HLTFilter( "HLTRPCFilter",
    rangestrips = cms.untracked.double( 1.0 ),
    rpcRecHits = cms.InputTag( 'hltRpcRecHits' ),
    rpcDTPoints = cms.InputTag( 'hltRPCPointProducer', 'RPCDTExtrapolatedPoints' ),
    rpcCSCPoints = cms.InputTag( 'hltRPCPointProducer', 'RPCCSCExtrapolatedPoints' )
)
process.hltRPCMuonNoTriggersL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sAlCaRPC' ),
    MaxEta = cms.double( 1.6 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( True ),
    SelectQualities = cms.vint32( 6 )
)
process.hltRPCMuonNormaL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sAlCaRPC' ),
    MaxEta = cms.double( 1.6 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( True ),
    SelectQualities = cms.vint32(  )
)
process.hltRPCPointProducer = cms.EDProducer( "RPCPointProducer",
    cscSegments = cms.InputTag( 'hltCscSegments' ),
    dt4DSegments = cms.InputTag( 'hltDt4DSegments' ),
    tracks = cms.InputTag( 'NotUsed' ),
    debug = cms.untracked.bool( False ),
    incldt = cms.untracked.bool( True ),
    inclcsc = cms.untracked.bool( True ),
    incltrack = cms.untracked.bool( False ),
    MinCosAng = cms.untracked.double( 0.95 ),
    MaxD = cms.untracked.double( 80.0 ),
    MaxDrb4 = cms.untracked.double( 150.0 ),
    ExtrapolatedRegion = cms.untracked.double( 0.5 ),
    TrackTransformer = cms.PSet(  )
)
process.hltRandomEventsFilter = cms.HLTFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 3 )
)
process.hltRecoEcalSuperClusterActivityCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scHybridBarrelProducer = cms.InputTag( 'hltCorrectedHybridSuperClustersActivity' ),
    scIslandEndcapProducer = cms.InputTag( 'hltCorrectedMulti5x5SuperClustersWithPreshowerActivity' ),
    recoEcalCandidateCollection = cms.string( "" )
)
process.hltRegionalCosmicCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( 'hltRegionalCosmicTrackerSeeds' ),
    TrajectoryBuilder = cms.string( "hltESPCkfTrajectoryBuilder" ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    NavigationSchool = cms.string( "CosmicNavigationSchool" ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    useHitsSplitting = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    maxNSeeds = cms.uint32( 200 )
)
process.hltRegionalCosmicTrackerSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    ClusterCheckPSet = cms.PSet(
      MaxNumberOfPixelClusters = cms.uint32( 300000 ),
      PixelClusterCollectionLabel = cms.InputTag( 'hltSiPixelClusters' ),
      MaxNumberOfCosmicClusters = cms.uint32( 300000 ),
      ClusterCollectionLabel = cms.InputTag( 'hltSiStripClusters' ),
      doClusterCheck = cms.bool( False )
    ),
    RegionFactoryPSet = cms.PSet(
      CollectionsPSet = cms.PSet(
        recoMuonsCollection = cms.InputTag( 'muons' ),
        recoTrackMuonsCollection = cms.InputTag( 'cosmicMuons' ),
        recoL2MuonsCollection = cms.InputTag( 'hltL2MuonCandidatesNoVtx' )
      ),
      ComponentName = cms.string( "CosmicRegionalSeedGenerator" ),
      RegionInJetsCheckPSet = cms.PSet(
        recoCaloJetsCollection = cms.InputTag( 'hltIterativeCone5CaloJets' ),
        deltaRExclusionSize = cms.double( 0.3 ),
        jetsPtMin = cms.double( 5.0 ),
        doJetsExclusionCheck = cms.bool( False )
      ),
      ToolsPSet = cms.PSet(
        regionBase = cms.string( "seedOnL2Muon" ),
        thePropagatorName = cms.string( "hltESPAnalyticalPropagator" )
      ),
      RegionPSet = cms.PSet(
        precise = cms.bool( False ),
        deltaPhiRegion = cms.double( 0.3 ),
        measurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
        zVertex = cms.double( 5.0 ),
        deltaEtaRegion = cms.double( 0.3 ),
        ptMin = cms.double( 5.0 ),
        rVertex = cms.double( 5.0 )
      )
    ),
    OrderedHitsFactoryPSet = cms.PSet(
      ComponentName = cms.string( "GenericPairGenerator" ),
      LayerPSet = cms.PSet(
        TOB = cms.PSet(
          TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
        ),
        layerList = cms.vstring( "TOB6+TOB5",
           "TOB6+TOB4",
           "TOB6+TOB3",
           "TOB5+TOB4",
           "TOB5+TOB3",
           "TOB4+TOB3" )
      )
    ),
    SeedComparitorPSet = cms.PSet(
      ComponentName = cms.string( "none" )
    ),
    SeedCreatorPSet = cms.PSet(
      ComponentName = cms.string( "CosmicSeedCreator" ),
      maxseeds = cms.int32( 100000 ),
      propagator = cms.string( "PropagatorWithMaterial" )
    ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltRegionalCosmicTracks = cms.EDProducer( "TrackProducer",
    TrajectoryInEvent = cms.bool( True ),
    useHitsSplitting = cms.bool( False ),
    clusterRemovalInfo = cms.InputTag( "" ),
    alias = cms.untracked.string( "hltRegionalCosmicTracks" ),
    Fitter = cms.string( "hltESPKFFittingSmoother" ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
    src = cms.InputTag( 'hltRegionalCosmicCkfTrackCandidates' ),
    beamSpot = cms.InputTag( 'hltOnlineBeamSpot' ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    AlgorithmName = cms.string( "undefAlgorithm" ),
    NavigationSchool = cms.string( "" )
)
process.hltRpcRecHits = cms.EDProducer( "RPCRecHitProducer",
    rpcDigiLabel = cms.InputTag( 'hltMuonRPCDigis' ),
    recAlgo = cms.string( "RPCRecHitStandardAlgo" ),
    maskSource = cms.string( "File" ),
    maskvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat" ),
    deadSource = cms.string( "File" ),
    deadvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat" ),
    recAlgoConfig = cms.PSet(  )
)
process.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( 'source' )
)
process.hltSelectedPFTauTightIsoTrackPt20 = cms.EDFilter( "PFTauSelector",
    src = cms.InputTag( 'hltPFTausTightIso' ),
    discriminators = cms.VPSet(
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauTightIsoTrackPt20Discriminator' ),
        selectionCut = cms.double( 0.5 )
      )
    )
)
process.hltSelectedPFTauTightIsoTrackPt20Isolation = cms.EDFilter( "PFTauSelector",
    src = cms.InputTag( 'hltPFTausTightIso' ),
    discriminators = cms.VPSet(
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauTightIsoTrackPt20Discriminator' ),
        selectionCut = cms.double( 0.5 )
      ),
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauTightIsoIsolationDiscriminator' ),
        selectionCut = cms.double( 0.5 )
      )
    )
)
process.hltSelectedPFTausTightIsoTrackFinding = cms.EDFilter( "PFTauSelector",
    src = cms.InputTag( 'hltPFTausTightIso' ),
    discriminators = cms.VPSet(
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauTightIsoTrackFindingDiscriminator' ),
        selectionCut = cms.double( 0.5 )
      )
    )
)
process.hltSelectedPFTausTightIsoTrackFindingIsolation = cms.EDFilter( "PFTauSelector",
    src = cms.InputTag( 'hltPFTausTightIso' ),
    discriminators = cms.VPSet(
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauTightIsoTrackFindingDiscriminator' ),
        selectionCut = cms.double( 0.5 )
      ),
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauTightIsoIsolationDiscriminator' ),
        selectionCut = cms.double( 0.5 )
      )
    )
)
process.hltSelectedPFTausTightIsoTrackPt5 = cms.EDFilter( "PFTauSelector",
    src = cms.InputTag( 'hltPFTausTightIso' ),
    discriminators = cms.VPSet(
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauTightIsoTrackPt5Discriminator' ),
        selectionCut = cms.double( 0.5 )
      )
    )
)
process.hltSelectedPFTausTightIsoTrackPt5Isolation = cms.EDFilter( "PFTauSelector",
    src = cms.InputTag( 'hltPFTausTightIso' ),
    discriminators = cms.VPSet(
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauTightIsoTrackPt5Discriminator' ),
        selectionCut = cms.double( 0.5 )
      ),
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauTightIsoIsolationDiscriminator' ),
        selectionCut = cms.double( 0.5 )
      )
    )
)
process.hltSelectedPFTausTrackFinding = cms.EDFilter( "PFTauSelector",
    src = cms.InputTag( 'hltPFTaus' ),
    discriminators = cms.VPSet(
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauTrackFindingDiscriminator' ),
        selectionCut = cms.double( 0.5 )
      )
    )
)
process.hltSelectedPFTausTrackFindingIsolation = cms.EDFilter( "PFTauSelector",
    src = cms.InputTag( 'hltPFTaus' ),
    discriminators = cms.VPSet(
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauTrackFindingDiscriminator' ),
        selectionCut = cms.double( 0.5 )
      ),
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauIsolationDiscriminator' ),
        selectionCut = cms.double( 0.5 )
      )
    )
)
process.hltSelectedPFTausTrackFindingLooseIsolation = cms.EDFilter( "PFTauSelector",
    src = cms.InputTag( 'hltPFTaus' ),
    discriminators = cms.VPSet(
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauTrackFindingDiscriminator' ),
        selectionCut = cms.double( 0.5 )
      ),
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauLooseIsolationDiscriminator' ),
        selectionCut = cms.double( 0.5 )
      )
    )
)
process.hltSelectedPFTausTrackPt5 = cms.EDFilter( "PFTauSelector",
    src = cms.InputTag( 'hltPFTaus' ),
    discriminators = cms.VPSet(
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauTrackPt5Discriminator' ),
        selectionCut = cms.double( 0.5 )
      )
    )
)
process.hltSelectedPFTausTrackPt5Isolation = cms.EDFilter( "PFTauSelector",
    src = cms.InputTag( 'hltPFTaus' ),
    discriminators = cms.VPSet(
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauTrackPt5Discriminator' ),
        selectionCut = cms.double( 0.5 )
      ),
      cms.PSet(
        discriminator = cms.InputTag( 'hltPFTauIsolationDiscriminator' ),
        selectionCut = cms.double( 0.5 )
      )
    )
)
process.hltSelector4Jets = cms.EDFilter( "LargestEtCaloJetSelector",
    src = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    filter = cms.bool( False ),
    maxNumber = cms.uint32( 4 )
)
process.hltSelectorEleJetsSingleTop = cms.EDFilter( "LargestEtCaloJetSelector",
    src = cms.InputTag( 'hltGetJetsfrom1EleCleanBJet40Central' ),
    filter = cms.bool( False ),
    maxNumber = cms.uint32( 4 )
)
process.hltSelectorJetsSingleTop = cms.EDFilter( "LargestEtCaloJetSelector",
    src = cms.InputTag( 'hltGetJetsfromBJet40Central' ),
    filter = cms.bool( False ),
    maxNumber = cms.uint32( 4 )
)
process.hltSiPixelClusters = cms.EDProducer( "SiPixelClusterProducer",
    src = cms.InputTag( 'hltSiPixelDigis' ),
    maxNumberOfClusters = cms.int32( 10000 ),
    payloadType = cms.string( "HLT" ),
    ClusterMode = cms.untracked.string( "PixelThresholdClusterizer" ),
    ChannelThreshold = cms.int32( 1000 ),
    SeedThreshold = cms.int32( 1000 ),
    ClusterThreshold = cms.double( 4000.0 ),
    VCaltoElectronGain = cms.int32( 65 ),
    VCaltoElectronOffset = cms.int32( -414 ),
    MissCalibrate = cms.untracked.bool( True ),
    SplitClusters = cms.bool( False )
)
process.hltSiPixelDigis = cms.EDProducer( "SiPixelRawToDigi",
    IncludeErrors = cms.bool( False ),
    UseQualityInfo = cms.bool( False ),
    UseCablingTree = cms.untracked.bool( True ),
    Timing = cms.untracked.bool( False ),
    InputLabel = cms.InputTag( 'source' )
)
process.hltSiPixelHLTSource = cms.EDAnalyzer( "SiPixelHLTSource",
    RawInput = cms.InputTag( 'source' ),
    ErrorInput = cms.InputTag( 'hltSiPixelDigis' ),
    saveFile = cms.untracked.bool( False ),
    slowDown = cms.untracked.bool( False ),
    DirName = cms.untracked.string( "Pixel/FEDIntegrity_EvF" ),
    outputFile = cms.string( "Pixel_DQM_HLT.root" )
)
process.hltSiPixelRecHits = cms.EDProducer( "SiPixelRecHitConverter",
    src = cms.InputTag( 'hltSiPixelClusters' ),
    VerboseLevel = cms.untracked.int32( 0 ),
    CPE = cms.string( "hltESPPixelCPEGeneric" )
)
process.hltSiStripClusters = cms.EDProducer( "MeasurementTrackerSiStripRefGetterProducer",
    InputModuleLabel = cms.InputTag( 'hltSiStripRawToClustersFacility' ),
    measurementTrackerName = cms.string( "hltESPMeasurementTracker" )
)
process.hltSiStripFEDCheck = cms.EDAnalyzer( "SiStripFEDCheckPlugin",
    RawDataTag = cms.InputTag( 'source' ),
    DirName = cms.untracked.string( "SiStrip/FEDIntegrity_EvF" ),
    PrintDebugMessages = cms.untracked.bool( False ),
    WriteDQMStore = cms.untracked.bool( False ),
    HistogramUpdateFrequency = cms.untracked.uint32( 1000 ),
    DoPayloadChecks = cms.untracked.bool( False ),
    CheckChannelLengths = cms.untracked.bool( False ),
    CheckChannelPacketCodes = cms.untracked.bool( False ),
    CheckFELengths = cms.untracked.bool( False ),
    CheckChannelStatus = cms.untracked.bool( False )
)
process.hltSiStripRawToClustersFacility = cms.EDProducer( "SiStripRawToClusters",
    ProductLabel = cms.InputTag( 'source' ),
    Clusterizer = cms.PSet(
      ChannelThreshold = cms.double( 2.0 ),
      MaxSequentialBad = cms.uint32( 1 ),
      MaxSequentialHoles = cms.uint32( 0 ),
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      MaxAdjacentBad = cms.uint32( 0 ),
      QualityLabel = cms.string( "" ),
      SeedThreshold = cms.double( 3.0 ),
      ClusterThreshold = cms.double( 5.0 )
    ),
    Algorithms = cms.PSet(
      SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
      CommonModeNoiseSubtractionMode = cms.string( "Median" ),
      PedestalSubtractionFedMode = cms.bool( True ),
      TruncateInSuppressor = cms.bool( True )
    )
)
process.hltSimple3x3Clusters = cms.EDProducer( "EgammaHLTNxNClusterProducer",
    doBarrel = cms.bool( True ),
    doEndcaps = cms.bool( True ),
    barrelHitProducer = cms.InputTag( 'hltEcalRegionalPi0EtaRecHit', 'EcalRecHitsEB' ),
    endcapHitProducer = cms.InputTag( 'hltEcalRegionalPi0EtaRecHit', 'EcalRecHitsEE' ),
    clusEtaSize = cms.int32( 3 ),
    clusPhiSize = cms.int32( 3 ),
    barrelClusterCollection = cms.string( "Simple3x3ClustersBarrel" ),
    endcapClusterCollection = cms.string( "Simple3x3ClustersEndcap" ),
    clusSeedThr = cms.double( 0.5 ),
    clusSeedThrEndCap = cms.double( 1.0 ),
    useRecoFlag = cms.bool( False ),
    flagLevelRecHitsToUse = cms.int32( 1 ),
    useDBStatus = cms.bool( True ),
    statusLevelRecHitsToUse = cms.int32( 1 ),
    maxNumberofSeeds = cms.int32( 200 ),
    maxNumberofClusters = cms.int32( 30 ),
    debugLevel = cms.int32( 0 ),
    posCalcParameters = cms.PSet(
      T0_barl = cms.double( 7.4 ),
      LogWeighted = cms.bool( True ),
      T0_endc = cms.double( 3.1 ),
      T0_endcPresh = cms.double( 1.2 ),
      W0 = cms.double( 4.2 ),
      X0 = cms.double( 0.89 )
    )
)
process.hltSingleEleCleanBJet40Central = cms.HLTFilter( "HLT1CaloBJet",
    inputTag = cms.InputTag( 'hltCleanEle25CaloIdVTTrkIdTFromAK5CorrJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 40.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 1 )
)
process.hltSingleJet110Regional = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltJetIDPassedJetsRegional' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 110.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
process.hltSingleJet150Regional = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltJetIDPassedJetsRegional' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 150.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
process.hltSingleJet190Regional = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltJetIDPassedJetsRegional' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 190.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
process.hltSingleJet240Regional = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltJetIDPassedJetsRegional' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 240.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
process.hltSingleJet30 = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltJetIDPassedCorrJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 30.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
process.hltSingleJet370Regional = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltJetIDPassedJetsRegional' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 370.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
process.hltSingleJet370RegionalNoJetID = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltL1MatchedJetsRegional' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 370.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
process.hltSingleJet60Regional = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltJetIDPassedJetsRegional' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 60.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
process.hltSingleJet80Regional = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltJetIDPassedJetsRegional' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 80.0 ),
    MaxEta = cms.double( 5.0 ),
    MinN = cms.int32( 1 )
)
process.hltSingleL2MuORL2PreFilteredNoVtx = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidatesNoVtx' ),
    PreviousCandTag = cms.InputTag( 'hltL1MuORL1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 0.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltSingleL2MuOpenL2PreFilteredNoVtx = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidatesNoVtx' ),
    PreviousCandTag = cms.InputTag( 'hltSingleMuOpenL1Filtered' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 0.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu12L2Filtered12 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1SingleMu12L1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 12.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( False )
)
process.hltSingleMu12L3Filtered12 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL2Mu7L2Filtered7' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 12.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu20L3Filtered20 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltSingleMu12L2Filtered12' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 20.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu24L3Filtered24 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL2Mu12L2Filtered12' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 24.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu30L3Filtered30 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL2Mu12L2Filtered12' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 30.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu3L2Filtered0 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltSingleMuOpenL1Filtered' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 0.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu3L3Filtered3 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltSingleMu3L2Filtered0' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu5EG5L2Filtered3 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1SingleMu3EG5L1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( False )
)
process.hltSingleMu5L2Filtered3 = cms.HLTFilter( "HLTMuonL2PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL1SingleMu3L1Filtered0' ),
    SeedMapTag = cms.InputTag( 'hltL2Muons' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 9999.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 3.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( False )
)
process.hltSingleMu5L3Filtered5 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltSingleMu5L2Filtered3' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 5.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu8EG5L3Filtered8 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltSingleMu5EG5L2Filtered3' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 8.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu8L3Filtered8 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL2Mu3L2Filtered3' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 8.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( True )
)
process.hltSingleMuIsoL2IsoFiltered10 = cms.HLTFilter( "HLTMuonIsoFilter",
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL2Mu10L2Filtered10' ),
    MinN = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    DepTag = cms.VInputTag( 'hltL2MuonIsolations' ),
    IsolatorPSet = cms.PSet(
      ComponentName = cms.string( "" )
    )
)
process.hltSingleMuIsoL2IsoFiltered12 = cms.HLTFilter( "HLTMuonIsoFilter",
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL2Mu12L2Filtered12' ),
    MinN = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    DepTag = cms.VInputTag( 'hltL2MuonIsolations' ),
    IsolatorPSet = cms.PSet(
      ComponentName = cms.string( "" )
    )
)
process.hltSingleMuIsoL2IsoFiltered7 = cms.HLTFilter( "HLTMuonIsoFilter",
    CandTag = cms.InputTag( 'hltL2MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltL2Mu7L2Filtered7' ),
    MinN = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( False ),
    DepTag = cms.VInputTag( 'hltL2MuonIsolations' ),
    IsolatorPSet = cms.PSet(
      ComponentName = cms.string( "" )
    )
)
process.hltSingleMuIsoL3IsoFiltered12 = cms.HLTFilter( "HLTMuonIsoFilter",
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltSingleMuIsoL3PreFiltered12' ),
    MinN = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( True ),
    DepTag = cms.VInputTag( 'hltL3MuonIsolations' ),
    IsolatorPSet = cms.PSet(
      ComponentName = cms.string( "" )
    )
)
process.hltSingleMuIsoL3IsoFiltered15 = cms.HLTFilter( "HLTMuonIsoFilter",
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltSingleMuIsoL3PreFiltered15' ),
    MinN = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( True ),
    DepTag = cms.VInputTag( 'hltL3MuonIsolations' ),
    IsolatorPSet = cms.PSet(
      ComponentName = cms.string( "" )
    )
)
process.hltSingleMuIsoL3IsoFiltered17 = cms.HLTFilter( "HLTMuonIsoFilter",
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltSingleMuIsoL3PreFiltered17' ),
    MinN = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( True ),
    DepTag = cms.VInputTag( 'hltL3MuonIsolations' ),
    IsolatorPSet = cms.PSet(
      ComponentName = cms.string( "" )
    )
)
process.hltSingleMuIsoL3IsoFiltered24 = cms.HLTFilter( "HLTMuonIsoFilter",
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltSingleMuIsoL3PreFiltered24' ),
    MinN = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( True ),
    DepTag = cms.VInputTag( 'hltL3MuonIsolations' ),
    IsolatorPSet = cms.PSet(
      ComponentName = cms.string( "" )
    )
)
process.hltSingleMuIsoL3IsoFiltered30 = cms.HLTFilter( "HLTMuonIsoFilter",
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltSingleMuIsoL3PreFiltered30' ),
    MinN = cms.int32( 1 ),
    SaveTag = cms.untracked.bool( True ),
    DepTag = cms.VInputTag( 'hltL3MuonIsolations' ),
    IsolatorPSet = cms.PSet(
      ComponentName = cms.string( "" )
    )
)
process.hltSingleMuIsoL3PreFiltered12 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltSingleMuIsoL2IsoFiltered7' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 12.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( False )
)
process.hltSingleMuIsoL3PreFiltered15 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltSingleMuIsoL2IsoFiltered10' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 15.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( False )
)
process.hltSingleMuIsoL3PreFiltered17 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltSingleMuIsoL2IsoFiltered10' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 17.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( False )
)
process.hltSingleMuIsoL3PreFiltered24 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltSingleMuIsoL2IsoFiltered12' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 24.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( False )
)
process.hltSingleMuIsoL3PreFiltered30 = cms.HLTFilter( "HLTMuonL3PreFilter",
    BeamSpotTag = cms.InputTag( 'hltOnlineBeamSpot' ),
    CandTag = cms.InputTag( 'hltL3MuonCandidates' ),
    PreviousCandTag = cms.InputTag( 'hltSingleMuIsoL2IsoFiltered12' ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinNhits = cms.int32( 0 ),
    MaxDr = cms.double( 2.0 ),
    MaxDz = cms.double( 9999.0 ),
    MinPt = cms.double( 30.0 ),
    NSigmaPt = cms.double( 0.0 ),
    SaveTag = cms.untracked.bool( False )
)
process.hltSingleMuOpenL1Filtered = cms.HLTFilter( "HLTMuonL1Filter",
    CandTag = cms.InputTag( 'hltL1extraParticles' ),
    PreviousCandTag = cms.InputTag( 'hltL1sL1SingleMuOpen' ),
    MaxEta = cms.double( 2.5 ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    ExcludeSingleSegmentCSC = cms.bool( False ),
    CSCTFtag = cms.InputTag( 'unused' ),
    SaveTag = cms.untracked.bool( False ),
    SelectQualities = cms.vint32(  )
)
process.hltSpike20HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
    candTag = cms.InputTag( 'hltEG20R9ShapeAntiFilter' ),
    isoTag = cms.InputTag( 'hltL1IsolatedPhotonHcalForHE' ),
    nonIsoTag = cms.InputTag( 'hltL1NonIsolatedPhotonHcalForHE' ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    thrRegularEB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    thrOverEEB = cms.double( 0.15 ),
    thrOverEEE = cms.double( 0.1 ),
    thrOverE2EB = cms.double( -1.0 ),
    thrOverE2EE = cms.double( -1.0 ),
    ncandcut = cms.int32( 1 ),
    doIsolated = cms.bool( False ),
    SaveTag = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltStoppedHSCPControl1CaloJetEnergy30 = cms.HLTFilter( "HLT1CaloJetEnergy",
    inputTag = cms.InputTag( 'hltStoppedHSCPIterativeCone5CaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinE = cms.double( 30.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 1 )
)
process.hltStoppedHSCPIterativeCone5CaloJets = cms.EDProducer( "FastjetJetProducer",
    UseOnlyVertexTracks = cms.bool( False ),
    UseOnlyOnePV = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    DxyTrVtxMax = cms.double( 0.0 ),
    MinVtxNdof = cms.int32( 5 ),
    MaxVtxZ = cms.double( 15.0 ),
    jetAlgorithm = cms.string( "IterativeCone" ),
    rParam = cms.double( 0.5 ),
    src = cms.InputTag( 'hltStoppedHSCPTowerMakerForAll' ),
    srcPVs = cms.InputTag( 'offlinePrimaryVertices' ),
    jetType = cms.string( "CaloJet" ),
    jetPtMin = cms.double( 1.0 ),
    inputEtMin = cms.double( 0.3 ),
    inputEMin = cms.double( 0.0 ),
    doPVCorrection = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    nSigmaPU = cms.double( 1.0 ),
    radiusPU = cms.double( 0.5 ),
    Active_Area_Repeats = cms.int32( 5 ),
    GhostArea = cms.double( 0.01 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    doAreaFastjet = cms.bool( False ),
    doRhoFastjet = cms.bool( False ),
    subtractorName = cms.string( "" ),
    sumRecHits = cms.bool( False )
)
process.hltStoppedHSCPLoose1CaloJetEnergy30 = cms.HLTFilter( "HLT1CaloJetEnergy",
    inputTag = cms.InputTag( 'hltStoppedHSCPIterativeCone5CaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinE = cms.double( 30.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 1 )
)
process.hltStoppedHSCPTight1CaloJetEnergy30 = cms.HLTFilter( "HLT1CaloJetEnergy",
    inputTag = cms.InputTag( 'hltStoppedHSCPIterativeCone5CaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinE = cms.double( 30.0 ),
    MaxEta = cms.double( 3.0 ),
    MinN = cms.int32( 1 )
)
process.hltStoppedHSCPTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
    EBThreshold = cms.double( 0.07 ),
    EEThreshold = cms.double( 0.3 ),
    UseEtEBTreshold = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    UseSymEBTreshold = cms.bool( False ),
    UseSymEETreshold = cms.bool( False ),
    HcalThreshold = cms.double( -1000.0 ),
    HBThreshold = cms.double( 0.7 ),
    HESThreshold = cms.double( 0.8 ),
    HEDThreshold = cms.double( 0.8 ),
    HOThreshold0 = cms.double( 3.5 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HF1Threshold = cms.double( 0.5 ),
    HF2Threshold = cms.double( 0.85 ),
    EBWeight = cms.double( 1.0 ),
    EEWeight = cms.double( 1.0 ),
    HBWeight = cms.double( 1.0 ),
    HESWeight = cms.double( 1.0 ),
    HEDWeight = cms.double( 1.0 ),
    HOWeight = cms.double( 1e-99 ),
    HF1Weight = cms.double( 1.0 ),
    HF2Weight = cms.double( 1.0 ),
    EcutTower = cms.double( -1000.0 ),
    EBSumThreshold = cms.double( 0.2 ),
    EESumThreshold = cms.double( 0.45 ),
    UseHO = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHBDepth = cms.double( 0.2 ),
    MomHEDepth = cms.double( 0.4 ),
    MomEBDepth = cms.double( 0.3 ),
    MomEEDepth = cms.double( 0.0 ),
    hbheInput = cms.InputTag( 'hltHbhereco' ),
    hoInput = cms.InputTag( "" ),
    hfInput = cms.InputTag( "" ),
    AllowMissingInputs = cms.bool( True ),
    HcalAcceptSeverityLevel = cms.uint32( 11 ),
    EcalAcceptSeverityLevel = cms.uint32( 3 ),
    UseHcalRecoveredHits = cms.bool( False ),
    UseEcalRecoveredHits = cms.bool( False ),
    UseRejectedHitsOnly = cms.bool( False ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    EcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    EBGrid = cms.vdouble(    ),
    EBWeights = cms.vdouble(    ),
    EEGrid = cms.vdouble(    ),
    EEWeights = cms.vdouble(    ),
    HBGrid = cms.vdouble(    ),
    HBWeights = cms.vdouble(    ),
    HESGrid = cms.vdouble(    ),
    HESWeights = cms.vdouble(    ),
    HEDGrid = cms.vdouble(    ),
    HEDWeights = cms.vdouble(    ),
    HOGrid = cms.vdouble(    ),
    HOWeights = cms.vdouble(    ),
    HF1Grid = cms.vdouble(    ),
    HF1Weights = cms.vdouble(    ),
    HF2Grid = cms.vdouble(    ),
    HF2Weights = cms.vdouble(    ),
    ecalInputs = cms.VInputTag(  )
)
process.hltTauJet5 = cms.HLTFilter( "HLT1Tau",
    inputTag = cms.InputTag( 'hltAntiKT5CaloJetsEt5' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 5.0 ),
    MaxEta = cms.double( 2.5 ),
    MinN = cms.int32( 1 )
)
process.hltTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
    EBThreshold = cms.double( 0.07 ),
    EEThreshold = cms.double( 0.3 ),
    UseEtEBTreshold = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    UseSymEBTreshold = cms.bool( False ),
    UseSymEETreshold = cms.bool( False ),
    HcalThreshold = cms.double( -1000.0 ),
    HBThreshold = cms.double( 0.7 ),
    HESThreshold = cms.double( 0.8 ),
    HEDThreshold = cms.double( 0.8 ),
    HOThreshold0 = cms.double( 3.5 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HF1Threshold = cms.double( 0.5 ),
    HF2Threshold = cms.double( 0.85 ),
    EBWeight = cms.double( 1.0 ),
    EEWeight = cms.double( 1.0 ),
    HBWeight = cms.double( 1.0 ),
    HESWeight = cms.double( 1.0 ),
    HEDWeight = cms.double( 1.0 ),
    HOWeight = cms.double( 1e-99 ),
    HF1Weight = cms.double( 1.0 ),
    HF2Weight = cms.double( 1.0 ),
    EcutTower = cms.double( -1000.0 ),
    EBSumThreshold = cms.double( 0.2 ),
    EESumThreshold = cms.double( 0.45 ),
    UseHO = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHBDepth = cms.double( 0.2 ),
    MomHEDepth = cms.double( 0.4 ),
    MomEBDepth = cms.double( 0.3 ),
    MomEEDepth = cms.double( 0.0 ),
    hbheInput = cms.InputTag( 'hltHbhereco' ),
    hoInput = cms.InputTag( 'hltHoreco' ),
    hfInput = cms.InputTag( 'hltHfreco' ),
    AllowMissingInputs = cms.bool( False ),
    HcalAcceptSeverityLevel = cms.uint32( 11 ),
    EcalAcceptSeverityLevel = cms.uint32( 3 ),
    UseHcalRecoveredHits = cms.bool( False ),
    UseEcalRecoveredHits = cms.bool( False ),
    UseRejectedHitsOnly = cms.bool( False ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    EcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    EBGrid = cms.vdouble(    ),
    EBWeights = cms.vdouble(    ),
    EEGrid = cms.vdouble(    ),
    EEWeights = cms.vdouble(    ),
    HBGrid = cms.vdouble(    ),
    HBWeights = cms.vdouble(    ),
    HESGrid = cms.vdouble(    ),
    HESWeights = cms.vdouble(    ),
    HEDGrid = cms.vdouble(    ),
    HEDWeights = cms.vdouble(    ),
    HOGrid = cms.vdouble(    ),
    HOWeights = cms.vdouble(    ),
    HF1Grid = cms.vdouble(    ),
    HF1Weights = cms.vdouble(    ),
    HF2Grid = cms.vdouble(    ),
    HF2Weights = cms.vdouble(    ),
    ecalInputs = cms.VInputTag( 'hltEcalRecHitAll:EcalRecHitsEB, hltEcalRecHitAll:EcalRecHitsEE' )
)
process.hltTowerMakerForHcal = cms.EDProducer( "CaloTowersCreator",
    EBThreshold = cms.double( 0.07 ),
    EEThreshold = cms.double( 0.3 ),
    UseEtEBTreshold = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    UseSymEBTreshold = cms.bool( False ),
    UseSymEETreshold = cms.bool( False ),
    HcalThreshold = cms.double( -1000.0 ),
    HBThreshold = cms.double( 0.7 ),
    HESThreshold = cms.double( 0.8 ),
    HEDThreshold = cms.double( 0.8 ),
    HOThreshold0 = cms.double( 3.5 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HF1Threshold = cms.double( 0.5 ),
    HF2Threshold = cms.double( 0.85 ),
    EBWeight = cms.double( 1e-99 ),
    EEWeight = cms.double( 1e-99 ),
    HBWeight = cms.double( 1.0 ),
    HESWeight = cms.double( 1.0 ),
    HEDWeight = cms.double( 1.0 ),
    HOWeight = cms.double( 1e-99 ),
    HF1Weight = cms.double( 1.0 ),
    HF2Weight = cms.double( 1.0 ),
    EcutTower = cms.double( -1000.0 ),
    EBSumThreshold = cms.double( 0.2 ),
    EESumThreshold = cms.double( 0.45 ),
    UseHO = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHBDepth = cms.double( 0.2 ),
    MomHEDepth = cms.double( 0.4 ),
    MomEBDepth = cms.double( 0.3 ),
    MomEEDepth = cms.double( 0.0 ),
    hbheInput = cms.InputTag( 'hltHbhereco' ),
    hoInput = cms.InputTag( 'hltHoreco' ),
    hfInput = cms.InputTag( 'hltHfreco' ),
    AllowMissingInputs = cms.bool( True ),
    HcalAcceptSeverityLevel = cms.uint32( 11 ),
    EcalAcceptSeverityLevel = cms.uint32( 3 ),
    UseHcalRecoveredHits = cms.bool( False ),
    UseEcalRecoveredHits = cms.bool( False ),
    UseRejectedHitsOnly = cms.bool( False ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    EcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    EBGrid = cms.vdouble(    ),
    EBWeights = cms.vdouble(    ),
    EEGrid = cms.vdouble(    ),
    EEWeights = cms.vdouble(    ),
    HBGrid = cms.vdouble(    ),
    HBWeights = cms.vdouble(    ),
    HESGrid = cms.vdouble(    ),
    HESWeights = cms.vdouble(    ),
    HEDGrid = cms.vdouble(    ),
    HEDWeights = cms.vdouble(    ),
    HOGrid = cms.vdouble(    ),
    HOWeights = cms.vdouble(    ),
    HF1Grid = cms.vdouble(    ),
    HF1Weights = cms.vdouble(    ),
    HF2Grid = cms.vdouble(    ),
    HF2Weights = cms.vdouble(    ),
    ecalInputs = cms.VInputTag(  )
)
process.hltTowerMakerForJets = cms.EDProducer( "CaloTowersCreator",
    EBThreshold = cms.double( 0.07 ),
    EEThreshold = cms.double( 0.3 ),
    UseEtEBTreshold = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    UseSymEBTreshold = cms.bool( False ),
    UseSymEETreshold = cms.bool( False ),
    HcalThreshold = cms.double( -1000.0 ),
    HBThreshold = cms.double( 0.7 ),
    HESThreshold = cms.double( 0.8 ),
    HEDThreshold = cms.double( 0.8 ),
    HOThreshold0 = cms.double( 3.5 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HF1Threshold = cms.double( 0.5 ),
    HF2Threshold = cms.double( 0.85 ),
    EBWeight = cms.double( 1.0 ),
    EEWeight = cms.double( 1.0 ),
    HBWeight = cms.double( 1.0 ),
    HESWeight = cms.double( 1.0 ),
    HEDWeight = cms.double( 1.0 ),
    HOWeight = cms.double( 1e-99 ),
    HF1Weight = cms.double( 1.0 ),
    HF2Weight = cms.double( 1.0 ),
    EcutTower = cms.double( -1000.0 ),
    EBSumThreshold = cms.double( 0.2 ),
    EESumThreshold = cms.double( 0.45 ),
    UseHO = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHBDepth = cms.double( 0.2 ),
    MomHEDepth = cms.double( 0.4 ),
    MomEBDepth = cms.double( 0.3 ),
    MomEEDepth = cms.double( 0.0 ),
    hbheInput = cms.InputTag( 'hltHbhereco' ),
    hoInput = cms.InputTag( 'hltHoreco' ),
    hfInput = cms.InputTag( 'hltHfreco' ),
    AllowMissingInputs = cms.bool( False ),
    HcalAcceptSeverityLevel = cms.uint32( 11 ),
    EcalAcceptSeverityLevel = cms.uint32( 3 ),
    UseHcalRecoveredHits = cms.bool( False ),
    UseEcalRecoveredHits = cms.bool( False ),
    UseRejectedHitsOnly = cms.bool( False ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    EcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    EBGrid = cms.vdouble(    ),
    EBWeights = cms.vdouble(    ),
    EEGrid = cms.vdouble(    ),
    EEWeights = cms.vdouble(    ),
    HBGrid = cms.vdouble(    ),
    HBWeights = cms.vdouble(    ),
    HESGrid = cms.vdouble(    ),
    HESWeights = cms.vdouble(    ),
    HEDGrid = cms.vdouble(    ),
    HEDWeights = cms.vdouble(    ),
    HOGrid = cms.vdouble(    ),
    HOWeights = cms.vdouble(    ),
    HF1Grid = cms.vdouble(    ),
    HF1Weights = cms.vdouble(    ),
    HF2Grid = cms.vdouble(    ),
    HF2Weights = cms.vdouble(    ),
    ecalInputs = cms.VInputTag( 'hltEcalRegionalJetsRecHit:EcalRecHitsEB, hltEcalRegionalJetsRecHit:EcalRecHitsEE' )
)
process.hltTowerMakerForMuons = cms.EDProducer( "CaloTowersCreator",
    EBThreshold = cms.double( 0.07 ),
    EEThreshold = cms.double( 0.3 ),
    UseEtEBTreshold = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    UseSymEBTreshold = cms.bool( False ),
    UseSymEETreshold = cms.bool( False ),
    HcalThreshold = cms.double( -1000.0 ),
    HBThreshold = cms.double( 0.7 ),
    HESThreshold = cms.double( 0.8 ),
    HEDThreshold = cms.double( 0.8 ),
    HOThreshold0 = cms.double( 3.5 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HF1Threshold = cms.double( 0.5 ),
    HF2Threshold = cms.double( 0.85 ),
    EBWeight = cms.double( 1.0 ),
    EEWeight = cms.double( 1.0 ),
    HBWeight = cms.double( 1.0 ),
    HESWeight = cms.double( 1.0 ),
    HEDWeight = cms.double( 1.0 ),
    HOWeight = cms.double( 1e-99 ),
    HF1Weight = cms.double( 1.0 ),
    HF2Weight = cms.double( 1.0 ),
    EcutTower = cms.double( -1000.0 ),
    EBSumThreshold = cms.double( 0.2 ),
    EESumThreshold = cms.double( 0.45 ),
    UseHO = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHBDepth = cms.double( 0.2 ),
    MomHEDepth = cms.double( 0.4 ),
    MomEBDepth = cms.double( 0.3 ),
    MomEEDepth = cms.double( 0.0 ),
    hbheInput = cms.InputTag( 'hltHbhereco' ),
    hoInput = cms.InputTag( 'hltHoreco' ),
    hfInput = cms.InputTag( 'hltHfreco' ),
    AllowMissingInputs = cms.bool( False ),
    HcalAcceptSeverityLevel = cms.uint32( 11 ),
    EcalAcceptSeverityLevel = cms.uint32( 3 ),
    UseHcalRecoveredHits = cms.bool( False ),
    UseEcalRecoveredHits = cms.bool( False ),
    UseRejectedHitsOnly = cms.bool( False ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    EcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    EBGrid = cms.vdouble(    ),
    EBWeights = cms.vdouble(    ),
    EEGrid = cms.vdouble(    ),
    EEWeights = cms.vdouble(    ),
    HBGrid = cms.vdouble(    ),
    HBWeights = cms.vdouble(    ),
    HESGrid = cms.vdouble(    ),
    HESWeights = cms.vdouble(    ),
    HEDGrid = cms.vdouble(    ),
    HEDWeights = cms.vdouble(    ),
    HOGrid = cms.vdouble(    ),
    HOWeights = cms.vdouble(    ),
    HF1Grid = cms.vdouble(    ),
    HF1Weights = cms.vdouble(    ),
    HF2Grid = cms.vdouble(    ),
    HF2Weights = cms.vdouble(    ),
    ecalInputs = cms.VInputTag( 'hltEcalRegionalMuonsRecHit:EcalRecHitsEB, hltEcalRegionalMuonsRecHit:EcalRecHitsEE' )
)
process.hltTrackMultiplicity110 = cms.HLTFilter( "HLTSingleVertexPixelTrackFilter",
    vertexCollection = cms.InputTag( 'hltPixelVerticesForHighMult' ),
    trackCollection = cms.InputTag( 'hltPixelCandsForHighMult' ),
    MinPt = cms.double( 0.6 ),
    MaxPt = cms.double( 10000.0 ),
    MaxEta = cms.double( 2.4 ),
    MaxVz = cms.double( 10.0 ),
    MinTrks = cms.int32( 110 ),
    MinSep = cms.double( 0.05 )
)
process.hltTrackMultiplicity125 = cms.HLTFilter( "HLTSingleVertexPixelTrackFilter",
    vertexCollection = cms.InputTag( 'hltPixelVerticesForHighMult' ),
    trackCollection = cms.InputTag( 'hltPixelCandsForHighMult' ),
    MinPt = cms.double( 0.6 ),
    MaxPt = cms.double( 10000.0 ),
    MaxEta = cms.double( 2.4 ),
    MaxVz = cms.double( 10.0 ),
    MinTrks = cms.int32( 125 ),
    MinSep = cms.double( 0.05 )
)
process.hltTrackerCosmicsPattern = cms.HLTFilter( "HLTLevel1Pattern",
    L1GtReadoutRecordTag = cms.InputTag( 'hltGtDigis' ),
    triggerBit = cms.string( "L1Tech_RPC_TTU_pointing_Cosmics.v0" ),
    daqPartitions = cms.uint32( 1 ),
    ignoreL1Mask = cms.bool( False ),
    invert = cms.bool( False ),
    throw = cms.bool( True ),
    bunchCrossings = cms.vint32( -2, -1, 0, 1, 2 ),
    triggerPattern = cms.vint32( 1, 1, 1, 0, 0 )
)
process.hltTriJet30Central = cms.HLTFilter( "HLT1CaloJet",
    inputTag = cms.InputTag( 'hltAntiKT5L2L3CorrCaloJets' ),
    saveTag = cms.untracked.bool( True ),
    MinPt = cms.double( 30.0 ),
    MaxEta = cms.double( 2.6 ),
    MinN = cms.int32( 3 )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    processName = cms.string( "@" )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)
process.hltTriggerType = cms.HLTFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
process.hltTripleEG10EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
    inputTag = cms.InputTag( 'hltEGRegionalL1TripleEG5' ),
    etcutEB = cms.double( 10.0 ),
    etcutEE = cms.double( 10.0 ),
    ncandcut = cms.int32( 3 ),
    SaveTag = cms.untracked.bool( False ),
    relaxed = cms.untracked.bool( True ),
    L1IsoCand = cms.InputTag( 'hltL1IsoRecoEcalCandidate' ),
    L1NonIsoCand = cms.InputTag( 'hltL1NonIsoRecoEcalCandidate' )
)
process.hltUnseededR9shape = cms.EDProducer( "EgammaHLTR9Producer",
    recoEcalCandidateProducer = cms.InputTag( 'hltRecoEcalSuperClusterActivityCandidate' ),
    ecalRechitEB = cms.InputTag( 'hltEcalRecHitAll', 'EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRecHitAll', 'EcalRecHitsEE' ),
    useSwissCross = cms.bool( False )
)

process.hltOutputA = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring( "HLT_BTagMu_DiJet20_Mu5_v1",
         "HLT_BTagMu_DiJet60_Mu7_v1",
         "HLT_BTagMu_DiJet80_Mu9_v1",
         "HLT_BeamGas_BSC_v1",
         "HLT_BeamGas_HF_v1",
         "HLT_CentralJet80_MET100_v1",
         "HLT_CentralJet80_MET160_v1",
         "HLT_CentralJet80_MET65_v1",
         "HLT_CentralJet80_MET80_v1",
         "HLT_DiJet100_PT100_v1",
         "HLT_DiJet130_PT130_v1",
         "HLT_DiJet60_MET45_v1",
         "HLT_DiJet70_PT70_v1",
         "HLT_DiJetAve100U_v4",
         "HLT_DiJetAve140U_v4",
         "HLT_DiJetAve15U_v4",
         "HLT_DiJetAve180U_v4",
         "HLT_DiJetAve300U_v4",
         "HLT_DiJetAve30U_v4",
         "HLT_DiJetAve50U_v4",
         "HLT_DiJetAve70U_v4",
         "HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_v1",
         "HLT_DoubleEle8_CaloIdL_TrkIdVL_HT160_v2",
         "HLT_DoubleEle8_CaloIdT_TrkIdVL_HT160_v2",
         "HLT_DoubleIsoPFTau20_Trk5_v1",
         "HLT_DoubleJet30_ForwardBackward_v1",
         "HLT_DoubleJet60_ForwardBackward_v1",
         "HLT_DoubleJet70_ForwardBackward_v1",
         "HLT_DoubleJet80_ForwardBackward_v1",
         "HLT_DoubleMu3_Bs_v1",
         "HLT_DoubleMu3_HT160_v2",
         "HLT_DoubleMu3_HT200_v2",
         "HLT_DoubleMu3_Jpsi_v1",
         "HLT_DoubleMu3_Quarkonium_v1",
         "HLT_DoubleMu3_v3",
         "HLT_DoubleMu4_Acoplanarity03_v1",
         "HLT_DoubleMu5_Ele8_CaloIdL_TrkIdVL_v2",
         "HLT_DoubleMu5_Ele8_v2",
         "HLT_DoubleMu6_v1",
         "HLT_DoubleMu7_v1",
         "HLT_DoublePhoton33_v1",
         "HLT_DoublePhoton5_IsoVL_CEP_v1",
         "HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v2",
         "HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v2",
         "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1",
         "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1",
         "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1",
         "HLT_Ele15_CaloIdVT_TrkIdT_LooseIsoPFTau15_v1",
         "HLT_Ele17_CaloIdL_CaloIsoVL_Ele15_HFL_v1",
         "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1",
         "HLT_Ele17_CaloIdL_CaloIsoVL_v1",
         "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v2",
         "HLT_Ele25_CaloIdVT_TrkIdT_CentralDiJet30_v1",
         "HLT_Ele25_CaloIdVT_TrkIdT_CentralJet30_v1",
         "HLT_Ele25_CaloIdVT_TrkIdT_CentralJet40_BTagIP_v1",
         "HLT_Ele25_CaloIdVT_TrkIdT_CentralTriJet30_v1",
         "HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1",
         "HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v1",
         "HLT_Ele45_CaloIdVT_TrkIdT_v1",
         "HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v1",
         "HLT_Ele8_CaloIdL_CaloIsoVL_v1",
         "HLT_Ele8_CaloIdL_TrkIdVL_v1",
         "HLT_Ele8_v1",
         "HLT_Ele90_NoSpikeFilter_v1",
         "HLT_ExclDiJet60_HFAND_v1",
         "HLT_ExclDiJet60_HFOR_v1",
         "HLT_GlobalRunHPDNoise_v2",
         "HLT_HT160_v2",
         "HLT_HT240_v2",
         "HLT_HT260_MHT60_v2",
         "HLT_HT260_v2",
         "HLT_HT300_MHT75_v2",
         "HLT_HT300_v2",
         "HLT_HT360_v2",
         "HLT_HT440_v2",
         "HLT_HT520_v2",
         "HLT_HcalNZS_v2",
         "HLT_HcalPhiSym_v2",
         "HLT_IsoMu12_LooseIsoPFTau10_v1",
         "HLT_IsoMu12_v1",
         "HLT_IsoMu15_v5",
         "HLT_IsoMu17_CentralJet40_BTagIP_v1",
         "HLT_IsoMu17_v5",
         "HLT_IsoMu24_v1",
         "HLT_IsoMu30_v1",
         "HLT_IsoPFTau35_Trk20_MET45_v1",
         "HLT_IsoTrackHB_v2",
         "HLT_IsoTrackHE_v3",
         "HLT_Jet110_v1",
         "HLT_Jet150_v1",
         "HLT_Jet190_v1",
         "HLT_Jet240_v1",
         "HLT_Jet30_v1",
         "HLT_Jet370_NoJetID_v1",
         "HLT_Jet370_v1",
         "HLT_Jet60_v1",
         "HLT_Jet80_v1",
         "HLT_JetE30_NoBPTX3BX_NoHalo_v2",
         "HLT_JetE30_NoBPTX_NoHalo_v2",
         "HLT_JetE30_NoBPTX_v1",
         "HLT_L1DoubleMu0_v1",
         "HLT_L1MuOpen_AntiBPTX_v2",
         "HLT_L1SingleEG5_v1",
         "HLT_L1SingleJet36_v1",
         "HLT_L1SingleMu10_v1",
         "HLT_L1SingleMu20_v1",
         "HLT_L1SingleMuOpen_DT_v1",
         "HLT_L1SingleMuOpen_v1",
         "HLT_L1Tech_BSC_halo_v1",
         "HLT_L1Tech_BSC_minBias_threshold1_v2",
         "HLT_L1Tech_HBHEHO_totalOR_v1",
         "HLT_L1TrackerCosmics_v2",
         "HLT_L1_BeamHalo_v1",
         "HLT_L1_Interbunch_BSC_v1",
         "HLT_L1_PreCollisions_v1",
         "HLT_L2DoubleMu0_v2",
         "HLT_L2DoubleMu35_NoVertex_v1",
         "HLT_L2Mu10_v1",
         "HLT_L2Mu20_v1",
         "HLT_L2MuOpen_NoVertex_v1",
         "HLT_L3MuonsCosmicTracking_v1",
         "HLT_MET100_v1",
         "HLT_MET120_v1",
         "HLT_MET200_v1",
         "HLT_MR100_v1",
         "HLT_Meff440_v2",
         "HLT_Meff520_v2",
         "HLT_Meff640_v2",
         "HLT_Mu10_Ele10_CaloIdL_v2",
         "HLT_Mu12_v1",
         "HLT_Mu15_DoublePhoton15_CaloIdL_v2",
         "HLT_Mu15_LooseIsoPFTau20_v1",
         "HLT_Mu15_Photon20_CaloIdL_v2",
         "HLT_Mu15_v2",
         "HLT_Mu17_CentralJet30_v1",
         "HLT_Mu17_CentralJet40_BTagIP_v1",
         "HLT_Mu17_DiCentralJet30_v1",
         "HLT_Mu17_Ele8_CaloIdL_v1",
         "HLT_Mu17_TriCentralJet30_v1",
         "HLT_Mu20_v1",
         "HLT_Mu24_v1",
         "HLT_Mu30_v1",
         "HLT_Mu3_Ele8_CaloIdL_TrkIdVL_HT160_v2",
         "HLT_Mu3_Ele8_CaloIdT_TrkIdVL_HT160_v2",
         "HLT_Mu3_Track3_Jpsi_v4",
         "HLT_Mu3_v3",
         "HLT_Mu5_DoubleEle8_v2",
         "HLT_Mu5_Ele8_CaloIdL_TrkIdVL_Ele8_v2",
         "HLT_Mu5_HT200_v3",
         "HLT_Mu5_L2Mu2_Jpsi_v1",
         "HLT_Mu5_L2Mu2_v1",
         "HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1",
         "HLT_Mu5_v3",
         "HLT_Mu7_Track5_Jpsi_v1",
         "HLT_Mu7_Track7_Jpsi_v1",
         "HLT_Mu8_Ele17_CaloIdL_v1",
         "HLT_Mu8_HT200_v2",
         "HLT_Mu8_Jet40_v2",
         "HLT_Mu8_Photon20_CaloIdVT_IsoT_v2",
         "HLT_Mu8_v1",
         "HLT_PFMHT150_v1",
         "HLT_Photon125_NoSpikeFilter_v1",
         "HLT_Photon20_CaloIdVT_IsoT_Ele8_CaloIdL_CaloIsoVL_v1",
         "HLT_Photon20_EBOnly_NoSpikeFilter_v1",
         "HLT_Photon20_NoSpikeFilter_v1",
         "HLT_Photon20_R9Id_Photon18_R9Id_v1",
         "HLT_Photon26_CaloIdL_IsoVL_Photon18_CaloIdL_IsoVL_v1",
         "HLT_Photon26_CaloIdL_IsoVL_Photon18_v1",
         "HLT_Photon26_IsoVL_Photon18_IsoVL_v1",
         "HLT_Photon26_IsoVL_Photon18_v1",
         "HLT_Photon26_Photon18_v1",
         "HLT_Photon30_CaloIdVL_IsoL_v1",
         "HLT_Photon30_CaloIdVL_v1",
         "HLT_Photon32_CaloIdL_Photon26_CaloIdL_v1",
         "HLT_Photon60_CaloIdL_HT200_v1",
         "HLT_Photon70_CaloIdL_HT200_v1",
         "HLT_Photon70_CaloIdL_HT300_v1",
         "HLT_Photon70_CaloIdL_MHT30_v1",
         "HLT_Photon70_CaloIdL_MHT50_v1",
         "HLT_Photon75_CaloIdVL_IsoL_v1",
         "HLT_Photon75_CaloIdVL_v1",
         "HLT_Physics_v1",
         "HLT_PixelTracks_Multiplicity110_v1",
         "HLT_PixelTracks_Multiplicity125_v1",
         "HLT_QuadJet40_IsoPFTau40_v1",
         "HLT_QuadJet40_v1",
         "HLT_QuadJet50_BTagIP_v1",
         "HLT_QuadJet50_Jet40_v1",
         "HLT_QuadJet60_v1",
         "HLT_QuadJet70_v1",
         "HLT_R032_MR100_v1",
         "HLT_R032_v1",
         "HLT_R035_MR100_v1",
         "HLT_Random_v1",
         "HLT_RegionalCosmicTracking_v1",
         "HLT_Spike20_v1",
         "HLT_TripleEle10_CaloIdL_TrkIdVL_v1",
         "HLT_TripleMu5_v2",
         "HLT_ZeroBias_v1" )
    ),
    outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*",
       "keep *_hltL1GtObjectMap_*_*",
       "keep FEDRawDataCollection_rawDataCollector_*_*",
       "keep FEDRawDataCollection_source_*_*",
       "keep edmTriggerResults_*_*_*",
       "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputALCAP0 = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring( "AlCa_EcalEta_v2",
         "AlCa_EcalPi0_v3" )
    ),
    outputCommands = cms.untracked.vstring( "drop *",
       "keep *_hltAlCaEtaRecHitsFilter_*_*",
       "keep *_hltAlCaPi0RecHitsFilter_*_*",
       "keep *_hltESRegionalPi0EtaRecHit_*_*",
       "keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*",
       "keep edmTriggerResults_*_*_*",
       "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputALCAPHISYM = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring( "AlCa_EcalPhiSym_v2" )
    ),
    outputCommands = cms.untracked.vstring( "drop *",
       "keep *_hltAlCaPhiSymStream_*_*",
       "keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*",
       "keep edmTriggerResults_*_*_*",
       "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputCalibration = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring( "HLT_Calibration_v1",
         "HLT_HcalCalibration_v1",
         "HLT_TrackerCalibration_v1" )
    ),
    outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*",
       "keep FEDRawDataCollection_rawDataCollector_*_*",
       "keep FEDRawDataCollection_source_*_*",
       "keep edmTriggerResults_*_*_*",
       "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputDQM = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring( "HLT_BTagMu_DiJet20_Mu5_v1",
         "HLT_BTagMu_DiJet60_Mu7_v1",
         "HLT_BTagMu_DiJet80_Mu9_v1",
         "HLT_BeamGas_BSC_v1",
         "HLT_BeamGas_HF_v1",
         "HLT_Calibration_v1",
         "HLT_CentralJet80_MET100_v1",
         "HLT_CentralJet80_MET160_v1",
         "HLT_CentralJet80_MET65_v1",
         "HLT_CentralJet80_MET80_v1",
         "HLT_DTErrors_v1",
         "HLT_DiJet100_PT100_v1",
         "HLT_DiJet130_PT130_v1",
         "HLT_DiJet60_MET45_v1",
         "HLT_DiJet70_PT70_v1",
         "HLT_DiJetAve100U_v4",
         "HLT_DiJetAve140U_v4",
         "HLT_DiJetAve15U_v4",
         "HLT_DiJetAve180U_v4",
         "HLT_DiJetAve300U_v4",
         "HLT_DiJetAve30U_v4",
         "HLT_DiJetAve50U_v4",
         "HLT_DiJetAve70U_v4",
         "HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_v1",
         "HLT_DoubleEle8_CaloIdL_TrkIdVL_HT160_v2",
         "HLT_DoubleEle8_CaloIdT_TrkIdVL_HT160_v2",
         "HLT_DoubleIsoPFTau20_Trk5_v1",
         "HLT_DoubleJet30_ForwardBackward_v1",
         "HLT_DoubleJet60_ForwardBackward_v1",
         "HLT_DoubleJet70_ForwardBackward_v1",
         "HLT_DoubleJet80_ForwardBackward_v1",
         "HLT_DoubleMu3_Bs_v1",
         "HLT_DoubleMu3_HT160_v2",
         "HLT_DoubleMu3_HT200_v2",
         "HLT_DoubleMu3_Jpsi_v1",
         "HLT_DoubleMu3_Quarkonium_v1",
         "HLT_DoubleMu3_v3",
         "HLT_DoubleMu4_Acoplanarity03_v1",
         "HLT_DoubleMu5_Ele8_CaloIdL_TrkIdVL_v2",
         "HLT_DoubleMu5_Ele8_v2",
         "HLT_DoubleMu6_v1",
         "HLT_DoubleMu7_v1",
         "HLT_DoublePhoton33_v1",
         "HLT_DoublePhoton5_IsoVL_CEP_v1",
         "HLT_EcalCalibration_v1",
         "HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v2",
         "HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v2",
         "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1",
         "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1",
         "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1",
         "HLT_Ele15_CaloIdVT_TrkIdT_LooseIsoPFTau15_v1",
         "HLT_Ele17_CaloIdL_CaloIsoVL_Ele15_HFL_v1",
         "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1",
         "HLT_Ele17_CaloIdL_CaloIsoVL_v1",
         "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v2",
         "HLT_Ele25_CaloIdVT_TrkIdT_CentralDiJet30_v1",
         "HLT_Ele25_CaloIdVT_TrkIdT_CentralJet30_v1",
         "HLT_Ele25_CaloIdVT_TrkIdT_CentralJet40_BTagIP_v1",
         "HLT_Ele25_CaloIdVT_TrkIdT_CentralTriJet30_v1",
         "HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1",
         "HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v1",
         "HLT_Ele45_CaloIdVT_TrkIdT_v1",
         "HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v1",
         "HLT_Ele8_CaloIdL_CaloIsoVL_v1",
         "HLT_Ele8_CaloIdL_TrkIdVL_v1",
         "HLT_Ele8_v1",
         "HLT_Ele90_NoSpikeFilter_v1",
         "HLT_ExclDiJet60_HFAND_v1",
         "HLT_ExclDiJet60_HFOR_v1",
         "HLT_GlobalRunHPDNoise_v2",
         "HLT_HT160_v2",
         "HLT_HT240_v2",
         "HLT_HT260_MHT60_v2",
         "HLT_HT260_v2",
         "HLT_HT300_MHT75_v2",
         "HLT_HT300_v2",
         "HLT_HT360_v2",
         "HLT_HT440_v2",
         "HLT_HT520_v2",
         "HLT_HcalCalibration_v1",
         "HLT_HcalNZS_v2",
         "HLT_HcalPhiSym_v2",
         "HLT_IsoMu12_LooseIsoPFTau10_v1",
         "HLT_IsoMu12_v1",
         "HLT_IsoMu15_v5",
         "HLT_IsoMu17_CentralJet40_BTagIP_v1",
         "HLT_IsoMu17_v5",
         "HLT_IsoMu30_v1",
         "HLT_IsoPFTau35_Trk20_MET45_v1",
         "HLT_IsoTrackHB_v2",
         "HLT_IsoTrackHE_v3",
         "HLT_Jet110_v1",
         "HLT_Jet150_v1",
         "HLT_Jet190_v1",
         "HLT_Jet240_v1",
         "HLT_Jet30_v1",
         "HLT_Jet370_NoJetID_v1",
         "HLT_Jet370_v1",
         "HLT_Jet60_v1",
         "HLT_Jet80_v1",
         "HLT_JetE30_NoBPTX3BX_NoHalo_v2",
         "HLT_JetE30_NoBPTX_NoHalo_v2",
         "HLT_JetE30_NoBPTX_v1",
         "HLT_L1DoubleMu0_v1",
         "HLT_L1MuOpen_AntiBPTX_v2",
         "HLT_L1SingleEG5_v1",
         "HLT_L1SingleJet36_v1",
         "HLT_L1SingleMu10_v1",
         "HLT_L1SingleMu20_v1",
         "HLT_L1SingleMuOpen_DT_v1",
         "HLT_L1SingleMuOpen_v1",
         "HLT_L1Tech_BSC_halo_v1",
         "HLT_L1Tech_HBHEHO_totalOR_v1",
         "HLT_L1TrackerCosmics_v2",
         "HLT_L1_BeamHalo_v1",
         "HLT_L1_Interbunch_BSC_v1",
         "HLT_L1_PreCollisions_v1",
         "HLT_L2DoubleMu0_v2",
         "HLT_L2DoubleMu35_NoVertex_v1",
         "HLT_L2Mu10_v1",
         "HLT_L2Mu20_v1",
         "HLT_L2MuOpen_NoVertex_v1",
         "HLT_L3MuonsCosmicTracking_v1",
         "HLT_LogMonitor_v1",
         "HLT_MET100_v1",
         "HLT_MET120_v1",
         "HLT_MET200_v1",
         "HLT_MR100_v1",
         "HLT_Meff440_v2",
         "HLT_Meff520_v2",
         "HLT_Meff640_v2",
         "HLT_Mu10_Ele10_CaloIdL_v2",
         "HLT_Mu12_v1",
         "HLT_Mu15_DoublePhoton15_CaloIdL_v2",
         "HLT_Mu15_LooseIsoPFTau20_v1",
         "HLT_Mu15_Photon20_CaloIdL_v2",
         "HLT_Mu15_v2",
         "HLT_Mu17_CentralJet30_v1",
         "HLT_Mu17_CentralJet40_BTagIP_v1",
         "HLT_Mu17_DiCentralJet30_v1",
         "HLT_Mu17_Ele8_CaloIdL_v1",
         "HLT_Mu17_TriCentralJet30_v1",
         "HLT_Mu20_v1",
         "HLT_Mu24_v1",
         "HLT_Mu30_v1",
         "HLT_Mu3_Ele8_CaloIdL_TrkIdVL_HT160_v2",
         "HLT_Mu3_Ele8_CaloIdT_TrkIdVL_HT160_v2",
         "HLT_Mu3_Track3_Jpsi_v4",
         "HLT_Mu3_v3",
         "HLT_Mu5_DoubleEle8_v2",
         "HLT_Mu5_Ele8_CaloIdL_TrkIdVL_Ele8_v2",
         "HLT_Mu5_HT200_v3",
         "HLT_Mu5_L2Mu2_Jpsi_v1",
         "HLT_Mu5_L2Mu2_v1",
         "HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1",
         "HLT_Mu5_v3",
         "HLT_Mu7_Track5_Jpsi_v1",
         "HLT_Mu7_Track7_Jpsi_v1",
         "HLT_Mu8_Ele17_CaloIdL_v1",
         "HLT_Mu8_HT200_v2",
         "HLT_Mu8_Jet40_v2",
         "HLT_Mu8_Photon20_CaloIdVT_IsoT_v2",
         "HLT_Mu8_v1",
         "HLT_PFMHT150_v1",
         "HLT_Photon125_NoSpikeFilter_v1",
         "HLT_Photon20_CaloIdVT_IsoT_Ele8_CaloIdL_CaloIsoVL_v1",
         "HLT_Photon20_R9Id_Photon18_R9Id_v1",
         "HLT_Photon26_CaloIdL_IsoVL_Photon18_CaloIdL_IsoVL_v1",
         "HLT_Photon26_CaloIdL_IsoVL_Photon18_v1",
         "HLT_Photon26_IsoVL_Photon18_IsoVL_v1",
         "HLT_Photon26_IsoVL_Photon18_v1",
         "HLT_Photon26_Photon18_v1",
         "HLT_Photon30_CaloIdVL_IsoL_v1",
         "HLT_Photon30_CaloIdVL_v1",
         "HLT_Photon32_CaloIdL_Photon26_CaloIdL_v1",
         "HLT_Photon60_CaloIdL_HT200_v1",
         "HLT_Photon70_CaloIdL_HT200_v1",
         "HLT_Photon70_CaloIdL_HT300_v1",
         "HLT_Photon70_CaloIdL_MHT30_v1",
         "HLT_Photon70_CaloIdL_MHT50_v1",
         "HLT_Photon75_CaloIdVL_IsoL_v1",
         "HLT_Photon75_CaloIdVL_v1",
         "HLT_Physics_v1",
         "HLT_PixelTracks_Multiplicity110_v1",
         "HLT_PixelTracks_Multiplicity125_v1",
         "HLT_QuadJet40_IsoPFTau40_v1",
         "HLT_QuadJet40_v1",
         "HLT_QuadJet50_BTagIP_v1",
         "HLT_QuadJet50_Jet40_v1",
         "HLT_QuadJet60_v1",
         "HLT_QuadJet70_v1",
         "HLT_R032_MR100_v1",
         "HLT_R032_v1",
         "HLT_R035_MR100_v1",
         "HLT_Random_v1",
         "HLT_RegionalCosmicTracking_v1",
         "HLT_TrackerCalibration_v1",
         "HLT_TripleEle10_CaloIdL_TrkIdVL_v1",
         "HLT_TripleMu5_v2",
         "HLT_ZeroBias_v1" )
    ),
    outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*",
       "keep *_hltDt4DSegments_*_*",
       "keep *_hltL1GtObjectMap_*_*",
       "keep FEDRawDataCollection_rawDataCollector_*_*",
       "keep FEDRawDataCollection_source_*_*",
       "keep edmTriggerResults_*_*_*",
       "keep triggerTriggerEventWithRefs_*_*_*",
       "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputEcalCalibration = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring( "HLT_EcalCalibration_v1" )
    ),
    outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*",
       "keep *_hltEcalCalibrationRaw_*_*",
       "keep edmTriggerResults_*_*_*",
       "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputExpress = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring( "HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1",
         "HLT_L1Tech_BSC_minBias_threshold1_v2",
         "HLT_Mu15_v2",
         "HLT_ZeroBias_v1" )
    ),
    outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*",
       "keep *_hltL1GtObjectMap_*_*",
       "keep FEDRawDataCollection_rawDataCollector_*_*",
       "keep FEDRawDataCollection_source_*_*",
       "keep edmTriggerResults_*_*_*",
       "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputHLTDQM = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring( "AlCa_EcalEta_v2",
         "AlCa_EcalPhiSym_v2",
         "AlCa_EcalPi0_v3",
         "AlCa_RPCMuonNoHits_v2",
         "AlCa_RPCMuonNoTriggers_v2",
         "AlCa_RPCMuonNormalisation_v2",
         "HLT_BTagMu_DiJet20_Mu5_v1",
         "HLT_BTagMu_DiJet60_Mu7_v1",
         "HLT_BTagMu_DiJet80_Mu9_v1",
         "HLT_BeamGas_BSC_v1",
         "HLT_BeamGas_HF_v1",
         "HLT_CentralJet80_MET100_v1",
         "HLT_CentralJet80_MET160_v1",
         "HLT_CentralJet80_MET65_v1",
         "HLT_CentralJet80_MET80_v1",
         "HLT_DTErrors_v1",
         "HLT_DiJet100_PT100_v1",
         "HLT_DiJet130_PT130_v1",
         "HLT_DiJet60_MET45_v1",
         "HLT_DiJet70_PT70_v1",
         "HLT_DiJetAve100U_v4",
         "HLT_DiJetAve140U_v4",
         "HLT_DiJetAve15U_v4",
         "HLT_DiJetAve180U_v4",
         "HLT_DiJetAve300U_v4",
         "HLT_DiJetAve30U_v4",
         "HLT_DiJetAve50U_v4",
         "HLT_DiJetAve70U_v4",
         "HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_v1",
         "HLT_DoubleEle8_CaloIdL_TrkIdVL_HT160_v2",
         "HLT_DoubleEle8_CaloIdT_TrkIdVL_HT160_v2",
         "HLT_DoubleIsoPFTau20_Trk5_v1",
         "HLT_DoubleJet30_ForwardBackward_v1",
         "HLT_DoubleJet60_ForwardBackward_v1",
         "HLT_DoubleJet70_ForwardBackward_v1",
         "HLT_DoubleJet80_ForwardBackward_v1",
         "HLT_DoubleMu3_Bs_v1",
         "HLT_DoubleMu3_HT160_v2",
         "HLT_DoubleMu3_HT200_v2",
         "HLT_DoubleMu3_Jpsi_v1",
         "HLT_DoubleMu3_Quarkonium_v1",
         "HLT_DoubleMu3_v3",
         "HLT_DoubleMu4_Acoplanarity03_v1",
         "HLT_DoubleMu5_Ele8_CaloIdL_TrkIdVL_v2",
         "HLT_DoubleMu5_Ele8_v2",
         "HLT_DoubleMu6_v1",
         "HLT_DoubleMu7_v1",
         "HLT_DoublePhoton33_v1",
         "HLT_DoublePhoton5_IsoVL_CEP_v1",
         "HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v2",
         "HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v2",
         "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1",
         "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1",
         "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1",
         "HLT_Ele15_CaloIdVT_TrkIdT_LooseIsoPFTau15_v1",
         "HLT_Ele17_CaloIdL_CaloIsoVL_Ele15_HFL_v1",
         "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1",
         "HLT_Ele17_CaloIdL_CaloIsoVL_v1",
         "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v2",
         "HLT_Ele25_CaloIdVT_TrkIdT_CentralDiJet30_v1",
         "HLT_Ele25_CaloIdVT_TrkIdT_CentralJet30_v1",
         "HLT_Ele25_CaloIdVT_TrkIdT_CentralJet40_BTagIP_v1",
         "HLT_Ele25_CaloIdVT_TrkIdT_CentralTriJet30_v1",
         "HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1",
         "HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v1",
         "HLT_Ele45_CaloIdVT_TrkIdT_v1",
         "HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v1",
         "HLT_Ele8_CaloIdL_CaloIsoVL_v1",
         "HLT_Ele8_CaloIdL_TrkIdVL_v1",
         "HLT_Ele8_v1",
         "HLT_Ele90_NoSpikeFilter_v1",
         "HLT_ExclDiJet60_HFAND_v1",
         "HLT_ExclDiJet60_HFOR_v1",
         "HLT_GlobalRunHPDNoise_v2",
         "HLT_HT160_v2",
         "HLT_HT240_v2",
         "HLT_HT260_MHT60_v2",
         "HLT_HT260_v2",
         "HLT_HT300_MHT75_v2",
         "HLT_HT300_v2",
         "HLT_HT360_v2",
         "HLT_HT440_v2",
         "HLT_HT520_v2",
         "HLT_HcalNZS_v2",
         "HLT_HcalPhiSym_v2",
         "HLT_IsoMu12_LooseIsoPFTau10_v1",
         "HLT_IsoMu12_v1",
         "HLT_IsoMu15_v5",
         "HLT_IsoMu17_CentralJet40_BTagIP_v1",
         "HLT_IsoMu17_v5",
         "HLT_IsoMu30_v1",
         "HLT_IsoPFTau35_Trk20_MET45_v1",
         "HLT_IsoTrackHB_v2",
         "HLT_IsoTrackHE_v3",
         "HLT_Jet110_v1",
         "HLT_Jet150_v1",
         "HLT_Jet190_v1",
         "HLT_Jet240_v1",
         "HLT_Jet30_v1",
         "HLT_Jet370_NoJetID_v1",
         "HLT_Jet370_v1",
         "HLT_Jet60_v1",
         "HLT_Jet80_v1",
         "HLT_JetE30_NoBPTX3BX_NoHalo_v2",
         "HLT_JetE30_NoBPTX_NoHalo_v2",
         "HLT_JetE30_NoBPTX_v1",
         "HLT_L1DoubleMu0_v1",
         "HLT_L1MuOpen_AntiBPTX_v2",
         "HLT_L1SingleEG5_v1",
         "HLT_L1SingleJet36_v1",
         "HLT_L1SingleMu10_v1",
         "HLT_L1SingleMu20_v1",
         "HLT_L1SingleMuOpen_DT_v1",
         "HLT_L1SingleMuOpen_v1",
         "HLT_L1Tech_BSC_halo_v1",
         "HLT_L1Tech_HBHEHO_totalOR_v1",
         "HLT_L1TrackerCosmics_v2",
         "HLT_L1_BeamHalo_v1",
         "HLT_L1_Interbunch_BSC_v1",
         "HLT_L1_PreCollisions_v1",
         "HLT_L2DoubleMu0_v2",
         "HLT_L2DoubleMu35_NoVertex_v1",
         "HLT_L2Mu10_v1",
         "HLT_L2Mu20_v1",
         "HLT_L2MuOpen_NoVertex_v1",
         "HLT_L3MuonsCosmicTracking_v1",
         "HLT_LogMonitor_v1",
         "HLT_MET100_v1",
         "HLT_MET120_v1",
         "HLT_MET200_v1",
         "HLT_MR100_v1",
         "HLT_Meff440_v2",
         "HLT_Meff520_v2",
         "HLT_Meff640_v2",
         "HLT_Mu10_Ele10_CaloIdL_v2",
         "HLT_Mu12_v1",
         "HLT_Mu15_DoublePhoton15_CaloIdL_v2",
         "HLT_Mu15_LooseIsoPFTau20_v1",
         "HLT_Mu15_Photon20_CaloIdL_v2",
         "HLT_Mu15_v2",
         "HLT_Mu17_CentralJet30_v1",
         "HLT_Mu17_CentralJet40_BTagIP_v1",
         "HLT_Mu17_DiCentralJet30_v1",
         "HLT_Mu17_Ele8_CaloIdL_v1",
         "HLT_Mu17_TriCentralJet30_v1",
         "HLT_Mu20_v1",
         "HLT_Mu24_v1",
         "HLT_Mu30_v1",
         "HLT_Mu3_Ele8_CaloIdL_TrkIdVL_HT160_v2",
         "HLT_Mu3_Ele8_CaloIdT_TrkIdVL_HT160_v2",
         "HLT_Mu3_Track3_Jpsi_v4",
         "HLT_Mu3_v3",
         "HLT_Mu5_DoubleEle8_v2",
         "HLT_Mu5_Ele8_CaloIdL_TrkIdVL_Ele8_v2",
         "HLT_Mu5_HT200_v3",
         "HLT_Mu5_L2Mu2_Jpsi_v1",
         "HLT_Mu5_L2Mu2_v1",
         "HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1",
         "HLT_Mu5_v3",
         "HLT_Mu7_Track5_Jpsi_v1",
         "HLT_Mu7_Track7_Jpsi_v1",
         "HLT_Mu8_Ele17_CaloIdL_v1",
         "HLT_Mu8_HT200_v2",
         "HLT_Mu8_Jet40_v2",
         "HLT_Mu8_Photon20_CaloIdVT_IsoT_v2",
         "HLT_Mu8_v1",
         "HLT_PFMHT150_v1",
         "HLT_Photon125_NoSpikeFilter_v1",
         "HLT_Photon20_CaloIdVT_IsoT_Ele8_CaloIdL_CaloIsoVL_v1",
         "HLT_Photon20_R9Id_Photon18_R9Id_v1",
         "HLT_Photon26_CaloIdL_IsoVL_Photon18_CaloIdL_IsoVL_v1",
         "HLT_Photon26_CaloIdL_IsoVL_Photon18_v1",
         "HLT_Photon26_IsoVL_Photon18_IsoVL_v1",
         "HLT_Photon26_IsoVL_Photon18_v1",
         "HLT_Photon26_Photon18_v1",
         "HLT_Photon30_CaloIdVL_IsoL_v1",
         "HLT_Photon30_CaloIdVL_v1",
         "HLT_Photon32_CaloIdL_Photon26_CaloIdL_v1",
         "HLT_Photon60_CaloIdL_HT200_v1",
         "HLT_Photon70_CaloIdL_HT200_v1",
         "HLT_Photon70_CaloIdL_HT300_v1",
         "HLT_Photon70_CaloIdL_MHT30_v1",
         "HLT_Photon70_CaloIdL_MHT50_v1",
         "HLT_Photon75_CaloIdVL_IsoL_v1",
         "HLT_Photon75_CaloIdVL_v1",
         "HLT_Physics_v1",
         "HLT_PixelTracks_Multiplicity110_v1",
         "HLT_PixelTracks_Multiplicity125_v1",
         "HLT_QuadJet40_IsoPFTau40_v1",
         "HLT_QuadJet40_v1",
         "HLT_QuadJet50_BTagIP_v1",
         "HLT_QuadJet50_Jet40_v1",
         "HLT_QuadJet60_v1",
         "HLT_QuadJet70_v1",
         "HLT_R032_MR100_v1",
         "HLT_R032_v1",
         "HLT_R035_MR100_v1",
         "HLT_Random_v1",
         "HLT_RegionalCosmicTracking_v1",
         "HLT_TripleEle10_CaloIdL_TrkIdVL_v1",
         "HLT_TripleMu5_v2",
         "HLT_ZeroBias_v1" )
    ),
    outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*",
       "keep *_hltAlCaEtaRecHitsFilter_*_*",
       "keep *_hltAlCaPhiSymStream_*_*",
       "keep *_hltAlCaPi0RecHitsFilter_*_*",
       "keep *_hltBLifetimeL25AssociatorStartupU_*_*",
       "keep *_hltBLifetimeL25BJetTagsStartupU_*_*",
       "keep *_hltBLifetimeL25JetsStartupU_*_*",
       "keep *_hltBLifetimeL25TagInfosStartupU_*_*",
       "keep *_hltBLifetimeL3AssociatorStartupU_*_*",
       "keep *_hltBLifetimeL3BJetTagsStartupU_*_*",
       "keep *_hltBLifetimeL3JetsStartupU_*_*",
       "keep *_hltBLifetimeL3TagInfosStartupU_*_*",
       "keep *_hltBLifetimeRegionalCtfWithMaterialTracksStartupU_*_*",
       "keep *_hltBSoftMuonL25BJetTagsUByDR_*_*",
       "keep *_hltBSoftMuonL25JetsU_*_*",
       "keep *_hltBSoftMuonL25TagInfosU_*_*",
       "keep *_hltBSoftMuonL3BJetTagsUByDR_*_*",
       "keep *_hltBSoftMuonL3TagInfosU_*_*",
       "keep *_hltCsc2DRecHits_*_*",
       "keep *_hltCscSegments_*_*",
       "keep *_hltDt4DSegments_*_*",
       "keep *_hltFilterL25LeadingTrackPtCutDoubleIsoTau15Trk5_*_*",
       "keep *_hltFilterL25LeadingTrackPtCutSingleIsoTau30Trk5MET20_*_*",
       "keep *_hltFilterL2EcalIsolationDoubleIsoTau15Trk5_*_*",
       "keep *_hltFilterL2EcalIsolationDoubleLooseIsoTau15_*_*",
       "keep *_hltFilterL2EcalIsolationSingleIsoTau30Trk5MET20_*_*",
       "keep *_hltFilterL2EcalIsolationSingleLooseIsoTau20_*_*",
       "keep *_hltFilterL2EtCutDoubleIsoTau15Trk5_*_*",
       "keep *_hltFilterL2EtCutDoubleLooseIsoTau15_*_*",
       "keep *_hltFilterL2EtCutSingleIsoTau30Trk5MET20_*_*",
       "keep *_hltFilterL2EtCutSingleLooseIsoTau20_*_*",
       "keep *_hltFilterL3TrackIsolationDoubleIsoTau15Trk5_*_*",
       "keep *_hltFilterL3TrackIsolationSingleIsoTau30Trk5MET20_*_*",
       "keep *_hltGtDigis_*_*",
       "keep *_hltHITCtfWithMaterialTracksHB8E29_*_*",
       "keep *_hltHITCtfWithMaterialTracksHE8E29_*_*",
       "keep *_hltHITIPTCorrectorHB8E29_*_*",
       "keep *_hltHITIPTCorrectorHE8E29_*_*",
       "keep *_hltHcalDigis_*_*",
       "keep *_hltIconeCentral1Regional_*_*",
       "keep *_hltIconeCentral2Regional_*_*",
       "keep *_hltIconeCentral3Regional_*_*",
       "keep *_hltIconeCentral4Regional_*_*",
       "keep *_hltIconeTau1Regional_*_*",
       "keep *_hltIconeTau2Regional_*_*",
       "keep *_hltIconeTau3Regional_*_*",
       "keep *_hltIconeTau4Regional_*_*",
       "keep *_hltIsolPixelTrackProdHB8E29_*_*",
       "keep *_hltIsolPixelTrackProdHE8E29_*_*",
       "keep *_hltIterativeCone5CaloJets_*_*",
       "keep *_hltL1IsoLargeWindowElectronPixelSeeds_*_*",
       "keep *_hltL1IsoRecoEcalCandidate_*_*",
       "keep *_hltL1IsoSiStripElectronPixelSeeds_*_*",
       "keep *_hltL1IsoStartUpElectronPixelSeeds_*_*",
       "keep *_hltL1IsolatedElectronHcalIsol_*_*",
       "keep *_hltL1NonIsoLargeWindowElectronPixelSeeds_*_*",
       "keep *_hltL1NonIsoRecoEcalCandidate_*_*",
       "keep *_hltL1NonIsoSiStripElectronPixelSeeds_*_*",
       "keep *_hltL1NonIsoStartUpElectronPixelSeeds_*_*",
       "keep *_hltL1NonIsolatedElectronHcalIsol_*_*",
       "keep *_hltL1extraParticles_*_*",
       "keep *_hltL1sDoubleLooseIsoTau15_*_*",
       "keep *_hltL1sSingleLooseIsoTau20_*_*",
       "keep *_hltL25TauConeIsolation_*_*",
       "keep *_hltL25TauCtfWithMaterialTracks_*_*",
       "keep *_hltL25TauJetTracksAssociator_*_*",
       "keep *_hltL25TauLeadingTrackPtCutSelector_*_*",
       "keep *_hltL2MuonCandidates_*_*",
       "keep *_hltL2MuonIsolations_*_*",
       "keep *_hltL2MuonSeeds_*_*",
       "keep *_hltL2Muons_*_*",
       "keep *_hltL2TauJets_*_*",
       "keep *_hltL2TauNarrowConeIsolationProducer_*_*",
       "keep *_hltL2TauRelaxingIsolationSelector_*_*",
       "keep *_hltL3MuonCandidates_*_*",
       "keep *_hltL3MuonIsolations_*_*",
       "keep *_hltL3MuonsIOHit_*_*",
       "keep *_hltL3MuonsLinksCombination_*_*",
       "keep *_hltL3MuonsOIHit_*_*",
       "keep *_hltL3MuonsOIState_*_*",
       "keep *_hltL3Muons_*_*",
       "keep *_hltL3TauConeIsolation_*_*",
       "keep *_hltL3TauCtfWithMaterialTracks_*_*",
       "keep *_hltL3TauIsolationSelector_*_*",
       "keep *_hltL3TauJetTracksAssociator_*_*",
       "keep *_hltL3TkFromL2OICombination_*_*",
       "keep *_hltL3TkTracksFromL2IOHit_*_*",
       "keep *_hltL3TkTracksFromL2OIHit_*_*",
       "keep *_hltL3TkTracksFromL2OIState_*_*",
       "keep *_hltL3TrackCandidateFromL2IOHit_*_*",
       "keep *_hltL3TrackCandidateFromL2OIHit_*_*",
       "keep *_hltL3TrackCandidateFromL2OIState_*_*",
       "keep *_hltL3TrajSeedIOHit_*_*",
       "keep *_hltL3TrajSeedOIHit_*_*",
       "keep *_hltL3TrajSeedOIState_*_*",
       "keep *_hltL3TrajectorySeed_*_*",
       "keep *_hltMCJetCorJetIcone5HF07_*_*",
       "keep *_hltMet_*_*",
       "keep *_hltMuTrackJpsiCtfTrackCands_*_*",
       "keep *_hltMuTrackJpsiPixelTrackCands_*_*",
       "keep *_hltMuonCSCDigis_*_*",
       "keep *_hltMuonRPCDigis_*_*",
       "keep *_hltOfflineBeamSpot_*_*",
       "keep *_hltPixelMatchLargeWindowElectronsL1Iso_*_*",
       "keep *_hltPixelMatchLargeWindowElectronsL1NonIso_*_*",
       "keep *_hltPixelTracks_*_*",
       "keep *_hltRpcRecHits_*_*",
       "keep *_hltSiPixelClusters_*_*",
       "keep *_hltSiStripRawToClustersFacility_*_*",
       "keep *_hltTowerMakerForMuons_*_*",
       "keep edmTriggerResults_*_*_*",
       "keep triggerTriggerEventWithRefs_*_*_*",
       "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputHLTDQMResults = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring( "HLTriggerFinalPath" )
    ),
    outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*",
       "keep LumiScalerss_*_*_*",
       "keep edmTriggerResults_*_*_*" )
)
process.hltOutputHLTMON = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring( "AlCa_EcalEta_v2",
         "AlCa_EcalPhiSym_v2",
         "AlCa_EcalPi0_v3",
         "AlCa_RPCMuonNoHits_v2",
         "AlCa_RPCMuonNoTriggers_v2",
         "AlCa_RPCMuonNormalisation_v2",
         "HLT_BTagMu_DiJet20_Mu5_v1",
         "HLT_BTagMu_DiJet60_Mu7_v1",
         "HLT_BTagMu_DiJet80_Mu9_v1",
         "HLT_BeamGas_BSC_v1",
         "HLT_BeamGas_HF_v1",
         "HLT_CentralJet80_MET100_v1",
         "HLT_CentralJet80_MET160_v1",
         "HLT_CentralJet80_MET65_v1",
         "HLT_CentralJet80_MET80_v1",
         "HLT_DTErrors_v1",
         "HLT_DiJet100_PT100_v1",
         "HLT_DiJet130_PT130_v1",
         "HLT_DiJet60_MET45_v1",
         "HLT_DiJet70_PT70_v1",
         "HLT_DiJetAve100U_v4",
         "HLT_DiJetAve140U_v4",
         "HLT_DiJetAve15U_v4",
         "HLT_DiJetAve180U_v4",
         "HLT_DiJetAve300U_v4",
         "HLT_DiJetAve30U_v4",
         "HLT_DiJetAve50U_v4",
         "HLT_DiJetAve70U_v4",
         "HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_v1",
         "HLT_DoubleEle8_CaloIdL_TrkIdVL_HT160_v2",
         "HLT_DoubleEle8_CaloIdT_TrkIdVL_HT160_v2",
         "HLT_DoubleIsoPFTau20_Trk5_v1",
         "HLT_DoubleJet30_ForwardBackward_v1",
         "HLT_DoubleJet60_ForwardBackward_v1",
         "HLT_DoubleJet70_ForwardBackward_v1",
         "HLT_DoubleJet80_ForwardBackward_v1",
         "HLT_DoubleMu3_Bs_v1",
         "HLT_DoubleMu3_HT160_v2",
         "HLT_DoubleMu3_HT200_v2",
         "HLT_DoubleMu3_Jpsi_v1",
         "HLT_DoubleMu3_Quarkonium_v1",
         "HLT_DoubleMu3_v3",
         "HLT_DoubleMu4_Acoplanarity03_v1",
         "HLT_DoubleMu5_Ele8_CaloIdL_TrkIdVL_v2",
         "HLT_DoubleMu5_Ele8_v2",
         "HLT_DoubleMu6_v1",
         "HLT_DoubleMu7_v1",
         "HLT_DoublePhoton33_v1",
         "HLT_DoublePhoton5_IsoVL_CEP_v1",
         "HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v2",
         "HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v2",
         "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1",
         "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1",
         "HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1",
         "HLT_Ele15_CaloIdVT_TrkIdT_LooseIsoPFTau15_v1",
         "HLT_Ele17_CaloIdL_CaloIsoVL_Ele15_HFL_v1",
         "HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1",
         "HLT_Ele17_CaloIdL_CaloIsoVL_v1",
         "HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v2",
         "HLT_Ele25_CaloIdVT_TrkIdT_CentralDiJet30_v1",
         "HLT_Ele25_CaloIdVT_TrkIdT_CentralJet30_v1",
         "HLT_Ele25_CaloIdVT_TrkIdT_CentralJet40_BTagIP_v1",
         "HLT_Ele25_CaloIdVT_TrkIdT_CentralTriJet30_v1",
         "HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1",
         "HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v1",
         "HLT_Ele45_CaloIdVT_TrkIdT_v1",
         "HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v1",
         "HLT_Ele8_CaloIdL_CaloIsoVL_v1",
         "HLT_Ele8_CaloIdL_TrkIdVL_v1",
         "HLT_Ele8_v1",
         "HLT_Ele90_NoSpikeFilter_v1",
         "HLT_ExclDiJet60_HFAND_v1",
         "HLT_ExclDiJet60_HFOR_v1",
         "HLT_GlobalRunHPDNoise_v2",
         "HLT_HT160_v2",
         "HLT_HT240_v2",
         "HLT_HT260_MHT60_v2",
         "HLT_HT260_v2",
         "HLT_HT300_MHT75_v2",
         "HLT_HT300_v2",
         "HLT_HT360_v2",
         "HLT_HT440_v2",
         "HLT_HT520_v2",
         "HLT_HcalNZS_v2",
         "HLT_HcalPhiSym_v2",
         "HLT_IsoMu12_LooseIsoPFTau10_v1",
         "HLT_IsoMu12_v1",
         "HLT_IsoMu15_v5",
         "HLT_IsoMu17_CentralJet40_BTagIP_v1",
         "HLT_IsoMu17_v5",
         "HLT_IsoMu30_v1",
         "HLT_IsoPFTau35_Trk20_MET45_v1",
         "HLT_IsoTrackHB_v2",
         "HLT_IsoTrackHE_v3",
         "HLT_Jet110_v1",
         "HLT_Jet150_v1",
         "HLT_Jet190_v1",
         "HLT_Jet240_v1",
         "HLT_Jet30_v1",
         "HLT_Jet370_NoJetID_v1",
         "HLT_Jet370_v1",
         "HLT_Jet60_v1",
         "HLT_Jet80_v1",
         "HLT_JetE30_NoBPTX3BX_NoHalo_v2",
         "HLT_JetE30_NoBPTX_NoHalo_v2",
         "HLT_JetE30_NoBPTX_v1",
         "HLT_L1DoubleMu0_v1",
         "HLT_L1MuOpen_AntiBPTX_v2",
         "HLT_L1SingleEG5_v1",
         "HLT_L1SingleJet36_v1",
         "HLT_L1SingleMu10_v1",
         "HLT_L1SingleMu20_v1",
         "HLT_L1SingleMuOpen_DT_v1",
         "HLT_L1SingleMuOpen_v1",
         "HLT_L1Tech_BSC_halo_v1",
         "HLT_L1Tech_HBHEHO_totalOR_v1",
         "HLT_L1TrackerCosmics_v2",
         "HLT_L1_BeamHalo_v1",
         "HLT_L1_Interbunch_BSC_v1",
         "HLT_L1_PreCollisions_v1",
         "HLT_L2DoubleMu0_v2",
         "HLT_L2DoubleMu35_NoVertex_v1",
         "HLT_L2Mu10_v1",
         "HLT_L2Mu20_v1",
         "HLT_L2MuOpen_NoVertex_v1",
         "HLT_L3MuonsCosmicTracking_v1",
         "HLT_LogMonitor_v1",
         "HLT_MET100_v1",
         "HLT_MET120_v1",
         "HLT_MET200_v1",
         "HLT_MR100_v1",
         "HLT_Meff440_v2",
         "HLT_Meff520_v2",
         "HLT_Meff640_v2",
         "HLT_Mu10_Ele10_CaloIdL_v2",
         "HLT_Mu12_v1",
         "HLT_Mu15_DoublePhoton15_CaloIdL_v2",
         "HLT_Mu15_LooseIsoPFTau20_v1",
         "HLT_Mu15_Photon20_CaloIdL_v2",
         "HLT_Mu15_v2",
         "HLT_Mu17_CentralJet30_v1",
         "HLT_Mu17_CentralJet40_BTagIP_v1",
         "HLT_Mu17_DiCentralJet30_v1",
         "HLT_Mu17_Ele8_CaloIdL_v1",
         "HLT_Mu17_TriCentralJet30_v1",
         "HLT_Mu20_v1",
         "HLT_Mu24_v1",
         "HLT_Mu30_v1",
         "HLT_Mu3_Ele8_CaloIdL_TrkIdVL_HT160_v2",
         "HLT_Mu3_Ele8_CaloIdT_TrkIdVL_HT160_v2",
         "HLT_Mu3_Track3_Jpsi_v4",
         "HLT_Mu3_v3",
         "HLT_Mu5_DoubleEle8_v2",
         "HLT_Mu5_Ele8_CaloIdL_TrkIdVL_Ele8_v2",
         "HLT_Mu5_HT200_v3",
         "HLT_Mu5_L2Mu2_Jpsi_v1",
         "HLT_Mu5_L2Mu2_v1",
         "HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1",
         "HLT_Mu5_v3",
         "HLT_Mu7_Track5_Jpsi_v1",
         "HLT_Mu7_Track7_Jpsi_v1",
         "HLT_Mu8_Ele17_CaloIdL_v1",
         "HLT_Mu8_HT200_v2",
         "HLT_Mu8_Jet40_v2",
         "HLT_Mu8_Photon20_CaloIdVT_IsoT_v2",
         "HLT_Mu8_v1",
         "HLT_PFMHT150_v1",
         "HLT_Photon125_NoSpikeFilter_v1",
         "HLT_Photon20_CaloIdVT_IsoT_Ele8_CaloIdL_CaloIsoVL_v1",
         "HLT_Photon20_R9Id_Photon18_R9Id_v1",
         "HLT_Photon26_CaloIdL_IsoVL_Photon18_CaloIdL_IsoVL_v1",
         "HLT_Photon26_CaloIdL_IsoVL_Photon18_v1",
         "HLT_Photon26_IsoVL_Photon18_IsoVL_v1",
         "HLT_Photon26_IsoVL_Photon18_v1",
         "HLT_Photon26_Photon18_v1",
         "HLT_Photon30_CaloIdVL_IsoL_v1",
         "HLT_Photon30_CaloIdVL_v1",
         "HLT_Photon32_CaloIdL_Photon26_CaloIdL_v1",
         "HLT_Photon60_CaloIdL_HT200_v1",
         "HLT_Photon70_CaloIdL_HT200_v1",
         "HLT_Photon70_CaloIdL_HT300_v1",
         "HLT_Photon70_CaloIdL_MHT30_v1",
         "HLT_Photon70_CaloIdL_MHT50_v1",
         "HLT_Photon75_CaloIdVL_IsoL_v1",
         "HLT_Photon75_CaloIdVL_v1",
         "HLT_Physics_v1",
         "HLT_PixelTracks_Multiplicity110_v1",
         "HLT_PixelTracks_Multiplicity125_v1",
         "HLT_QuadJet40_IsoPFTau40_v1",
         "HLT_QuadJet40_v1",
         "HLT_QuadJet50_BTagIP_v1",
         "HLT_QuadJet50_Jet40_v1",
         "HLT_QuadJet60_v1",
         "HLT_QuadJet70_v1",
         "HLT_R032_MR100_v1",
         "HLT_R032_v1",
         "HLT_R035_MR100_v1",
         "HLT_Random_v1",
         "HLT_RegionalCosmicTracking_v1",
         "HLT_TripleEle10_CaloIdL_TrkIdVL_v1",
         "HLT_TripleMu5_v2",
         "HLT_ZeroBias_v1" )
    ),
    outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*",
       "keep *_hltAlCaEtaRecHitsFilter_*_*",
       "keep *_hltAlCaPi0RecHitsFilter_*_*",
       "keep *_hltBLifetimeL25AssociatorStartupU_*_*",
       "keep *_hltBLifetimeL25BJetTagsStartupU_*_*",
       "keep *_hltBLifetimeL25JetsStartupU_*_*",
       "keep *_hltBLifetimeL25TagInfosStartupU_*_*",
       "keep *_hltBLifetimeL3AssociatorStartupU_*_*",
       "keep *_hltBLifetimeL3BJetTagsStartupU_*_*",
       "keep *_hltBLifetimeL3JetsStartupU_*_*",
       "keep *_hltBLifetimeL3TagInfosStartupU_*_*",
       "keep *_hltBLifetimeRegionalCtfWithMaterialTracksStartupU_*_*",
       "keep *_hltBSoftMuonL25BJetTagsUByDR_*_*",
       "keep *_hltBSoftMuonL25JetsU_*_*",
       "keep *_hltBSoftMuonL25TagInfosU_*_*",
       "keep *_hltBSoftMuonL3BJetTagsUByDR_*_*",
       "keep *_hltBSoftMuonL3BJetTagsUByPt_*_*",
       "keep *_hltBSoftMuonL3TagInfosU_*_*",
       "keep *_hltCkfL1IsoLargeWindowTrackCandidates_*_*",
       "keep *_hltCkfL1NonIsoLargeWindowTrackCandidates_*_*",
       "keep *_hltCorrectedHybridSuperClustersL1Isolated_*_*",
       "keep *_hltCorrectedHybridSuperClustersL1NonIsolated_*_*",
       "keep *_hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated_*_*",
       "keep *_hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated_*_*",
       "keep *_hltCscSegments_*_*",
       "keep *_hltCtfL1IsoLargeWindowWithMaterialTracks_*_*",
       "keep *_hltCtfL1NonIsoLargeWindowWithMaterialTracks_*_*",
       "keep *_hltDt1DRecHits_*_*",
       "keep *_hltDt4DSegments_*_*",
       "keep *_hltFilterL25LeadingTrackPtCutDoubleIsoTau15Trk5_*_*",
       "keep *_hltFilterL25LeadingTrackPtCutSingleIsoTau30Trk5MET20_*_*",
       "keep *_hltFilterL2EcalIsolationDoubleIsoTau15Trk5_*_*",
       "keep *_hltFilterL2EcalIsolationDoubleLooseIsoTau15_*_*",
       "keep *_hltFilterL2EcalIsolationSingleIsoTau30Trk5MET20_*_*",
       "keep *_hltFilterL2EcalIsolationSingleLooseIsoTau20_*_*",
       "keep *_hltFilterL2EtCutDoubleIsoTau15Trk5_*_*",
       "keep *_hltFilterL2EtCutDoubleLooseIsoTau15_*_*",
       "keep *_hltFilterL2EtCutSingleIsoTau30Trk5MET20_*_*",
       "keep *_hltFilterL2EtCutSingleLooseIsoTau20_*_*",
       "keep *_hltFilterL3TrackIsolationDoubleIsoTau15Trk5_*_*",
       "keep *_hltFilterL3TrackIsolationSingleIsoTau30Trk5MET20_*_*",
       "keep *_hltGctDigis_*_*",
       "keep *_hltGtDigis_*_*",
       "keep *_hltHoreco_*_*",
       "keep *_hltIconeCentral1Regional_*_*",
       "keep *_hltIconeCentral2Regional_*_*",
       "keep *_hltIconeCentral3Regional_*_*",
       "keep *_hltIconeCentral4Regional_*_*",
       "keep *_hltIconeTau1Regional_*_*",
       "keep *_hltIconeTau2Regional_*_*",
       "keep *_hltIconeTau3Regional_*_*",
       "keep *_hltIconeTau4Regional_*_*",
       "keep *_hltL1GtObjectMap_*_*",
       "keep *_hltL1IsoEgammaRegionalCTFFinalFitWithMaterial_*_*",
       "keep *_hltL1IsoEgammaRegionalCkfTrackCandidates_*_*",
       "keep *_hltL1IsoEgammaRegionalPixelSeedGenerator_*_*",
       "keep *_hltL1IsoHLTClusterShape_*_*",
       "keep *_hltL1IsoLargeWindowElectronPixelSeeds_*_*",
       "keep *_hltL1IsoPhotonHollowTrackIsol_*_*",
       "keep *_hltL1IsoStartUpElectronPixelSeeds_*_*",
       "keep *_hltL1IsolatedPhotonEcalIsol_*_*",
       "keep *_hltL1IsolatedPhotonHcalIsol_*_*",
       "keep *_hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial_*_*",
       "keep *_hltL1NonIsoEgammaRegionalCkfTrackCandidates_*_*",
       "keep *_hltL1NonIsoEgammaRegionalPixelSeedGenerator_*_*",
       "keep *_hltL1NonIsoHLTClusterShape_*_*",
       "keep *_hltL1NonIsoLargeWindowElectronPixelSeeds_*_*",
       "keep *_hltL1NonIsoPhotonHollowTrackIsol_*_*",
       "keep *_hltL1NonIsoStartUpElectronPixelSeeds_*_*",
       "keep *_hltL1NonIsolatedPhotonEcalIsol_*_*",
       "keep *_hltL1NonIsolatedPhotonHcalIsol_*_*",
       "keep *_hltL1extraParticles_*_*",
       "keep *_hltL1sDoubleLooseIsoTau15_*_*",
       "keep *_hltL1sSingleLooseIsoTau20_*_*",
       "keep *_hltL25TauConeIsolation_*_*",
       "keep *_hltL25TauCtfWithMaterialTracks_*_*",
       "keep *_hltL25TauJetTracksAssociator_*_*",
       "keep *_hltL25TauLeadingTrackPtCutSelector_*_*",
       "keep *_hltL2MuonCandidatesNoVtx_*_*",
       "keep *_hltL2MuonCandidates_*_*",
       "keep *_hltL2MuonIsolations_*_*",
       "keep *_hltL2MuonSeeds_*_*",
       "keep *_hltL2Muons_*_*",
       "keep *_hltL2TauJets_*_*",
       "keep *_hltL2TauNarrowConeIsolationProducer_*_*",
       "keep *_hltL2TauRelaxingIsolationSelector_*_*",
       "keep *_hltL3MuonCandidatesNoVtx_*_*",
       "keep *_hltL3MuonCandidates_*_*",
       "keep *_hltL3MuonIsolations_*_*",
       "keep *_hltL3MuonsIOHit_*_*",
       "keep *_hltL3MuonsLinksCombination_*_*",
       "keep *_hltL3MuonsNoVtx_*_*",
       "keep *_hltL3MuonsOIHit_*_*",
       "keep *_hltL3MuonsOIState_*_*",
       "keep *_hltL3Muons_*_*",
       "keep *_hltL3TauConeIsolation_*_*",
       "keep *_hltL3TauCtfWithMaterialTracks_*_*",
       "keep *_hltL3TauIsolationSelector_*_*",
       "keep *_hltL3TauJetTracksAssociator_*_*",
       "keep *_hltL3TkFromL2OICombination_*_*",
       "keep *_hltL3TkTracksFromL2IOHit_*_*",
       "keep *_hltL3TkTracksFromL2OIHit_*_*",
       "keep *_hltL3TkTracksFromL2OIState_*_*",
       "keep *_hltL3TkTracksFromL2_*_*",
       "keep *_hltL3TrackCandidateFromL2IOHit_*_*",
       "keep *_hltL3TrackCandidateFromL2OIHit_*_*",
       "keep *_hltL3TrackCandidateFromL2OIState_*_*",
       "keep *_hltL3TrackCandidateFromL2_*_*",
       "keep *_hltL3TrajSeedIOHit_*_*",
       "keep *_hltL3TrajSeedOIHit_*_*",
       "keep *_hltL3TrajSeedOIState_*_*",
       "keep *_hltL3TrajectorySeedNoVtx_*_*",
       "keep *_hltL3TrajectorySeed_*_*",
       "keep *_hltMet_*_*",
       "keep *_hltMuTrackJpsiCtfTrackCands_*_*",
       "keep *_hltMuTrackJpsiCtfTracks_*_*",
       "keep *_hltMuTrackJpsiPixelTrackCands_*_*",
       "keep *_hltMuTrackJpsiPixelTrackSelector_*_*",
       "keep *_hltMuTrackJpsiTrackSeeds_*_*",
       "keep *_hltMuonRPCDigis_*_*",
       "keep *_hltOfflineBeamSpot_*_*",
       "keep *_hltPixelMatchElectronsL1Iso_*_*",
       "keep *_hltPixelMatchElectronsL1NonIso_*_*",
       "keep *_hltPixelMatchLargeWindowElectronsL1Iso_*_*",
       "keep *_hltPixelMatchLargeWindowElectronsL1NonIso_*_*",
       "keep *_hltPixelTracks_*_*",
       "keep *_hltPixelVertices_*_*",
       "keep *_hltRpcRecHits_*_*",
       "keep *_hltSiPixelRecHits_*_*",
       "keep *_hltSiStripClusters_*_*",
       "keep *_hltSiStripRawToClustersFacility_*_*",
       "keep *_hltTowerMakerForAll_*_*",
       "keep *_hltTowerMakerForMuons_*_*",
       "keep FEDRawDataCollection_rawDataCollector_*_*",
       "keep FEDRawDataCollection_source_*_*",
       "keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*",
       "keep edmTriggerResults_*_*_*",
       "keep triggerTriggerEventWithRefs_*_*_*",
       "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputNanoDST = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring( "HLT_Physics_NanoDST_v1" )
    ),
    outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*",
       "keep *_hltFEDSelector_*_*",
       "keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*",
       "keep L1MuGMTReadoutCollection_hltGtDigis_*_*",
       "keep edmTriggerResults_*_*_*" )
)
process.hltOutputOnlineErrors = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring( "HLT_DTErrors_v1",
         "HLT_LogMonitor_v1" )
    ),
    outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*",
       "keep *_hltL1GtObjectMap_*_*",
       "keep FEDRawDataCollection_rawDataCollector_*_*",
       "keep FEDRawDataCollection_source_*_*",
       "keep edmTriggerResults_*_*_*",
       "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputRPCMON = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring( "AlCa_RPCMuonNoHits_v2",
         "AlCa_RPCMuonNoTriggers_v2",
         "AlCa_RPCMuonNormalisation_v2" )
    ),
    outputCommands = cms.untracked.vstring( "drop *",
       "keep *_hltCscSegments_*_*",
       "keep *_hltDt4DSegments_*_*",
       "keep *_hltMuonCSCDigis_*_*",
       "keep *_hltMuonDTDigis_*_*",
       "keep *_hltMuonRPCDigis_*_*",
       "keep *_hltRpcRecHits_*_*",
       "keep L1GlobalTriggerReadoutRecord_*_*_*",
       "keep L1MuGMTCands_hltGtDigis_*_*",
       "keep L1MuGMTReadoutCollection_hltGtDigis_*_*",
       "keep edmTriggerResults_*_*_*",
       "keep triggerTriggerEvent_*_*_*" )
)

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtDigis + process.hltGctDigis + process.hltL1GtObjectMap + process.hltL1extraParticles )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot + process.hltOfflineBeamSpot )
process.HLTBeginSequenceBPTX = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.hltBPTXCoincidence + process.HLTBeamSpot )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )
process.HLTDoLocalHcalSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhereco + process.hltHfreco + process.hltHoreco )
process.HLTDoCaloSequence = cms.Sequence( process.hltEcalRawToRecHitFacility + process.hltEcalRegionalRestFEDs + process.hltEcalRecHitAll + process.HLTDoLocalHcalSequence + process.hltTowerMakerForAll )
process.HLTRecoJetSequenceAK5Uncorrected = cms.Sequence( process.HLTDoCaloSequence + process.hltAntiKT5CaloJets )
process.HLTRecoJetSequenceAK5Corrected = cms.Sequence( process.HLTRecoJetSequenceAK5Uncorrected + process.hltAntiKT5L2L3CorrCaloJets + process.hltJetIDPassedCorrJets )
process.HLTDoRegionalJetEcalSequence = cms.Sequence( process.hltEcalRawToRecHitFacility + process.hltEcalRegionalJetsFEDs + process.hltEcalRegionalJetsRecHit )
process.HLTRegionalTowerMakerForJetsSequence = cms.Sequence( process.HLTDoRegionalJetEcalSequence + process.HLTDoLocalHcalSequence )
process.HLTRegionalRecoJetSequenceAK5Corrected = cms.Sequence( process.HLTRegionalTowerMakerForJetsSequence )
process.HLTRecoMETSequence = cms.Sequence( process.HLTDoCaloSequence )
process.HLTRecoJetSequencePrePF = cms.Sequence( process.HLTRecoJetSequenceAK5Uncorrected )
process.HLTDoLocalPixelSequence = cms.Sequence( process.hltSiPixelDigis + process.hltSiPixelClusters + process.hltSiPixelRecHits )
process.HLTRecopixelvertexingSequence = cms.Sequence( process.hltPixelTracks + process.hltPixelVertices )
process.HLTDoLocalStripSequence = cms.Sequence( process.hltSiStripRawToClustersFacility + process.hltSiStripClusters )
process.HLTTrackReconstructionForJets = cms.Sequence( process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingSequence + process.HLTDoLocalStripSequence + process.hltPFJetPixelSeeds + process.hltPFJetCkfTrackCandidates + process.hltPFJetCtfWithMaterialTracks + process.hltPFlowTrackSelectionHighPurity )
process.HLTPreshowerSequence = cms.Sequence( process.hltESRawToRecHitFacility + process.hltEcalRegionalESRestFEDs + process.hltESRecHitAll )
process.HLTParticleFlowSequence = cms.Sequence( process.HLTPreshowerSequence + process.hltParticleFlowRecHitECAL + process.hltParticleFlowRecHitHCAL + process.hltParticleFlowRecHitPS + process.hltParticleFlowClusterECAL + process.hltParticleFlowClusterHCAL + process.hltParticleFlowClusterHFEM + process.hltParticleFlowClusterHFHAD + process.hltParticleFlowClusterPS + process.hltLightPFTracks + process.hltParticleFlowBlock + process.hltParticleFlow )
process.HLTPFJetsSequence = cms.Sequence( process.hltAntiKT5PFJets + process.hltAntiKT5ConvPFJets )
process.HLTPFTauTightIsoSequence = cms.Sequence( process.hltPFTauJetTracksAssociator + process.hltPFTauTagInfo + process.hltPFTausTightIso + process.hltPFTauTightIsoTrackFindingDiscriminator + process.hltPFTauTightIsoTrackPt5Discriminator + process.hltPFTauTightIsoIsolationDiscriminator + process.hltSelectedPFTausTightIsoTrackFinding + process.hltSelectedPFTausTightIsoTrackPt5 + process.hltSelectedPFTausTightIsoTrackFindingIsolation + process.hltSelectedPFTausTightIsoTrackPt5Isolation + process.hltConvPFTausTightIsoTrackFinding + process.hltConvPFTausTightIsoTrackFindingIsolation + process.hltConvPFTausTightIso + process.hltConvPFTausTightIsoTrackPt5 + process.hltConvPFTausTightIsoTrackPt5Isolation )
process.HLTBTagIPSequenceL25 = cms.Sequence( process.HLTDoLocalPixelSequence )
process.HLTBTagIPSequenceL3 = cms.Sequence( process.HLTDoLocalPixelSequence )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence )
process.HLTStoppedHSCPJetSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhereco + process.hltStoppedHSCPTowerMakerForAll + process.hltStoppedHSCPIterativeCone5CaloJets )
process.HLTBeginSequenceAntiBPTX = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence )
process.HLTDoJet40HTRecoSequence = cms.Sequence( process.hltJet40Ht )
process.HLTRSequence = cms.Sequence( process.HLTRecoJetSequenceAK5Corrected )
process.HLTmuonlocalrecoSequence = cms.Sequence( process.hltMuonDTDigis + process.hltDt1DRecHits + process.hltDt4DSegments + process.hltMuonCSCDigis + process.hltCsc2DRecHits + process.hltCscSegments + process.hltMuonRPCDigis + process.hltRpcRecHits )
process.HLTL2muonrecoNocandSequence = cms.Sequence( process.HLTmuonlocalrecoSequence + process.hltL2MuonSeeds + process.hltL2Muons )
process.HLTL2muonrecoSequenceNoVtx = cms.Sequence( process.HLTL2muonrecoNocandSequence + process.hltL2MuonCandidatesNoVtx )
process.HLTL2muonrecoSequence = cms.Sequence( process.HLTL2muonrecoNocandSequence )
process.HLTL3muonTkCandidateSequence = cms.Sequence( process.HLTDoLocalPixelSequence )
process.HLTL3muonrecoNocandSequence = cms.Sequence( process.HLTL3muonTkCandidateSequence )
process.HLTL3muonrecoSequence = cms.Sequence( process.HLTL3muonrecoNocandSequence )
process.HLTL2muonisorecoSequence = cms.Sequence( process.hltEcalRawToRecHitFacility + process.hltEcalRegionalMuonsFEDs + process.hltEcalRegionalMuonsRecHit + process.HLTDoLocalHcalSequence )
process.HLTL3muonisorecoSequence = cms.Sequence( process.hltPixelTracks + process.hltL3MuonIsolations )
process.HLTMuTrackJpsiPixelRecoSequence = cms.Sequence( process.HLTDoLocalPixelSequence )
process.HLTMuTrackJpsiTrackRecoSequence = cms.Sequence( process.HLTDoLocalStripSequence )
process.HLTMuTkMuJpsiTkMuRecoSequence = cms.Sequence( process.hltMuTkMuJpsiTrackerMuons + process.hltMuTkMuJpsiTrackerMuonCands )
process.HLTDoRegionalEgammaEcalSequence = cms.Sequence( process.hltESRawToRecHitFacility + process.hltEcalRawToRecHitFacility + process.hltEcalRegionalEgammaFEDs + process.hltEcalRegionalEgammaRecHit + process.hltESRegionalEgammaRecHit )
process.HLTMulti5x5SuperClusterL1Isolated = cms.Sequence( process.hltMulti5x5BasicClustersL1Isolated + process.hltMulti5x5SuperClustersL1Isolated + process.hltMulti5x5EndcapSuperClustersWithPreshowerL1Isolated + process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated )
process.HLTL1IsolatedEcalClustersSequence = cms.Sequence( process.hltHybridSuperClustersL1Isolated + process.hltCorrectedHybridSuperClustersL1Isolated + process.HLTMulti5x5SuperClusterL1Isolated )
process.HLTMulti5x5SuperClusterL1NonIsolated = cms.Sequence( process.hltMulti5x5BasicClustersL1NonIsolated + process.hltMulti5x5SuperClustersL1NonIsolated + process.hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated + process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedTemp + process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated )
process.HLTL1NonIsolatedEcalClustersSequence = cms.Sequence( process.hltHybridSuperClustersL1NonIsolated + process.hltCorrectedHybridSuperClustersL1NonIsolatedTemp + process.hltCorrectedHybridSuperClustersL1NonIsolated + process.HLTMulti5x5SuperClusterL1NonIsolated )
process.HLTEgammaR9ShapeSequence = cms.Sequence( process.hltL1IsoR9shape + process.hltL1NonIsoR9shape )
process.HLTDoLocalHcalWithoutHOSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhereco + process.hltHfreco )
process.HLTPhoton30CaloIdVLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltEGRegionalL1SingleEG15 + process.hltEG30EtFilter + process.HLTEgammaR9ShapeSequence + process.hltEG30R9ShapeFilter + process.hltL1IsoHLTClusterShape + process.hltL1NonIsoHLTClusterShape + process.hltEG30CaloIdVLClusterShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltEG30CaloIdVLHEFilter )
process.HLTPhoton30CaloIdVLIsoLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTL1IsoEgammaRegionalRecoTrackerSequence = cms.Sequence( process.hltL1IsoEgammaRegionalPixelSeedGenerator + process.hltL1IsoEgammaRegionalCkfTrackCandidates + process.hltL1IsoEgammaRegionalCTFFinalFitWithMaterial )
process.HLTL1NonIsoEgammaRegionalRecoTrackerSequence = cms.Sequence( process.hltL1NonIsoEgammaRegionalPixelSeedGenerator + process.hltL1NonIsoEgammaRegionalCkfTrackCandidates + process.hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial )
process.HLTPhoton75CaloIdVLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTPhoton75CaloIdVLIsoLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTSinglePhoton125L1NonIsolatedHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTDoublePhoton5IsoVLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTDoublePhoton33Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTEcalActivitySequence = cms.Sequence( process.hltEcalRawToRecHitFacility + process.hltESRawToRecHitFacility + process.hltEcalRegionalRestFEDs + process.hltEcalRegionalESRestFEDs + process.hltEcalRecHitAll + process.hltESRecHitAll + process.hltHybridSuperClustersActivity + process.hltCorrectedHybridSuperClustersActivity + process.hltMulti5x5BasicClustersActivity + process.hltMulti5x5SuperClustersActivity + process.hltMulti5x5SuperClustersWithPreshowerActivity + process.hltCorrectedMulti5x5SuperClustersWithPreshowerActivity + process.hltRecoEcalSuperClusterActivityCandidate + process.hltEcalActivitySuperClusterWrapper )
process.HLTEle8Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTEle8CaloIdLCaloIsoVLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTEle8CaloIdLTrkIdVLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTPixelMatchElectronL1IsoTrackingSequence = cms.Sequence( process.hltCkfL1IsoTrackCandidates + process.hltCtfL1IsoWithMaterialTracks + process.hltPixelMatchElectronsL1Iso )
process.HLTPixelMatchElectronL1NonIsoTrackingSequence = cms.Sequence( process.hltCkfL1NonIsoTrackCandidates + process.hltCtfL1NonIsoWithMaterialTracks + process.hltPixelMatchElectronsL1NonIso )
process.HLTDoElectronDetaDphiSequence = cms.Sequence( process.hltElectronL1IsoDetaDphi + process.hltElectronL1NonIsoDetaDphi )
process.HLTEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTEle17CaloIdLCaloIsoVLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTEle27CaloIdTCaloIsoTTrkIdTTrkIsoTSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTEle45CaloIdVTTrkIdTSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTEle90NoSpikeFilterSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTPhoton20R9IdPhoton18R9IdSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTEgammaR9IDSequence = cms.Sequence( process.hltL1IsoR9ID + process.hltL1NonIsoR9ID )
process.HLTPhoton20CaloIdVTIsoTSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTEle8CaloIdLCaloIsoVLNoL1SeedSequence = cms.Sequence( process.HLTEcalActivitySequence )
process.HLTPhoton26Photon18Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTPhoton26IsoVLPhoton18Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTPhoton26IsoVLPhoton18IsoVLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTEcalActivityEgammaRegionalRecoTrackerSequence = cms.Sequence( process.hltEcalActivityEgammaRegionalPixelSeedGenerator + process.hltEcalActivityEgammaRegionalCkfTrackCandidates + process.hltEcalActivityEgammaRegionalCTFFinalFitWithMaterial )
process.HLTPhoton26CaloIdLIsoVLPhoton18Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTPhoton26CaloIdLIsoVLPhoton18CaloIdLIsoVLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTPhoton32CaloIdLPhoton26CaloIdLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTSinglePhoton60CaloIdLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTSinglePhoton70CaloIdLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTEle17CaloIdIsoEle8CaloIdIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8Mass30Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTSingleElectronEt17CaloIdIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTHFEM15Sequence = cms.Sequence( process.hltHFEMClusters + process.hltHFRecoEcalCandidate + process.hltHFEMFilter )
process.HLTEle32CaloIdLCaloIsoVLSC17Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTCaloTausCreatorRegionalSequence = cms.Sequence( process.HLTDoRegionalJetEcalSequence )
process.HLTL2TauJetsSequence = cms.Sequence( process.HLTCaloTausCreatorRegionalSequence )
process.HLTBTagMuSequenceL25 = cms.Sequence( process.HLTL2muonrecoNocandSequence )
process.HLTBTagMu5SelSequenceL3 = cms.Sequence( process.HLTL3muonrecoNocandSequence )
process.HLTBTagMu7SelSequenceL3 = cms.Sequence( process.HLTL3muonrecoNocandSequence )
process.HLTBTagMu9SelSequenceL3 = cms.Sequence( process.HLTL3muonrecoNocandSequence )
process.HLTPixelMatchElectronActivityTrackingSequence = cms.Sequence( process.hltCkfActivityTrackCandidates + process.hltCtfActivityWithMaterialTracks + process.hltPixelMatchElectronsActivity )
process.HLTMu5Ele8CaloIdLTrkIdVLEle8L1NonIsoHLTnonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTDoEgammaClusterShapeSequence = cms.Sequence( process.hltL1IsoHLTClusterShape + process.hltL1NonIsoHLTClusterShape )
process.HLTMu5DoubleEle8L1NonIsoHLTnonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTDoEGammaStartupSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTDoEGammaHESequence = cms.Sequence( process.HLTDoLocalHcalWithoutHOSequence )
process.HLTDoEGammaPixelSequence = cms.Sequence( process.HLTDoLocalPixelSequence )
process.HLTPhoton20CaloIdVTIsoTMu8Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTPFJetTriggerSequence = cms.Sequence( process.HLTTrackReconstructionForJets )
process.HLTPFTauSequence = cms.Sequence( process.hltPFTauJetTracksAssociator + process.hltPFTauTagInfo + process.hltPFTaus + process.hltPFTauTrackFindingDiscriminator + process.hltPFTauTrackPt5Discriminator + process.hltPFTauLooseIsolationDiscriminator + process.hltPFTauIsolationDiscriminator + process.hltSelectedPFTausTrackFinding + process.hltSelectedPFTausTrackPt5 + process.hltSelectedPFTausTrackFindingIsolation + process.hltSelectedPFTausTrackFindingLooseIsolation + process.hltSelectedPFTausTrackPt5Isolation + process.hltConvPFTausTrackFinding + process.hltConvPFTausTrackFindingIsolation + process.hltConvPFTausTrackFindingLooseIsolation + process.hltConvPFTaus + process.hltConvPFTausTrackPt5 + process.hltConvPFTausTrackPt5Isolation )
process.HLTBTagIPSequenceL25SingleTop = cms.Sequence( process.HLTDoLocalPixelSequence )
process.HLTBTagIPSequenceL3SingleTop = cms.Sequence( process.HLTDoLocalPixelSequence )
process.HLTDoubleMu5Ele8L1NonIsoHLTnonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTDoubleMu5Ele8L1NonIsoHLTCaloIdLTrkIdVLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTSingleElectronEt10HT200L1NonIsoHLTCaloIdLTrkIdVLCaloIsolVLTrkIsolVLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTSingleElectronEt10HT200L1NonIsoHLTCaloIdTTrkIdTCaloIsolVLTrkIsolVLSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTEle15CaloIdVTTrkIdTSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTEle25CaloIdVTCaloTrkIdSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTBTagIPSequenceL25EleJetSingleTop = cms.Sequence( process.HLTDoLocalPixelSequence )
process.HLTBTagIPSequenceL3EleJetSingleTop = cms.Sequence( process.HLTDoLocalPixelSequence )
process.HLTDoubleEle8HTT50L1NonIsoHLTCaloIdLSequence = cms.Sequence( process.HLTDoEGammaStartupSequence )
process.HLTDoubleEle8HTT50L1NonIsoHLTCaloIdTSequence = cms.Sequence( process.HLTDoEGammaStartupSequence )
process.HLTTripleElectronEt10L1NonIsoHLTNonIsoSequence = cms.Sequence( process.HLTDoEGammaStartupSequence )
process.HLTPhoton20EBOnlyNoSpikeFilterSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTPhoton20NoSpikeFilterSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTSpike20Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence )
process.HLTRecopixelvertexingForHighMultSequence = cms.Sequence( process.hltPixelTracksForHighMult + process.hltPixelVerticesForHighMult )
process.HLTBeginSequenceNZS = cms.Sequence( process.hltTriggerType + process.hltL1EventNumberNZS + process.HLTL1UnpackerSequence )
process.HLTBeginSequenceCalibration = cms.Sequence( process.hltCalibrationEventsFilter + process.hltGtDigis )
process.HLTBeginSequenceRandom = cms.Sequence( process.hltRandomEventsFilter + process.hltGtDigis )
process.HLTDoRegionalPi0EtaSequence = cms.Sequence( process.hltESRawToRecHitFacility + process.hltEcalRawToRecHitFacility + process.hltEcalRegionalPi0EtaFEDs + process.hltESRegionalPi0EtaRecHit + process.hltEcalRegionalPi0EtaRecHit )

process.HLT_L1SingleJet36_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet36 + process.hltPreL1SingleJet36 + process.HLTEndSequence )
process.HLT_Jet30_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet16 + process.hltPreJet30 + process.hltSingleJet30 + process.HLTRecoJetSequenceAK5Corrected + process.HLTEndSequence )
process.HLT_Jet60_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet36 + process.hltPreJet60 + process.HLTRegionalRecoJetSequenceAK5Corrected + process.hltSingleJet60Regional + process.HLTEndSequence )
process.HLT_Jet80_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet52 + process.hltPreJet80 + process.hltSingleJet80Regional + process.HLTRegionalRecoJetSequenceAK5Corrected + process.HLTEndSequence )
process.HLT_Jet110_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet68 + process.hltPreJet110 + process.HLTRegionalRecoJetSequenceAK5Corrected + process.hltSingleJet110Regional + process.HLTEndSequence )
process.HLT_Jet150_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet92 + process.hltPreJet150 + process.HLTRegionalRecoJetSequenceAK5Corrected + process.hltSingleJet150Regional + process.HLTEndSequence )
process.HLT_Jet190_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet92 + process.hltPreJet190 + process.hltSingleJet190Regional + process.HLTRegionalRecoJetSequenceAK5Corrected + process.HLTEndSequence )
process.HLT_Jet240_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet92 + process.hltPreJet240 + process.HLTRegionalRecoJetSequenceAK5Corrected + process.hltSingleJet240Regional + process.HLTEndSequence )
process.HLT_Jet370_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet92 + process.hltPreJet370 + process.HLTRegionalRecoJetSequenceAK5Corrected + process.hltSingleJet370Regional + process.HLTEndSequence )
process.HLT_Jet370_NoJetID_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet92 + process.hltPreJet370NoJetID + process.hltAntiKT5CaloJetsRegional + process.HLTRegionalTowerMakerForJetsSequence + process.hltAntiKT5L2L3CorrCaloJetsRegional + process.hltL1MatchedJetsRegional + process.hltSingleJet370RegionalNoJetID + process.HLTEndSequence )
process.HLT_DiJetAve15U_v4 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet16 + process.hltPreDiJetAve15U + process.HLTRecoJetSequenceAK5Uncorrected + process.hltJetIDPassedAK5Jets + process.hltDiJetAve15U + process.HLTEndSequence )
process.HLT_DiJetAve30U_v4 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet36 + process.hltPreDiJetAve30U + process.hltJetIDPassedAK5Jets + process.HLTRecoJetSequenceAK5Uncorrected + process.hltDiJetAve30U + process.HLTEndSequence )
process.HLT_DiJetAve50U_v4 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet52 + process.hltPreDiJetAve50U + process.HLTRecoJetSequenceAK5Uncorrected + process.hltJetIDPassedAK5Jets + process.hltDiJetAve50U + process.HLTEndSequence )
process.HLT_DiJetAve70U_v4 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet68 + process.hltPreDiJetAve70U + process.hltJetIDPassedAK5Jets + process.HLTRecoJetSequenceAK5Uncorrected + process.hltDiJetAve70U + process.HLTEndSequence )
process.HLT_DiJetAve100U_v4 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet92 + process.hltPreDiJetAve100U + process.HLTRecoJetSequenceAK5Uncorrected + process.hltJetIDPassedAK5Jets + process.hltDiJetAve100U + process.HLTEndSequence )
process.HLT_DiJetAve140U_v4 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet92 + process.hltPreDiJetAve140U + process.HLTRecoJetSequenceAK5Uncorrected + process.hltJetIDPassedAK5Jets + process.hltDiJetAve140U + process.HLTEndSequence )
process.HLT_DiJetAve180U_v4 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet92 + process.hltPreDiJetAve180U + process.hltJetIDPassedAK5Jets + process.HLTRecoJetSequenceAK5Uncorrected + process.hltDiJetAve180U + process.HLTEndSequence )
process.HLT_DiJetAve300U_v4 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet92 + process.hltPreDiJetAve300U + process.HLTRecoJetSequenceAK5Uncorrected + process.hltJetIDPassedAK5Jets + process.hltDiJetAve300U + process.HLTEndSequence )
process.HLT_DoubleJet30_ForwardBackward_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleForJet20EtaOpp + process.hltPreDoubleJet30ForwardBackward + process.HLTRecoJetSequenceAK5Corrected + process.hltDoubleJet30ForwardBackward + process.HLTEndSequence )
process.HLT_DoubleJet60_ForwardBackward_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleForJet20EtaOpp + process.hltPreDoubleJet60ForwardBackward + process.hltDoubleJet60ForwardBackward + process.HLTRecoJetSequenceAK5Corrected + process.HLTEndSequence )
process.HLT_DoubleJet70_ForwardBackward_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleForJet20EtaOpp + process.hltPreDoubleJet70ForwardBackward + process.HLTRecoJetSequenceAK5Corrected + process.hltDoubleJet70ForwardBackward + process.HLTEndSequence )
process.HLT_DoubleJet80_ForwardBackward_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleForJet36EtaOpp + process.hltPreDoubleJet80ForwardBackward + process.hltDoubleJet80ForwardBackward + process.HLTRecoJetSequenceAK5Corrected + process.HLTEndSequence )
process.HLT_CentralJet80_MET65_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet52 + process.hltPreCenJet80MET65 + process.HLTRegionalRecoJetSequenceAK5Corrected + process.hltCenJet80CentralRegional + process.HLTRecoMETSequence + process.hltMET65 + process.HLTEndSequence )
process.HLT_CentralJet80_MET80_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet52 + process.hltPreCenJet80MET80 + process.hltCenJet80CentralRegional + process.HLTRegionalRecoJetSequenceAK5Corrected + process.hltMET80 + process.HLTRecoMETSequence + process.HLTEndSequence )
process.HLT_CentralJet80_MET100_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet52 + process.hltPreCenJet80MET100 + process.hltCenJet80CentralRegional + process.HLTRegionalRecoJetSequenceAK5Corrected + process.hltMET100 + process.HLTRecoMETSequence + process.HLTEndSequence )
process.HLT_CentralJet80_MET160_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet52 + process.hltPreCenJet80MET160 + process.hltCenJet80CentralRegional + process.HLTRegionalRecoJetSequenceAK5Corrected + process.hltMET160 + process.HLTRecoMETSequence + process.HLTEndSequence )
process.HLT_DiJet60_MET45_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1ETM20 + process.hltPreDiJet60MET45 + process.HLTRecoJetSequenceAK5Corrected + process.hltDiJet60 + process.hltMet45 + process.HLTRecoMETSequence + process.HLTEndSequence )
process.HLT_DiJet70_PT70_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet36 + process.hltPreDiJet70PT70 + process.HLTRecoJetSequenceAK5Corrected + process.hltDijet70PT70 + process.HLTEndSequence )
process.HLT_DiJet100_PT100_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet52 + process.hltPreDiJet100PT100 + process.hltDijet100PT100 + process.HLTRecoJetSequenceAK5Corrected + process.HLTEndSequence )
process.HLT_DiJet130_PT130_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet52 + process.hltPreDiJet130PT130 + process.HLTRecoJetSequenceAK5Corrected + process.hltDijet130PT130 + process.HLTEndSequence )
process.HLT_QuadJet40_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1QuadJet20Central + process.hltPreQuadJet40 + process.HLTRecoJetSequenceAK5Corrected + process.hltQuadJet40Central + process.HLTEndSequence )
process.HLT_QuadJet40_IsoPFTau40_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1QuadJet20Central + process.hltPreQuadJet40IsoPFTau40 + process.HLTRecoJetSequenceAK5Corrected + process.hltQuadJet40IsoPFTau40 + process.HLTRecoJetSequencePrePF + process.HLTTrackReconstructionForJets + process.HLTParticleFlowSequence + process.HLTPFJetsSequence + process.HLTPFTauTightIsoSequence + process.hltPFTau5Track + process.hltPFTau5Track5 + process.hltFilterPFTauTrack5TightIsoL1QuadJet20Central + process.hltFilterPFTauTrack5TightIsoL1QuadJet20CentralPFTau40 + process.HLTEndSequence )
process.HLT_QuadJet50_BTagIP_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1QuadJet20Central + process.hltPreQuadJet50 + process.hltQuadJet50Central + process.HLTRecoJetSequenceAK5Corrected + process.hltBLifetimeL25Filter + process.HLTBTagIPSequenceL25 + process.hltBLifetimeL3Filter + process.HLTBTagIPSequenceL3 + process.HLTEndSequence )
process.HLT_QuadJet50_Jet40_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1QuadJet20Central + process.hltPreQuadJet50Jet40 + process.HLTRecoJetSequenceAK5Corrected + process.hltPentaJet40Central + process.hltQuadJet50Central + process.HLTEndSequence )
process.HLT_QuadJet60_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1QuadJet20Central + process.hltPreQuadJet60 + process.hltQuadJet60 + process.HLTRecoJetSequenceAK5Corrected + process.HLTEndSequence )
process.HLT_QuadJet70_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1QuadJet20Central + process.hltPreQuadJet70 + process.HLTRecoJetSequenceAK5Corrected + process.hltQuadJet70 + process.HLTEndSequence )
process.HLT_ExclDiJet60_HFOR_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet36 + process.hltPreExclDiJet60HFOR + process.HLTRecoJetSequenceAK5Corrected + process.hltExclDiJet60HFOR + process.HLTEndSequence )
process.HLT_ExclDiJet60_HFAND_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet36FwdVeto + process.hltPreExclDiJet60HFAND + process.hltExclDiJet60HFAND + process.HLTRecoJetSequenceAK5Corrected + process.HLTEndSequence )
process.HLT_JetE30_NoBPTX_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet20NoBPTX + process.hltPreJetE30NoBPTX + process.HLTStoppedHSCPJetSequence + process.hltStoppedHSCPControl1CaloJetEnergy30 + process.HLTEndSequence )
process.HLT_JetE30_NoBPTX_NoHalo_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet20NoBPTXNoHalo + process.hltL1BeamHaloAntiCoincidence3BX + process.hltPreJetE30NoBPTXNoHalo + process.HLTStoppedHSCPJetSequence + process.hltStoppedHSCPLoose1CaloJetEnergy30 + process.HLTEndSequence )
process.HLT_JetE30_NoBPTX3BX_NoHalo_v2 = cms.Path( process.HLTBeginSequenceAntiBPTX + process.hltL1sL1SingleJet20NoBPTXNoHalo + process.hltL1BeamHaloAntiCoincidence3BX + process.hltPreJetE30NoBPTX3BXNoHalo + process.HLTStoppedHSCPJetSequence + process.hltStoppedHSCPTight1CaloJetEnergy30 + process.HLTEndSequence )
process.HLT_HT160_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT50 + process.hltPreHT160 + process.HLTRecoJetSequenceAK5Corrected + process.hltHT160 + process.HLTDoJet40HTRecoSequence + process.HLTEndSequence )
process.HLT_HT240_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT50 + process.hltPreHT240 + process.hltHT240 + process.HLTRecoJetSequenceAK5Corrected + process.HLTDoJet40HTRecoSequence + process.HLTEndSequence )
process.HLT_HT260_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT100 + process.hltPreHT260 + process.HLTRecoJetSequenceAK5Corrected + process.hltHT260 + process.HLTEndSequence + process.HLTDoJet40HTRecoSequence )
process.HLT_HT260_MHT60_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT100 + process.hltPreHT260MHT60 + process.hltHT260 + process.HLTRecoJetSequenceAK5Corrected + process.HLTDoJet40HTRecoSequence + process.hltMHT60 + process.HLTEndSequence )
process.HLT_HT300_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT100 + process.hltPreHT300 + process.HLTRecoJetSequenceAK5Corrected + process.hltHT300 + process.HLTEndSequence + process.HLTDoJet40HTRecoSequence )
process.HLT_HT300_MHT75_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT100 + process.hltPreHT300MHT75 + process.HLTRecoJetSequenceAK5Corrected + process.HLTDoJet40HTRecoSequence + process.hltHT300 + process.hltMHT75 + process.HLTEndSequence )
process.HLT_HT360_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT100 + process.hltPreHT360 + process.hltHT360 + process.HLTRecoJetSequenceAK5Corrected + process.HLTDoJet40HTRecoSequence + process.HLTEndSequence )
process.HLT_HT440_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT100 + process.hltPreHT440 + process.HLTRecoJetSequenceAK5Corrected + process.hltHT440 + process.HLTDoJet40HTRecoSequence + process.HLTEndSequence )
process.HLT_HT520_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT100 + process.hltPreHT520 + process.hltHT520 + process.HLTRecoJetSequenceAK5Corrected + process.HLTDoJet40HTRecoSequence + process.HLTEndSequence )
process.HLT_PFMHT150_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1ETM30 + process.hltPrePFMHT150 + process.HLTRecoMETSequence + process.hltMET80 + process.HLTRecoJetSequencePrePF + process.HLTTrackReconstructionForJets + process.HLTParticleFlowSequence + process.hltPFMHT150Filter + process.HLTPFJetsSequence + process.HLTEndSequence )
process.HLT_MET100_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1ETM30 + process.hltPreMET100 + process.hltMET100 + process.HLTRecoMETSequence + process.HLTEndSequence )
process.HLT_MET120_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1ETM30 + process.hltPreMET120 + process.HLTRecoMETSequence + process.hltMET120 + process.HLTEndSequence )
process.HLT_MET200_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1ETM30 + process.hltPreMET200 + process.HLTRecoMETSequence + process.hltMET200 + process.HLTEndSequence )
process.HLT_Meff440_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT100 + process.hltPreMeff440 + process.hltMeff440 + process.HLTRecoJetSequenceAK5Corrected + process.HLTEndSequence )
process.HLT_Meff520_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT100 + process.hltPreMeff520 + process.HLTRecoJetSequenceAK5Corrected + process.hltMeff520 + process.HLTEndSequence )
process.HLT_Meff640_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT100 + process.hltPreMeff640 + process.HLTRecoJetSequenceAK5Corrected + process.hltMeff640 + process.HLTEndSequence )
process.HLT_MR100_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleJet36Central + process.hltPreMR100 + process.hltMR100 + process.HLTRSequence + process.HLTEndSequence )
process.HLT_R032_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleJet36Central + process.hltPreR032 + process.hltR032 + process.HLTRSequence + process.HLTEndSequence )
process.HLT_R032_MR100_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleJet36Central + process.hltPreR032MR100 + process.HLTRSequence + process.hltR032MR100 + process.HLTEndSequence )
process.HLT_R035_MR100_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleJet36Central + process.hltPreR035MR100 + process.HLTRSequence + process.hltR035MR100 + process.HLTEndSequence )
process.HLT_L1SingleMuOpen_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMuOpen + process.hltPreL1SingleMuOpen + process.hltL1MuOpenL1Filtered0 + process.HLTEndSequence )
process.HLT_L1SingleMuOpen_DT_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMuOpen + process.hltPreL1SingleMuOpenDT + process.hltL1MuOpenL1FilteredDT + process.HLTEndSequence )
process.HLT_L1SingleMu10_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu10 + process.hltPreL1Mu10 + process.hltL1SingleMu10L1Filtered0 + process.HLTEndSequence )
process.HLT_L1SingleMu20_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu20 + process.hltPreL1Mu20 + process.hltL1SingleMu20L1Filtered0 + process.HLTEndSequence )
process.HLT_L1DoubleMu0_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMu0 + process.hltPreL1DoubleMu0 + process.hltDiMuonL1Filtered0 + process.HLTEndSequence )
process.HLT_L2MuOpen_NoVertex_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleMuOpen + process.hltPreL2MuOpenNoVertex + process.hltSingleMuOpenL1Filtered + process.hltSingleL2MuOpenL2PreFilteredNoVtx + process.HLTL2muonrecoSequenceNoVtx + process.HLTEndSequence )
process.HLT_L2Mu10_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu10 + process.hltPreL2Mu10 + process.hltL1SingleMu10L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu10L2Filtered10 + process.HLTEndSequence )
process.HLT_L2Mu20_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu12 + process.hltPreL2Mu20 + process.hltL1SingleMu12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu20L2Filtered20 + process.HLTEndSequence )
process.HLT_L2DoubleMu0_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMu0 + process.hltPreL2DoubleMu0 + process.hltDiMuonL1Filtered0 + process.hltDiMuonL2PreFiltered0 + process.HLTL2muonrecoSequence + process.HLTEndSequence )
process.HLT_Mu3_v3 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMuOpen + process.hltPreMu3 + process.hltSingleMuOpenL1Filtered + process.HLTL2muonrecoSequence + process.hltSingleMu3L2Filtered0 + process.HLTL3muonrecoSequence + process.hltSingleMu3L3Filtered3 + process.HLTEndSequence )
process.HLT_Mu5_v3 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu3 + process.hltPreMu5 + process.hltL1SingleMu3L1Filtered0 + process.HLTL2muonrecoSequence + process.hltSingleMu5L2Filtered3 + process.hltSingleMu5L3Filtered5 + process.HLTL3muonrecoSequence + process.HLTEndSequence )
process.HLT_Mu8_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu3 + process.hltPreMu8 + process.hltL1SingleMu3L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu3L2Filtered3 + process.hltSingleMu8L3Filtered8 + process.HLTL3muonrecoSequence + process.HLTEndSequence )
process.HLT_Mu12_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu7 + process.hltPreMu12 + process.hltL1SingleMu7L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu7L2Filtered7 + process.hltSingleMu12L3Filtered12 + process.HLTL3muonrecoSequence + process.HLTEndSequence )
process.HLT_Mu15_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu10 + process.hltPreMu15 + process.hltL1SingleMu10L1Filtered0 + process.hltL2Mu10L2Filtered10 + process.HLTL2muonrecoSequence + process.hltL3Muon15 + process.HLTL3muonrecoSequence + process.HLTEndSequence )
process.HLT_Mu20_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu12 + process.hltPreMu20 + process.hltL1SingleMu12L1Filtered0 + process.hltSingleMu12L2Filtered12 + process.HLTL2muonrecoSequence + process.hltSingleMu20L3Filtered20 + process.HLTL3muonrecoSequence + process.HLTEndSequence )
process.HLT_Mu24_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu12 + process.hltPreMu24 + process.hltL1SingleMu12L1Filtered0 + process.hltL2Mu12L2Filtered12 + process.HLTL2muonrecoSequence + process.hltSingleMu24L3Filtered24 + process.HLTL3muonrecoSequence + process.HLTEndSequence )
process.HLT_Mu30_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu12 + process.hltPreMu30 + process.hltL1SingleMu12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu12L2Filtered12 + process.HLTL3muonrecoSequence + process.hltSingleMu30L3Filtered30 + process.HLTEndSequence )
process.HLT_IsoMu12_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu7 + process.hltPreIsoMu12 + process.hltL1SingleMu7L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu7L2Filtered7 + process.HLTL2muonisorecoSequence + process.hltSingleMuIsoL2IsoFiltered7 + process.hltSingleMuIsoL3PreFiltered12 + process.hltSingleMuIsoL3IsoFiltered12 + process.HLTL3muonrecoSequence + process.HLTL3muonisorecoSequence + process.HLTEndSequence )
process.HLT_IsoMu15_v5 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu10 + process.hltPreIsoMu15 + process.hltL1SingleMu10L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu10L2Filtered10 + process.HLTL2muonisorecoSequence + process.hltSingleMuIsoL2IsoFiltered10 + process.HLTL3muonrecoSequence + process.hltSingleMuIsoL3PreFiltered15 + process.HLTL3muonisorecoSequence + process.hltSingleMuIsoL3IsoFiltered15 + process.HLTEndSequence )
process.HLT_IsoMu17_v5 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu10 + process.hltPreIsoMu17 + process.hltL1SingleMu10L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu10L2Filtered10 + process.HLTL2muonisorecoSequence + process.hltSingleMuIsoL2IsoFiltered10 + process.HLTL3muonrecoSequence + process.hltSingleMuIsoL3PreFiltered17 + process.HLTL3muonisorecoSequence + process.hltSingleMuIsoL3IsoFiltered17 + process.HLTEndSequence )
process.HLT_IsoMu24_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu12 + process.hltPreIsoMu24 + process.hltL1SingleMu12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu12L2Filtered12 + process.hltSingleMuIsoL2IsoFiltered12 + process.hltSingleMuIsoL3PreFiltered24 + process.HLTL2muonisorecoSequence + process.hltSingleMuIsoL3IsoFiltered24 + process.HLTL3muonrecoSequence + process.HLTL3muonisorecoSequence + process.HLTEndSequence )
process.HLT_IsoMu30_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu12 + process.hltPreIsoMu30 + process.hltL1SingleMu12L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu12L2Filtered12 + process.HLTL2muonisorecoSequence + process.hltSingleMuIsoL2IsoFiltered12 + process.HLTL3muonrecoSequence + process.hltSingleMuIsoL3PreFiltered30 + process.HLTL3muonisorecoSequence + process.hltSingleMuIsoL3IsoFiltered30 + process.HLTEndSequence )
process.HLT_L2DoubleMu35_NoVertex_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMu3 + process.hltPreL2DoubleMu35NoVertex + process.hltL1DoubleMuon3L1Filtered0 + process.hltL2DoubleMu35NoVertexL2PreFiltered + process.HLTL2muonrecoSequenceNoVtx + process.HLTEndSequence )
process.HLT_DoubleMu3_v3 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMu0 + process.hltPreDoubleMu3 + process.hltDiMuonL1Filtered0 + process.HLTL2muonrecoSequence + process.hltDiMuonL2PreFiltered0 + process.hltDiMuonL3PreFiltered3 + process.HLTL3muonrecoSequence + process.HLTEndSequence )
process.HLT_DoubleMu6_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMu3 + process.hltPreDoubleMu6 + process.hltL1DoubleMuon3L1Filtered0 + process.HLTL2muonrecoSequence + process.hltDiMuon3L2PreFiltered0 + process.hltDiMuonL3PreFiltered6 + process.HLTL3muonrecoSequence + process.HLTEndSequence )
process.HLT_DoubleMu7_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMu3 + process.hltPreDoubleMu7 + process.hltL1DoubleMuon3L1Filtered0 + process.HLTL2muonrecoSequence + process.hltDiMuon3L2PreFiltered0 + process.hltDiMuonL3PreFiltered7 + process.HLTL3muonrecoSequence + process.HLTEndSequence )
process.HLT_DoubleMu3_Bs_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMu0 + process.hltPreDoubleMu0Bs + process.hltDiMuonL1Filtered0 + process.hltDiMuonL2PreFiltered2 + process.HLTL2muonrecoSequence + process.hltDiMuonL3PreFiltered3Onia + process.HLTL3muonrecoSequence + process.hltDoubleMu3BsL3Filtered + process.HLTEndSequence )
process.HLT_DoubleMu3_Jpsi_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMu0 + process.hltPreDoubleMu0Jpsi + process.hltDiMuonL1Filtered0 + process.hltDiMuonL2PreFiltered2 + process.HLTL2muonrecoSequence + process.hltDiMuonL3PreFiltered3Onia + process.HLTL3muonrecoSequence + process.hltDoubleMu3JpsiL3Filtered + process.HLTEndSequence )
process.HLT_DoubleMu3_Quarkonium_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMu0 + process.hltPreDoubleMu0Quarkonium + process.hltDiMuonL1Filtered0 + process.HLTL2muonrecoSequence + process.hltDiMuonL2PreFiltered2 + process.HLTL3muonrecoSequence + process.hltDiMuonL3PreFiltered3Onia + process.hltDoubleMu3QuarkoniumL3Filtered + process.HLTEndSequence )
process.HLT_DoubleMu4_Acoplanarity03_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMu3 + process.hltPreDoubleMu4Excl + process.hltL1DoubleMuon3L1Filtered3 + process.HLTL2muonrecoSequence + process.hltL2DoubleMu3L2Filtered + process.hltDiMuonL3PreFiltered4 + process.hltDoubleMu4ExclL3PreFiltered + process.HLTL3muonrecoSequence + process.HLTEndSequence )
process.HLT_TripleMu5_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMu3 + process.hltPreTripleMu3 + process.hltL1DoubleMu3L1TriMuFiltered3 + process.hltL1DoubleMu3L2TriMuFiltered3 + process.HLTL2muonrecoSequence + process.hltL1DoubleMu3L3TriMuFiltered5 + process.HLTL3muonrecoSequence + process.HLTEndSequence )
process.HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu5BQ7 + process.hltPreMu5TkMu0JpsiTightB5Q7 + process.hltMu5TrackJpsiL1Filtered0Eta15 + process.hltMu5TrackJpsiL2Filtered5Eta15 + process.HLTL2muonrecoSequence + process.hltMu5TrackJpsiL3Filtered5Eta15 + process.HLTL3muonrecoSequence + process.hltMu5TrackJpsiPixelMassFilteredEta15 + process.HLTMuTrackJpsiPixelRecoSequence + process.hltMu5TkMuJpsiTrackMassFiltered + process.HLTMuTrackJpsiTrackRecoSequence + process.hltMu5TkMuJpsiTkMuMassFilteredTight + process.HLTMuTkMuJpsiTkMuRecoSequence + process.HLTEndSequence )
process.HLT_Mu5_L2Mu2_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMu05 + process.hltPreMu5L2Mu0 + process.hltMu5L2Mu2L1Filtered0 + process.hltMu5L2Mu2L2PreFiltered0 + process.HLTL2muonrecoSequence + process.hltMu5L2Mu0L3Filtered5 + process.HLTL3muonrecoSequence + process.HLTEndSequence )
process.HLT_Mu5_L2Mu2_Jpsi_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMu05 + process.hltPreMu5L2Mu2Jpsi + process.hltMu5L2Mu2L1Filtered0 + process.HLTL2muonrecoSequence + process.hltMu5L2Mu2L2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltMu5L2Mu0L3Filtered5 + process.hltMu5L2Mu2JpsiTrackMassFiltered + process.HLTEndSequence )
process.HLT_Mu3_Track3_Jpsi_v4 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu3 + process.hltPreMu3Track3Jpsi + process.hltL1SingleMu3L1Filtered0 + process.HLTL2muonrecoSequence + process.hltMu3TrackJpsiL2Filtered3 + process.hltMu3TrackJpsiL3Filtered3 + process.hltMu3TrackJpsiPixelMassFiltered + process.HLTL3muonrecoSequence + process.hltMu3Track3JpsiTrackMassFiltered + process.HLTMuTrackJpsiPixelRecoSequence + process.HLTMuTrackJpsiTrackRecoSequence + process.HLTEndSequence )
process.HLT_Mu7_Track5_Jpsi_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu7 + process.hltPreMu7Track5Jpsi + process.hltL1SingleMu7L1Filtered0 + process.HLTL2muonrecoSequence + process.hltMu7TrackJpsiL2Filtered3 + process.HLTL3muonrecoSequence + process.hltMu7TrackJpsiL3Filtered3 + process.HLTMuTrackJpsiPixelRecoSequence + process.hltMu7TrackJpsiPixelMassFiltered + process.HLTMuTrackJpsiTrackRecoSequence + process.hltMu7Track5JpsiTrackMassFiltered + process.HLTEndSequence )
process.HLT_Mu7_Track7_Jpsi_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu7 + process.hltPreMu7Track7Jpsi + process.hltL1SingleMu7L1Filtered0 + process.HLTL2muonrecoSequence + process.hltMu7TrackJpsiL2Filtered3 + process.HLTL3muonrecoSequence + process.hltMu7TrackJpsiL3Filtered3 + process.HLTMuTrackJpsiPixelRecoSequence + process.hltMu7TrackJpsiPixelMassFiltered + process.HLTMuTrackJpsiTrackRecoSequence + process.hltMu7Track7JpsiTrackMassFiltered + process.HLTEndSequence )
process.HLT_L1SingleEG5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG5 + process.hltPreL1SingleEG5 + process.HLTEndSequence )
process.HLT_Photon30_CaloIdVL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG15 + process.hltPrePhoton30CaloIdVL + process.HLTPhoton30CaloIdVLSequence + process.HLTEndSequence )
process.HLT_Photon30_CaloIdVL_IsoL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG15 + process.hltPrePhoton30CaloIdVLIsoL + process.HLTPhoton30CaloIdVLIsoLSequence + process.HLTEndSequence )
process.HLT_Photon75_CaloIdVL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG20 + process.hltPrePhoton75CaloIdVL + process.HLTPhoton75CaloIdVLSequence + process.HLTEndSequence )
process.HLT_Photon75_CaloIdVL_IsoL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG20 + process.hltPrePhoton75CaloIdVLIsoL + process.HLTPhoton75CaloIdVLIsoLSequence + process.HLTEndSequence )
process.HLT_Photon125_NoSpikeFilter_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG20 + process.hltPrePhoton125NoSpikeFilter + process.HLTSinglePhoton125L1NonIsolatedHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_DoublePhoton5_IsoVL_CEP_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleEG2FwdVeto + process.hltPreDoublePhoton5IsoVLCEP + process.HLTDoublePhoton5IsoVLSequence + process.hltTowerMakerForHcal + process.hltHcalTowerFilter + process.HLTEndSequence )
process.HLT_DoublePhoton33_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG20 + process.hltPreDoublePhoton33 + process.HLTDoublePhoton33Sequence + process.HLTEndSequence )
process.HLT_Ele8_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG5 + process.hltPreEle8 + process.HLTEle8Sequence + process.HLTEndSequence )
process.HLT_Ele8_CaloIdL_CaloIsoVL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG5 + process.hltPreEle8CaloIdLCaloIsoVL + process.HLTEle8CaloIdLCaloIsoVLSequence + process.HLTEndSequence )
process.HLT_Ele8_CaloIdL_TrkIdVL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG5 + process.hltPreEle8CaloIdLTrkIdVL + process.HLTEle8CaloIdLTrkIdVLSequence + process.HLTEndSequence )
process.HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPreEle15CaloIdVTCaloIsoTTrkIdTTrkIsoT + process.HLTEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTSequence + process.HLTEndSequence )
process.HLT_Ele17_CaloIdL_CaloIsoVL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPreEle17CaloIdLCaloIsoVL + process.HLTEle17CaloIdLCaloIsoVLSequence + process.HLTEndSequence )
process.HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG15 + process.hltPreEle27CaloIdVTCaloIsoTTrkIdTTrkIsoT + process.HLTEle27CaloIdTCaloIsoTTrkIdTTrkIsoTSequence + process.HLTEndSequence )
process.HLT_Ele45_CaloIdVT_TrkIdT_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG20 + process.hltPreEle45CaloIdVTTrkIdT + process.HLTEle45CaloIdVTTrkIdTSequence + process.HLTEndSequence )
process.HLT_Ele90_NoSpikeFilter_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG20 + process.hltPreEle90NoSpikeFilter + process.HLTEle90NoSpikeFilterSequence + process.HLTEndSequence )
process.HLT_Photon20_R9Id_Photon18_R9Id_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPrePhoton20R9IdPhoton18R9Id + process.HLTPhoton20R9IdPhoton18R9IdSequence + process.HLTEndSequence )
process.HLT_Photon20_CaloIdVT_IsoT_Ele8_CaloIdL_CaloIsoVL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPrePhoton20CaloIdVTIsoTEle8CaloIdLCaloIsoVL + process.hltPhoton20CaloIdVTIsoTEle8CaloIdLCaloIsoVLDoubleLegCombFilter + process.HLTPhoton20CaloIdVTIsoTSequence + process.HLTEle8CaloIdLCaloIsoVLNoL1SeedSequence + process.HLTEndSequence )
process.HLT_Photon26_Photon18_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPrePhoton26Photon18 + process.HLTPhoton26Photon18Sequence + process.HLTEndSequence )
process.HLT_Photon26_IsoVL_Photon18_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPrePhoton26IsoVLPhoton18 + process.HLTPhoton26IsoVLPhoton18Sequence + process.HLTEndSequence )
process.HLT_Photon26_IsoVL_Photon18_IsoVL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPrePhoton26IsoVLPhoton18IsoVL + process.HLTPhoton26IsoVLPhoton18IsoVLSequence + process.HLTEndSequence )
process.HLT_Photon26_CaloIdL_IsoVL_Photon18_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPrePhoton26CaloIdLIsoVLPhoton18 + process.HLTPhoton26CaloIdLIsoVLPhoton18Sequence + process.HLTEndSequence )
process.HLT_Photon26_CaloIdL_IsoVL_Photon18_CaloIdL_IsoVL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPrePhoton26CaloIdLIsoVLPhoton18CaloIdLIsoVL + process.HLTPhoton26CaloIdLIsoVLPhoton18CaloIdLIsoVLSequence + process.HLTEndSequence )
process.HLT_Photon32_CaloIdL_Photon26_CaloIdL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG20 + process.hltPrePhoton32CaloIdLPhoton26CaloIdL + process.HLTPhoton32CaloIdLPhoton26CaloIdLSequence + process.HLTEndSequence )
process.HLT_Photon60_CaloIdL_HT200_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG20 + process.hltPrePhoton60CaloIdLHT200 + process.hltHT200 + process.HLTRecoJetSequenceAK5Corrected + process.HLTSinglePhoton60CaloIdLSequence + process.HLTEndSequence + process.HLTDoJet40HTRecoSequence )
process.HLT_Photon70_CaloIdL_HT200_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG20 + process.hltPrePhoton70CaloIdLHT200 + process.HLTSinglePhoton70CaloIdLSequence + process.HLTRecoJetSequenceAK5Corrected + process.hltHT200 + process.HLTDoJet40HTRecoSequence + process.HLTEndSequence )
process.HLT_Photon70_CaloIdL_HT300_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG20 + process.hltPrePhoton70CaloIdLHT300 + process.hltHT300 + process.HLTRecoJetSequenceAK5Corrected + process.HLTSinglePhoton70CaloIdLSequence + process.HLTEndSequence + process.HLTDoJet40HTRecoSequence )
process.HLT_Photon70_CaloIdL_MHT30_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG20 + process.hltPrePhoton70CaloIdLMHT30 + process.HLTSinglePhoton70CaloIdLSequence + process.HLTRecoJetSequenceAK5Corrected + process.hltMHT30 + process.HLTEndSequence )
process.HLT_Photon70_CaloIdL_MHT50_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG20 + process.hltPrePhoton70CaloIdLMHT50 + process.hltMHT50 + process.HLTSinglePhoton70CaloIdLSequence + process.HLTRecoJetSequenceAK5Corrected + process.HLTEndSequence )
process.HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPreEle17CaloIdLCaloIsoVLEle8CaloIdLCaloIsoVL + process.HLTEle17CaloIdIsoEle8CaloIdIsoSequence + process.HLTEndSequence )
process.HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPreEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8Mass30 + process.HLTEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTSC8Mass30Sequence + process.HLTEndSequence )
process.HLT_Ele17_CaloIdL_CaloIsoVL_Ele15_HFL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPreEle17CaloIdLCaloIsoVLEle15HFL + process.HLTSingleElectronEt17CaloIdIsoSequence + process.HLTHFEM15Sequence + process.HLTEndSequence )
process.HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG20 + process.hltPreEle32CaloIdLCaloIsoVLSC17 + process.HLTEle32CaloIdLCaloIsoVLSC17Sequence + process.HLTEndSequence )
process.HLT_IsoPFTau35_Trk20_MET45_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sSingleIsoTau35Trk20MET45 + process.hltPreSingleIsoTau35Trk20MET45 + process.HLTL2TauJetsSequence + process.hltFilterL2EtCutSingleIsoPFTau35Trk20MET45 + process.HLTRecoMETSequence + process.hltMet45 + process.HLTRecoJetSequencePrePF + process.hltPFTauTightIso35 + process.hltPFTauTightIso35Track + process.hltPFTauTightIsoTrackPt20Discriminator + process.hltSelectedPFTauTightIsoTrackPt20 + process.HLTTrackReconstructionForJets + process.HLTParticleFlowSequence + process.HLTPFJetsSequence + process.HLTPFTauTightIsoSequence + process.hltConvPFTauTightIsoTrackPt20 + process.hltFilterSingleIsoPFTau35Trk20LeadTrackPt20 + process.hltSelectedPFTauTightIsoTrackPt20Isolation + process.hltConvPFTauTightIsoTrackPt20Isolation + process.hltL1HLTSingleIsoPFTau35Trk20Met45JetsMatch + process.hltFilterSingleIsoPFTau35Trk20MET45LeadTrack20MET45IsolationL1HLTMatched + process.HLTEndSequence )
process.HLT_DoubleIsoPFTau20_Trk5_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sDoubleIsoTau20Trk5 + process.hltPreDoubleIsoTau20Trk5 + process.HLTL2TauJetsSequence + process.hltFilterL2EtCutDoublePFIsoTau20Trk5 + process.hltDoublePFTauTightIso20Track + process.hltDoublePFTauTightIso20Track5 + process.HLTRecoJetSequencePrePF + process.HLTTrackReconstructionForJets + process.HLTParticleFlowSequence + process.HLTPFJetsSequence + process.HLTPFTauTightIsoSequence + process.hltL1HLTDoubleIsoPFTau20Trk5JetsMatch + process.hltFilterDoubleIsoPFTau20Trk5LeadTrack5IsolationL1HLTMatched + process.HLTEndSequence )
process.HLT_BTagMu_DiJet20_Mu5_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu3Jet16 + process.hltPreBTagMuDiJet20Mu5 + process.hltBDiJet20Central + process.HLTRecoJetSequenceAK5Corrected + process.hltBSoftMuonL25FilterByDR + process.HLTBTagMuSequenceL25 + process.HLTBTagMu5SelSequenceL3 + process.hltBSoftMuon5SelL3FilterByDR + process.HLTEndSequence )
process.HLT_BTagMu_DiJet60_Mu7_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu3Jet16 + process.hltPreBTagMuDiJet60Mu7 + process.HLTRecoJetSequenceAK5Corrected + process.hltBDiJet60Central + process.hltBSoftMuonL25FilterByDR + process.hltBSoftMuon7SelL3FilterByDR + process.HLTBTagMuSequenceL25 + process.HLTBTagMu7SelSequenceL3 + process.HLTEndSequence )
process.HLT_BTagMu_DiJet80_Mu9_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu3Jet20 + process.hltPreBTagMuDiJet80Mu9 + process.hltBDiJet80Central + process.HLTRecoJetSequenceAK5Corrected + process.hltBSoftMuonL25FilterByDR + process.HLTBTagMuSequenceL25 + process.hltBSoftMuon9SelL3FilterByDR + process.HLTBTagMu9SelSequenceL3 + process.HLTEndSequence )
process.HLT_Mu3_Ele8_CaloIdL_TrkIdVL_HT160_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu0HTT50 + process.hltPreMu3Ele8CaloIdLTrkIdVLHT160 + process.hltL1Mu0HTT50L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL1Mu0HTT50L2Filtered0 + process.HLTL3muonrecoSequence + process.hltL1Mu0HTT50L3Filtered3 + process.HLTRecoJetSequenceAK5Corrected + process.hltHT160 + process.hltL1NonIsoHLTNonIsoSingleEle8NoCandEtFilter + process.hltUnseededR9shape + process.hltL1NonIsoHLTNonIsoSingleEle8NoCandR9ShapeFilter + process.HLTDoJet40HTRecoSequence + process.hltActivityPhotonClusterShape + process.HLTEcalActivitySequence + process.hltL1NonIsoHLTCaloIdLSingleEle8NoCandClusterShapeFilter + process.hltActivityPhotonHcalForHE + process.hltL1NonIsoHLTCaloIdLSingleEle8NoCandHEFilter + process.hltActivityStartUpElectronPixelSeeds + process.hltL1NonIsoHLTCaloIdLSingleEle8NoCandPixelMatchFilter + process.hltL1NonIsoHLTCaloIdLTrkIdVLSingleElectronEt8NoCandOneOEMinusOneOPFilter + process.hltElectronActivityDetaDphi + process.hltL1NonIsoHLTCaloIdLTrkIdVLSingleElectronEt8NoCandDetaFilter + process.hltL1NonIsoHLTCaloIdLTrkIdVLSingleElectronEt8NoCandDphiFilter + process.HLTPixelMatchElectronActivityTrackingSequence + process.HLTEndSequence )
process.HLT_Mu3_Ele8_CaloIdT_TrkIdVL_HT160_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu0HTT50 + process.hltPreMu3Ele8CaloIdTTrkIdVLHT160 + process.hltL1Mu0HTT50L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL1Mu0HTT50L2Filtered0 + process.hltL1Mu0HTT50L3Filtered3 + process.hltHT160 + process.HLTL3muonrecoSequence + process.hltL1NonIsoHLTNonIsoSingleEle8NoCandEtFilter + process.HLTRecoJetSequenceAK5Corrected + process.HLTDoJet40HTRecoSequence + process.hltUnseededR9shape + process.HLTEcalActivitySequence + process.hltL1NonIsoHLTNonIsoSingleEle8NoCandR9ShapeFilter + process.hltActivityPhotonClusterShape + process.hltL1NonIsoHLTCaloIdTSingleEle8NoCandClusterShapeFilter + process.hltActivityPhotonHcalForHE + process.hltL1NonIsoHLTCaloIdTSingleEle8NoCandHEFilter + process.hltActivityStartUpElectronPixelSeeds + process.hltL1NonIsoHLTCaloIdTSingleEle8NoCandPixelMatchFilter + process.hltL1NonIsoHLTCaloIdTTrkIdVLSingleElectronEt8NoCandOneOEMinusOneOPFilter + process.hltElectronActivityDetaDphi + process.HLTPixelMatchElectronActivityTrackingSequence + process.hltL1NonIsoHLTCaloIdTTrkIdVLSingleElectronEt8NoCandDetaFilter + process.hltL1NonIsoHLTCaloIdTTrkIdVLSingleElectronEt8NoCandDphiFilter + process.HLTEndSequence )
process.HLT_Mu5_Ele8_CaloIdL_TrkIdVL_Ele8_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu3EG5 + process.hltPreMu5Ele8CaloIdLTrkIdVLEle8 + process.hltL1Mu3EG5L1Filtered3 + process.HLTL2muonrecoSequence + process.hltL2Mu3EG5L2Filtered3 + process.HLTL3muonrecoSequence + process.hltMu3EG5L3Filtered5 + process.HLTMu5Ele8CaloIdLTrkIdVLEle8L1NonIsoHLTnonIsoSequence + process.HLTEndSequence )
process.HLT_Mu5_DoubleEle8_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu3EG5 + process.hltPreMu5DoubleEle8 + process.hltL1Mu3EG5L1Filtered3 + process.HLTL2muonrecoSequence + process.hltL2Mu3EG5L2Filtered3 + process.HLTL3muonrecoSequence + process.hltMu3EG5L3Filtered5 + process.HLTMu5DoubleEle8L1NonIsoHLTnonIsoSequence + process.HLTEndSequence )
process.HLT_Mu5_HT200_v3 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu0HTT50 + process.hltPreMu5HT200 + process.hltL1Mu0HTT50L1MuFiltered3 + process.HLTL2muonrecoSequence + process.hltL1Mu0HTT50L2MuFiltered3 + process.hltL1Mu0HTT50L3MuFiltered5 + process.hltHT200 + process.HLTL3muonrecoSequence + process.HLTRecoJetSequenceAK5Corrected + process.HLTDoJet40HTRecoSequence + process.HLTEndSequence )
process.HLT_Mu8_HT200_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu0HTT50 + process.hltPreMu8HT200 + process.hltL1Mu0HTT50L1MuFiltered5 + process.HLTL2muonrecoSequence + process.hltL1Mu0HTT50L2MuFiltered5 + process.HLTL3muonrecoSequence + process.hltL1Mu0HTT50L3MuFiltered8 + process.HLTRecoJetSequenceAK5Corrected + process.hltHT200 + process.HLTDoJet40HTRecoSequence + process.HLTEndSequence )
process.HLT_Mu8_Ele17_CaloIdL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu3EG5 + process.hltPreMu8Ele17CaloIdL + process.hltL1Mu3EG5L1Filtered5 + process.HLTL2muonrecoSequence + process.hltL1Mu3EG5L2Filtered5 + process.HLTL3muonrecoSequence + process.hltL1Mu3EG5L3Filtered8 + process.HLTDoEGammaStartupSequence + process.hltEGRegionalL1Mu3EG5 + process.hltEG17EtFilterL1Mu3EG5 + process.HLTEgammaR9ShapeSequence + process.hltL1NonIsoHLTNonIsoMu8Ele17R9ShapeFilter + process.HLTDoEgammaClusterShapeSequence + process.hltL1NonIsoHLTCaloIdLMu8Ele17ClusterShapeFilter + process.HLTDoEGammaHESequence + process.hltL1NonIsoHLTNonIsoMu8Ele17HEFilter + process.HLTDoEGammaPixelSequence + process.hltL1NonIsoHLTNonIsoMu8Ele17PixelMatchFilter + process.HLTEndSequence )
process.HLT_Mu8_Photon20_CaloIdVT_IsoT_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1Mu3EG5 + process.hltPreMu8Photon20CaloIdVTIsoT + process.hltL1SingleMu3EG5L1Filtered0 + process.HLTPhoton20CaloIdVTIsoTMu8Sequence + process.hltSingleMu5EG5L2Filtered3 + process.HLTL2muonrecoSequence + process.hltSingleMu8EG5L3Filtered8 + process.HLTL3muonrecoSequence + process.HLTEndSequence )
process.HLT_Mu8_Jet40_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1Mu3Jet20 + process.hltPreMu8Jet40 + process.hltL1Mu3Jet20L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu8Jet20L2Filtered3 + process.hltL3Mu8Jet20L3Filtered8 + process.hltJet40 + process.HLTL3muonrecoSequence + process.HLTRecoJetSequenceAK5Corrected + process.HLTEndSequence )
process.HLT_Mu10_Ele10_CaloIdL_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu3EG5 + process.hltPreMu10Ele10CaloIdL + process.hltL1Mu3EG5L1Filtered5 + process.HLTL2muonrecoSequence + process.hltL1Mu3EG5L2Filtered5 + process.HLTL3muonrecoSequence + process.hltL1Mu3EG5L3Filtered10 + process.HLTDoEGammaStartupSequence + process.hltEGRegionalL1Mu3EG5 + process.hltEG10EtFilterL1Mu3EG5 + process.HLTEgammaR9ShapeSequence + process.hltL1NonIsoHLTNonIsoMu10Ele10R9ShapeFilter + process.HLTDoEgammaClusterShapeSequence + process.hltL1NonIsoHLTCaloIdLMu10Ele10ClusterShapeFilter + process.HLTDoEGammaHESequence + process.hltL1NonIsoHLTNonIsoMu10Ele10HEFilter + process.HLTDoEGammaPixelSequence + process.hltL1NonIsoHLTNonIsoMu10Ele10PixelMatchFilter + process.HLTEndSequence )
process.HLT_Mu15_Photon20_CaloIdL_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu3EG5 + process.hltPreMu15Photon20CaloIdL + process.hltL1Mu3EG5L1Filtered5 + process.HLTL2muonrecoSequence + process.hltL1Mu3EG5L2Filtered5 + process.HLTL3muonrecoSequence + process.hltL1Mu3EG5L3Filtered15 + process.HLTDoEGammaStartupSequence + process.hltEGRegionalL1Mu3EG5 + process.hltEG20EtFilterMu3EG5 + process.HLTEgammaR9ShapeSequence + process.hltEG20R9ShapeFilterMu3EG5 + process.HLTDoEgammaClusterShapeSequence + process.hltMu15Photon20CaloIdLClusterShapeFilter + process.HLTDoEGammaHESequence + process.hltMu15Photon20CaloIdLHEFilter + process.HLTEndSequence )
process.HLT_Mu15_DoublePhoton15_CaloIdL_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu3EG5 + process.hltPreMu15DoublePhoton15CaloIdL + process.hltL1Mu3EG5L1Filtered5 + process.HLTL2muonrecoSequence + process.hltL1Mu3EG5L2Filtered5 + process.HLTL3muonrecoSequence + process.hltL1Mu3EG5L3Filtered15 + process.HLTDoEGammaStartupSequence + process.hltEGRegionalL1Mu3EG5 + process.hltDoubleEG15EtFilterL1Mu3EG5 + process.HLTEgammaR9ShapeSequence + process.hltMu15DiPhoton15R9ShapeFilter + process.HLTDoEgammaClusterShapeSequence + process.hltMu15DiPhoton15CaloIdLClusterShapeFilter + process.HLTDoEGammaHESequence + process.hltMu15DiPhoton15CaloIdLHEFilter + process.HLTEndSequence )
process.HLT_Mu15_LooseIsoPFTau20_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu10 + process.hltPreMu15IsoPFTau20 + process.hltL1SingleMu10L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu10L2Filtered10 + process.HLTL3muonrecoSequence + process.hltL3Muon15 + process.HLTRecoJetSequencePrePF + process.hltTauJet5 + process.HLTPFJetTriggerSequence + process.hltPFJet20 + process.HLTPFTauSequence + process.hltPFTau20Track + process.hltPFTau20TrackLooseIso + process.hltOverlapFilterMu15IsoPFTau20 + process.HLTEndSequence )
process.HLT_Mu17_CentralJet30_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu7Jet20Central + process.hltPreMu17TriCenJet30 + process.hltL1Mu7CenJet20L1MuFiltered0 + process.HLTL2muonrecoSequence + process.hltL2Muon7 + process.HLTL3muonrecoSequence + process.hltL3Muon17 + process.hltJet30Central + process.HLTRecoJetSequenceAK5Corrected + process.HLTEndSequence )
process.HLT_Mu17_DiCentralJet30_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu7Jet20Central + process.hltPreMu17TriCenJet30 + process.hltL1Mu7CenJet20L1MuFiltered0 + process.hltL2Muon7 + process.HLTL2muonrecoSequence + process.hltL3Muon17 + process.HLTL3muonrecoSequence + process.HLTRecoJetSequenceAK5Corrected + process.hltDiJet30Central + process.HLTEndSequence )
process.HLT_Mu17_TriCentralJet30_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu7Jet20Central + process.hltPreMu17TriCenJet30 + process.hltL1Mu7CenJet20L1MuFiltered0 + process.HLTL2muonrecoSequence + process.hltL2Muon7 + process.hltL3Muon17 + process.hltTriJet30Central + process.HLTL3muonrecoSequence + process.HLTRecoJetSequenceAK5Corrected + process.HLTEndSequence )
process.HLT_Mu17_Ele8_CaloIdL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu3EG5 + process.hltPreMu17Ele8CaloIdL + process.hltL1Mu3EG5L1Filtered12 + process.HLTL2muonrecoSequence + process.hltL1Mu3EG5L2Filtered12 + process.HLTL3muonrecoSequence + process.hltL1Mu3EG5L3Filtered17 + process.HLTDoEGammaStartupSequence + process.hltEGRegionalL1Mu3EG5 + process.hltEG8EtFilterMu3EG5 + process.HLTEgammaR9ShapeSequence + process.hltEG8R9ShapeFilterMu3EG5 + process.HLTDoEgammaClusterShapeSequence + process.hltL1NonIsoHLTCaloIdLMu17Ele8ClusterShapeFilter + process.HLTDoEGammaHESequence + process.hltL1NonIsoHLTNonIsoMu17Ele8HEFilter + process.HLTDoEGammaPixelSequence + process.hltL1NonIsoHLTNonIsoMu17Ele8PixelMatchFilter + process.HLTEndSequence )
process.HLT_Mu17_CentralJet40_BTagIP_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu7Jet20Central + process.hltPreMu17BTagIPCenJet40 + process.hltL1Mu7CenJet20L1MuFiltered0 + process.HLTL2muonrecoSequence + process.hltL2Muon7 + process.HLTRecoJetSequenceAK5Corrected + process.hltBJet40Central + process.HLTBTagIPSequenceL25SingleTop + process.hltBLifetimeL25FilterSingleTop + process.HLTL3muonrecoSequence + process.hltL3Muon17 + process.hltBLifetimeL3FilterSingleTop + process.HLTBTagIPSequenceL3SingleTop + process.HLTEndSequence )
process.HLT_IsoMu17_CentralJet40_BTagIP_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu7Jet20Central + process.hltPreIsoMu17BTagIPCentJet40 + process.hltL1Mu7CenJet20L1MuFiltered0 + process.HLTL2muonrecoSequence + process.hltL2Muon7 + process.HLTL2muonisorecoSequence + process.hltIsoMu7CenJet40L2IsoFiltered7 + process.HLTRecoJetSequenceAK5Corrected + process.hltBJet40Central + process.HLTBTagIPSequenceL25SingleTop + process.hltBLifetimeL25FilterSingleTop + process.HLTL3muonrecoSequence + process.hltIsoMu17CenJet40L3Filtered17 + process.HLTL3muonisorecoSequence + process.hltIsoMu17CenJet40L3IsoFiltered17 + process.hltBLifetimeL3FilterSingleTop + process.HLTBTagIPSequenceL3SingleTop + process.HLTEndSequence )
process.HLT_IsoMu12_LooseIsoPFTau10_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu7 + process.hltPreIsoMu12IsoPFTau10 + process.hltL1SingleMu7L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu7L2Filtered7 + process.HLTL2muonisorecoSequence + process.hltSingleMuIsoL2IsoFiltered7 + process.HLTL3muonrecoSequence + process.hltSingleMuIsoL3PreFiltered12 + process.HLTL3muonisorecoSequence + process.hltSingleMuIsoL3IsoFiltered12 + process.HLTRecoJetSequencePrePF + process.hltTauJet5 + process.HLTPFJetTriggerSequence + process.hltPFJet10 + process.hltPFTau10Track + process.hltFilterIsoMu12IsoPFTau10LooseIsolation + process.hltOverlapFilterIsoMu12IsoPFTau10 + process.HLTPFTauSequence + process.HLTEndSequence )
process.HLT_DoubleMu3_HT160_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu0HTT50 + process.hltPreDoubleMu3HT160 + process.hltL1Mu0HTT50L1DiMuFiltered0 + process.HLTL2muonrecoSequence + process.hltL1Mu0HTT50L2DiMuFiltered0 + process.HLTL3muonrecoSequence + process.hltL1Mu0HTT50L3DiMuFiltered3 + process.hltHT160 + process.HLTRecoJetSequenceAK5Corrected + process.HLTDoJet40HTRecoSequence + process.HLTEndSequence )
process.HLT_DoubleMu3_HT200_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu0HTT50 + process.hltPreDoubleMu3HT160 + process.hltL1Mu0HTT50L1DiMuFiltered0 + process.HLTL2muonrecoSequence + process.hltL1Mu0HTT50L2DiMuFiltered0 + process.HLTL3muonrecoSequence + process.hltL1Mu0HTT50L3DiMuFiltered3 + process.HLTRecoJetSequenceAK5Corrected + process.HLTDoJet40HTRecoSequence + process.hltHT200 + process.HLTEndSequence )
process.HLT_DoubleMu5_Ele8_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu3EG5 + process.hltPreDoubleMu5Ele8 + process.hltL1Mu3EG5L1DiMuFiltered3 + process.HLTL2muonrecoSequence + process.hltL1Mu3EG5L2DiMuFiltered3 + process.hltL1Mu3EG5L3DiMuFiltered5 + process.HLTEndSequence + process.HLTL3muonrecoSequence + process.HLTDoubleMu5Ele8L1NonIsoHLTnonIsoSequence )
process.HLT_DoubleMu5_Ele8_CaloIdL_TrkIdVL_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu3EG5 + process.hltPreDoubleMu5Ele8CaloIdLTrkIdVL + process.hltL1Mu3EG5L1DiMuFiltered3 + process.hltL1Mu3EG5L2DiMuFiltered3 + process.HLTL2muonrecoSequence + process.hltL1Mu3EG5L3DiMuFiltered5 + process.HLTL3muonrecoSequence + process.HLTDoubleMu5Ele8L1NonIsoHLTCaloIdLTrkIdVLSequence + process.HLTEndSequence )
process.HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG5 + process.hltPreEle8CaloIdLCaloIsoVLJet40 + process.hltAntiKT5L2L3CaloJetsEle8CaloIdLCaloIsoVLRemoved + process.HLTEle8CaloIdLCaloIsoVLSequence + process.HLTRecoJetSequenceAK5Corrected + process.hltJet40Ele8CaloIdLCaloIsoVLRemoved + process.HLTEndSequence )
process.HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1EG5HTT75 + process.hltPreEle10CaloIdLCaloIsoVLTrkIdVLTrkIsoVLHT200 + process.HLTRecoJetSequenceAK5Corrected + process.hltHT200 + process.HLTSingleElectronEt10HT200L1NonIsoHLTCaloIdLTrkIdVLCaloIsolVLTrkIsolVLSequence + process.HLTDoJet40HTRecoSequence + process.HLTEndSequence )
process.HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1EG5HTT75 + process.hltPreEle10CaloIdTCaloIsoVLTrkIdTTrkIsoVLHT200 + process.hltHT200 + process.HLTRecoJetSequenceAK5Corrected + process.HLTDoJet40HTRecoSequence + process.HLTSingleElectronEt10HT200L1NonIsoHLTCaloIdTTrkIdTCaloIsolVLTrkIsolVLSequence + process.HLTEndSequence )
process.HLT_Ele15_CaloIdVT_TrkIdT_LooseIsoPFTau15_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPreEle15CaloIdVTTrkIdTLooseIsoPFTau15 + process.HLTEle15CaloIdVTTrkIdTSequence + process.HLTRecoJetSequencePrePF + process.hltTauJet5 + process.hltOverlapFilterEle15CaloJet5 + process.HLTPFJetTriggerSequence + process.hltPFJet15 + process.hltPFTau15 + process.hltPFTau15Track + process.hltPFTau15TrackLooseIso + process.hltOverlapFilterEle15IsoPFTau15 + process.HLTPFTauSequence + process.HLTEndSequence )
process.HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPreEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTLooseIsoPFTau15 + process.HLTEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTSequence + process.HLTRecoJetSequencePrePF + process.hltTauJet5 + process.hltOverlapFilterIsoEle15CaloJet5 + process.HLTPFJetTriggerSequence + process.hltPFJet15 + process.hltPFTau15 + process.hltPFTau15Track + process.hltPFTau15TrackLooseIso + process.hltOverlapFilterIsoEle15IsoPFTau15 + process.HLTPFTauSequence + process.HLTEndSequence )
process.HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPreEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTLooseIsoPFTau20 + process.HLTEle15CaloIdVTCaloIsoTTrkIdTTrkIsoTSequence + process.hltTauJet5 + process.hltOverlapFilterIsoEle15CaloJet5 + process.HLTRecoJetSequencePrePF + process.hltPFJet20 + process.hltPFTau20 + process.HLTPFJetTriggerSequence + process.hltPFTau20Track + process.HLTPFTauSequence + process.hltPFTau20TrackLooseIso + process.hltOverlapFilterIsoEle15IsoPFTau20 + process.HLTEndSequence )
process.HLT_Ele25_CaloIdVT_TrkIdT_CentralJet30_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPreEle25CaloIdVTTrkIdTCentralJet30 + process.hltCleanEle25CaloIdVTTrkIdTFromAK5CorrJets + process.HLTEle25CaloIdVTCaloTrkIdSequence + process.HLTRecoJetSequenceAK5Corrected + process.hltEle25CaloIdVTTrkIdTCentralJet30Cleaned + process.HLTEndSequence )
process.HLT_Ele25_CaloIdVT_TrkIdT_CentralDiJet30_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPreEle25CaloIdVTTrkIdTCentralDiJet30 + process.hltCleanEle25CaloIdVTTrkIdTFromAK5CorrJets + process.HLTEle25CaloIdVTCaloTrkIdSequence + process.HLTRecoJetSequenceAK5Corrected + process.hltEle25CaloIdVTTrkIdTCentralDiJet30Cleaned + process.HLTEndSequence )
process.HLT_Ele25_CaloIdVT_TrkIdT_CentralTriJet30_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPreEle25CaloIdVTTrkIdTCentralTriJet30 + process.hltCleanEle25CaloIdVTTrkIdTFromAK5CorrJets + process.HLTEle25CaloIdVTCaloTrkIdSequence + process.HLTRecoJetSequenceAK5Corrected + process.hltEle25CaloIdVTTrkIdTCentralTriJet30Cleaned + process.HLTEndSequence )
process.HLT_Ele25_CaloIdVT_TrkIdT_CentralJet40_BTagIP_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleEG12 + process.hltPreEle25CaloIdVTTrkIdTCentralJet40BTagIP + process.hltCleanEle25CaloIdVTTrkIdTFromAK5CorrJets + process.HLTEle25CaloIdVTCaloTrkIdSequence + process.HLTRecoJetSequenceAK5Corrected + process.hltSingleEleCleanBJet40Central + process.hltBLifetimeL25FilterEleJetSingleTop + process.HLTBTagIPSequenceL25EleJetSingleTop + process.hltBLifetimeL3FilterEleJetSingleTop + process.HLTBTagIPSequenceL3EleJetSingleTop + process.HLTEndSequence )
process.HLT_DoubleEle8_CaloIdL_TrkIdVL_HT160_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleEG5HTT50 + process.hltPreDoubleEle8CaloIdLTrkIdVLHT160 + process.hltL1NonIsoHLTCaloIdLTrkIdVLDoubleEle8HTT50OneOEMinusOneOPFilter + process.HLTDoubleEle8HTT50L1NonIsoHLTCaloIdLSequence + process.HLTPixelMatchElectronL1IsoTrackingSequence + process.HLTPixelMatchElectronL1NonIsoTrackingSequence + process.hltL1NonIsoHLTCaloIdLTrkIdVLDoubleEle8HTT50DetaFilter + process.HLTDoElectronDetaDphiSequence + process.hltL1NonIsoHLTCaloIdLTrkIdVLDoubleEle8HTT50DphiFilter + process.hltHT160 + process.HLTRecoJetSequenceAK5Corrected + process.HLTDoJet40HTRecoSequence + process.HLTEndSequence )
process.HLT_DoubleEle8_CaloIdT_TrkIdVL_HT160_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleEG5HTT50 + process.hltPreDoubleEle8CaloIdTTrkIdVLHT160 + process.hltL1NonIsoHLTCaloIdTTrkIdVLDoubleEle8HTT50OneOEMinusOneOPFilter + process.HLTDoubleEle8HTT50L1NonIsoHLTCaloIdTSequence + process.HLTPixelMatchElectronL1IsoTrackingSequence + process.HLTPixelMatchElectronL1NonIsoTrackingSequence + process.hltL1NonIsoHLTCaloIdTTrkIdVLDoubleEle8HTT50DetaFilter + process.HLTDoElectronDetaDphiSequence + process.hltL1NonIsoHLTCaloIdTTrkIdVLDoubleEle8HTT50DphiFilter + process.hltHT160 + process.HLTRecoJetSequenceAK5Corrected + process.HLTDoJet40HTRecoSequence + process.HLTEndSequence )
process.HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1TripleEG5 + process.hltPreDoubleEle10CaloIdLTrkIdVLEle10 + process.hltL1NonIsoHLT2CaloIdLTripleElectronEt10HEFilter + process.HLTTripleElectronEt10L1NonIsoHLTNonIsoSequence + process.hltL1NonIsoHLT2LegEleIdTripleElectronEt10ClusterShapeFilter + process.HLTDoEgammaClusterShapeSequence + process.hltL1NonIsoHLT2LegEleIdTripleElectronEt10OneOEMinusOneOPFilter + process.HLTPixelMatchElectronL1IsoTrackingSequence + process.HLTPixelMatchElectronL1NonIsoTrackingSequence + process.hltL1NonIsoHLT2LegEleIdTripleElectronEt10EleIdDetaFilter + process.HLTDoElectronDetaDphiSequence + process.hltL1NonIsoHLT2LegEleIdTripleElectronEt10EleIdDphiFilter + process.HLTEndSequence )
process.HLT_TripleEle10_CaloIdL_TrkIdVL_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1TripleEG5 + process.hltPreTripleEle10CaloIdLTrkIdVL + process.HLTTripleElectronEt10L1NonIsoHLTNonIsoSequence + process.hltL1NonIsoHLT3LegEleIdTripleElectronEt10ClusterShapeFilter + process.hltL1NonIsoHLT3LegEleIdTripleElectronEt10OneOEMinusOneOPFilter + process.HLTDoEgammaClusterShapeSequence + process.hltL1NonIsoHLT3LegEleIdTripleElectronEt10EleIdDetaFilter + process.HLTPixelMatchElectronL1IsoTrackingSequence + process.HLTPixelMatchElectronL1NonIsoTrackingSequence + process.hltL1NonIsoHLT3LegEleIdTripleElectronEt10EleIdDphiFilter + process.HLTDoElectronDetaDphiSequence + process.HLTEndSequence )
process.HLT_Photon20_EBOnly_NoSpikeFilter_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG12 + process.hltPrePhoton20EBOnlyNoSpikeFilter + process.HLTPhoton20EBOnlyNoSpikeFilterSequence + process.HLTEndSequence )
process.HLT_Photon20_NoSpikeFilter_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG12 + process.hltPrePhoton20NoSpikeFilter + process.HLTPhoton20NoSpikeFilterSequence + process.HLTEndSequence )
process.HLT_Spike20_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG12 + process.hltPreSpike20 + process.HLTSpike20Sequence + process.HLTEndSequence )
process.HLT_PixelTracks_Multiplicity110_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sETT180 + process.hltPrePixelTracksMultiplicity110 + process.hltPixelClusterShapeFilter + process.HLTDoLocalPixelSequence + process.hltPixelCandsForHighMult + process.HLTRecopixelvertexingForHighMultSequence + process.hltTrackMultiplicity110 + process.HLTEndSequence )
process.HLT_PixelTracks_Multiplicity125_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sETT180 + process.hltPrePixelTracksMultiplicity125 + process.HLTDoLocalPixelSequence + process.hltPixelClusterShapeFilter + process.HLTRecopixelvertexingForHighMultSequence + process.hltPixelCandsForHighMult + process.hltTrackMultiplicity125 + process.HLTEndSequence )
process.HLT_BeamGas_HF_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1BeamGasHf + process.hltHcalDigis + process.hltHfreco + process.hltHFAsymmetryFilter + process.hltPreL1BeamGasHf + process.HLTEndSequence )
process.HLT_BeamGas_BSC_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1BeamGasBsc + process.hltSiPixelDigis + process.hltSiPixelClusters + process.hltPixelActivityFilter + process.hltPixelAsymmetryFilter + process.hltPreL1BeamGasBsc + process.HLTEndSequence )
process.HLT_L1_BeamHalo_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1BeamHalo + process.hltPreL1BeamHalo + process.HLTEndSequence )
process.HLT_L1Tech_BSC_minBias_threshold1_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreL1TechBSCminBiasthreshold1 + process.hltL1TechBSCminBiasthreshold1 + process.HLTEndSequence )
process.HLT_L1Tech_BSC_halo_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sZeroBias + process.hltPreL1TechBSChalo + process.hltL1TechBSChalo + process.HLTEndSequence )
process.HLT_L1_PreCollisions_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1PreCollisions + process.hltPreL1PreCollisions + process.HLTEndSequence )
process.HLT_L1_Interbunch_BSC_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1InterbunchBsc + process.hltPreL1Interbunch1 + process.HLTEndSequence )
process.HLT_IsoTrackHE_v3 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet52 + process.hltPreIsoTrackHE + process.hltHITPixelTracksHB + process.HLTDoLocalPixelSequence + process.hltHITPixelTracksHE + process.hltHITPixelVerticesHE + process.hltIsolPixelTrackProdHE + process.hltIsolPixelTrackL2FilterHE + process.hltHITPixelTripletSeedGeneratorHE + process.HLTDoLocalStripSequence + process.hltHITCkfTrackCandidatesHE + process.hltHITCtfWithMaterialTracksHE + process.hltHITIPTCorrectorHE + process.hltIsolPixelTrackL3FilterHE + process.HLTEndSequence )
process.HLT_IsoTrackHB_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet52 + process.hltPreIsoTrackHB + process.HLTDoLocalPixelSequence + process.hltHITPixelTracksHB + process.hltHITPixelVerticesHB + process.hltIsolPixelTrackProdHB + process.hltIsolPixelTrackL2FilterHB + process.HLTDoLocalStripSequence + process.hltHITPixelTripletSeedGeneratorHB + process.hltHITCkfTrackCandidatesHB + process.hltHITCtfWithMaterialTracksHB + process.hltHITIPTCorrectorHB + process.hltIsolPixelTrackL3FilterHB + process.HLTEndSequence )
process.HLT_HcalPhiSym_v2 = cms.Path( process.HLTBeginSequenceNZS + process.hltL1sHcalPhiSym + process.hltPreHcalPhiSym + process.HLTEndSequence )
process.HLT_HcalNZS_v2 = cms.Path( process.HLTBeginSequenceNZS + process.hltL1sHcalNZS + process.hltPreHcalNZS + process.HLTEndSequence )
process.HLT_GlobalRunHPDNoise_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sGlobalRunHPDNoise + process.hltPreGlobalRunHPDNoise + process.HLTEndSequence )
process.HLT_L1Tech_HBHEHO_totalOR_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sTechTrigHCALNoise + process.hltPreTechTrigHCALNoise + process.HLTEndSequence )
process.HLT_ZeroBias_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreZeroBias + process.HLTEndSequence )
process.HLT_Physics_v1 = cms.Path( process.HLTBeginSequence + process.hltPrePhysics + process.HLTEndSequence )
process.HLT_Physics_NanoDST_v1 = cms.Path( process.HLTBeginSequence + process.hltPrePhysicsNanoDST + process.HLTEndSequence )
process.HLT_Calibration_v1 = cms.Path( process.HLTBeginSequenceCalibration + process.hltPreCalibration + process.HLTEndSequence )
process.HLT_EcalCalibration_v1 = cms.Path( process.hltCalibrationEventsFilter + process.hltGtDigis + process.hltPreEcalCalibration + process.hltEcalCalibrationRaw + process.HLTEndSequence )
process.HLT_HcalCalibration_v1 = cms.Path( process.hltCalibrationEventsFilter + process.hltGtDigis + process.hltPreHcalCalibration + process.hltHcalCalibTypeFilter + process.HLTEndSequence )
process.HLT_TrackerCalibration_v1 = cms.Path( process.HLTBeginSequenceCalibration + process.hltPreTrackerCalibration + process.hltLaserAlignmentEventFilter + process.HLTEndSequence )
process.HLT_Random_v1 = cms.Path( process.HLTBeginSequenceRandom + process.hltPreRandom + process.HLTEndSequence )
process.HLT_L1MuOpen_AntiBPTX_v2 = cms.Path( process.HLTBeginSequenceAntiBPTX + process.hltL1sL1SingleMuOpen + process.hltPreL1MuOpenAntiBPTX + process.hltL1MuOpenL1Filtered0 + process.HLTEndSequence )
process.HLT_L1TrackerCosmics_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sTrackerCosmics + process.hltPreTrackerCosmics + process.hltTrackerCosmicsPattern + process.HLTEndSequence )
process.HLT_RegionalCosmicTracking_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sTrackerCosmics + process.hltPreRegionalCosmicTracking + process.hltTrackerCosmicsPattern + process.hltL1sL1SingleMuOpenCandidate + process.hltL1MuORL1Filtered0 + process.HLTL2muonrecoSequenceNoVtx + process.hltSingleL2MuORL2PreFilteredNoVtx + process.hltRegionalCosmicTrackerSeeds + process.hltRegionalCosmicCkfTrackCandidates + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltRegionalCosmicTracks + process.hltCosmicTrackSelector + process.HLTEndSequence )
process.HLT_L3MuonsCosmicTracking_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sTrackerCosmics + process.hltPreL3MuonsCosmicTracking + process.hltTrackerCosmicsPattern + process.hltL1sL1SingleMuOpenCandidate + process.hltL1MuORL1Filtered0 + process.hltSingleL2MuORL2PreFilteredNoVtx + process.HLTL2muonrecoSequenceNoVtx + process.hltL3TrajectorySeedNoVtx + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL3TrackCandidateFromL2NoVtx + process.hltL3TkTracksFromL2NoVtx + process.hltL3MuonsNoVtx + process.hltL3MuonCandidatesNoVtx + process.hltMu5NoVertexL3PreFiltered5 + process.HLTEndSequence )
process.HLT_LogMonitor_v1 = cms.Path( process.hltGtDigis + process.hltPreLogMonitor + process.hltLogMonitorFilter + process.HLTEndSequence )
process.HLT_DTErrors_v1 = cms.Path( process.hltGtDigis + process.hltPreAlCaDTErrors + process.hltDTROMonitorFilter + process.hltDynAlCaDTErrors + process.HLTEndSequence )
process.AlCa_EcalPi0_v3 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sAlCaEcalPi0Eta + process.hltPreAlCaEcalPi0 + process.HLTDoRegionalPi0EtaSequence + process.hltSimple3x3Clusters + process.hltAlCaPi0RecHitsFilter + process.HLTEndSequence )
process.AlCa_EcalEta_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sAlCaEcalPi0Eta + process.hltPreAlCaEcalEta + process.hltSimple3x3Clusters + process.HLTDoRegionalPi0EtaSequence + process.hltAlCaEtaRecHitsFilter + process.HLTEndSequence )
process.AlCa_EcalPhiSym_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1BscMinBiasORBptxPlusANDMinus + process.hltPreAlCaEcalPhiSym + process.hltEcalRawToRecHitFacility + process.hltESRawToRecHitFacility + process.hltEcalRegionalRestFEDs + process.hltEcalRecHitAll + process.hltAlCaPhiSymStream + process.HLTEndSequence )
process.AlCa_RPCMuonNoTriggers_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sAlCaRPC + process.hltPreRPCMuonNoTriggers + process.hltRPCMuonNoTriggersL1Filtered0 + process.HLTmuonlocalrecoSequence + process.HLTEndSequence )
process.AlCa_RPCMuonNoHits_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sAlCaRPC + process.hltPreRPCMuonNoHits + process.HLTmuonlocalrecoSequence + process.hltRPCPointProducer + process.hltRPCFilter + process.HLTEndSequence )
process.AlCa_RPCMuonNormalisation_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sAlCaRPC + process.hltPreRPCMuonNorma + process.hltRPCMuonNormaL1Filtered0 + process.HLTmuonlocalrecoSequence + process.HLTEndSequence )
process.DQM_FEDIntegrity_v2 = cms.Path( process.HLTBeginSequence + process.hltPreFEDIntegrity + process.hltCSCMonitorModule + process.hltDTDQMEvF + process.hltEcalRawToRecHitFacility + process.hltEcalRegionalRestFEDs + process.hltEcalRecHitAll + process.hltEcalRawToRecHitByproductProducer + process.hltEBHltTask + process.hltEEHltTask + process.hltESFEDIntegrityTask + process.hltHcalDigis + process.hltL1tfed + process.hltSiPixelDigis + process.hltSiPixelHLTSource + process.hltSiStripFEDCheck + process.hltMuonRPCDigis + process.hltRPCFEDIntegrity + process.hltBoolFalse )
process.HLTriggerFinalPath = cms.Path( process.hltGtDigis + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW + process.hltBoolTrue )

process.AOutput = cms.EndPath( process.hltOutputA )
process.ALCAP0Output = cms.EndPath( process.hltPreALCAP0Output + process.hltOutputALCAP0 )
process.ALCAPHISYMOutput = cms.EndPath( process.hltPreALCAPHISYMOutput + process.hltOutputALCAPHISYM )
process.CalibrationOutput = cms.EndPath( process.hltPreCalibrationOutput + process.hltOutputCalibration )
process.DQMOutput = cms.EndPath( process.hltDQML1Scalers + process.hltDQML1SeedLogicScalers + process.hltDQMHLTScalers + process.hltPreDQMOutput + process.hltPreDQMOutputSmart + process.hltOutputDQM )
process.EcalCalibrationOutput = cms.EndPath( process.hltPreEcalCalibrationOutput + process.hltOutputEcalCalibration )
process.ExpressOutput = cms.EndPath( process.hltPreExpressOutput + process.hltPreExpressOutputSmart + process.hltOutputExpress )
process.HLTDQMOutput = cms.EndPath( process.hltPreHLTDQMOutput + process.hltPreHLTDQMOutputSmart + process.hltOutputHLTDQM )
process.HLTDQMResultsOutput = cms.EndPath( process.hltPreHLTDQMResultsOutput + process.hltOutputHLTDQMResults )
process.HLTMONOutput = cms.EndPath( process.hltPreHLTMONOutput + process.hltPreHLTMONOutputSmart + process.hltOutputHLTMON )
process.NanoDSTOutput = cms.EndPath( process.hltPreNanoDSTOutput + process.hltOutputNanoDST )
process.OnlineErrorsOutput = cms.EndPath( process.hltPreOnlineErrorsOutput + process.hltOutputOnlineErrors )
process.RPCMONOutput = cms.EndPath( process.hltPreRPCMONOutput + process.hltOutputRPCMON )

process.HLTSchedule = cms.Schedule( *(process.HLT_L1SingleJet36_v1, process.HLT_Jet30_v1, process.HLT_Jet60_v1, process.HLT_Jet80_v1, process.HLT_Jet110_v1, process.HLT_Jet150_v1, process.HLT_Jet190_v1, process.HLT_Jet240_v1, process.HLT_Jet370_v1, process.HLT_Jet370_NoJetID_v1, process.HLT_DiJetAve15U_v4, process.HLT_DiJetAve30U_v4, process.HLT_DiJetAve50U_v4, process.HLT_DiJetAve70U_v4, process.HLT_DiJetAve100U_v4, process.HLT_DiJetAve140U_v4, process.HLT_DiJetAve180U_v4, process.HLT_DiJetAve300U_v4, process.HLT_DoubleJet30_ForwardBackward_v1, process.HLT_DoubleJet60_ForwardBackward_v1, process.HLT_DoubleJet70_ForwardBackward_v1, process.HLT_DoubleJet80_ForwardBackward_v1, process.HLT_CentralJet80_MET65_v1, process.HLT_CentralJet80_MET80_v1, process.HLT_CentralJet80_MET100_v1, process.HLT_CentralJet80_MET160_v1, process.HLT_DiJet60_MET45_v1, process.HLT_DiJet70_PT70_v1, process.HLT_DiJet100_PT100_v1, process.HLT_DiJet130_PT130_v1, process.HLT_QuadJet40_v1, process.HLT_QuadJet40_IsoPFTau40_v1, process.HLT_QuadJet50_BTagIP_v1, process.HLT_QuadJet50_Jet40_v1, process.HLT_QuadJet60_v1, process.HLT_QuadJet70_v1, process.HLT_ExclDiJet60_HFOR_v1, process.HLT_ExclDiJet60_HFAND_v1, process.HLT_JetE30_NoBPTX_v1, process.HLT_JetE30_NoBPTX_NoHalo_v2, process.HLT_JetE30_NoBPTX3BX_NoHalo_v2, process.HLT_HT160_v2, process.HLT_HT240_v2, process.HLT_HT260_v2, process.HLT_HT260_MHT60_v2, process.HLT_HT300_v2, process.HLT_HT300_MHT75_v2, process.HLT_HT360_v2, process.HLT_HT440_v2, process.HLT_HT520_v2, process.HLT_PFMHT150_v1, process.HLT_MET100_v1, process.HLT_MET120_v1, process.HLT_MET200_v1, process.HLT_Meff440_v2, process.HLT_Meff520_v2, process.HLT_Meff640_v2, process.HLT_MR100_v1, process.HLT_R032_v1, process.HLT_R032_MR100_v1, process.HLT_R035_MR100_v1, process.HLT_L1SingleMuOpen_v1, process.HLT_L1SingleMuOpen_DT_v1, process.HLT_L1SingleMu10_v1, process.HLT_L1SingleMu20_v1, process.HLT_L1DoubleMu0_v1, process.HLT_L2MuOpen_NoVertex_v1, process.HLT_L2Mu10_v1, process.HLT_L2Mu20_v1, process.HLT_L2DoubleMu0_v2, process.HLT_Mu3_v3, process.HLT_Mu5_v3, process.HLT_Mu8_v1, process.HLT_Mu12_v1, process.HLT_Mu15_v2, process.HLT_Mu20_v1, process.HLT_Mu24_v1, process.HLT_Mu30_v1, process.HLT_IsoMu12_v1, process.HLT_IsoMu15_v5, process.HLT_IsoMu17_v5, process.HLT_IsoMu24_v1, process.HLT_IsoMu30_v1, process.HLT_L2DoubleMu35_NoVertex_v1, process.HLT_DoubleMu3_v3, process.HLT_DoubleMu6_v1, process.HLT_DoubleMu7_v1, process.HLT_DoubleMu3_Bs_v1, process.HLT_DoubleMu3_Jpsi_v1, process.HLT_DoubleMu3_Quarkonium_v1, process.HLT_DoubleMu4_Acoplanarity03_v1, process.HLT_TripleMu5_v2, process.HLT_Mu5_TkMu0_OST_Jpsi_Tight_B5Q7_v1, process.HLT_Mu5_L2Mu2_v1, process.HLT_Mu5_L2Mu2_Jpsi_v1, process.HLT_Mu3_Track3_Jpsi_v4, process.HLT_Mu7_Track5_Jpsi_v1, process.HLT_Mu7_Track7_Jpsi_v1, process.HLT_L1SingleEG5_v1, process.HLT_Photon30_CaloIdVL_v1, process.HLT_Photon30_CaloIdVL_IsoL_v1, process.HLT_Photon75_CaloIdVL_v1, process.HLT_Photon75_CaloIdVL_IsoL_v1, process.HLT_Photon125_NoSpikeFilter_v1, process.HLT_DoublePhoton5_IsoVL_CEP_v1, process.HLT_DoublePhoton33_v1, process.HLT_Ele8_v1, process.HLT_Ele8_CaloIdL_CaloIsoVL_v1, process.HLT_Ele8_CaloIdL_TrkIdVL_v1, process.HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1, process.HLT_Ele17_CaloIdL_CaloIsoVL_v1, process.HLT_Ele27_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_v1, process.HLT_Ele45_CaloIdVT_TrkIdT_v1, process.HLT_Ele90_NoSpikeFilter_v1, process.HLT_Photon20_R9Id_Photon18_R9Id_v1, process.HLT_Photon20_CaloIdVT_IsoT_Ele8_CaloIdL_CaloIsoVL_v1, process.HLT_Photon26_Photon18_v1, process.HLT_Photon26_IsoVL_Photon18_v1, process.HLT_Photon26_IsoVL_Photon18_IsoVL_v1, process.HLT_Photon26_CaloIdL_IsoVL_Photon18_v1, process.HLT_Photon26_CaloIdL_IsoVL_Photon18_CaloIdL_IsoVL_v1, process.HLT_Photon32_CaloIdL_Photon26_CaloIdL_v1, process.HLT_Photon60_CaloIdL_HT200_v1, process.HLT_Photon70_CaloIdL_HT200_v1, process.HLT_Photon70_CaloIdL_HT300_v1, process.HLT_Photon70_CaloIdL_MHT30_v1, process.HLT_Photon70_CaloIdL_MHT50_v1, process.HLT_Ele17_CaloIdL_CaloIsoVL_Ele8_CaloIdL_CaloIsoVL_v1, process.HLT_Ele17_CaloIdVT_CaloIsoVT_TrkIdT_TrkIsoVT_SC8_Mass30_v2, process.HLT_Ele17_CaloIdL_CaloIsoVL_Ele15_HFL_v1, process.HLT_Ele32_CaloIdL_CaloIsoVL_SC17_v1, process.HLT_IsoPFTau35_Trk20_MET45_v1, process.HLT_DoubleIsoPFTau20_Trk5_v1, process.HLT_BTagMu_DiJet20_Mu5_v1, process.HLT_BTagMu_DiJet60_Mu7_v1, process.HLT_BTagMu_DiJet80_Mu9_v1, process.HLT_Mu3_Ele8_CaloIdL_TrkIdVL_HT160_v2, process.HLT_Mu3_Ele8_CaloIdT_TrkIdVL_HT160_v2, process.HLT_Mu5_Ele8_CaloIdL_TrkIdVL_Ele8_v2, process.HLT_Mu5_DoubleEle8_v2, process.HLT_Mu5_HT200_v3, process.HLT_Mu8_HT200_v2, process.HLT_Mu8_Ele17_CaloIdL_v1, process.HLT_Mu8_Photon20_CaloIdVT_IsoT_v2, process.HLT_Mu8_Jet40_v2, process.HLT_Mu10_Ele10_CaloIdL_v2, process.HLT_Mu15_Photon20_CaloIdL_v2, process.HLT_Mu15_DoublePhoton15_CaloIdL_v2, process.HLT_Mu15_LooseIsoPFTau20_v1, process.HLT_Mu17_CentralJet30_v1, process.HLT_Mu17_DiCentralJet30_v1, process.HLT_Mu17_TriCentralJet30_v1, process.HLT_Mu17_Ele8_CaloIdL_v1, process.HLT_Mu17_CentralJet40_BTagIP_v1, process.HLT_IsoMu17_CentralJet40_BTagIP_v1, process.HLT_IsoMu12_LooseIsoPFTau10_v1, process.HLT_DoubleMu3_HT160_v2, process.HLT_DoubleMu3_HT200_v2, process.HLT_DoubleMu5_Ele8_v2, process.HLT_DoubleMu5_Ele8_CaloIdL_TrkIdVL_v2, process.HLT_Ele8_CaloIdL_CaloIsoVL_Jet40_v1, process.HLT_Ele10_CaloIdL_CaloIsoVL_TrkIdVL_TrkIsoVL_HT200_v2, process.HLT_Ele10_CaloIdT_CaloIsoVL_TrkIdT_TrkIsoVL_HT200_v2, process.HLT_Ele15_CaloIdVT_TrkIdT_LooseIsoPFTau15_v1, process.HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau15_v1, process.HLT_Ele15_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_LooseIsoPFTau20_v1, process.HLT_Ele25_CaloIdVT_TrkIdT_CentralJet30_v1, process.HLT_Ele25_CaloIdVT_TrkIdT_CentralDiJet30_v1, process.HLT_Ele25_CaloIdVT_TrkIdT_CentralTriJet30_v1, process.HLT_Ele25_CaloIdVT_TrkIdT_CentralJet40_BTagIP_v1, process.HLT_DoubleEle8_CaloIdL_TrkIdVL_HT160_v2, process.HLT_DoubleEle8_CaloIdT_TrkIdVL_HT160_v2, process.HLT_DoubleEle10_CaloIdL_TrkIdVL_Ele10_v1, process.HLT_TripleEle10_CaloIdL_TrkIdVL_v1, process.HLT_Photon20_EBOnly_NoSpikeFilter_v1, process.HLT_Photon20_NoSpikeFilter_v1, process.HLT_Spike20_v1, process.HLT_PixelTracks_Multiplicity110_v1, process.HLT_PixelTracks_Multiplicity125_v1, process.HLT_BeamGas_HF_v1, process.HLT_BeamGas_BSC_v1, process.HLT_L1_BeamHalo_v1, process.HLT_L1Tech_BSC_minBias_threshold1_v2, process.HLT_L1Tech_BSC_halo_v1, process.HLT_L1_PreCollisions_v1, process.HLT_L1_Interbunch_BSC_v1, process.HLT_IsoTrackHE_v3, process.HLT_IsoTrackHB_v2, process.HLT_HcalPhiSym_v2, process.HLT_HcalNZS_v2, process.HLT_GlobalRunHPDNoise_v2, process.HLT_L1Tech_HBHEHO_totalOR_v1, process.HLT_ZeroBias_v1, process.HLT_Physics_v1, process.HLT_Physics_NanoDST_v1, process.HLT_Calibration_v1, process.HLT_EcalCalibration_v1, process.HLT_HcalCalibration_v1, process.HLT_TrackerCalibration_v1, process.HLT_Random_v1, process.HLT_L1MuOpen_AntiBPTX_v2, process.HLT_L1TrackerCosmics_v2, process.HLT_RegionalCosmicTracking_v1, process.HLT_L3MuonsCosmicTracking_v1, process.HLT_LogMonitor_v1, process.HLT_DTErrors_v1, process.AlCa_EcalPi0_v3, process.AlCa_EcalEta_v2, process.AlCa_EcalPhiSym_v2, process.AlCa_RPCMuonNoTriggers_v2, process.AlCa_RPCMuonNoHits_v2, process.AlCa_RPCMuonNormalisation_v2, process.DQM_FEDIntegrity_v2, process.HLTriggerFinalPath, process.AOutput, process.ALCAP0Output, process.ALCAPHISYMOutput, process.CalibrationOutput, process.DQMOutput, process.EcalCalibrationOutput, process.ExpressOutput, process.HLTDQMOutput, process.HLTDQMResultsOutput, process.HLTMONOutput, process.NanoDSTOutput, process.OnlineErrorsOutput, process.RPCMONOutput ))
