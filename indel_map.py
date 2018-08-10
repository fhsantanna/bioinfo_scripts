#!/usr/bin/env python

from Bio import AlignIO
import sys

file_name = sys.argv[1]
alignment = AlignIO.read(file_name, "fasta")

y = 0

print("Indel")
print("Id", "Protein", "Pos", "Strain_1", "AA_1", "AA_2", "Strain_2")
for r in range(0,len(alignment[1].seq)):
     if alignment[0,r] != alignment[1,r]:
        if alignment[0,r] == "-" or alignment[1,r] == "-":
            y = y + 1
            print(y, file_name, r, alignment[0].name, alignment[0,r], alignment[1,r], alignment[1].name)
        else:
            y = 0
