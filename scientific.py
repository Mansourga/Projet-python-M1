import sys
from sys import argv
import os
from os import path
import pathlib
import time
import init
import time

#import projet
def main():
    if len(argv)==4:
        if argv[1]== 'init' :
            if  path.isdir(argv[2]) == True and path.isfile(argv[3])==True:
                init.initialiser(argv[2],argv[3])
                
        else:
            print("pas bien")
    if len (argv)==3:
        import cite
        if argv[1]=="cite":
            cite.liste_des_auteurs_cités(argv[2])
        else:
            print("Veuillez entrer un d'auteur qui existe")
if __name__== "__main__":
    main()

