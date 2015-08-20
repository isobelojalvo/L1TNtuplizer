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
    input = cms.untracked.int32(10000)
    )

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring("/store/user/alevine/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6_Sept12AtUW_Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/05a81b8d696d27a5c3c2ca036967addd/skim_100_1_35f.root",
"/store/user/alevine/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6_Sept12AtUW_Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/05a81b8d696d27a5c3c2ca036967addd/skim_101_1_Am4.root",
"/store/user/alevine/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6_Sept12AtUW_Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/05a81b8d696d27a5c3c2ca036967addd/skim_102_1_3Us.root",
"/store/user/alevine/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6_Sept12AtUW_Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/05a81b8d696d27a5c3c2ca036967addd/skim_103_1_eYo.root",
"/store/user/alevine/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6_Sept12AtUW_Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/05a81b8d696d27a5c3c2ca036967addd/skim_104_1_tlE.root",
"/store/user/alevine/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6_Sept12AtUW_Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/05a81b8d696d27a5c3c2ca036967addd/skim_105_1_pL0.root",
"/store/user/alevine/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6_Sept12AtUW_Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/05a81b8d696d27a5c3c2ca036967addd/skim_106_1_sRJ.root",
"/store/user/alevine/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6_Sept12AtUW_Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/05a81b8d696d27a5c3c2ca036967addd/skim_107_1_mEU.root",
"/store/user/alevine/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6_Sept12AtUW_Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/05a81b8d696d27a5c3c2ca036967addd/skim_108_1_0M9.root",
"/store/user/alevine/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6_Sept12AtUW_Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/05a81b8d696d27a5c3c2ca036967addd/skim_109_1_sig.root",
"/store/user/alevine/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6/GluGluToHToTauTau_M-125_13TeV-powheg-pythia6_Sept12AtUW_Fall13dr-tsg_PU40bx25_POSTLS162_V2-v1/05a81b8d696d27a5c3c2ca036967addd/skim_10_1_Pel.root"
                                      )
    )

process.options = cms.untracked.PSet()

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag.connect = cms.string('frontier://FrontierProd/CMS_COND_31X_GLOBALTAG')
process.GlobalTag.globaltag = cms.string('POSTLS162_V2::All')

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

### Set RCT EG Activity Threshold and Hadronic Activity Threshold Here
process.load("L1Trigger.L1TCalorimeter.caloStage1RCTLuts_cff")
process.RCTConfigProducers.hActivityCut = options.hActivityCut
process.RCTConfigProducers.eActivityCut = options.eActivityCut

##### ECAL HCAL Calibration Factors
process.RCTConfigProducers.eGammaECalScaleFactors = [
1.11, 1.11, 1.11, 1.13, 1.14, 1.15, 1.13, 1.14, 1.16, 1.16, 1.17, 1.19, 1.24, 1.27, 1.29, 1.29, 1.3, 1.48, 1.3, 1.41, 1.41, 1.4, 1.32, 1.3, 1.26, 1.2, 1.22, 1.16,
1.1847, 1.16759, 1.17779, 1.19955, 1.21125, 1.214, 1.21503, 1.22515, 1.24151, 1.27836, 1.30292, 1.33526, 1.42338, 1.4931, 1.49597, 1.50405, 1.52785, 1.81552, 1.59856, 1.75692, 1.76496, 1.77562, 1.69527, 1.66827, 1.61861, 1.56645, 1, 1,
1.1351, 1.12589, 1.12834, 1.13725, 1.14408, 1.1494, 1.14296, 1.14852, 1.1578, 1.17634, 1.18038, 1.19386, 1.23758, 1.27605, 1.27818, 1.28195, 1.34881, 1.71053, 1.37338, 1.52571, 1.54801, 1.53316, 1.4397, 1.40497, 1.37743, 1.33914, 1, 1,
1.18043, 1.17823, 1.1751, 1.17608, 1.19152, 1.196, 1.20125, 1.2068, 1.22584, 1.22476, 1.22395, 1.22302, 1.25137, 1.28097, 1.29871, 1.2862, 1.33489, 1.60937, 1.28365, 1.41367, 1.42521, 1.42041, 1.36784, 1.34922, 1.32754, 1.29825, 1, 1,
1.11664, 1.11852, 1.11861, 1.12367, 1.12405, 1.14814, 1.14304, 1.15337, 1.16607, 1.18698, 1.17048, 1.17463, 1.2185, 1.23842, 1.23214, 1.24744, 1.30047, 1.47152, 1.22868, 1.33121, 1.34841, 1.35178, 1.30048, 1.28537, 1.27012, 1.24159, 1,1,
1.08422, 1.08146, 1.08706, 1.08906, 1.08636, 1.10092, 1.10363, 1.11102, 1.1186, 1.13301, 1.12369, 1.14377, 1.16477, 1.17801, 1.18782, 1.17168, 1.24593, 1.36835, 1.20252, 1.28349, 1.29828, 1.30328, 1.26848, 1.25817, 1.2464, 1.22259, 1,1,
1.07444, 1.06774, 1.06883, 1.0707, 1.07881, 1.08859, 1.08285, 1.08747, 1.09736, 1.10678, 1.10008, 1.10717, 1.12858, 1.15383, 1.15826, 1.14855, 1.19911, 1.32567, 1.17553, 1.25976, 1.27926, 1.28459, 1.24524, 1.23706, 1.22597, 1.20006, 1,1,
1.06224, 1.05968, 1.05767, 1.06254, 1.06729, 1.0691, 1.07125, 1.07312, 1.08124, 1.08966, 1.08695, 1.08826, 1.10611, 1.13115, 1.12641, 1.13093, 1.17074, 1.28958, 1.16217, 1.22844, 1.24812, 1.25352, 1.22065, 1.21287, 1.20544, 1.18344, 1,1,
1.03589, 1.03224, 1.03229, 1.03623, 1.03979, 1.04403, 1.04574, 1.049, 1.04821, 1.06183, 1.0588, 1.06655, 1.08582, 1.10289, 1.10052, 1.10506, 1.143, 1.27373, 1.1459, 1.2156, 1.23455, 1.23968, 1.20753, 1.20127, 1.19629, 1.16809, 1, 1,
1.03456, 1.02955, 1.03079, 1.03509, 1.03949, 1.0437, 1.04236, 1.04486, 1.0517, 1.05864, 1.05516, 1.06167, 1.07738, 1.0985, 1.09317, 1.09559, 1.13557, 1.26076, 1.14118, 1.20545, 1.22137, 1.22802, 1.19936, 1.19676, 1.19088, 1.16709, 1, 1
]
process.RCTConfigProducers.jetMETHCalScaleFactors = [
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1.511112, 1.519900, 1.499483, 1.488560, 1.528111, 1.475114, 1.476616, 1.514163, 1.515306, 1.542464, 1.511663, 1.593745, 1.493667, 1.485315, 1.419925, 1.349169, 1.312518, 1.423302, 1.478461, 1.525868, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1.383350, 1.365700, 1.368470, 1.354610, 1.348480, 1.329720, 1.272250, 1.301710, 1.322210, 1.360860, 1.333850, 1.392200, 1.403060, 1.394870, 1.322050, 1.244570, 1.206910, 1.321870, 1.344160, 1.403270, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1.245690, 1.238320, 1.245420, 1.234830, 1.243730, 1.249790, 1.179450, 1.213620, 1.219030, 1.252130, 1.209560, 1.250710, 1.280490, 1.262800, 1.254060, 1.186810, 1.127830, 1.260000, 1.275140, 1.305850, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1.189940, 1.189120, 1.177120, 1.179690, 1.185510, 1.150590, 1.151830, 1.167860, 1.154310, 1.163190, 1.161700, 1.136100, 1.161870, 1.195050, 1.153910, 1.117900, 1.106750, 1.208120, 1.160020, 1.232800, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1.122540, 1.129520, 1.125080, 1.115150, 1.118250, 1.096190, 1.108170, 1.087490, 1.109750, 1.099780, 1.081000, 1.050610, 1.078270, 1.079460, 1.047740, 1.041400, 1.041750, 1.116880, 1.097730, 1.125780, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1.110470, 1.117340, 1.115980, 1.088490, 1.088260, 1.078230, 1.062720, 1.054690, 1.053270, 1.086640, 1.050620, 1.038470, 1.046440, 1.059130, 1.012240, 1.039030, 1.036040, 1.088460, 1.078880, 1.090600, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1.115970, 1.111010, 1.113170, 1.079390, 1.076850, 1.063730, 1.039300, 1.049910, 1.040100, 1.025820, 1.015830, 1.015850, 1.010810, 1.014210, 0.980321, 1.023580, 1.045990, 1.073220, 1.057750, 1.059850, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1.061180, 1.059770, 1.071210, 1.064420, 1.065340, 1.043070, 1.041400, 1.022680, 1.017410, 1.017690, 1.005610, 1.006360, 0.999420, 0.990866, 0.986723, 0.989036, 0.995116, 1.045620, 1.024330, 1.040660, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1.083150, 1.067090, 1.083180, 1.061010, 1.075640, 1.051640, 1.038760, 1.042670, 1.010910, 1.011580, 1.006560, 0.984468, 0.986642, 0.985799, 0.968133, 1.000290, 1.011210, 1.046690, 1.016670, 1.020470, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
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
    process.L1TRerunHCALTP_FromRAW
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
