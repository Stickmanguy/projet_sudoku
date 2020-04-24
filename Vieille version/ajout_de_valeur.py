from Test.verification import *


def ajout_valeur(tableau, x, y, nb):
    if x == "" or y == "" or nb == "":
        ajout_valeur(tableau)
    else:
        nb = int(nb)
        x = int(x)
        y = int(y)
        if verif_case(tableau, x, y, nb) & verif_colonne(tableau, x, nb) and verif_ligne(tableau, y, nb) and 0 < nb <= 9 and tableau[y, x] == 0 or nb == 0:
                tableau[y, x] = nb
                return tableau, True
        else:
            return tableau, False
