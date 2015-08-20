import FWCore.ParameterSet.Config as cms
import os

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('analysis')
options.outputFile = "L1TreeRecoDB.root"
options.register ('eActivityCut',   4, VarParsing.multiplicity.singleton, VarParsing.varType.int,
                  "Tau Veto HCAL Activity Threshold")
options.register ('hActivityCut',   4, VarParsing.multiplicity.singleton, VarParsing.varType.int,
                  "Tau Veto ECAL Activity Threshold")
options.register ('tauThresh',      7, VarParsing.multiplicity.singleton, VarParsing.varType.int,
                  "Tau Seed Threshold")
options.register ('tauNThresh',     0, VarParsing.multiplicity.singleton, VarParsing.varType.int,
                  "Tau Neighbor Seed Threshold")
options.register ('tauMaxPtTauVeto',  64, VarParsing.multiplicity.singleton, VarParsing.varType.int,
                  "Tau max Pt Tau Veto")
options.register ('tauIsoLUTFile',  "L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.15Iso.txt", VarParsing.multiplicity.singleton, VarParsing.varType.string,
                  "Tau Isolation Cut")
options.register ('tauCalibLUTFile', "L1Trigger/L1TCalorimeter/data/tauCalibrationLUT_stage1.txt", VarParsing.multiplicity.singleton, VarParsing.varType.string,
                  "Tau Calibration LUT")
#options.register('inputFiles', "", VarParsing.multiplicity.singleton, VarParsing.varType.string,
#                  "files to run over")
#options.register('outputFile', "L1TreeReco", VarParsing.multiplicity.singleton, VarParsing.varType.string,
#                  "file to output")


options.parseArguments()
print '========Tau Parameter Configuration======='
print 'eActivityCut =   ',options.eActivityCut,' GeV'
print 'hActivityCut =   ',options.hActivityCut,' GeV'
print 'tauThresh    =   ',options.tauThresh,' GeV'
print 'tauNThresh   =   ',options.tauNThresh,' GeV'
print 'tauMaxPtTauVeto =  ',options.tauMaxPtTauVeto,' GeV'
print 'tauIsoLUTFile = ',options.tauIsoLUTFile
process = cms.Process('EmulatorEffiNtupilizer')

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.load('Configuration.EventContent.EventContent_cff')

process.load('Configuration.Geometry.GeometryIdeal_cff')
# Make the framework shut up.
process.load("FWCore.MessageLogger.MessageLogger_cfi")
#process.MessageLogger.cerr.FwkReport.reportEvery = 100

# Spit out filter efficiency at the end.
#process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))

#Max Events
process.maxEvents = cms.untracked.PSet(
	input = cms.untracked.int32(-1)
	#input = cms.untracked.int32(100)
)

from L1Trigger.L1TNtuplizer.outputSecondaryFileMapDataRECO_cfi import *
#from L1Trigger.L1NTuplizer.outputSecondaryFileMapDataRECO_cfi import *

print options.inputFiles[0]

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        options.inputFiles
        ),
   #fileNames = cms.untracked.vstring(options.inputFiles),
   secondaryFileNames = cms.untracked.vstring(secondaryMap[options.inputFiles[0]])
   #fileNames = cms.untracked.vstring(options.inputFiles),
   #secondaryFileNames = cms.untracked.vstring(secondaryMap[options.inputFiles[0]])
)

#Output
process.TFileService = cms.Service(
	"TFileService",
	fileName = cms.string(options.outputFile)
)

#from Configuration.AlCa.GlobalTag import GlobalTag
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag = 'GR_P_V56'

import FWCore.PythonUtilities.LumiList as LumiList
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/DCSOnly/json_DCSONLY_Run2015B.txt').getVLuminosityBlockRange()
process.source.lumisToProcess = LumiList.LumiList(filename = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON_v2.txt').getVLuminosityBlockRange()



#########################
from L1Trigger.L1TCalorimeter.caloStage1Params_cfi import *
process.load("L1Trigger.L1TCalorimeter.caloStage1Params_cfi")
process.caloStage1Params.tauSeedThreshold         = cms.double(options.tauThresh)    #pre-RCT Calibration 7GeV
process.caloStage1Params.tauNeighbourThreshold    = cms.double(options.tauNThresh)   #pre-RCT Calibration 0GeV
process.caloStage1Params.tauMaxPtTauVeto          = cms.double(options.tauMaxPtTauVeto) #pre-RCT Calibration 64GeV
process.caloStage1Params.tauIsoLUTFile            = cms.FileInPath(options.tauIsoLUTFile)  #pre-RCT Calibration 0.1
process.caloStage1Params.tauCalibrationLUTFile    = cms.FileInPath(options.tauCalibLUTFile)  #pre-RCT Calibration 0.1

#process.load('L1Trigger.L1TCalorimeter.L1TCaloStage1_PPFromRaw_cff')
# HCAL TP hack
process.load("L1Trigger.L1TCalorimeter.L1TRerunHCALTP_FromRaw_cff")

### Set RCT EG Activity Threshold and Hadronic Activity Threshold Here
#process.load("L1Trigger.L1TCalorimeter.caloStage1RCTLuts_cff")
#process.load("L1Trigger.L1TCalorimeter.caloStage1RCTLuts_NewRCTCalib_cff")
process.load("L1Trigger.L1TCalorimeter.caloStage1RCTLuts_NewRCTCalibWithECALTransparency_cff")
process.RCTConfigProducers.hActivityCut = options.hActivityCut
process.RCTConfigProducers.eActivityCut = options.eActivityCut

### RCT To Digi Sequence
process.load("Configuration.StandardSequences.RawToDigi_Data_cff")

# RCT
# HCAL input would be from hcalDigis if hack not needed
process.load("L1Trigger.Configuration.SimL1Emulator_cff");
process.simRctDigis.ecalDigis = cms.VInputTag( cms.InputTag( 'ecalDigis:EcalTriggerPrimitives' ) )
process.simRctDigis.hcalDigis = cms.VInputTag( cms.InputTag( 'simHcalTriggerPrimitiveDigis' ) )

from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup
process.newRCTConfig = cms.ESSource("PoolDBESSource",
    CondDBSetup,
    connect = cms.string('frontier://FrontierPrep/CMS_COND_L1T'),
    DumpStat=cms.untracked.bool(True),
    toGet = cms.VPSet(
        cms.PSet(
            record = cms.string('L1RCTParametersRcd'),
            tag = cms.string('L1RCTParametersRcd_L1TDevelCollisions_ExtendedScaleFactorsV1')
        ) 
    ) 
)
process.prefer("newRCTConfig")


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
                     # GT
from L1Trigger.Configuration.SimL1Emulator_cff import simGtDigis
process.simGtDigis = simGtDigis.clone()
process.simGtDigis.GmtInputTag = 'simGmtDigis'
process.simGtDigis.GctInputTag = 'caloStage1LegacyFormatDigis'
process.simGtDigis.TechnicalTriggersInputTags = cms.VInputTag( )




#reco_object_step = process.recoObjects
#process.p1 = cms.Path(
#        process.L1TRerunHCALTP_FromRAW
#        +process.ecalDigis
#        +process.simRctDigis
#        +process.L1TCaloStage1
#        +process.simGtDigis
#        +process.l1ExtraLayer2
#)

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


#process.p2 = cms.Path(
#    process.l1NtupleProducer
#)

#process.schedule = cms.Schedule(#
#	process.p1,
#	process.p2
#)
