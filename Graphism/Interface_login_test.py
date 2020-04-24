from Test.Interface_enregistrement_test import *
from verif_utilisateur import *


class Login2:

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

        self.lbl_id = Label(text="Identifiant:", font=("Helvetica", 14, tkFont.BOLD), bg="#2f3640", fg="#f5f6fa")
        self.lbl_id.place(x=44, y=272)

        entry_identifiant = self.txt_id = Entry(self.window, width=22, font=("Helvetica", 13))
        self.txt_id.place(x=263, y=273)

        self.lbl_mdp = Label(text="Mot de passe:", font=("Helvetica", 14, tkFont.BOLD), bg="#2f3640", fg="#f5f6fa")
        self.lbl_mdp.place(x=44, y=332)

        entry_password = self.txt_mdp = Entry(self.window, width=22, font=("Helvetica", 13), show="*")
        self.txt_mdp.place(x=263, y=333)

        self.lbl_mdp_oublie = Label(self.window, text="Mot de passe oublié", font=("Helvetica", 10, UNDERLINE),
                                    relief=FLAT, bg="#2f3640", fg="#00a8ff")
        self.lbl_mdp_oublie.place(x=300, y=358)
        self.lbl_mdp_oublie.bind("<Button-1>", mdp_oublie)

        def button_click_login():
            identifiant = str(entry_identifiant.get())
            password = str(entry_password.get())
            if verif_utilisateur(identifiant, password):
                print("Tu passes")
            else:
                print("Tu passes pas ")

        self.bouton_login = Button(text="Se connecter", width=30, height=1, font=("Helvetica", 16, tkFont.BOLD),
                                   bg="#dfe6e9", activebackground="#b2bec3", relief=RIDGE, command=button_click_login)
        self.bouton_login.place(x=60, y=415)

        self.bouton_register = Button(text="S'inscrire", width=30, height=1, font=("Helvetica", 16, tkFont.BOLD),
                                 bg="#dfe6e9", activebackground="#b2bec3", relief=RIDGE, command=self.register)
        self.bouton_register.place(x=60, y=460)

        self.window.mainloop()

    def register(self):
        self.window.destroy()
        a = Enregistrement()


def mdp_oublie(event):
    print("mdp oublié")
