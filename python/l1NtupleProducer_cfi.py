import FWCore.ParameterSet.Config as cms


l1NtupleProducer = cms.EDAnalyzer("L1TNtuplizer",
                                  rctSource               = cms.InputTag("simRctDigis"),
                                  gctTauJetsSource        = cms.InputTag("simCaloStage1LegacyFormatDigis","tauJets"),
                                  gctIsoTauJetsSource     = cms.InputTag("simCaloStage1LegacyFormatDigis","isoTauJets"),
                                  l1ExtraTauSource        = cms.InputTag("l1ExtraLayer2","Tau"),
                                  l1ExtraIsoTauSource     = cms.InputTag("l1ExtraLayer2","IsoTau"),
                                  recoTau                 = cms.InputTag("hpsPFTauProducer"),
                                  #remove all possible muons
                                  recoTauDiscriminatorIso = cms.InputTag("hpsPFTauDiscriminationByLooseIsolation"),
                                  recoTauDiscriminatorMu  = cms.InputTag("hpsPFTauDiscriminationByTightMuonRejection3"),
                                  vertices                = cms.InputTag("offlinePrimaryVertices"),
                                  folderName              = cms.untracked.string("firstFolder"),
                                  recoPtCut               = cms.double(4),
                                  pfCands                 = cms.InputTag("particleFlow"),
                                  ecalDigis               = cms.InputTag( 'ecalDigis:EcalTriggerPrimitives' ),
                                  hcalDigis               = cms.InputTag( 'simHcalTriggerPrimitiveDigis' )

#edm::SortedCollection<CaloTower,edm::StrictWeakOrdering<CaloTower> >    "towerMaker"   ""       "RECO"
#hpsPFTauDiscriminationByTightMuonRejection3
#reco::PFTauDiscriminator              "hpsPFTauDiscriminationByLooseIsolation"
)
