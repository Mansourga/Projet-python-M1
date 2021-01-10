#!/bin/env python3
import os
import sys
from os import path
import pathlib
import re
import json
import pickle
import time
import init
from pprint import pprint


class Communaute:
 
    def __init__(self,nom):
        
        self.nom=nom  
        self.cita=init.Initialisation.load(self,"citation.json")
        self.article=init.Initialisation.load(self,"article.json")
        

    def les_articles_de_l_auteur(self,nom):
        """
        ici, on recupere les articles ecrits par l'auteur 

        """
        self.nom=nom
        keys_de_auteur=list()
        for a,b in self.article.items():  
            for j in b:  
                if j == nom:#regarde si le nom de l'auteur donné se trouve dans les values de notre dictionnaire
                    keys_de_auteur.append(a) # si if est vrai, on recupere le numéro de l'article dont il a ecrit
          
        return keys_de_auteur



    def article_réferncé(self,nom):
        """
        je recupere ici les references de l'article de l'auteur donné 
        
        """
        cite=list()
        for m in self.les_articles_de_l_auteur(nom):
            for l in self.cita:

                if l[0]==m: #regarde  dans les citation si son article fait reference à un autre article 
                    cite.append(l[1]) #  recupere le numero de l'article referencé par l'auteur 

                
        return cite
        
    
    def liste_des_auteurs_cités(self,nom):
        """
        Ici, on recupere  la liste des auteurs cité par l'auteur en question

        """
        citation=list()
        article_re=self.article_réferncé(nom)
        for i in article_re :
            for a,b in self.article.items():
                if i==a and nom not in a: # on regarde si les artcles referencés par l'auteur correspondent aux numeros des articles
                    for l in b: # on fait ça car on des listes de liste et pour le faire en une liste et on recupere tout ce qui est à l'interieur de notre liste
                        citation.append(l) # c'est ici où  on  recupere les auteurs cités par l'aueteur donné
        les_noms=sorted(list(set(citation)))
        if nom in les_noms:
            les_noms.remove(nom)
        return les_noms

