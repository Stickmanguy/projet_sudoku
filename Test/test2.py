import numpy as np
import random

data = np.array([[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]])
x = 0
while(x < 20):
    posX = random.randrange(0,8)
    posY = random.randrange(0,8)
    valeur = random.randrange(1,9)
    if(data[posY,posX] != 0):
        x -= 1
    data[posY,posX] = valeur
    x += 1

print(data)