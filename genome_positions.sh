#!/bin/bash

for file in *.gbk; do
	perl gb2bed.pl -i $file -k gene -o `basename $file .gbk`_raw.genes
	awk '($2 < $3)' `basename $file .gbk`_raw.genes > `basename $file .gbk`.genes
	#if first position is larger than second 
	#(e.g. origin, starting at the end of the file and ending at the start of the file), the record is excluded
	echo -e "$(grep "VERSION" $file | sed 's/\s */\t/g' | cut -f2)\t$(grep "LOCUS" $file | sed 's/\s */\t/g' | cut -f3)" > `basename $file .gbk`.genome
done


