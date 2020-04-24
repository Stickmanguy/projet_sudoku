from tkinter import *
import tkinter.font as tkFont
from Interface_function import *
from change_mdp import *
import tkinter.messagebox
from verif_utilisateur import *


class Password_change:

    def __init__(self, master):
        global entry_identifiant
        global entry_old_password
        global entry_new_password
        global entry_new_password_2

        self.window = master

        self.window.title("Changement de mot de passe")
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

        self.lbl_id = Label(self.window, text="Identifiant:", font=("Helvetica", 12, tkFont.BOLD), bg="#902220",
                            fg="#f5f6fa")
        self.lbl_id.place(x=44, y=243)
        entry_identifiant = self.txt_id = Entry(self.window, width=22, font=("Helvetica", 13))
        self.txt_id.place(x=263, y=243)

        self.lbl_pass = Label(self.window, text="Mot de passe actuel:", font=("Helvetica", 12, tkFont.BOLD),
                              bg="#902220", fg="#f5f6fa")
        self.lbl_pass.place(x=44, y=303)
        entry_old_password = self.txt_pass = Entry(self.window, width=22, font=("Helvetica", 13), show="*")
        self.txt_pass.place(x=263, y=303)

        self.lbl_new_pass = Label(self.window, text="Nouveau mot de passe:", font=("Helvetica", 12, tkFont.BOLD),
                                  bg="#902220", fg="#f5f6fa")
        self.lbl_new_pass.place(x=44, y=363)
        entry_new_password = self.txt_new_pass = Entry(self.window, width=22, font=("Helvetica", 13), show="*")
        self.txt_new_pass.place(x=263, y=363)

        self.lbl_new_pass_2 = Label(self.window, text="Confirmer le mot de passe:", font=("Helvetica", 12,
                                    tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_new_pass_2.place(x=44, y=423)
        entry_new_password_2 = self.lbl_new_pass_2 = Entry(self.window, width=22, font=("Helvetica", 13), show="*")
        self.lbl_new_pass_2.place(x=263, y=423)

        self.btn_confirm = Button(self.window, text="Changer le mot de passe", width=30, height=1, font=("Helvetica",
                                  16, tkFont.BOLD), bg="#dfe6e9", activebackground="#b2bec3", relief=FLAT, command=self.change_password)
        self.btn_confirm.place(x=60, y=480)

        self.window.config(menu=self.main_menu)

    def exit(self):
        self.window.destroy()

    def change_password(self):
        identifiant = str(entry_identifiant.get())
        old_password = str(entry_old_password.get())
        new_password = str(entry_new_password.get())
        new_password2 = str(entry_new_password_2.get())

        if identifiant == "" or old_password == "" or new_password == "" or new_password2 == "":
            tkinter.messagebox.showwarning("Attention", "Veuillez remplir tout les champs")
        else:
            if verif_utilisateur(identifiant, old_password):
                if new_password == new_password2:
                    if old_password == new_password:
                        tkinter.messagebox.showwarning("Attention", "Veuillez saisir un nouveau mot de passe différent de l'ancien")
                    else:
                        change_mdp(old_password, new_password, identifiant)
                        tkinter.messagebox.showinfo("Changement de mot de passe", "Votre mot de passe a été correctement modifié")
                        self.window.destroy()
                else:
                    tkinter.messagebox.showwarning("Attention", "Veuillez confirmer correctement votre nouveau mot de passe")
            else:
                tkinter.messagebox.showwarning("Attention", "Veuillez vérifier que l'identifiant ou son mot de passe actuel est correct")