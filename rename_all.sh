#!/bin/bash
#This script was created to modify .pep output files created in Amphoranet website. The aim is to prepare these files for subsequent concatenation of alignments using phyutils. after alignment.
#Firstly,decompress each zipped file in a folder with the name of the species.

for dir in *; do
cd $dir
	for file in *.pep; do
	sed "s/>.*/>`basename $dir`/g" $file > `basename $dir`_`basename $file .pep`_ren.fas #rename fasta header with folder name and creates a new file
	done
cd ..
done

#Fasta files from a specific gene but from different lineages cam be joined for subsequent alignment. Ex: cat *rpoB_ren.fas > rpoB_all.fasta; muscle -in rpoB_all.fasta -out rpoB_all_aln.fasta
#Alignments can be joined using phyutils. Ex: java -jar /opt/phyutility/phyutility.jar -concat -in *.fas -out paeni_conc.nex

