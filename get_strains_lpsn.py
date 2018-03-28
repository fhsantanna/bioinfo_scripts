#/usr/bin/env python

#Author: Dr. Fernando Hayashi Sant'Anna
#Date: 03/26/2018

#Captura código das linhagens e número acesso de espécies do gênero de interesse a partir do LPSN.
#This script accesses bacterio.net(LPSN), captures type strain codes and 16S rRNA accession numbers from species of a genus of interest, generating a table as output.

#Usage: python get_strains_lpsn.py <strain> <output>

import re
import sys

strain = sys.argv[1]
outfile_name = sys.argv[2]

#strain = input("Type the name of the genus of interest (e.g. escherichia): ")
#outfile_name = input("Type the name of the output file: ")

url = "http://bacterio.net/" + strain.lower() + ".html"

outfile = open(outfile_name, "a")
outfile.write("Species" + "\t" + "Strain" + "\t" + "Accession number" + "\n")

from bs4 import BeautifulSoup
import requests

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
text = soup.get_text()
text_ed = text.replace("\r\n","\n")

pattern = " *({0}.+)\n.*\n *Type.+\.net\) *(.+)\..*\n.*\n *Sequence.+\: *(.+)\.".format(strain.title())
lista = re.findall(pattern, text_ed)

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
        outfile.write(sname + "\t" + strain + "\t" + anumber16S + "\n")

outfile.close()
