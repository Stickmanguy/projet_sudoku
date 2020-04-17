#coding:utf-8

import numpy as np
import random
from verification import *

data = np.array([[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]])
x = 0
while(x < 20):
    # Prend une position random en X
    posX = random.randrange(0,8)
    # Prend une position random en Y
    posY = random.randrange(0,8)
    # Prend une valeur aléatoire entre 1 et 9
    valeur = random.randrange(1,9)

    #Vérifie les cases et colonnes et 
    if(verif_case(data, posX, posY, valeur) & verif_colonne(data, posX, valeur) & verif_ligne(data, posY, valeur)):
        if(data[posY,posX] != 0):
            x -= 1
        data[posY,posX] = valeur
        x += 1

print(data)