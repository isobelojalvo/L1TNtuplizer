m#!/bin/sh 

#voms-proxy-init --voms cms --valid 100:00

cat Stage1DataRECORCT.py > SUBStage1.py
#cat submitSecondaryFiles.py >> SUBStage1.py
#tauIsoLutTest0.12Iso.txt  tauIsoLutTest0.15Iso.txt  tauIsoLutTest0.17Iso.txt  tauIsoLutTest0.2Iso.txt

farmoutAnalysisJobs  $1 --vsize-limit=8000 --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist  tau-RCT-Data-NOEG-NOREG $CMSSW_BASE $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=4 hActivityCut=4 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" RCTCalibrationMode='L1RCTParametersRcd_L1TDevelCollisions_ExtendedScaleFactors_EGOnly_v1' 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs  $1 --vsize-limit=8000 --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist  tau-RCT-Data-NOEG $CMSSW_BASE $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=4 hActivityCut=4 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" RCTCalibrationMode='L1RCTParametersRcd_L1TDevelCollisions_ExtendedScaleFactorsV3' 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs  $1 --vsize-limit=8000 --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist  tau-RCT-Data-FullEG $CMSSW_BASE $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=4 hActivityCut=4 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" RCTCalibrationMode='L1RCTParametersRcd_L1TDevelCollisions_ExtendedScaleFactors_NewTau_FullEGTransparency_v1' 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'


rm SUBStage1.py

