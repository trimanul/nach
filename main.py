import numpy as np
from math import sqrt
from random import randint

from solver.solver import Solver
from queue import Empty

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QScrollArea, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QPainter, QFont, QFontDatabase, QPen, QPixmap, QPaintEvent, QColor, QPainterPath
import sys

# Equation of a line through 2 known dots:
# y = ((x - x1) * (y2 - y1) + y1 * (x2 - x1)) / (x2 - x1)

def count_cross(dot1_1, dot1_2, dot2_1, dot2_2):
    x1 = -dot1_1.x() / 4
    y1 = -dot1_1.y() / 4

    x2 = -dot1_2.x() / 4
    y2 = -dot1_2.y() / 4

    x3 = -dot2_1.x() / 4
    y3 = -dot2_1.y() / 4

    x4 = -dot2_2.x() / 4
    y4 = -dot2_2.y() / 4

    A = np.array([[(y2 - y1), (x2 - x1)], [(y4 - y3), (x4 - x3)]])
    B = np.array([(x1*(y2-y1) - y1*(x2-x1)), (x3*(y4-y3) - y3*(x4-x3))])

    xs = np.linalg.inv(A).dot(B)

    X = xs[0]
    Y = -xs[1]

    return X, Y 

def count_perp(dotc, dot1, loffset=80, roffset=20):
    v1_x = -dot1.x() / 4 - (-dotc.x() / 4)
    v1_y = -dot1.y() / 4 - (-dotc.y() / 4)

    #v1_x * x + v1_y * y = v1_x * (-dotc.x() / 4) + v1_y * (-dotc.y() / 4)

    X1 = (-dotc.x() / 4) + loffset
    Y1 = ((v1_x * (-dotc.x() / 4) + v1_y * (-dotc.y() / 4)) - v1_x * X1) / v1_y

    X2 = (-dotc.x() / 4) - roffset
    Y2 = ((v1_x * (-dotc.x() / 4) + v1_y * (-dotc.y() / 4)) - v1_x * X2) / v1_y

    return X1, Y1, X2, Y2


class SurveyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.widget = QWidget()

        self.vbox = QVBoxLayout()
        self.vbox.setAlignment(Qt.AlignLeft)

        hbox = QHBoxLayout()

        label1 = QLabel("Bx: ")
        self.Bxtxt = QLineEdit()

        hbox.addWidget(label1)
        hbox.addWidget(self.Bxtxt)

        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()

        label2 = QLabel("By: ")
        self.Bytxt = QLineEdit()

        hbox.addWidget(label2)
        hbox.addWidget(self.Bytxt)

        self.vbox.addLayout(hbox)


        hbox = QHBoxLayout()

        labelz = QLabel("Bz: ")
        self.Bztxt = QLineEdit()

        hbox.addWidget(labelz)
        hbox.addWidget(self.Bztxt)

        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()        

        label3 = QLabel("Cx: ")
        self.Cxtxt = QLineEdit()

        hbox.addWidget(label3)
        hbox.addWidget(self.Cxtxt)

        self.vbox.addLayout(hbox)


        hbox = QHBoxLayout()

        label4 = QLabel("Cy: ")
        self.Cytxt = QLineEdit()

        hbox.addWidget(label4)
        hbox.addWidget(self.Cytxt)

        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()

        labelz = QLabel("Cz: ")
        self.Cztxt = QLineEdit()

        hbox.addWidget(labelz)
        hbox.addWidget(self.Cztxt)

        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()

        label5 = QLabel("Ex: ")
        self.Extxt = QLineEdit()

        hbox.addWidget(label5)
        hbox.addWidget(self.Extxt)

        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()

        label6 = QLabel("Ey: ")
        self.Eytxt = QLineEdit()

        hbox.addWidget(label6)
        hbox.addWidget(self.Eytxt)

        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()

        labelz = QLabel("Ez: ")
        self.Eztxt = QLineEdit()

        hbox.addWidget(labelz)
        hbox.addWidget(self.Eztxt)

        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()

        label7 = QLabel("Fx: ")
        self.Fxtxt = QLineEdit()

        hbox.addWidget(label7)
        hbox.addWidget(self.Fxtxt)

        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()

        label8 = QLabel("Fy: ")
        self.Fytxt = QLineEdit()

        hbox.addWidget(label8)
        hbox.addWidget(self.Fytxt)

        self.vbox.addLayout(hbox)

        hbox = QHBoxLayout()

        labelz = QLabel("Fz: ")
        self.Fztxt = QLineEdit()

        hbox.addWidget(labelz)
        hbox.addWidget(self.Fztxt)

        self.vbox.addLayout(hbox)

    
        hbox = QHBoxLayout()
        self.btn = QPushButton("Proceed")
        self.final = QPushButton("Final")
        self.rand = QPushButton("Random")

        hbox.addWidget(self.btn)
        hbox.addWidget(self.final)
        hbox.addWidget(self.rand)

        self.vbox.addLayout(hbox)

        self.widget.setLayout(self.vbox)

        self.win = DrawingWindow()

        self.btn.clicked.connect(self.buttonClicked)
        self.final.clicked.connect(self.finalClicked)
        self.rand.clicked.connect(self.randClicked)

        self.setCentralWidget(self.widget)
        self.setGeometry(600, 100, 300, 400)
        self.setWindowTitle('?')
        self.show()

    def buttonClicked(self):
        self.hide()
        self.win.Bx = int(self.Bxtxt.text())
        self.win.By = int(self.Bytxt.text())
        self.win.Bz = int(self.Bztxt.text())

        self.win.Cx = int(self.Cxtxt.text())
        self.win.Cy = int(self.Cytxt.text())
        self.win.Cz = int(self.Cztxt.text())

        self.win.Ex = int(self.Extxt.text())
        self.win.Ey = int(self.Eytxt.text())
        self.win.Ez = int(self.Eztxt.text())

        self.win.Fx = int(self.Fxtxt.text())
        self.win.Fy = int(self.Fytxt.text())
        self.win.Fz = int(self.Fztxt.text())


        self.win.initUI()
        self.win.show()

    def finalClicked(self):
        self.hide()
        self.win.Bx = int(self.Bxtxt.text())
        self.win.By = int(self.Bytxt.text())
        self.win.Bz = int(self.Bztxt.text())

        self.win.Cx = int(self.Cxtxt.text())
        self.win.Cy = int(self.Cytxt.text())
        self.win.Cz = int(self.Cztxt.text())

        self.win.Ex = int(self.Extxt.text())
        self.win.Ey = int(self.Eytxt.text())
        self.win.Ez = int(self.Eztxt.text())

        self.win.Fx = int(self.Fxtxt.text())
        self.win.Fy = int(self.Fytxt.text())
        self.win.Fz = int(self.Fztxt.text())
        self.win.initUI()
        self.win.final()
        self.win.show()
        

    def randClicked(self):
            randBx = str(randint(70, 180))
            self.Bxtxt.setText(randBx)

            randBy = str(randint(0, 125))
            self.Bytxt.setText(randBy)

            randBz = str(randint(0, 145))
            self.Bztxt.setText(randBz)

            randCx = str(randint(35, 180))
            self.Cxtxt.setText(randCx)

            randCy = str(randint(0, 125))
            self.Cytxt.setText(randCy)

            randCz = str(randint(0, 145))
            self.Cztxt.setText(randCz)

            randEx = str(randint(35, 180))
            self.Extxt.setText(randEx)

            randEy = str(randint(0, 125))
            self.Eytxt.setText(randEy)

            randEz = str(randint(0, 125))
            self.Eztxt.setText(randEz)

            randFx = str(randint(35, 180))
            self.Fxtxt.setText(randFx)

            randFy = str(randint(0, 125))
            self.Fytxt.setText(randFy)

            randFz = str(randint(0, 145))
            self.Fztxt.setText(str(randint(0, 145)))

            with open("coords.csv", "w") as f:
                f.write(f" ,B,C,E,F\n X,{randBx},{randCx},{randEx},{randFx}\nY,{randBy},{randCy},{randEy},{randFy}\nZ,{randBz},{randCz},{randEz},{randFz}")

            self.widget.update()



class DrawingWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.Bx = 0
        self.By = 0
        self.Bz = 0

        self.Cx = 0
        self.Cy = 0
        self.Cz = 0

        self.Ex = 0
        self.Ey = 0
        self.Ez = 0

        self.Fx = 0
        self.Fy = 0
        self.Fz = 0


    def initUI(self):
        self.solution = Solver()

        self.scroll = QScrollArea()             
        self.widget = QWidget()                 
        self.pixmap = QPixmap(297 * 4, 420 * 4)   
        self.pixmap.fill(Qt.white)

        self.ZERO = QPoint(287 * 4 , 420 * 2 )

        self.label = QLabel()
        self.label.setPixmap(self.pixmap)


        self.btn = QPushButton("Next")

        self.hbox = QHBoxLayout()
        
        self.hbox.addWidget(self.btn)
        self.hbox.addWidget(self.label)
        self.hbox.setAlignment(Qt.AlignRight)

        self.widget.setLayout(self.hbox)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.btn.clicked.connect(self.buttonClicked)
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('Solution')
    

    def putDot(self, painter, x, y, name, dot_visible=True, let_visible=True):
        qp = painter
        dot = QPoint(-x * 4, -y * 4)
        if (dot_visible):
            qp.drawEllipse(dot, 2, 2)

        if(let_visible):
            qp.drawText(dot.x() + 4, dot.y() - 4, name)
        
        return dot

    def final(self):
        qp = QPainter(self.label.pixmap())
        qp.begin(self.label)
        qp.translate(self.ZERO)
        font = QFont("ГОСТ тип А")
        pen = QPen()
        pen.setWidth(1)
        qp.setFont(font)
        while True:
            code = self.solution.next_frame()
            if not code:
                self.solution.solution_queue.put("self.hide()\nsys.exit()")
                self.widget.update()
                qp.end()
                break

            exec(code)
            self.widget.update()


        qp.end()

        

    def buttonClicked(self):
        qp = QPainter(self.label.pixmap())
        qp.begin(self.label)
        qp.translate(self.ZERO)
        font = QFont("ГОСТ тип А")
        pen = QPen()
        pen.setWidth(1)
        qp.setFont(font)

        code = self.solution.next_frame()

        if not code:
                self.solution.solution_queue.put("self.hide()\nsys.exit()")
                code = self.solution.next_frame()
                exec(code)
                self.widget.update()
                qp.end()

        else:
            exec(code)

        self.widget.update()

        qp.end()
    
        


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = SurveyWindow()

    app.exec_()