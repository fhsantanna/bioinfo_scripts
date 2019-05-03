#!/usr/bin/env python

#Script for getting proteins in a range from a genbank file
#Usage: python get_proteins.py file start:end

import sys
from Bio import SeqIO

rec = SeqIO.read(sys.argv[1], 'genbank')
feats = [feat for feat in rec.features if feat.type == "CDS"]
start, end = sys.argv[2].split(':')

desired = set(range(int(start),int(end),1))

for f in feats:
    span = set(range(f.location._start.position, f.location._end.position))
    if span & desired:
        print(">%s,%s,%d:%d\n%s\n" % (
					f.qualifiers['locus_tag'][0],
					f.qualifiers['product'][0],
					f.location._start.position,
					f.location._end.position,
					f.qualifiers['translation'][0]))