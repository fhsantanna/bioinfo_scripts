from Bio import SeqIO
import sys

#usage: gbk_split.py < assembly.gbk
#source: http://seqanswers.com/forums/showthread.php?t=18525

for rec in SeqIO.parse(sys.stdin, "genbank"):
   SeqIO.write([rec], open(rec.id + ".gbk", "w"), "genbank")
