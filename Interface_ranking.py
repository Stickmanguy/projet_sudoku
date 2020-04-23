from tkinter import *
import tkinter.font as tkFont
from Interface_function import *


class Ranking:

    def __init__(self, master):
        self.window = master

        self.window.title("Classement")
        self.window.geometry("500x453")
        self.window.resizable(width=False, height=False)
        self.window.configure(background="#902220")
        self.window.iconbitmap("icone.ico")

        canvas = Canvas(self.window, width=520, height=453, bg="#902220")
        ligne1 = canvas.create_line(260, 0, 260, 453)
        canvas.pack()

        self.main_menu = Menu(self.window)

        self.menu_option = Menu(self.main_menu, tearoff=0)
        self.menu_option.add_command(label="Quitter", command=self.exit)

        self.main_menu.add_cascade(label="Option", menu=self.menu_option)

        self.main_menu.add_command(label="Règles du jeu", command=rules)

        self.main_menu.add_command(label="À propos", command=about)

        self.lbl_clas = Label(self.window, text="Top classic:", font=("Helvetica", 18, tkFont.BOLD,
                              UNDERLINE), bg="#902220", fg="#f5f6fa")
        self.lbl_clas.place(x=75, y=40)

        self.lbl_mort = Label(self.window, text="Top mort subite:", font=("Helvetica", 18, tkFont.BOLD, UNDERLINE),
                              bg="#902220", fg="#f5f6fa")
        self.lbl_mort.place(x=280, y=40)

        self.lbl_n1 = Label(self.window, text="1:", font=("Helvetica", 18, tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_n1.place(x=30, y=90)

        self.txt_t1 = Entry(self.window, width=15, font=("Helvetica", 9))
        self.txt_t1.place(x=60, y=99)

        self.txt_tim1 = Entry(self.window, width=9, font=("Helvetica", 9))
        self.txt_tim1.place(x=180, y=99)

        self.lbl_n2 = Label(self.window, text="2:", font=("Helvetica", 18, tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_n2.place(x=30, y=140)

        self.txt_t2 = Entry(self.window, width=15, font=("Helvetica", 9))
        self.txt_t2.place(x=60, y=149)

        self.txt_tim2 = Entry(self.window, width=9, font=("Helvetica", 9))
        self.txt_tim2.place(x=180, y=149)

        self.lbl_n3 = Label(self.window, text="3:", font=("Helvetica", 18, tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_n3.place(x=30, y=190)

        self.txt_t3 = Entry(self.window, width=15, font=("Helvetica", 9))
        self.txt_t3.place(x=60, y=198)

        self.txt_tim3 = Entry(self.window, width=9, font=("Helvetica", 9))
        self.txt_tim3.place(x=180, y=198)

        self.lbl_n4 = Label(self.window, text="4:", font=("Helvetica", 18, tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_n4.place(x=30, y=240)

        self.txt_t4 = Entry(self.window, width=15, font=("Helvetica", 9))
        self.txt_t4.place(x=60, y=250)

        self.txt_tim4 = Entry(self.window, width=9, font=("Helvetica", 9))
        self.txt_tim4.place(x=180, y=250)

        self.lbl_n5 = Label(self.window, text="5:", font=("Helvetica", 18, tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_n5.place(x=30, y=290)

        self.txt_t5 = Entry(self.window, width=15, font=("Helvetica", 9))
        self.txt_t5.place(x=60, y=299)

        self.txt_tim5 = Entry(self.window, width=9, font=("Helvetica", 9))
        self.txt_tim5.place(x=180, y=299)

        self.txt_t6 = Entry(self.window, width=15, font=("Helvetica", 9))
        self.txt_t6.place(x=280, y=99)

        self.txt_t7 = Entry(self.window, width=15, font=("Helvetica", 9))
        self.txt_t7.place(x=280, y=149)

        self.txt_t8 = Entry(self.window, width=15, font=("Helvetica", 9))
        self.txt_t8.place(x=280, y=198)

        self.txt_t9 = Entry(self.window, width=15, font=("Helvetica", 9))
        self.txt_t9.place(x=280, y=250)

        self.txt_t6 = Entry(self.window, width=15, font=("Helvetica", 9))
        self.txt_t6.place(x=280, y=299)

        self.txt_tim6 = Entry(self.window, width=9, font=("Helvetica", 9))
        self.txt_tim6.place(x=400, y=99)

        self.txt_tim7 = Entry(self.window, width=9, font=("Helvetica", 9))
        self.txt_tim7.place(x=400, y=149)

        self.txt_tim8 = Entry(self.window, width=9, font=("Helvetica", 9))
        self.txt_tim8.place(x=400, y=198)

        self.txt_tim9 = Entry(self.window, width=9, font=("Helvetica", 9))
        self.txt_tim9.place(x=400, y=249)

        self.txt_tim10 = Entry(self.window, width=9, font=("Helvetica", 9))
        self.txt_tim10.place(x=400, y=299)

        self.window.config(menu=self.main_menu)

    def exit(self):
        self.window.destroy()
