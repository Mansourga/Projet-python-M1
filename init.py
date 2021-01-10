#!/bin/env python3
import os
import sys
from os import path
import pathlib
import re
import json
import pickle



class Initialisation:
    """ 
     Dans cette classe, nous allons faire le nettoyage des données puis créer 
     de nouveaux fichiers: article.json qui sera sous forme d'un dictionnaire avec comme clé (le numero de l'article)
     et comme values ( une liste contenant les auteurs de l'articles  associés à chaque clé du dictionnaire  )
    
    """
    
    mot = re.compile(r"\([^\)\(]*\)") #expression réguliere qui permet d'enlever tout ce qui est dans un parathese
    ext = r"**\*.abs"

    def __init__(self,chemin_articles,chemin_citations):

        self.chemin_articles=chemin_articles
        self.chemin_citations=chemin_citations
        
    def write(self,objet,nom_de_la_citation):

        """
        Cette methode permet de creer les fichier

        """

        with open(nom_de_la_citation, 'wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(objet)
    
  
    def load (self,nom_de_la_citation):   

        """
        Cette methode  permet de charger les fichiers

        """       
        with open(nom_de_la_citation, 'rb') as fichier:
            mon_depickler = pickle.Unpickler(fichier)
            recupere = mon_depickler.load()

            return recupere    

    def initialiser(self,chemin_articles,chemin_citations):

        with open(str(self.chemin_citations),"r") as data:        
            citation=[]
            for line in data:
                citation.append(line.split())

        self.write(citation, "citation.json")
        print("le fichier citation.json à été crée")
        self.load("citation.json")       
        print("le fichier citation.json à été charger") 
        les_abstras = [str(i) for i in pathlib.Path(self.chemin_articles).glob(Initialisation.ext)]  # stocke le chemin absolu des articles 
        
        dict_id_aut = dict()

        for fichier in les_abstras:
        
            with open(fichier,"r") as data:
                
                text = data.readlines()
                Author = [l for l in text if l.startswith("Author")==True][0] #[0] permet d'extraire le contenu de la liste
                Author_idx = text.index(Author) # prend l'index de l'auteur dans le text
                
                Author_idx+=1 
                while text[Author_idx].startswith(" ")==True: #cherche tant que toutes les lignes qui suivent commencent par un espace 
                    Author=Author+text[Author_idx] 
                    Author_idx+=1 
    
                
                Author=Author.replace("\n","") #supprime le retour à la ligne
                Author=re.sub(Initialisation.mot,"",Author)
                Author=Author.replace(" and ",",") 
                Author = Author.split(":")[1] #fait le split en utilisant les deux points
                
                if "(" in Author:
                    Author=Author.replace(Author.split("(")[1],"") #me fait la separation en fonction de (
                    Author=Author.replace("(","")  #puis  supprime la paranthese
                Author=Author.replace(",,",",")
                Author=Author.replace("  "," ")
                
                authors = [a.strip() for a in Author.split(",")]  #met les auteurs de chaque article dans  son propre liste une fois le split, strip():suprrime les espaces au debut
                

                num_ident=os.path.basename(fichier).split(".abs")[0] # split le nom de l'article en fonction du point
                dict_id_aut[num_ident]=[k for k in authors] #créé le dictionnaire avec comme keys:le numero d'identifiant et values:liste des auteurs de chaque article
        
        self.write(dict_id_aut,"article.json") 
        print("le fichier article.json à été crée")
        self.load("article.json")                                 # on peut le stocker dans une variable ou l'utiliser comme ça, utilise le print dans la fonction load pour voir
        print("le fichier article.json à été chargée")

        

