from tkinter import *
import tkinter.font as tkFont
from tkinter.ttk import Combobox
from Interface_function import *
from Interface_game import *


class Welcome:

    def __init__(self):

        self.window = Tk()

        self.window.title("Sudoku mania")
        self.window.geometry("520x520")
        self.window.resizable(width=False, height=False)
        self.window.configure(background="#902220")
        self.window.iconbitmap("icone.ico")

        self.main_menu = Menu(self.window)

        self.menu_option = Menu(self.main_menu, tearoff=0)
        self.menu_option.add_command(label="Changer le mot de passe")
        self.menu_option.add_command(label="Se déconnecter")
        self.menu_option.add_command(label="Quitter", command=self.exit)

        self.main_menu.add_cascade(label="Options", menu=self.menu_option)

        self.main_menu.add_command(label="Classement", command=ranking)

        self.main_menu.add_command(label="Règles du jeu", command=rules)

        self.main_menu.add_command(label="À propos", command=about)

        self.logo = PhotoImage(file='logo_projet.png')
        self.image = Label(image=self.logo, bg="#902220")
        self.image.pack()

        self.lbl_acc = Label(text="Bienvenue", font=("Helvetica", 18, tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_acc.pack(pady=15)

        self.lbl_mode = Label(text="Modes de jeu", font=("Helvetica", 14, tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_mode.pack(pady=20)

        self.cbx_list = ["Classique", "Mort subite"]
        self.cbx_modes = Combobox(values=self.cbx_list, state="readonly", width=20, font=("Helvetica", 16),
                                  justify=CENTER)
        self.cbx_modes.pack()
        self.cbx_modes.current(0)

        self.btn_jouer = Button(text="Jouer", width=30, height=1, font=("Helvetica", 16, tkFont.BOLD), bg="#dfe6e9",
                                activebackground="#b2bec3", relief=FLAT, command=self.play)
        self.btn_jouer.pack(pady=50)

        self.window.config(menu=self.main_menu)

        self.window.mainloop()

    def exit(self):
        self.window.destroy()

    def play(self):
        self.window.destroy()
        Game()