#/usr/bin/env python

#Transforma texto do LPSN (copiar da página) em tabela contendo nome da espécie, linhagens e número de acesso do 16S.

import re

infilename = "paenibacillus_lpsn.txt"

with open(infilename, "r") as infile:
    infile_content = infile.read()

pattern = "(Paenibacillus.*)\nType strain:.*\.net\)(.*)\nSequence.*: (.*)."
lista = re.findall(pattern, infile_content)

for species in (range(0,len(lista))):
    strains = lista[species][1].split("=")
    anumber16S = lista[species][2]
    for n in range(0,len(strains)):
        name_split = lista[species][0].split(" ")
        strain = strains[n]
        if name_split[2] != "subsp.":
            sname = " ".join(name_split[0:2])
        else:
            sname = " ".join(name_split[0:4])
        print(sname + "\t" + strain + "\t" + anumber16S)
