import intensite

def communauté(nom):
    influence=intensite.influence_auteur(nom).keys()
    #print(set(influence))
    influencé=intensite.influencés_par_auteur(nom).keys()
    #print(set(influencé))
    print(set(influence).intersection(set(influencé)))
    #intersec=set(influence).intersection(set(influencé))
    #print((set()).intersection(set(intensite.influencés_par_auteur(nom).keys())))


print(communauté('Cumrun Vafa'))