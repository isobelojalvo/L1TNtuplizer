#!/bin/sh 
#rm -rf /scratch/ojalvo/tauSeedStudy-data
#mkdir /scratch/ojalvo/tauSeedStudy-data
#cd /scratch/ojalvo/tauSeedStudy-data
mkdir /scratch/ojalvo/tauIsoStudy-data

#farmoutAnalysisJobs \
#   --merge \
#   --input-files-per-job=100 \
#   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/ojalvo/tauSeed-7-hTT-really-SUBStage1 \
#   htt-tauSeed-7 \
#   /cms/ojalvo/stage1Emulator/test1/CMSSW_7_5_0_pre1

#hadd tau-Stage1-SingleMuonRECO-4GeV /hdfs/store/user/ojalvo/tau-Stage1-SingleMuonRECO-4GeV-SUBStage1/*
#hadd -f tauSeed-data.root /hdfs/store/user/ojalvo/tau-Stage1-SingleMuonRECO-SUBStage1/*
#hadd -f tauSeed-data-calibrated.root /hdfs/store/user/ojalvo/tau-Stage1-SingleMuonRECO-tauCalibrated-SUBStage1/*

for dir in  tauC-e4-h4-SUBStage1 tauC-e3-h3-SUBStage1 tauC-e3-h5-SUBStage1 tauC-e5-h5-SUBStage1 tauC-e6-h6-SUBStage1 tauC-e4-h5-SUBStage1 tauC-e4-h6-SUBStage1 tauIsoC-e3-h6-SUBStage1 tauIsoC-e4-h4-SUBStage1 tauIsoC-e3-h3-SUBStage1 tauIsoC-e3-h5-SUBStage1
do
    hadd $dir.root /hdfs/store/user/ojalvo/$dir/*
done

for dir in  tauIsoC-e4-h5-SUBStage1 tauIsoC-e5-h5-SUBStage1 tauIsoC-e4-h6-SUBStage1 tauIsoC-e6-h6-SUBStage1 #tauIsoC-e3-h6-SUBStage1 tauIsoC-e4-h4-SUBStage1 tauIsoC-e3-h3-SUBStage1 tauIsoC-e3-h5-SUBStage1
do
    hadd $dir.root /hdfs/store/user/ojalvo/$dir/*
done


#hadd $dir /hdfs/store/user/ojalvo/tau-e3-h3-SUBStage1-merge-mergeFilesJob/*

