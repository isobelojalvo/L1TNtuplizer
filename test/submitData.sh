m#!/bin/sh 

#voms-proxy-init --voms cms --valid 100:00

cat Stage1DataRECO.py > SUBStage1.py
#cat submitSecondaryFiles.py >> SUBStage1.py
#tauIsoLutTest0.12Iso.txt  tauIsoLutTest0.15Iso.txt  tauIsoLutTest0.17Iso.txt  tauIsoLutTest0.2Iso.txt

farmoutAnalysisJobs  $1 --vsize-limit=8000 --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist  tau-Stage1-SingleMuonRECO-4GeV-3Prong $CMSSW_BASE $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'
exit;
farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauIsoC-e3-h3-iso-12       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.12Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauIsoC-e3-h3-iso-15       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.15Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauIsoC-e3-h3-iso-17       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.17Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauIsoC-e3-h3-iso-20       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.2Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'
######
farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauIsoC-e6-h6-iso-12       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=6 hActivityCut=6 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.12Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauIsoC-e6-h6-iso-15       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=6 hActivityCut=6 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.15Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauIsoC-e6-h6-iso-17       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=6 hActivityCut=6 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.17Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauIsoC-e6-h6-iso-20       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=6 hActivityCut=6 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.2Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'


exit;

#farmoutAnalysisJobs  $1 --vsize-limit=8000 --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist  tau-Stage1-SingleMuonRECO-tauCalibrated $CMSSW_BASE $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName' 

exit;

#Matching E and H activity
farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauC-e3-h3       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauC-e4-h4       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=4 hActivityCut=4 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'
farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauC-e5-h5       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=5 hActivityCut=5 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'
farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauC-e6-h6       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=6 hActivityCut=6 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

#Ecal Activity = 3
farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauC-e3-h5       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=5 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauC-e3-h6       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=6 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'
#Ecal Activity = 4
farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauC-e4-h5       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=4 hActivityCut=5 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauC-e4-h6       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=4 hActivityCut=6 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'


#tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.15Iso.txt"

#Matching E and H activity
farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauIsoC-e3-h3       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=3 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.12Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'
farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauIsoC-e4-h4       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=4 hActivityCut=4 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.12Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'
farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauIsoC-e5-h5       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=5 hActivityCut=5 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.12Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'
farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauIsoC-e6-h6       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=6 hActivityCut=6 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.12Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

#Ecal Activity = 3
farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauIsoC-e3-h5       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=5 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.12Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauIsoC-e3-h6       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=3 hActivityCut=6 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.12Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'
#Ecal Activity = 4
farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauIsoC-e4-h5       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=4 hActivityCut=5 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.12Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'

farmoutAnalysisJobs    --vsize-limit=8000    --input-files-per-job=1 --input-dir=root://cmsxrootd.hep.wisc.edu/ --input-file-list=SingleMuonRECO.txt --assume-input-files-exist    tauIsoC-e4-h6       $CMSSW_BASE   $CMSSW_BASE/src/L1Trigger/L1TNtuplizer/test/SUBStage1.py eActivityCut=4 hActivityCut=6 tauThresh=7 tauNThresh=0 tauMaxPtTauVeto=64  tauIsoLUTFile="L1Trigger/L1TCalorimeter/data/tauIsoLutTest0.12Iso.txt" tauCalibLUTFile="L1Trigger/L1TCalorimeter/data/tauL1Calib_LUT.txt" 'inputFiles=$inputFileNames' 'outputFile=$outputFileName'


rm SUBStage1.py

