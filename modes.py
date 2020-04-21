from ajout_de_valeur import *
import random
import victory_condition
import time


def classic(tableau):
    print(tableau)
    debut = float(time.time())
    while True:
        ajout_valeur(tableau)
        if victory_condition.victory(tableau):
            fin = float(time.time())
            print("victoire!")
            print("Temps pour réussir: " + str(fin - debut))
            break


def mort_subite(tableau):
    print(tableau)
    debut = time.time()  # prend le temps du commencement
    while True:  # boucle pour la résolution du sudoku
        if not ajout_valeur(tableau):  # malus en cas d'érreur
            x = 0
            while x < 2:
                # Prends une position random en X
                posX = random.randrange(0, 8)
                # Prends une position random en Y
                posY = random.randrange(0, 8)
                if tableau[posY, posX] == 0:
                    x -= 1
                tableau[posY, posX] = 0
                x += 1

        if victory_condition.victory(tableau):
            fin = time.time()
            print("victoire!")
            print("Temps pour réussir: " + str(fin - debut))
            break

        if victory_condition.lose((tableau)):
            fin = time.time()
            print("défaite")
            print("vous avez perdu en :" + str(fin - debut))
            break
