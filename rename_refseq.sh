#!/bin/bash

#Rename RefSeq files (fna and gbff) to organism name.

for file in *.gbff; do
orgname=$(grep "ORGANISM" $file | sed 's/  ORGANISM  //g' | sed 's/ /_/g' | uniq)
cp `basename $file .gbff`.fna $orgname.fna
echo $orgname
done

for file in *.gbff; do
orgname=$(grep "ORGANISM" $file | sed 's/  ORGANISM  //g' | sed 's/ /_/g' | uniq)
cp `basename $file .gbff`.gbff $orgname.gbk
echo $orgname
done

