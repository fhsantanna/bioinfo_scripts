# -*- coding: utf-8 -*-
"""
Author: Fernando Hayashi Sant'Anna
Data: 19-05-2018
Calcula a precisão, tx de fn, tx de fp, vp, fp, vn, fn para a matriz de ani,
Para utilizar, colocar o nome das tipo na lista.
Uso: python ani_stats.py
"""

import pandas as pd

ani = pd.read_csv("ANIb_percentage_identity.tab", sep="\t")
output = "tabela_estat.txt"

with open(output, "a+") as f:
        f.write("type_strain" + "\t" + "vp_strain" + "\t" + "fp_strain" + "\t" + "vn_strain" + "\t" + "fn_strain" + "\t" + "precision_strain" + "\t" + "tx_fn_strain" + "\t" + "tx_fp_strain" + "\n")
        
lista = ["GCF_000236805.1_Paenibacillus_peoriae_KCTC_3763", "GCF_000217775.1_Paenibacillus_polymyxa_ATCC_842", "GCF_000316285.1_Paenibacillus_sonchi_X19-5"] #adicionar aqui as tipos

def precision_calc(vp, fp):
    prec = (vp / (vp + fp)) * 100
    return prec

def tx_fn_calc(vp, fn):
    tx_fn = (fn / (fn + vp)) * 100
    return tx_fn

def tx_fp_calc(fp, vn):
    tx_fp = (fp / (fp + vn)) * 100
    return tx_fp

for type_strain in lista:
    strain_table = ani[["Index", type_strain]] #fica com coluna da tipo
    
    specific_name = type_strain.split("_")[3]
    rows_strain = strain_table[strain_table["Index"].str.contains(specific_name)] #fica com linhas contendo nome especìfico
    rows_not_strain = strain_table[~strain_table["Index"].str.contains(specific_name)] #fica com linhas sem nome específico   
     
    #calculo vp
    vp_temp = rows_strain[(rows_strain[type_strain] >= 0.95)].count() - 1
    vp_strain = vp_temp[type_strain]

    
    #calculo fp
    fp_temp = rows_strain[(rows_strain[type_strain] < 0.95)].count()
    fp_strain = fp_temp[type_strain]
    
   
    #calculo vn
    vn_temp = rows_not_strain[(rows_not_strain[type_strain]) < 0.95].count()
    vn_strain = vn_temp[type_strain]

    #calculo fn
    fn_temp = rows_not_strain[(rows_not_strain[type_strain]) >= 0.95].count()
    fn_strain = fn_temp[type_strain]
   
    #precisao
    prec_strain = precision_calc(vp_strain, fp_strain)
    
    #taxa fn
    tx_fn_strain = tx_fn_calc(vp_strain, fn_strain)

    #taxa fp
    tx_fp_strain = tx_fp_calc(fp_strain, vn_strain)
    
    print(type_strain)
    
    with open(output, "a+") as f:
        f.write(type_strain + "\t" + str(vp_strain) + "\t" + str(fp_strain) + "\t" + str(vn_strain) + "\t" + str(fn_strain) + "\t" + str(prec_strain) + "\t" + str(tx_fn_strain) + "\t" + str(tx_fp_strain) + "\n")        
        
