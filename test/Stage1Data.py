import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')

options.register ('eActivityCut',   4, VarParsing.multiplicity.singleton, VarParsing.varType.int,
                  "Tau Veto HCAL Activity Threshold")
options.register ('hActivityCut',   4, VarParsing.multiplicity.singleton, VarParsing.varType.int,
                  "Tau Veto ECAL Activity Threshold")
options.register ('tauThresh',      7, VarParsing.multiplicity.singleton, VarParsing.varType.int,
                  "Tau Seed Threshold")
options.register ('tauNThresh',     0, VarParsing.multiplicity.singleton, VarParsing.varType.int,
                  "Tau Neighbor Seed Threshold")
options.register ('maxPtTauVeto',  64, VarParsing.multiplicity.singleton, VarParsing.varType.int,
                  "Tau max Pt Tau Veto")
options.register ('tauMinPtIso',  192, VarParsing.multiplicity.singleton, VarParsing.varType.int,
                  "Tau Isolation Pt Threshold")
options.register ('tauMaxJetIso', 100, VarParsing.multiplicity.singleton, VarParsing.varType.int,
                  "Tau Veto ECAL Activity Threshold")
options.register ('tauIsoValue',  0.1, VarParsing.multiplicity.singleton, VarParsing.varType.float,
                  "Tau Isolation Cut")

options.parseArguments()
print '========Tau Parameter Configuration======='
print 'eActivityCut =   ',options.eActivityCut,' GeV'
print 'hActivityCut =   ',options.hActivityCut,' GeV'
print 'tauThresh    =   ',options.tauThresh,' GeV'
print 'tauNThresh   =   ',options.tauNThresh,' GeV'
print 'maxPtTauVeto =  ',options.maxPtTauVeto,' GeV'
print 'tauMinPtIso  = ',options.tauMinPtIso,' GeV'
print 'tauMaxJetIso = ',options.tauMaxJetIso,' GeV'
print 'tauIsoValue  = ',options.tauIsoValue

process = cms.Process('L1TEMULATION')

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.Geometry.GeometryIdeal_cff')

# Select the Message Logger output you would like to see:
process.load('FWCore.MessageService.MessageLogger_cfi')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
    )

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        options.inputFiles
        ),
   secondaryFileNames = cms.untracked.vstring(secondaryMap[options.inputFiles[0]])
)

process.options = cms.untracked.PSet()

# Other statements
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
#process.GlobalTag.connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG')
#process.GlobalTag.globaltag = cms.string('POSTLS162_V2::All')

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = 'GR_P_V56'


#########################
from L1Trigger.L1TNtuplizer.caloStage1ParamsModifyParameters_cfi import *
process.load("L1Trigger.L1TNtuplizer.caloStage1ParamsModifyParameters_cfi")
process.caloStage1Params.tauSeedThreshold         = cms.double(options.tauThresh)    #pre-RCT Calibration 7GeV
process.caloStage1Params.tauNeighbourThreshold    = cms.double(options.tauNThresh)   #pre-RCT Calibration 0GeV
process.caloStage1Params.tauMaxPtTauVeto          = cms.double(options.maxPtTauVeto) #pre-RCT Calibration 64GeV
process.caloStage1Params.tauMinPtJetIsolationB    = cms.double(options.tauMinPtIso)  #pre-RCT Calibration 192GeV
process.caloStage1Params.tauMaxJetIsolationB      = cms.double(options.tauMaxJetIso) #pre-RCT Calibration 100GeV
process.caloStage1Params.tauMaxJetIsolationA      = cms.double(options.tauIsoValue)  #pre-RCT Calibration 0.1

# HCAL TP hack
process.load("L1Trigger.L1TCalorimeter.L1TRerunHCALTP_FromRaw_cff")
#from L1Trigger.L1TCalorimeter.L1TRerunHCALTP_FromRaw_cff import *
#process.load("")

### Set RCT EG Activity Threshold and Hadronic Activity Threshold Here
process.load("L1Trigger.L1TCalorimeter.caloStage1RCTLuts_cff")
process.RCTConfigProducers.hActivityCut = options.hActivityCut
process.RCTConfigProducers.eActivityCut = options.eActivityCut

process.RCTConfigProducers.eGammaECalScaleFactors = [
 1.11, 1.11, 1.11, 1.13, 1.14, 1.15, 1.13, 1.14, 1.16, 1.16, 1.17, 1.19, 1.24, 1.27, 1.29, 1.29, 1.3, 1.48, 1.3, 1.41, 1.41, 1.4, 1.32, 1.3, 1.26, 1.2, 1.22, 1.16,#Old SF
1.204772, 1.213636, 1.222593, 1.182629, 1.243846, 1.225251, 1.228466, 1.221463, 1.244637, 1.313051, 1.287068, 1.262398, 1.282544, 1.342669, 1.351468, 1.370895, 1.391770, 1.562276, 1.487895, 1.510230, 1.578938, 1.631488, 1.605999, 1.609515, 1.637187, 1.721263, 1.760116, 1.733094, 
1.204772, 1.213636, 1.222593, 1.182629, 1.243846, 1.225251, 1.228466, 1.221463, 1.244637, 1.313051, 1.287068, 1.262398, 1.282544, 1.342669, 1.351468, 1.370895, 1.391770, 1.562276, 1.487895, 1.510230, 1.578938, 1.631488, 1.605999, 1.609515, 1.637187, 1.721263, 1.760116, 1.733094, 
1.141363, 1.160973, 1.133853, 1.138220, 1.169487, 1.172944, 1.169129, 1.176950, 1.185458, 1.192115, 1.193747, 1.206746, 1.245520, 1.281312, 1.301019, 1.307651, 1.324583, 1.451967, 1.433444, 1.433267, 1.503950, 1.545258, 1.540701, 1.536614, 1.567509, 1.667633, 1.707519, 1.606923, 
1.142051, 1.142141, 1.119592, 1.134651, 1.152122, 1.145785, 1.140578, 1.145707, 1.154906, 1.158494, 1.164353, 1.171921, 1.204233, 1.241946, 1.263247, 1.263594, 1.274716, 1.351273, 1.354642, 1.368800, 1.445195, 1.477991, 1.482562, 1.486204, 1.528721, 1.622263, 1.636796, 1.636796, 
1.126384, 1.120251, 1.107199, 1.114144, 1.125037, 1.125901, 1.121943, 1.124232, 1.135352, 1.144936, 1.147341, 1.156995, 1.186459, 1.213671, 1.233263, 1.238585, 1.244408, 1.289789, 1.295699, 1.337312, 1.409391, 1.432030, 1.442084, 1.443991, 1.483644, 1.565615, 1.589603, 1.589603, 
1.105715, 1.105966, 1.097476, 1.100877, 1.110686, 1.111321, 1.111937, 1.110059, 1.118839, 1.131184, 1.136397, 1.148604, 1.163164, 1.197143, 1.208039, 1.214186, 1.230526, 1.271366, 1.267899, 1.279311, 1.374360, 1.387349, 1.385369, 1.395601, 1.435982, 1.489833, 1.524636, 1.524636, 
1.099813, 1.097799, 1.091391, 1.094092, 1.091036, 1.099597, 1.102687, 1.102992, 1.105222, 1.110909, 1.121844, 1.130550, 1.154720, 1.170157, 1.177153, 1.185432, 1.197469, 1.222308, 1.193889, 1.232942, 1.309696, 1.333690, 1.358762, 1.367090, 1.374255, 1.414572, 1.442653, 1.442653, 
1.089654, 1.084703, 1.081743, 1.081986, 1.085267, 1.091116, 1.086594, 1.091165, 1.096822, 1.098262, 1.104246, 1.112869, 1.118845, 1.145236, 1.166358, 1.160349, 1.173260, 1.187422, 1.183422, 1.182242, 1.262352, 1.298997, 1.274992, 1.299525, 1.246296, 1.310882, 1.310882, 1.310882, 
1.089654, 1.084703, 1.081743, 1.081986, 1.085267, 1.091116, 1.086594, 1.091165, 1.096822, 1.098262, 1.104246, 1.112869, 1.118845, 1.145236, 1.166358, 1.160349, 1.173260, 1.187422, 1.183422, 1.182242, 1.262352, 1.298997, 1.274992, 1.299525, 1.246296, 1.310882, 1.310882, 1.310882, 
]
process.RCTConfigProducers.jetMETHCalScaleFactors = [
 1.11, 1.11, 1.11, 1.13, 1.14, 1.15, 1.13, 1.14, 1.16, 1.16, 1.17, 1.19, 1.24, 1.27, 1.29, 1.29, 1.3, 1.48, 1.3, 1.41, 1.41, 1.4, 1.32, 1.3, 1.26, 1.2, 1.22, 1.16,#Old SF
1.204772, 1.213636, 1.222593, 1.182629, 1.243846, 1.225251, 1.228466, 1.221463, 1.244637, 1.313051, 1.287068, 1.262398, 1.282544, 1.342669, 1.351468, 1.370895, 1.391770, 1.562276, 1.487895, 1.510230, 1.578938, 1.631488, 1.605999, 1.609515, 1.637187, 1.721263, 1.760116, 1.733094, 
1.204772, 1.213636, 1.222593, 1.182629, 1.243846, 1.225251, 1.228466, 1.221463, 1.244637, 1.313051, 1.287068, 1.262398, 1.282544, 1.342669, 1.351468, 1.370895, 1.391770, 1.562276, 1.487895, 1.510230, 1.578938, 1.631488, 1.605999, 1.609515, 1.637187, 1.721263, 1.760116, 1.733094, 
1.141363, 1.160973, 1.133853, 1.138220, 1.169487, 1.172944, 1.169129, 1.176950, 1.185458, 1.192115, 1.193747, 1.206746, 1.245520, 1.281312, 1.301019, 1.307651, 1.324583, 1.451967, 1.433444, 1.433267, 1.503950, 1.545258, 1.540701, 1.536614, 1.567509, 1.667633, 1.707519, 1.606923, 
1.142051, 1.142141, 1.119592, 1.134651, 1.152122, 1.145785, 1.140578, 1.145707, 1.154906, 1.158494, 1.164353, 1.171921, 1.204233, 1.241946, 1.263247, 1.263594, 1.274716, 1.351273, 1.354642, 1.368800, 1.445195, 1.477991, 1.482562, 1.486204, 1.528721, 1.622263, 1.636796, 1.636796, 
1.126384, 1.120251, 1.107199, 1.114144, 1.125037, 1.125901, 1.121943, 1.124232, 1.135352, 1.144936, 1.147341, 1.156995, 1.186459, 1.213671, 1.233263, 1.238585, 1.244408, 1.289789, 1.295699, 1.337312, 1.409391, 1.432030, 1.442084, 1.443991, 1.483644, 1.565615, 1.589603, 1.589603, 
1.105715, 1.105966, 1.097476, 1.100877, 1.110686, 1.111321, 1.111937, 1.110059, 1.118839, 1.131184, 1.136397, 1.148604, 1.163164, 1.197143, 1.208039, 1.214186, 1.230526, 1.271366, 1.267899, 1.279311, 1.374360, 1.387349, 1.385369, 1.395601, 1.435982, 1.489833, 1.524636, 1.524636, 
1.099813, 1.097799, 1.091391, 1.094092, 1.091036, 1.099597, 1.102687, 1.102992, 1.105222, 1.110909, 1.121844, 1.130550, 1.154720, 1.170157, 1.177153, 1.185432, 1.197469, 1.222308, 1.193889, 1.232942, 1.309696, 1.333690, 1.358762, 1.367090, 1.374255, 1.414572, 1.442653, 1.442653, 
1.089654, 1.084703, 1.081743, 1.081986, 1.085267, 1.091116, 1.086594, 1.091165, 1.096822, 1.098262, 1.104246, 1.112869, 1.118845, 1.145236, 1.166358, 1.160349, 1.173260, 1.187422, 1.183422, 1.182242, 1.262352, 1.298997, 1.274992, 1.299525, 1.246296, 1.310882, 1.310882, 1.310882, 
1.089654, 1.084703, 1.081743, 1.081986, 1.085267, 1.091116, 1.086594, 1.091165, 1.096822, 1.098262, 1.104246, 1.112869, 1.118845, 1.145236, 1.166358, 1.160349, 1.173260, 1.187422, 1.183422, 1.182242, 1.262352, 1.298997, 1.274992, 1.299525, 1.246296, 1.310882, 1.310882, 1.310882, 
]

### RCT To Digi Sequence
process.load("Configuration.StandardSequences.RawToDigi_Data_cff")

# RCT
# HCAL input would be from hcalDigis if hack not needed
process.load("L1Trigger.Configuration.SimL1Emulator_cff");
process.simRctDigis.ecalDigis = cms.VInputTag( cms.InputTag( 'ecalDigis:EcalTriggerPrimitives' ) )
process.simRctDigis.hcalDigis = cms.VInputTag( cms.InputTag( 'simHcalTriggerPrimitiveDigis' ) )

### stage 1 
process.load("L1Trigger.L1TCalorimeter.L1TCaloStage1_cff")

### L1Extra
process.load("L1Trigger.Configuration.L1Extra_cff")
process.l1ExtraLayer2 = L1Trigger.Configuration.L1Extra_cff.l1extraParticles.clone()
process.l1ExtraLayer2.isolatedEmSource    = cms.InputTag("simCaloStage1LegacyFormatDigis","isoEm")
process.l1ExtraLayer2.nonIsolatedEmSource = cms.InputTag("simCaloStage1LegacyFormatDigis","nonIsoEm")

process.l1ExtraLayer2.forwardJetSource = cms.InputTag("simCaloStage1LegacyFormatDigis","forJets")
process.l1ExtraLayer2.centralJetSource = cms.InputTag("simCaloStage1LegacyFormatDigis","cenJets")
process.l1ExtraLayer2.tauJetSource     = cms.InputTag("simCaloStage1LegacyFormatDigis","tauJets")
process.l1ExtraLayer2.isoTauJetSource  = cms.InputTag("simCaloStage1LegacyFormatDigis","isoTauJets")

process.l1ExtraLayer2.etTotalSource = cms.InputTag("simCaloStage1LegacyFormatDigis")
process.l1ExtraLayer2.etHadSource   = cms.InputTag("simCaloStage1LegacyFormatDigis")
process.l1ExtraLayer2.etMissSource  = cms.InputTag("simCaloStage1LegacyFormatDigis")
process.l1ExtraLayer2.htMissSource  = cms.InputTag("simCaloStage1LegacyFormatDigis")

process.l1ExtraLayer2.hfRingEtSumsSource    = cms.InputTag("simCaloStage1LegacyFormatDigis")
process.l1ExtraLayer2.hfRingBitCountsSource = cms.InputTag("simCaloStage1LegacyFormatDigis")

## update l1ExtraLayer2 muon tag
process.l1ExtraLayer2.muonSource = cms.InputTag("simGmtDigis")

#########################

# GT
from L1Trigger.Configuration.SimL1Emulator_cff import simGtDigis
process.simGtDigis = simGtDigis.clone()
process.simGtDigis.GmtInputTag = 'simGmtDigis'
process.simGtDigis.GctInputTag = 'caloStage1LegacyFormatDigis'
process.simGtDigis.TechnicalTriggersInputTags = cms.VInputTag( )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('L1Tree.root')
)


process.load("L1Trigger.L1TNtuplizer.l1NtupleProducer_cfi")

process.p1 = cms.Path(
    #process.L1TRerunHCALTP_FromRAW
    process.L1TRerunHCALTP_FromRAW
    #process.hcalDigis
    #simHcalTriggerPrimitiveDigis
    #L1TRerunHCALTP_FromRAW
    +process.ecalDigis
    +process.simRctDigis
    +process.L1TCaloStage1
    +process.simGtDigis
    +process.l1ExtraLayer2
    +process.l1NtupleProducer
#    +process.isolation1
#    +process.isolation2
    )

process.schedule = cms.Schedule(
    process.p1
    )

# Spit out filter efficiency at the end.
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
