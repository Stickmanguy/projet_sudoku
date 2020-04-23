
from random import shuffle
import copy
from verification import *

class CreateSudoku:

    def __init__(self, tableau=None):
        self.counter = 0
        self.path = []
        if tableau:
            if len(tableau[0]) == 9 and len(tableau) == 9:
                self.tableau = tableau
                self.original = copy.deepcopy(tableau)
                self.soluce_sudoku()
        else:
            self.tableau = [[0 for i in range(9)] for j in range(9)]
            self.generation_casse_tete()
            self.original = copy.deepcopy(self.tableau)

    def soluce_sudoku(self):
        self.generate_solution(self.tableau)
        return

    def generation_casse_tete(self):
        self.generate_solution(self.tableau)
        self.effaceur()
        self.data()
        return

    def data(self):

        return self.tableau

    def test_sudoku(self, tableau):
        for y in range(9):
            for x in range(9):
                nb = tableau[y][x]
                tableau[y][x] = 0
                if not self.test_final(tableau, y, x, nb):
                    return False
                else:
                    tableau[y][x] = nb
        return True

    def test_final(self, tableau, y, x, number):
        if not verif_ligne(tableau, y, number):
            return False
        elif not verif_colonne(tableau, x, number):
            return False
        elif not verif_case(tableau, x, y, number):
            return False
        return True

    def pos_vide(self, tableau):
        for i in range(9):
            for j in range(9):
                if tableau[i][j] == 0:
                    return (i, j)
        return


    def generate_solution(self, tableau):
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(0, 81):
            y = i // 9
            x = i % 9

            if tableau[y][x] == 0:
                shuffle(number_list)
                for number in number_list:
                    if self.test_final(tableau, y, x, number):
                        self.path.append((number, y, x))
                        tableau[y][x] = number
                        if not self.pos_vide(tableau):
                            return True
                        else:
                            if self.generate_solution(tableau):
                                return True
                break
        tableau[y][x] = 0
        return False

    def resolution(self, tableau):
        for i in range(0, 81):
            y = i // 9
            x = i % 9
            if tableau[y][x] == 0:
                for nb in range(1, 10):
                    if self.test_final(tableau, y, x, nb):
                        tableau[y][x] = nb
                        if not self.pos_vide(tableau):
                            self.counter += 1
                            break
                        else:
                            if self.resolution(tableau):
                                return True
                break
        tableau[x][y] = 0
        return False

    def donne_pos_non_vide(self, tableau):
        pos_pas_vide = []
        for i in range(len(tableau)):
            for j in range(len(tableau)):
                if tableau[i][j] != 0:
                    pos_pas_vide.append((i, j))
        shuffle(pos_pas_vide)
        return pos_pas_vide

    def effaceur(self):
        pos_pas_vide = self.donne_pos_non_vide(self.tableau)
        compt_pos_pas_vide = len(pos_pas_vide)
        rounds = 3
        while rounds > 0 and compt_pos_pas_vide >= 17:
            y, x = pos_pas_vide.pop()
            compt_pos_pas_vide -= 1
            case_suppr = self.tableau[y][x]
            self.tableau[y][x] = 0
            grid_copy = copy.deepcopy(self.tableau)
            self.counter = 0
            self.resolution(grid_copy)
            if self.counter != 1:
                self.tableau[y][x] = case_suppr
                compt_pos_pas_vide += 1
                rounds -= 1
        return

