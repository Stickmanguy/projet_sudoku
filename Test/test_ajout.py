from verification import *
import create_sudoku

sudoku_01 = create_sudoku.CreateSudoku()


def ajout_valeur(tableau):
    nb = int(input("rentrer la valeur de la case:"))
    x = int(input("entrer les coordonées en x :"))
    y = int(input("entrer les coordonées en Y :"))

    if verif_case(tableau, x, y, nb) & verif_colonne(tableau, x, nb) & verif_ligne(tableau, y, nb) & tableau[y, x] == 0 & nb <= 9 & nb > 0:
        tableau[y, x] = nb
        print(tableau)
    elif nb > 9 | nb < 0:
        print("la valeur est hors range")
    elif tableau[y, x] != 0:
        print("Il y'a déjà une valeur")
    else:
        print("Entrez une valeur correct")


print(sudoku_01.data)
ajout_valeur(sudoku_01.data)
