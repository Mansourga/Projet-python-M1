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
#print(G.degree('9912293'))

def influence_auteur(nom):

    #Ici, je cherche ceux qui ont influencé l'auteur en prenant en compte aussi ces co-auteurs


    article1=cite.les_articles_de_l_auteur(nom)
    #print(article1)
    #referencé=cite.article_réferncé(nom)
    liste_ecrits=[]    
    liste_d_ensemble=[]
    nomss=[]
    #ensemble=set()
    dic=dict()
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
   
        for h in set(liste_ecrits):
            for k,l in cite.article.items():    
                if k==h:
                    for e in l:
                        nomss.append(e)
        les_nom=sorted((list(set(nomss))))
        if nom in les_nom:
              les_nom.remove(nom)
        b=nx.single_source_shortest_path_length(G,i,5)
        for x,y in b.items():
            #print(y)
            for name in les_nom:
                if name in cite.article[x] and y!=0:
                    if name not in dic.keys() :
                        dic[name]=1/y
                    else:
                        dic[name]+=1/y



    pprint(dic)
    print(len(dic))

#print(influence_auteur('N. Warner'))
#print(influence_auteur('N. Seiberg'))
#print((influence_auteur('Thomas Appelquist'))) #qui ont influencé l'auteur

 #appelle de la fonction
#print(influence_auteur('Andreas Nyffeler'))
#print(time.time() - tmps1)


#################################
def influencés_par_auteur(nom):
    article1=cite.les_articles_de_l_auteur(nom)
    #print(article)
    nomss=[]
    liste_ecrits=[]
    dic=dict()
    for i in article1:
        #b=nx.single_target_shortest_path_length(G,i,1)
        #print(b)

        #print(i)
        #for t in referencé:
            #a=nx.dijkstra_path_length(G,i,t)
        #print(i)
        #a=nx.single_target_shortest_path(G,i,1) #sort un dict dans lequel les keys sont les cibles et les values() :des liste de valeur allant de la source vers la cible
        #print(a)
        #c=nx.single_source_shortest_path(G,i,2)
        #print(c)
        a=nx.single_target_shortest_path(G,i,20)
        #print(b)
        #d=nx.single_source_shortest_path_length(G,i,2)
        
        #print(d)
        for j in a.values():
            for m in j:
                if m!=i: # je prends pas en compte l'auteur et ses co-auteurs 
                    liste_ecrits.append(m)
    #print(liste_ecrits)
    
        for h in set(liste_ecrits):
            for k,l in cite.article.items():
                if k==h:
                    for e in l:
                        nomss.append(e)

        les_nom=sorted((list(set(nomss))))
        if nom in les_nom:
              les_nom.remove(nom)
        for x,y in a.items():
            #print(len(y))
            if len(y)>1:
                #m=y[0] #rec le prmier arictl de la liste valu
                #print(m)
                for name in les_nom:
                    if name in cite.article[y[0]]:
                        if name not in dic.keys():
                            dic[name]=1/(len(y)-1)
                        else:
                            dic[name]+=1/(len(y)-1)

    pprint(dic)
    print(len(dic))


            



    
    #pprint(dic)
    #print(len(dic))
        #b=nx.single_source_dijkstra_path(G,i,1)
        #print(a)
        #print("rien")
        #print(b)

    #liste_ecrits.append(a)

    #print(liste_ecrits)
#print(influencés_par_auteur('N. Warner'))
#print(influencés_par_auteur('Andreas Nyffeler'))
print((influencés_par_auteur('Thomas Appelquist')))
print(time.time() - tmps1)
#

#print(cite.article['9912293'])