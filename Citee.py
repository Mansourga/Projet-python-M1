import os
import sys
from os import path
import pathlib
import re
import json
import pickle
import time
import initi
from pprint import pprint

class Communaute:

    def __init__(self,nom):
        self.nom=nom  
        self.cita=initi.Initialisation.load(self,"citation.json")
        self.article=initi.Initialisation.load(self,"article.json")
        
        #super().__init__(self)
        #self.cita=initi.Initialisation.load(self, "citation.json")
        #print(self.cita)
        #self.article=initi.Initialisation.load(self,"article.json")




    """
    def __init__(self,nom):
        self.nom=nom
        cita=initi.Initialisation.load(self, nom_de_la_citation)
        article=initi.Initialisation.load("article.json")
    """
    def les_articles_de_l_auteur(self,nom):
        self.nom=nom
        keys_de_auteur=list()
        for a,b in self.article.items(): #a:keys(), b:values()
            #print(b)
            for j in b:
                if j == nom:#regarde si le nom de l'auteur donné se trouve dans les values de notre dictionnaire
                    #print(a)
                    keys_de_auteur.append(a) # si if est vrai, je recupere le numéro de l'article dont il a ecrit
          
        return keys_de_auteur



    def article_réferncé(self,nom):
        """
        je recupere ici les references de l'article de l'auteur donné 
        """
        cite=list()
        #les_articles_de_l_auteur= self.les_articles_de_l_auteur(nom)
        #print(les_articles_de_l_auteur)
        #cita= self.cita
        for m in self.les_articles_de_l_auteur(nom):
            #print(m)
            for l in self.cita:
                #print(l)
                if l[0]==m: #regarde  dans les citation si son article fait reference à un autre article 
                    cite.append(l[1]) # je recupere le numero de l'article referencé par l'auteur 
            #        print(cite)
                
        return cite
        
    
    def liste_des_auteurs_cités(self,nom):
        citation=list()
        article_re=self.article_réferncé(nom)
        for i in article_re :
            for a,b in self.article.items():
                if i==a and nom not in a: #je regarde si les artcles referencés par l'auteur correspondent aux numeros des articles afin de recuperer les auteurs de ces artcles 
                    for l in b: #j'ai fait ça car on des listes de liste et pour le faire en une liste je recupere tout ce qui est à l'interieur de notre liste
                        citation.append(l) # c'est ici où je recupere les auteurs cités par l'aueteur donné
        les_noms=sorted(list(set(citation)))
        if nom in les_noms:
            les_noms.remove(nom)
        print(les_noms)
        
        #pprint(les_noms) #j'ai utilisé set pour eviter le doublon des noms : set est <-> à l'union en maths
        #print(len(les_noms))    
    #liste_des_auteurs_cités()
