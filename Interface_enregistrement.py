from tkinter import *
import tkinter.font as tkFont
import Interface_login
from ajout_utilisateur import *
from tkinter.ttk import Combobox

class Enregistrement:


    def __init__(self):
        self.window = Tk()

        self.window.title("Sudoku mania")
        self.window.geometry("520x535")
        self.window.resizable(width=False, height=False)
        self.window.configure(background="#2f3640")
        self.window.iconbitmap("icone.ico")

        self.logo = PhotoImage(file='logo_projet.png')
        self.image = Label(image=self.logo, bg="#2f3640")
        self.image.pack()

        self.lbl_id = Label(text="Identifiant:", font=("Helvetica", 12, tkFont.BOLD), bg="#2f3640", fg="#f5f6fa")
        self.lbl_id.place(x=44, y=273)

        entry_identifiant = self.txt_id = Entry(self.window, width=22, font=("Helvetica", 13))
        self.txt_id.place(x=263, y=273)

        self.lbl_mdp = Label(text="Mot de passe:", font=("Helvetica", 12, tkFont.BOLD), bg="#2f3640", fg="#f5f6fa")
        self.lbl_mdp.place(x=44, y=333)

        entry_password = self.txt_mdp = Entry(self.window, width=22, font=("Helvetica", 13), show="*")
        self.txt_mdp.place(x=263, y=333)

        self.lbl_mdp = Label(text="Confirmer le mot de passe:", font=("Helvetica", 12, tkFont.BOLD), bg="#2f3640",
                             fg="#f5f6fa")
        self.lbl_mdp.place(x=44, y=393)

        entry_password_conf = self.txt_mdp = Entry(self.window, width=22, font=("Helvetica", 13), show="*")
        self.txt_mdp.place(x=263, y=393)

        def buton_click():
            identifiant = entry_identifiant.get()
            password1 = entry_password.get()
            password2 = entry_password_conf.get()
            if identifiant != "":
                if password1 == password2:
                    if password1 != "":
                        ajout_utilisateur(identifiant, password1)
                        print("utilisateur ajouté")
                        print(password1)
                        self.window.destroy()
                        Interface_login.Login()

                    else:
                        print("entrez un mdp")
                else:
                    print("recommence")
            else:
                print("recommence")
            print(identifiant)

        self.bouton_save = Button(text="S'inscrire", width=30, height=1, font=("Helvetica", 16, tkFont.BOLD),
                                  bg="#dfe6e9", activebackground="#b2bec3", relief=RIDGE, command=buton_click)
        self.bouton_save.place(x=60, y=460)

        self.window.mainloop()

