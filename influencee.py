
import networkx as nx
import Citee
import initi
import time

tmps1=time.time()

class Graph:
    def __init__(self):
        self.G=nx.DiGraph()
    
    def creation_du_graph(self):
        self.citation=initi.Initialisation.load(self,"citation.json")
        for i in self.citation:
            self.G.add_node(i[0])
            self.G.add_edge(i[0],i[1])
        return self.G
        #print(self.G.number_of_nodes())

class Auteur(Graph):
    def __init__(self,nom):
        super().__init__()
        self.nom=nom
        self.article=initi.Initialisation.load(self,"article.json")
        self.numero_d_itenfiant=Citee.Communaute.les_articles_de_l_auteur(self,nom)
        self.liste_ecrits=list()
        self.liste_des_noms=list()
        self.dict=dict()
        self.nomss=list()
        self.dic=dict()
        #print(self.numero_d_itenfiant)
    
    def influencés_par_l_auteur(self,nom,N):
        self.N=N
        #self.Citee.Communaute.les_articles_de_l_auteur()
        #self.numero_d_itenfiant=Citee.Communaute.les_articles_de_l_auteur(self,nom)
        #self.referencé=Citee.Communaute.article_réferncé(self,nom)

        for numero in self.numero_d_itenfiant:
            if numero in self.creation_du_graph().nodes():
                liste_des_articles_de_reference=nx.single_target_shortest_path(self.G,numero,self.N)
                
                for i in liste_des_articles_de_reference.values():
                    for m in i:
                        if m!=numero: # je prends pas en compte l'auteur et ses co-auteurs 
                            self.liste_ecrits.append(m)
            #print(liste_ecrits)
                
                for h in set(self.liste_ecrits):
                    for k,l in self.article.items():
                        if k==h:
                            for e in l:
                                self.nomss.append(e)
                    
                les_nom=sorted((list(set(self.nomss))))
                if nom in les_nom:
                    les_nom.remove(nom)
                for x,y in liste_des_articles_de_reference.items():
                    #print(len(y))
                    if len(y)>1:
                        #m=y[0] #rec le prmier arictl de la liste valu
                        #print(m)
                        for name in les_nom:
                            if name in self.article[y[0]]:
                                if name not in self.dic.keys():
                                    self.dic[name]=1/(len(y)-1)
                                else:
                                    self.dic[name]+=1/(len(y)-1)

        return self.dic

    
    def influence_auteur(self,nom,N):
        self.N=N

        #Ici, je cherche ceux qui ont influencé l'auteur en prenant en compte aussi ces co-auteurs
        #print(article1)
        for numero in self.numero_d_itenfiant:
        #print(i)
            if numero in self.creation_du_graph().nodes():
                liste_chaines_de_reference=nx.single_source_shortest_path(self.G,numero,self.N) #le plus court chemin pour aller vers la cible
                for j in liste_chaines_de_reference.values(): 
                    for m in j:
                        if m!=numero:
                    
                        #for k in article1:
                            #if m!=k:
                        #rajouté
                            self.liste_ecrits.append(m)
            #print(len(liste_ecrits))    
            

                for h in set(self.liste_ecrits):
                    for k,l in self.article.items():    
                        if k==h:
                            for e in l:
                                self.nomss.append(e)
                les_nom=sorted((list(set(self.nomss))))
                if nom in les_nom:
                    les_nom.remove(nom)
                liste_des_chaines_de_reference_de_l_auteur=nx.single_source_shortest_path_length(self.G,numero,self.N)
                for x,y in liste_des_chaines_de_reference_de_l_auteur.items():
                    #print(y)
                    for name in les_nom:
                        if name in self.article[x] and y!=0:
                            if name not in self.dic.keys() :
                                self.dic[name]=1/y
                            else:
                                self.dic[name]+=1/y


        print(len(self.dic))
        
        return self.dic
print(time.time() - tmps1)

















if __name__== "__main__":
    c=Graph()
    #print(c.creation_du_graph())
    A=Auteur("Andreas Nyffeler")
    print(A.influencés_par_l_auteur("Andreas Nyffeler",2))
    #print(A.influence_auteur("Andreas Nyffeler",2))




 