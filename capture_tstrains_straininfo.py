#!/usr/bin/env python

#Captura linhagens-tipo de espécies de Paenibacillus descritas no StrainInfo

import requests
from bs4 import BeautifulSoup

file = open("paenibacillus_type.tab", "a")
file.write("Species" + "\t" + "Strain" + "\n")

web_page = "http://www.straininfo.net/strains/search?typeStrain=true&strainNumber=&exactStrain=true&taxon=paenibacillus&includeSubtaxa=true&sequence=&cultureId=&fullText=&firstResult="

for i in range(0,110,10):
    page_paenibacillus = requests.get(web_page + str(i))
    soup_paenibacillus = BeautifulSoup(page_paenibacillus.content, 'html.parser')
    strains = soup_paenibacillus.find_all("div", class_="strainnumber")
    for item in strains:
        species = item.find("span", class_="speciesname").get_text()
        strain = item.a.get_text()
        file.write(species + "\t" + strain + "\n")

file.close()
