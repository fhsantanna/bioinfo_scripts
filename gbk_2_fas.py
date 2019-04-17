from Bio import SeqIO
import sys

#usage: gbk_2_fas.py < cromossome.gbk


for seq_record in SeqIO.parse(sys.stdin, "genbank"):
	with open("{}.fasta".format(str(seq_record.description)), "w") as output_handle:
		output_handle.write(">%s\n%s\n" % (
            seq_record.description,
            seq_record.seq))
print("Converted {} records".format(seq_record.id))
