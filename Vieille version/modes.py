from ajout_de_valeur import *
import random
import victory_condition
import time


def classic(tableau, x, y, nb):
    tableau, bol = ajout_valeur(tableau, x, y, nb)
    return tableau


def mort_subite(tableau, x, y, nb):
    tableau, bol = ajout_valeur(tableau, x, y, nb)
    return tableau, bol;