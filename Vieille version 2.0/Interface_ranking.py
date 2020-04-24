from tkinter import *
import tkinter.font as tkFont
from Interface_function import *
import json


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

        self.user_list_classique = []
        self.user_list_subite = []
        self.rank_classique = []
        self.rank_subite = []

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

        self.txt_t1 = Label(self.window, width=15, font=("Helvetica", 9))
        self.txt_t1.place(x=60, y=99)
        self.user_list_classique.append(self.txt_t1)

        self.txt_tim1 = Label(self.window, text="", width=9, font=("Helvetica", 9))
        self.txt_tim1.place(x=180, y=99)
        self.rank_classique.append(self.txt_tim1)

        self.lbl_n2 = Label(self.window, text="2:", font=("Helvetica", 18, tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_n2.place(x=30, y=140)

        self.txt_t2 = Label(self.window, text="", width=15, font=("Helvetica", 9))
        self.txt_t2.place(x=60, y=149)
        self.user_list_classique.append(self.txt_t2)

        self.txt_tim2 = Label(self.window, text="", width=9, font=("Helvetica", 9))
        self.txt_tim2.place(x=180, y=149)
        self.rank_classique.append(self.txt_tim2)

        self.lbl_n3 = Label(self.window, text="3:", font=("Helvetica", 18, tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_n3.place(x=30, y=190)

        self.txt_t3 = Label(self.window, text="", width=15, font=("Helvetica", 9))
        self.txt_t3.place(x=60, y=198)
        self.user_list_classique.append(self.txt_t3)

        self.txt_tim3 = Label(self.window, text="", width=9, font=("Helvetica", 9))
        self.txt_tim3.place(x=180, y=198)
        self.rank_classique.append(self.txt_tim3)

        self.lbl_n4 = Label(self.window, text="4:", font=("Helvetica", 18, tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_n4.place(x=30, y=240)

        self.txt_t4 = Label(self.window, text="", width=15, font=("Helvetica", 9))
        self.txt_t4.place(x=60, y=250)
        self.user_list_classique.append(self.txt_t4)

        self.txt_tim4 = Label(self.window, text="", width=9, font=("Helvetica", 9))
        self.txt_tim4.place(x=180, y=250)
        self.rank_classique.append(self.txt_tim4)

        self.lbl_n5 = Label(self.window, text="5:", font=("Helvetica", 18, tkFont.BOLD), bg="#902220", fg="#f5f6fa")
        self.lbl_n5.place(x=30, y=290)

        self.txt_t5 = Label(self.window, text="", width=15, font=("Helvetica", 9))
        self.txt_t5.place(x=60, y=299)
        self.user_list_classique.append(self.txt_t5)

        self.txt_tim5 = Label(self.window, text="", width=9, font=("Helvetica", 9))
        self.txt_tim5.place(x=180, y=299)
        self.rank_classique.append(self.txt_tim5)

        self.txt_t6 = Label(self.window, text="", width=15, font=("Helvetica", 9))
        self.txt_t6.place(x=280, y=99)
        self.user_list_subite.append(self.txt_t6)

        self.txt_t7 = Label(self.window, text="", width=15, font=("Helvetica", 9))
        self.txt_t7.place(x=280, y=149)
        self.user_list_subite.append(self.txt_t7)

        self.txt_t8 = Label(self.window, text="", width=15, font=("Helvetica", 9))
        self.txt_t8.place(x=280, y=198)
        self.user_list_subite.append(self.txt_t8)

        self.txt_t9 = Label(self.window, text="", width=15, font=("Helvetica", 9))
        self.txt_t9.place(x=280, y=250)
        self.user_list_subite.append(self.txt_t9)

        self.txt_t10 = Label(self.window, text="", width=15, font=("Helvetica", 9))
        self.txt_t10.place(x=280, y=299)
        self.user_list_subite.append(self.txt_t10)

        self.txt_tim6 = Label(self.window, text="", width=9, font=("Helvetica", 9))
        self.txt_tim6.place(x=400, y=99)
        self.rank_subite.append(self.txt_tim6)

        self.txt_tim7 = Label(self.window, text="", width=9, font=("Helvetica", 9))
        self.txt_tim7.place(x=400, y=149)
        self.rank_subite.append(self.txt_tim7)

        self.txt_tim8 = Label(self.window, text="", width=9, font=("Helvetica", 9))
        self.txt_tim8.place(x=400, y=198)
        self.rank_subite.append(self.txt_tim8)

        self.txt_tim9 = Label(self.window, text="", width=9, font=("Helvetica", 9))
        self.txt_tim9.place(x=400, y=249)
        self.rank_subite.append(self.txt_tim9)

        self.txt_tim10 = Label(self.window, text="", width=9, font=("Helvetica", 9))
        self.txt_tim10.place(x=400, y=299)
        self.rank_subite.append(self.txt_tim10)

        self.window.config(menu=self.main_menu)

        self.classement_classique = []
        self.classement_subite = []
        self.classement_classique_trie = []
        self.classement_subite_trie = []
        self.i = 0

        with open('user.json', 'r', encoding='utf-8') as json_file:
            user_list = json.load(json_file)
            json_file.close()
            for p in user_list['people']:
                self.classement_classique.append(p['ranking_classique'])
                self.classement_subite.append(p['raking_subite'])
                self.i = self.i + 1

        for p in sorted(self.classement_classique, reverse=True):
            self.classement_classique_trie.append(p)

        for p in sorted(self.classement_subite, reverse=True):
            self.classement_subite_trie.append(p)

        if self.i > 5: self.i = 5

        for i in range(self.i):
            self.rank_classique[i].config(text=str(self.classement_classique_trie[i]))
            self.rank_subite[i].config(text=str(self.classement_subite_trie[i]))

        with open('user.json', 'r', encoding='utf-8') as json_file:
            user_list = json.load(json_file)
            json_file.close()
            for i in range(self.i):
                for p in user_list['people']:
                    if p['ranking_classique'] == self.classement_classique_trie[i]:
                        self.user_list_classique[i].config(text=str(p['name']))
                        if i > 3:
                            break

        with open('user.json', 'r', encoding='utf-8') as json_file:
            user_list = json.load(json_file)
            json_file.close()
            for i in range(self.i):
                for p in user_list['people']:
                    if p['raking_subite'] == self.classement_subite_trie[i]:
                        self.user_list_subite[i].config(text=str(p['name']))
                        if i > 3:
                            break

    def exit(self):
        self.window.destroy()
