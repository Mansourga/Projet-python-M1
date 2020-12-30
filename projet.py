
"""
import pandas as pd
data=pd.read_csv("https://math.univ-angers.fr/~ducrot/pyds1/data/hep-th-abs.tar.gz")
print(data)


data=pd.read_csv("hep-th-citations")
print(data)
"""

import numpy as np
import tarfile
import os
import json
#tar = tarfile.open("hep-th-abs.tar.gz")
#tar=tarfile.open("hep-th-citations.tar.gz")
#tar.extractall()
#tar.close()
#Data = np.loadtxt(tar,decodage= "utf_8")

import re
mot= re.compile(r"\([^\)\(]*\)")#re.compile(r'\([^)]*\)')

auteur=[]
files= os.listdir(r"C:\Users\gayem\Desktop\tp charbon\projet")

for i in files:
    data= os.listdir(r"C:\Users\gayem\Desktop\tp charbon\projet\{}".format(i))
    for j in data:
        dict_id_aut=dict()
        with open(r"C:\Users\gayem\Desktop\tp charbon\projet\{}\{}".format(i,j),"r") as f:

            text=f.readlines()
            
            Author=[l for l in text if l.startswith("Author")==True][0] #[0] me permet d'extraire le contenu de la liste
            Author_idx=text.index(Author) #je prend l'index de l'auteur dans le text
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
            #print(Author)
            authors = [a.strip() for a in Author.split(",")]  #met les auteur de chaque article dans  son propre liste une fois le split, strip():suprrime les espaces au debut
            #print(authors)
            num_ident=j.split(".")[0] # split le nom de l'article en fonction du point
            dict_id_aut[num_ident]=[k for k in authors] #créé la dictionnaire avec comme keys:ident et val:liste des auteurs de chaque article
            #print(num_ident)
            #print(dict_id_aut["0304256"])
            with open(r"auteur.txt", "w") as fichier2:
            
                fichier2.write(json.dumps(dict_id_aut))
                fichier2.close()

        
            
