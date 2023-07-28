# /cdaq/special/Tests/HighRateTest/v3.3/HLT/V4 (CMSSW_8_0_19_patch2)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "HLT" )

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/cdaq/special/Tests/HighRateTest/v3.3/HLT/V4')
)

process.HLTPSetInitialStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetInitialStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetInitialStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 3 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPInitialStepChi2ChargeMeasurementEstimator30" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
process.HLTPSetDetachedStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 3 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
process.HLTPSetPixelPairStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 3 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
process.HLTPSetMixedStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForMixedStep" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMixedStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMixedStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 2 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeTightMeasurementEstimator16" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialForMixedStepOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
process.HLTPSetPixelLessStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelLessStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelLessStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 2 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeTightMeasurementEstimator16" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 4 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
process.transferSystem = cms.PSet( 
  destinations = cms.vstring( 'Tier0',
    'DQM',
    'ECAL',
    'EventDisplay',
    'Lustre',
    'None' ),
  transferModes = cms.vstring( 'default',
    'test',
    'emulator' ),
  streamA = cms.PSet( 
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'Lustre' )
  ),
  streamCalibration = cms.PSet( 
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamDQM = cms.PSet( 
    default = cms.vstring( 'DQM' ),
    test = cms.vstring( 'DQM',
      'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamDQMCalibration = cms.PSet( 
    default = cms.vstring( 'DQM' ),
    test = cms.vstring( 'DQM',
      'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamEcalCalibration = cms.PSet( 
    default = cms.vstring( 'ECAL' ),
    test = cms.vstring( 'ECAL' ),
    emulator = cms.vstring( 'None' )
  ),
  streamEventDisplay = cms.PSet( 
    default = cms.vstring( 'EventDisplay',
      'Tier0' ),
    test = cms.vstring( 'EventDisplay',
      'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamExpressCosmics = cms.PSet( 
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'Lustre' )
  ),
  streamNanoDST = cms.PSet( 
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamRPCMON = cms.PSet( 
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  streamTrackerCalibration = cms.PSet( 
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'None' )
  ),
  default = cms.PSet( 
    default = cms.vstring( 'Tier0' ),
    test = cms.vstring( 'Lustre' ),
    emulator = cms.vstring( 'Lustre' ),
    streamLookArea = cms.PSet(  )
  ),
  streamLookArea = cms.PSet( 
    default = cms.vstring( 'DQM' ),
    test = cms.vstring( 'DQM',
      'Lustre' ),
    emulator = cms.vstring( 'None' )
  )
)
process.HLTPSetTrajectoryBuilderForGsfElectrons = cms.PSet( 
  propagatorAlong = cms.string( "hltESPFwdElectronPropagator" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryFilterForElectrons" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "hltESPBwdElectronPropagator" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator2000" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 90.0 )
)
process.HLTIter4PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter4PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter4ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeLooseMeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  minNrOfHitsForRebuild = cms.untracked.int32( 4 )
)
process.HLTIter3PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter3PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter3ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeLooseMeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTIter2PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter2ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTIter1PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter1PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter1ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetTrajectoryBuilderForElectrons = cms.PSet( 
  propagatorAlong = cms.string( "hltESPFwdElectronPropagator" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryFilterForElectrons" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "hltESPBwdElectronPropagator" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 90.0 )
)
process.HLTPSetMuTrackJpsiTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuTrackJpsiTrajectoryFilter" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetMuTrackJpsiEffTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuTrackJpsiEffTrajectoryFilter" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetMuonCkfTrajectoryBuilderSeedHit = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryFilter" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "MuonCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  useSeedLayer = cms.bool( True ),
  deltaEta = cms.double( -1.0 ),
  deltaPhi = cms.double( -1.0 ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetMuonCkfTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryFilter" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "MuonCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  useSeedLayer = cms.bool( False ),
  deltaEta = cms.double( -1.0 ),
  deltaPhi = cms.double( -1.0 ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetPvClusterComparer = cms.PSet( 
  track_pt_min = cms.double( 2.5 ),
  track_pt_max = cms.double( 10.0 ),
  track_chi2_max = cms.double( 9999999.0 ),
  track_prob_min = cms.double( -1.0 )
)
process.HLTIter0PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetPvClusterComparerForBTag = cms.PSet( 
  track_pt_min = cms.double( 0.1 ),
  track_pt_max = cms.double( 20.0 ),
  track_chi2_max = cms.double( 20.0 ),
  track_prob_min = cms.double( -1.0 )
)
process.HLTSeedFromConsecutiveHitsTripletOnlyCreator = cms.PSet( 
  ComponentName = cms.string( "SeedFromConsecutiveHitsTripletOnlyCreator" ),
  propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  MinOneOverPtError = cms.double( 1.0 ),
  magneticField = cms.string( "ParabolicMf" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  forceKinematicWithRegionDirection = cms.bool( False )
)
process.HLTSeedFromConsecutiveHitsCreator = cms.PSet( 
  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
  propagator = cms.string( "PropagatorWithMaterial" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  MinOneOverPtError = cms.double( 1.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  forceKinematicWithRegionDirection = cms.bool( False ),
  magneticField = cms.string( "" )
)
process.HLTIter0HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 4 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTIter2HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2HighPtTkMuPSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "hltIter2HighPtTkMuESPMeasurementTracker" )
)
process.HLTPSetPvClusterComparerForIT = cms.PSet( 
  track_pt_min = cms.double( 1.0 ),
  track_pt_max = cms.double( 20.0 ),
  track_chi2_max = cms.double( 20.0 ),
  track_prob_min = cms.double( -1.0 )
)
process.HLTSiStripClusterChargeCutNone = cms.PSet(  value = cms.double( -1.0 ) )
process.HLTSiStripClusterChargeCutLoose = cms.PSet(  value = cms.double( 1620.0 ) )
process.HLTSiStripClusterChargeCutTight = cms.PSet(  value = cms.double( 1945.0 ) )
process.HLTSeedFromConsecutiveHitsCreatorIT = cms.PSet( 
  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
  propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  MinOneOverPtError = cms.double( 1.0 ),
  magneticField = cms.string( "ParabolicMf" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  forceKinematicWithRegionDirection = cms.bool( False )
)
process.HLTSeedFromProtoTracks = cms.PSet( 
  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
  propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  MinOneOverPtError = cms.double( 1.0 ),
  magneticField = cms.string( "ParabolicMf" ),
  TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  forceKinematicWithRegionDirection = cms.bool( False )
)
process.HLTPSetMuonTrackingRegionBuilder8356 = cms.PSet( 
  Rescale_eta = cms.double( 3.0 ),
  Rescale_phi = cms.double( 3.0 ),
  Rescale_Dz = cms.double( 3.0 ),
  EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
  EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
  PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
  PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
  UseVertex = cms.bool( False ),
  Pt_fixed = cms.bool( False ),
  Z_fixed = cms.bool( True ),
  Phi_fixed = cms.bool( False ),
  Eta_fixed = cms.bool( False ),
  Pt_min = cms.double( 1.5 ),
  Phi_min = cms.double( 0.1 ),
  Eta_min = cms.double( 0.1 ),
  DeltaZ = cms.double( 15.9 ),
  DeltaR = cms.double( 0.2 ),
  DeltaEta = cms.double( 0.2 ),
  DeltaPhi = cms.double( 0.2 ),
  maxRegions = cms.int32( 2 ),
  precise = cms.bool( True ),
  OnDemand = cms.int32( -1 ),
  MeasurementTrackerName = cms.InputTag( "hltESPMeasurementTracker" ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  vertexCollection = cms.InputTag( "pixelVertices" ),
  input = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
process.HLTPSetDetachedCkfTrajectoryBuilderForHI = cms.PSet( 
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryFilterForHI" ) ),
  maxCand = cms.int32( 2 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator9" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryFilterForHI" ) ),
  useSameTrajFilter = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 0.0 ),
  maxPtForLooperReconstruction = cms.double( 0.0 ),
  bestHitOnly = cms.bool( True )
)
process.HLTPSetPixelPairCkfTrajectoryBuilderForHI = cms.PSet( 
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryFilterForHI" ) ),
  maxCand = cms.int32( 3 ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9ForHI" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryFilterForHI" ) ),
  useSameTrajFilter = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  bestHitOnly = cms.bool( True )
)
process.HLTSiStripClusterChargeCutForHI = cms.PSet(  value = cms.double( 2069.0 ) )
process.HLTPSetDetachedCkfTrajectoryBuilderForHIGlobalPt8 = cms.PSet( 
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8" ) ),
  maxCand = cms.int32( 2 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator9" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8" ) ),
  useSameTrajFilter = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 0.0 ),
  maxPtForLooperReconstruction = cms.double( 0.0 ),
  bestHitOnly = cms.bool( True )
)
process.HLTPSetPixelPairCkfTrajectoryBuilderForHIGlobalPt8 = cms.PSet( 
  MeasurementTrackerName = cms.string( "" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8" ) ),
  maxCand = cms.int32( 3 ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9ForHI" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8" ) ),
  useSameTrajFilter = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  bestHitOnly = cms.bool( True )
)
process.HLTPSetInitialCkfTrajectoryBuilderForHI = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialForHI" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetInitialCkfTrajectoryFilterForHI" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  intermediateCleaning = cms.bool( False ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTSiStripClusterChargeCutTiny = cms.PSet(  value = cms.double( 800.0 ) )
process.HLTPSetTobTecStepTrajectoryBuilder = cms.PSet( 
  MeasurementTrackerName = cms.string( "" ),
  useSameTrajFilter = cms.bool( False ),
  minNrOfHitsForRebuild = cms.int32( 4 ),
  alwaysUseInvalidHits = cms.bool( False ),
  maxCand = cms.int32( 2 ),
  estimator = cms.string( "hltESPChi2ChargeTightMeasurementEstimator16" ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTobTecStepTrajectoryFilterBase" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTobTecStepInOutTrajectoryFilterBase" ) ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
)
process.HLTPSetLowPtStepTrajectoryBuilder = cms.PSet( 
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  bestHitOnly = cms.bool( True ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtStepTrajectoryFilter" ) ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetLowPtStepTrajectoryFilter" ) ),
  useSameTrajFilter = cms.bool( True ),
  maxCand = cms.int32( 4 ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "" ),
  lockHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  maxPtForLooperReconstruction = cms.double( 0.7 )
)
process.HLTPSetDetachedStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CompositeTrajectoryFilter" ),
  filters = cms.VPSet( 
    cms.PSet(  refToPSet_ = cms.string( "HLTPSetDetachedStepTrajectoryFilterBase" )    )
  )
)
process.HLTPSetInitialStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CompositeTrajectoryFilter" ),
  filters = cms.VPSet( 
    cms.PSet(  refToPSet_ = cms.string( "HLTPSetInitialStepTrajectoryFilterBase" )    )
  )
)
process.HLTPSetPixelPairStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CompositeTrajectoryFilter" ),
  filters = cms.VPSet( 
    cms.PSet(  refToPSet_ = cms.string( "HLTPSetPixelPairStepTrajectoryFilterBase" )    )
  )
)
process.HLTPSetInitialStepTrajectoryFilterBase = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.2 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  maxCCCLostHits = cms.int32( 2 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  seedPairPenalty = cms.int32( 0 ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.HLTPSetDetachedStepTrajectoryFilterBase = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.075 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  maxCCCLostHits = cms.int32( 2 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  seedPairPenalty = cms.int32( 0 ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.HLTPSetPixelPairStepTrajectoryFilterBase = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  maxCCCLostHits = cms.int32( 2 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  seedPairPenalty = cms.int32( 0 ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.HLTPSetMixedStepTrajectoryFilterBase = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  seedPairPenalty = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.05 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 0 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.HLTPSetPixelLessStepTrajectoryFilterBase = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 4 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.05 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 0 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTIter4PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 6 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTIter3PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTIter2PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  maxCCCLostHits = cms.int32( 1 ),
  seedExtension = cms.int32( 1 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTIter1PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.2 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  maxCCCLostHits = cms.int32( 1 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTPSetbJetRegionalTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 1.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 8 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTPSetTrajectoryFilterL3 = cms.PSet( 
  minPt = cms.double( 0.5 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 1000000000 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTPSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTPSetTrajectoryFilterForElectrons = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minPt = cms.double( 2.0 ),
  minHitsMinPt = cms.int32( -1 ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minimumNumberOfHits = cms.int32( 5 ),
  chargeSignificance = cms.double( -1.0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTPSetMuonCkfTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 0.9 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minimumNumberOfHits = cms.int32( 5 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTPSetMuTrackJpsiTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 10.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 8 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTPSetMuTrackJpsiEffTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 1.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 9 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTPSetCkfTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 0.9 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTPSetCkf3HitTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 0.9 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTIter0PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  maxCCCLostHits = cms.int32( 1 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTIter2HighPtTkMuPSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 3 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTPSetDetachedCkfTrajectoryFilterForHI = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 6 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 1 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  constantValueForLostHitsFractionFilter = cms.double( 0.701 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTPSetPixelPairCkfTrajectoryFilterForHI = cms.PSet( 
  minPt = cms.double( 1.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 6 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTPSetDetachedCkfTrajectoryFilterForHIGlobalPt8 = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 6 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 8.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 1 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  constantValueForLostHitsFractionFilter = cms.double( 0.701 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTPSetPixelPairCkfTrajectoryFilterForHIGlobalPt8 = cms.PSet( 
  minPt = cms.double( 8.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 6 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTPSetInitialCkfTrajectoryFilterForHI = cms.PSet( 
  minimumNumberOfHits = cms.int32( 6 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 999 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minPt = cms.double( 0.9 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  maxCCCLostHits = cms.int32( 9999 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 )
)
process.HLTPSetTobTecStepTrajectoryFilterBase = cms.PSet( 
  maxLostHits = cms.int32( 0 ),
  minimumNumberOfHits = cms.int32( 5 ),
  seedPairPenalty = cms.int32( 1 ),
  minPt = cms.double( 0.1 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  chargeSignificance = cms.double( -1.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  strictSeedExtension = cms.bool( False ),
  seedExtension = cms.int32( 0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.HLTPSetTobTecStepInOutTrajectoryFilterBase = cms.PSet( 
  maxLostHits = cms.int32( 0 ),
  minimumNumberOfHits = cms.int32( 4 ),
  seedPairPenalty = cms.int32( 1 ),
  minPt = cms.double( 0.1 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  chargeSignificance = cms.double( -1.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  strictSeedExtension = cms.bool( False ),
  seedExtension = cms.int32( 0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.HLTPSetLowPtStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  seedPairPenalty = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.075 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 1 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.HLTPSetMixedStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 3 ),
  seedPairPenalty = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 999 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.4 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.HLTPSetPixelLessStepTrajectoryFilter = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minimumNumberOfHits = cms.int32( 4 ),
  seedPairPenalty = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  minPt = cms.double( 0.1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHits = cms.int32( 0 ),
  maxConsecLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  constantValueForLostHitsFractionFilter = cms.double( 2.0 ),
  seedExtension = cms.int32( 0 ),
  strictSeedExtension = cms.bool( False ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsForLoopers = cms.int32( 13 )
)
process.streams = cms.PSet( 
  ALCALUMIPIXELS = cms.vstring( 'AlCaLumiPixels' ),
  ALCAPHISYM = cms.vstring( 'AlCaPhiSym' ),
  Calibration = cms.vstring( 'TestEnablesEcalHcal' ),
  DQM = cms.vstring( 'OnlineMonitor' ),
  DQMCalibration = cms.vstring( 'TestEnablesEcalHcalDQM' ),
  DQMEventDisplay = cms.vstring( 'CosmicsForEventDisplay' ),
  EcalCalibration = cms.vstring( 'EcalLaser' ),
  ExpressCosmics = cms.vstring( 'ExpressCosmics' ),
  NanoDST = cms.vstring( 'L1Accept' ),
  Physics = cms.vstring( 'Cosmics',
    'HLTPhysics',
    'HcalNZS',
    'MinimumBias' ),
  RPCMON = cms.vstring( 'RPCMonitor' )
)
process.datasets = cms.PSet( 
  AlCaLumiPixels = cms.vstring( 'AlCa_LumiPixels_Random_v1',
    'AlCa_LumiPixels_ZeroBias_v2' ),
  AlCaPhiSym = cms.vstring( 'AlCa_EcalPhiSym_v4' ),
  Cosmics = cms.vstring( 'HLT_L1SingleMu3_v1',
    'HLT_L1SingleMu5_v1',
    'HLT_L1SingleMu7_v1',
    'HLT_L1SingleMuOpen_DT_v2',
    'HLT_L1SingleMuOpen_v2' ),
  CosmicsForEventDisplay = cms.vstring( 'HLT_L1SingleMu7_v1' ),
  EcalLaser = cms.vstring( 'HLT_EcalCalibration_v2' ),
  ExpressCosmics = cms.vstring( 'HLT_L1SingleMuOpen_DT_v2',
    'HLT_L1SingleMuOpen_v2',
    'HLT_Random_v1' ),
  HLTPhysics = cms.vstring( 'HLT_Physics_v2' ),
  HcalNZS = cms.vstring( 'HLT_HcalNZS_v2',
    'HLT_HcalPhiSym_v2' ),
  L1Accept = cms.vstring( 'DST_Physics_v1' ),
  MinimumBias = cms.vstring( 'HLT_L1SingleEG5_v1',
    'HLT_L1TowerCount40_v1',
    'HLT_Physics_v2',
    'HLT_Random_v1',
    'HLT_ZeroBias_v2' ),
  OnlineMonitor = cms.vstring( 'HLT_HcalNZS_v2',
    'HLT_HcalPhiSym_v2',
    'HLT_L1DoubleMu0_v1',
    'HLT_L1FatEvents_v1',
    'HLT_L1SingleEG5_v1',
    'HLT_L1SingleMu3_v1',
    'HLT_L1SingleMu5_v1',
    'HLT_L1SingleMu7_v1',
    'HLT_L1SingleMuOpen_DT_v2',
    'HLT_L1SingleMuOpen_v2',
    'HLT_Physics_v2',
    'HLT_Random_v1',
    'HLT_ZeroBias_v2' ),
  RPCMonitor = cms.vstring( 'AlCa_RPCMuonNoHits_v2',
    'AlCa_RPCMuonNoTriggers_v2',
    'AlCa_RPCMuonNormalisation_v2' ),
  TestEnablesEcalHcal = cms.vstring( 'HLT_EcalCalibration_v2',
    'HLT_HcalCalibration_v1' ),
  TestEnablesEcalHcalDQM = cms.vstring( 'HLT_EcalCalibration_v2',
    'HLT_HcalCalibration_v1' )
)

process.source = cms.Source( "FedRawDataInputSource",
    numBuffers = cms.untracked.uint32( 2 ),
    useL1EventID = cms.untracked.bool( False ),
    eventChunkSize = cms.untracked.uint32( 32 ),
    fileNames = cms.untracked.vstring(  ),
    verifyChecksum = cms.untracked.bool( True ),
    eventChunkBlock = cms.untracked.uint32( 32 ),
    verifyAdler32 = cms.untracked.bool( True ),
    maxBufferedFiles = cms.untracked.uint32( 2 ),
    fileListMode = cms.untracked.bool( False )
)

process.GlobalParametersRcdSource = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "L1TGlobalParametersRcd" ),
    firstValid = cms.vuint32( 1 )
)
process.CSCChannelMapperESSource = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "CSCChannelMapperRecord" ),
    firstValid = cms.vuint32( 1 )
)
process.CSCINdexerESSource = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "CSCIndexerRecord" ),
    firstValid = cms.vuint32( 1 )
)
process.GlobalTag = cms.ESSource( "PoolDBESSource",
    globaltag = cms.string( "80X_dataRun2_HLT_v12" ),
    RefreshEachRun = cms.untracked.bool( True ),
    snapshotTime = cms.string( "" ),
    toGet = cms.VPSet( 
    ),
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
    RefreshAlways = cms.untracked.bool( False ),
    connect = cms.string( "frontier://(proxyurl=http://localhost:3128)(serverurl=http://localhost:8000/FrontierOnProd)(serverurl=http://localhost:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_CONDITIONS" ),
    ReconnectEachRun = cms.untracked.bool( True ),
    RefreshOpenIOVs = cms.untracked.bool( False ),
    DumpStat = cms.untracked.bool( False )
)
process.HepPDTESSource = cms.ESSource( "HepPDTESSource",
    pdtFileName = cms.FileInPath( "SimGeneral/HepPDTESSource/data/pythiaparticle.tbl" )
)
process.StableParametersRcdSource = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "L1TGlobalStableParametersRcd" ),
    firstValid = cms.vuint32( 1 )
)
process.eegeom = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "EcalMappingRcd" ),
    firstValid = cms.vuint32( 1 )
)
process.es_hardcode = cms.ESSource( "HcalHardcodeCalibrations",
    fromDDD = cms.untracked.bool( False ),
    toGet = cms.untracked.vstring( 'GainWidths' )
)
process.hltESSBTagRecord = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "JetTagComputerRecord" ),
    firstValid = cms.vuint32( 1 )
)
process.hltESSEcalSeverityLevel = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "EcalSeverityLevelAlgoRcd" ),
    firstValid = cms.vuint32( 1 )
)
process.hltESSHcalSeverityLevel = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "HcalSeverityLevelComputerRcd" ),
    firstValid = cms.vuint32( 1 )
)

process.hltESPPixelLessStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPPixelLessStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.11 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
process.hltESPTobTecStepFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 30.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPTobTecStepRKFitter" ),
  MinNumberOfHits = cms.int32( 7 ),
  Smoother = cms.string( "hltESPTobTecStepRKSmoother" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  ComponentName = cms.string( "hltESPTobTecStepFitterSmoother" ),
  RejectTracks = cms.bool( True )
)
process.hltESPTobTecStepFittingSmootherForLoopers = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 30.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPTobTecStepRKFitterForLoopers" ),
  MinNumberOfHits = cms.int32( 7 ),
  Smoother = cms.string( "hltESPTobTecStepRKSmootherForLoopers" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  ComponentName = cms.string( "hltESPTobTecStepFitterSmootherForLoopers" ),
  RejectTracks = cms.bool( True )
)
process.hltESPLowPtStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPLowPtStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.16 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
process.hltESPTobTecStepRKTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 7 ),
  ComponentName = cms.string( "hltESPTobTecStepRKSmoother" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPTobTecStepRKTrajectorySmootherForLoopers = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 7 ),
  ComponentName = cms.string( "hltESPTobTecStepRKSmootherForLoopers" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialForLoopers" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPTobTecStepRKTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 7 ),
  ComponentName = cms.string( "hltESPTobTecStepRKFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPTobTecStepRKTrajectoryFitterForLoopers = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 7 ),
  ComponentName = cms.string( "hltESPTobTecStepRKFitterForLoopers" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialForLoopers" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPTobTecStepFlexibleKFFittingSmoother = cms.ESProducer( "FlexibleKFFittingSmootherESProducer",
  ComponentName = cms.string( "hltESPTobTecStepFlexibleKFFittingSmoother" ),
  appendToDataLabel = cms.string( "" ),
  standardFitter = cms.string( "hltESPTobTecStepFitterSmoother" ),
  looperFitter = cms.string( "hltESPTobTecStepFitterSmootherForLoopers" )
)
process.hltESPTobTecStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTobTecStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.09 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
process.hltESPChi2ChargeTightMeasurementEstimator16 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPChi2ChargeTightMeasurementEstimator16" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 16.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
process.hltESPInitialStepChi2ChargeMeasurementEstimator30 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  value = cms.double( 800.0 ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPInitialStepChi2ChargeMeasurementEstimator30" ),
  pTChargeCutThreshold = cms.double( 15.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 30.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
process.hltESPTobTecStepClusterShapeHitFilter = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "hltESPTobTecStepClusterShapeHitFilter" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  PixelShapeFile = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape.par" )
)
process.hltESPPixelLessStepClusterShapeHitFilter = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "hltESPPixelLessStepClusterShapeHitFilter" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  PixelShapeFile = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape.par" )
)
process.hltESPMixedStepClusterShapeHitFilter = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "hltESPMixedStepClusterShapeHitFilter" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTight" ) ),
  PixelShapeFile = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape.par" )
)
process.AnyDirectionAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "AnyDirectionAnalyticalPropagator" ),
  PropagationDirection = cms.string( "anyDirection" )
)
process.CSCChannelMapperESProducer = cms.ESProducer( "CSCChannelMapperESProducer",
  AlgoName = cms.string( "CSCChannelMapperPostls1" )
)
process.CSCGeometryESModule = cms.ESProducer( "CSCGeometryESModule",
  useRealWireGeometry = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  alignmentsLabel = cms.string( "" ),
  useGangedStripsInME1a = cms.bool( False ),
  debugV = cms.untracked.bool( False ),
  useOnlyWiresInME1a = cms.bool( False ),
  useDDD = cms.bool( False ),
  useCentreTIOffsets = cms.bool( False ),
  applyAlignment = cms.bool( True )
)
process.CSCIndexerESProducer = cms.ESProducer( "CSCIndexerESProducer",
  AlgoName = cms.string( "CSCIndexerPostls1" )
)
process.CSCObjectMapESProducer = cms.ESProducer( "CSCObjectMapESProducer",
  appendToDataLabel = cms.string( "" )
)
process.CaloGeometryBuilder = cms.ESProducer( "CaloGeometryBuilder",
  SelectedCalos = cms.vstring( 'HCAL',
    'ZDC',
    'EcalBarrel',
    'EcalEndcap',
    'EcalPreshower',
    'TOWER' )
)
process.CaloTopologyBuilder = cms.ESProducer( "CaloTopologyBuilder" )
process.CaloTowerConstituentsMapBuilder = cms.ESProducer( "CaloTowerConstituentsMapBuilder",
  appendToDataLabel = cms.string( "" ),
  MapFile = cms.untracked.string( "Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz" )
)
process.CaloTowerGeometryFromDBEP = cms.ESProducer( "CaloTowerGeometryFromDBEP",
  applyAlignment = cms.bool( False ),
  hcalTopologyConstants = cms.PSet( 
    maxDepthHE = cms.int32( 3 ),
    maxDepthHB = cms.int32( 2 ),
    mode = cms.string( "HcalTopologyMode::LHC" )
  )
)
process.CaloTowerTopologyEP = cms.ESProducer( "CaloTowerTopologyEP",
  appendToDataLabel = cms.string( "" )
)
process.CastorDbProducer = cms.ESProducer( "CastorDbProducer",
  appendToDataLabel = cms.string( "" )
)
process.ClusterShapeHitFilterESProducer = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "ClusterShapeHitFilter" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  PixelShapeFile = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape.par" )
)
process.DTGeometryESModule = cms.ESProducer( "DTGeometryESModule",
  appendToDataLabel = cms.string( "" ),
  fromDDD = cms.bool( False ),
  applyAlignment = cms.bool( True ),
  alignmentsLabel = cms.string( "" )
)
process.DTObjectMapESProducer = cms.ESProducer( "DTObjectMapESProducer",
  appendToDataLabel = cms.string( "" )
)
process.EcalBarrelGeometryFromDBEP = cms.ESProducer( "EcalBarrelGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
process.EcalElectronicsMappingBuilder = cms.ESProducer( "EcalElectronicsMappingBuilder" )
process.EcalEndcapGeometryFromDBEP = cms.ESProducer( "EcalEndcapGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
process.EcalLaserCorrectionService = cms.ESProducer( "EcalLaserCorrectionService" )
process.EcalPreshowerGeometryFromDBEP = cms.ESProducer( "EcalPreshowerGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
process.HcalGeometryFromDBEP = cms.ESProducer( "HcalGeometryFromDBEP",
  applyAlignment = cms.bool( False ),
  hcalTopologyConstants = cms.PSet( 
    maxDepthHE = cms.int32( 3 ),
    maxDepthHB = cms.int32( 2 ),
    mode = cms.string( "HcalTopologyMode::LHC" )
  )
)
process.HcalTopologyIdealEP = cms.ESProducer( "HcalTopologyIdealEP",
  Exclude = cms.untracked.string( "" ),
  appendToDataLabel = cms.string( "" )
)
process.MaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterial" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.MaterialPropagatorForHI = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForHI" ),
  Mass = cms.double( 0.139 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.MaterialPropagatorParabolicMF = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialParabolicMf" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.OppositeMaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialOpposite" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.OppositeMaterialPropagatorForHI = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialOppositeForHI" ),
  Mass = cms.double( 0.139 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.OppositeMaterialPropagatorParabolicMF = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.OppositePropagatorWithMaterialForMixedStep = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForMixedStepOpposite" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( 0.1 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.ParametrizedMagneticFieldProducer = cms.ESProducer( "AutoParametrizedMagneticFieldProducer",
  version = cms.string( "Parabolic" ),
  valueOverride = cms.int32( -1 ),
  label = cms.untracked.string( "ParabolicMf" )
)
process.PropagatorWithMaterialForLoopers = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForLoopers" ),
  Mass = cms.double( 0.1396 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 4.0 ),
  useRungeKutta = cms.bool( False )
)
process.PropagatorWithMaterialForMixedStep = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialForMixedStep" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( 0.1 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.RPCGeometryESModule = cms.ESProducer( "RPCGeometryESModule",
  useDDD = cms.untracked.bool( False ),
  compatibiltyWith11 = cms.untracked.bool( True )
)
process.SiStripGainESProducer = cms.ESProducer( "SiStripGainESProducer",
  printDebug = cms.untracked.bool( False ),
  appendToDataLabel = cms.string( "" ),
  APVGain = cms.VPSet( 
    cms.PSet(  Record = cms.string( "SiStripApvGainRcd" ),
      NormalizationFactor = cms.untracked.double( 1.0 ),
      Label = cms.untracked.string( "" )
    ),
    cms.PSet(  Record = cms.string( "SiStripApvGain2Rcd" ),
      NormalizationFactor = cms.untracked.double( 1.0 ),
      Label = cms.untracked.string( "" )
    )
  ),
  AutomaticNormalization = cms.bool( False )
)
process.SiStripQualityESProducer = cms.ESProducer( "SiStripQualityESProducer",
  appendToDataLabel = cms.string( "" ),
  PrintDebugOutput = cms.bool( False ),
  ThresholdForReducedGranularity = cms.double( 0.3 ),
  UseEmptyRunInfo = cms.bool( False ),
  ReduceGranularity = cms.bool( False ),
  ListOfRecordToMerge = cms.VPSet( 
    cms.PSet(  record = cms.string( "SiStripDetVOffRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripDetCablingRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripBadChannelRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripBadFiberRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripBadModuleRcd" ),
      tag = cms.string( "" )
    )
  )
)
process.SiStripRecHitMatcherESProducer = cms.ESProducer( "SiStripRecHitMatcherESProducer",
  PreFilter = cms.bool( False ),
  ComponentName = cms.string( "StandardMatcher" ),
  NSigmaInside = cms.double( 3.0 )
)
process.SiStripRegionConnectivity = cms.ESProducer( "SiStripRegionConnectivity",
  EtaDivisions = cms.untracked.uint32( 20 ),
  PhiDivisions = cms.untracked.uint32( 20 ),
  EtaMax = cms.untracked.double( 2.5 )
)
process.SimpleSecondaryVertex3TrkComputer = cms.ESProducer( "SimpleSecondaryVertexESProducer",
  minTracks = cms.uint32( 3 ),
  minVertices = cms.uint32( 2 ),
  use3d = cms.bool( True ),
  unBoost = cms.bool( False ),
  useSignificance = cms.bool( True )
)
process.StableParameters = cms.ESProducer( "StableParametersTrivialProducer",
  NumberL1JetCounts = cms.uint32( 12 ),
  NumberL1NoIsoEG = cms.uint32( 4 ),
  NumberL1CenJet = cms.uint32( 4 ),
  NumberL1Tau = cms.uint32( 8 ),
  NumberConditionChips = cms.uint32( 1 ),
  NumberL1EGamma = cms.uint32( 12 ),
  TotalBxInEvent = cms.int32( 5 ),
  NumberL1Mu = cms.uint32( 4 ),
  PinsOnConditionChip = cms.uint32( 512 ),
  WordLength = cms.int32( 64 ),
  PinsOnChip = cms.uint32( 512 ),
  OrderOfChip = cms.vint32( 1 ),
  IfMuEtaNumberBits = cms.uint32( 6 ),
  OrderConditionChip = cms.vint32( 1 ),
  appendToDataLabel = cms.string( "" ),
  NumberL1TauJet = cms.uint32( 4 ),
  NumberL1Jet = cms.uint32( 12 ),
  NumberPhysTriggers = cms.uint32( 512 ),
  NumberL1Muon = cms.uint32( 12 ),
  UnitLength = cms.int32( 8 ),
  NumberL1IsoEG = cms.uint32( 4 ),
  NumberTechnicalTriggers = cms.uint32( 64 ),
  NumberL1ForJet = cms.uint32( 4 ),
  IfCaloEtaNumberBits = cms.uint32( 4 ),
  NumberPsbBoards = cms.int32( 7 ),
  NumberChips = cms.uint32( 5 ),
  NumberPhysTriggersExtended = cms.uint32( 64 )
)
process.SteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "anyDirection" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "SteppingHelixPropagatorAny" )
)
process.TrackerDigiGeometryESModule = cms.ESProducer( "TrackerDigiGeometryESModule",
  appendToDataLabel = cms.string( "" ),
  fromDDD = cms.bool( False ),
  applyAlignment = cms.bool( True ),
  alignmentsLabel = cms.string( "" )
)
process.TrackerGeometricDetESModule = cms.ESProducer( "TrackerGeometricDetESModule",
  appendToDataLabel = cms.string( "" ),
  fromDDD = cms.bool( False )
)
process.TransientTrackBuilderESProducer = cms.ESProducer( "TransientTrackBuilderESProducer",
  ComponentName = cms.string( "TransientTrackBuilder" )
)
process.VolumeBasedMagneticFieldESProducer = cms.ESProducer( "VolumeBasedMagneticFieldESProducerFromDB",
  debugBuilder = cms.untracked.bool( False ),
  valueOverride = cms.int32( -1 ),
  label = cms.untracked.string( "" )
)
process.ZdcGeometryFromDBEP = cms.ESProducer( "ZdcGeometryFromDBEP",
  applyAlignment = cms.bool( False )
)
process.caloDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "CaloDetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.cosmicsNavigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "CosmicNavigationSchool" ),
  SimpleMagneticField = cms.string( "" )
)
process.ecalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "EcalDetIdAssociator" ),
  etaBinSize = cms.double( 0.02 ),
  nEta = cms.int32( 300 ),
  nPhi = cms.int32( 360 ),
  includeBadChambers = cms.bool( False )
)
process.ecalSeverityLevel = cms.ESProducer( "EcalSeverityLevelESProducer",
  dbstatusMask = cms.PSet( 
    kGood = cms.vstring( 'kOk' ),
    kProblematic = cms.vstring( 'kDAC',
      'kNoLaser',
      'kNoisy',
      'kNNoisy',
      'kNNNoisy',
      'kNNNNoisy',
      'kNNNNNoisy',
      'kFixedG6',
      'kFixedG1',
      'kFixedG0' ),
    kRecovered = cms.vstring(  ),
    kTime = cms.vstring(  ),
    kWeird = cms.vstring(  ),
    kBad = cms.vstring( 'kNonRespondingIsolated',
      'kDeadVFE',
      'kDeadFE',
      'kNoDataNoTP' )
  ),
  timeThresh = cms.double( 2.0 ),
  flagMask = cms.PSet( 
    kGood = cms.vstring( 'kGood' ),
    kProblematic = cms.vstring( 'kPoorReco',
      'kPoorCalib',
      'kNoisy',
      'kSaturated' ),
    kRecovered = cms.vstring( 'kLeadingEdgeRecovered',
      'kTowerRecovered' ),
    kTime = cms.vstring( 'kOutOfTime' ),
    kWeird = cms.vstring( 'kWeird',
      'kDiWeird' ),
    kBad = cms.vstring( 'kFaultyHardware',
      'kDead',
      'kKilled' )
  )
)
process.hcalDDDRecConstants = cms.ESProducer( "HcalDDDRecConstantsESModule",
  appendToDataLabel = cms.string( "" )
)
process.hcalDDDSimConstants = cms.ESProducer( "HcalDDDSimConstantsESModule",
  appendToDataLabel = cms.string( "" )
)
process.hcalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HcalDetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.hcalRecAlgos = cms.ESProducer( "HcalRecAlgoESProducer",
  RecoveredRecHitBits = cms.vstring( 'TimingAddedBit',
    'TimingSubtractedBit' ),
  SeverityLevels = cms.VPSet( 
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 0 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellCaloTowerProb' ),
      Level = cms.int32( 1 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HSCP_R1R2',
  'HSCP_FracLeader',
  'HSCP_OuterEnergy',
  'HSCP_ExpFit',
  'ADCSaturationBit',
  'HBHEIsolatedNoise',
  'AddedSimHcalNoise' ),
      ChannelStatus = cms.vstring( 'HcalCellExcludeFromHBHENoiseSummary' ),
      Level = cms.int32( 5 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HBHEHpdHitMultiplicity',
  'HBHEPulseShape',
  'HOBit',
  'HFInTimeWindow',
  'ZDCBit',
  'CalibrationBit',
  'TimingErrorBit',
  'HBHETriangleNoise',
  'HBHETS4TS5Noise' ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 8 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HFLongShort',
  'HFPET',
  'HFS8S1Ratio',
  'HFDigiTime' ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 11 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HBHEFlatNoise',
  'HBHESpikeNoise' ),
      ChannelStatus = cms.vstring( 'HcalCellCaloTowerMask' ),
      Level = cms.int32( 12 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellHot' ),
      Level = cms.int32( 15 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellOff',
        'HcalCellDead' ),
      Level = cms.int32( 20 )
    )
  ),
  DropChannelStatusBits = cms.vstring( 'HcalCellMask',
    'HcalCellOff',
    'HcalCellDead' )
)
process.hcal_db_producer = cms.ESProducer( "HcalDbProducer" )
process.hltCombinedSecondaryVertex = cms.ESProducer( "CombinedSecondaryVertexESProducer",
  charmCut = cms.double( 1.5 ),
  recordLabel = cms.string( "HLT" ),
  useTrackWeights = cms.bool( True ),
  useCategories = cms.bool( True ),
  pseudoMultiplicityMin = cms.uint32( 2 ),
  categoryVariableName = cms.string( "vertexCategory" ),
  trackPseudoSelection = cms.PSet( 
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip3dSigMin = cms.double( -99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    maxDistToAxis = cms.double( 0.07 ),
    sip2dValMax = cms.double( 99999.9 ),
    maxDecayLen = cms.double( 5.0 ),
    ptMin = cms.double( 0.0 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( 2.0 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip2dValMin = cms.double( -99999.9 ),
    sip3dValMin = cms.double( -99999.9 )
  ),
  calibrationRecords = cms.vstring( 'CombinedSVRecoVertex',
    'CombinedSVPseudoVertex',
    'CombinedSVNoVertex' ),
  trackPairV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.03 ) ),
  correctVertexMass = cms.bool( True ),
  vertexFlip = cms.bool( False ),
  minimumTrackWeight = cms.double( 0.5 ),
  pseudoVertexV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
  trackMultiplicityMin = cms.uint32( 3 ),
  trackSelection = cms.PSet( 
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip3dSigMin = cms.double( -99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    maxDistToAxis = cms.double( 0.07 ),
    sip2dValMax = cms.double( 99999.9 ),
    maxDecayLen = cms.double( 5.0 ),
    ptMin = cms.double( 0.0 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( -99999.9 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip2dValMin = cms.double( -99999.9 ),
    sip3dValMin = cms.double( -99999.9 )
  ),
  trackSort = cms.string( "sip2dSig" ),
  SoftLeptonFlip = cms.bool( False ),
  trackFlip = cms.bool( False )
)
process.hltCombinedSecondaryVertexV2 = cms.ESProducer( "CombinedSecondaryVertexESProducer",
  charmCut = cms.double( 1.5 ),
  recordLabel = cms.string( "HLT" ),
  useTrackWeights = cms.bool( True ),
  useCategories = cms.bool( True ),
  pseudoMultiplicityMin = cms.uint32( 2 ),
  categoryVariableName = cms.string( "vertexCategory" ),
  trackPseudoSelection = cms.PSet( 
    b_pT = cms.double( 0.3684 ),
    max_pT = cms.double( 500.0 ),
    useVariableJTA = cms.bool( False ),
    maxDecayLen = cms.double( 5.0 ),
    sip3dValMin = cms.double( -99999.9 ),
    max_pT_dRcut = cms.double( 0.1 ),
    a_pT = cms.double( 0.005263 ),
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    a_dR = cms.double( -0.001053 ),
    maxDistToAxis = cms.double( 0.07 ),
    ptMin = cms.double( 0.0 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip2dValMax = cms.double( 99999.9 ),
    max_pT_trackPTcut = cms.double( 3.0 ),
    sip2dValMin = cms.double( -99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip3dSigMin = cms.double( -99999.9 ),
    min_pT = cms.double( 120.0 ),
    min_pT_dRcut = cms.double( 0.5 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( 2.0 ),
    b_dR = cms.double( 0.6263 )
  ),
  calibrationRecords = cms.vstring( 'CombinedSVIVFV2RecoVertex',
    'CombinedSVIVFV2PseudoVertex',
    'CombinedSVIVFV2NoVertex' ),
  trackPairV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.03 ) ),
  correctVertexMass = cms.bool( True ),
  vertexFlip = cms.bool( False ),
  minimumTrackWeight = cms.double( 0.5 ),
  pseudoVertexV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
  trackMultiplicityMin = cms.uint32( 3 ),
  trackSelection = cms.PSet( 
    b_pT = cms.double( 0.3684 ),
    max_pT = cms.double( 500.0 ),
    useVariableJTA = cms.bool( False ),
    maxDecayLen = cms.double( 5.0 ),
    sip3dValMin = cms.double( -99999.9 ),
    max_pT_dRcut = cms.double( 0.1 ),
    a_pT = cms.double( 0.005263 ),
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    a_dR = cms.double( -0.001053 ),
    maxDistToAxis = cms.double( 0.07 ),
    ptMin = cms.double( 0.0 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip2dValMax = cms.double( 99999.9 ),
    max_pT_trackPTcut = cms.double( 3.0 ),
    sip2dValMin = cms.double( -99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip3dSigMin = cms.double( -99999.9 ),
    min_pT = cms.double( 120.0 ),
    min_pT_dRcut = cms.double( 0.5 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( -99999.9 ),
    b_dR = cms.double( 0.6263 )
  ),
  trackSort = cms.string( "sip2dSig" ),
  SoftLeptonFlip = cms.bool( False ),
  trackFlip = cms.bool( False )
)
process.hltDisplacedDijethltESPPromptTrackCountingESProducer = cms.ESProducer( "PromptTrackCountingESProducer",
  maxImpactParameterSig = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  deltaRmin = cms.double( 0.0 ),
  maxImpactParameter = cms.double( 0.1 ),
  useSignedImpactParameterSig = cms.bool( True ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  nthTrack = cms.int32( -1 )
)
process.hltDisplacedDijethltESPTrackCounting2D1st = cms.ESProducer( "TrackCountingESProducer",
  b_pT = cms.double( 0.3684 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( 0.05 ),
  a_dR = cms.double( -0.001053 ),
  min_pT = cms.double( 120.0 ),
  maximumDistanceToJetAxis = cms.double( 9999999.0 ),
  max_pT = cms.double( 500.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  useVariableJTA = cms.bool( False ),
  min_pT_dRcut = cms.double( 0.5 ),
  max_pT_trackPTcut = cms.double( 3.0 ),
  max_pT_dRcut = cms.double( 0.1 ),
  b_dR = cms.double( 0.6263 ),
  a_pT = cms.double( 0.005263 ),
  maximumDecayLength = cms.double( 999999.0 ),
  nthTrack = cms.int32( 1 ),
  useSignedImpactParameterSig = cms.bool( False )
)
process.hltESPAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "hltESPAnalyticalPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" )
)
process.hltESPBwdAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "hltESPBwdAnalyticalPropagator" ),
  PropagationDirection = cms.string( "oppositeToMomentum" )
)
process.hltESPBwdElectronPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPBwdElectronPropagator" ),
  Mass = cms.double( 5.11E-4 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.hltESPChi2ChargeLooseMeasurementEstimator16 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPChi2ChargeLooseMeasurementEstimator16" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 16.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
process.hltESPChi2ChargeMeasurementEstimator16 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTiny" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 16.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
process.hltESPChi2ChargeMeasurementEstimator2000 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  MinimalTolerance = cms.double( 10.0 ),
  MaxDisplacement = cms.double( 100.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator2000" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( -1.0 ),
  MaxChi2 = cms.double( 2000.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
process.hltESPChi2ChargeMeasurementEstimator30 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  MinimalTolerance = cms.double( 10.0 ),
  MaxDisplacement = cms.double( 100.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( -1.0 ),
  MaxChi2 = cms.double( 30.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
process.hltESPChi2ChargeMeasurementEstimator9 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutTiny" ) ),
  MinimalTolerance = cms.double( 0.5 ),
  MaxDisplacement = cms.double( 0.5 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  pTChargeCutThreshold = cms.double( 15.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( 2.0 ),
  MaxChi2 = cms.double( 9.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
process.hltESPChi2ChargeMeasurementEstimator9ForHI = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutForHI" ) ),
  MinimalTolerance = cms.double( 10.0 ),
  MaxDisplacement = cms.double( 100.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator9ForHI" ),
  pTChargeCutThreshold = cms.double( 15.0 ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( -1.0 ),
  MaxChi2 = cms.double( 9.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
process.hltESPChi2MeasurementEstimator16 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  MinimalTolerance = cms.double( 10.0 ),
  MaxDisplacement = cms.double( 100.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator16" ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( -1.0 ),
  MaxChi2 = cms.double( 16.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
process.hltESPChi2MeasurementEstimator30 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  MinimalTolerance = cms.double( 10.0 ),
  MaxDisplacement = cms.double( 100.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator30" ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( -1.0 ),
  MaxChi2 = cms.double( 30.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
process.hltESPChi2MeasurementEstimator9 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  MinimalTolerance = cms.double( 10.0 ),
  MaxDisplacement = cms.double( 100.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator9" ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( -1.0 ),
  MaxChi2 = cms.double( 9.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
process.hltESPCloseComponentsMerger5D = cms.ESProducer( "CloseComponentsMergerESProducer5D",
  ComponentName = cms.string( "hltESPCloseComponentsMerger5D" ),
  MaxComponents = cms.int32( 12 ),
  DistanceMeasure = cms.string( "hltESPKullbackLeiblerDistance5D" )
)
process.hltESPDetachedStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPDetachedStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.13 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
process.hltESPDisplacedDijethltPromptTrackCountingESProducer = cms.ESProducer( "PromptTrackCountingESProducer",
  maxImpactParameterSig = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  deltaRmin = cms.double( 0.0 ),
  maxImpactParameter = cms.double( 0.1 ),
  useSignedImpactParameterSig = cms.bool( True ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  nthTrack = cms.int32( -1 )
)
process.hltESPDisplacedDijethltPromptTrackCountingESProducerLong = cms.ESProducer( "PromptTrackCountingESProducer",
  maxImpactParameterSig = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  deltaRmin = cms.double( 0.0 ),
  maxImpactParameter = cms.double( 0.2 ),
  useSignedImpactParameterSig = cms.bool( True ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  nthTrack = cms.int32( -1 )
)
process.hltESPDisplacedDijethltTrackCounting2D1st = cms.ESProducer( "TrackCountingESProducer",
  b_pT = cms.double( 0.3684 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( 0.05 ),
  a_dR = cms.double( -0.001053 ),
  min_pT = cms.double( 120.0 ),
  maximumDistanceToJetAxis = cms.double( 9999999.0 ),
  max_pT = cms.double( 500.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  useVariableJTA = cms.bool( False ),
  min_pT_dRcut = cms.double( 0.5 ),
  max_pT_trackPTcut = cms.double( 3.0 ),
  max_pT_dRcut = cms.double( 0.1 ),
  b_dR = cms.double( 0.6263 ),
  a_pT = cms.double( 0.005263 ),
  maximumDecayLength = cms.double( 999999.0 ),
  nthTrack = cms.int32( 1 ),
  useSignedImpactParameterSig = cms.bool( False )
)
process.hltESPDisplacedDijethltTrackCounting2D2ndLong = cms.ESProducer( "TrackCountingESProducer",
  b_pT = cms.double( 0.3684 ),
  deltaR = cms.double( -1.0 ),
  minimumImpactParameter = cms.double( 0.2 ),
  a_dR = cms.double( -0.001053 ),
  min_pT = cms.double( 120.0 ),
  maximumDistanceToJetAxis = cms.double( 9999999.0 ),
  max_pT = cms.double( 500.0 ),
  impactParameterType = cms.int32( 1 ),
  trackQualityClass = cms.string( "any" ),
  useVariableJTA = cms.bool( False ),
  min_pT_dRcut = cms.double( 0.5 ),
  max_pT_trackPTcut = cms.double( 3.0 ),
  max_pT_dRcut = cms.double( 0.1 ),
  b_dR = cms.double( 0.6263 ),
  a_pT = cms.double( 0.005263 ),
  maximumDecayLength = cms.double( 999999.0 ),
  nthTrack = cms.int32( 2 ),
  useSignedImpactParameterSig = cms.bool( True )
)
process.hltESPDummyDetLayerGeometry = cms.ESProducer( "DetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPEcalTrigTowerConstituentsMapBuilder = cms.ESProducer( "EcalTrigTowerConstituentsMapBuilder",
  MapFile = cms.untracked.string( "Geometry/EcalMapping/data/EndCap_TTMap.txt" )
)
process.hltESPElectronMaterialEffects = cms.ESProducer( "GsfMaterialEffectsESProducer",
  BetheHeitlerParametrization = cms.string( "BetheHeitler_cdfmom_nC6_O5.par" ),
  EnergyLossUpdator = cms.string( "GsfBetheHeitlerUpdator" ),
  ComponentName = cms.string( "hltESPElectronMaterialEffects" ),
  MultipleScatteringUpdator = cms.string( "MultipleScatteringUpdator" ),
  Mass = cms.double( 5.11E-4 ),
  BetheHeitlerCorrection = cms.int32( 2 )
)
process.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "anyDirection" ),
  useTuningForL2Speed = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorAny" )
)
process.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useTuningForL2Speed = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" )
)
process.hltESPFittingSmootherIT = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  ComponentName = cms.string( "hltESPFittingSmootherIT" ),
  RejectTracks = cms.bool( True )
)
process.hltESPFittingSmootherRK = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  ComponentName = cms.string( "hltESPFittingSmootherRK" ),
  RejectTracks = cms.bool( True )
)
process.hltESPFlexibleKFFittingSmoother = cms.ESProducer( "FlexibleKFFittingSmootherESProducer",
  ComponentName = cms.string( "hltESPFlexibleKFFittingSmoother" ),
  appendToDataLabel = cms.string( "" ),
  standardFitter = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
  looperFitter = cms.string( "hltESPKFFittingSmootherForLoopers" )
)
process.hltESPFwdElectronPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPFwdElectronPropagator" ),
  Mass = cms.double( 5.11E-4 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.hltESPGlobalDetLayerGeometry = cms.ESProducer( "GlobalDetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPGlobalTrackingGeometryESProducer = cms.ESProducer( "GlobalTrackingGeometryESProducer" )
process.hltESPGsfElectronFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPGsfTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPGsfTrajectorySmoother" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  ComponentName = cms.string( "hltESPGsfElectronFittingSmoother" ),
  RejectTracks = cms.bool( True )
)
process.hltESPGsfTrajectoryFitter = cms.ESProducer( "GsfTrajectoryFitterESProducer",
  Merger = cms.string( "hltESPCloseComponentsMerger5D" ),
  ComponentName = cms.string( "hltESPGsfTrajectoryFitter" ),
  MaterialEffectsUpdator = cms.string( "hltESPElectronMaterialEffects" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" ),
  GeometricalPropagator = cms.string( "hltESPAnalyticalPropagator" )
)
process.hltESPGsfTrajectorySmoother = cms.ESProducer( "GsfTrajectorySmootherESProducer",
  ErrorRescaling = cms.double( 100.0 ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" ),
  Merger = cms.string( "hltESPCloseComponentsMerger5D" ),
  ComponentName = cms.string( "hltESPGsfTrajectorySmoother" ),
  GeometricalPropagator = cms.string( "hltESPBwdAnalyticalPropagator" ),
  MaterialEffectsUpdator = cms.string( "hltESPElectronMaterialEffects" )
)
process.hltESPInitialStepChi2MeasurementEstimator36 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  MinimalTolerance = cms.double( 10.0 ),
  MaxDisplacement = cms.double( 100.0 ),
  ComponentName = cms.string( "hltESPInitialStepChi2MeasurementEstimator36" ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( -1.0 ),
  MaxChi2 = cms.double( 36.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
process.hltESPKFFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPKFTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPKFTrajectorySmoother" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  ComponentName = cms.string( "hltESPKFFittingSmoother" ),
  RejectTracks = cms.bool( True )
)
process.hltESPKFFittingSmootherForL2Muon = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  ComponentName = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
  RejectTracks = cms.bool( True )
)
process.hltESPKFFittingSmootherForLoopers = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 20.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -14.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPKFTrajectoryFitterForLoopers" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPKFTrajectorySmootherForLoopers" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  ComponentName = cms.string( "hltESPKFFittingSmootherForLoopers" ),
  RejectTracks = cms.bool( True )
)
process.hltESPKFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 20.0 ),
  appendToDataLabel = cms.string( "" ),
  LogPixelProbabilityCut = cms.double( -14.0 ),
  MinDof = cms.int32( 2 ),
  NoOutliersBeginEnd = cms.bool( False ),
  Fitter = cms.string( "hltESPRKTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPRKTrajectorySmoother" ),
  MaxNumberOfOutliers = cms.int32( 3 ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  MaxFractionOutliers = cms.double( 0.3 ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  ComponentName = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
  RejectTracks = cms.bool( True )
)
process.hltESPKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFTrajectoryFitterForLoopers = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitterForLoopers" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialForLoopers" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPKFTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmoother" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFTrajectorySmootherForLoopers = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForLoopers" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialForLoopers" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFUpdator = cms.ESProducer( "KFUpdatorESProducer",
  ComponentName = cms.string( "hltESPKFUpdator" )
)
process.hltESPKullbackLeiblerDistance5D = cms.ESProducer( "DistanceBetweenComponentsESProducer5D",
  ComponentName = cms.string( "hltESPKullbackLeiblerDistance5D" ),
  DistanceMeasure = cms.string( "KullbackLeibler" )
)
process.hltESPL3MuKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPSmartPropagatorAny" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  UseStripStripQualityDB = cms.bool( True ),
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    ),
    TID = cms.PSet( 
      maxBad = cms.uint32( 4 ),
      maxConsecutiveBad = cms.uint32( 2 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 2 ),
      maxBad = cms.uint32( 4 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  UsePixelModuleQualityDB = cms.bool( True ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  SiStripQualityLabel = cms.string( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  MaskBadAPVFibers = cms.bool( True )
)
process.hltESPMixedStepTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPMixedStepTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.11 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
process.hltESPMuonDetLayerGeometryESProducer = cms.ESProducer( "MuonDetLayerGeometryESProducer" )
process.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer( "MuonTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
)
process.hltESPPixelCPEGeneric = cms.ESProducer( "PixelCPEGenericESProducer",
  useLAAlignmentOffsets = cms.bool( False ),
  DoCosmics = cms.bool( False ),
  eff_charge_cut_highX = cms.double( 1.0 ),
  eff_charge_cut_highY = cms.double( 1.0 ),
  inflate_all_errors_no_trk_angle = cms.bool( False ),
  eff_charge_cut_lowY = cms.double( 0.0 ),
  eff_charge_cut_lowX = cms.double( 0.0 ),
  UseErrorsFromTemplates = cms.bool( True ),
  TruncatePixelCharge = cms.bool( True ),
  size_cutY = cms.double( 3.0 ),
  size_cutX = cms.double( 3.0 ),
  useLAWidthFromDB = cms.bool( False ),
  inflate_errors = cms.bool( False ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  PixelErrorParametrization = cms.string( "NOTcmsim" ),
  EdgeClusterErrorX = cms.double( 50.0 ),
  EdgeClusterErrorY = cms.double( 85.0 ),
  LoadTemplatesFromDB = cms.bool( True ),
  ComponentName = cms.string( "hltESPPixelCPEGeneric" ),
  MagneticFieldRecord = cms.ESInputTag( "" ),
  IrradiationBiasCorrection = cms.bool( False )
)
process.hltESPPixelCPETemplateReco = cms.ESProducer( "PixelCPETemplateRecoESProducer",
  DoLorentz = cms.bool( True ),
  DoCosmics = cms.bool( False ),
  LoadTemplatesFromDB = cms.bool( True ),
  ComponentName = cms.string( "hltESPPixelCPETemplateReco" ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  speed = cms.int32( -2 ),
  UseClusterSplitter = cms.bool( False )
)
process.hltESPPixelPairStepChi2MeasurementEstimator25 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  appendToDataLabel = cms.string( "" ),
  MinimalTolerance = cms.double( 10.0 ),
  MaxDisplacement = cms.double( 100.0 ),
  ComponentName = cms.string( "hltESPPixelPairStepChi2MeasurementEstimator25" ),
  nSigma = cms.double( 3.0 ),
  MaxSagitta = cms.double( -1.0 ),
  MaxChi2 = cms.double( 25.0 ),
  MinPtForHitRecoveryInGluedDet = cms.double( 1000000.0 )
)
process.hltESPPixelPairTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPPixelPairTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.19 ),
  ValidHitBonus = cms.double( 5.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 20.0 ),
  allowSharedFirstHit = cms.bool( True )
)
process.hltESPRKTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPRKTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPRKTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPRKTrajectorySmoother" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPRungeKuttaTrackerPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( True )
)
process.hltESPSmartPropagator = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagator" )
)
process.hltESPSmartPropagatorAny = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorAny" )
)
process.hltESPSmartPropagatorAnyOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorAnyOpposite" )
)
process.hltESPSoftLeptonByDistance = cms.ESProducer( "LeptonTaggerByDistanceESProducer",
  distance = cms.double( 0.5 )
)
process.hltESPSteppingHelixPropagatorAlong = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "alongMomentum" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorAlong" )
)
process.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
)
process.hltESPStripCPEfromTrackAngle = cms.ESProducer( "StripCPEESProducer",
  ComponentType = cms.string( "StripCPEfromTrackAngle" ),
  ComponentName = cms.string( "hltESPStripCPEfromTrackAngle" ),
  parameters = cms.PSet( 
    mLC_P2 = cms.double( 0.3 ),
    mLC_P1 = cms.double( 0.618 ),
    mLC_P0 = cms.double( -0.326 ),
    useLegacyError = cms.bool( False ),
    mTEC_P1 = cms.double( 0.471 ),
    mTEC_P0 = cms.double( -1.885 ),
    mTOB_P0 = cms.double( -1.026 ),
    mTOB_P1 = cms.double( 0.253 ),
    mTIB_P0 = cms.double( -0.742 ),
    mTIB_P1 = cms.double( 0.202 ),
    mTID_P0 = cms.double( -1.427 ),
    mTID_P1 = cms.double( 0.433 ),
    maxChgOneMIP = cms.double( 6000.0 )
  )
)
process.hltESPTTRHBWithTrackAngle = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPETemplateReco" ),
  ComponentName = cms.string( "hltESPTTRHBuilderAngleAndTemplate" )
)
process.hltESPTTRHBuilderPixelOnly = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBuilderPixelOnly" )
)
process.hltESPTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
)
process.hltESPTrackerRecoGeometryESProducer = cms.ESProducer( "TrackerRecoGeometryESProducer",
  appendToDataLabel = cms.string( "" ),
  trackerGeometryLabel = cms.untracked.string( "" )
)
process.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.5 ),
  ValidHitBonus = cms.double( 100.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 0.0 ),
  allowSharedFirstHit = cms.bool( False )
)
process.hltESPTrajectoryCleanerBySharedSeeds = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedSeeds" ),
  fractionShared = cms.double( 0.5 ),
  ValidHitBonus = cms.double( 100.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedSeeds" ),
  MissingHitPenalty = cms.double( 0.0 ),
  allowSharedFirstHit = cms.bool( True )
)
process.hltESPTrajectoryFitterRK = cms.ESProducer( "KFTrajectoryFitterESProducer",
  appendToDataLabel = cms.string( "" ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPTrajectoryFitterRK" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPTrajectorySmootherRK = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPTrajectorySmootherRK" ),
  appendToDataLabel = cms.string( "" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hoDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HODetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 30 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.muonDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "MuonDetIdAssociator" ),
  etaBinSize = cms.double( 0.125 ),
  nEta = cms.int32( 48 ),
  nPhi = cms.int32( 48 ),
  includeBadChambers = cms.bool( False )
)
process.navigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "SimpleNavigationSchool" ),
  SimpleMagneticField = cms.string( "ParabolicMf" )
)
process.preshowerDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "PreshowerDetIdAssociator" ),
  etaBinSize = cms.double( 0.1 ),
  nEta = cms.int32( 60 ),
  nPhi = cms.int32( 30 ),
  includeBadChambers = cms.bool( False )
)
process.siPixelQualityESProducer = cms.ESProducer( "SiPixelQualityESProducer",
  ListOfRecordToMerge = cms.VPSet( 
    cms.PSet(  record = cms.string( "SiPixelQualityFromDbRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiPixelDetVOffRcd" ),
      tag = cms.string( "" )
    )
  )
)
process.siPixelTemplateDBObjectESProducer = cms.ESProducer( "SiPixelTemplateDBObjectESProducer" )
process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer( "SiStripBackPlaneCorrectionDepESProducer",
  LatencyRecord = cms.PSet( 
    record = cms.string( "SiStripLatencyRcd" ),
    label = cms.untracked.string( "" )
  ),
  BackPlaneCorrectionDeconvMode = cms.PSet( 
    record = cms.string( "SiStripBackPlaneCorrectionRcd" ),
    label = cms.untracked.string( "deconvolution" )
  ),
  BackPlaneCorrectionPeakMode = cms.PSet( 
    record = cms.string( "SiStripBackPlaneCorrectionRcd" ),
    label = cms.untracked.string( "peak" )
  )
)
process.siStripLorentzAngleDepESProducer = cms.ESProducer( "SiStripLorentzAngleDepESProducer",
  LatencyRecord = cms.PSet( 
    record = cms.string( "SiStripLatencyRcd" ),
    label = cms.untracked.string( "" )
  ),
  LorentzAngleDeconvMode = cms.PSet( 
    record = cms.string( "SiStripLorentzAngleRcd" ),
    label = cms.untracked.string( "deconvolution" )
  ),
  LorentzAnglePeakMode = cms.PSet( 
    record = cms.string( "SiStripLorentzAngleRcd" ),
    label = cms.untracked.string( "peak" )
  )
)
process.sistripconn = cms.ESProducer( "SiStripConnectivity" )
process.trackerTopology = cms.ESProducer( "TrackerTopologyEP",
  appendToDataLabel = cms.string( "" )
)

process.DQMStore = cms.Service( "DQMStore",
    referenceFileName = cms.untracked.string( "" ),
    verbose = cms.untracked.int32( 0 ),
    collateHistograms = cms.untracked.bool( False ),
    enableMultiThread = cms.untracked.bool( True ),
    forceResetOnBeginLumi = cms.untracked.bool( False ),
    LSbasedMode = cms.untracked.bool( True ),
    verboseQT = cms.untracked.int32( 0 )
)
process.EvFDaqDirector = cms.Service( "EvFDaqDirector",
    buBaseDir = cms.untracked.string( "." ),
    baseDir = cms.untracked.string( "." ),
    fuLockPollInterval = cms.untracked.uint32( 2000 ),
    runNumber = cms.untracked.uint32( 0 ),
    microMergeDisabled = cms.untracked.bool( False ),
    outputAdler32Recheck = cms.untracked.bool( False ),
    selectedTransferMode = cms.untracked.string( "" ),
    requireTransfersPSet = cms.untracked.bool( False ),
    emptyLumisectionMode = cms.untracked.bool( False )
)
process.FastMonitoringService = cms.Service( "FastMonitoringService",
    filePerFwkStream = cms.untracked.bool( False ),
    fastMonIntervals = cms.untracked.uint32( 2 ),
    sleepTime = cms.untracked.int32( 1 )
)
process.FastTimerService = cms.Service( "FastTimerService",
    dqmPath = cms.untracked.string( "HLT/TimerService" ),
    dqmModuleTimeRange = cms.untracked.double( 40.0 ),
    useRealTimeClock = cms.untracked.bool( True ),
    enableTimingModules = cms.untracked.bool( True ),
    enableDQM = cms.untracked.bool( True ),
    enableDQMbyModule = cms.untracked.bool( False ),
    enableTimingExclusive = cms.untracked.bool( True ),
    skipFirstPath = cms.untracked.bool( False ),
    enableDQMbyLumiSection = cms.untracked.bool( True ),
    dqmPathTimeResolution = cms.untracked.double( 0.5 ),
    dqmPathTimeRange = cms.untracked.double( 100.0 ),
    dqmTimeRange = cms.untracked.double( 1000.0 ),
    dqmLumiSectionsRange = cms.untracked.uint32( 2500 ),
    enableDQMbyProcesses = cms.untracked.bool( True ),
    enableDQMSummary = cms.untracked.bool( True ),
    enableTimingSummary = cms.untracked.bool( True ),
    enableDQMbyPathTotal = cms.untracked.bool( True ),
    enableTimingPaths = cms.untracked.bool( True ),
    enableDQMbyPathExclusive = cms.untracked.bool( False ),
    dqmTimeResolution = cms.untracked.double( 5.0 ),
    dqmModuleTimeResolution = cms.untracked.double( 0.2 ),
    enableDQMbyPathActive = cms.untracked.bool( False ),
    enableDQMbyPathDetails = cms.untracked.bool( False ),
    enableDQMbyPathOverhead = cms.untracked.bool( False ),
    enableDQMbyPathCounters = cms.untracked.bool( True ),
    enableDQMbyModuleType = cms.untracked.bool( False )
)
process.MessageLogger = cms.Service( "MessageLogger",
    suppressInfo = cms.untracked.vstring(  ),
    debugs = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    suppressDebug = cms.untracked.vstring(  ),
    cout = cms.untracked.PSet(  placeholder = cms.untracked.bool( True ) ),
    cerr_stats = cms.untracked.PSet( 
      threshold = cms.untracked.string( "WARNING" ),
      output = cms.untracked.string( "cerr" ),
      optionalPSet = cms.untracked.bool( True )
    ),
    warnings = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    statistics = cms.untracked.vstring( 'cerr' ),
    cerr = cms.untracked.PSet( 
      INFO = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      noTimeStamps = cms.untracked.bool( False ),
      FwkReport = cms.untracked.PSet( 
        reportEvery = cms.untracked.int32( 1 ),
        limit = cms.untracked.int32( 0 )
      ),
      default = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) ),
      Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkSummary = cms.untracked.PSet( 
        reportEvery = cms.untracked.int32( 1 ),
        limit = cms.untracked.int32( 10000000 )
      ),
      threshold = cms.untracked.string( "INFO" ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    FrameworkJobReport = cms.untracked.PSet( 
      default = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) )
    ),
    suppressWarning = cms.untracked.vstring( 'hltOnlineBeamSpot',
      'hltCtf3HitL1SeededWithMaterialTracks',
      'hltL3MuonsOIState',
      'hltPixelTracksForHighMult',
      'hltHITPixelTracksHE',
      'hltHITPixelTracksHB',
      'hltCtfL1SeededWithMaterialTracks',
      'hltRegionalTracksForL3MuonIsolation',
      'hltSiPixelClusters',
      'hltActivityStartUpElectronPixelSeeds',
      'hltLightPFTracks',
      'hltPixelVertices3DbbPhi',
      'hltL3MuonsIOHit',
      'hltPixelTracks',
      'hltSiPixelDigis',
      'hltL3MuonsOIHit',
      'hltL1SeededElectronGsfTracks',
      'hltL1SeededStartUpElectronPixelSeeds',
      'hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV',
      'hltCtfActivityWithMaterialTracks' ),
    errors = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    fwkJobReports = cms.untracked.vstring( 'FrameworkJobReport' ),
    debugModules = cms.untracked.vstring(  ),
    infos = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    categories = cms.untracked.vstring( 'FwkJob',
      'FwkReport',
      'FwkSummary',
      'Root_NoDictionary' ),
    destinations = cms.untracked.vstring( 'warnings',
      'errors',
      'infos',
      'debugs',
      'cout',
      'cerr' ),
    threshold = cms.untracked.string( "INFO" ),
    suppressError = cms.untracked.vstring( 'hltOnlineBeamSpot',
      'hltL3MuonCandidates',
      'hltL3TkTracksFromL2OIState',
      'hltPFJetCtfWithMaterialTracks',
      'hltL3TkTracksFromL2IOHit',
      'hltL3TkTracksFromL2OIHit' )
)
process.PrescaleService = cms.Service( "PrescaleService",
    forceDefault = cms.bool( False ),
    prescaleTable = cms.VPSet( 
      cms.PSet(  pathName = cms.string( "HLT_Physics_v2" ),
        prescales = cms.vuint32( 80, 80, 800, 800, 800, 800 )
      ),
      cms.PSet(  pathName = cms.string( "DST_Physics_v1" ),
        prescales = cms.vuint32( 10, 10, 10, 10, 10, 10 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_Random_v1" ),
        prescales = cms.vuint32( 60, 10000, 60, 60, 60, 60 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_ZeroBias_v2" ),
        prescales = cms.vuint32( 100, 100, 100, 100, 10000, 10000 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_L1SingleEG5_v1" ),
        prescales = cms.vuint32( 3, 3, 100, 3, 3, 1 )
      ),
      cms.PSet(  pathName = cms.string( "AlCa_LumiPixels_Random_v1" ),
        prescales = cms.vuint32( 10, 1500, 10, 10, 10, 10 )
      ),
      cms.PSet(  pathName = cms.string( "AlCa_LumiPixels_ZeroBias_v2" ),
        prescales = cms.vuint32( 1, 1, 1, 1, 1000, 1000 )
      ),
      cms.PSet(  pathName = cms.string( "PhysicsEGammaCommissioningOutput" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "DQMOutput" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "DQMCalibrationOutput" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "DQMEventDisplayOutput" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "RPCMONOutput" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "CalibrationOutput" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "EcalCalibrationOutput" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "ALCAPHISYMOutput" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "ALCALUMIPIXELSOutput" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "ExpressOutput" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "NanoDSTOutput" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 0 )
      )
    ),
    lvl1DefaultLabel = cms.string( "Cosmics" ),
    lvl1Labels = cms.vstring( 'Cosmics',
      'Cosmics+HighRandom',
      'HighEG',
      'HighJet',
      'HighBPTX',
      'Dummy' )
)

process.hltGetConditions = cms.EDAnalyzer( "EventSetupRecordDataGetter",
    toGet = cms.VPSet( 
    ),
    verbose = cms.untracked.bool( False )
)
process.hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
process.hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
process.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
process.hltGtStage2Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage2::GTSetup" ),
    MinFeds = cms.uint32( 0 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    MTF7 = cms.untracked.bool( False ),
    FWId = cms.uint32( 0 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1404 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    FWOverride = cms.bool( False )
)
process.hltCaloStage2Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage2::CaloSetup" ),
    MinFeds = cms.uint32( 0 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    MTF7 = cms.untracked.bool( False ),
    FWId = cms.uint32( 0 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1360 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    FWOverride = cms.bool( False )
)
process.hltGmtStage2Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage2::GMTSetup" ),
    MinFeds = cms.uint32( 0 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    MTF7 = cms.untracked.bool( False ),
    FWId = cms.uint32( 0 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1402 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    FWOverride = cms.bool( False )
)
process.hltGtStage2ObjectMap = cms.EDProducer( "L1TGlobalProducer",
    L1DataBxInEvent = cms.int32( 5 ),
    JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    AlgorithmTriggersUnmasked = cms.bool( True ),
    EmulateBxInEvent = cms.int32( 1 ),
    ExtInputTag = cms.InputTag( "hltGtStage2Digis" ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    Verbosity = cms.untracked.int32( 0 ),
    EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    ProduceL1GtDaqRecord = cms.bool( True ),
    PrescaleSet = cms.uint32( 1 ),
    EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    TriggerMenuLuminosity = cms.string( "startup" ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    PrescaleCSVFile = cms.string( "prescale_L1TGlobal.csv" ),
    TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    BstLengthBytes = cms.int32( -1 ),
    MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' )
)
process.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    maxZ = cms.double( 40.0 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    changeToCMSCoordinates = cms.bool( False ),
    setSigmaZ = cms.double( 0.0 ),
    maxRadius = cms.double( 2.0 )
)
process.hltL1sSingleMu3 = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu3" ),
    L1EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreL1SingleMu3 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1fL1sMu3L1Filtered0 = cms.EDFilter( "HLTMuonL1TFilter",
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL1sSingleMu3" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    CentralBxOnly = cms.bool( True ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( 'hltGmtStage2Digis','Muon' )
)
process.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltL1sSingleMu5 = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu5" ),
    L1EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreL1SingleMu5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1fL1sMu5L1Filtered0 = cms.EDFilter( "HLTMuonL1TFilter",
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL1sSingleMu5" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    CentralBxOnly = cms.bool( True ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( 'hltGmtStage2Digis','Muon' )
)
process.hltL1sSingleMu7 = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu7" ),
    L1EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreL1SingleMu7 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1fL1sMu7L1Filtered0 = cms.EDFilter( "HLTMuonL1TFilter",
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL1sSingleMu7" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    CentralBxOnly = cms.bool( True ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( 'hltGmtStage2Digis','Muon' )
)
process.hltL1sSingleMuOpen = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleMuOpen" ),
    L1EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreL1SingleMuOpen = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1MuOpenL1Filtered0 = cms.EDFilter( "HLTMuonL1TFilter",
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL1sSingleMuOpen" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    CentralBxOnly = cms.bool( True ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( 'hltGmtStage2Digis','Muon' )
)
process.hltPreL1SingleMuOpenDT = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1MuOpenL1FilteredDT = cms.EDFilter( "HLTMuonL1TFilter",
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL1sSingleMuOpen" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.25 ),
    CentralBxOnly = cms.bool( True ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( 'hltGmtStage2Digis','Muon' )
)
process.hltL1EventNumberL1Fat = cms.EDFilter( "HLTL1NumberFilter",
    invert = cms.bool( False ),
    period = cms.uint32( 107 ),
    rawInput = cms.InputTag( "rawDataCollector" ),
    fedId = cms.int32( 1024 )
)
process.hltPreL1FatEvents = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPrePhysics = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreDSTPhysics = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltRandomEventsFilter = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 3 )
)
process.hltPreRandom = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sL1ZeroBias = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_ZeroBias" ),
    L1EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreZeroBias = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sDoubleMu0 = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_DoubleMu0" ),
    L1EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreL1DoubleMu0 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltDoubleMu0L1Filtered = cms.EDFilter( "HLTMuonL1TFilter",
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL1sDoubleMu0" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 2 ),
    MaxEta = cms.double( 2.5 ),
    CentralBxOnly = cms.bool( True ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( 'hltGmtStage2Digis','Muon' )
)
process.hltL1sSingleEG5 = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG5" ),
    L1EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreL1SingleEG5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltCalibrationEventsFilter = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 2 )
)
process.hltPreEcalCalibration = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEcalCalibrationRaw = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 1024 )
)
process.hltPreHcalCalibration = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltHcalCalibTypeFilter = cms.EDFilter( "HLTHcalCalibTypeFilter",
    InputTag = cms.InputTag( "rawDataCollector" ),
    CalibTypes = cms.vint32( 1, 2, 3, 4, 5, 6 ),
    FilterSummary = cms.untracked.bool( False )
)
process.hltHcalCalibrationRaw = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 1024, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199 )
)
process.hltL1sL1ZeroBiasORAlwaysTrue = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_ZeroBias OR L1_AlwaysTrue" ),
    L1EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreAlCaEcalPhiSym = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltEcalDigis = cms.EDProducer( "EcalRawToDigi",
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    FedLabel = cms.InputTag( "listfeds" ),
    eventPut = cms.bool( True ),
    srpUnpacking = cms.bool( True ),
    syncCheck = cms.bool( True ),
    headerUnpacking = cms.bool( True ),
    feUnpacking = cms.bool( True ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    tccUnpacking = cms.bool( True ),
    numbTriggerTSamples = cms.int32( 1 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    numbXtalTSamples = cms.int32( 10 ),
    feIdCheck = cms.bool( True ),
    FEDs = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    silentMode = cms.untracked.bool( True ),
    DoRegional = cms.bool( False ),
    forceToKeepFRData = cms.bool( False ),
    memUnpacking = cms.bool( True )
)
process.hltEcalPreshowerDigis = cms.EDProducer( "ESRawToDigi",
    sourceTag = cms.InputTag( "rawDataCollector" ),
    debugMode = cms.untracked.bool( False ),
    InstanceES = cms.string( "" ),
    ESdigiCollection = cms.string( "" ),
    LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" )
)
process.hltEcalUncalibRecHit = cms.EDProducer( "EcalUncalibRecHitProducer",
    EEdigiCollection = cms.InputTag( 'hltEcalDigis','eeDigis' ),
    EBdigiCollection = cms.InputTag( 'hltEcalDigis','ebDigis' ),
    EEhitCollection = cms.string( "EcalUncalibRecHitsEE" ),
    EBhitCollection = cms.string( "EcalUncalibRecHitsEB" ),
    algo = cms.string( "EcalUncalibRecHitWorkerMultiFit" ),
    algoPSet = cms.PSet( 
      outOfTimeThresholdGain61pEB = cms.double( 5.0 ),
      EBtimeFitParameters = cms.vdouble( -2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 91.01147, -50.35761, 11.05621 ),
      activeBXs = cms.vint32( -5, -4, -3, -2, -1, 0, 1, 2 ),
      amplitudeThresholdEE = cms.double( 10.0 ),
      EBtimeConstantTerm = cms.double( 0.6 ),
      EEtimeFitLimits_Lower = cms.double( 0.2 ),
      outOfTimeThresholdGain61pEE = cms.double( 1000.0 ),
      ebSpikeThreshold = cms.double( 1.042 ),
      EBtimeNconst = cms.double( 28.5 ),
      ampErrorCalculation = cms.bool( False ),
      kPoorRecoFlagEB = cms.bool( True ),
      EBtimeFitLimits_Lower = cms.double( 0.2 ),
      kPoorRecoFlagEE = cms.bool( False ),
      chi2ThreshEB_ = cms.double( 65.0 ),
      EEtimeFitParameters = cms.vdouble( -2.390548, 3.553628, -17.62341, 67.67538, -133.213, 140.7432, -75.41106, 16.20277 ),
      useLumiInfoRunHeader = cms.bool( False ),
      outOfTimeThresholdGain12mEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain12mEB = cms.double( 5.0 ),
      EEtimeFitLimits_Upper = cms.double( 1.4 ),
      prefitMaxChiSqEB = cms.double( 15.0 ),
      EEamplitudeFitParameters = cms.vdouble( 1.89, 1.4 ),
      prefitMaxChiSqEE = cms.double( 10.0 ),
      EBamplitudeFitParameters = cms.vdouble( 1.138, 1.652 ),
      EBtimeFitLimits_Upper = cms.double( 1.4 ),
      timealgo = cms.string( "None" ),
      amplitudeThresholdEB = cms.double( 10.0 ),
      outOfTimeThresholdGain12pEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain12pEB = cms.double( 5.0 ),
      EEtimeNconst = cms.double( 31.8 ),
      outOfTimeThresholdGain61mEB = cms.double( 5.0 ),
      outOfTimeThresholdGain61mEE = cms.double( 1000.0 ),
      EEtimeConstantTerm = cms.double( 1.0 ),
      chi2ThreshEE_ = cms.double( 50.0 ),
      doPrefitEE = cms.bool( True ),
      doPrefitEB = cms.bool( True )
    )
)
process.hltEcalDetIdToBeRecovered = cms.EDProducer( "EcalDetIdToBeRecoveredProducer",
    ebIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebDetIdToBeRecovered = cms.string( "ebDetId" ),
    integrityTTIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityTTIdErrors' ),
    eeIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    ebFEToBeRecovered = cms.string( "ebFE" ),
    ebIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    eeDetIdToBeRecovered = cms.string( "eeDetId" ),
    eeIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    eeIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    ebSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    eeSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    integrityBlockSizeErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityBlockSizeErrors' ),
    eeFEToBeRecovered = cms.string( "eeFE" )
)
process.hltEcalRecHit = cms.EDProducer( "EcalRecHitProducer",
    recoverEEVFE = cms.bool( False ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    recoverEBIsolatedChannels = cms.bool( False ),
    recoverEBVFE = cms.bool( False ),
    laserCorrection = cms.bool( True ),
    EBLaserMIN = cms.double( 0.5 ),
    killDeadChannels = cms.bool( True ),
    dbStatusToBeExcludedEB = cms.vint32( 14, 78, 142 ),
    EEuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEE' ),
    EBLaserMAX = cms.double( 3.0 ),
    EELaserMIN = cms.double( 0.5 ),
    ebFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebFE' ),
    EELaserMAX = cms.double( 8.0 ),
    recoverEEIsolatedChannels = cms.bool( False ),
    eeDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeDetId' ),
    recoverEBFE = cms.bool( True ),
    algo = cms.string( "EcalRecHitWorkerSimple" ),
    ebDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebDetId' ),
    singleChannelRecoveryThreshold = cms.double( 8.0 ),
    ChannelStatusToBeExcluded = cms.vstring(  ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    singleChannelRecoveryMethod = cms.string( "NeuralNetworks" ),
    recoverEEFE = cms.bool( True ),
    triggerPrimitiveDigiCollection = cms.InputTag( 'hltEcalDigis','EcalTriggerPrimitives' ),
    dbStatusToBeExcludedEE = cms.vint32( 14, 78, 142 ),
    flagsMapDBReco = cms.PSet( 
      kGood = cms.vstring( 'kOk',
        'kDAC',
        'kNoLaser',
        'kNoisy' ),
      kNeighboursRecovered = cms.vstring( 'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE' ),
      kDead = cms.vstring( 'kNoDataNoTP' ),
      kNoisy = cms.vstring( 'kNNoisy',
        'kFixedG6',
        'kFixedG1' ),
      kTowerRecovered = cms.vstring( 'kDeadFE' )
    ),
    EBuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEB' ),
    skipTimeCalib = cms.bool( False ),
    algoRecover = cms.string( "EcalRecHitWorkerRecover" ),
    eeFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeFE' ),
    cleaningConfig = cms.PSet( 
      e6e2thresh = cms.double( 0.04 ),
      tightenCrack_e6e2_double = cms.double( 3.0 ),
      e4e1Threshold_endcap = cms.double( 0.3 ),
      tightenCrack_e4e1_single = cms.double( 3.0 ),
      tightenCrack_e1_double = cms.double( 2.0 ),
      cThreshold_barrel = cms.double( 4.0 ),
      e4e1Threshold_barrel = cms.double( 0.08 ),
      tightenCrack_e1_single = cms.double( 2.0 ),
      e4e1_b_barrel = cms.double( -0.024 ),
      e4e1_a_barrel = cms.double( 0.04 ),
      ignoreOutOfTimeThresh = cms.double( 1.0E9 ),
      cThreshold_endcap = cms.double( 15.0 ),
      e4e1_b_endcap = cms.double( -0.0125 ),
      e4e1_a_endcap = cms.double( 0.02 ),
      cThreshold_double = cms.double( 10.0 )
    ),
    logWarningEtThreshold_EB_FE = cms.double( 50.0 ),
    logWarningEtThreshold_EE_FE = cms.double( 50.0 )
)
process.hltEcalPreshowerRecHit = cms.EDProducer( "ESRecHitProducer",
    ESRecoAlgo = cms.int32( 0 ),
    ESrechitCollection = cms.string( "EcalRecHitsES" ),
    algo = cms.string( "ESRecHitWorker" ),
    ESdigiCollection = cms.InputTag( "hltEcalPreshowerDigis" )
)
process.hltEcalPhiSymFilter = cms.EDFilter( "HLTEcalPhiSymFilter",
    ampCut_endcapM = cms.vdouble( 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0 ),
    phiSymBarrelDigiCollection = cms.string( "phiSymEcalDigisEB" ),
    phiSymEndcapDigiCollection = cms.string( "phiSymEcalDigisEE" ),
    barrelDigiCollection = cms.InputTag( 'hltEcalDigis','ebDigis' ),
    barrelUncalibHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEB' ),
    statusThreshold = cms.uint32( 3 ),
    useRecoFlag = cms.bool( False ),
    endcapUncalibHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEE' ),
    endcapHitCollection = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    ampCut_barrelM = cms.vdouble( 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0 ),
    endcapDigiCollection = cms.InputTag( 'hltEcalDigis','eeDigis' ),
    barrelHitCollection = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    ampCut_endcapP = cms.vdouble( 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0, 14.0 ),
    ampCut_barrelP = cms.vdouble( 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0, 12.0 )
)
process.hltL1EventNumberNZS = cms.EDFilter( "HLTL1NumberFilter",
    invert = cms.bool( False ),
    period = cms.uint32( 4096 ),
    rawInput = cms.InputTag( "rawDataCollector" ),
    fedId = cms.int32( 1024 )
)
process.hltL1sHcalNZS = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG5 OR L1_SingleJet24 OR L1_ZeroBias" ),
    L1EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHcalNZS = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleEG5IorSingleMuOpen = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG5 OR L1_SingleMuOpen" ),
    L1EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreHcalPhiSym = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sTowerCount40 = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_TowerCount40" ),
    L1EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreL1TowerCount40 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltL1sSingleMu5IorSingleMu7 = cms.EDFilter( "HLTL1TSeed",
    L1SeedsLogicalExpression = cms.string( "L1_SingleMu5 OR L1_SingleMu7" ),
    L1EGammaInputTag = cms.InputTag( 'hltCaloStage2Digis','EGamma' ),
    L1JetInputTag = cms.InputTag( 'hltCaloStage2Digis','Jet' ),
    saveTags = cms.bool( True ),
    L1ObjectMapInputTag = cms.InputTag( "hltGtStage2ObjectMap" ),
    L1EtSumInputTag = cms.InputTag( 'hltCaloStage2Digis','EtSum' ),
    L1TauInputTag = cms.InputTag( 'hltCaloStage2Digis','Tau' ),
    L1MuonInputTag = cms.InputTag( 'hltGmtStage2Digis','Muon' ),
    L1GlobalInputTag = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPreAlCaRPCMuonNoTriggers = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltRPCMuonNoTriggersL1Filtered0 = cms.EDFilter( "HLTMuonL1TFilter",
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL1sSingleMu5IorSingleMu7" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.6 ),
    CentralBxOnly = cms.bool( True ),
    SelectQualities = cms.vint32( 6 ),
    CandTag = cms.InputTag( 'hltGmtStage2Digis','Muon' )
)
process.hltMuonDTDigis = cms.EDProducer( "DTUnpackingModule",
    useStandardFEDid = cms.bool( True ),
    maxFEDid = cms.untracked.int32( 779 ),
    inputLabel = cms.InputTag( "rawDataCollector" ),
    minFEDid = cms.untracked.int32( 770 ),
    dataType = cms.string( "DDU" ),
    readOutParameters = cms.PSet( 
      debug = cms.untracked.bool( False ),
      rosParameters = cms.PSet( 
        writeSC = cms.untracked.bool( True ),
        readingDDU = cms.untracked.bool( True ),
        performDataIntegrityMonitor = cms.untracked.bool( False ),
        readDDUIDfromDDU = cms.untracked.bool( True ),
        debug = cms.untracked.bool( False ),
        localDAQ = cms.untracked.bool( False )
      ),
      localDAQ = cms.untracked.bool( False ),
      performDataIntegrityMonitor = cms.untracked.bool( False )
    ),
    dqmOnly = cms.bool( False )
)
process.hltDt1DRecHits = cms.EDProducer( "DTRecHitProducer",
    debug = cms.untracked.bool( False ),
    recAlgoConfig = cms.PSet( 
      tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
      minTime = cms.double( -3.0 ),
      stepTwoFromDigi = cms.bool( False ),
      doVdriftCorr = cms.bool( True ),
      debug = cms.untracked.bool( False ),
      maxTime = cms.double( 420.0 ),
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
      useUncertDB = cms.bool( True )
    ),
    dtDigiLabel = cms.InputTag( "hltMuonDTDigis" ),
    recAlgo = cms.string( "DTLinearDriftFromDBAlgo" )
)
process.hltDt4DSegments = cms.EDProducer( "DTRecSegment4DProducer",
    debug = cms.untracked.bool( False ),
    Reco4DAlgoName = cms.string( "DTCombinatorialPatternReco4D" ),
    recHits2DLabel = cms.InputTag( "dt2DSegments" ),
    recHits1DLabel = cms.InputTag( "hltDt1DRecHits" ),
    Reco4DAlgoConfig = cms.PSet( 
      segmCleanerMode = cms.int32( 2 ),
      Reco2DAlgoName = cms.string( "DTCombinatorialPatternReco" ),
      recAlgoConfig = cms.PSet( 
        tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
        minTime = cms.double( -3.0 ),
        stepTwoFromDigi = cms.bool( False ),
        doVdriftCorr = cms.bool( True ),
        debug = cms.untracked.bool( False ),
        maxTime = cms.double( 420.0 ),
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
        useUncertDB = cms.bool( True )
      ),
      nSharedHitsMax = cms.int32( 2 ),
      hit_afterT0_resolution = cms.double( 0.03 ),
      Reco2DAlgoConfig = cms.PSet( 
        segmCleanerMode = cms.int32( 2 ),
        recAlgoConfig = cms.PSet( 
          tTrigMode = cms.string( "DTTTrigSyncFromDB" ),
          minTime = cms.double( -3.0 ),
          stepTwoFromDigi = cms.bool( False ),
          doVdriftCorr = cms.bool( True ),
          debug = cms.untracked.bool( False ),
          maxTime = cms.double( 420.0 ),
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
          useUncertDB = cms.bool( True )
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
        performT0SegCorrection = cms.bool( False ),
        perform_delta_rejecting = cms.bool( False )
      ),
      performT0_vdriftSegCorrection = cms.bool( False ),
      debug = cms.untracked.bool( False ),
      recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
      nUnSharedHitsMin = cms.int32( 2 ),
      AllDTRecHits = cms.bool( True ),
      performT0SegCorrection = cms.bool( False ),
      perform_delta_rejecting = cms.bool( False )
    )
)
process.hltMuonCSCDigis = cms.EDProducer( "CSCDCCUnpacker",
    PrintEventNumber = cms.untracked.bool( False ),
    SuppressZeroLCT = cms.untracked.bool( True ),
    UseExaminer = cms.bool( True ),
    Debug = cms.untracked.bool( False ),
    ErrorMask = cms.uint32( 0x0 ),
    InputObjects = cms.InputTag( "rawDataCollector" ),
    ExaminerMask = cms.uint32( 0x1febf3f6 ),
    runDQM = cms.untracked.bool( False ),
    UnpackStatusDigis = cms.bool( False ),
    VisualFEDInspect = cms.untracked.bool( False ),
    FormatedEventDump = cms.untracked.bool( False ),
    UseFormatStatus = cms.bool( True ),
    UseSelectiveUnpacking = cms.bool( True ),
    VisualFEDShort = cms.untracked.bool( False )
)
process.hltCsc2DRecHits = cms.EDProducer( "CSCRecHitDProducer",
    XTasymmetry_ME1b = cms.double( 0.0 ),
    XTasymmetry_ME1a = cms.double( 0.0 ),
    ConstSyst_ME1a = cms.double( 0.022 ),
    ConstSyst_ME1b = cms.double( 0.007 ),
    XTasymmetry_ME41 = cms.double( 0.0 ),
    CSCStripxtalksOffset = cms.double( 0.03 ),
    CSCUseCalibrations = cms.bool( True ),
    CSCUseTimingCorrections = cms.bool( True ),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32( 2 ),
    XTasymmetry_ME22 = cms.double( 0.0 ),
    UseFivePoleFit = cms.bool( True ),
    XTasymmetry_ME21 = cms.double( 0.0 ),
    ConstSyst_ME21 = cms.double( 0.0 ),
    CSCDebug = cms.untracked.bool( False ),
    ConstSyst_ME22 = cms.double( 0.0 ),
    CSCUseGasGainCorrections = cms.bool( False ),
    XTasymmetry_ME31 = cms.double( 0.0 ),
    readBadChambers = cms.bool( True ),
    NoiseLevel_ME13 = cms.double( 8.0 ),
    NoiseLevel_ME12 = cms.double( 9.0 ),
    NoiseLevel_ME32 = cms.double( 9.0 ),
    NoiseLevel_ME31 = cms.double( 9.0 ),
    XTasymmetry_ME32 = cms.double( 0.0 ),
    ConstSyst_ME41 = cms.double( 0.0 ),
    CSCStripClusterSize = cms.untracked.int32( 3 ),
    CSCStripClusterChargeCut = cms.double( 25.0 ),
    CSCStripPeakThreshold = cms.double( 10.0 ),
    readBadChannels = cms.bool( False ),
    UseParabolaFit = cms.bool( False ),
    XTasymmetry_ME13 = cms.double( 0.0 ),
    XTasymmetry_ME12 = cms.double( 0.0 ),
    wireDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCWireDigi' ),
    ConstSyst_ME12 = cms.double( 0.0 ),
    ConstSyst_ME13 = cms.double( 0.0 ),
    ConstSyst_ME32 = cms.double( 0.0 ),
    ConstSyst_ME31 = cms.double( 0.0 ),
    UseAverageTime = cms.bool( False ),
    NoiseLevel_ME1a = cms.double( 7.0 ),
    NoiseLevel_ME1b = cms.double( 8.0 ),
    CSCWireClusterDeltaT = cms.int32( 1 ),
    CSCUseStaticPedestals = cms.bool( False ),
    stripDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCStripDigi' ),
    CSCstripWireDeltaTime = cms.int32( 8 ),
    NoiseLevel_ME21 = cms.double( 9.0 ),
    NoiseLevel_ME22 = cms.double( 9.0 ),
    NoiseLevel_ME41 = cms.double( 9.0 )
)
process.hltCscSegments = cms.EDProducer( "CSCSegmentProducer",
    inputObjects = cms.InputTag( "hltCsc2DRecHits" ),
    algo_psets = cms.VPSet( 
      cms.PSet(  chamber_types = cms.vstring( 'ME1/a',
  'ME1/b',
  'ME1/2',
  'ME1/3',
  'ME2/1',
  'ME2/2',
  'ME3/1',
  'ME3/2',
  'ME4/1',
  'ME4/2' ),
        algo_name = cms.string( "CSCSegAlgoST" ),
        parameters_per_chamber_type = cms.vint32( 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 ),
        algo_psets = cms.VPSet( 
          cms.PSet(  maxRatioResidualPrune = cms.double( 3.0 ),
            yweightPenalty = cms.double( 1.5 ),
            maxRecHitsInCluster = cms.int32( 20 ),
            dPhiFineMax = cms.double( 0.025 ),
            preClusteringUseChaining = cms.bool( True ),
            ForceCovariance = cms.bool( False ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            NormChi2Cut2D = cms.double( 20.0 ),
            BPMinImprovement = cms.double( 10000.0 ),
            Covariance = cms.double( 0.0 ),
            tanPhiMax = cms.double( 0.5 ),
            SeedBig = cms.double( 0.0015 ),
            onlyBestSegment = cms.bool( False ),
            dRPhiFineMax = cms.double( 8.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            curvePenalty = cms.double( 2.0 ),
            dXclusBoxMax = cms.double( 4.0 ),
            BrutePruning = cms.bool( True ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            CorrectTheErrors = cms.bool( True ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            useShowering = cms.bool( False ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            minHitsPerSegment = cms.int32( 3 ),
            ForceCovarianceAll = cms.bool( False ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            prePrunLimit = cms.double( 3.17 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            preClustering = cms.bool( True ),
            prePrun = cms.bool( True ),
            maxDPhi = cms.double( 999.0 ),
            maxDTheta = cms.double( 999.0 ),
            Pruning = cms.bool( True ),
            dYclusBoxMax = cms.double( 8.0 )
          ),
          cms.PSet(  maxRatioResidualPrune = cms.double( 3.0 ),
            yweightPenalty = cms.double( 1.5 ),
            maxRecHitsInCluster = cms.int32( 24 ),
            dPhiFineMax = cms.double( 0.025 ),
            preClusteringUseChaining = cms.bool( True ),
            ForceCovariance = cms.bool( False ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            NormChi2Cut2D = cms.double( 20.0 ),
            BPMinImprovement = cms.double( 10000.0 ),
            Covariance = cms.double( 0.0 ),
            tanPhiMax = cms.double( 0.5 ),
            SeedBig = cms.double( 0.0015 ),
            onlyBestSegment = cms.bool( False ),
            dRPhiFineMax = cms.double( 8.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            curvePenalty = cms.double( 2.0 ),
            dXclusBoxMax = cms.double( 4.0 ),
            BrutePruning = cms.bool( True ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            CorrectTheErrors = cms.bool( True ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            useShowering = cms.bool( False ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            minHitsPerSegment = cms.int32( 3 ),
            ForceCovarianceAll = cms.bool( False ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            prePrunLimit = cms.double( 3.17 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            preClustering = cms.bool( True ),
            prePrun = cms.bool( True ),
            maxDPhi = cms.double( 999.0 ),
            maxDTheta = cms.double( 999.0 ),
            Pruning = cms.bool( True ),
            dYclusBoxMax = cms.double( 8.0 )
          )
        )
      )
    ),
    algo_type = cms.int32( 1 )
)
process.hltMuonRPCDigis = cms.EDProducer( "RPCUnpackingModule",
    InputLabel = cms.InputTag( "rawDataCollector" ),
    doSynchro = cms.bool( False )
)
process.hltRpcRecHits = cms.EDProducer( "RPCRecHitProducer",
    recAlgoConfig = cms.PSet(  ),
    deadvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat" ),
    rpcDigiLabel = cms.InputTag( "hltMuonRPCDigis" ),
    maskvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat" ),
    recAlgo = cms.string( "RPCRecHitStandardAlgo" ),
    deadSource = cms.string( "File" ),
    maskSource = cms.string( "File" )
)
process.hltPreAlCaRPCMuonNoHits = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltRPCPointProducer = cms.EDProducer( "RPCPointProducer",
    cscSegments = cms.InputTag( "hltCscSegments" ),
    rangestripsRB4 = cms.untracked.double( 4.0 ),
    TrackTransformer = cms.PSet(  ),
    tracks = cms.InputTag( "NotUsed" ),
    rangestrips = cms.untracked.double( 4.0 ),
    incltrack = cms.untracked.bool( False ),
    MinCosAng = cms.untracked.double( 0.95 ),
    MaxDrb4 = cms.untracked.double( 150.0 ),
    inclcsc = cms.untracked.bool( True ),
    dt4DSegments = cms.InputTag( "hltDt4DSegments" ),
    ExtrapolatedRegion = cms.untracked.double( 0.5 ),
    incldt = cms.untracked.bool( True ),
    debug = cms.untracked.bool( False ),
    MaxD = cms.untracked.double( 80.0 )
)
process.hltRPCFilter = cms.EDFilter( "HLTRPCFilter",
    rangestrips = cms.untracked.double( 1.0 ),
    rpcDTPoints = cms.InputTag( 'hltRPCPointProducer','RPCDTExtrapolatedPoints' ),
    rpcRecHits = cms.InputTag( "hltRpcRecHits" ),
    rpcCSCPoints = cms.InputTag( 'hltRPCPointProducer','RPCCSCExtrapolatedPoints' )
)
process.hltPreAlCaRPCMuonNormalisation = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltRPCMuonNormaL1Filtered0 = cms.EDFilter( "HLTMuonL1TFilter",
    saveTags = cms.bool( True ),
    PreviousCandTag = cms.InputTag( "hltL1sSingleMu5IorSingleMu7" ),
    MinPt = cms.double( 0.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 1.6 ),
    CentralBxOnly = cms.bool( True ),
    SelectQualities = cms.vint32(  ),
    CandTag = cms.InputTag( 'hltGmtStage2Digis','Muon' )
)
process.hltPreAlCaLumiPixelsRandom = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltFEDSelectorLumiPixels = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39 )
)
process.hltPreAlCaLumiPixelsZeroBias = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 1023, 1024 )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    processName = cms.string( "@" )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)
process.hltPreRatesMonitoring = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltHLTriggerJSONMonitoring = cms.EDAnalyzer( "HLTriggerJSONMonitoring",
    triggerResults = cms.InputTag( 'TriggerResults','','HLT' )
)
process.hltL1TriggerJSONMonitoring = cms.EDAnalyzer( "L1TriggerJSONMonitoring",
    L1Results = cms.InputTag( "hltGtStage2Digis" )
)
process.hltPrePhysicsEGammaCommissioningOutput = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreDQMOutput = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreDQMOutputSmart = cms.EDFilter( "TriggerResultsFilter",
    hltResults = cms.InputTag( "TriggerResults" ),
    l1tResults = cms.InputTag( "" ),
    triggerConditions = cms.vstring( '( FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR HLT_L1SingleMu3_v1 OR HLT_L1SingleMuOpen_v2 OR HLT_L1SingleMuOpen_DT_v2 OR FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR FALSE OR HLT_Random_v1 OR HLT_L1SingleEG5_v1 OR FALSE OR HLT_HcalNZS_v2 OR HLT_HcalPhiSym_v2 ) / 2',
      'HLT_L1FatEvents_v1',
      'HLT_Physics_v2 / 10',
      'HLT_ZeroBias_v2 / 30',
      'HLT_L1DoubleMu0_v1 / 30' ),
    l1tIgnoreMaskAndPrescale = cms.bool( False ),
    throw = cms.bool( True )
)
process.hltPreDQMCalibrationOutput = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreDQMEventDisplayOutput = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreDQMEventDisplayOutputSmart = cms.EDFilter( "TriggerResultsFilter",
    hltResults = cms.InputTag( "TriggerResults" ),
    l1tResults = cms.InputTag( "" ),
    triggerConditions = cms.vstring( 'HLT_L1SingleMu7_v1' ),
    l1tIgnoreMaskAndPrescale = cms.bool( False ),
    throw = cms.bool( True )
)
process.hltPreRPCMONOutput = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreCalibrationOutput = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreEcalCalibrationOutput = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreALCAPHISYMOutput = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreALCALUMIPIXELSOutput = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreExpressOutput = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreExpressOutputSmart = cms.EDFilter( "TriggerResultsFilter",
    hltResults = cms.InputTag( "TriggerResults" ),
    l1tResults = cms.InputTag( "" ),
    triggerConditions = cms.vstring( 'HLT_L1SingleMuOpen_v2 / 4',
      'HLT_Random_v1 / 2' ),
    l1tIgnoreMaskAndPrescale = cms.bool( False ),
    throw = cms.bool( True )
)
process.hltPreNanoDSTOutput = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltPreDQMHistograms = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
process.hltTriggerRatesMonitor = cms.EDAnalyzer( "TriggerRatesMonitor",
    dqmPath = cms.untracked.string( "HLT/TriggerRates" ),
    hltResults = cms.untracked.InputTag( 'TriggerResults','','HLT' ),
    lumisectionRange = cms.untracked.uint32( 2500 ),
    l1tResults = cms.untracked.InputTag( "hltGtStage2Digis" )
)
process.hltTriggerBxMonitor = cms.EDAnalyzer( "TriggerBxMonitor",
    dqmPath = cms.untracked.string( "HLT/TriggerBx" ),
    hltResults = cms.untracked.InputTag( 'TriggerResults','','HLT' ),
    l1tResults = cms.untracked.InputTag( "hltGtStage2Digis" )
)
process.hltDQMFileSaver = cms.EDAnalyzer( "DQMFileSaver",
    runIsComplete = cms.untracked.bool( False ),
    referenceHandling = cms.untracked.string( "all" ),
    producer = cms.untracked.string( "DQM" ),
    forceRunNumber = cms.untracked.int32( -1 ),
    saveByRun = cms.untracked.int32( 1 ),
    saveAtJobEnd = cms.untracked.bool( False ),
    saveByLumiSection = cms.untracked.int32( 1 ),
    version = cms.untracked.int32( 1 ),
    referenceRequireStatus = cms.untracked.int32( 100 ),
    convention = cms.untracked.string( "FilterUnit" ),
    dirName = cms.untracked.string( "." ),
    fileFormat = cms.untracked.string( "PB" )
)

process.hltOutputPhysics = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_HcalNZS_v2',
  'HLT_HcalPhiSym_v2',
  'HLT_L1SingleEG5_v1',
  'HLT_L1SingleMu3_v1',
  'HLT_L1SingleMu5_v1',
  'HLT_L1SingleMu7_v1',
  'HLT_L1SingleMuOpen_DT_v2',
  'HLT_L1SingleMuOpen_v2',
  'HLT_L1TowerCount40_v1',
  'HLT_Physics_v2',
  'HLT_Random_v1',
  'HLT_ZeroBias_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputDQM = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_HcalNZS_v2',
  'HLT_HcalPhiSym_v2',
  'HLT_L1DoubleMu0_v1',
  'HLT_L1FatEvents_v1',
  'HLT_L1SingleEG5_v1',
  'HLT_L1SingleMu3_v1',
  'HLT_L1SingleMu5_v1',
  'HLT_L1SingleMu7_v1',
  'HLT_L1SingleMuOpen_DT_v2',
  'HLT_L1SingleMuOpen_v2',
  'HLT_Physics_v2',
  'HLT_Random_v1',
  'HLT_ZeroBias_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltCombinedSecondaryVertexBJetTagsCalo_*_*',
      'keep *_hltCombinedSecondaryVertexBJetTagsPF_*_*',
      'keep *_hltIter2Merged_*_*',
      'keep *_hltL3NoFiltersNoVtxMuonCandidates_*_*',
      'keep *_hltOnlineBeamSpot_*_*',
      'keep *_hltPFJetForBtag_*_*',
      'keep *_hltPixelTracks_*_*',
      'keep *_hltSelector8CentralJetsL1FastJet_*_*',
      'keep *_hltSiPixelClusters_*_*',
      'keep *_hltSiStripRawToClustersFacility_*_*',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputDQMCalibration = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_EcalCalibration_v2',
  'HLT_HcalCalibration_v1' ) ),
    outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*',
      'keep *_hltEcalCalibrationRaw_*_*',
      'keep *_hltHcalCalibrationRaw_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputDQMEventDisplay = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_L1SingleMu7_v1' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputRPCMON = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'AlCa_RPCMuonNoHits_v2',
  'AlCa_RPCMuonNoTriggers_v2',
  'AlCa_RPCMuonNormalisation_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltCscSegments_*_*',
      'keep *_hltDt4DSegments_*_*',
      'keep *_hltGtStage2Digis_*_*',
      'keep *_hltMuonCSCDigis_MuonCSCStripDigi_*',
      'keep *_hltMuonCSCDigis_MuonCSCWireDigi_*',
      'keep *_hltMuonDTDigis_*_*',
      'keep *_hltMuonRPCDigis_*_*',
      'keep *_hltRpcRecHits_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputCalibration = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_EcalCalibration_v2',
  'HLT_HcalCalibration_v1' ) ),
    outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*',
      'keep *_hltEcalCalibrationRaw_*_*',
      'keep *_hltHcalCalibrationRaw_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputEcalCalibration = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_EcalCalibration_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *_hlt*_*_*',
      'keep *_hltEcalCalibrationRaw_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputALCAPHISYM = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'AlCa_EcalPhiSym_v4' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltEcalPhiSymFilter_*_*',
      'keep *_hltGtStage2Digis_*_*',
      'keep edmTriggerResults_*_*_*' )
)
process.hltOutputALCALUMIPIXELS = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'AlCa_LumiPixels_Random_v1',
  'AlCa_LumiPixels_ZeroBias_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltFEDSelectorLumiPixels_*_*',
      'keep *_hltGtStage2Digis_*_*',
      'keep edmTriggerResults_*_*_*' )
)
process.hltOutputExpressCosmics = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_L1SingleMuOpen_DT_v2',
  'HLT_L1SingleMuOpen_v2',
  'HLT_Random_v1' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep GlobalObjectMapRecord_hltGtStage2ObjectMap_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputNanoDST = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'DST_Physics_v1' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltFEDSelector_*_*',
      'keep *_hltGtStage2Digis_*_*',
      'keep edmTriggerResults_*_*_*' )
)

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtStage2Digis + process.hltCaloStage2Digis + process.hltGmtStage2Digis + process.hltGtStage2ObjectMap )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )
process.HLTBeginSequenceL1Fat = cms.Sequence( process.hltTriggerType + process.hltL1EventNumberL1Fat + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTBeginSequenceRandom = cms.Sequence( process.hltRandomEventsFilter + process.hltGtStage2Digis )
process.HLTBeginSequenceCalibration = cms.Sequence( process.hltCalibrationEventsFilter + process.hltGtStage2Digis )
process.HLTDoFullUnpackingEgammaEcalSequence = cms.Sequence( process.hltEcalDigis + process.hltEcalPreshowerDigis + process.hltEcalUncalibRecHit + process.hltEcalDetIdToBeRecovered + process.hltEcalRecHit + process.hltEcalPreshowerRecHit )
process.HLTBeginSequenceNZS = cms.Sequence( process.hltTriggerType + process.hltL1EventNumberNZS + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTMuonLocalRecoSequence = cms.Sequence( process.hltMuonDTDigis + process.hltDt1DRecHits + process.hltDt4DSegments + process.hltMuonCSCDigis + process.hltCsc2DRecHits + process.hltCscSegments + process.hltMuonRPCDigis + process.hltRpcRecHits )

process.HLTriggerFirstPath = cms.Path( process.hltGetConditions + process.hltGetRaw + process.hltBoolFalse )
process.HLT_L1SingleMu3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleMu3 + process.hltPreL1SingleMu3 + process.hltL1fL1sMu3L1Filtered0 + process.HLTEndSequence )
process.HLT_L1SingleMu5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleMu5 + process.hltPreL1SingleMu5 + process.hltL1fL1sMu5L1Filtered0 + process.HLTEndSequence )
process.HLT_L1SingleMu7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleMu7 + process.hltPreL1SingleMu7 + process.hltL1fL1sMu7L1Filtered0 + process.HLTEndSequence )
process.HLT_L1SingleMuOpen_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleMuOpen + process.hltPreL1SingleMuOpen + process.hltL1MuOpenL1Filtered0 + process.HLTEndSequence )
process.HLT_L1SingleMuOpen_DT_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleMuOpen + process.hltPreL1SingleMuOpenDT + process.hltL1MuOpenL1FilteredDT + process.HLTEndSequence )
process.HLT_L1FatEvents_v1 = cms.Path( process.HLTBeginSequenceL1Fat + process.hltPreL1FatEvents + process.HLTEndSequence )
process.HLT_Physics_v2 = cms.Path( process.HLTBeginSequence + process.hltPrePhysics + process.HLTEndSequence )
process.DST_Physics_v1 = cms.Path( process.HLTBeginSequence + process.hltPreDSTPhysics + process.HLTEndSequence )
process.HLT_Random_v1 = cms.Path( process.HLTBeginSequenceRandom + process.hltPreRandom + process.HLTEndSequence )
process.HLT_ZeroBias_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBias + process.hltPreZeroBias + process.HLTEndSequence )
process.HLT_L1DoubleMu0_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sDoubleMu0 + process.hltPreL1DoubleMu0 + process.hltDoubleMu0L1Filtered + process.HLTEndSequence )
process.HLT_L1SingleEG5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleEG5 + process.hltPreL1SingleEG5 + process.HLTEndSequence )
process.HLT_EcalCalibration_v2 = cms.Path( process.HLTBeginSequenceCalibration + process.hltPreEcalCalibration + process.hltEcalCalibrationRaw + process.HLTEndSequence )
process.HLT_HcalCalibration_v1 = cms.Path( process.HLTBeginSequenceCalibration + process.hltPreHcalCalibration + process.hltHcalCalibTypeFilter + process.hltHcalCalibrationRaw + process.HLTEndSequence )
process.AlCa_EcalPhiSym_v4 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBiasORAlwaysTrue + process.hltPreAlCaEcalPhiSym + process.HLTDoFullUnpackingEgammaEcalSequence + process.hltEcalPhiSymFilter + process.HLTEndSequence )
process.HLT_HcalNZS_v2 = cms.Path( process.HLTBeginSequenceNZS + process.hltL1sHcalNZS + process.hltPreHcalNZS + process.HLTEndSequence )
process.HLT_HcalPhiSym_v2 = cms.Path( process.HLTBeginSequenceNZS + process.hltL1sSingleEG5IorSingleMuOpen + process.hltPreHcalPhiSym + process.HLTEndSequence )
process.HLT_L1TowerCount40_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sTowerCount40 + process.hltPreL1TowerCount40 + process.HLTEndSequence )
process.AlCa_RPCMuonNoTriggers_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleMu5IorSingleMu7 + process.hltPreAlCaRPCMuonNoTriggers + process.hltRPCMuonNoTriggersL1Filtered0 + process.HLTMuonLocalRecoSequence + process.HLTEndSequence )
process.AlCa_RPCMuonNoHits_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleMu5IorSingleMu7 + process.hltPreAlCaRPCMuonNoHits + process.HLTMuonLocalRecoSequence + process.hltRPCPointProducer + process.hltRPCFilter + process.HLTEndSequence )
process.AlCa_RPCMuonNormalisation_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleMu5IorSingleMu7 + process.hltPreAlCaRPCMuonNormalisation + process.hltRPCMuonNormaL1Filtered0 + process.HLTMuonLocalRecoSequence + process.HLTEndSequence )
process.AlCa_LumiPixels_Random_v1 = cms.Path( process.HLTBeginSequenceRandom + process.hltPreAlCaLumiPixelsRandom + process.hltFEDSelectorLumiPixels + process.HLTEndSequence )
process.AlCa_LumiPixels_ZeroBias_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBias + process.hltPreAlCaLumiPixelsZeroBias + process.hltFEDSelectorLumiPixels + process.HLTEndSequence )
process.HLTriggerFinalPath = cms.Path( process.hltGtStage2Digis + process.hltScalersRawToDigi + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW + process.hltBoolFalse )
process.RatesMonitoring = cms.EndPath( process.hltGtStage2Digis + process.hltPreRatesMonitoring + process.hltHLTriggerJSONMonitoring + process.hltL1TriggerJSONMonitoring )
process.PhysicsEGammaCommissioningOutput = cms.EndPath( process.hltGtStage2Digis + process.hltPrePhysicsEGammaCommissioningOutput + process.hltOutputPhysics )
process.DQMOutput = cms.EndPath( process.hltGtStage2Digis + process.hltPreDQMOutput + process.hltPreDQMOutputSmart + process.hltOutputDQM )
process.DQMCalibrationOutput = cms.EndPath( process.hltGtStage2Digis + process.hltPreDQMCalibrationOutput + process.hltOutputDQMCalibration )
process.DQMEventDisplayOutput = cms.EndPath( process.hltGtStage2Digis + process.hltPreDQMEventDisplayOutput + process.hltPreDQMEventDisplayOutputSmart + process.hltOutputDQMEventDisplay )
process.RPCMONOutput = cms.EndPath( process.hltGtStage2Digis + process.hltPreRPCMONOutput + process.hltOutputRPCMON )
process.CalibrationOutput = cms.EndPath( process.hltGtStage2Digis + process.hltPreCalibrationOutput + process.hltOutputCalibration )
process.EcalCalibrationOutput = cms.EndPath( process.hltGtStage2Digis + process.hltPreEcalCalibrationOutput + process.hltOutputEcalCalibration )
process.ALCAPHISYMOutput = cms.EndPath( process.hltGtStage2Digis + process.hltPreALCAPHISYMOutput + process.hltOutputALCAPHISYM )
process.ALCALUMIPIXELSOutput = cms.EndPath( process.hltGtStage2Digis + process.hltPreALCALUMIPIXELSOutput + process.hltOutputALCALUMIPIXELS )
process.ExpressOutput = cms.EndPath( process.hltGtStage2Digis + process.hltPreExpressOutput + process.hltPreExpressOutputSmart + process.hltOutputExpressCosmics )
process.NanoDSTOutput = cms.EndPath( process.hltGtStage2Digis + process.hltPreNanoDSTOutput + process.hltOutputNanoDST )
process.DQMHistograms = cms.EndPath( process.hltGtStage2Digis + process.hltPreDQMHistograms + process.hltTriggerRatesMonitor + process.hltTriggerBxMonitor + process.hltDQMFileSaver )


process.HLTSchedule = cms.Schedule( *(process.HLTriggerFirstPath, process.HLT_L1SingleMu3_v1, process.HLT_L1SingleMu5_v1, process.HLT_L1SingleMu7_v1, process.HLT_L1SingleMuOpen_v2, process.HLT_L1SingleMuOpen_DT_v2, process.HLT_L1FatEvents_v1, process.HLT_Physics_v2, process.DST_Physics_v1, process.HLT_Random_v1, process.HLT_ZeroBias_v2, process.HLT_L1DoubleMu0_v1, process.HLT_L1SingleEG5_v1, process.HLT_EcalCalibration_v2, process.HLT_HcalCalibration_v1, process.AlCa_EcalPhiSym_v4, process.HLT_HcalNZS_v2, process.HLT_HcalPhiSym_v2, process.HLT_L1TowerCount40_v1, process.AlCa_RPCMuonNoTriggers_v2, process.AlCa_RPCMuonNoHits_v2, process.AlCa_RPCMuonNormalisation_v2, process.AlCa_LumiPixels_Random_v1, process.AlCa_LumiPixels_ZeroBias_v2, process.HLTriggerFinalPath, process.RatesMonitoring, process.PhysicsEGammaCommissioningOutput, process.DQMOutput, process.DQMCalibrationOutput, process.DQMEventDisplayOutput, process.RPCMONOutput, process.CalibrationOutput, process.EcalCalibrationOutput, process.ALCAPHISYMOutput, process.ALCALUMIPIXELSOutput, process.ExpressOutput, process.NanoDSTOutput, process.DQMHistograms ))

