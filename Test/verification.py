# coding:utf-8
import numpy as np


def verif_case(tableau, x, y, nb):
    mX = 0
    nY = 0
    if (x <= 2):
        if (y <= 2):  # 1 ère case
            mX = 0
            nY = 0
        elif (y >= 6):  # 7 ème case
            mX = 0
            nY = 6
        else:   # 4 ème case
            mX = 0
            nY = 3
    elif (x >= 6):
        if (y <= 2):    # 3 ème case
            mX = 6
            nY = 0
        elif (y >= 6):  #
            mX = 6
            nY = 6
        else:
            mX = 6
            nY = 3
    else:
        if (y <= 2):
            mX = 3
            nY = 0
        elif (y >= 6):
            mX = 3
            nY = 6
        else:
            mX = 3
            nY = 3

    listeM = [mX, mX + 1, mX + 2]
    listeN = [nY, nY + 1, nY + 2]

    verif = True
    for mX in listeM:
        for nY in listeN:
            if tableau[nY, mX] == nb:
                verif = False
    return verif


def verif_ligne(tableau, y, nb):
    verif = True
    x = 0
    for x in range(9):
        if tableau[y, x] == nb:
            verif = False
    return verif


def verif_colonne(tableau, x, nb):
    verif = True
    y = 0
    for y in range(0, 9):
        if tableau[y, x] == nb:
            verif = False
    return verif


