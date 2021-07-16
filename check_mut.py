#!/usr/bin/env python

#Identify differential characters between a pair of aligned sequences.
#usage: ./check_mut.py file.fasta > file.csv

from Bio import AlignIO
import sys

file_name = sys.argv[1]
alignment = AlignIO.read(file_name, "fasta")


print("File", "Pos", "Sequence_1", "NT_1", "NT_2", "Sequence_2")
for r in range(0,len(alignment[1].seq)):
     if alignment[0,r] != alignment[1,r]:
        print(file_name, r+1, alignment[0].name, alignment[0,r], alignment[1,r], alignment[1].name)