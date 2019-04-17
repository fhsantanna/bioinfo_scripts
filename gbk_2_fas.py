from Bio import SeqIO
import sys

#usage: gbk_2_fas.py < cromossome.gbk


for seq_record in SeqIO.parse(sys.stdin, "genbank"):
	with open("{}.fasta".format(str(seq_record.id)), "w") as output_handle:
		count = SeqIO.write(seq_record, output_handle, "fasta")

print("Converted %i records" % count)
