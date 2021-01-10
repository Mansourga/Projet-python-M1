#!/bin/env python3
import networkx as nx
import cite
import init
import time

tmps1=time.time()

class Graph:
    """
    Dans cette classe, on crée un graphe orienté à partir du fichier citation

    """
    def __init__(self):
        self.G=nx.DiGraph()
    
    def creation_du_graph(self):
        self.citation=init.Initialisation.load(self,"citation.json")
        for i in self.citation:
            self.G.add_node(i[0])
            self.G.add_edge(i[0],i[1])
        return self.G

class Auteur(Graph):

    def __init__(self,nom):
        super().__init__()
        self.nom=nom
        self.article=init.Initialisation.load(self,"article.json")
        self.numero_d_itenfiant=cite.Communaute.les_articles_de_l_auteur(self,nom)
        self.liste_ecrits=list()
        self.liste_des_noms=list()
        self.dict=dict()
        self.nomss=list()
        self.dic=dict()
        
    
    def influencés_par_l_auteur(self,nom,N):
        """
        ici, on sort la liste pondérée des auteurs Bi influencés avec une profondeur d’au plus N par un auteur donné .
        
        """ 
        self.N=N
        for numero in self.numero_d_itenfiant:
            if numero in self.creation_du_graph().nodes():

                liste_des_articles_de_reference=nx.single_target_shortest_path(self.G,numero,self.N) #donne la liste des predecesseurs de longeur au plus N de l'article
                
                for i in liste_des_articles_de_reference.values():
                    for m in i:
                        if m!=numero: # on prend pas en compte l'auteur et ses co-auteurs 
                            self.liste_ecrits.append(m)
                
                for h in set(self.liste_ecrits): #set: nous permet ne pas retrouver les doublons
                    for k,l in self.article.items():
                        if k==h:
                            for e in l:
                                self.nomss.append(e)
                    
                les_nom=sorted((list(set(self.nomss)))) # c'est ici que l'on recupere la liste des auteurs influencé par l'auteur donné
                if nom in les_nom:
                    les_nom.remove(nom) #si le nom de l'auteur se trouve dans la liste les_nom: on l'enleve

                """

                C'est à ce niveau où l'on va faire les calculs de l'intensité
                
                """
                for x,y in liste_des_articles_de_reference.items():
                    if len(y)>1:
                        for name in les_nom:
                            if name in self.article[y[0]]:
                                if name not in self.dic.keys():
                                    self.dic[name]=1/(len(y)-1)
                                else:
                                    self.dic[name]+=1/(len(y)-1)

        return self.dic

    
    def influence_auteur(self,nom,N):
        """
        Ici, on sort la liste pondérée des auteurs Bi qui influencent l'auteur en question avec une profondeur au plus N. 
        
        """
        self.N=N

        #Ici, on cherche ceux qui ont influencé l'auteur en prenant en compte aussi ces co-auteurs
        
        for numero in self.numero_d_itenfiant:
            if numero in self.creation_du_graph().nodes():
                liste_chaines_de_reference=nx.single_source_shortest_path(self.G,numero,self.N) # donne les chaines de reference de longeur au plus N
                for j in liste_chaines_de_reference.values(): 
                    for m in j:
                        if m!=numero:
                            self.liste_ecrits.append(m) 
            
                for h in set(self.liste_ecrits):
                    for k,l in self.article.items():    
                        if k==h:
                            for e in l:
                                self.nomss.append(e)
                les_nom=sorted((list(set(self.nomss)))) #recupere la liste des auteurs qui influencent l'auteur donné
                if nom in les_nom:
                    les_nom.remove(nom)
                liste_des_chaines_de_reference_de_l_auteur=nx.single_source_shortest_path_length(self.G,numero,self.N)
                
                for x,y in liste_des_chaines_de_reference_de_l_auteur.items():
                
                    for name in les_nom:
                        if name in self.article[x] and y!=0:
                            if name not in self.dic.keys() :
                                self.dic[name]=1/y
                            else:
                                self.dic[name]+=1/y

        
        return self.dic


















if __name__== "__main__":
    c=Graph()
    #print(c.creation_du_graph())
    A=Auteur("Andreas Nyffeler")
    print(A.influencés_par_l_auteur("Andreas Nyffeler",2))
    #print(A.influence_auteur("Andreas Nyffeler",2))




 