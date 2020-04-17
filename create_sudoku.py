#coding:utf-8

# Importation des bibliothèques
from verification import *
import numpy as np 
import random


class CreateSudoku :
    def __init__(self):
        # Déclaration d'un tableau utilisable facilement 
        self.data = np.array([[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]])
        # Déclaration d'une variable pour initier la boucle
        x = 0
        # Tant que je n'ai pas 20 - c'est aussi le vecteur de la difficulté
        while(x < 20):
            # Prend une position random en X
            posX = random.randrange(0,8)
            # Prend une position random en Y
            posY = random.randrange(0,8)
            # Prend une valeur aléatoire entre 1 et 9
            valeur = random.randrange(1,9)
            #Vérifie les cases et colonnes et des lignes et des cases
            if(verif_case(self.data, posX, posY, valeur) & verif_colonne(self.data, posX, valeur) & verif_ligne(self.data, posY, valeur)):
                if(self.data[posY,posX] != 0):
                    x -= 1
                self.data[posY,posX] = valeur
                x += 1

            