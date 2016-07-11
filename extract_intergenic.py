
#!/usr/bin/env python

#Extract intergenic sequences from all CDSs of a genbank file to a fasta file. Usage "python extract_intergenic.py file.gbk > output.fas". This script needs BioPython. 

from Bio import SeqIO
import sys

for rec in SeqIO.parse(open(sys.argv[1],"rU"),"genbank"):
    if rec.features:
        for feature in rec.features:
            try:
            	if feature.type == "misc_feature":
            		print ">%s|%s\n%s" % (feature.qualifiers["intergenic_tag"],feature.location,feature.location.extract(rec).seq)
            		pass
            except:
            		continue