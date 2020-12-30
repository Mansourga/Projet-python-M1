import re
import os
mot= re.compile(r"\([^\)\(]*\)")#re.compile(r'\([^)]*\)')
auteur=[]
files= os.listdir(r"C:\Users\gayem\Desktop\tp charbon\projet")

for i in files:
    data= os.listdir(r"C:\Users\gayem\Desktop\tp charbon\projet\{}".format(i))
    
    for j in data:
        dict_id_aut=dict()
        with open(r"C:\Users\gayem\Desktop\tp charbon\projet\{}\{}".format(i,j),"r") as f:

            text=f.readlines()
            
            Author=[l for l in text if l.startswith("Author")==True][0] #[0] me permet d'extraire le contenu de la liste
            Author_idx=text.index(Author) #je prend l'index de l'auteur dans le text
            Author_idx+=1 
            while text[Author_idx].startswith(" ")==True: #cherche tant que toutes les lignes qui suivent commencent par un espace 
                Author=Author+text[Author_idx] #rajoute dans la ligne de l'auteur la ligne qui suit sur une meme ligne
                Author_idx+=1 
            Author=Author.replace("\n","")
            #Author=Author.replace("( ","")
            #Author=Author.replace(" )","")
            Author=re.sub(mot,"",Author)
            Author=Author.replace(" and ",",") #and (line.replace("Authors:", "") and line.replace("Author:","")
            Author = Author.split(":")[1] #fait le split en utilisant les deux points et [1],i.e que je vais prendre l'indexe 1
            #Author = Author.split("(")
            if "(" in Author:
                Author=Author.replace(Author.split("(")[1],"") #me fait la separation en fonction de (
                Author=Author.replace("(","")  #puis le supprime
            Author=Author.replace(",,",",")
            #print(Author)
            authors = [a.strip() for a in Author.split(",")]  #met les auteur de chaque article dans  son propre liste une fois le split
            #print(authors)
            with open(r"C:\Users\gayem\Desktop\tp charbon\projet\{}\{}".format(i,j),"r") as f:
                with open(r"auteur.txt", "w") as fichier2:
                    for line in f:
                        fichier2.writes(line)
                fichier2.close()
                            #fichier2.write(f.read().split())

