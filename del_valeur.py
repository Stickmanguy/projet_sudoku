from ajout_de_valeur import *


def del_valeur(posX, posY, sudoku, tableau):
    if sudoku[posY, posX] == tableau[posY, posX]:
        print("ne peut pas supprimer la valeur")
        return sudoku
    else:
        tableau[posY, posX] = 0
        return tableau
