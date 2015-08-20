/*
 * \file L1TNtuplizer.cc
 *
 * \author I. Ojalvo
 *
 */

#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "L1Trigger/L1TNtuplizer/interface/L1TNtuplizer.h"
#include "DataFormats/Provenance/interface/EventAuxiliary.h"
#include "DataFormats/L1Trigger/interface/Tau.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/TauReco/interface/PFTau.h"
#include "DataFormats/Common/interface/RefToPtr.h"

#include "DataFormats/Math/interface/deltaR.h"

using namespace edm;
using std::cout;
using std::endl;
using std::vector;

L1TNtuplizer::L1TNtuplizer( const ParameterSet & cfg ) :
  rctSource_(cfg.getParameter<edm::InputTag>("rctSource")),
  pfCandsToken_(consumes<reco::PFCandidateCollection>(cfg.getParameter<edm::InputTag>("pfCands")))
  {

  l1ExtraTauSource_    = cfg.getParameter<edm::InputTag>("l1ExtraTauSource");
  l1ExtraIsoTauSource_ = cfg.getParameter<edm::InputTag>("l1ExtraIsoTauSource");
  gctTauJetsSource_    = cfg.getParameter<edm::InputTag>("gctTauJetsSource");
  gctIsoTauJetsSource_ = cfg.getParameter<edm::InputTag>("gctIsoTauJetsSource");
  tauSrc_              = cfg.getParameter<edm::InputTag>("recoTau");
  discriminatorIso_    = cfg.getParameter<edm::InputTag>("recoTauDiscriminatorIso");
  discriminatorMu_     = cfg.getParameter<edm::InputTag>("recoTauDiscriminatorMu");
  vtxLabel_            = cfg.getParameter<edm::InputTag>("vertices");
  folderName_          = cfg.getUntrackedParameter<std::string>("folderName");
  recoPt_              = cfg.getParameter<double>("recoPtCut");
  ecalSrc_             = cfg.getParameter<edm::InputTag>("ecalDigis");
  hcalSrc_             = cfg.getParameter<edm::InputTag>("hcalDigis");
  //caloTowerProducer_   = cfg.getParameter<edm::InputTag>("caloTowerProducer");

  //cout<<"folderName "<<folderNameSrc_<<endl;
  //TFileDirectory subDir = tfs_->mkdir( folderName_ );
  //TFileDirectory subSubDir = subDir.mkdir( folderName_ );

  efficiencyTree = tfs_->make<TTree>("EfficiencyTree", "Efficiency Tree");
  efficiencyTree->Branch("run",    &run,     "run/I");
  efficiencyTree->Branch("lumi",   &lumi,    "lumi/I");
  efficiencyTree->Branch("event",  &event,   "event/I");
  efficiencyTree->Branch("nvtx",          &nvtx,         "nvtx/I");

  efficiencyTree->Branch("recoPt",    &recoPt,   "recoPt/D");

  efficiencyTree->Branch("decayMode", &decayMode,   "decayMode/I");

  efficiencyTree->Branch("tauEtaEcalEnt", &tauEtaEcalEnt,"tauEtaEcalEnt/D");
  efficiencyTree->Branch("tauPhiEcalEnt", &tauPhiEcalEnt,"tauPhiEcalEnt/D");
  efficiencyTree->Branch("rawEcal",       &rawEcal,      "rawEcal/D");
  efficiencyTree->Branch("rawHcal",       &rawHcal,      "rawHcal/D");
  efficiencyTree->Branch("ecal",          &ecal,         "ecal/D");
  efficiencyTree->Branch("hcal",          &hcal,         "hcal/D");
  efficiencyTree->Branch("jetEt",         &jetEt,        "jetEt/D");
  efficiencyTree->Branch("jetEta",        &jetEta,       "jetEta/D");
  efficiencyTree->Branch("jetPhi",        &jetPhi,       "jetPhi/D");
  efficiencyTree->Branch("pfCandsEt",     &pfCandsEt,    "pfCandsEt/D");
  efficiencyTree->Branch("signalCandsEt", &signalCandsEt,"signalCandsEt/D");
  efficiencyTree->Branch("isoCandsEt",    &isoCandsEt,   "isoCandsEt/D");

  efficiencyTree->Branch("max3ProngDeltaR",     &max3ProngDeltaR,    "max3ProngDeltaR/D");
  efficiencyTree->Branch("minProngPt",          &minProngPt,         "minProngPt/D");
  efficiencyTree->Branch("midProngPt",          &midProngPt,         "midProngPt/D");
  efficiencyTree->Branch("maxProngPt",          &maxProngPt,         "maxProngPt/D");
  efficiencyTree->Branch("n3ProngCands",        &n3ProngCands,       "maxProngPt/I");

  efficiencyTree->Branch("hcal",          &hcal,         "hcal/D");

  efficiencyTree->Branch("ecalTPG2x2",    &TPGE2x2,      "ecalTPG2x2/D");
  efficiencyTree->Branch("hcalTPG2x2",    &TPGH2x2,      "hcalTPG2x2/D");
  efficiencyTree->Branch("TPG2x2",        &TPG2x2,       "TPG2x2/D");

  efficiencyTree->Branch("ecalTPG5x5",    &TPGE5x5,      "ecalTPG5x5/D");
  efficiencyTree->Branch("hcalTPG5x5",    &TPGH5x5,      "hcalTPG5x5/D");
  efficiencyTree->Branch("TPG5x5",        &TPG5x5,       "TPG5x5/D");

  efficiencyTree->Branch("ecalTPG6x6",    &TPGE6x6,      "ecalTPG6x6/D");
  efficiencyTree->Branch("hcalTPG6x6",    &TPGH6x6,      "hcalTPG6x6/D");
  efficiencyTree->Branch("TPG6x6",        &TPG6x6,       "TPG6x6/D");

  efficiencyTree->Branch("ecalTPG7x7",    &TPGE7x7,      "ecalTPG7x7/D");
  efficiencyTree->Branch("hcalTPG7x7",    &TPGH7x7,      "hcalTPG7x7/D");
  efficiencyTree->Branch("TPG7x7",        &TPG7x7,       "TPG7x7/D");


  efficiencyTree->Branch("isoTauPt",      &isoTauPt, "isoTauPt/D");
  efficiencyTree->Branch("rlxTauPt",      &rlxTauPt, "rlxTauPt/D");

  efficiencyTree->Branch("recoEta",       &recoEta,   "recoEta/D");
  efficiencyTree->Branch("isoTauEta",     &isoTauEta, "isoTauEta/D");
  efficiencyTree->Branch("rlxTauEta",     &rlxTauEta, "rlxTauEta/D");

  efficiencyTree->Branch("recoPhi",       &recoPhi,   "recoPhi/D");
  efficiencyTree->Branch("isoTauPhi",     &isoTauPhi, "isoTauPhi/D");
  efficiencyTree->Branch("rlxTauPhi",     &rlxTauPhi, "rlxTauPhi/D");

  efficiencyTree->Branch("l1IsoMatched",  &l1IsoMatched, "l1IsoMatched/I");
  efficiencyTree->Branch("l1RlxMatched",  &l1RlxMatched, "l1RlxMatched/I");

  isoTau_pt   = tfs_->make<TH1F>( "isoTau_pt"  , "p_{T}", 100,  0., 100. );
  tau_pt      = tfs_->make<TH1F>( "tau_pt"  , "p_{t}", 100,  0., 100. );
  recoTau_pt  = tfs_->make<TH1F>( "recoTau_pt"  , "p_{t}", 100,  0., 100. );


}

void L1TNtuplizer::beginJob( const EventSetup & es) {
}

//unsigned int const L1TNtuplizer::N_TOWER_PHI = 72;
//unsigned int const L1TNtuplizer::N_TOWER_ETA = 56;

void L1TNtuplizer::analyze( const Event& evt, const EventSetup& es )
 {


  run = evt.id().run();
  lumi = evt.id().luminosityBlock();
  event = evt.id().event();

  edm::Handle<reco::VertexCollection> vertices;
  if(evt.getByLabel(vtxLabel_, vertices)){
    const reco::Vertex &PV = vertices->front();
    nvtx = vertices->size();
  }

  Handle<L1CaloRegionCollection> regions;

  edm::Handle<reco::PFTauDiscriminator> discriminatorIso;
  edm::Handle<reco::PFTauDiscriminator> discriminatorMu;

  edm::Handle < L1GctJetCandCollection > l1IsoTauJets;
  edm::Handle < L1GctJetCandCollection > l1TauJets;

  edm::Handle < vector<l1extra::L1JetParticle> > l1ExtraTaus;
  edm::Handle < vector<l1extra::L1JetParticle> > l1ExtraIsoTaus;

  std::vector<reco::PFTauRef> goodTausRef;
  std::vector<reco::PFTau> goodTaus;
  edm::Handle<reco::PFCandidateCollection> pfCands;
  edm::Handle<EcalTrigPrimDigiCollection> ecalTPGs;
  edm::Handle<HcalTrigPrimDigiCollection> hcalTPGs;

  //edm::SortedCollection<CaloTower,edm::StrictWeakOrdering<CaloTower> > caloTowers;
  //edm::Handle<CaloTowerCollection> towerHandle;
  //if(!evt.getByLabel(towerProducer_, towerHandle))
  //std::cout<<"ERROR GETTING THE HCAL TPGS"<<std::endl;
  //const CaloTowerCollection* caloTowers = towerHandle.product();
  //if(!evt.getByLabel(caloTower_, caloTowers))


  if(!evt.getByLabel(ecalSrc_, ecalTPGs))
    std::cout<<"ERROR GETTING THE ECAL TPGS"<<std::endl;
  if(!evt.getByLabel(hcalSrc_, hcalTPGs))
    std::cout<<"ERROR GETTING THE HCAL TPGS"<<std::endl;

  ESHandle<L1CaloHcalScale> hcalScale;
  es.get<L1CaloHcalScaleRcd>().get(hcalScale);

  //get pfcandidate particles
  if(!evt.getByToken(pfCandsToken_, pfCands)){
    std::cout<<"Error Getting PFCandidates"<<std::endl;
  }

  //Make Rates
  // loop over taus
  Handle<reco::PFTauCollection> taus;
  if(evt.getByLabel(tauSrc_, taus)){//Begin Getting Reco Taus
    for ( unsigned iTau = 0; iTau < taus->size(); ++iTau ) {
      reco::PFTauRef tauCandidate(taus, iTau);
      reco::PFTau tau = taus->at(iTau);
      //std::cout<<"good tau pt "<< tauCandidate->pt()<< std::endl;
      if(evt.getByLabel(discriminatorMu_, discriminatorMu))
	if(evt.getByLabel(discriminatorIso_, discriminatorIso)){
	  //std::cout<<"Tau Candidate Discriminator value "<< (*discriminator)[tauCandidate] << " decay mode "<< tau.decayMode()<<std::endl;
	  if( (*discriminatorIso)[tauCandidate] > 0.5 && tau.decayMode()>-1 && (*discriminatorMu)[tauCandidate] > 0.5 ){
	    recoTau_pt->Fill( tauCandidate->pt() );
	    if(tauCandidate->pt() > recoPt_ ) //get rid of the garbage
	      goodTaus.push_back(tau);
	}
      }
    }
  }//End Getting Reco Taus

  //Begin Making Rate Plots
  if(evt.getByLabel(l1ExtraTauSource_, l1ExtraTaus)){
    for( vector<l1extra::L1JetParticle>::const_iterator rlxTau = l1ExtraTaus->begin(); rlxTau != l1ExtraTaus->end(); rlxTau++ ) {
	tau_pt->Fill( rlxTau->pt() );
    }
  }

  if(evt.getByLabel(l1ExtraIsoTauSource_ , l1ExtraIsoTaus)){
    for( vector<l1extra::L1JetParticle>::const_iterator isoTau = l1ExtraIsoTaus->begin();  isoTau != l1ExtraIsoTaus->end();  ++isoTau ) {
	isoTau_pt->Fill( isoTau->pt() );
    }
  }
  //End Making Rate Plots

  bool testMode = false;


  //If there isn't at least 1 good reco tau don't bother doing all the work
  if(goodTaus.size()>0){
    double deltaR_ = 0.5;
    
    ////Make TPG Maps
    //ecal
    //vector<vector<double> > eTowerETMap(75, vector<double>(65));
    double eTowerETMap[73][57]={{0}};
    //hcal
    //vector<vector<double> > hTowerETMap(75, vector<double>(65));
    double hTowerETMap[73][57]={{0}};

    initializeECALTPGMap( ecalTPGs, eTowerETMap, testMode );
    initializeHCALTPGMap( hcalTPGs, hcalScale, hTowerETMap, testMode);
    
    ////Make efficiencies
    for(unsigned int i = 0; i < goodTaus.size(); i++){
      
      reco::PFTau recoTau = goodTaus.at(i);
      
      tauEtaEcalEnt =-999, tauPhiEcalEnt =-999;
    decayMode = -999, jetEt = -999, jetEta = -999, jetPhi = -999, rawEcal = 0, rawHcal = 0,  ecal = 0, hcal = 0;
    TPG2x2 = 0, TPGH2x2 = 0, TPGE2x2 = 0;
    TPG5x5 = 0, TPGH5x5 = 0, TPGE5x5 = 0;
    TPG6x6 = 0, TPGH6x6 = 0, TPGE6x6 = 0;
    TPG7x7 = 0, TPGH7x7 = 0, TPGE7x7 = 0;

    ////Fill Reco Objects
    recoPt  = recoTau.pt();
    recoEta = recoTau.eta();
    recoPhi = recoTau.phi();

    decayMode = recoTau.decayMode();
    if(decayMode==10){
      getThreeProngInfo(recoTau, max3ProngDeltaR, minProngPt, midProngPt, maxProngPt, n3ProngCands);
    }

    getRawEcalHcalEnergy(recoTau.leadPFChargedHadrCand(), rawEcal, rawHcal, ecal, hcal);

    if(recoTau.leadPFChargedHadrCand().isNonnull()){
      tauEtaEcalEnt = recoTau.leadPFChargedHadrCand()->positionAtECALEntrance().eta();
      tauPhiEcalEnt = recoTau.leadPFChargedHadrCand()->positionAtECALEntrance().phi();
    }

    signalCandsEt = getPFCandsEt(recoTau.signalPFCands());
    //Cone of 0.4?
    isoCandsEt    = getPFCandsEt(recoTau.isolationPFCands());
    //Cone of 0.2
    pfCandsEt     = getPFCandsEtEtaPhi(pfCands, recoTau, 0.5);
    //Jet Seed pt, eta, phi
    jetEt  = recoTau.jetRef()->pt();
    jetEta = recoTau.jetRef()->eta();
    jetPhi = recoTau.jetRef()->phi();
    ////Finished Filling Reco Objects

    //Fill TPG Objects
    //   Use the ECAL Entrance Info for Eta Phi
    if(testMode && i == 0 ){
      recoPhi = 2.92;
      recoEta = 0.871;
      recoPt  = 20;
      std::cout<<"Running Test Mode"<<std::endl;
    }

    int tauTpgPhi = convertGenPhi(recoPhi);//convertGenPhi(recoPhi);//
    int tauTpgEta = convertGenEta(recoEta);//convertGenEta(recoEta);//
    
    if(tauTpgPhi>0 && tauTpgEta >0){
      TPG2x2 = get2x2TPGs(tauTpgEta, tauTpgPhi, eTowerETMap, hTowerETMap, TPGE2x2, TPGH2x2);
      TPG5x5 = get5x5TPGs(tauTpgEta, tauTpgPhi, eTowerETMap, hTowerETMap, TPGE5x5, TPGH5x5);
      TPG6x6 = get6x6TPGs(tauTpgEta, tauTpgPhi, eTowerETMap, hTowerETMap, TPGE6x6, TPGH6x6);
      TPG7x7 = get7x7TPGs(tauTpgEta, tauTpgPhi, eTowerETMap, hTowerETMap, TPGE7x7, TPGH7x7);
    }
    else
      std::cout<<"ERROR tauTPGPHI: "<<tauTpgPhi<<" tauTPGETA: "<<tauTpgEta<<std::endl;
    
    //std::cout<< "Using recp phi eta: tauRecoEta " << recoEta <<" recoPhi " << recoPhi << "reco Pt "<< recoPt << " tauTPGEta "<< tauTpgEta << " tauTpgPhi "<< tauTpgPhi<< " TPGE5x5 " << TPGE5x5 << " TPGH5x5  "<< TPGH5x5 << " TPG5x5 "<< TPG5x5 << " ecal "<< ecal << " hcal "<< hcal<<std::endl;

    //Fill L1 Objects
    l1IsoMatched = -1; l1RlxMatched = -1;
    isoTauPt = 0; isoTauEta = -99; isoTauPhi = -99; 
    rlxTauPt = 0; rlxTauEta = -99; rlxTauPhi = -99;

    if(evt.getByLabel(l1ExtraIsoTauSource_ , l1ExtraIsoTaus)){
      for( vector<l1extra::L1JetParticle>::const_iterator isoTau = l1ExtraIsoTaus->begin();  isoTau != l1ExtraIsoTaus->end();  ++isoTau ) {
	double dR = deltaR( recoTau.p4(), isoTau->p4());
	//std::cout<<"Pt "<< isoTau->pt() << " Eta "<< isoTau->eta()<< " Phi "<< isoTau->phi()<< " DR "<< dR << endl;
	if( dR < deltaR_){

	  //isoTauPt  = isoTau->gctJetCandRef()->rank();//isoTau->pt();
	  isoTauPt  = isoTau->pt();
	  isoTauEta = isoTau->eta();
	  isoTauPhi = isoTau->phi();
	  l1IsoMatched = 1;
	  break;
	}
      }
    }
    else
      std::cout<<"ERROR GETTING L1EXTRA ISO TAUS"<<std::endl;

    if(evt.getByLabel(l1ExtraTauSource_, l1ExtraTaus)){
      for( vector<l1extra::L1JetParticle>::const_iterator rlxTau = l1ExtraTaus->begin(); rlxTau != l1ExtraTaus->end(); rlxTau++ ) {
	double dR = deltaR( recoTau.p4(), rlxTau->p4());
	//std::cout<<"Pt "<< rlxTau->pt() << " Eta "<< rlxTau->eta()<< " Phi "<< rlxTau->phi()<< " DR "<< dR << endl;
	if(dR < deltaR_){
	  //isoTauPt  = rlxTau->gctJetCandRef()->rank();//isoTau->pt();
	  rlxTauPt  = rlxTau->pt();
	  rlxTauEta = rlxTau->eta();
	  rlxTauPhi = rlxTau->phi();
	  l1RlxMatched = 1;
	  break;
	}
      }
    }
    else
      std::cout<<"ERROR GETTING L1EXTRA ISO TAUS"<<std::endl;

    efficiencyTree->Fill();

    }

  }

}

/*
 * Return DeltaR of three Prong
 * Min prong Pt
 * nSignal Cands
 */
void 
L1TNtuplizer::getThreeProngInfo(const reco::PFTau & tau, double &maxDeltaR, double &minProngPt, double &midProngPt, double &maxProngPt, int &nCands){
  maxDeltaR = 0;
  minProngPt = tau.signalPFCands().at(0)->pt();
  midProngPt = tau.signalPFCands().at(0)->pt();
  maxProngPt = tau.signalPFCands().at(0)->pt();
  int i = 0;
  for(i = 0; i < tau.signalPFCands().size(); i++){
    double dR = deltaR( tau.p4(), tau.signalPFCands().at(i)->p4());
    double ptProng = tau.signalPFCands().at(i)->pt();
    if(dR>maxDeltaR)
      maxDeltaR = dR;

    if(minProngPt>ptProng)
      minProngPt = ptProng;

    if(maxProngPt<ptProng){
      midProngPt = maxProngPt;
      maxProngPt = ptProng;
    }
    
  }
  nCands = i;
}

void
L1TNtuplizer::getRawEcalHcalEnergy(const reco::PFCandidatePtr pfCand, double &rawEcal, double &rawHcal, double &ecal, double &hcal){
  //edm::Ptr<reco::PFCandidate> PFCand = tau.leadPFCand();
  //std::cout<<"Pt "<<pfCand->pt()<<std::endl;
  if(pfCand.isNonnull()){
    rawEcal = pfCand->rawEcalEnergy();
    rawHcal = pfCand->rawHcalEnergy();
    ecal = pfCand->ecalEnergy();
    hcal = pfCand->hcalEnergy();
  }
}

//four vector addition vs linear sum
double
L1TNtuplizer::getPFCandsEt(const std::vector<reco::PFCandidatePtr> pfCands){
  double etTotal = 0;
  for (uint32_t i = 0; i < pfCands.size(); i++ ) {
    etTotal +=pfCands.at(i)->et();
  }
  return etTotal;
}

double
L1TNtuplizer::getPFCandsEtEtaPhi(edm::Handle<std::vector<reco::PFCandidate> >& pfCands, const reco::PFTau & tau, double dR){
  double etTotal = 0;
  for (uint32_t i = 0; i < pfCands->size(); i++ ) {
    if(reco::deltaR(tau, pfCands->at(i)) < dR){
      etTotal +=pfCands->at(i).et();
    }
  }
  return etTotal;
}


int
L1TNtuplizer::get2x2TPGs(const int maxTPGPt_eta,const int maxTPGPt_phi, const double eTowerETMap[73][57], const double hTowerETMap[73][57], double &TPGe5x5_, double &TPGh5x5_ ){
  
  //TPG5x5_gcteta_ = twrEta2RegionEta(maxTPGPt_eta);
  //TPG5x5_tpgeta_ = maxTPGPt_eta;
  for (int j = -1; j < 2; ++j) {//phi
    for (int k = -1; k < 2; ++k) { //eta
      int tpgsquarephi= maxTPGPt_phi+j;
      int tpgsquareeta= maxTPGPt_eta+k;
      if (tpgsquarephi==-1) {tpgsquarephi=71;}
      if (tpgsquarephi==-2) {tpgsquarephi=70;}
      if (tpgsquarephi==-3) {tpgsquarephi=69;}
      if (tpgsquarephi==-4) {tpgsquarephi=68;}
      if (tpgsquarephi==-5) {tpgsquarephi=67;}
      if (tpgsquarephi==72) {tpgsquarephi=0;}
      if (tpgsquarephi==73) {tpgsquarephi=1;}
      if (tpgsquarephi==74) {tpgsquarephi=2;}
      if (tpgsquarephi==75) {tpgsquarephi=3;}
      if (tpgsquarephi==76) {tpgsquarephi=4;}
      if (tpgsquareeta>55 || tpgsquareeta<0) {continue;}//No Eta values beyond
      TPGh5x5_ += hTowerETMap[tpgsquarephi][tpgsquareeta];
      TPGe5x5_ += eTowerETMap[tpgsquarephi][tpgsquareeta];
    }
  }
  //std::cout<<"TPGe5x5_ "<<TPGe5x5_<<" TPGh5x5_ "<<TPGh5x5_<<std::endl;
  return (TPGe5x5_ + TPGh5x5_);
}


int
L1TNtuplizer::get5x5TPGs(const int maxTPGPt_eta,const int maxTPGPt_phi, const double eTowerETMap[73][57], const double hTowerETMap[73][57], double &TPGe5x5_, double &TPGh5x5_ ){
  
  //TPG5x5_gcteta_ = twrEta2RegionEta(maxTPGPt_eta);
  //TPG5x5_tpgeta_ = maxTPGPt_eta;
  for (int j = -5; j < 6; ++j) {//phi
    for (int k = -5; k < 6; ++k) { //eta
      int tpgsquarephi= maxTPGPt_phi+j;
      int tpgsquareeta= maxTPGPt_eta+k;
      if (tpgsquarephi==-1) {tpgsquarephi=71;}
      if (tpgsquarephi==-2) {tpgsquarephi=70;}
      if (tpgsquarephi==-3) {tpgsquarephi=69;}
      if (tpgsquarephi==-4) {tpgsquarephi=68;}
      if (tpgsquarephi==-5) {tpgsquarephi=67;}
      if (tpgsquarephi==72) {tpgsquarephi=0;}
      if (tpgsquarephi==73) {tpgsquarephi=1;}
      if (tpgsquarephi==74) {tpgsquarephi=2;}
      if (tpgsquarephi==75) {tpgsquarephi=3;}
      if (tpgsquarephi==76) {tpgsquarephi=4;}
      if (tpgsquareeta>55 || tpgsquareeta<0) {continue;}//No Eta values beyond
      TPGh5x5_ += hTowerETMap[tpgsquarephi][tpgsquareeta];
      TPGe5x5_ += eTowerETMap[tpgsquarephi][tpgsquareeta];
    }
  }
  //std::cout<<"TPGe5x5_ "<<TPGe5x5_<<" TPGh5x5_ "<<TPGh5x5_<<std::endl;
  return (TPGe5x5_ + TPGh5x5_);
}

int
L1TNtuplizer::get6x6TPGs(const int maxTPGPt_eta,const int maxTPGPt_phi, const double eTowerETMap[73][57], const double hTowerETMap[73][57], double &TPGe6x6_, double &TPGh6x6_ ){

  for (int j = -6; j < 7; ++j) {//phi
    for (int k = -6; k < 7; ++k) { //eta
      int tpgsquarephi= maxTPGPt_phi+j;
      int tpgsquareeta= maxTPGPt_eta+k;
      if (tpgsquarephi==-1) {tpgsquarephi=71;}
      if (tpgsquarephi==-2) {tpgsquarephi=70;}
      if (tpgsquarephi==-3) {tpgsquarephi=69;}
      if (tpgsquarephi==-4) {tpgsquarephi=68;}
      if (tpgsquarephi==-5) {tpgsquarephi=67;}
      if (tpgsquarephi==72) {tpgsquarephi=0;}
      if (tpgsquarephi==73) {tpgsquarephi=1;}
      if (tpgsquarephi==74) {tpgsquarephi=2;}
      if (tpgsquarephi==75) {tpgsquarephi=3;}
      if (tpgsquarephi==76) {tpgsquarephi=4;}
      if (tpgsquareeta>55 || tpgsquareeta<0) {continue;}//No Eta values beyond
      TPGh6x6_ += hTowerETMap[tpgsquarephi][tpgsquareeta];
      TPGe6x6_ += eTowerETMap[tpgsquarephi][tpgsquareeta];
    }
  }
  //std::cout<<"TPGe6x6_ "<<TPGe6x6_<<" TPGh6x6_ "<<TPGh6x6_<<std::endl;
  return (TPGe6x6_ + TPGh6x6_);
}


int
L1TNtuplizer::get7x7TPGs(const int maxTPGPt_eta,const int maxTPGPt_phi, const double eTowerETMap[73][57], const double hTowerETMap[73][57], double &TPGe7x7_, double &TPGh7x7_ ){
  for (int j = -7; j < 8; ++j) {//phi
    for (int k = -7; k < 8; ++k) { //eta
      int tpgsquarephi= maxTPGPt_phi+j;
      int tpgsquareeta= maxTPGPt_eta+k;
      if (tpgsquarephi==-1) {tpgsquarephi=71;}
      if (tpgsquarephi==-2) {tpgsquarephi=70;}
      if (tpgsquarephi==-3) {tpgsquarephi=69;}
      if (tpgsquarephi==-4) {tpgsquarephi=68;}
      if (tpgsquarephi==-5) {tpgsquarephi=67;}
      if (tpgsquarephi==72) {tpgsquarephi=0;}
      if (tpgsquarephi==73) {tpgsquarephi=1;}
      if (tpgsquarephi==74) {tpgsquarephi=2;}
      if (tpgsquarephi==75) {tpgsquarephi=3;}
      if (tpgsquarephi==76) {tpgsquarephi=4;}
      if (tpgsquareeta>55 || tpgsquareeta<0) {continue;}//No Eta values beyond
      TPGh7x7_ += hTowerETMap[tpgsquarephi][tpgsquareeta];
      TPGe7x7_ += eTowerETMap[tpgsquarephi][tpgsquareeta];
    }
  }
  //std::cout<<"TPGe7x7_ "<<TPGe7x7_<<" TPGh7x7_ "<<TPGh7x7_<<std::endl;
  return (TPGe7x7_ + TPGh7x7_);
}

  
/*
 * Get the ECAL TPGS create a TPG map for the event
 *
 */
  
void L1TNtuplizer::initializeECALTPGMap(Handle<EcalTrigPrimDigiCollection> ecal, double eTowerETMap[73][57], bool testMode){
  
  //std::cout << "ECAL TPGS" << std::endl;
  for (size_t i = 0; i < ecal->size(); ++i) {
    int cal_ieta = (*ecal)[i].id().ieta();
    int cal_iphi = (*ecal)[i].id().iphi();
    int iphi = cal_iphi-1;
    int ieta = TPGEtaRange(cal_ieta);
    // TPG iPhi starts at 1 and goes to 72.  Let's index starting at zero.
    // TPG ieta ideal goes from 0-55.
    double LSB = 0.5;
    double et= (*ecal)[i].compressedEt()*LSB;

    if(testMode && iphi == 34 && ieta == 11){
      et = 40;
    }

    //if(et>0)
    //cout<<"Before filling eTower"
    //<<"ECAL ieta:"<<ieta<<" cal_ieta:"<< cal_ieta<<" iphi:"<<iphi<<" et:"<<et<<endl;

    if (iphi >= 0 && iphi <= 72 &&
	ieta >= 0 && ieta <= 55) {
      eTowerETMap[iphi][ieta] = et; 
    }

  }

}

 void L1TNtuplizer::initializeHCALTPGMap(const Handle<HcalTrigPrimDigiCollection> hcal, 
					 const ESHandle<L1CaloHcalScale>  hcalScale, 
					 double hTowerETMap[73][57], bool testMode){
  for (size_t i = 0; i < hcal->size(); ++i) {
    HcalTriggerPrimitiveDigi tpg = (*hcal)[i];
    int cal_ieta = tpg.id().ieta();
    int cal_iphi = tpg.id().iphi();
    int iphi = cal_iphi-1;
    int ieta = TPGEtaRange(cal_ieta);
    short absieta = std::abs(tpg.id().ieta());
    short zside = tpg.id().zside();
    double energy = hcalScale->et(tpg.SOI_compressedEt(), absieta, zside); 

    if(testMode && iphi == 34 && ieta == 12){
      energy = 40;
    }

    if (iphi >= 0 && iphi <= 71 &&
	ieta >= 0 && ieta <= 55) {

      //(*hcal)[i].SOI_compressedEt(), absieta, zside)*LSB; //*LSB
      //if(energy>0)
      //std::cout<<"hcal iphi "<<iphi<<" ieta "<<ieta<<" energy "<<energy<<std::endl;
      hTowerETMap[iphi][ieta] = energy;
      //TPGSum_ +=energy;
      //TPGH_ += energy;
      //double alpha_h = TPGSFp_[cal_ieta]; //v3
      //hCorrTowerETMap[cal_iphi][cal_ieta] = alpha_h*energy;
      //cTPGH_ += alpha_h*energy;
      //if (energy > 0) {
      //std::cout << "hcal eta/phi=" << ieta << "/" << iphi
      //<< " = (" << getEtaTPG(ieta) << "/" << getPhiTPG(iphi) << ") "
      //<< " et=" << (*hcal)[i].SOI_compressedEt()
      //<< " energy=" << energy
      //<< " rctEta="<< twrEta2RegionEta(cal_ieta) << " rctPhi=" << twrPhi2RegionPhi(cal_iphi)
      //<< " fg=" << (*hcal)[i].SOI_fineGrain() << std::endl;
      //}
      //if (energy>maxTPGHPt){
      //maxTPGHPt=energy;
      //maxTPGHPt_phi = cal_iphi; //this one starts at 0-72
      //maxTPGHPt_eta = cal_ieta; //this one is 0-54
      //} 
    }
    //else
      //std::cout<<"HCAL failed checks iphi "<<iphi<<" ieta "<<ieta<<std::endl;
  }//end HCAL TPG
}

void L1TNtuplizer::endJob() {
}

L1TNtuplizer::~L1TNtuplizer(){
}

DEFINE_FWK_MODULE(L1TNtuplizer);
