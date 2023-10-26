# -*- coding: utf-8 -*-
"""
ExploRe_Calcul boucle avec Excel
Programme principal
@author: Heloise
"""
import ExploRe_Interface

import pandas as pd
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

# Charger le fichier Excel
wb = Workbook()
sheet = wb.active
nom_fichier = 'BBPapoose12_bur.xlsx'
table_entree = openpyxl.load_workbook(nom_fichier)
feuille = table_entree

# Définir les variables d'entrée pour l'étude paramétrique à lier avec la saisie Tkinter
nom_parametre1 = entry_nom.ExploRe_Interface.get()
val_cellule = entry_loc.ExploRe_Interface.get()
par_min1 = entry_min.ExploRe_Interface.get()
par_max1 = entry_max.ExploRe_Interface.get()
nb_calculs1 = entry_iter.ExploRe_Interface.get()

# Définir les variables de résultats
nom_resultat1= entry_nom_res.get()
res_min1 = entry_min_res.get()
res_max1 = entry_max_res.get()

# Lire la valeur d'une cellule spécifique (par exemple, cellule A1)

# Boucler pour produire les variables
increment1 = (par_max1 - par_min1) / nb_calculs1 # valeur à additionner à la valeur de base parametre1 = par_min1
for parametre1 in range ( nb_calculs ):
    feuille[val_cellule].value = par_min1 + increment1
    
    table_resultat.append [parametre1, parametre2, parametre3, parametre4, parametre5, resultat1, resultat2, resultat3, resultat4, resultat5]


# Sauvegarder le fichier Excel avec les résultats # Créer une table excel des résultats
sheet.add_table()
nom_fichier_resultat = "ExploResultat.xlsx"
wb.save(nom_fichier_resultat)
wb.close()




