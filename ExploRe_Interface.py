# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:26:43 2023
Module ExploRe_Interface
@author: heloise
"""
# import ExploRe_Calcul
# import ExploRe_Graph

import tkinter as tk
from tkinter import ttk
import plotly.graph_objects as go


# Variables et fonctions entry vers calcul


# options de base
nb_parametres = 5
nb_resultats = 5

# entry des paramteres

def calculer_tout():
    nom_parametre = entry_nom.get()
    val_cellule = entry_loc.get()
    parametre_min = entry_min.get()
    parametre_max = entry_max.get()
    nb_calculs = entry_iter.get()
    print( nom_parametre, val_cellule, parametre_min, parametre_max, nb_calculs )

# Interface graphique Tkinter
root = tk.Tk()
root.title("ExploRe xlsx")
root.geometry("800x600")

# Menu
def preferences():
    showinfo("Préférences", "Nombre de paramètres, nombre de résultats, chemin du fichier excel source")

menubar = tk.Menu(root)
menu = tk.Menu(menubar)
menu.add_command(label="Préférences", command = preferences)
menu.add_separator()
menu.add_command(label="Quitter", command = root.quit)
menubar.add_cascade(label="Fichier", menu = menu)

# Saisie paramètres
frame_param = tk.Frame(root)
frame_param.grid()

label_par = tk.LabelFrame(frame_param, text = "Paramètres") 
label_par.grid(column = 0, row = 0, padx = 10, pady = 10)

label_nom = label = tk.Label(frame_param, text = "Nom du paramètre") 
label_nom.grid(column = 0, row =0)

label_loc = tk.Label(frame_param, text = "Localisation de la case") 
label_loc.grid(column = 1, row =0)

label_min = tk.Label(frame_param, text = "Valeur minimale") 
label_min.grid(column = 2, row =0)

label_max = tk.Label(frame_param, text = "Valeur maximale") 
label_max.grid(column = 3, row =0)

label_iter = tk.Label(frame_param, text = "Nombre d'itérations") 
label_iter.grid(column = 4, row =0)

for i in range (nb_parametres):
    entry_nom = tk.StringVar()
    entry_nom = tk.Entry(frame_param, width=23, text = 'Surface de fenêtres' )
    entry_nom.grid(column = 0, row = 1+i)
    
    entry_loc = tk.StringVar()
    entry_loc = tk.Entry(frame_param, width=23, text = 'A1' )
    entry_loc.grid(column = 1, row = 1+i)
    
    entry_min = tk.DoubleVar()
    entry_min = tk.Entry(frame_param, width=23, text = 0.23 )
    entry_min.grid(column = 2, row = 1+i)
    
    entry_max = tk.DoubleVar()
    entry_max = tk.Entry(frame_param, width=23, text = 45.52 )
    entry_max.grid(column = 3, row = 1+i)

    entry_iter = tk.Spinbox(frame_param, from_= 2, to = 5 )
    entry_iter.grid(column = 4, row = 1+i)
    
"""    
# Saisie résulats

label_res = tk.Label(root, text = "Résultats à ExploRer :") 
label_res.grid(column = 0, row = 12)

label_nom = label = tk.Label(root, text = "Nom du résultat") 
label_nom.grid(column = 1, row = 13)

label_loc = tk.Label(root, text = "Localisation de la case") 
label_loc.grid(column = 2, row = 13)

label_min = tk.Label(root, text = "Valeur minimale") 
label_min.grid(column = 3, row = 13)

label_max = tk.Label(root, text = "Valeur maximale") 
label_max.grid(column = 4, row = 13)


for j in range (nb_resultats):
    entry_nom.grid(column = 1, row = 14+j)
    entry_loc.grid(column = 2, row = 14+j)
    entry_min.grid(column = 3, row = 14+j)
    entry_max.grid(column = 4, row = 14+j)
"""
    
# Bouton pour valider la saisie
bouton = tk.Button(root, text="Lancer les calculs", bg="red", fg = 'white', command = calculer_tout )
bouton.grid(column = 0, row = 20)
    
# Widget Graphique interactif de coordonnées parallèles du module graph, mais à voir car graph HTML
"""
graph_widget = go.FigureWidget(graph.ExploRe_Graph)
graph_widget_widget = graph_widget.show()
graph_widget_widget.grid(column = 1, row =40, expand=True)
"""

root.mainloop()