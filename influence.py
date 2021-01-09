
import networkx as nx
import cite
from pprint import pprint
 
import time 

tmps1=time.time()

G=nx.DiGraph()
for i in cite.cita:
    G.add_node(i[0])
    G.add_edge(i[0],i[1])
#print(G.nodes())
#print(G.edges())
#print(G.number_of_nodes())
#print(G.number_of_edges())
##nx.draw_circular(G)
#plt.show()
#print(G.degree('9901023'))
"""
def influence_auteur(nom):

    #Ici, je cherche ceux qui ont influencé l'auteur en prenant en compte aussi ces co-auteurs


    article1=cite.les_articles_de_l_auteur(nom)
    #print(article)
    #referencé=cite.article_réferncé(nom)
    liste_ecrits=[]    
    liste_d_ensemble=[]
    #ensemble=set()
    for i in article1:
        #print(i)
        #for t in referencé:
            #a=nx.dijkstra_path_length(G,i,t)
        a=nx.single_source_shortest_path(G,i,5) #le plus court chemin pour aller vers la cible
        #ensemble=set(a.values())
        #print(ensemble)
        #intensité=nx.shortest_path_length(G,i,3) 
        #print(intensité)
        #print(i)
        #print(a)
        #ens=a[:len(a.values())-1]
        #print(ens)
        for j in a.values(): 
            #print(i)
            #print(j)
        #    liste_sans_les_co_auteurs=j[1:]
        #    for m in liste_sans_les_co_auteurs:
            for m in j:
                if m!=i:
            
                #for k in article1:
                    #if m!=k:

                 #rajouté
                    liste_ecrits.append(m)
    #print(len(liste_ecrits))    
    nomss=[]
    for h in set(liste_ecrits):
        for k,l in cite.article.items():    
            if k==h:
                for e in l:
                    nomss.append(e)
    les_nom=sorted((list(set(nomss))))
    if nom in les_nom:
        les_nom.remove(nom)
    pprint(les_nom)
    print(len((list(set(les_nom)))))
    print(len(liste_ecrits))
        #b=nx.single_source_dijkstra_path(G,i,1)
        #print(a)
        #print("rien")
        #print(b)

    #liste_ecrits.append(a)

    #print(liste_ecrits)
#print(influence_auteur('N. Seiberg'))
print(influence_auteur('Andreas Nyffeler'))
#print((influence_auteur('Thomas Appelquist'))) #qui ont influencé l'auteur

 #appelle de la fonction
#print(influence_auteur('N. Warner'))
print(time.time() - tmps1)

"""


def influencés_par_auteur(nom):
    article=cite.les_articles_de_l_auteur(nom)
    #print(article)
    referencé=cite.article_réferncé(nom)
    liste_ecrits=[]    
    for i in article:
        #print(i)
        #for t in referencé:
            #a=nx.dijkstra_path_length(G,i,t)
        if i in G.nodes():
            a=nx.single_target_shortest_path(G,i,2) #sort un dict dans lequel les keys sont les cibles et les values() :des liste de valeur allant de la source vers la cible
        
        #print(a)
            for j in a.values():
                for m in j:
                    if m!=i: # je prends pas en compte l'auteur et ses co-auteurs 
                        liste_ecrits.append(m)
    #print(liste_ecrits)
    nomss=[]
    for h in liste_ecrits:
        for k,l in cite.article.items():
            if k==h:
                for e in l:
                    nomss.append(e)
    pprint(sorted(list(set(nomss))))
    print(len(list(set(nomss))))
        #b=nx.single_source_dijkstra_path(G,i,1)
        #print(a)
        #print("rien")
        #print(b)

    #liste_ecrits.append(a)

    #print(liste_ecrits)
#print(influencés_par_auteur('N. Warner'))

#print((influencés_par_auteur('Thomas Appelquist'))) #qui ont influencé l'auteur
#print(influencés_par_auteur('N. Warner'))
print((influencés_par_auteur('Cumrun Vafa')))

#Repondre la
"""
def influencés_par_auteur(nom):
    article=cite.les_articles_de_l_auteur(nom)
    #print(article)
    referencé=cite.article_réferncé(nom)
    liste_ecrits=[]   
    dic={}
    nomss=[]
    for i in article:
        #print(i)
        #for t in referencé:
            #a=nx.dijkstra_path_length(G,i,t)
        b=nx.single_source_shortest_path(G,i,5)
        a=nx.single_source_shortest_path_length(G,i,5)
        for j in b.values():
            for m in j:
                if m!=i: # je prends pas en compte l'auteur et ses co-auteurs 
                    liste_ecrits.append(m)
    #print(liste_ecrits) 
                    for h in liste_ecrits:
                        for k,l in cite.article.items():
                            if k==h:
                                for e in l:

        #print(b)
                                     #sort un dict dans lequel les keys sont les cibles et les values() :des liste de valeur allant de la source vers la cible
        #for j,l in a.items():
        #for m in b.values():

                                    
                                    for numero,longeur in a.items():
                                            try:
                                                if e in cite.article[numero]:
                                            
                                                    dic[e]+=1/longeur
                                                else:
                                                    dic[e]= 1/longeur
                                            except:
                                                pass
    pprint(dic)
                                        #nomss.append(e)

                #for k,l in cite.article.items():
            #print(j)

        #print(a)

##########
    
        for j in a.values():
            for m in j:
                if m!=i: # je prends pas en compte l'auteur et ses co-auteurs 
                liste_ecrits.append(m)
    #print(liste_ecrits)
    nomss=[]
    for h in liste_ecrits:
        for k,l in cite.article.items():
            if k==h:
                for e in l:
                    nomss.append(e)
    pprint(sorted(list(set(nomss))))
    print(len(list(set(nomss))))
        #b=nx.single_source_dijkstra_path(G,i,1)
        #print(a)
        #print("rien")
        #print(b)

    #liste_ecrits.append(a)

    #print(liste_ecrits)
    """
#print(influencés_par_auteur('N. Warner'))

#print((influencés_par_auteur('Andreas Nyffeler'))) #qui ont influencé l'auteur
#print(influencés_par_auteur('N. Warner'))
