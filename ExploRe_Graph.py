# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 15:51:14 2023
Module ExploRe_Graph
@author: heloise
"""
# import ExploRe_Calcul
# import ExploRe_Interface

# Librairies pour les graphiques
import pandas as pd
import openpyxl
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots


# Tableur source à transformer vers excel xlsx
# df = pd.read_xlsx("ExploResultat.xlsx")

df = pd.read_csv("TestGraph.csv") # pour le test

# Variables du graph
# Définir les variables d'entrée pour étude paramétrique à lier avec la saisie Tkinter
parametre1 = 'fenetreTOT'
parametre2 = 'facade1'
parametre3 = 'isol_mur1'
parametre4 = 'isol_toiture1'
parametre5 = 'fenetreS'

# Définir les variables de résultats
resultat1 = 'Iouv'
resultat2 = 'Icomp'
resultat3 = 'Iisol indice disolation'
resultat4 = 'ISCH indice de surchauffe'
resultat5 = 'BCH besoins de chauffage'

# parametres (2 à 5 max)
nom_parametre1 = 'fenetreTOT'
par_min1 = 200
par_max1 = 500

# résultats (2 à 5 max)
nom_resultat1 = 'Besoins de chauffage'
res_min1 = 1
res_max1 = 300

# Diagramme de coordonnées parallèles (nb paramètres en boucle ?)
graph = go.Figure(data = go.Parcoords(
        line = dict(color = df['resultat5'],
                   colorscale = 'Electric',
                   showscale = True,
                   cmin = res_min1,
                   cmax = res_max1),
        dimensions = list([
            dict(range = [par_min1,par_max1],
                 label = nom_parametre1 , values = df[ 'parametre1' ]),
            dict(range = [res_min1, res_max1],
                 label = nom_resultatA , values = df[ 'resultat1'])
        ]
)))
graph.show()


# Afficher et sauvegarder les graphs
pio.renderers.default = 'browser'
pio.renderers.default = 'svg'
