from tkinter import *
import tkinter.font as tkFont


class Password_change:

    def __init__(self, master):

        self.window = master

        self.window.title("Changement de mot de passe")
        self.window.geometry("520x550")
        self.window.resizable(width=False, height=False)
        self.window.configure(background="#902220")
        self.window.iconbitmap("icone.ico")

        self.logo = PhotoImage(file='logo_projet.png')
        self.image = Label(self.window, image=self.logo, bg="#902220")
        self.image.pack()

        self.lbl_id = Label(self.window, text="Identifiant:", font=("Helvetica", 12, tkFont.BOLD), bg="#902220",
                            fg="#f5f6fa")
        self.lbl_id.place(x=44, y=243)
        self.lbl_id = Entry(self.window, width=22, font=("Helvetica", 13))
        self.lbl_id.place(x=263, y=243)

        self.lbl_pass = Label(self.window, text="Mot de passe actuel:", font=("Helvetica", 12, tkFont.BOLD),
                              bg="#902220", fg="#f5f6fa")
        self.lbl_pass.place(x=44, y=303)
        self.txt_pass = Entry(self.window, width=22, font=("Helvetica", 13), show="*")
        self.txt_pass.place(x=263, y=303)

        self.lbl_new_pass = Label(self.window, text="Nouveau mot de passe:", font=("Helvetica", 12, tkFont.BOLD),
                                  bg="#902220", fg="#f5f6fa")
        self.lbl_new_pass.place(x=44, y=363)
        self.txt_new_pass = Entry(self.window, width=22, font=("Helvetica", 13), show="*")
        self.txt_new_pass.place(x=263, y=363)

        self.lbl_new_pass_2 = Label(self.window, text="Confirmer le mot de passe:", font=("Helvetica", 12,
                                    tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_new_pass_2.place(x=44, y=423)
        self.lbl_new_pass_2 = Entry(self.window, width=22, font=("Helvetica", 13), show="*")
        self.lbl_new_pass_2.place(x=263, y=423)

        self.btn_confirm = Button(self.window, text="Changer le mot de passe", width=30, height=1, font=("Helvetica",
                                  16, tkFont.BOLD), bg="#dfe6e9", activebackground="#b2bec3", relief=FLAT)
        self.btn_confirm.place(x=60, y=480)