import numpy as np

tableau = np.array([[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,8,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]])
print(tableau)

def verif_case(tableau, x, y, nb):
    mX = 0
    nY = 0
    if (x <= 2):
        if (y <= 2):  # 1 ère case - test fait
            mX = 0
            nY = 0
        elif (y >= 6):  # 7 ème case - test fait
            mX = 0
            nY = 6
        else:   # 4 ème case
            mX = 0
            nY = 3
    elif (x >= 6):
        if (y <= 2):    # 3 ème case
            mX = 6
            nY = 0
        elif (y >= 6): #
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

    listeM = [mX, mX+1, mX+2]
    listeN = [nY, nY+1, nY+2]
    verif = True
    for mX in listeM:
        for nY in listeN:
            if tableau[nY, mX] == nb:
                print("anus")
                verif = False
    return verif

print(verif_case(tableau,1,6,5))
