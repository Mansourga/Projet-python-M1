import influencee
import networkx as nx
import Citee
import initi
import time
from influencee import Auteur
from influencee import Graph
from pprint import pprint
class Communautes(Auteur):
    def __init__(self,nom):
        super().__init__(nom)
        self.nom= nom
        #self.N=N
    def communautes(self,nom,N):
        self.N=N
        #print(self.N)
        self.influence_auteur=self.influence_auteur(nom,N)
        #print(self.influence_auteur)
        self.influencé_par_l_auteur=influencee.Auteur.influencés_par_l_auteur(self,nom,N)
        return sorted(list(set(self.influence_auteur).intersection(set(self.influencé_par_l_auteur))))

    #intersec=set(influence).intersection(set(influencé))
    #print((set()).intersection(set(intensite.influencés_par_auteur(nom).keys())))



if __name__== "__main__":
    #c=Graph()
    #print(c.creation_du_graph())
    A=Communautes("Andreas Nyffeler")
    
    #print(A.influence_auteur("Andreas Nyffeler",2))
    pprint(A.communautes('Andreas Nyffeler',3))