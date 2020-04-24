# coding:utf-8
import numpy as np


def verif_case(tableau, x, y, nb):
    posy = (y // 3) * 3
    posx = (x // 3) * 3
    for i in range(posy, (posy + 3)):
        for j in range(posx, (posx + 3)):
            if tableau[i][j] == nb:
                return False
    return True


def verif_ligne(tableau, y, nb):
    verif = True
    x = 0
    for x in range(9):
        if tableau[y][x] == nb:
            verif = False
    return verif


def verif_colonne(tableau, x, nb):
    verif = True
    y = 0
    for y in range(0, 9):
        if tableau[y][x] == nb:
            verif = False
    return verif


