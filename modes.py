from ajout_de_valeur import *
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
            print("Temps pour réussir: " + str(fin-debut))
            break
