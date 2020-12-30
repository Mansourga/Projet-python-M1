import init
#import numpy
import json
import init
from pprint import pprint

cita=init.load("citation.json") 

#print(cita[0][1])
article=init.load("article.json")
#print(article.values())

#print(article['0304262'])

def les_articles_de_l_auteur(nom): # C'est pour recuperer la liste des articles ecrits par un auteur donné
    """ 
    Je recupere les articles ecrits par un auteur donné
    """
    keys_de_auteur=[]
    for a,b in article.items(): #a:keys(), b:values()
        #print(b)
        for j in b:
            #print(j)
            if nom ==j: #regarde si le nom de l'auteur donné se trouve dans les values de notre dictionnaire
                keys_de_auteur.append(a) # si if est vrai, je recupere le numéro de l'article dont il a ecrit
    return keys_de_auteur

#print(les_articles_de_l_auteur('Cumrun Vafa'))
def article_réferncé(nom):
    """
    je recupere ici les references de l'article de l'auteur donné 

    """
    cite=[]
    for m in les_articles_de_l_auteur(nom):
        for l in cita:
            if l[0]==m: #regarde  dans les citation si son article fait reference à un autre article 
                cite.append(l[1]) # je recupere le numero de l'article referencé par l'auteur 
            
    return cite

#print(cité('Cumrun Vafa'))
def liste_des_auteurs_cités(nom):
    citation=[]
    for i in article_réferncé(nom):
        for a,b in article.items():
            if i==a and nom not in a: #je regarde si les artcles referencés par l'auteur correspondent aux numeros des articles afin de recuperer les auteurs de ces artcles 
                for l in b: #j'ai fait ça car on des listes de liste et pour le faire en une liste je recupere tout ce qui est à l'interieur de notre liste
                    citation.append(l) # c'est ici où je recupere les auteurs cités par l'aueteur donné
    les_noms=sorted(list(set(citation)))
    if nom in les_noms:
        les_noms.remove(nom)
     
    pprint(les_noms) #j'ai utilisé set pour eviter le doublon des noms : set est <-> à l'union en maths
    print(len(les_noms))    
#liste_des_auteurs_cités()





"""
Dans cette partie, je fais sortir la liste des auteurs qui ont cité un auteur donné. C'est pas demandé dans le projet
def cité(nom):
    cite=[]
    for m in les_articles_de_l_auteur(nom):
        for l in cita:
            if l[1]==m:
                cite.append(l[0])
    return cite


#print(cité('Cumrun Vafa'))
def citatio(nom):
    citation=[]
    for i in cité(nom):
        for a,b in article.items():
            if i==a and nom not in a:
                citation.append(b)
    return citation

print(citatio('Andreas Nyffeler'))
"""



