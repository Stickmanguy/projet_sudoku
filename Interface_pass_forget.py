from tkinter import *
import tkinter.font as tkFont
from tkinter import Tk


class Password_forget:

    def __init__(self, master):

        self.window = master

        self.window.title("Sudoku mania")
        self.window.geometry("520x360")
        self.window.resizable(width=False, height=False)
        self.window.configure(background="#902220")
        self.window.iconbitmap("icone.ico")

        self.logo = PhotoImage(file='logo_projet.png')
        self.image = Label(image=self.logo, bg="#902220")
        self.image.pack()

        self.lbl_mail = Label(text="Email:", font=("Helvetica", 18, tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_mail.place(x=55, y=228)

        self.txt_mail = Entry(self.window, width=22, font=("Helvetica", 13))
        self.txt_mail.place(x=263, y=233)

        self.btn_confirm = Button(text="Envoyer mail de recuperation", width=30, height=1, font=("Helvetica", 16, tkFont.BOLD),
                                  bg="#dfe6e9", activebackground="#b2bec3", relief=FLAT)
        self.btn_confirm.place(x=60, y=293)
