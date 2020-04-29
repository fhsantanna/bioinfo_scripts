#!/usr/bin/env python

#Extract nucleotide sequences from all CDSs of a genbank file to a fasta file. Usage "python extract_CDS.py file.gbk > output.fas". This script needs BioPython. 

from Bio import SeqIO
import sys

for rec in SeqIO.parse(open(sys.argv[1],"rU"),"genbank"):
    if rec.features:
        for feature in rec.features:
            if feature.type == "CDS":
                print(">%s|%s\n%s" % (feature.qualifiers["locus_tag"][0],feature.location,feature.location.extract(rec).seq))
