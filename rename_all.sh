#!/bin/bash
#This script was created to modify .pep output files created in Amphoranet website. The aim is to prepare this files for subsequent concatenation using phyutils, after alignment.

for dir in *; do
cd $dir
	for file in *.pep; do
	sed "s/>.*/>`basename $dir`/g" $file > `basename $dir`_`basename $file .pep`_ren.fas #rename fasta header with folder name and creates a new file
	done
cd ..
done
