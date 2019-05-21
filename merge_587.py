#!/bin/env python3

from Bio import SeqIO
merged_rec = ''
infile = "S587_split00000000.bgpipe.output.gb"
for rec in SeqIO.parse(open(infile,"r"), "genbank") :
    merged_rec += rec
    # you could insert a spacer if needed
    # merged_rec += rec + ("N" * 50)
merged_rec.id = "mergedseq"
merged_rec.description = "merged seq"
SeqIO.write(merged_rec, "S587_merged.gbk", "genbank")