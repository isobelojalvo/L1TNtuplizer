#!/bin/sh 
mkdir /scratch/ojalvo/tauThreshStudy-data
cd /scratch/ojalvo/tauThreshStudy-data

#farmoutAnalysisJobs \
#   --merge \
#   --input-files-per-job=100 \
#   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/ojalvo/tauSeed-7-hTT-really-SUBStage1 \
#   htt-tauSeed-7 \
#   /cms/ojalvo/stage1Emulator/test1/CMSSW_7_5_0_pre1

#hadd tau-Stage1-SingleMuonRECO-4GeV /hdfs/store/user/ojalvo/tau-Stage1-SingleMuonRECO-4GeV-SUBStage1/*
#hadd -f tauSeed-data.root /hdfs/store/user/ojalvo/tau-Stage1-SingleMuonRECO-SUBStage1/*
#hadd -f tauSeed-data-calibrated.root /hdfs/store/user/ojalvo/tau-Stage1-SingleMuonRECO-tauCalibrated-SUBStage1/*

for dir in  tauIsoC-e3-h3-thresh-1 tauIsoC-e3-h3-thresh-2 tauIsoC-e3-h3-thresh-3 tauIsoC-e3-h3-thresh-4 tauIsoC-e3-h3-thresh-5 tauIsoC-e3-h3-thresh-6 tauIsoC-e3-h3-thresh-7 tauIsoC-e3-h3-thresh-8 tauIsoC-e3-h3-thresh-9 
do
    hadd $dir.root /hdfs/store/user/ojalvo/$dir-SUBStage1/*
done

