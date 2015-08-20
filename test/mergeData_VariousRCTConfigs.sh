#!/bin/sh 
mkdir /scratch/ojalvo/tauData_VariousRCTConfigs
cd /scratch/ojalvo/tauData_VariousRCTConfigs

for dir in tau-RCT-Data-NOEG-NOREG tau-RCT-Data-NOEG tau-RCT-Data-FullEG     
do
    hadd $dir.root /hdfs/store/user/ojalvo/$dir-SUBStage1/*
done

