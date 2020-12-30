import os
import sys
from os import path
import pathlib
import re
import json
import pickle
import time
#print(os.path.isfile(r"C:\Users\gayem\Downloads\hep-th-citations\hep-th-citations"))
"""
ecriture des fichier
"""

def write(fichier,nom): #fichier c'est juste une variabe qui prendra soit dict_id_aut soit citation et nom: c'est le nom qu'on veut donner à nos fichiers
    """
    cette partie mise en commentaire est là où je trouve des difficultés pour le chemin absolu avec des \\.
        Ci dessous, est le code utilisé mais ne fonctionne pas 
    data=path.dirname(os.path.abspath(__file__)) #je voulais recuperer ici le chemin absolu du repertoire de travail
    chemin=path.join(data,'donnée',nom) # cette partie fait comme suit: data\donnée\nom 
    with open(chemin,"w") as data:
        return data.write(json.dumps(fichier))
    """
    

    with open(r"C:\Users\gayem\Desktop\tp_charbon\projet_code\{}".format(nom),'wt') as data:
        return data.write(json.dumps(fichier))


mot= re.compile(r"\([^\)\(]*\)")#re.compile(r'\([^)]*\)')
def initialiser(articles,citations):
    with open(str(citations),"r") as data:
        citation=[]
        for line in data:
            citation.append(line.split())
    write(citation,"citation.json") # c'est à ce niveau où on fait l'appel de la fonction write pour creér le fichier citation.json
    #print(citation)
    ext=r"**\*.abs"
    les_abstras=[str(i) for i in pathlib.Path(articles).glob(ext)]

    #print(les_abstras)
    dict_id_aut=dict()
    for fichier in les_abstras:
        with open(fichier,"r") as data:
            text=data.readlines()
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
            
            Author=Author.replace("..",",")
            #print(Author)
            Author=Author.replace(" and ",",") #and (line.replace("Authors:", "") and line.replace("Author:","")
            Author = Author.split(":")[1] #fait le split en utilisant les deux points et [1],i.e que je vais prendre l'indexe 1
            Author=Author.replace(",,",",")
            #Author = Author.split("(")
            if "("  in Author:
                Author=Author.replace(Author.split("(")[1],"") #me fait la separation en fonction de (
                Author=Author.replace("(","")  #puis  supprime la paranthese
            if ")"  in Author:
                Author=Author.replace(Author.split(")")[1],"")
                Author=Author.replace(")","")
            Author=Author.replace(";","")
            Author=Author.replace("&",",")
            Author=Author.replace("&",",")      
            authors = [a.strip() for a in Author.split(",")]  #met les auteur de chaque article dans  son propre liste une fois le split, strip():suprrime les espaces au debut
            #print(str(authors))
            num_ident=os.path.basename(fichier).split(".abs")[0] # split le nom de l'article en fonction du point
            dict_id_aut[num_ident]=[k for k in authors] #créé la dictionnaire avec comme keys:ident et val:liste des auteurs de chaque article
    write(dict_id_aut,"article.json")
    
    #print(dict_id_aut["0304140"])       #print(num_ident)
    """
    fichier=open("articles.json","wt")
    fichier.write(json.dumps(dict_id_aut))
    fichier.close()
    fichier2=open("citation.json","wt")
    fichier2.write(json.dumps(citation))
    fichier2.close()
    """

    
    
        
        
    

            


    
        