#!/usr/bin/env python

#Cria arquivos ptt e rnt a partir de um arquivo genbank. Útil para a utilização do EDGE-pro (Estimated Degree of Gene Expression for Prokaryotes).

from Bio import SeqIO
annotation_file = "P_riograndensis_LN831776.gbk"
rnt_file = "P_riograndensis_LN831776.rnt"
ptt_file = "P_riograndensis_LN831776.ptt"
fasta_file = "P_riograndensis_LN831776.fas"
r = SeqIO.parse(annotation_file, "gb")
for record in r:
   fasta_file = open(fasta_file, "a")
   SeqIO.write(record, fasta_file, "fasta")
   fasta_file.close()
   record.features = [f for f in record.features if f.type == "rRNA" or f.type == "tRNA"]
   fout = open(rnt_file, "a")
   fout.write("{0} - 0..{1}\n".format(record.description, len(record)))
   fout.write("{0} RNAs\n".format(len(record.features)))
   fout.write("Location\tStrand\tLength\tPID\tGene\tSynonym Code\tCOG\tProduct\n")
   strand = {1:'+', -1:'-'}
   for f in record.features:
       fout.write("{0}\n".format("\t".join([str(f.location.start)+".."+str(f.location.end),strand[f.strand],str(abs(f.location.start-f.location.end)),'-',f.qualifiers["locus_tag"][0],f.qualifiers["locus_tag"][0],"-",f.qualifiers["product"][0]])))
   fout.close()

r = SeqIO.parse(annotation_file, "gb")
for record in r:
   record.features = [f for f in record.features if f.type == "CDS"]
   fout = open(ptt_file, "a")
   fout.write("{0} - 0..{1}\n".format(record.description, len(record)))
   fout.write("{0} proteins\n".format(len(record.features)))
   fout.write("Location\tStrand\tLength\tPID\tGene\tSynonym Code\tCOG\tProduct\n")
   for f in record.features:
       fout.write("{0}\n".format("\t".join([str(f.location.start)+".."+str(f.location.end),strand[f.strand],str(abs(f.location.start-f.location.end)),'-',f.qualifiers["locus_tag"][0],f.qualifiers["locus_tag"][0],"-",f.qualifiers["product"][0]])))
   fout.close()
