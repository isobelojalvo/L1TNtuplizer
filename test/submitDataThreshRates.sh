#!/bin/sh 

#voms-proxy-init --voms cms --valid 100:00

cat Stage1DataRECORates.py > SUBStage1.py
#cat submitSecondaryFiles.py >> SUBStage1.py
#tauIsoLutTest0.12Iso.txt  tauIsoLutTest0.15Iso.txt  tauIsoLutTest0.17Iso.txt  tauIsoLutTest0.2Iso.txt

#farmoutAnalysisJobs  $1 --vsize-limit=8000 --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist  tau-Stage1-SingleMuonRECO-4GeV $CMSSW_BASE $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=ZeroBias_2015BFull.txt --assume-input-files-exist    tauRates-e3-h3-thresh-1       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=1 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.12Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=ZeroBias_2015BFull.txt --assume-input-files-exist    tauRates-e3-h3-thresh-2     $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=2 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.15Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=ZeroBias_2015BFull.txt --assume-input-files-exist    tauRates-e3-h3-thresh-3     $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=3 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.17Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=ZeroBias_2015BFull.txt --assume-input-files-exist    tauRates-e3-h3-thresh-4     $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=4 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.2Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=ZeroBias_2015BFull.txt --assume-input-files-exist    tauRates-e3-h3-thresh-5     $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=5 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.2Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=ZeroBias_2015BFull.txt --assume-input-files-exist    tauRates-e3-h3-thresh-6     $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=6 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.2Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=ZeroBias_2015BFull.txt --assume-input-files-exist    tauRates-e3-h3-thresh-7     $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.2Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=ZeroBias_2015BFull.txt --assume-input-files-exist    tauRates-e3-h3-thresh-8     $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=8 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.2Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=ZeroBias_2015BFull.txt --assume-input-files-exist    tauRates-e3-h3-thresh-9     $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=9 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.2Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'


rm SUBStage1.py

