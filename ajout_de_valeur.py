#coding:utf-8
import verification


def ajout_valeur(tableau):
    nb = input("rentrer la valeur de la case:")
    x, y = input("entrer les coordonées en x et y de la case:")
    if verification.verif_case(x, y, nb, tableau) & verification.verif_colonne(tableau, x, nb) & verification.verif_ligne(tableau, y, nb):
        tableau[x, y] = nb
        print(tableau)
    else:
        print("la valeur ne peut être rentrée ici")