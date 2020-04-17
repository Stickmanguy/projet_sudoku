import numpy as np 
import random

class CreateSudoku :
    def __init__(self):
        self.data = np.array([[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]])
        x = 0
        while(x < 20):
            posX = random.randrange(0,8)
            posY = random.randrange(0,8)
            valeur = random.randrange(1,9)
            self.data[posY,posJ] = valeur
            x += 1

        