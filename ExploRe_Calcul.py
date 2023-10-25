# -*- coding: utf-8 -*-
"""
ExploRe_Calcul boucle avec Excel
Programme principal
@author: Heloise
"""
 # import ExploRe_Interface

import pandas as pd
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo


# Charger le fichier Excel
wb = Workbook()
ws = wb.active
nom_fichier = 'BBPapoose12.xlsx'
table_entree = openpyxl.load_workbook(nom_fichier)
feuille = table_entree

# Définir les variables d'entrée pour étude paramétrique à lier avec la saisie Tkinter
parametre1 = 'fenetreTOT'
parametre2 = 'facade1'
parametre3 = 'isol_mur1'
parametre4 = 'isol_toiture1'
parametre5 = 'fenetreS'

# Définir les variables de résultats
resultatA = 'Iouv'
resultatB = 'Icomp'
resultatC = 'Iisol indice disolation'
resultatD = 'ISCH indice de surchauffe'
resultatE = 'BCH besoins de chauffage'

# Lire la valeur d'une cellule spécifique (par exemple, cellule A1)
val_cellule = 'A1'
valeur_init = feuille[ val_cellule ].value

# Modifier la valeur de la cellule  alcul à refaire
increment = (parametre_max - parametre_min) / nb_calculs # valeur à additionner à la valeur de base
for k in range ( nb_calculs ):
    valeur_incremente = parametre_min + increment

# Boucler pour produire les variables
for parametre1 in range (increment):
    feuille['A1'] = valeur_incremente
    table_resultat.append [parametre1, parametre2, parametre3, parametre4, parametre5, resultatA, resultatB, resultatC, resultatD, resultatE]

ws.add_table(tab)
wb.save("table.xlsx")

# Sauvegarder le fichier Excel avec les résultats # Créer une table excel des résultats
nom_fichier_resultat = "ExploResultat.xlsx"
classeur.save(nom_fichier_resultat)



