#!/usr/bin/env python

#Identify positions containing gaps or missing characters in a sequence.
#usage: ./gap_detect.py file.fasta > file.csv

from Bio import SeqIO
import sys

file_name = sys.argv[1]
seq = SeqIO.read(file_name, "fasta")

print("File", "Pos", "nt")
for r in range(0,len(seq.seq)):
     if seq[r] in ["-","N", "?"]:
        print("{}\t{}\t{}".format(file_name,r+1,seq[r]))