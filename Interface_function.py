import tkinter.messagebox
from Interface_pass_forget import Password_forget
from tkinter import *


def about():
    tkinter.messagebox.showinfo("À propos de Sudoku mania", "Sudoku mania a été conçu dans le cadre d'un projet "
                                                            "scolaire.\n\nLes participants sont : Mauro CERAMI - "
                                                            "Joël DOWONO\nSteven SEMEU - "
                                                            "Célien VANHUYGHEM - Arthur DRAYE")


def rules():
    tkinter.messagebox.showinfo("Règles de sudoku", "Mode Classique:\nUne partie de sudoku commence avec une grille dans "
                                                    "laquelle un certain nombre de numéros sont déjà placés.\nLa grille "
                                                    "est complète lorsque tous les chiffres de 1 à 9 apparaissent une "
                                                    "seule fois dans chacune des neuf lignes, des neuf colonnes et des "
                                                    "neuf blocs.\nEtudiez la grille pour trouver les numéros qui "
                                                    "pourraient se trouver dans chaque cellule.\n\nMode mort subite:\nCe mode "
                                                    "comporte les mêmes règles que le mode classique. En plus à chaque "
                                                    "erreur 2 chiffres sont supprimés Aléatoirement des grilles.\nToute "
                                                    "les minutes qui passe deux chiffres sont également supprimer")


def ranking():
    tkinter.messagebox.showinfo("Classement", "")