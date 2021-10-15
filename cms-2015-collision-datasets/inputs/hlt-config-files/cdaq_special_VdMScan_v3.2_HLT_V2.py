# /cdaq/special/VdMScan/v3.2/HLT/V2 (CMSSW_7_4_10_patch1)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "HLT" )

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/cdaq/special/VdMScan/v3.2/HLT/V2')
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
    emulator = cms.vstring( 'Lustre' )
  )
)
process.streams = cms.PSet( 
  DQM = cms.vstring( 'OnlineMonitor' ),
  DQMEventDisplay = cms.vstring( 'EventDisplay' ),
  Express = cms.vstring( 'ExpressPhysics' ),
  LookArea = cms.vstring( 'LookAreaPD' ),
  NanoDST = cms.vstring( 'L1Accept' ),
  PhysicsVdM1 = cms.vstring( 'ZeroBias1' ),
  PhysicsVdM2 = cms.vstring( 'ZeroBias2' ),
  PhysicsVdM3 = cms.vstring( 'ZeroBias3' ),
  PhysicsVdM4 = cms.vstring( 'ZeroBias4' ),
  PhysicsVdM5 = cms.vstring( 'ZeroBias5' ),
  PhysicsVdM6 = cms.vstring( 'ZeroBias6' ),
  PhysicsVdM7 = cms.vstring( 'ZeroBias7' ),
  PhysicsVdM8 = cms.vstring( 'ZeroBias8' )
)
process.datasets = cms.PSet( 
  EventDisplay = cms.vstring( 'HLT_L1AlwaysTrue_part1_v1',
    'HLT_L1AlwaysTrue_part2_v1',
    'HLT_L1AlwaysTrue_part3_v1',
    'HLT_L1AlwaysTrue_part4_v1',
    'HLT_L1AlwaysTrue_part5_v1',
    'HLT_L1AlwaysTrue_part6_v1',
    'HLT_L1AlwaysTrue_part7_v1',
    'HLT_L1AlwaysTrue_part8_v1',
    'HLT_ZeroBias_part1_v2',
    'HLT_ZeroBias_part2_v2',
    'HLT_ZeroBias_part3_v2',
    'HLT_ZeroBias_part4_v2',
    'HLT_ZeroBias_part5_v2',
    'HLT_ZeroBias_part6_v2',
    'HLT_ZeroBias_part7_v2',
    'HLT_ZeroBias_part8_v2' ),
  ExpressPhysics = cms.vstring( 'HLT_L1AlwaysTrue_part1_v1',
    'HLT_L1AlwaysTrue_part2_v1',
    'HLT_L1AlwaysTrue_part3_v1',
    'HLT_L1AlwaysTrue_part4_v1',
    'HLT_L1AlwaysTrue_part5_v1',
    'HLT_L1AlwaysTrue_part6_v1',
    'HLT_L1AlwaysTrue_part7_v1',
    'HLT_L1AlwaysTrue_part8_v1',
    'HLT_ZeroBias_part1_v2',
    'HLT_ZeroBias_part2_v2',
    'HLT_ZeroBias_part3_v2',
    'HLT_ZeroBias_part4_v2',
    'HLT_ZeroBias_part5_v2',
    'HLT_ZeroBias_part6_v2',
    'HLT_ZeroBias_part7_v2',
    'HLT_ZeroBias_part8_v2' ),
  L1Accept = cms.vstring( 'DST_Physics_v1' ),
  LookAreaPD = cms.vstring( 'HLT_L1AlwaysTrue_part1_v1',
    'HLT_L1AlwaysTrue_part2_v1',
    'HLT_L1AlwaysTrue_part3_v1',
    'HLT_L1AlwaysTrue_part4_v1',
    'HLT_L1AlwaysTrue_part5_v1',
    'HLT_L1AlwaysTrue_part6_v1',
    'HLT_L1AlwaysTrue_part7_v1',
    'HLT_L1AlwaysTrue_part8_v1',
    'HLT_ZeroBias_part1_v2',
    'HLT_ZeroBias_part2_v2',
    'HLT_ZeroBias_part3_v2',
    'HLT_ZeroBias_part4_v2',
    'HLT_ZeroBias_part5_v2',
    'HLT_ZeroBias_part6_v2',
    'HLT_ZeroBias_part7_v2',
    'HLT_ZeroBias_part8_v2' ),
  OnlineMonitor = cms.vstring( 'HLT_L1AlwaysTrue_part1_v1',
    'HLT_L1AlwaysTrue_part2_v1',
    'HLT_L1AlwaysTrue_part3_v1',
    'HLT_L1AlwaysTrue_part4_v1',
    'HLT_L1AlwaysTrue_part5_v1',
    'HLT_L1AlwaysTrue_part6_v1',
    'HLT_L1AlwaysTrue_part7_v1',
    'HLT_L1AlwaysTrue_part8_v1',
    'HLT_ZeroBias_part1_v2',
    'HLT_ZeroBias_part2_v2',
    'HLT_ZeroBias_part3_v2',
    'HLT_ZeroBias_part4_v2',
    'HLT_ZeroBias_part5_v2',
    'HLT_ZeroBias_part6_v2',
    'HLT_ZeroBias_part7_v2',
    'HLT_ZeroBias_part8_v2' ),
  ZeroBias1 = cms.vstring( 'HLT_L1AlwaysTrue_part1_v1',
    'HLT_ZeroBias_part1_v2' ),
  ZeroBias2 = cms.vstring( 'HLT_L1AlwaysTrue_part2_v1',
    'HLT_ZeroBias_part2_v2' ),
  ZeroBias3 = cms.vstring( 'HLT_L1AlwaysTrue_part3_v1',
    'HLT_ZeroBias_part3_v2' ),
  ZeroBias4 = cms.vstring( 'HLT_L1AlwaysTrue_part4_v1',
    'HLT_ZeroBias_part4_v2' ),
  ZeroBias5 = cms.vstring( 'HLT_L1AlwaysTrue_part5_v1',
    'HLT_ZeroBias_part5_v2' ),
  ZeroBias6 = cms.vstring( 'HLT_L1AlwaysTrue_part6_v1',
    'HLT_ZeroBias_part6_v2' ),
  ZeroBias7 = cms.vstring( 'HLT_L1AlwaysTrue_part7_v1',
    'HLT_ZeroBias_part7_v2' ),
  ZeroBias8 = cms.vstring( 'HLT_L1AlwaysTrue_part8_v1',
    'HLT_ZeroBias_part8_v2' )
)

process.source = cms.Source( "FedRawDataInputSource",
    numBuffers = cms.untracked.uint32( 2 ),
    useL1EventID = cms.untracked.bool( False ),
    eventChunkSize = cms.untracked.uint32( 32 ),
    eventChunkBlock = cms.untracked.uint32( 32 ),
    getLSFromFilename = cms.untracked.bool( True ),
    verifyAdler32 = cms.untracked.bool( True )
)

process.GlobalTag = cms.ESSource( "PoolDBESSource",
    globaltag = cms.string( "74X_dataRun2_HLT_v1" ),
    RefreshEachRun = cms.untracked.bool( True ),
    RefreshOpenIOVs = cms.untracked.bool( False ),
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
    BlobStreamerName = cms.untracked.string( "TBufferBlobStreamingService" ),
    DumpStat = cms.untracked.bool( False )
)

process.FastTimerService = cms.Service( "FastTimerService",
    dqmPath = cms.untracked.string( "HLT/TimerService" ),
    dqmModuleTimeRange = cms.untracked.double( 40.0 ),
    useRealTimeClock = cms.untracked.bool( True ),
    enableTimingModules = cms.untracked.bool( True ),
    enableDQM = cms.untracked.bool( True ),
    enableDQMbyModule = cms.untracked.bool( False ),
    enableTimingExclusive = cms.untracked.bool( False ),
    skipFirstPath = cms.untracked.bool( False ),
    enableDQMbyLumiSection = cms.untracked.bool( True ),
    dqmPathTimeResolution = cms.untracked.double( 0.5 ),
    dqmPathTimeRange = cms.untracked.double( 100.0 ),
    dqmTimeRange = cms.untracked.double( 1000.0 ),
    dqmLumiSectionsRange = cms.untracked.uint32( 2500 ),
    enableDQMbyProcesses = cms.untracked.bool( True ),
    enableDQMSummary = cms.untracked.bool( True ),
    enableTimingSummary = cms.untracked.bool( False ),
    enableDQMbyPathTotal = cms.untracked.bool( True ),
    enableTimingPaths = cms.untracked.bool( True ),
    enableDQMbyPathExclusive = cms.untracked.bool( True ),
    dqmTimeResolution = cms.untracked.double( 5.0 ),
    dqmModuleTimeResolution = cms.untracked.double( 0.2 ),
    enableDQMbyPathActive = cms.untracked.bool( True ),
    enableDQMbyPathDetails = cms.untracked.bool( True ),
    enableDQMbyPathOverhead = cms.untracked.bool( False ),
    enableDQMbyPathCounters = cms.untracked.bool( True ),
    enableDQMbyModuleType = cms.untracked.bool( False )
)
process.FastMonitoringService = cms.Service( "FastMonitoringService",
    slowName = cms.untracked.string( "slowmoni" ),
    sleepTime = cms.untracked.int32( 1 ),
    fastMonIntervals = cms.untracked.uint32( 2 ),
    fastName = cms.untracked.string( "fastmoni" )
)
process.EvFDaqDirector = cms.Service( "EvFDaqDirector",
    buBaseDir = cms.untracked.string( "." ),
    outputAdler32Recheck = cms.untracked.bool( False ),
    fuLockPollInterval = cms.untracked.uint32( 2000 ),
    runNumber = cms.untracked.uint32( 0 ),
    baseDir = cms.untracked.string( "." ),
    selectedTransferMode = cms.untracked.string( "" ),
    requireTransfersPSet = cms.untracked.bool( False )
)
process.DQMStore = cms.Service( "DQMStore",
    verbose = cms.untracked.int32( 0 ),
    collateHistograms = cms.untracked.bool( False ),
    enableMultiThread = cms.untracked.bool( True ),
    forceResetOnBeginLumi = cms.untracked.bool( False ),
    LSbasedMode = cms.untracked.bool( True ),
    verboseQT = cms.untracked.int32( 0 )
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
      cms.PSet(  pathName = cms.string( "HLT_L1AlwaysTrue_part1_v1" ),
        prescales = cms.vuint32( 16, 24, 32, 48, 64, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_L1AlwaysTrue_part2_v1" ),
        prescales = cms.vuint32( 16, 24, 32, 48, 64, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_L1AlwaysTrue_part3_v1" ),
        prescales = cms.vuint32( 16, 24, 32, 48, 64, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_L1AlwaysTrue_part4_v1" ),
        prescales = cms.vuint32( 16, 24, 32, 48, 64, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_L1AlwaysTrue_part5_v1" ),
        prescales = cms.vuint32( 16, 24, 32, 48, 64, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_L1AlwaysTrue_part6_v1" ),
        prescales = cms.vuint32( 16, 24, 32, 48, 64, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_L1AlwaysTrue_part7_v1" ),
        prescales = cms.vuint32( 16, 24, 32, 48, 64, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_L1AlwaysTrue_part8_v1" ),
        prescales = cms.vuint32( 16, 24, 32, 48, 64, 0, 0, 0, 0, 0 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_ZeroBias_part1_v2" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 16, 24, 32, 48, 64 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_ZeroBias_part2_v2" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 16, 24, 32, 48, 64 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_ZeroBias_part3_v2" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 16, 24, 32, 48, 64 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_ZeroBias_part4_v2" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 16, 24, 32, 48, 64 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_ZeroBias_part5_v2" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 16, 24, 32, 48, 64 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_ZeroBias_part6_v2" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 16, 24, 32, 48, 64 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_ZeroBias_part7_v2" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 16, 24, 32, 48, 64 )
      ),
      cms.PSet(  pathName = cms.string( "HLT_ZeroBias_part8_v2" ),
        prescales = cms.vuint32( 0, 0, 0, 0, 0, 16, 24, 32, 48, 64 )
      ),
      cms.PSet(  pathName = cms.string( "DST_Physics_v1" ),
        prescales = cms.vuint32( 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 )
      ),
      cms.PSet(  pathName = cms.string( "DQMOutput" ),
        prescales = cms.vuint32( 200, 100, 50, 20, 10, 200, 100, 50, 20, 10 )
      ),
      cms.PSet(  pathName = cms.string( "LookAreaOutput" ),
        prescales = cms.vuint32( 200, 100, 50, 20, 10, 200, 100, 50, 20, 10 )
      ),
      cms.PSet(  pathName = cms.string( "ExpressOutput" ),
        prescales = cms.vuint32( 1000, 500, 250, 100, 50, 1000, 500, 250, 100, 50 )
      )
    ),
    lvl1DefaultLabel = cms.string( "2kHzZeroBias" ),
    lvl1Labels = cms.vstring( '18kHz',
      '9kHz',
      '6kHz',
      '4kHz',
      '2kHz',
      '18kHzZeroBias',
      '9kHzZeroBias',
      '6kHzZeroBias',
      '4kHzZeroBias',
      '2kHzZeroBias' )
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
process.hltGtDigis = cms.EDProducer( "L1GlobalTriggerRawToDigi",
    DaqGtFedId = cms.untracked.int32( 813 ),
    Verbosity = cms.untracked.int32( 0 ),
    UnpackBxInEvent = cms.int32( 5 ),
    ActiveBoardsMask = cms.uint32( 0xffff ),
    DaqGtInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltCaloStage1Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage1::CaloSetup" ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    FWId = cms.uint32( 4294967295 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1352 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    FWOverride = cms.bool( False )
)
process.hltCaloStage1LegacyFormatDigis = cms.EDProducer( "L1TCaloUpgradeToGCTConverter",
    InputHFCountsCollection = cms.InputTag( 'hltCaloStage1Digis','HFBitCounts' ),
    InputHFSumsCollection = cms.InputTag( 'hltCaloStage1Digis','HFRingSums' ),
    bxMin = cms.int32( 0 ),
    bxMax = cms.int32( 0 ),
    InputCollection = cms.InputTag( "hltCaloStage1Digis" ),
    InputIsoTauCollection = cms.InputTag( 'hltCaloStage1Digis','isoTaus' ),
    InputRlxTauCollection = cms.InputTag( 'hltCaloStage1Digis','rlxTaus' )
)
process.hltL1GtObjectMap = cms.EDProducer( "L1GlobalTrigger",
    TechnicalTriggersUnprescaled = cms.bool( True ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    AlgorithmTriggersUnmasked = cms.bool( False ),
    EmulateBxInEvent = cms.int32( 1 ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    ProduceL1GtDaqRecord = cms.bool( False ),
    ReadTechnicalTriggerRecords = cms.bool( True ),
    RecordLength = cms.vint32( 3, 0 ),
    TechnicalTriggersUnmasked = cms.bool( False ),
    ProduceL1GtEvmRecord = cms.bool( False ),
    GmtInputTag = cms.InputTag( "hltGtDigis" ),
    TechnicalTriggersVetoUnmasked = cms.bool( True ),
    AlternativeNrBxBoardEvm = cms.uint32( 0 ),
    TechnicalTriggersInputTags = cms.VInputTag( 'simBscDigis' ),
    CastorInputTag = cms.InputTag( "castorL1Digis" ),
    GctInputTag = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    WritePsbL1GtDaqRecord = cms.bool( False ),
    BstLengthBytes = cms.int32( -1 )
)
process.hltL1extraParticles = cms.EDProducer( "L1ExtraParticlesProd",
    tauJetSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','tauJets' ),
    etHadSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    isoTauJetSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','isoTauJets' ),
    etTotalSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    centralBxOnly = cms.bool( True ),
    centralJetSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','cenJets' ),
    etMissSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    hfRingEtSumsSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    produceMuonParticles = cms.bool( True ),
    forwardJetSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','forJets' ),
    ignoreHtMiss = cms.bool( False ),
    htMissSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" ),
    produceCaloParticles = cms.bool( True ),
    muonSource = cms.InputTag( "hltGtDigis" ),
    isolatedEmSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','isoEm' ),
    nonIsolatedEmSource = cms.InputTag( 'hltCaloStage1LegacyFormatDigis','nonIsoEm' ),
    hfRingBitCountsSource = cms.InputTag( "hltCaloStage1LegacyFormatDigis" )
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
process.hltL1sL1AlwaysTrue = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_AlwaysTrue" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreL1AlwaysTruepart1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltPreL1AlwaysTruepart2 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 1 )
)
process.hltPreL1AlwaysTruepart3 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 2 )
)
process.hltPreL1AlwaysTruepart4 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 3 )
)
process.hltPreL1AlwaysTruepart5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 4 )
)
process.hltPreL1AlwaysTruepart6 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 5 )
)
process.hltPreL1AlwaysTruepart7 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 6 )
)
process.hltPreL1AlwaysTruepart8 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 7 )
)
process.hltL1sL1ZeroBias = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_ZeroBias" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreZeroBiaspart1 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 1 )
)
process.hltPreZeroBiaspart2 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 2 )
)
process.hltPreZeroBiaspart3 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 3 )
)
process.hltPreZeroBiaspart4 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 4 )
)
process.hltPreZeroBiaspart5 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 5 )
)
process.hltPreZeroBiaspart6 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 6 )
)
process.hltPreZeroBiaspart7 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 7 )
)
process.hltPreZeroBiaspart8 = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 8 )
)
process.hltPreDSTPhysics = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 1023 )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    processName = cms.string( "@" )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)
process.hltTriggerRatesMonitor = cms.EDAnalyzer( "TriggerRatesMonitor",
    dqmPath = cms.untracked.string( "HLT/TriggerRates" ),
    hltResults = cms.untracked.InputTag( 'TriggerResults','','HLT' ),
    lumisectionRange = cms.untracked.uint32( 2500 ),
    l1tResults = cms.untracked.InputTag( "hltGtDigis" )
)
process.hltTriggerJSONMonitoring = cms.EDAnalyzer( "TriggerJSONMonitoring",
    triggerResults = cms.InputTag( 'TriggerResults','','HLT' ),
    L1Results = cms.InputTag( "hltGtDigis" )
)
process.hltDQMSaver = cms.EDAnalyzer( "DQMFileSaver",
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
process.hltPreDQMOutput = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPreDQMOutputSmart = cms.EDFilter( "TriggerResultsFilter",
    l1tIgnoreMask = cms.bool( False ),
    l1tResults = cms.InputTag( "hltGtDigis" ),
    l1techIgnorePrescales = cms.bool( False ),
    hltResults = cms.InputTag( "TriggerResults" ),
    triggerConditions = cms.vstring( 'HLT_L1AlwaysTrue_part1_v1',
      'HLT_L1AlwaysTrue_part2_v1',
      'HLT_L1AlwaysTrue_part3_v1',
      'HLT_L1AlwaysTrue_part4_v1',
      'HLT_L1AlwaysTrue_part5_v1',
      'HLT_L1AlwaysTrue_part6_v1',
      'HLT_L1AlwaysTrue_part7_v1',
      'HLT_L1AlwaysTrue_part8_v1',
      'HLT_ZeroBias_part1_v2',
      'HLT_ZeroBias_part2_v2',
      'HLT_ZeroBias_part3_v2',
      'HLT_ZeroBias_part4_v2',
      'HLT_ZeroBias_part5_v2',
      'HLT_ZeroBias_part6_v2',
      'HLT_ZeroBias_part7_v2',
      'HLT_ZeroBias_part8_v2' ),
    throw = cms.bool( True ),
    daqPartitions = cms.uint32( 1 )
)
process.hltPreLookAreaOutput = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPreLookAreaOutputSmart = cms.EDFilter( "TriggerResultsFilter",
    l1tIgnoreMask = cms.bool( False ),
    l1tResults = cms.InputTag( "hltGtDigis" ),
    l1techIgnorePrescales = cms.bool( False ),
    hltResults = cms.InputTag( "TriggerResults" ),
    triggerConditions = cms.vstring( 'HLT_L1AlwaysTrue_part1_v1 / 2',
      'HLT_L1AlwaysTrue_part2_v1 / 2',
      'HLT_L1AlwaysTrue_part3_v1 / 2',
      'HLT_L1AlwaysTrue_part4_v1 / 2',
      'HLT_L1AlwaysTrue_part5_v1 / 2',
      'HLT_L1AlwaysTrue_part6_v1 / 2',
      'HLT_L1AlwaysTrue_part7_v1 / 2',
      'HLT_L1AlwaysTrue_part8_v1 / 2',
      'HLT_ZeroBias_part1_v2 / 2',
      'HLT_ZeroBias_part2_v2 / 2',
      'HLT_ZeroBias_part3_v2 / 2',
      'HLT_ZeroBias_part4_v2 / 2',
      'HLT_ZeroBias_part5_v2 / 2',
      'HLT_ZeroBias_part6_v2 / 2',
      'HLT_ZeroBias_part7_v2 / 2',
      'HLT_ZeroBias_part8_v2 / 2' ),
    throw = cms.bool( True ),
    daqPartitions = cms.uint32( 1 )
)
process.hltPreDQMEventDisplayOutput = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPreDQMEventDisplayOutputSmart = cms.EDFilter( "TriggerResultsFilter",
    l1tIgnoreMask = cms.bool( False ),
    l1tResults = cms.InputTag( "hltGtDigis" ),
    l1techIgnorePrescales = cms.bool( False ),
    hltResults = cms.InputTag( "TriggerResults" ),
    triggerConditions = cms.vstring( 'HLT_L1AlwaysTrue_part1_v1 / 1000',
      'HLT_L1AlwaysTrue_part2_v1 / 1000',
      'HLT_L1AlwaysTrue_part3_v1 / 1000',
      'HLT_L1AlwaysTrue_part4_v1 / 1000',
      'HLT_L1AlwaysTrue_part5_v1 / 1000',
      'HLT_L1AlwaysTrue_part6_v1 / 1000',
      'HLT_L1AlwaysTrue_part7_v1 / 1000',
      'HLT_L1AlwaysTrue_part8_v1 / 1000',
      'HLT_ZeroBias_part1_v2 / 1000',
      'HLT_ZeroBias_part2_v2 / 1000',
      'HLT_ZeroBias_part3_v2 / 1000',
      'HLT_ZeroBias_part4_v2 / 1000',
      'HLT_ZeroBias_part5_v2 / 1000',
      'HLT_ZeroBias_part6_v2 / 1000',
      'HLT_ZeroBias_part7_v2 / 1000',
      'HLT_ZeroBias_part8_v2 / 1000' ),
    throw = cms.bool( True ),
    daqPartitions = cms.uint32( 1 )
)
process.hltPreExpressOutput = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltPreExpressOutputSmart = cms.EDFilter( "TriggerResultsFilter",
    l1tIgnoreMask = cms.bool( False ),
    l1tResults = cms.InputTag( "hltGtDigis" ),
    l1techIgnorePrescales = cms.bool( False ),
    hltResults = cms.InputTag( "TriggerResults" ),
    triggerConditions = cms.vstring( 'HLT_L1AlwaysTrue_part1_v1',
      'HLT_L1AlwaysTrue_part2_v1',
      'HLT_L1AlwaysTrue_part3_v1',
      'HLT_L1AlwaysTrue_part4_v1',
      'HLT_L1AlwaysTrue_part5_v1',
      'HLT_L1AlwaysTrue_part6_v1',
      'HLT_L1AlwaysTrue_part7_v1',
      'HLT_L1AlwaysTrue_part8_v1',
      'HLT_ZeroBias_part1_v2',
      'HLT_ZeroBias_part2_v2',
      'HLT_ZeroBias_part3_v2',
      'HLT_ZeroBias_part4_v2',
      'HLT_ZeroBias_part5_v2',
      'HLT_ZeroBias_part6_v2',
      'HLT_ZeroBias_part7_v2',
      'HLT_ZeroBias_part8_v2' ),
    throw = cms.bool( True ),
    daqPartitions = cms.uint32( 1 )
)
process.hltPreNanoDSTOutput = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)

process.hltOutputPhysicsVdM1 = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_L1AlwaysTrue_part1_v1',
  'HLT_ZeroBias_part1_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltL1GtObjectMap_*_*',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputPhysicsVdM2 = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_L1AlwaysTrue_part2_v1',
  'HLT_ZeroBias_part2_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltL1GtObjectMap_*_*',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputPhysicsVdM3 = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_L1AlwaysTrue_part3_v1',
  'HLT_ZeroBias_part3_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltL1GtObjectMap_*_*',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputPhysicsVdM4 = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_L1AlwaysTrue_part4_v1',
  'HLT_ZeroBias_part4_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltL1GtObjectMap_*_*',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputPhysicsVdM5 = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_L1AlwaysTrue_part5_v1',
  'HLT_ZeroBias_part5_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltL1GtObjectMap_*_*',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputPhysicsVdM6 = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_L1AlwaysTrue_part6_v1',
  'HLT_ZeroBias_part6_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltL1GtObjectMap_*_*',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputPhysicsVdM7 = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_L1AlwaysTrue_part7_v1',
  'HLT_ZeroBias_part7_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltL1GtObjectMap_*_*',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputPhysicsVdM8 = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_L1AlwaysTrue_part8_v1',
  'HLT_ZeroBias_part8_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltL1GtObjectMap_*_*',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputDQM = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_L1AlwaysTrue_part1_v1',
  'HLT_L1AlwaysTrue_part2_v1',
  'HLT_L1AlwaysTrue_part3_v1',
  'HLT_L1AlwaysTrue_part4_v1',
  'HLT_L1AlwaysTrue_part5_v1',
  'HLT_L1AlwaysTrue_part6_v1',
  'HLT_L1AlwaysTrue_part7_v1',
  'HLT_L1AlwaysTrue_part8_v1',
  'HLT_ZeroBias_part1_v2',
  'HLT_ZeroBias_part2_v2',
  'HLT_ZeroBias_part3_v2',
  'HLT_ZeroBias_part4_v2',
  'HLT_ZeroBias_part5_v2',
  'HLT_ZeroBias_part6_v2',
  'HLT_ZeroBias_part7_v2',
  'HLT_ZeroBias_part8_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltL1GtObjectMap_*_*',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputLookArea = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_L1AlwaysTrue_part1_v1',
  'HLT_L1AlwaysTrue_part2_v1',
  'HLT_L1AlwaysTrue_part3_v1',
  'HLT_L1AlwaysTrue_part4_v1',
  'HLT_L1AlwaysTrue_part5_v1',
  'HLT_L1AlwaysTrue_part6_v1',
  'HLT_L1AlwaysTrue_part7_v1',
  'HLT_L1AlwaysTrue_part8_v1',
  'HLT_ZeroBias_part1_v2',
  'HLT_ZeroBias_part2_v2',
  'HLT_ZeroBias_part3_v2',
  'HLT_ZeroBias_part4_v2',
  'HLT_ZeroBias_part5_v2',
  'HLT_ZeroBias_part6_v2',
  'HLT_ZeroBias_part7_v2',
  'HLT_ZeroBias_part8_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltL1GtObjectMap_*_*',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputDQMEventDisplay = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_L1AlwaysTrue_part1_v1',
  'HLT_L1AlwaysTrue_part2_v1',
  'HLT_L1AlwaysTrue_part3_v1',
  'HLT_L1AlwaysTrue_part4_v1',
  'HLT_L1AlwaysTrue_part5_v1',
  'HLT_L1AlwaysTrue_part6_v1',
  'HLT_L1AlwaysTrue_part7_v1',
  'HLT_L1AlwaysTrue_part8_v1',
  'HLT_ZeroBias_part1_v2',
  'HLT_ZeroBias_part2_v2',
  'HLT_ZeroBias_part3_v2',
  'HLT_ZeroBias_part4_v2',
  'HLT_ZeroBias_part5_v2',
  'HLT_ZeroBias_part6_v2',
  'HLT_ZeroBias_part7_v2',
  'HLT_ZeroBias_part8_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputExpress = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'HLT_L1AlwaysTrue_part1_v1',
  'HLT_L1AlwaysTrue_part2_v1',
  'HLT_L1AlwaysTrue_part3_v1',
  'HLT_L1AlwaysTrue_part4_v1',
  'HLT_L1AlwaysTrue_part5_v1',
  'HLT_L1AlwaysTrue_part6_v1',
  'HLT_L1AlwaysTrue_part7_v1',
  'HLT_L1AlwaysTrue_part8_v1',
  'HLT_ZeroBias_part1_v2',
  'HLT_ZeroBias_part2_v2',
  'HLT_ZeroBias_part3_v2',
  'HLT_ZeroBias_part4_v2',
  'HLT_ZeroBias_part5_v2',
  'HLT_ZeroBias_part6_v2',
  'HLT_ZeroBias_part7_v2',
  'HLT_ZeroBias_part8_v2' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltL1GtObjectMap_*_*',
      'keep FEDRawDataCollection_rawDataCollector_*_*',
      'keep FEDRawDataCollection_source_*_*',
      'keep edmTriggerResults_*_*_*',
      'keep triggerTriggerEvent_*_*_*' )
)
process.hltOutputNanoDST = cms.OutputModule( "ShmStreamConsumer",
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'DST_Physics_v1' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep *_hltFEDSelector_*_*',
      'keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*',
      'keep L1MuGMTReadoutCollection_hltGtDigis_*_*',
      'keep edmTriggerResults_*_*_*' )
)

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtDigis + process.hltCaloStage1Digis + process.hltCaloStage1LegacyFormatDigis + process.hltL1GtObjectMap + process.hltL1extraParticles )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )

process.HLTriggerFirstPath = cms.Path( process.hltGetConditions + process.hltGetRaw + process.hltBoolFalse )
process.HLT_L1AlwaysTrue_part1_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1AlwaysTrue + process.hltPreL1AlwaysTruepart1 + process.HLTEndSequence )
process.HLT_L1AlwaysTrue_part2_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1AlwaysTrue + process.hltPreL1AlwaysTruepart2 + process.HLTEndSequence )
process.HLT_L1AlwaysTrue_part3_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1AlwaysTrue + process.hltPreL1AlwaysTruepart3 + process.HLTEndSequence )
process.HLT_L1AlwaysTrue_part4_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1AlwaysTrue + process.hltPreL1AlwaysTruepart4 + process.HLTEndSequence )
process.HLT_L1AlwaysTrue_part5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1AlwaysTrue + process.hltPreL1AlwaysTruepart5 + process.HLTEndSequence )
process.HLT_L1AlwaysTrue_part6_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1AlwaysTrue + process.hltPreL1AlwaysTruepart6 + process.HLTEndSequence )
process.HLT_L1AlwaysTrue_part7_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1AlwaysTrue + process.hltPreL1AlwaysTruepart7 + process.HLTEndSequence )
process.HLT_L1AlwaysTrue_part8_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1AlwaysTrue + process.hltPreL1AlwaysTruepart8 + process.HLTEndSequence )
process.HLT_ZeroBias_part1_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBias + process.hltPreZeroBiaspart1 + process.HLTEndSequence )
process.HLT_ZeroBias_part2_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBias + process.hltPreZeroBiaspart2 + process.HLTEndSequence )
process.HLT_ZeroBias_part3_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBias + process.hltPreZeroBiaspart3 + process.HLTEndSequence )
process.HLT_ZeroBias_part4_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBias + process.hltPreZeroBiaspart4 + process.HLTEndSequence )
process.HLT_ZeroBias_part5_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBias + process.hltPreZeroBiaspart5 + process.HLTEndSequence )
process.HLT_ZeroBias_part6_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBias + process.hltPreZeroBiaspart6 + process.HLTEndSequence )
process.HLT_ZeroBias_part7_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBias + process.hltPreZeroBiaspart7 + process.HLTEndSequence )
process.HLT_ZeroBias_part8_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBias + process.hltPreZeroBiaspart8 + process.HLTEndSequence )
process.DST_Physics_v1 = cms.Path( process.HLTBeginSequence + process.hltPreDSTPhysics + process.HLTEndSequence )
process.HLTriggerFinalPath = cms.Path( process.hltGtDigis + process.hltScalersRawToDigi + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW + process.hltBoolFalse )
process.RatesMonitoring = cms.EndPath( process.hltGtDigis + process.hltTriggerRatesMonitor + process.hltTriggerJSONMonitoring )
process.PhysicsVdM1Output = cms.EndPath( process.hltOutputPhysicsVdM1 )
process.PhysicsVdM2Output = cms.EndPath( process.hltOutputPhysicsVdM2 )
process.PhysicsVdM3Output = cms.EndPath( process.hltOutputPhysicsVdM3 )
process.PhysicsVdM4Output = cms.EndPath( process.hltOutputPhysicsVdM4 )
process.PhysicsVdM5Output = cms.EndPath( process.hltOutputPhysicsVdM5 )
process.PhysicsVdM6Output = cms.EndPath( process.hltOutputPhysicsVdM6 )
process.PhysicsVdM7Output = cms.EndPath( process.hltOutputPhysicsVdM7 )
process.PhysicsVdM8Output = cms.EndPath( process.hltOutputPhysicsVdM8 )
process.DQMOutput = cms.EndPath( process.hltDQMSaver + process.hltGtDigis + process.hltPreDQMOutput + process.hltPreDQMOutputSmart + process.hltOutputDQM )
process.LookAreaOutput = cms.EndPath( process.hltDQMSaver + process.hltGtDigis + process.hltPreLookAreaOutput + process.hltPreLookAreaOutputSmart + process.hltOutputLookArea )
process.DQMEventDisplayOutput = cms.EndPath( process.hltGtDigis + process.hltPreDQMEventDisplayOutput + process.hltPreDQMEventDisplayOutputSmart + process.hltOutputDQMEventDisplay )
process.ExpressOutput = cms.EndPath( process.hltGtDigis + process.hltPreExpressOutput + process.hltPreExpressOutputSmart + process.hltOutputExpress )
process.NanoDSTOutput = cms.EndPath( process.hltGtDigis + process.hltPreNanoDSTOutput + process.hltOutputNanoDST )


process.HLTSchedule = cms.Schedule( *(process.HLTriggerFirstPath, process.HLT_L1AlwaysTrue_part1_v1, process.HLT_L1AlwaysTrue_part2_v1, process.HLT_L1AlwaysTrue_part3_v1, process.HLT_L1AlwaysTrue_part4_v1, process.HLT_L1AlwaysTrue_part5_v1, process.HLT_L1AlwaysTrue_part6_v1, process.HLT_L1AlwaysTrue_part7_v1, process.HLT_L1AlwaysTrue_part8_v1, process.HLT_ZeroBias_part1_v2, process.HLT_ZeroBias_part2_v2, process.HLT_ZeroBias_part3_v2, process.HLT_ZeroBias_part4_v2, process.HLT_ZeroBias_part5_v2, process.HLT_ZeroBias_part6_v2, process.HLT_ZeroBias_part7_v2, process.HLT_ZeroBias_part8_v2, process.DST_Physics_v1, process.HLTriggerFinalPath, process.RatesMonitoring, process.PhysicsVdM1Output, process.PhysicsVdM2Output, process.PhysicsVdM3Output, process.PhysicsVdM4Output, process.PhysicsVdM5Output, process.PhysicsVdM6Output, process.PhysicsVdM7Output, process.PhysicsVdM8Output, process.DQMOutput, process.LookAreaOutput, process.DQMEventDisplayOutput, process.ExpressOutput, process.NanoDSTOutput ))

