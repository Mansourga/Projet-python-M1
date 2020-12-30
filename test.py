
"""
import pandas as pd
data=pd.read_csv("https://math.univ-angers.fr/~ducrot/pyds1/data/hep-th-abs.tar.gz")
print(data)


data=pd.read_csv("hep-th-citations")
print(data)
"""

import numpy as np
import tarfile
import os

#tar = tarfile.open("hep-th-abs.tar.gz")
#tar=tarfile.open("hep-th-citations.tar.gz")
#tar.extractall()
#tar.close()
#Data = np.loadtxt(tar,decodage= "utf_8")

import re
mot=re.compile("\w+")
auteur=[]
files= os.listdir(r"C:\Users\gayem\Desktop\tp charbon\projet")
for i in files:
    data= os.listdir(r"C:\Users\gayem\Desktop\tp charbon\projet\{}".format(i))
    for j in data:
        with open(r"C:\Users\gayem\Desktop\tp charbon\projet\{}\{}".format(i,j),"r") as f:
            for line in f:
                if line.startswith("Author")==True:
                    text=line.replace(" and ",",") #and (line.replace("Authors:", "") and line.replace("Author:","")
                    rtext=text.replace("Authors:", "")
                    retext=rtext.replace("Author:", "")
                    content=retext.split()
                    for mot in content:
                        if str(mot).startswith("(")==True:
                            content.remove(mot)
                            print(content)

with open(r"C:\Users\gayem\Desktop\tp charbon\projet_code\hep-th-citations","r") as citations:
    A=dict()
    for line in citations:
        if line.split()[0] in A:
            A[line.split()[0]].add([line.split()[0]])
        else:
            A[line.split()[0]]=1
    print(A)



#14/12
import re
mot=re.compile(r'\([^)]*\)')
auteur=[]
files= os.listdir(r"C:\Users\gayem\Desktop\tp charbon\projet")
for i in files:
    data= os.listdir(r"C:\Users\gayem\Desktop\tp charbon\projet\{}".format(i))
    for j in data:
        with open(r"C:\Users\gayem\Desktop\tp charbon\projet\{}\{}".format(i,j),"r") as f:
            for line in f:
                if line.startswith("Author")==True:
                    text=line.replace(" and ",",") #and (line.replace("Authors:", "") and line.replace("Author:","")
                    rtext=text.replace("Authors:", "")
                    retext=rtext.replace("Author:", "")
                    text=re.sub(mot,"",retext)
                    print(text)
