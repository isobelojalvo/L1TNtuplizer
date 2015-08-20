#!/bin/sh 
mkdir /scratch/ojalvo/tauThreshStudy-mc
cd /scratch/ojalvo/tauThreshStudy-mc


for dir in tauIsoC-MC-e3-h3-thresh-1 tauIsoC-MC-e3-h3-thresh-2 tauIsoC-MC-e3-h3-thresh-3 tauIsoC-MC-e3-h3-thresh-4 tauIsoC-MC-e3-h3-thresh-5 tauIsoC-MC-e3-h3-thresh-6 tauIsoC-MC-e3-h3-thresh-7 tauIsoC-MC-e3-h3-thresh-8 tauIsoC-MC-e3-h3-thresh-9 
do
    hadd $dir.root /hdfs/store/user/ojalvo/$dir-SUBStage1/*
done