#!/bin/env python3
import influence
import networkx as nx
import cite
import init
import time
from influence import Auteur
from influence import Graph
from pprint import pprint


class Communautes(Auteur):
    """
    Dans cette classe, on cherche la liste de toutes les communautés autour de A de profondeur N .

    """

    def __init__(self,nom):

        super().__init__(nom)
        self.nom= nom

    def communautes(self,nom,N):
        """ 
        Avec notre comprehension, pour sortir la liste d'une communauté, il faut que l'auteur en question soit influencé par un auteur et ce dernier l'influence aussi.
        Donc, les 2 noms doivent se trouver dans la liste influencé_par_l'auteur et aussi dans la liste influence_auteur.
        C'est pourquoi on a utilisé l'intersection des deux ensembles.
        """
        self.N=N
       
        self.influence_auteur=self.influence_auteur(nom,N)

        self.influencé_par_l_auteur=influence.Auteur.influencés_par_l_auteur(self,nom,N)
        return sorted(list(set(self.influence_auteur).intersection(set(self.influencé_par_l_auteur))))


