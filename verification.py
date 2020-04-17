#coding:utf-8
import numpy as np

def verif_case(tableau, x, y , nb):
    m=0
    n=0
    if(x<=2):
        if(y<=2):
            m=0
            n=0
        elif(y>=6):
            m=0
            n=6
        else:
            m=0
            n=3
    elif(x>=6):
        if(y<=2):
            m=6
            n=0
        elif(y>=6):
            m=6
            n=6
        else:
            m=6
            n=3
    else:
        if(y<=2):
            m=3
            n=0
        elif(y>=6):
            m=3
            n=6
        else:
            m=3
            n=3

    listeM = [m, m+1, m+2]
    listeN = [n, n+1, n+2]
    verif = True
    for n in listeM:
        for m in listeN:
            if tableau[n,m] == nb:
                verif = False
    return verif


def verif_ligne(tableau, y, nb):
    verif = True
    x=0
    for x in range(9):
        if tableau [y,x]==nb:
            verif = False
    return verif

def verif_colonne(tableau, x, nb):
    verif = True
    y=0
    for y in range (0,9):
        if tableau[y,x] == nb:
            verif = False
    return verif
