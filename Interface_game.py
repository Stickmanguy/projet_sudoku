from timeit import default_timer
from tkinter import *
from create_sudoku import *


class Game:

    def __init__(self):

        self.window = Tk()

        self.window.title("Sudoku mania")
        self.window.geometry("478x690")
        self.window.resizable(width=False, height=False)
        self.window.configure(background="#902220")
        self.window.iconbitmap("icone.ico")

        self.lbl_time = Label(text="10:10:00", font=("times", 50, "bold"), relief=GROOVE, bd=5, bg="#2c3e50",
                              fg="#ecf0f1")
        self.lbl_time.place(x=110)

        self.btn_grid = []

        self.btn_0_0 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(0))
        self.btn_0_0.place(x=40, y=130)
        self.btn_grid.append(self.btn_0_0)

        self.btn_0_1 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(1))
        self.btn_0_1.place(x=84, y=130)
        self.btn_grid.append(self.btn_0_1)

        self.btn_0_2 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(2))
        self.btn_0_2.place(x=128, y=130)
        self.btn_grid.append(self.btn_0_2)

        self.btn_0_3 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(3))
        self.btn_0_3.place(x=174, y=130)
        self.btn_grid.append(self.btn_0_3)

        self.btn_0_4 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(4))
        self.btn_0_4.place(x=218, y=130)
        self.btn_grid.append(self.btn_0_4)

        self.btn_0_5 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(5))
        self.btn_0_5.place(x=262, y=130)
        self.btn_grid.append(self.btn_0_5)

        self.btn_0_6 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(6))
        self.btn_0_6.place(x=308, y=130)
        self.btn_grid.append(self.btn_0_6)

        self.btn_0_7 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(7))
        self.btn_0_7.place(x=352, y=130)
        self.btn_grid.append(self.btn_0_7)

        self.btn_0_8 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(8))
        self.btn_0_8.place(x=396, y=130)
        self.btn_grid.append(self.btn_0_8)

        self.btn_1_0 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(9))
        self.btn_1_0.place(x=40, y=170)
        self.btn_grid.append(self.btn_1_0)

        self.btn_1_1 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(10))
        self.btn_1_1.place(x=84, y=170)
        self.btn_grid.append(self.btn_1_1)

        self.btn_1_2 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(11))
        self.btn_1_2.place(x=128, y=170)
        self.btn_grid.append(self.btn_1_2)

        self.btn_1_3 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(12))
        self.btn_1_3.place(x=174, y=170)
        self.btn_grid.append(self.btn_1_3)

        self.btn_1_4 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(13))
        self.btn_1_4.place(x=218, y=170)
        self.btn_grid.append(self.btn_1_4)

        self.btn_1_5 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(14))
        self.btn_1_5.place(x=262, y=170)
        self.btn_grid.append(self.btn_1_5)

        self.btn_1_6 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(15))
        self.btn_1_6.place(x=308, y=170)
        self.btn_grid.append(self.btn_1_6)

        self.btn_1_7 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(16))
        self.btn_1_7.place(x=352, y=170)
        self.btn_grid.append(self.btn_1_7)

        self.btn_1_8 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(17))
        self.btn_1_8.place(x=396, y=170)
        self.btn_grid.append(self.btn_1_8)

        self.btn_2_0 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(18))
        self.btn_2_0.place(x=40, y=210)
        self.btn_grid.append(self.btn_2_0)

        self.btn_2_1 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(19))
        self.btn_2_1.place(x=84, y=210)
        self.btn_grid.append(self.btn_2_1)

        self.btn_2_2 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(20))
        self.btn_2_2.place(x=128, y=210)
        self.btn_grid.append(self.btn_2_2)

        self.btn_2_3 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(21))
        self.btn_2_3.place(x=174, y=210)
        self.btn_grid.append(self.btn_2_3)

        self.btn_2_4 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(22))
        self.btn_2_4.place(x=218, y=210)
        self.btn_grid.append(self.btn_2_4)

        self.btn_2_5 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(23))
        self.btn_2_5.place(x=262, y=210)
        self.btn_grid.append(self.btn_2_5)

        self.btn_2_6 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(24))
        self.btn_2_6.place(x=308, y=210)
        self.btn_grid.append(self.btn_2_6)

        self.btn_2_7 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(25))
        self.btn_2_7.place(x=352, y=210)
        self.btn_grid.append(self.btn_2_7)

        self.btn_2_8 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(26))
        self.btn_2_8.place(x=396, y=210)
        self.btn_grid.append(self.btn_2_8)

        self.btn_3_0 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(27))
        self.btn_3_0.place(x=40, y=252)
        self.btn_grid.append(self.btn_3_0)

        self.btn_3_1 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(28))
        self.btn_3_1.place(x=84, y=252)
        self.btn_grid.append(self.btn_3_1)

        self.btn_3_2 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(29))
        self.btn_3_2.place(x=128, y=252)
        self.btn_grid.append(self.btn_3_2)

        self.btn_3_3 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(30))
        self.btn_3_3.place(x=174, y=252)
        self.btn_grid.append(self.btn_3_3)

        self.btn_3_4 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(31))
        self.btn_3_4.place(x=218, y=252)
        self.btn_grid.append(self.btn_3_4)

        self.btn_3_5 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(32))
        self.btn_3_5.place(x=262, y=252)
        self.btn_grid.append(self.btn_3_5)

        self.btn_3_6 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(33))
        self.btn_3_6.place(x=308, y=252)
        self.btn_grid.append(self.btn_3_6)

        self.btn_3_7 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(34))
        self.btn_3_7.place(x=352, y=252)
        self.btn_grid.append(self.btn_3_7)

        self.btn_3_8 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(35))
        self.btn_3_8.place(x=396, y=252)
        self.btn_grid.append(self.btn_3_8)

        self.btn_4_0 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(36))
        self.btn_4_0.place(x=40, y=292)
        self.btn_grid.append(self.btn_4_0)

        self.btn_4_1 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(37))
        self.btn_4_1.place(x=84, y=292)
        self.btn_grid.append(self.btn_4_1)

        self.btn_4_2 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(38))
        self.btn_4_2.place(x=128, y=292)
        self.btn_grid.append(self.btn_4_2)

        self.btn_4_3 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(39))
        self.btn_4_3.place(x=174, y=292)
        self.btn_grid.append(self.btn_4_3)

        self.btn_4_4 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(40))
        self.btn_4_4.place(x=218, y=292)
        self.btn_grid.append(self.btn_4_4)

        self.btn_4_5 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(41))
        self.btn_4_5.place(x=262, y=292)
        self.btn_grid.append(self.btn_4_5)

        self.btn_4_6 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(42))
        self.btn_4_6.place(x=308, y=292)
        self.btn_grid.append(self.btn_4_6)

        self.btn_4_7 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(43))
        self.btn_4_7.place(x=352, y=292)
        self.btn_grid.append(self.btn_4_7)

        self.btn_4_8 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(44))
        self.btn_4_8.place(x=396, y=292)
        self.btn_grid.append(self.btn_4_8)

        self.btn_5_0 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(45))
        self.btn_5_0.place(x=40, y=332)
        self.btn_grid.append(self.btn_5_0)

        self.btn_5_1 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(46))
        self.btn_5_1.place(x=84, y=332)
        self.btn_grid.append(self.btn_5_1)

        self.btn_5_2 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(47))
        self.btn_5_2.place(x=128, y=332)
        self.btn_grid.append(self.btn_5_2)

        self.btn_5_3 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(48))
        self.btn_5_3.place(x=174, y=332)
        self.btn_grid.append(self.btn_5_3)

        self.btn_5_4 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(49))
        self.btn_5_4.place(x=218, y=332)
        self.btn_grid.append(self.btn_5_4)

        self.btn_5_5 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(50))
        self.btn_5_5.place(x=262, y=332)
        self.btn_grid.append(self.btn_5_5)

        self.btn_5_6 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(51))
        self.btn_5_6.place(x=308, y=332)
        self.btn_grid.append(self.btn_5_6)

        self.btn_5_7 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(52))
        self.btn_5_7.place(x=352, y=332)
        self.btn_grid.append(self.btn_5_7)

        self.btn_5_8 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(53))
        self.btn_5_8.place(x=396, y=332)
        self.btn_grid.append(self.btn_5_8)

        self.btn_6_0 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(54))
        self.btn_6_0.place(x=40, y=374)
        self.btn_grid.append(self.btn_6_0)

        self.btn_6_1 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(55))
        self.btn_6_1.place(x=84, y=374)
        self.btn_grid.append(self.btn_6_1)

        self.btn_6_2 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(56))
        self.btn_6_2.place(x=128, y=374)
        self.btn_grid.append(self.btn_6_2)

        self.btn_6_3 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(57))
        self.btn_6_3.place(x=174, y=374)
        self.btn_grid.append(self.btn_6_3)

        self.btn_6_4 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(58))
        self.btn_6_4.place(x=218, y=374)
        self.btn_grid.append(self.btn_6_4)

        self.btn_6_5 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(59))
        self.btn_6_5.place(x=262, y=374)
        self.btn_grid.append(self.btn_6_5)

        self.btn_6_6 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(60))
        self.btn_6_6.place(x=308, y=374)
        self.btn_grid.append(self.btn_6_6)

        self.btn_6_7 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(61))
        self.btn_6_7.place(x=352, y=374)
        self.btn_grid.append(self.btn_6_7)

        self.btn_6_8 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(62))
        self.btn_6_8.place(x=396, y=374)
        self.btn_grid.append(self.btn_6_8)

        self.btn_7_0 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(63))
        self.btn_7_0.place(x=40, y=414)
        self.btn_grid.append(self.btn_7_0)

        self.btn_7_1 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(64))
        self.btn_7_1.place(x=84, y=414)
        self.btn_grid.append(self.btn_7_1)

        self.btn_7_2 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(65))
        self.btn_7_2.place(x=128, y=414)
        self.btn_grid.append(self.btn_7_2)

        self.btn_7_3 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(66))
        self.btn_7_3.place(x=174, y=414)
        self.btn_grid.append(self.btn_7_3)

        self.btn_7_4 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(67))
        self.btn_7_4.place(x=218, y=414)
        self.btn_grid.append(self.btn_7_4)

        self.btn_7_5 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(68))
        self.btn_7_5.place(x=262, y=414)
        self.btn_grid.append(self.btn_7_5)

        self.btn_7_6 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(69))
        self.btn_7_6.place(x=308, y=414)
        self.btn_grid.append(self.btn_7_6)

        self.btn_7_7 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(70))
        self.btn_7_7.place(x=352, y=414)
        self.btn_grid.append(self.btn_7_7)

        self.btn_7_8 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(71))
        self.btn_7_8.place(x=396, y=414)
        self.btn_grid.append(self.btn_7_8)

        self.btn_8_0 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(72))
        self.btn_8_0.place(x=40, y=454)
        self.btn_grid.append(self.btn_8_0)

        self.btn_8_1 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(73))
        self.btn_8_1.place(x=84, y=454)
        self.btn_grid.append(self.btn_8_1)

        self.btn_8_2 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(74))
        self.btn_8_2.place(x=128, y=454)
        self.btn_grid.append(self.btn_8_2)

        self.btn_8_3 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(75))
        self.btn_8_3.place(x=174, y=454)
        self.btn_grid.append(self.btn_8_3)

        self.btn_8_4 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(76))
        self.btn_8_4.place(x=218, y=454)
        self.btn_grid.append(self.btn_8_4)

        self.btn_8_5 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(77))
        self.btn_8_5.place(x=262, y=454)
        self.btn_grid.append(self.btn_8_5)

        self.btn_8_6 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(78))
        self.btn_8_6.place(x=308, y=454)
        self.btn_grid.append(self.btn_8_6)

        self.btn_8_7 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(79))
        self.btn_8_7.place(x=352, y=454)
        self.btn_grid.append(self.btn_8_7)

        self.btn_8_8 = Button(self.window, width=3, font=("Helvetica", 14), relief=FLAT,
                              command=lambda: self.selected(80))
        self.btn_8_8.place(x=396, y=454)
        self.btn_grid.append(self.btn_8_8)

        self.btn1 = Button(text="1", width=3, font=("Helvetica", 15), relief=FLAT)
        self.btn1.place(x=106, y=530)

        self.btn2 = Button(text="2", width=3, font=("Helvetica", 15), relief=FLAT)
        self.btn2.place(x=151, y=530)

        self.btn3 = Button(text="3", width=3, font=("Helvetica", 15), relief=FLAT)
        self.btn3.place(x=196, y=530)

        self.btn4 = Button(text="4", width=3, font=("Helvetica", 15), relief=FLAT)
        self.btn4.place(x=106, y=572)

        self.btn5 = Button(text="5", width=3, font=("Helvetica", 15), relief=FLAT)
        self.btn5.place(x=151, y=572)

        self.btn6 = Button(text="6", width=3, font=("Helvetica", 15), relief=FLAT)
        self.btn6.place(x=196, y=572)

        self.btn7 = Button(text="7", width=3, font=("Helvetica", 15), relief=FLAT)
        self.btn7.place(x=106, y=614)

        self.btn8 = Button(text="8", width=3, font=("Helvetica", 15), relief=FLAT)
        self.btn8.place(x=151, y=614)

        self.btn9 = Button(text="9", width=3, font=("Helvetica", 15), relief=FLAT)
        self.btn9.place(x=196, y=614)

        self.btn_supp = Button(text="Effacer", width=6, font=("Helvetica", 15), relief=FLAT)
        self.btn_supp.place(x=357, y=530)

        self.btn_exit = Button(text="Quitter", width=6, font=("Helvetica", 15), relief=FLAT)
        self.btn_exit.place(x=357, y=614)

        self.start = default_timer()
        self.update_clock()
        sudoku_01 = CreateSudoku()
        for ligne in range(0, 9):
            for col in range(0, 9):
                lc = ligne * 9 + col
                self.btn_grid[lc].config(text=str(sudoku_01.data[ligne, col]))

        self.window.mainloop()
    def update_sudoku(self, tableau):
        for ligne in range(0, 9):
            for col in range(0, 9):
                lc = ligne * 9 + col
                self.btn_grid[lc].config(text=str(sudoku_01.data[ligne, col]))
                
    def update_clock(self):
        now = default_timer() - self.start
        minutes, seconds = divmod(now, 60)
        hours, minutes = divmod(minutes, 60)
        str_time = "%02d:%02d:%02d" % (hours, minutes, seconds)
        self.lbl_time.configure(text=str_time)
        self.window.after(1000, self.update_clock)

    def selected(self, lc):
        print(lc)


