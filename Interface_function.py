import tkinter.messagebox
import webbrowser


def about():
    tkinter.messagebox.showinfo("À propos de Sudoku mania", "Sudoku mania a été conçu dans le cadre d'un projet "
                                                            "scolaire.\n\nLes participants sont : Mauro CERAMI - "
                                                            "Joël DOWONO\nSteven SEMEU - "
                                                            "Célien VANHUYGHEM - Arthur DRAYE")


def rules():
    webbrowser.open_new("page_règle\page_règle.html")