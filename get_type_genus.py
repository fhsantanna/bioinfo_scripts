
#/usr/bin/env python

#Author: Dr. Fernando Hayashi Sant'Anna
#Date: 10/07/2018

#This script accesses bacterio.net(LPSN), captures type species code from a genus of interest, generating a table as output.

#Usage: python get_strains_lpsn.py <species> <output>

import re
from bs4 import BeautifulSoup
import requests
import sys

genus = sys.argv[1]
outfile_name = sys.argv[2]

url = "http://bacterio.net/" + genus.lower() + ".html"

outfile = open(outfile_name, "a")

page_url = requests.get(url)
soup = BeautifulSoup(page_url.content, 'html.parser')
text = soup.get_text()
text_ed = text.replace("\r\n", "\n").replace("\r", "\n").replace("(see also StrainInfo.net)", "")

#find type species
pattern_type_species = "Type species: ¤ ([A-Z][a-z]+ [a-z]+)"

species_type = re.findall(pattern_type_species, text_ed)[0]

#find accession from type species
genus_type = species_type.split(" ")[0]
epythet_type = species_type.split(" ")[1]

pattern_accession = " *{0} {1}.+\n.*\n *Type.+: *.+\..*\n.*\n *Sequence.+\: *(.+)\.".format(genus_type.title(), epythet_type)

accession = re.findall(pattern_accession, text_ed)[0]

outfile.write(genus + "\t" + species_type + "\t" + accession + "\n")

outfile.close()