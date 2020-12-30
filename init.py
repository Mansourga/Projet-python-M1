#!/usr/bin/env python3

import os
import sys
from os import path
import pathlib
import re
import json
import pickle
import time
#print(os.path.isfile(r"C:\Users\gayem\Downloads\hep-th-citations\hep-th-citations"))

mot = re.compile(r"\([^\)\(]*\)")#re.compile(r'\([^)]*\)')

def write(objet, nom): #fichier c'est juste une variabe qui prendra soit dict_id_aut soit citation et nom: c'est le nom qu'on veut donner à nos fichiers

    with open(nom, 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(objet)

"""
def récupérer(nom_fichier):              # récupere ou charger le fichier , # il faut passer le nom du fichier, (cette fonction je l ai pas utiliser)
    with open(str(nom_fichier), 'rb',encoding="utf_8") as fichier:
        mon_depickler = pickle.Unpickler(fichier)
"""

def load(nom_fichier):                  # lecture de fichier (contenant la charge du fichier aussi qui sera faite d'abord)
    with open(nom_fichier, 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        recupere = mon_depickler.load()
        #print(recupere)
        return recupere                    



def initialiser(articles,citations):
    with open(str(citations),"r") as data:         # citation c'est fichier on donne son chemin absolue directement
        citation=[]
        for line in data:
            citation.append(line.split())

    write(citation, "citation.json")
    print("le fichier citation.json à été crée")
    load("citation.json")       # on peut le stocker dans une variable ou l'utiliser comme ça, utilise le print dans la fonction load pour voir
    print("le fichier citation.json à été charger")
    #print(citation)
    ext = r"**\*.abs"
    les_abstras = [str(i) for i in pathlib.Path(articles).glob(ext)]  # return le chemin absolu des articles 
    #files= os.listdir(str(articles))
    #for i in files:
    #  data=os.listdir(str(articles))
        
    #print(les_abstras)
    dict_id_aut = dict()

    for fichier in les_abstras:
        
        with open(fichier,"r") as data:
            
            text = data.readlines()
            Author = [l for l in text if l.startswith("Author")==True][0] #[0] me permet d'extraire le contenu de la liste
            Author_idx = text.index(Author) #je prend l'index de l'auteur dans le text
            Author_idx+=1 
            while text[Author_idx].startswith(" ")==True: #cherche tant que toutes les lignes qui suivent commencent par un espace 
                Author=Author+text[Author_idx] #rajoute dans la ligne de l'auteur la ligne qui suit sur une meme ligne
                Author_idx+=1 
            #print(Author)
            
            Author=Author.replace("\n","") #supprime le retour à la ligne
            #Author=Author.replace("( ","")
            #Author=Author.replace(" )","")
            Author=re.sub(mot,"",Author)
            #print(Author)
            Author=Author.replace(" and ",",") #and (line.replace("Authors:", "") and line.replace("Author:","")
            Author = Author.split(":")[1] #fait le split en utilisant les deux points et [1],i.e que je vais prendre l'indexe 1
            #Author = Author.split("(")
            
            if "(" in Author:
                Author=Author.replace(Author.split("(")[1],"") #me fait la separation en fonction de (
                Author=Author.replace("(","")  #puis  supprime la paranthese
            Author=Author.replace(",,",",")
            Author=Author.replace("  "," ")
            authors = [a.strip() for a in Author.split(",")]  #met les auteurs de chaque article dans  son propre liste une fois le split, strip():suprrime les espaces au debut
            
            #print(str(authors))
            num_ident=os.path.basename(fichier).split(".abs")[0] # split le nom de l'article en fonction du point
            dict_id_aut[num_ident]=[k for k in authors] #créé la dictionnaire avec comme keys:ident et val:liste des auteurs de chaque article
    
    write(dict_id_aut,"article.json") 
    print("le fichier article.json à été crée")
    load("article.json")                                 # on peut le stocker dans une variable ou l'utiliser comme ça, utilise le print dans la fonction load pour voir
    print("le fichier article.json à été chargée")



    #print(dict_id_aut)       
    #fichier1=open("article.json","wt")
    #fichier1.write(json.dumps(dict_id_aut))
    #print("le fichier article à été crée et le chemin est :  {}".format(os.path.abspath("article.json")))
    #fichier1.close()
    

