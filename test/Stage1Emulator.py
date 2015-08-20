import FWCore.ParameterSet.Config as cms

process = cms.Process('L1TEMULATION')

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.Geometry.GeometryIdeal_cff')
process.load('Configuration/StandardSequences/SimL1Emulator_cff')
process.load("Configuration.StandardSequences.RawToDigi_Data_cff")
process.load('Configuration/StandardSequences/EndOfProcess_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('Configuration/EventContent/EventContent_cff')
process.load('Configuration.StandardSequences.ReconstructionCosmics_cff')

# Select the Message Logger output you would like to see:
process.load('FWCore.MessageService.MessageLogger_cfi')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
    )

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring("/store/user/alevine/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6_Sept12AtUW_Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/05a81b8d696d27a5c3c2ca036967addd/skim_100_1_35f.root")
    )


#process.output = cms.OutputModule(
#    "PoolOutputModule",
#    splitLevel = cms.untracked.int32(0),
#    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
#    outputCommands = cms.untracked.vstring('drop *',
#                                           'keep *_*_*_L1TEMULATION'),
#    fileName = cms.untracked.string('SimL1Emulator_Stage1_PP.root'),
#    dataset = cms.untracked.PSet(
#        filterName = cms.untracked.string(''),
#        dataTier = cms.untracked.string('')
#    )
#                                          )
process.options = cms.untracked.PSet()

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag.connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG')
process.GlobalTag.globaltag = cms.string('POSTLS162_V2::All')


from L1Trigger.L1TNtuplizer.caloStage1ParamsModifyParameters_cff import *

process.load('L1Trigger.L1TNtuplizer.L1TCaloStage1_PPFromRawModifyParameters_cff')

# analysis
process.load("L1Trigger.Configuration.L1Extra_cff")

# GT
from L1Trigger.Configuration.SimL1Emulator_cff import simGtDigis
process.simGtDigis = simGtDigis.clone()
process.simGtDigis.GmtInputTag = 'simGmtDigis'
process.simGtDigis.GctInputTag = 'caloStage1LegacyFormatDigis'
process.simGtDigis.TechnicalTriggersInputTags = cms.VInputTag( )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('L1Tree_2.root'),
                                   closeFileFast = cms.untracked.bool(True)
)

# Ntuplizer
process.load("L1Trigger/L1TNtuplizer/l1NtupleProducer_cfi")

process.p1 = cms.Path(
    process.L1TCaloStage1_PPFromRaw
    +process.gctDigis
    +process.dttfDigis
    +process.csctfDigis
    +process.simGtDigis
    +process.l1ExtraLayer2
    +process.l1NtupleProducer
    +process.l1extraParticles
    )

#process.output_step = cms.EndPath(process.output)

process.schedule = cms.Schedule(
    process.p1#, process.output_step
    )

# Spit out filter efficiency at the end.
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
