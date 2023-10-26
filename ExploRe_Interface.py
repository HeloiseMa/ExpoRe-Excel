# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 11:26:43 2023
Module ExploRe_Interface
@author: heloise
"""
# import ExploRe_Calcul
import ExploRe_Graph

import tkinter as tk
from tkinter import ttk

# Variables et fonctions entry vers calcul

# options de base
nb_parametres = 1
nb_resultats = 1

# entry des paramteres

def calculer_tout():
    nom_parametre1 = entry_nom.get()
    val_cellule = entry_loc.get()
    par_min1 = entry_min.get()
    par_max1 = entry_max.get()
    nb_calculs = entry_iter.get()
    nom_resultat1= entry_nom_res.get()
    res_min1 = entry_min_res.get()
    res_max1 = entry_max_res.get()
    #graph.ExploRe_Graph.show()
    print( nom_parametre1, val_cellule, par_min1, par_max1, nb_calculs )

# Interface graphique Tkinter
root = tk.Tk()
root.title("ExploRe xlsx")
root.geometry("800x400")

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
frame = tk.Frame(root)
frame.pack(padx=5, pady=5)

frame_param = tk.LabelFrame(frame, text = "Paramètres") 
frame_param.grid(sticky="w", column = 0, row = 0, padx = 10, pady = 10)

label_nom = label = tk.Label(frame_param, text = "Nom du paramètre") 
label_nom.grid(column = 0, row =0)

label_loc = tk.Label(frame_param, text = "Localisation de la\ncellule dans excel") 
label_loc.grid(column = 1, row =0)

label_min = tk.Label(frame_param, text = "Valeur minimale") 
label_min.grid(column = 2, row =0)

label_max = tk.Label(frame_param, text = "Valeur maximale") 
label_max.grid(column = 3, row =0)

label_iter = tk.Label(frame_param, text = "Nombre d'itérations") 
label_iter.grid(column = 4, row =0)

for i in range (nb_parametres):
    entry_nom = tk.StringVar()
    entry_nom = tk.Entry(frame_param, width=40 )
    entry_nom.insert(0, 'Surface de fenêtres')
    entry_nom.grid(column = 0, row = 1+i)
    
    entry_loc = tk.StringVar()
    entry_loc = tk.Entry(frame_param, width=18)
    entry_loc.insert(0, 'K18')
    entry_loc.grid(column = 1, row = 1+i)
    
    entry_min = tk.DoubleVar()
    entry_min = tk.Entry(frame_param, width=18)
    entry_min.insert(0, 500.0)
    entry_min.grid(column = 2, row = 1+i)
    
    entry_max = tk.DoubleVar()
    entry_max = tk.Entry(frame_param, width=18)
    entry_max.insert(0, 1000.0 )
    entry_max.grid(column = 3, row = 1+i)

    entry_iter = tk.Spinbox(frame_param, from_= 2, to = 5 )
    entry_iter.grid(column = 4, row = 1+i)

for widget in frame_param.winfo_children():
    widget.grid_configure(padx=2, pady=2)
    
 
# Saisie résulats

frame_result = tk.LabelFrame(frame, text = " Résultats") 
frame_result.grid(sticky="news", column = 0, row = 12, padx = 10, pady = 10) 

label_nom_res = label = tk.Label(frame_result, text = "Nom du résultat")
label_nom_res.grid(column = 0, row = 13)

label_loc_res = tk.Label(frame_result, text = "Localisation de la\ncellule dans excel") 
label_loc_res.grid(column = 1, row = 13)

label_min_res = tk.Label(frame_result, text = "Valeur minimale") 
label_min_res.grid(column = 2, row = 13)

label_max_res = tk.Label(frame_result, text = "Valeur maximale") 
label_max_res.grid(column = 3, row = 13)

for j in range (nb_resultats):
    entry_nom_res = tk.StringVar()
    entry_nom_res = tk.Entry(frame_result, width=40 )
    entry_nom_res.insert(0, 'Besoins de chauffage')
    entry_nom_res.grid(column = 0, row = 14+j)
    
    entry_loc_res = tk.StringVar()
    entry_loc_res = tk.Entry(frame_result, width=18)
    entry_loc_res.insert(0, 'E93')
    entry_loc_res.grid(column = 1, row = 14+j)
    
    entry_min_res = tk.DoubleVar()
    entry_min_res = tk.Entry(frame_result, width=18)
    entry_min_res.insert(0, 0.5)
    entry_min_res.grid(column = 2, row = 14+j)
    
    entry_max_res = tk.DoubleVar()
    entry_max_res = tk.Entry(frame_result, width=18)
    entry_max_res.insert(0, 50.2)
    entry_max_res.grid(column = 3, row = 14+j)
    
for widget in frame_result.winfo_children():
    widget.grid_configure(padx=2, pady=2)
        

    
# Bouton pour valider la saisie

bouton = tk.Button(root, text="Lancer les calculs", bg="red", fg = 'white', command = calculer_tout,  width=30,  )
bouton.pack(padx=20, pady=10)

"""    
# Widget Graphique interactif de coordonnées parallèles du module graph, mais à voir car graph HTML
graph_widget = go.FigureWidget(graph.ExploRe_Graph)
graph_widget_widget = graph_widget.show()
graph_widget_widget.pack()
"""

root.mainloop()