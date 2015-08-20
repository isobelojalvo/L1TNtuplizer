#!/bin/sh 
cd /scratch/ojalvo/tauSeedStudy
hadd tauSeed-5.root /hdfs/store/user/ojalvo/htt-tauSeed-5-mergeFilesJob/*
hadd tauSeed-7.root /hdfs/store/user/ojalvo/htt-tauSeed-7-mergeFilesJob/*
hadd tauSeed-8.root /hdfs/store/user/ojalvo/htt-tauSeed-8-mergeFilesJob/*
hadd tauSeed-9.root /hdfs/store/user/ojalvo/htt-tauSeed-9-mergeFilesJob/*

#/cms/sw/farmout/mergeFiles  htt-tauSeed-5.root /hdfs/store/user/$USER/tauSeed-7-hTT-SUBStage1
#/cms/sw/farmout/mergeFiles  htt-tauSeed-7.root /hdfs/store/user/$USER/tauSeed-7-hTT-really-SUBStage1
#/cms/sw/farmout/mergeFiles  htt-tauSeed-8.root /hdfs/store/user/$USER/tauSeed-8-hTT-SUBStage1
#/cms/sw/farmout/mergeFiles  htt-tauSeed-9.root /hdfs/store/user/$USER/tauSeed-9-hTT-SUBStage1


