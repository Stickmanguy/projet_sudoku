from tkinter import *
import tkinter.font as tkFont
from Interface_function import *
from change_mdp import *


class Password_forget:

    def __init__(self, master):
        global entry_id
        global entry_mail
        self.window = master

        self.window.title("Mot de passe oublié")
        self.window.geometry("520x453")
        self.window.resizable(width=False, height=False)
        self.window.configure(background="#902220")
        self.window.iconbitmap("icone.ico")

        self.main_menu = Menu(self.window)

        self.menu_option = Menu(self.main_menu, tearoff=0)
        self.menu_option.add_command(label="Quitter", command=self.exit)

        self.main_menu.add_cascade(label="Options")

        self.main_menu.add_command(label="Règles du jeu")

        self.main_menu.add_command(label="À propos")

        self.logo = PhotoImage(file='logo_projet.png')
        self.image = Label(self.window, image=self.logo, bg="#902220")
        self.image.pack()

        self.lbl_id = Label(self.window, text="Identifiant:", font=("Helvetica", 18, tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_id.place(x=55, y=228)

        entry_id = self.txt_id = Entry(self.window, width=22, font=("Helvetica", 13))
        self.txt_id.place(x=236, y=234)

        self.lbl_mail = Label(self.window, text="Email:", font=("Helvetica", 18, tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_mail.place(x=55, y=300)

        entry_mail = self.txt_mail = Entry(self.window, width=22, font=("Helvetica", 13))
        self.txt_mail.place(x=236, y=306)

        self.btn_confirm = Button(self.window, text="Envoyer mail de recuperation", width=30, height=1, font=("Helvetica", 16,
                                  tkFont.BOLD), bg="#dfe6e9", activebackground="#b2bec3", relief=FLAT, command=self.mdp_oubli_int)
        self.btn_confirm.place(x=60, y=360)

        self.window.config(menu=self.main_menu)

    def exit(self):
        self.window.destroy()

    def mdp_oubli_int(self):
        mdp_oubli(str(entry_id), str(entry_mail))
        self.window.destroy()
