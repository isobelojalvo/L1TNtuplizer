#!/bin/sh 
mkdir /scratch/ojalvo/tauThreshStudyRates-data
cd /scratch/ojalvo/tauThreshStudyRates-data


for dir in  tauRates-e3-h3-thresh-1 tauRates-e3-h3-thresh-2 tauRates-e3-h3-thresh-3 tauRates-e3-h3-thresh-4 tauRates-e3-h3-thresh-5 tauRates-e3-h3-thresh-6 tauRates-e3-h3-thresh-7 tauRates-e3-h3-thresh-8 tauRates-e3-h3-thresh-9 
do
    hadd $dir.root /hdfs/store/user/ojalvo/$dir-SUBStage1/*
done

