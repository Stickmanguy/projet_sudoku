from tkinter import *
import tkinter.font as tkFont
from Interface_function import *
from change_mdp import *
import tkinter.messagebox
from validate_email import validate_email
from verif_utilisateur import *
from Interface_function import *


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

        self.main_menu.add_cascade(label="Option", menu=self.menu_option)

        self.main_menu.add_command(label="Règles du jeu", command=rules)

        self.main_menu.add_command(label="À propos", command=about)

        self.logo = PhotoImage(file='logo_projet.png')
        self.image = Label(self.window, image=self.logo, bg="#902220")
        self.image.pack()

        self.lbl_id = Label(self.window, text="Identifiant:", font=("Helvetica", 18, tkFont.BOLD), bg="#902220",
                            fg="#f5f6fa")
        self.lbl_id.place(x=55, y=228)

        entry_id = self.txt_id = Entry(self.window, width=22, font=("Helvetica", 13))
        self.txt_id.place(x=236, y=234)

        self.lbl_mail = Label(self.window, text="Email:", font=("Helvetica", 18, tkFont.BOLD), bg="#902220",
                              fg="#f5f6fa")
        self.lbl_mail.place(x=55, y=300)

        entry_mail = self.txt_mail = Entry(self.window, width=22, font=("Helvetica", 13))
        self.txt_mail.place(x=236, y=306)

        self.btn_confirm = Button(self.window, text="Envoyer mail de recuperation", width=30, height=1,
                                  font=("Helvetica", 16,
                                        tkFont.BOLD), bg="#dfe6e9", activebackground="#b2bec3", relief=FLAT,
                                  command=self.pass_forget)
        self.btn_confirm.place(x=60, y=360)

        self.window.config(menu=self.main_menu)

    def exit(self):
        self.window.destroy()

    def pass_forget(self):
        identifiant = str(entry_id.get())
        mail = str(entry_mail.get())

        if identifiant == "" or mail == "":
            tkinter.messagebox.showwarning("Attention", "Veuillez remplir tous les champs")

        else:
            if validate_email(mail):
                if verif_mail(identifiant) == None:
                    tkinter.messagebox.showwarning("Attention", "L'identifiant n'existe pas")
                else:
                    if verif_mail(identifiant) == mail:
                        mdp_oubli(identifiant, mail)
                        tkinter.messagebox.showinfo("Mot de passe oublié", "Un mail de récupération de mot de passe a bien été envoyé à l'adresse mail: " + mail)
                        self.window.destroy()
                    else:
                        tkinter.messagebox.showwarning("Attention", "Cet identifiant n'est pas associé à la bonne adresse mail")

            else:
                tkinter.messagebox.showwarning("Attention", "L'adresse mail que vous avez saisie est incorrect")

