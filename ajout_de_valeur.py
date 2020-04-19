from verification import *


def ajout_valeur(tableau):
    nb = input("entrer la valeur de la case:")
    x = input("entrer les coordonées en x :")
    y = input("entrer les coordonées en Y :")
    if x == "" or y == "" or nb == "":
        print("Entrez toutes les valeurs !")
        ajout_valeur(tableau)
    nb = int(nb)
    x = int(x)
    y = int(y)
    if verif_case(tableau, x, y, nb):
        if verif_colonne(tableau, x, nb) and verif_ligne(tableau, y, nb) and 0 < nb <= 9 and tableau[y, x] == 0:
            tableau[y, x] = nb
            print(tableau)
            return True
    else:
        print("Pas bon")
        print(tableau)
        return False
