
"""
    for i in article:
        for t in referencé:
            #print(nx.has_path(G,i,t))
            print(nx.shortest_path(G,'9609072', '9501130'))
            liste_ecrits=set(nx.single_target_shortest_path_length(G,i,t))
        #m=set(nx.shortest_path(G,i))
    #print(m)
        #print(i)
    """
    """
        try: 
            for j in list(G.successors(i)):
                liste_ecrits.append(j)
        except:
            print("rien")
    liste1_ecrits=[]
    for t in referencé:
        for j in list(G.successors(t)):
            liste1_ecrits.append(j)
    """
    
"""
    print(liste_ecrits)
print(inf('Andras Kaiser'))

jh
"""



def inf(nom):
    article=cite.les_articles_de_l_auteur(nom)
    print(article)
    referencé=cite.article_réferncé(nom)
    print(referencé)
    liste_ecrits=[]
    try:
        print(nx.has_path(G,source='9609072',target='9501130'))
        m=nx.single_target_shortest_path_length(G,'9501130',3)
        print(m)
        liste_ecrits.append(a)
                
            
            
    except:
        print("pas de chemin")

    
print(inf('Andras Kaiser'))
