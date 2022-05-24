import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QGridLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # klasa bazowa konstruktor QmainWindow
        self.stan = [[0, 0, 2, 0], [0, 2, 0, 0], [0, 4, 0, 0], [0, 4, 0, 0]]
        self.puste = 0

        self.setMinimumSize(QSize(1000, 600))
        self.setWindowTitle("2048 ZAPRASZAM DO GRY")
        self.pybutton1 = QLabel(str(self.stan[0][0]), self)
        self.pybutton1.resize(100, 100)
        self.pybutton1.move(100, 50)

        self.pybutton2 = QLabel(str(self.stan[0][1]), self)
        self.pybutton2.resize(100, 100)
        self.pybutton2.move(200, 50)

        self.pybutton3 = QLabel(str(self.stan[0][2]), self)
        self.pybutton3.resize(100, 100)
        self.pybutton3.move(300, 50)

        self.pybutton4 = QLabel(str(self.stan[0][3]), self)
        self.pybutton4.resize(100, 100)
        self.pybutton4.move(400, 50)

        self.pybutton5 = QLabel(str(self.stan[1][0]), self)
        self.pybutton5.resize(100, 100)
        self.pybutton5.move(100, 150)
        self.pybutton6 = QLabel(str(self.stan[1][1]), self)
        self.pybutton6.resize(100, 100)
        self.pybutton6.move(200, 150)
        self.pybutton7 = QLabel(str(self.stan[1][2]), self)
        self.pybutton7.resize(100, 100)
        self.pybutton7.move(300, 150)
        self.pybutton8 = QLabel(str(self.stan[1][3]), self)
        self.pybutton8.resize(100, 100)
        self.pybutton8.move(400, 150)

        self.pybutton9 = QLabel(str(self.stan[2][0]), self)
        self.pybutton9.resize(100, 100)
        self.pybutton9.move(100, 250)
        self.pybutton10 = QLabel(str(self.stan[2][1]), self)
        self.pybutton10.resize(100, 100)
        self.pybutton10.move(200, 250)
        self.pybutton11 = QLabel(str(self.stan[2][2]), self)
        self.pybutton11.resize(100, 100)
        self.pybutton11.move(300, 250)
        self.pybutton12 = QLabel(str(self.stan[2][3]), self)
        self.pybutton12.resize(100, 100)
        self.pybutton12.move(400, 250)

        self.pybutton13 = QLabel(str(self.stan[3][0]), self)
        self.pybutton13.resize(100, 100)
        self.pybutton13.move(100, 350)
        self.pybutton14 = QLabel(str(self.stan[3][1]), self)
        self.pybutton14.resize(100, 100)
        self.pybutton14.move(200, 350)
        self.pybutton15 = QLabel(str(self.stan[3][2]), self)
        self.pybutton15.resize(100, 100)
        self.pybutton15.move(300, 350)
        self.pybutton16 = QLabel(str(self.stan[3][3]), self)
        self.pybutton16.resize(100, 100)
        self.pybutton16.move(400, 350)
        self.pybutton16.setStyleSheet("background-color: lightgreen")
        self.pybutton15.setStyleSheet("background-color: green")

        self.up = QPushButton("up", self)
        self.up.resize(100, 100)
        self.up.move(600, 150)
        self.up.clicked.connect(self.koniecruchup)

        self.down= QPushButton("down", self)
        self.down.resize(100, 100)
        self.down.move(600, 250)
        self.down.clicked.connect(self.koniecruchdown)
        self.left = QPushButton("left", self)
        self.left.resize(100, 100)
        self.left.move(500, 200)
        self.left.clicked.connect(self.koniecruchleft)
        self.right = QPushButton("right", self)
        self.right.resize(100, 100)
        self.right.move(700, 200)
        self.right.clicked.connect(self.koniecruchright)



    def tmp(self):
        self.pybutton1.setText(str(self.stan[0][0]))
        self.pybutton2.setText(str(self.stan[0][1]))
        self.pybutton3.setText(str(self.stan[0][2]))
        self.pybutton4.setText(str(self.stan[0][3]))
        self.pybutton5.setText(str(self.stan[1][0]))
        self.pybutton6.setText(str(self.stan[1][1]))
        self.pybutton7.setText(str(self.stan[1][2]))
        self.pybutton8.setText(str(self.stan[1][3]))
        self.pybutton9.setText(str(self.stan[2][0]))
        self.pybutton10.setText(str(self.stan[2][1]))
        self.pybutton11.setText(str(self.stan[2][2]))
        self.pybutton12.setText(str(self.stan[2][3]))
        self.pybutton13.setText(str(self.stan[3][0]))
        self.pybutton14.setText(str(self.stan[3][1]))
        self.pybutton15.setText(str(self.stan[3][2]))
        self.pybutton16.setText(str(self.stan[3][3]))

    def motionup(self):
        print('up')
        while (True):
            zmiana = 0
            for j in range(1, 4):
                for i in range(0, 4):
                    if self.stan[j][i] != 0 and self.stan[j - 1][i] == 0:
                        zmiana = 1
                        self.stan[j][i], self.stan[j - 1][i] = self.stan[j - 1][i], self.stan[j][i]
            if (zmiana == 0):
                break




    def motiondown(self):
        # 1 up , 2 right, 3 down, 4 left
        print('down')
        while (True):
            zmiana = 0
            for j in range(0, 3):
                for i in range(0, 4):
                    if self.stan[j][i] != 0 and self.stan[j + 1][i] == 0:
                        zmiana = 1
                        self.stan[j][i], self.stan[j + 1][i] = self.stan[j + 1][i], self.stan[j][i]
            if (zmiana == 0):
                break



    def motionleft(self):
        # 1 up , 2 right, 3 down, 4 left
        print('left')
        while (True):
            zmiana = 0
            for j in range(0, 4):
                for i in range(1, 4):
                    if self.stan[j][i] != 0 and self.stan[j][i - 1] == 0:
                        zmiana = 1
                        self.stan[j][i], self.stan[j][i - 1] = self.stan[j][i - 1], self.stan[j][i]
            if (zmiana == 0):
                break

        self.newbox()
        self.tmp()

    def motionright(self):
        # 1 up , 2 right, 3 down, 4 left
        while (True):
            zmiana = 0
            for j in range(0, 4):
                for i in range(0, 3):
                    if self.stan[j][i] != 0 and self.stan[j][i + 1] == 0:
                        zmiana = 1
                        self.stan[j][i], self.stan[j][i + 1] = self.stan[j][i + 1], self.stan[j][i]
            if (zmiana == 0):
                break
        print('right')
        self.newbox()
        self.tmp()

    def sprawdzpuste(self):
        self.puste = 0
        for j in range(0, 4):
            for i in range(0, 4):
                if self.stan[j][i] == 0:
                    self.puste = self.puste + 1
        print(self.puste)

    def newbox(self):
        self.sprawdzpuste()
        if (self.puste != 0):
            y = random.randint(1, self.puste)
            print(y)
            z = 0
            for j in range(0, 4):
                for i in range(0, 4):
                    if self.stan[j][i] == 0:
                        z = z + 1
                        if (z == y):
                            self.stan[j][i] = random.randint(1, 2) * 2
                            break
        else:
            print("Koniec gry przegrałeś")
    def lacznieup(self):
        for j in range(0, 3):
            for i in range(0,4):
                if self.stan[j][i]==self.stan[j+1][i] and self.stan[j][i]!=0:
                    self.stan[j][i]=self.stan[j][i]*2
                    self.stan[j+1][i ]=0
                    self.motionup()

    def laczniedown(self):
        for j in range(1, 4):
            for i in range(0,4):
                if self.stan[3-j][i] == self.stan[3-j+1][i] and self.stan[3-j][i] != 0:
                    self.stan[3-j][i] = self.stan[3-j][i]*2
                    self.stan[3-j+1][i] = 0
                    self.motiondown()
    def lacznieleft(self):
        for j in range(0, 4):
            for i in range(0,3):
                if self.stan[j][i] == self.stan[j][i+1] and self.stan[j][i] != 0:
                    self.stan[j][i] = self.stan[j][i]*2
                    self.stan[j][i+1] = 0
                    self.motionleft()
    def lacznieright(self):
        for j in range(0, 4):
            for i in range(0,3):
                if self.stan[j][3-i] == self.stan[j][2-i] and self.stan[j][3-i] != 0:
                    self.stan[j][3-i] = self.stan[j][3-i]*2
                    self.stan[j][2-i] = 0
                    self.motionright()


    def koniecruchup(self):
        self.motionup()
        self.lacznieup()
        self.newbox()
        self.tmp()

    def koniecruchdown(self):
        self.motiondown()
        self.laczniedown()
        self.newbox()
        self.tmp()
    def koniecruchright(self):
        self.motionright()
        self.lacznieright()
        self.newbox()
        self.tmp()
    def koniecruchleft(self):
        self.motionleft()
        self.lacznieleft()
        self.newbox()
        self.tmp()
if __name__ == '__main__':

    app = QApplication(sys.argv)

    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


