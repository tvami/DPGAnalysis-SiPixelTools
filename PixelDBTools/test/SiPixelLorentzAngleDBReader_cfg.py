import FWCore.ParameterSet.Config as cms

process = cms.Process("Test")
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource",
#    lastRun = cms.untracked.uint32(1),
#    timetype = cms.string('runnumber'),
#    interval = cms.uint32(1),
    firstRun = cms.untracked.uint32(1)
#    firstRun = cms.untracked.uint32(180000),
# iov 1
#    firstRun = cms.untracked.uint32(190000),
#    firstRun = cms.untracked.uint32(190703),
# iov 2
#    firstRun = cms.untracked.uint32(197000),
# iov 3
#    firstRun = cms.untracked.uint32(200000),
# iov 4 
#    firstRun = cms.untracked.uint32(202000),
# iov 5
#    firstRun = cms.untracked.uint32(204000),
# iov 6
#    firstRun = cms.untracked.uint32(206000),
# iov 7
#    firstRun = cms.untracked.uint32(208686),
)


process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("histo.root")
                                   )

process.MessageLogger = cms.Service("MessageLogger",
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('WARNING')
    ),
    destinations = cms.untracked.vstring('cout')
)

#process.Timing = cms.Service("Timing")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "GR_R_70_V1::All"
#process.GlobalTag.globaltag = 'FT_R_53_V21::All'
#process.GlobalTag.globaltag = 'MC_70_V1::All'
#process.GlobalTag.globaltag = 'POSTLS171_V3::All'
#process.GlobalTag.globaltag = 'PRE_MC_71_V5::All'

process.load("Configuration.StandardSequences.GeometryIdeal_cff")

# DB stuff 
useLocalDB = True
if useLocalDB :
  process.QualityReader = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0),
        authenticationPath = cms.untracked.string('')
    ),
    toGet = cms.VPSet(
		cms.PSet(
			record = cms.string("SiPixelLorentzAngleRcd"),
# 			label = cms.untracked.string("fromAlignment"),
# 			label = cms.untracked.string("forWidth"),
#			tag = cms.string("SiPixelLorentzAngle_v02_mc")
#			tag = cms.string("SiPixelLorentzAngle_forWidth_v01_mc")
#			tag = cms.string("SiPixelLorentzAngle_forWidth_v01")
#			tag = cms.string("SiPixelLorentzAngle_fromAlignment_v0_mc")
#			tag = cms.string("SiPixelLorentzAngle_fromAlignment_v01_mc")
#			tag = cms.string("SiPixelLorentzAngle_fromAlignment_v01")
                        # express/prompt, hlt
                        #tag = cms.string("SiPixelLorentzAngle_2009_v1_express")
                        #tag = cms.string("SiPixelLorentzAngle_2009_v1_hlt")
                        # offline
                        #tag = cms.string("SiPixelLorentzAngle_v00")
                        #tag = cms.string("SiPixelLorentzAngle_v01")
                        #tag = cms.string("SiPixelLorentzAngle_offline")
                        #tag = cms.string("SiPixelLorentzAngle_v1_offline")
                        #tag = cms.string("SiPixelLorentzAngle_v02_offline")
                        #tag = cms.string("SiPixelLorentzAngle_v03_offline")
                        tag = cms.string("SiPixelLorentzAngle_v4_offline")
                        #tag = cms.string("SiPixelLorentzAngle_v5_offline")
                        # in v4_offline
                        #tag = cms.string("SiPixelLorentzAngle_r194912_v1")
                        #tag = cms.string("SiPixelLorentzAngle_r196364_v1")
                        #tag = cms.string("SiPixelLorentzAngle_r200091_v2")
                        #tag = cms.string("SiPixelLorentzAngle_r202237_v2")
                        #tag = cms.string("SiPixelLorentzAngle_r203987_v2")
                        #tag = cms.string("SiPixelLorentzAngle_2012_IOV6")
                        #tag = cms.string("SiPixelLorentzAngle_2012_IOV7")
                        # in v5_offline
                        #tag = cms.string("SiPixelLorentzAngle_r194912_v2")
                        #tag = cms.string("SiPixelLorentzAngle_r196364_v2")
                        #tag = cms.string("SiPixelLorentzAngle_r200091_v2")
                        #tag = cms.string("SiPixelLorentzAngle_r202237_v2")
                        #tag = cms.string("SiPixelLorentzAngle_r203987_v2")
                        #tag = cms.string("SiPixelLorentzAngle_2012_IOV6")
                        #tag = cms.string("SiPixelLorentzAngle_2012_IOV7")
		),
#		cms.PSet(
#			record = cms.string("SiPixelLorentzAngleSimRcd"),
#			tag = cms.string("trivial_LorentzAngle_Sim")
#			tag = cms.string("SiPixelLorentzAngleSim_v02_mc")
#		)
	),

#    connect = cms.string('sqlite_file:prova.db')
#    connect = cms.string('sqlite_file:SiPixelLorentzAngle_forWidth_v01_mc.db')
#    connect = cms.string('sqlite_file:SiPixelLorentzAngle_forWidth_v01.db')
#    connect = cms.string('sqlite_file:SiPixelLorentzAngle_fromAlignment_v01_mc.db')
#    connect = cms.string('sqlite_file:SiPixelLorentzAngle_fromAlignment_v01.db')

    connect = cms.string('frontier://FrontierProd/CMS_COND_31X_PIXEL')

  ) # end process
  process.es_prefer_QualityReader = cms.ESPrefer("PoolDBESSource","QualityReader")

#  end if

process.LorentzAngleReader = cms.EDAnalyzer("SiPixelLorentzAngleDBReader",
    printDebug = cms.untracked.bool(True),
    useSimRcd = cms.bool(False)
)

process.LorentzAngleSimReader = cms.EDAnalyzer("SiPixelLorentzAngleDBReader",
    printDebug = cms.untracked.bool(False),
    useSimRcd = cms.bool(True)
                                             
)

#process.p = cms.Path(process.LorentzAngleReader*process.LorentzAngleSimReader)
#process.p = cms.Path(process.LorentzAngleSimReader)
process.p = cms.Path(process.LorentzAngleReader)

