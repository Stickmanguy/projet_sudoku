from tkinter import *
import tkinter.font as tkFont
from Interface_register import Register
from Interface_function import *
from Interface_welcome import Welcome
from Interface_pass_forget import Password_forget
from verif_utilisateur import *
import tkinter.messagebox


class Login:

    def __init__(self, master):
        global entry_identifiant
        global entry_password
        self.window = master

        self.window.title("Connection")
        self.window.geometry("520x535")
        self.window.resizable(width=False, height=False)
        self.window.configure(background="#902220")
        self.window.iconbitmap("icone.ico")

        self.main_menu = Menu(self.window)

        self.menu_option = Menu(self.main_menu, tearoff=0)
        self.menu_option.add_command(label="Quitter", command=self.exit)

        self.main_menu.add_cascade(label="Option", menu=self.menu_option)

        self.main_menu.add_command(label="Règles du jeu", command=rules)

        self.main_menu.add_command(label="À propos", command=about)

        self.logo = PhotoImage(file='logo_projet.png')
        self.image = Label(self.window, image=self.logo, bg="#902220", relief=FLAT, bd=0)
        self.image.pack()

        self.lbl_id = Label(self.window, text="Identifiant:", font=("Helvetica", 14, tkFont.BOLD), bg="#902220",
                            fg="#f5f6fa")
        self.lbl_id.place(x=44, y=252)

        entry_identifiant = self.txt_id = Entry(self.window, width=22, font=("Helvetica", 13))
        self.txt_id.place(x=263, y=253)

        self.lbl_pass = Label(self.window, text="Mot de passe:", font=("Helvetica", 14, tkFont.BOLD), bg="#902220",
                              fg="#f5f6fa")
        self.lbl_pass.place(x=44, y=312)

        entry_password = self.txt_pass = Entry(self.window, width=22, font=("Helvetica", 13), show="*")
        self.txt_pass.place(x=263, y=313)

        self.btn_pass_forget = Button(self.window, text="Mot de passe oublié", font=("Helvetica", 10, UNDERLINE),
                                      relief=FLAT, bg="#902220", fg="#00a8ff", activebackground="#902220",
                                      activeforeground="#00a8ff", bd=0, command=self.pass_forget)
        self.btn_pass_forget.place(x=300, y=338)

        self.btn_login = Button(self.window, text="Se connecter", width=30, height=1, font=("Helvetica", 16,
                                tkFont.BOLD), bg="#dfe6e9", activebackground="#b2bec3", relief=FLAT, command=self.login)
        self.btn_login.place(x=60, y=395)

        self.btn_register = Button(self.window, text="S'inscrire", width=30, height=1, font=("Helvetica", 16,
                                   tkFont.BOLD), bg="#dfe6e9", activebackground="#b2bec3", relief=FLAT,
                                   command=self.register)
        self.btn_register.place(x=60, y=440)

        self.window.config(menu=self.main_menu)

    def register(self):
        identifiant = str(entry_identifiant.get())
        password = str(entry_password.get())
        if verif_utilisateur(identifiant, password):
            tkinter.messagebox.showwarning("Attention", "Vous avez déjà un compte veuillez vous connecter")
        else:
            root_register = Toplevel(self.window)
            Register(root_register)

    def pass_forget(self):
        root_pass_forget = Toplevel(self.window)
        Password_forget(root_pass_forget)

    def login(self):
        identifiant = str(entry_identifiant.get())
        password = str(entry_password.get())
        if identifiant == "" or password == "":
            tkinter.messagebox.showwarning("Attention", "Veuillez remplir tous les champs")
        else:
            if verif_utilisateur(identifiant, password):
                self.window.destroy()
                Welcome(identifiant)
            else:
                tkinter.messagebox.showwarning("Attention", "L'identifiant ou le mot de passe que vous avez saisi est incorrect")

    def exit(self):
        self.window.destroy()