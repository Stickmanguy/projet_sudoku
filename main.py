from create_sudoku import CreateSudoku
from ajout_de_valeur import *
from ajout_utilisateur import *
from verif_utilisateur import *
from Interface_login import *
from Interface_enregistrement import *
from change_mdp import *
import modes

sudoku_01 = CreateSudoku()
modes.mort_subite(sudoku_01.data)