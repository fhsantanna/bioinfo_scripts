import sys
import pandas as pd

genes_bed = sys.argv[1]
genome_bed = sys.argv[2]
out_file = sys.argv[3]

genes = pd.read_csv(genes_bed, sep="\t", header=None)
genes.columns = ["accession", "start", "end", "locus", "score", "strand"]
genes["gene_midpoint"] = (genes["end"] + genes["start"])/2

genome = pd.read_csv(genome_bed, sep="\t", header=None)
genome.columns = ["accession", "length"]
genome["midpoint"] = genome["length"] / 2

distances = genes[["accession", "locus", "gene_midpoint"]]
distances["distance_from_PII"] = abs(distances["gene_midpoint"] - genome["midpoint"][0])

distances.to_csv(out_file)