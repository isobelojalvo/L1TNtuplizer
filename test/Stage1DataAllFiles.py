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
    fileNames = cms.untracked.vstring(
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/162/00000/160C08A3-4227-E511-B829-02163E01259F.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/164/00000/544E58CD-A226-E511-834E-02163E0134D6.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/167/00000/EE9594B8-A826-E511-A18B-02163E011A7D.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/168/00000/4E8E390B-EA26-E511-9EDA-02163E013567.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/168/00000/60FF8405-EA26-E511-A892-02163E01387D.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/244/00000/68275270-7C27-E511-B1F0-02163E011A46.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/244/00000/B6304C6F-7C27-E511-9C77-02163E01250E.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/251/00000/EEBF2AF4-8D27-E511-91F7-02163E014527.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/252/00000/0438FA5A-A127-E511-BA6F-02163E013414.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/252/00000/7E4A8F57-A127-E511-9BF5-02163E014629.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/493/00000/6A4D2AB2-E828-E511-B82B-02163E0121E9.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/497/00000/668C5130-FE28-E511-8F78-02163E0133B0.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/498/00000/50CD6709-0C29-E511-8F8B-02163E0134FD.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/499/00000/402D1C6D-1729-E511-ABF5-02163E011DFF.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/500/00000/62310AED-3729-E511-AC61-02163E012712.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/500/00000/A2A303EC-3729-E511-9ECE-02163E011A29.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/521/00000/425B1189-6729-E511-AF38-02163E013728.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/522/00000/F6930521-5D29-E511-B517-02163E011D37.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/548/00000/44CE0650-EF29-E511-BA0D-02163E012601.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/560/00000/A886DB09-E029-E511-8A06-02163E0125C8.root',
       '/store/data/Run2015B/SingleMuon/MINIAOD/PromptReco-v1/000/251/561/00000/F6A7CE0F-132A-E511-A423-02163E011D88.root'
        ),
   secondaryFileNames = cms.untracked.vstring(
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/162/00000/0050EEC0-AD25-E511-9A32-02163E011962.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/164/00000/82568FFB-1225-E511-96EF-02163E01477B.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/167/00000/02E73B02-1325-E511-B602-02163E01342D.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/168/00000/18FAC13D-2D25-E511-AAF5-02163E01342D.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/168/00000/1EFD8D46-2725-E511-B5DC-02163E0122D3.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/168/00000/382EE8DB-2825-E511-B3E0-02163E013597.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/168/00000/3AF7425B-1F25-E511-A25E-02163E0118C7.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/168/00000/A6567D6A-2D25-E511-B388-02163E013970.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/168/00000/BC535941-1C25-E511-8310-02163E011D46.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/168/00000/C617FE0B-1B25-E511-92D6-02163E012543.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/244/00000/121414E3-BC25-E511-A61B-02163E0134BE.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/244/00000/22451D13-B125-E511-B5D1-02163E0133C2.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/244/00000/26C4AB15-B125-E511-B06F-02163E0137FC.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/244/00000/2A20CC30-B125-E511-9D25-02163E01340C.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/244/00000/4A944B18-B125-E511-8CF7-02163E011BD1.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/244/00000/76310675-BC25-E511-8167-02163E011D12.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/244/00000/9A266904-B125-E511-81BE-02163E0143C0.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/244/00000/9CD30F09-B125-E511-95D8-02163E013390.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/244/00000/A0DBC00A-B125-E511-B1B4-02163E011D4A.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/244/00000/BA480726-AF25-E511-97A9-02163E0120B0.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/244/00000/C254C44D-AC25-E511-983E-02163E01264D.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/251/00000/02E8B556-CA25-E511-A441-02163E011BB9.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/251/00000/0691B06D-CA25-E511-8FBD-02163E0133B6.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/251/00000/4CD4166A-CA25-E511-A474-02163E011D4A.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/251/00000/9E73A652-CA25-E511-B232-02163E0133ED.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/252/00000/144F0B64-DA25-E511-ACE2-02163E0125E8.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/252/00000/1CC77DF3-D525-E511-B548-02163E011DCE.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/252/00000/228CBF0B-E325-E511-91A0-02163E012093.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/252/00000/602A6CDA-DB25-E511-86C4-02163E014527.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/252/00000/92425F6D-CF25-E511-90F1-02163E0123FE.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/252/00000/B6467676-D225-E511-92AB-02163E013948.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/252/00000/BEFB3A85-DD25-E511-ACF0-02163E011FAB.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/252/00000/C645F038-CD25-E511-A3F2-02163E0118F6.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/252/00000/CACD9D92-DF25-E511-B9CB-02163E011836.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/252/00000/D6DDBA39-E625-E511-A89A-02163E012096.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/252/00000/FC11624F-CA25-E511-8036-02163E011A19.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/493/00000/1020CD98-3D27-E511-9A4B-02163E014553.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/493/00000/469C5C93-3D27-E511-B83C-02163E011955.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/493/00000/E4DEC8DC-3D27-E511-82BA-02163E0128F2.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/496/00000/10D5E7B8-3E27-E511-8654-02163E014531.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/496/00000/3E1F4883-4127-E511-AFA4-02163E013553.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/496/00000/B233E0B5-3E27-E511-849C-02163E011A5A.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/496/00000/C2D671BC-3E27-E511-B26C-02163E0144F6.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/496/00000/E01EF67E-4127-E511-AA05-02163E0146D1.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/497/00000/08D32850-4D27-E511-BB1A-02163E014558.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/497/00000/B6FB2AD6-5227-E511-A09C-02163E0127EF.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/497/00000/C4C3BC50-4D27-E511-A346-02163E014543.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/497/00000/CA0152DB-5227-E511-82B9-02163E01287D.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/497/00000/CE9E3443-5327-E511-BA06-02163E014576.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/497/00000/F48153DA-5227-E511-8D14-02163E011CD7.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/498/00000/06E3F0BF-5727-E511-B7C1-02163E013455.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/498/00000/4AD39833-5827-E511-A9EA-02163E01445F.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/498/00000/B647BDA7-5227-E511-AD5C-02163E011DAE.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/498/00000/E8E0A3C3-5727-E511-A0E3-02163E0133F9.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/499/00000/2087CBFF-6027-E511-976A-02163E0141EF.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/499/00000/9E5092F2-5F27-E511-AA22-02163E011955.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/499/00000/C89FEDFE-6027-E511-BB2C-02163E01433A.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/499/00000/D2A6B4EA-6027-E511-A47A-02163E0120D4.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/499/00000/DA44C501-6127-E511-9BB6-02163E014616.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/499/00000/EE9E8FAD-5927-E511-B460-02163E01182A.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/500/00000/023842E2-6F27-E511-A824-02163E01358B.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/500/00000/080FE4D6-6F27-E511-B93A-02163E013896.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/500/00000/6ECBF1D8-6F27-E511-8F7D-02163E012044.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/500/00000/70EC3D19-7027-E511-A679-02163E01208E.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/500/00000/98BE33D9-6F27-E511-9122-02163E014729.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/500/00000/B269B8DA-6F27-E511-AE66-02163E012283.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/500/00000/B2B214DB-6F27-E511-B411-02163E01413E.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/500/00000/CC9F16E6-6F27-E511-B1D7-02163E012787.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/500/00000/F26D7EDA-6F27-E511-8AE8-02163E0144DA.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/521/00000/DC5B8AC8-C527-E511-A816-02163E011CD6.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/522/00000/1481AFAA-C527-E511-B618-02163E012351.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/548/00000/B818C586-1028-E511-B70B-02163E011DA4.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/548/00000/E8FFA41B-1128-E511-9092-02163E01379D.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/560/00000/9A77BD5F-4928-E511-A882-02163E01360C.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/561/00000/2262F3C5-5328-E511-BE4C-02163E014553.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/561/00000/2CDEBF20-5128-E511-BA67-02163E013770.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/561/00000/56C5654F-5228-E511-90EB-02163E0138A8.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/561/00000/64F510B2-5128-E511-A302-02163E0134FD.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/561/00000/88F2779E-5028-E511-8350-02163E011DA4.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/561/00000/8A4B5321-5128-E511-8B0C-02163E0138A8.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/561/00000/B66AED4C-5428-E511-90DB-02163E011D37.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/561/00000/C4D3141B-5128-E511-9F48-02163E0133F2.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/561/00000/C6E151B9-5128-E511-8B8C-02163E012166.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/561/00000/DEDDA01F-5128-E511-958A-02163E011F52.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/045C8941-5C28-E511-A2C0-02163E011836.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/08057B7A-6628-E511-8A5C-02163E014637.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/0AE9515E-7A28-E511-8DC2-02163E01416E.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/0EF75E7B-6628-E511-83E9-02163E012031.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/10AFAA61-7A28-E511-A21D-02163E01192D.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/14732C75-8628-E511-BA5E-02163E012031.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/14B88EA2-7028-E511-B691-02163E013425.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/14E36389-5728-E511-8B32-02163E0133A4.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/16385780-6628-E511-AE13-02163E012AA4.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/18D3F277-8628-E511-A7AB-02163E012A2C.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/18ED7477-8628-E511-B5B6-02163E0121CD.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/1A40AA74-8628-E511-B449-02163E0121CC.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/2235978F-8628-E511-ACBB-02163E014181.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/263E637A-8628-E511-AFF0-02163E0137EA.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/281B8665-7B28-E511-9D0E-02163E014241.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/28DCAF7C-5B28-E511-8788-02163E012603.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/306B341F-6628-E511-8C6B-02163E0118E8.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/38E57077-8628-E511-A067-02163E01474A.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/3A7C7FE3-6328-E511-8123-02163E01287D.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/485F6B1D-6628-E511-B697-02163E011B19.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/5682F875-8628-E511-9734-02163E014543.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/56FD6C2C-5928-E511-859D-02163E0121E9.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/5A84B068-7B28-E511-A6DC-02163E013406.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/64AE3FB0-6128-E511-8D47-02163E01420D.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/68F4F861-7A28-E511-A3CC-02163E0127DF.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/6A533C68-7A28-E511-9CF6-02163E0133A7.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/6E89FD79-8628-E511-9688-02163E011DA4.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/746697DA-6728-E511-93CE-02163E011824.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/78341CE2-6328-E511-BEC4-02163E0144D6.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/7840F0ED-8628-E511-BF62-02163E011DE5.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/7A052F9F-7028-E511-81D5-02163E014272.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/7A96007F-5B28-E511-B11B-02163E011ABC.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/82677777-8628-E511-A3A6-02163E01474A.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/925E477A-6628-E511-BDFE-02163E0118A2.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/984D4675-8628-E511-B203-02163E011DE5.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/9E28AA19-6628-E511-8816-02163E0143F8.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/A058C521-6628-E511-8A70-02163E011ABC.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/A0BA549E-7028-E511-A996-02163E0144D6.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/A6F8CB8D-7A28-E511-80D2-02163E012BDE.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/A8A305A2-7028-E511-843B-02163E012916.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/AE571892-8628-E511-9DD7-02163E0138B3.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/B22C9D75-8628-E511-BE33-02163E011DE5.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/C4A8CF1B-6628-E511-9BF9-02163E01477B.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/C63B827E-5728-E511-99F4-02163E013770.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/D2F49581-5828-E511-85B7-02163E013425.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/D603CF9A-5C28-E511-A55A-02163E011ABC.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/DE6A091F-6628-E511-ADD2-02163E0118E7.root',
       '/store/data/Run2015B/SingleMuon/RAW/v1/000/251/562/00000/E2766E75-8628-E511-98EA-02163E01416E.root'

        )
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
