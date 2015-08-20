#!/bin/sh 
cd /scratch/ojalvo/tauSeedStudy

#farmoutAnalysisJobs \
#   --merge \
#   --input-files-per-job=100 \
#   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/ojalvo/tauSeed-7-hTT-really-SUBStage1 \
#   htt-tauSeed-7 \
#   /cms/ojalvo/stage1Emulator/test1/CMSSW_7_5_0_pre1


#for dir in tau-e3-h3-SUBStage1 tau-e3-h6-SUBStage1 tau-e4-h5-SUBStage1 tau-e5-h5-SUBStage1 tau-rctCal-e3-h3-SUBStage1 tau-rctCal-e3-h6-SUBStage1 tau-rctCal-e4-h5-SUBStage1 tau-rctCal-e5-h5-SUBStage1 tau-e3-h5-SUBStage1 tau-e4-h4-SUBStage1 tau-e4-h6-SUBStage1 tau-e6-h6-SUBStage1 tau-rctCal-e3-h5-SUBStage1 tau-rctCal-e4-h4-SUBStage1 tau-rctCal-e4-h6-SUBStage1 tau-rctCal-e6-h6-SUBStage1;
for dir in tau-rctCal-e3-h3-SUBStage1 tau-rctCal-e3-h6-SUBStage1 tau-rctCal-e4-h5-SUBStage1 tau-rctCal-e5-h5-SUBStage1 tau-rctCal-e3-h5-SUBStage1 tau-rctCal-e4-h4-SUBStage1 tau-rctCal-e4-h6-SUBStage1 tau-rctCal-e6-h6-SUBStage1;
do
    farmoutAnalysisJobs \
   --merge \
   --input-files-per-job=500 \
   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/ojalvo/$dir \
   $dir-merge \
   /cms/ojalvo/stage1Emulator/test1/CMSSW_7_5_0_pre1
done