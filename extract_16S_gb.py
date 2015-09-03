#!/usr/bin/env python

from Bio import SeqIO, SeqFeature
import sys

gbank=SeqIO.parse(open(sys.argv[1],"rU"),"genbank")

for genome in gbank:
    for gene in genome.features:
        if gene.type=="rRNA": 
            if 'product' in gene.qualifiers:
                if '16S' in gene.qualifiers['product'][0]:
                    start = gene.location.nofuzzy_start
                    end = gene.location.nofuzzy_end
                    if 'locus_tag' in gene.qualifiers:
                        locus=[]
                        locus=str(gene.qualifiers['locus_tag'])
                        print ">GeneId|%s|16S rRNA|%s\n%s" % (locus,genome.description,genome.seq[start:end])
                    else:
                        print ">GeneId|NoGenID|16S rRNA|%s\n%s" % (genome.description,genome.seq[start:end])
