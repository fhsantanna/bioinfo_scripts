#!/usr/bin/env python

#Create list corresponding locus_tag to product

from Bio import SeqIO
import sys

for rec in SeqIO.parse(open(sys.argv[1],"rU"),"genbank"):
    if rec.features:
        for feature in rec.features:
            if feature.type == "rRNA":
                print "%s\t%s" % (feature.qualifiers["locus_tag"][0],feature.qualifiers["product"][0])
            if feature.type == "CDS":
                print "%s\t%s" % (feature.qualifiers["locus_tag"][0],feature.qualifiers["product"][0])
            if feature.type == "tRNA":
                print "%s\t%s" % (feature.qualifiers["locus_tag"][0],feature.qualifiers["product"][0])

