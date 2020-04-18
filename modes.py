from ajout_de_valeur import *
import victory_condition
import time


def classic(tableau):
    debut=time.time()
    while True:
        ajout_valeur(tableau)
        if victory_condition.victory(tableau):
            fin=time.time()
            print("victoire!")
            print("Temps pour réussir: " + fin-debut)
            break