from verification import *

def ajout_valeur(tableau):
    nb = int(input("rentrer la valeur de la case:"))
    x = int(input("entrer les coordonées en x :"))
    y = int(input("entrer les coordonées en Y :"))

    if verif_case(tableau, x, y, nb):
        if verif_colonne(tableau, x, nb) and verif_ligne(tableau, y, nb) and 0 < nb <= 9 and tableau[y, x] == 0:
            tableau[y, x] = nb
            print(tableau)
    else:
        print("Pas bon")

