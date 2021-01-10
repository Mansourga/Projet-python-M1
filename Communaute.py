#!/bin/env python3
import sys
from sys import argv
import os
from os import path
import pathlib
import time
import init
import time
from pprint import pprint
import influence
import cite
import communautes

 
def main():
    if len (argv)==3 :
        if argv[1]=='cite':
            cites=cite.Communaute(argv[2])
            pprint(cites.liste_des_auteurs_cités(argv[2]))
        else:
            print( "\n Veuillez saisir 'cite' \n")
        
    if len(argv)==4 :
        try:
            if argv[1]== 'init' :
                if  path.isdir(argv[2]) == True and path.isfile(argv[3])==True:
                    ini=init.Initialisation(argv[2],argv[3])
                    ini.initialiser(argv[2],argv[3])
                else:
                    print(" \n Vous n'avez pas saisi les bons  chemins \n")  
            if argv[1]=='influencés_par':
                    G=influence.Graph()
                    A=influence.Auteur(argv[2])
                    pprint(list(A.influencés_par_l_auteur(argv[2],int(argv[3]))))
                    

                    
            if argv[1]=='influence':
                    G=influence.Graph()
                    A=influence.Auteur(argv[2])
                    pprint(list(A.influence_auteur(argv[2],int(argv[3]))))
            
            if argv[1]=='communautes':
                A=  communautes.Communautes(argv[2])
                pprint(A.communautes(argv[2],int(argv[3])))
            
        except:
            print( '\n Veuillez saisir les bonnes informations avec un entier positif \n')
            
    
        
    
    
if __name__== "__main__":
    main()

