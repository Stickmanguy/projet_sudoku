from tkinter import *
import tkinter.font as tkFont
from Interface_function import *
from ajout_utilisateur import *
import tkinter.messagebox
from validate_email import validate_email
from verif_utilisateur import *

class Register:

    def __init__(self, master):
        global entry_identifiant
        global entry_password
        global entry_password_conf
        global entry_mail

        self.window = master

        self.window.title("Inscription")
        self.window.geometry("520x570")
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

        self.lbl_email = Label(self.window, text="Email:", font=("Helvetica", 12, tkFont.BOLD), bg="#902220",
                               fg="#f5f6fa")
        self.lbl_email.place(x=44, y=243)
        entry_mail = self.lbl_email = Entry(self.window, width=22, font=("Helvetica", 13))
        self.lbl_email.place(x=263, y=243)

        self.lbl_id = Label(self.window, text="Identifiant:", font=("Helvetica", 12, tkFont.BOLD),
                            bg="#902220", fg="#f5f6fa")
        self.lbl_id.place(x=44, y=303)
        entry_identifiant = self.txt_id = Entry(self.window, width=22, font=("Helvetica", 13))
        self.txt_id.place(x=263, y=303)

        self.lbl_pass = Label(self.window, text="Mot de passe:", font=("Helvetica", 12, tkFont.BOLD),
                              bg="#902220", fg="#f5f6fa")
        self.lbl_pass.place(x=44, y=363)
        entry_password = self.txt_pass = Entry(self.window, width=22, font=("Helvetica", 13), show="*")
        self.txt_pass.place(x=263, y=363)

        self.lbl_pass_2 = Label(self.window, text="Confirmer le mot de passe:", font=("Helvetica", 12,
                                tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_pass_2.place(x=44, y=423)
        entry_password_conf = self.txt_pass_2 = Entry(self.window, width=22, font=("Helvetica", 13), show="*")
        self.txt_pass_2.place(x=263, y=423)

        self.btn_enregistrement = Button(self.window, text="S'inscrire", width=30, height=1, font=("Helvetica", 16,
                                   tkFont.BOLD), bg="#dfe6e9", activebackground="#b2bec3", relief=FLAT, command=self.inscription)
        self.btn_enregistrement.place(x=60, y=480)

        self.window.config(menu=self.main_menu)

    def exit(self):
        self.window.destroy()

    def inscription(self):
        identifiant = str(entry_identifiant.get())
        mail = str(entry_mail.get())
        password1 = str(entry_password.get())
        password2 = str(entry_password_conf.get())

        if identifiant == "" or mail == "" or password1 == "" or password2 == "":
            tkinter.messagebox.showwarning("Attention", "Veuillez remplir tous les champs")

        else:
            if validate_email(mail):
                if password1 == password2:
                    if verif_mail(identifiant) != None:
                        tkinter.messagebox.showwarning("Attention", "L'identifiant existe déjà")
                    else:
                        ajout_utilisateur(identifiant, mail, password1)
                        tkinter.messagebox.showinfo("Inscription", "L'utilisateur " + identifiant + " a bien été créer")
                        self.window.destroy()
                else:
                    tkinter.messagebox.showwarning("Attention", "Les mots de passe ne sont pas identiques")
            else:
                tkinter.messagebox.showwarning("Attention", "L'adresse mail que vous avez saisie est incorrect")

