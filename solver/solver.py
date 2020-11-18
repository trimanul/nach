import queue
from time import sleep

class Solver(object):

    def __init__(self):

        self.solution_queue = queue.Queue()

        code = """
#Draw axes
qp.drawLine(0, 0, -280 * 4, 0)
path = QPainterPath()
path.moveTo(-280 * 4, 0)
path.lineTo(-280 * 4 + 7 * 4, 0)
path.lineTo(-280 * 4 + 7 * 4, 1 * 4)
path.lineTo(-280 * 4, 0)
path.lineTo(-280 * 4 + 7 * 4, -1 * 4)
path.lineTo(-280 * 4 + 7 * 4, 0)

qp.drawLine(0, 0, 0, 400 * 2)
path.moveTo(0, 400 * 2)
path.lineTo(0, 400 * 2 - 7 * 4)
path.lineTo(0 - 1 * 4, 400 * 2 - 7 * 4)
path.lineTo(0, 400 * 2)
path.lineTo(0 + 1 * 4, 400 * 2 - 7 * 4)
path.lineTo(0, 400 * 2 - 7 * 4)


qp.drawLine(0, 0, 0, -400 * 2)
path.moveTo(0, -400 * 2)
path.lineTo(0, -400 * 2 + 7 * 4)
path.lineTo(0 - 1 * 4, -400 * 2 + 7 * 4)
path.lineTo(0, -400 * 2)
path.lineTo(0 + 1 * 4, -400 * 2 + 7 * 4)
path.lineTo(0, -400 * 2 + 7 * 4)

qp.drawPath(path)
qp.fillPath(path, Qt.black)

"""
        self.solution_queue.put(code)



        code = """
#Draw initial points' frontal projections
self.B = self.putDot(qp, self.Bx, self.Bz, "B'\'")

self.C = self.putDot(qp, self.Cx, self.Cz, "C\'\'")


self.E = self.putDot(qp, self.Ex, self.Ez, "E\'\'")

self.F = self.putDot(qp, self.Fx, self.Fz, "F\'\'")

qp.drawLine(self.C, self.B)
qp.drawLine(self.E, self.F)
"""
        self.solution_queue.put(code)


        code = """
#Draw initial points' horizontal projections
self.Bf = self.putDot(qp, self.Bx, -self.By, "B\'")
self.Cf = self.putDot(qp, self.Cx, -self.Cy, "C\'")

self.Ef = self.putDot(qp, self.Ex, -self.Ey, "E\'")

self.Ff = self.putDot(qp, self.Fx, -self.Fy, "F\'")

qp.drawLine(self.Cf, self.Bf)
qp.drawLine(self.Ef, self.Ff)
qp.drawLine(self.Bf, self.B)
qp.drawLine(self.C, self.Cf)
qp.drawLine(self.E, self.Ef)
qp.drawLine(self.F, self.Ff)
"""
        self.solution_queue.put(code)
    

        code = """
#K - BC's middle dot
self.K = self.putDot(qp, (self.Bx + self.Cx) / 2, (self.Bz + self.Cz) / 2, "K\'\'")
"""
        self.solution_queue.put(code)

        code = """
#K's frontal projection
self.k = self.putDot(qp, (self.Bx + self.Cx) / 2, (self.Bz + self.Cz) / 2 - 20, " ", dot_visible=False, let_visible=False)

x, y = count_cross(self.K, self.k, self.Bf, self.Cf)

self.Kf = self.putDot(qp, x, y, "K\'")
qp.drawLine(self.K, self.Kf)
        """
        self.solution_queue.put(code)

        code = """
#Frontal level line f's frontal projection
pen.setWidth(2)
pen.setColor(Qt.red)
qp.setPen(pen)
if self.Bf.x() < self.Ef.x():
        self.ff = self.putDot(qp, -self.Kf.x() / 4 + 20, -self.Kf.y() / 4, "f\'", dot_visible=False)
        self.f_f = self.putDot(qp, -self.Kf.x() / 4 - 80, -self.Kf.y() / 4, " ", let_visible=False, dot_visible=False)
else:
        self.ff = self.putDot(qp, -self.Kf.x() / 4 - 20, -self.Kf.y() / 4, "f\'", dot_visible=False)
        self.f_f = self.putDot(qp, -self.Kf.x() / 4 + 80, -self.Kf.y() / 4, " ", let_visible=False, dot_visible=False)
qp.drawLine(self.ff, self.f_f)
"""
        self.solution_queue.put(code)

        code = """
#Horizontal level line h's frontal projection
pen.setWidth(2)
pen.setColor(Qt.blue)
qp.setPen(pen)
if self.Bf.x() < self.Ef.x():
        x, y, x1, y1 = count_perp(self.Kf, self.Bf, roffset=80, loffset=20)
        self.h_f = self.putDot(qp, x1, y1, " ", dot_visible=False, let_visible=False)
        self.hf = self.putDot(qp, x, y, "h\'", dot_visible=False)
else:
        x, y, x1, y1 = count_perp(self.Kf, self.Bf, roffset=20, loffset=80)
        self.h_f = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False)
        self.hf = self.putDot(qp, x1, y1, "h\'", dot_visible=False)

qp.drawLine(self.hf, self.h_f)
"""
        self.solution_queue.put(code)

        code = """
#Frontal level line f's horizontal projection
pen.setWidth(2)
pen.setColor(Qt.red)
qp.setPen(pen)
if self.Bf.x() < self.Ef.x():
        x, y, x1, y1 = count_perp(self.K, self.B, roffset=80, loffset=20)
        self.f_ = self.putDot(qp, x1, y1, " ", dot_visible=False, let_visible=False)
        self.f = self.putDot(qp, x, y, "f\'\'", dot_visible=False)
else:
        x, y, x1, y1 = count_perp(self.K, self.B, roffset=20, loffset=80)
        self.f_ = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False)
        self.f = self.putDot(qp, x1, y1, "f\'\'", dot_visible=False)
qp.drawLine(self.f, self.f_)
"""
        self.solution_queue.put(code)

        code = """
#Horizontal level line h's gorizontal projection
pen.setWidth(2)
pen.setColor(Qt.blue)
qp.setPen(pen)
if self.Bf.x() < self.Ef.x():
        self.h = self.putDot(qp, -self.K.x() / 4 + 20, -self.K.y() / 4, "h\'\'", dot_visible=False)
        self.h_ = self.putDot(qp, -self.K.x() / 4 - 80, -self.K.y() / 4, " ", let_visible=False, dot_visible=False)

else:
        self.h = self.putDot(qp, -self.K.x() / 4 - 20, -self.K.y() / 4, "h\'\'", dot_visible=False)
        self.h_ = self.putDot(qp, -self.K.x() / 4 + 80, -self.K.y() / 4, " ", let_visible=False, dot_visible=False)
qp.drawLine(self.h, self.h_)
"""
        self.solution_queue.put(code)

        code = """
#Drawing the f0gamma tail
pen.setWidth(3)
pen.setColor(Qt.black)
qp.setPen(pen)
if self.E.x() < self.F.x():
        x1 = self.Ex + 10
        x2 = self.Ex + 5
else:
        x1 = self.Ex - 10
        x2 = self.Ex - 5
y1 =  ((x1 - self.Ex) * (self.Fz - self.Ez) + self.Ez * (self.Fx - self.Ex)) / (self.Fx - self.Ex)
gammaf = self.putDot(qp, x1, y1, "f" + chr(8320) + chr(947), dot_visible=False)

y2 = ((x2 - self.Ex) * (self.Fz - self.Ez) + self.Ez * (self.Fx - self.Ex)) / (self.Fx - self.Ex)
gammaf_ = self.putDot(qp, x2, y2, " ", dot_visible=False, let_visible=False)

qp.drawLine(gammaf, gammaf_)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)
x, y = count_cross(self.E, self.F, self.h, self.h_)
self.N1 = self.putDot(qp, x, y, "1\'\'")
qp.drawLine(self.E, self.N1)

pen.setWidth(2)
pen.setColor(Qt.blue)
qp.setPen(pen)
qp.drawLine(self.N1, self.h)
"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)
x, y = count_cross(self.E, self.F, self.f, self.f_)
self.N2 = self.putDot(qp, x, y, "2\'\'")
qp.drawLine(self.N2, self.E)
qp.drawLine(self.f, self.N2)
"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)
_N1 = QPoint(self.N1.x(), self.N1.y() - 50)
x, y = count_cross(self.hf, self.h_f, self.N1, _N1)
self.N1f = self.putDot(qp, x, y, "1\'")

qp.drawLine(self.N1, self.N1f)

pen.setWidth(2)
pen.setColor(Qt.blue)
qp.setPen(pen)
qp.drawLine(self.hf, self.N1f)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)
_N2 = QPoint(self.N2.x(), self.N2.y() - 50)
x, y = count_cross(self.ff, self.f_f, self.N2, _N2)
self.N2f = self.putDot(qp, x, y, "2\'")

qp.drawLine(self.N2, self.N2f)

pen.setWidth(2)
pen.setColor(Qt.red)
qp.setPen(pen)
qp.drawLine(self.ff, self.N2f)
"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)
qp.drawLine(self.N1f, self.N2f)

x, y = count_cross(self.N1f, self.N2f, self.Ef, self.Ff)

self.Af = self.putDot(qp, x, y, "A\'")
qp.drawLine(self.Ef, self.Af)
"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)
_Af = QPoint(self.Af.x(), self.Af.y() + 50)
x, y = count_cross(self.E, self.F, self.Af, _Af)
self.A = self.putDot(qp, x, y, "A\'\'")

qp.drawLine(self.Af, self.A)
"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

qp.drawLine(self.A, self.B)
"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

qp.drawLine(self.B, self.C)
"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

qp.drawLine(self.C, self.A)
"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

qp.drawLine(self.Af, self.Bf)
"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

qp.drawLine(self.Bf, self.Cf)
"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

qp.drawLine(self.Cf, self.Af)
"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

if (-self.Bf.x() > -self.Cf.x()) or (-self.Bf.x() > -self.Af.x()):
        self.h1 = self.putDot(qp, (-self.B.x() / 4) + 20, (-self.B.y() / 4), "h1\'\'", dot_visible=False)
        self.h1_ = self.putDot(qp, (-self.h1.x() / 4) - 150, (-self.h1.y() / 4), " ", dot_visible=False)

else:
        self.h1 = self.putDot(qp, (-self.B.x() / 4) - 20, (-self.B.y() / 4), "h1\'\'", dot_visible=False)
        self.h1_ = self.putDot(qp, (-self.h1.x() / 4) + 150, (-self.h1.y() / 4), " ", dot_visible=False)
qp.drawLine(self.h1, self.h1_)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

x, y = count_cross(self.A, self.C, self.h1, self.h1_)

self.N3 = self.putDot(qp, x, y, "3\'\'")

qp.drawLine(self.N3, self.A)
qp.drawLine(self.h1, self.N3)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)


_N3 = QPoint(self.N3.x(), self.N3.y() - 50)

x, y = count_cross(self.N3, _N3, self.Af, self.Cf)

self.N3f = self.putDot(qp, x, y, "3\'")
qp.drawLine(self.N3, self.N3f)
qp.drawLine(self.N3f, self.Af)

if (-self.Bf.x() > -self.Cf.x()) or (-self.Bf.x() > -self.Af.x()):
        x = -(self.Bf.x() / 4) + 10
else:
        x = -(self.Bf.x() / 4) - 10

x1 = -(self.N3f.x() / 4)
x2 = -(self.Bf.x() / 4)
y1 = -(self.N3f.y()) / 4
y2 = -(self.Bf.y()) / 4

y = ((x - x1) * (y2 - y1) + y1 * (x2 - x1)) / (x2 - x1)

self.h1f = self.putDot(qp, x, y, "h1\'", dot_visible=False)

qp.drawLine(self.N3f, self.h1f)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

if (-self.Bf.x() > -self.Cf.x()) or (-self.Bf.x() > -self.Af.x()):
        self.f1f = self.putDot(qp, (-self.Bf.x() / 4) + 20, (-self.Bf.y() / 4), "f1\'", dot_visible=False)
        self.f1_f = self.putDot(qp, (-self.f1f.x() / 4) - 150, (-self.f1f.y() / 4), " ", dot_visible=False)
else:
        self.f1f = self.putDot(qp, (-self.Bf.x() / 4) - 20, (-self.Bf.y() / 4), "f1\'", dot_visible=False)
        self.f1_f = self.putDot(qp, (-self.f1f.x() / 4) + 150, (-self.f1f.y() / 4), " ", dot_visible=False)

qp.drawLine(self.f1f, self.f1_f)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)




x, y = count_cross(self.Af, self.Cf, self.f1f, self.f1_f)

self.N4f = self.putDot(qp, x, y, "4\'")

qp.drawLine(self.N4f, self.Af)
qp.drawLine(self.f1f, self.N4f)

"""
        self.solution_queue.put(code)


        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)


_N4f = QPoint(self.N4f.x(), self.N4f.y() + 50)

x, y = count_cross(self.N4f, _N4f, self.A, self.C)

self.N4 = self.putDot(qp, x, y, "4\'\'")
qp.drawLine(self.N4, self.N4f)
qp.drawLine(self.N4, self.A)

if (-self.Bf.x() > -self.Cf.x()) or (-self.Bf.x() > -self.Af.x()):
        x = -(self.B.x() / 4) + 10
else:
        x = -(self.B.x() / 4) - 10

x1 = -(self.N4.x() / 4)
x2 = -(self.B.x() / 4)
y1 = -(self.N4.y()) / 4
y2 = -(self.B.y()) / 4

y = ((x - x1) * (y2 - y1) + y1 * (x2 - x1)) / (x2 - x1)

self.f1 = self.putDot(qp, x, y, "f1\'\'", dot_visible=False)

qp.drawLine(self.N4, self.f1)
qp.drawLine(self.B, self.f1)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

x, y, _, _ = count_perp(self.B, self.f1, loffset=30)
_, _, x1, y1 = count_perp(self.B, self.f1, roffset=30)

if y > y1:
        self.N5 = self.putDot(qp, x, y, "5\'\'")
else:
        self.N5 = self.putDot(qp, x1, y1, "5\'\'")

qp.drawLine(self.B, self.N5)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

if (self.Bf.x() < self.Cf.x()) and (self.Bf.x() < self.Af.x()):
        x, y, _, _ = count_perp(self.Bf, self.h1f, loffset=30)
else:
        _, _, x, y = count_perp(self.Bf, self.h1f, roffset=30)

self.N6 = self.putDot(qp, x, y, " ", dot_visible=False)

qp.drawLine(self.Bf, self.N6)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

_N5 = QPoint(self.N5.x(), self.N5.y() - 50)

x, y = count_cross(self.N5, _N5, self.Bf, self.N6)

self.N5f = self.putDot(qp, x, y, "5\'")

qp.drawLine(self.N5f, self.N5)
qp.drawLine(self.N5f, self.Bf)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

delta_y = abs(self.N5f.y() - self.Bf.y()) / 4

if (self.Bf.x() < self.Cf.x()) and (self.Bf.x() < self.Af.x()):
        x, y, _, _ = count_perp(self.N5, self.B, loffset=30)
else:
       _, _, x, y = count_perp(self.N5, self.B, roffset=30) 

_B0 = self.putDot(qp, x, y, " ", dot_visible=False)

B5len = sqrt(((-(_B0.x())/4) - (-(self.N5.x()) / 4))**2 + ((-(_B0.y())/4) - (-(self.N5.y()) / 4))**2)

lmb = delta_y / (B5len - delta_y)


x1 = (-(self.N5.x() / 4) + lmb * (-(_B0.x() / 4))) / (1 + lmb)
y1 = (-(self.N5.y() / 4) + lmb * (-(_B0.y() / 4))) / (1 + lmb)

self.B0 = self.putDot(qp, x1, y1, "B" + chr(8320))
qp.drawLine(self.N5, self.B0)
"""
        self.solution_queue.put(code)

        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)
qp.drawLine(self.B, self.B0)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

BB0len = sqrt(((-(self.B0.x())/4) - (-(self.B.x()) / 4))**2 + ((-(self.B0.y())/4) - (-(self.B.y()) / 4))**2)

lmb = 70 / (BB0len - 70)


x1 = (-(self.B.x() / 4) + lmb * (-(self.B0.x() / 4))) / (1 + lmb)
y1 = (-(self.B.y() / 4) + lmb * (-(self.B0.y() / 4))) / (1 + lmb)

self.N6 = self.putDot(qp, x1, y1, "6\'\'")
qp.drawLine(self.B, self.N6)
qp.drawLine(self.B0, self.N6)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

difx = -(self.B0.x() / 4) - (-(self.N6.x() / 4))
dify = -(self.B0.y() / 4) - (-(self.N6.y() / 4))

_B1 = self.putDot(qp, (-(self.N5.x() / 4) - difx), (-(self.N5.y() / 4) - dify), " ", dot_visible=False)

x, y = count_cross(self.B, self.N5, self.N6, _B1)

self.B1 = self.putDot(qp, x, y, "B1\'\'")

qp.drawLine(self.B1, self.N6)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

difx = -(self.B1.x() / 4) - (-(self.B.x() / 4))
dify = -(self.B1.y() / 4) - (-(self.B.y() / 4))

x = -(self.C.x() / 4) + difx
y = -(self.C.y() / 4) + dify

self.C1 = self.putDot(qp, x, y, "C1\'\'")

qp.drawLine(self.C1, self.C)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

difx = -(self.B1.x() / 4) - (-(self.B.x() / 4))
dify = -(self.B1.y() / 4) - (-(self.B.y() / 4))

x = -(self.A.x() / 4) + difx
y = -(self.A.y() / 4) + dify

self.A1 = self.putDot(qp, x, y, "A1\'\'")

qp.drawLine(self.A1, self.A)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)


qp.drawLine(self.B1, self.C1)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)


qp.drawLine(self.C1, self.A1)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)


qp.drawLine(self.A1, self.B1)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)


qp.drawLine(self.B1, self.B)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)


qp.drawLine(self.C1, self.C)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)


qp.drawLine(self.A1, self.A)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

_B1 = QPoint(self.B1.x(), self.B1.y() - 50)

x, y = count_cross(self.B1, _B1, self.Bf, self.N5f)
self.B1f = self.putDot(qp, x, y, "B1\'")
qp.drawLine(self.B1, self.B1f)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

difx = -(self.B1f.x() / 4) - (-(self.Bf.x() / 4))
dify = -(self.B1f.y() / 4) - (-(self.Bf.y() / 4))

x = -(self.Af.x() / 4) + difx
y = -(self.Af.y() / 4) + dify

self.A1f = self.putDot(qp, x, y, "A1\'")

qp.drawLine(self.A1f, self.Af)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

difx = -(self.B1f.x() / 4) - (-(self.Bf.x() / 4))
dify = -(self.B1f.y() / 4) - (-(self.Bf.y() / 4))

x = -(self.Cf.x() / 4) + difx
y = -(self.Cf.y() / 4) + dify

self.C1f = self.putDot(qp, x, y, "C1\'")

qp.drawLine(self.C1f, self.Cf)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)


qp.drawLine(self.B1f, self.A1f)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)


qp.drawLine(self.A1f, self.C1f)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)


qp.drawLine(self.C1f, self.B1f)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)


qp.drawLine(self.A1f, self.Af)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)


qp.drawLine(self.B1f, self.Bf)

"""
        self.solution_queue.put(code)

        code = """
pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)


qp.drawLine(self.C1f, self.Cf)

"""
        self.solution_queue.put(code)

        code = """
self.AB_visible = False
self.AC_visible = False
self.BC_visible = False

self.A1B1_visible = False
self.A1C1_visible = False
self.B1C1_visible = False

self.AA1_visible = False
self.BB1_visible = False
self.CC1_visible = False

pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)

if  -(self.C.y() / 4) > -(self.A.y() / 4) and  -(self.C.y() / 4) > -(self.B.y() / 4):
        qp.drawLine(self.A, self.B)
        self.AB_visible = True

        
        if -(self.A.x() / 4) > -(self.B.x() / 4):
                if -(self.C.x() / 4) > -(self.A.x() / 4):
                        qp.drawLine(self.A, self.C)
                        self.AC_visible = True

                        qp.drawLine(self.C, self.C1)
                        self.CC1_visible = True

                        qp.drawLine(self.B, self.B1)
                        self.BB1_visible = True

                        qp.drawLine(self.B1, self.C1)
                        self.B1C1_visible = True

                elif -(self.C.x() / 4) < -(self.B.x() / 4):
                        qp.drawLine(self.B, self.C)
                        self.BC_visible = True

                        qp.drawLine(self.C, self.C1)
                        self.CC1_visible = True

                        qp.drawLine(self.A, self.A1)
                        self.AA1_visible = True

                        qp.drawLine(self.A1, self.C1)
                        self.A1C1_visible = True

                elif -(self.A.x() / 4) > -(self.C.x() / 4) > -(self.B.x() / 4):
                        qp.drawLine(self.A, self.A1)
                        self.AA1_visible = True

                        qp.drawLine(self.B, self.B1)
                        self.BB1_visible = True

                        qp.drawLine(self.A1, self.C1)
                        self.A1C1_visible = True

                        qp.drawLine(self.B1, self.C1)
                        self.B1C1_visible = True

        if -(self.B.x() / 4) > -(self.A.x() / 4):
                if -(self.C.x() / 4) > -(self.B.x() / 4):
                        qp.drawLine(self.B, self.C)
                        self.BC_visible = True

                        qp.drawLine(self.C, self.C1)
                        self.CC1_visible = True

                        qp.drawLine(self.A, self.A1)
                        self.AA1_visible = True

                        qp.drawLine(self.A1, self.C1)
                        self.A1C1_visible = True

                elif -(self.C.x() / 4) < -(self.A.x() / 4):
                        qp.drawLine(self.A, self.B)
                        self.AB_visible = True

                        qp.drawLine(self.C, self.C1)
                        self.CC1_visible = True

                        qp.drawLine(self.B, self.B1)
                        self.BB1_visible = True

                        qp.drawLine(self.B1, self.C1)
                        self.B1C1_visible = True

                elif -(self.B.x() / 4) > -(self.C.x() / 4) > -(self.A.x() / 4):
                        qp.drawLine(self.A, self.A1)
                        self.AA1_visible = True

                        qp.drawLine(self.B, self.B1)
                        self.BB1_visible = True

                        qp.drawLine(self.A1, self.C1)
                        self.A1C1_visible = True

                        qp.drawLine(self.B1, self.C1)
                        self.B1C1_visible = True

if  -(self.A.y() / 4) > -(self.C.y() / 4) and  -(self.A.y() / 4) > -(self.B.y() / 4):
        
        qp.drawLine(self.C, self.B)
        BC_visible = True

        
        if -(self.C.x() / 4) > -(self.B.x() / 4):
                if -(self.A.x() / 4) > -(self.C.x() / 4):
                        qp.drawLine(self.A, self.C)
                        self.AC_visible = True

                        qp.drawLine(self.A, self.A1)
                        self.AA1_visible = True

                        qp.drawLine(self.B, self.B1)
                        self.BB1_visible = True

                        qp.drawLine(self.A1, self.B1)
                        self.A1B1_visible = True

                elif -(self.A.x() / 4) < -(self.B.x() / 4):
                        qp.drawLine(self.A, self.B)
                        self.AB_visible = True

                        qp.drawLine(self.C, self.C1)
                        self.CC1_visible = True

                        qp.drawLine(self.A, self.A1)
                        self.AA1_visible = True

                        qp.drawLine(self.A1, self.C1)
                        self.A1C1_visible = True

                elif -(self.C.x() / 4) > -(self.A.x() / 4) > -(self.B.x() / 4):
                        qp.drawLine(self.C, self.C1)
                        self.CC1_visible = True

                        qp.drawLine(self.B, self.B1)
                        self.BB1_visible = True

                        qp.drawLine(self.A1, self.C1)
                        self.A1C1_visible = True

                        qp.drawLine(self.A1, self.B1)
                        self.A1B1_visible = True

        if -(self.B.x() / 4) > -(self.C.x() / 4):
                if -(self.A.x() / 4) > -(self.B.x() / 4):
                        qp.drawLine(self.A, self.B)
                        self.AB_visible = True

                        qp.drawLine(self.C, self.C1)
                        self.CC1_visible = True

                        qp.drawLine(self.A, self.A1)
                        self.AA1_visible = True

                        qp.drawLine(self.A1, self.C1)
                        self.A1C1_visible = True

                elif -(self.A.x() / 4) < -(self.C.x() / 4):
                        qp.drawLine(self.A, self.C)
                        self.AC_visible = True

                        qp.drawLine(self.A, self.A1)
                        self.AA1_visible = True

                        qp.drawLine(self.B, self.B1)
                        self.BB1_visible = True

                        qp.drawLine(self.A1, self.B1)
                        self.A1B1_visible = True

                elif -(self.B.x() / 4) > -(self.A.x() / 4) > -(self.C.x() / 4):
                        qp.drawLine(self.B, self.B1)
                        self.BB1_visible = True

                        qp.drawLine(self.C, self.C1)
                        self.CC1_visible = True

                        qp.drawLine(self.A1, self.C1)
                        self.A1C1_visible = True

                        qp.drawLine(self.A1, self.B1)
                        self.A1B1_visible = True

if  -(self.B.y() / 4) > -(self.C.y() / 4) and  -(self.B.y() / 4) > -(self.A.y() / 4):
        
        qp.drawLine(self.A, self.C)
        self.AC_visible = True

        
        if -(self.A.x() / 4) > -(self.C.x() / 4):
                if -(self.B.x() / 4) > -(self.A.x() / 4):
                        qp.drawLine(self.A, self.B)
                        self.AB_visible = True

                        qp.drawLine(self.B, self.B1)
                        self.BB1_visible = True

                        qp.drawLine(self.C, self.C1)
                        self.CC1_visible = True

                        qp.drawLine(self.B1, self.C1)
                        self.B1C1_visible = True

                elif -(self.B.x() / 4) < -(self.C.x() / 4):
                        qp.drawLine(self.B, self.C)
                        self.BC_visible = True

                        qp.drawLine(self.A, self.A1)
                        self.AA1_visible = True

                        qp.drawLine(self.B, self.B1)
                        self.BB1_visible = True

                        qp.drawLine(self.A1, self.B1)
                        self.A1B1_visible = True

                elif -(self.A.x() / 4) > -(self.B.x() / 4) > -(self.C.x() / 4):
                        qp.drawLine(self.C, self.C1)
                        self.CC1_visible = True

                        qp.drawLine(self.A, self.A1)
                        self.AA1_visible = True

                        qp.drawLine(self.A1, self.B1)
                        self.A1B1_visible = True

                        qp.drawLine(self.B1, self.C1)
                        self.B1C1_visible = True

        if -(self.C.x() / 4) > -(self.A.x() / 4):
                if -(self.B.x() / 4) > -(self.C.x() / 4):
                        qp.drawLine(self.B, self.C)
                        self.BC_visible = True

                        qp.drawLine(self.B, self.B1)
                        self.BB1_visible = True

                        qp.drawLine(self.A, self.A1)
                        self.AA1_visible = True

                        qp.drawLine(self.B1, self.A1)
                        B1A1_visible = True

                if -(self.B.x() / 4) < -(self.A.x() / 4):
                        qp.drawLine(self.A, self.B)
                        self.AB_visible = True

                        qp.drawLine(self.B, self.B1)
                        self.BB1_visible = True

                        qp.drawLine(self.C, self.C1)
                        self.CC1_visible = True

                        qp.drawLine(self.B1, self.C1)
                        self.B1C1_visible = True

                elif -(self.C.x() / 4) > -(self.B.x() / 4) > -(self.A.x() / 4):
                        qp.drawLine(self.A, self.A1)
                        self.AA1_visible = True

                        qp.drawLine(self.C, self.C1)
                        self.CC1_visible = True

                        qp.drawLine(self.B1, self.C1)
                        self.B1C1_visible = True

                        qp.drawLine(self.A1, self.B1)
                        self.A1B1_visible = True
"""
        self.solution_queue.put(code)


        code = """
flag = True
#A1B1 & AC
x, y = count_cross(self.A1, self.B1, self.A, self.C)
if flag and ((self.A.x() <= x <= self.C.x()) or (self.C.x() <= x <= self.A.x())) and ((self.A.y() <= y <= self.C.y()) or (self.C.y() <= y <= self.A.y())) and ((self.A1.x() <= x <= self.B1.x()) or (self.B1.x() <= x <= self.A1.x())) and ((self.A1.y() <= y <= self.B1.y()) or (self.B1.y() <= y <= self.A1.y())):
        
        self.N7 = self.putDot(qp, x, y, "7\'\' \u2261 8\'\'") # A1B1
        self.N8 = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #AC
        
        _N7 = QPoint(self.N7.x(), self.N7.y() - 50)
        x, y = count_cross(self.N7, _N7, self.A1f, self.B1f)
        self.N7f = self.putDot(qp, x, y, "7\'")

        _N8 = QPoint(self.N8.x(), self.N8.y() - 50)
        x, y = count_cross(self.N8, _N8, self.Af, self.Cf)
        self.N8f = self.putDot(qp, x, y, "8\'")
        qp.drawLine(self.N7, self.N7f)
        qp.drawLine(self.N7f, self.N8f)

        if -(self.N7f.y() / 4) < -(self.N8f.y() / 4):
                self.A1B1_visible = True
                self.A1C1_visible = True
                self.AA1_visible = True

                self.B1C1_visible = True
                self.BB1_visible = True

        else:
                self.AC_visible = True
                self.AB_visible = True
                self.AA1_visible = True

                self.BC_visible = True
                self.CC1_visible = True

        flag = False

#A1B1 & CB
x, y = count_cross(self.A1, self.B1, self.B, self.C)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.B.x() <= x <= self.C.x()) or (self.C.x() <= x <= self.B.x())) and ((self.B.y() <= y <= self.C.y()) or (self.C.y() <= y <= self.B.y())) and ((self.A1.x() <= x <= self.B1.x()) or (self.B1.x() <= x <= self.A1.x())) and ((self.A1.y() <= y <= self.B1.y()) or (self.B1.y() <= y <= self.A1.y())):
        x = -(x / 4)
        y = -(y / 4)

        self.N7 = self.putDot(qp, x, y, "7\'\' \u2261 8\'\'") #A1B1
        self.N8 = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #BC

        _N7 = QPoint(self.N7.x(), self.N7.y() - 50)
        x, y = count_cross(self.N7, _N7, self.A1f, self.B1f)
        self.N7f = self.putDot(qp, x, y, "7\'")

        _N8 = QPoint(self.N8.x(), self.N8.y() - 50)
        x, y = count_cross(self.N8, _N8, self.Bf, self.Cf)
        self.N8f = self.putDot(qp, x, y, "8\'")
        qp.drawLine(self.N7, self.N7f)
        qp.drawLine(self.N7f, self.N8f)

        if -(self.N7f.y() / 4) < -(self.N8f.y() / 4):
                self.A1B1_visible = True
                self.A1C1_visible = True
                self.AA1_visible = True

                self.B1C1_visible = True
                self.BB1_visible = True

        else:
                self.BC_visible = True
                self.AB_visible = True
                self.BB1_visible = True

                self.AC_visble = True
                self.CC1_visible = True


        flag = False

#A1B1 & CC1
x, y = count_cross(self.A1, self.B1, self.C1, self.C)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.C1.x() <= x <= self.C.x()) or (self.C.x() <= x <= self.C1.x())) and ((self.C1.y() <= y <= self.C.y()) or (self.C.y() <= y <= self.C1.y())) and ((self.A1.x() <= x <= self.B1.x()) or (self.B1.x() <= x <= self.A1.x())) and ((self.A1.y() <= y <= self.B1.y()) or (self.B1.y() <= y <= self.A1.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N7 = self.putDot(qp, x, y, "7\'\' \u2261 8\'\'") #A1B1
        self.N8 = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #CC1

        _N7 = QPoint(self.N7.x(), self.N7.y() - 50)
        x, y = count_cross(self.N7, _N7, self.A1f, self.B1f)
        self.N7f = self.putDot(qp, x, y, "7\'")

        _N8 = QPoint(self.N8.x(), self.N8.y() - 50)
        x, y = count_cross(self.N8, _N8, self.Cf, self.C1f)
        self.N8f = self.putDot(qp, x, y, "8\'")

        qp.drawLine(self.N7, self.N7f)
        qp.drawLine(self.N7f, self.N8f)

        if -(self.N7f.y() / 4) < -(self.N8f.y() / 4):
                self.A1B1_visible = True
                self.A1C1_visible = True
                self.AA1_visible = True

                self.B1C1_visible = True
                self.BB1_visible = True

        else:
                self.CC1_visible = True
                self.AC_visible = True
                self.BC_visible = True

                self.A1C1_visible = True
                self.B1C1_visible = True

        flag = False

#A1C1 & CB
x, y = count_cross(self.A1, self.C1, self.C, self.B)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.B.x() <= x <= self.C.x()) or (self.C.x() <= x <= self.B.x())) and ((self.B.y() <= y <= self.C.y()) or (self.C.y() <= y <= self.B.y())) and ((self.A1.x() <= x <= self.C1.x()) or (self.C1.x() <= x <= self.A1.x())) and ((self.A1.y() <= y <= self.C1.y()) or (self.C1.y() <= y <= self.A1.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N7 = self.putDot(qp, x, y, "7\'\' \u2261 8\'\'") #A1C1
        self.N8 = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #BC
        
        _N7 = QPoint(self.N7.x(), self.N7.y() - 50)
        x, y = count_cross(self.N7, _N7, self.A1f, self.C1f)
        self.N7f = self.putDot(qp, x, y, "7\'")

        _N8 = QPoint(self.N8.x(), self.N8.y() - 50)
        x, y = count_cross(self.N8, _N8, self.Bf, self.Cf)
        self.N8f = self.putDot(qp, x, y, "8\'")

        qp.drawLine(self.N7, self.N7f)
        qp.drawLine(self.N7f, self.N8f)

        if -(self.N7f.y() / 4) < -(self.N8f.y() / 4):
                self.A1C1_visible = True
                self.A1B1_visible = True
                self.AA1_visible = True

                self.B1C1_visible = True
                self.CC1_visible = True

        else:
                self.BC_visible = True
                self.AB_visible = True
                self.BB1_visible = True

                AC_vislbe = True
                self.CC1_visible = True

        flag = False

#A1C1 & AB
x, y = count_cross(self.A1, self.C1, self.A, self.B)
x = -(x * 4)
y = -(y * 4) 
if flag and ((self.B.x() <= x <= self.A.x()) or (self.A.x() <= x <= self.B.x())) and ((self.B.y() <= y <= self.A.y()) or (self.A.y() <= y <= self.B.y())) and ((self.A1.x() <= x <= self.C1.x()) or (self.C1.x() <= x <= self.A1.x())) and ((self.A1.y() <= y <= self.C1.y()) or (self.C1.y() <= y <= self.A1.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N7 = self.putDot(qp, x, y, "7\'\' \u2261 8\'\'") #A1C1
        self.N8 = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #AB

        _N7 = QPoint(self.N7.x(), self.N7.y() - 50)
        x, y = count_cross(self.N7, _N7, self.A1f, self.C1f)
        self.N7f = self.putDot(qp, x, y, "7\'")

        _N8 = QPoint(self.N8.x(), self.N8.y() - 50)
        x, y = count_cross(self.N8, _N8, self.Af, self.Bf)
        self.N8f = self.putDot(qp, x, y, "8\'")

        qp.drawLine(self.N7, self.N7f)
        qp.drawLine(self.N7f, self.N8f)

        if -(self.N7f.y() / 4) < -(self.N8f.y() / 4):
                self.A1C1_visible = True
                self.A1B1_visible = True
                self.AA1_visible = True

                self.B1C1_visible = True
                self.CC1_visible = True

        else:
                self.AB_visible = True
                self.AC_visible = True
                self.AA1_visible = True

                self.BC_visible = True
                self.BB1_visible = True

        flag = False

#A1C1 & BB1
x, y = count_cross(self.A1, self.C1, self.B1, self.B)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.B.x() <= x <= self.B1.x()) or (self.B1.x() <= x <= self.B.x())) and ((self.B.y() <= y <= self.B1.y()) or (self.B1.y() <= y <= self.B.y())) and ((self.A1.x() <= x <= self.C1.x()) or (self.C1.x() <= x <= self.A1.x())) and ((self.A1.y() <= y <= self.C1.y()) or (self.C1.y() <= y <= self.A1.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N7 = self.putDot(qp, x, y, "7\'\' \u2261 8\'\'") #A1C1
        self.N8 = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #BB1

        _N7 = QPoint(self.N7.x(), self.N7.y() - 50)
        x, y = count_cross(self.N7, _N7, self.A1f, self.C1f)
        self.N7f = self.putDot(qp, x, y, "7\'")

        _N8 = QPoint(self.N8.x(), self.N8.y() - 50)
        x, y = count_cross(self.N8, _N8, self.Bf, self.B1f)
        self.N8f = self.putDot(qp, x, y, "8\'")

        qp.drawLine(self.N7, self.N7f)
        qp.drawLine(self.N7f, self.N8f)

        if -(self.N7f.y() / 4) < -(self.N8f.y() / 4):
                self.A1C1_visible = True
                self.A1B1_visible = True
                self.AA1_visible = True

                self.B1C1_visible = True
                self.CC1_visible = True

        else:
                self.BB1_visible = True
                self.AB_visible = True
                self.BC_visible = True

                self.A1B1_visible = True
                self.B1C1_visible = True

        flag = False

#B1C1 & AB
x, y = count_cross(self.B1, self.C1, self.A, self.B)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.B.x() <= x <= self.A.x()) or (self.A.x() <= x <= self.B.x())) and ((self.B.y() <= y <= self.A.y()) or (self.A.y() <= y <= self.B.y())) and ((self.B1.x() <= x <= self.C1.x()) or (self.C1.x() <= x <= self.B1.x())) and ((self.B1.y() <= y <= self.C1.y()) or (self.C1.y() <= y <= self.B1.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N7 = self.putDot(qp, x, y, "7\'\' \u2261 8\'\'") #B1C1
        self.N8 = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #AB
        
        _N7 = QPoint(self.N7.x(), self.N7.y() - 50)
        x, y = count_cross(self.N7, _N7, self.B1f, self.C1f)
        self.N7f = self.putDot(qp, x, y, "7\'")

        _N8 = QPoint(self.N8.x(), self.N8.y() - 50)
        x, y = count_cross(self.N8, _N8, self.Af, self.Bf)
        self.N8f = self.putDot(qp, x, y, "8\'")

        qp.drawLine(self.N7, self.N7f)
        qp.drawLine(self.N7f, self.N8f)

        if -(self.N7f.y() / 4) < -(self.N8f.y() / 4):
                self.B1C1_visible = True
                self.A1B1_visible = True
                self.BB1_visible = True

                self.A1C1_visible = True
                self.CC1_visible = True

        else:
                self.AB_visible = True
                self.AC_visible = True
                self.AA1_visible = True

                self.BC_visible = True
                self.BB1_visible = True

        flag = False

#B1C1 & AC
x, y = count_cross(self.B1, self.C1, self.A, self.C)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.C.x() <= x <= self.A.x()) or (self.A.x() <= x <= self.C.x())) and ((self.C.y() <= y <= self.A.y()) or (self.A.y() <= y <= self.C.y())) and ((self.B1.x() <= x <= self.C1.x()) or (self.C1.x() <= x <= self.B1.x())) and ((self.B1.y() <= y <= self.C1.y()) or (self.C1.y() <= y <= self.B1.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N7 = self.putDot(qp, x, y, "7\'\' \u2261 8\'\'") #B1C1
        self.N8 = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #AC

        _N7 = QPoint(self.N7.x(), self.N7.y() - 50)
        x, y = count_cross(self.N7, _N7, self.B1f, self.C1f)
        self.N7f = self.putDot(qp, x, y, "7\'")

        _N8 = QPoint(self.N8.x(), self.N8.y() - 50)
        x, y = count_cross(self.N8, _N8, self.Af, self.Cf)
        self.N8f = self.putDot(qp, x, y, "8\'")

        qp.drawLine(self.N7, self.N7f)
        qp.drawLine(self.N7f, self.N8f)

        if -(self.N7f.y() / 4) < -(self.N8f.y() / 4):
                self.B1C1_visible = True
                self.A1B1_visible = True
                self.BB1_visible = True

                self.A1C1_visible = True
                self.CC1_visible = True

        else:
                self.AC_visible = True
                self.AB_visible = True
                self.AA1_visible = True

                self.BC_visible = True
                self.CC1_visible = True
        flag = False

#B1C1 & AA1
x, y = count_cross(self.B1, self.C1, self.A, self.A1)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.A1.x() <= x <= self.A.x()) or (self.A.x() <= x <= self.A1.x())) and ((self.A1.y() <= y <= self.A.y()) or (self.A.y() <= y <= self.A1.y())) and ((self.B1.x() <= x <= self.C1.x()) or (self.C1.x() <= x <= self.B1.x())) and ((self.B1.y() <= y <= self.C1.y()) or (self.C1.y() <= y <= self.B1.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N7 = self.putDot(qp, x, y, "7\'\' \u2261 8\'\'") #B1C1
        self.N8 = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #AA1

        _N7 = QPoint(self.N7.x(), self.N7.y() - 50)
        x, y = count_cross(self.N7, _N7, self.B1f, self.C1f)
        self.N7f = self.putDot(qp, x, y, "7\'")

        _N8 = QPoint(self.N8.x(), self.N8.y() - 50)
        x, y = count_cross(self.N8, _N8, self.Af, self.A1f)
        self.N8f = self.putDot(qp, x, y, "8\'")

        qp.drawLine(self.N7, self.N7f)
        qp.drawLine(self.N7f, self.N8f)

        if -(self.N7f.y() / 4) < -(self.N8f.y() / 4):
                self.B1C1_visible = True
                self.A1B1_visible = True
                self.BB1_visible = True

                self.A1C1_visible = True
                self.CC1_visible = True

        else:
                self.AA1_visible = True
                self.AB_visible = True
                self.AC_visible = True

                self.A1C1_visible = True
                self.A1B1_visible = True
        flag = False

#AA1 & BC
x, y = count_cross(self.B, self.C, self.A, self.A1)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.C.x() <= x <= self.B.x()) or (self.B.x() <= x <= self.C.x())) and ((self.C.y() <= y <= self.B.y()) or (self.B.y() <= y <= self.C.y())) and ((self.A.x() <= x <= self.A1.x()) or (self.A1.x() <= x <= self.A.x())) and ((self.A.y() <= y <= self.A1.y()) or (self.A1.y() <= y <= self.A.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N7 = self.putDot(qp, x, y, "7\'\' \u2261 8\'\'") #AA1
        self.N8 = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #BC

        _N7 = QPoint(self.N7.x(), self.N7.y() - 50)
        x, y = count_cross(self.N7, _N7, self.Af, self.A1f)
        self.N7f = self.putDot(qp, x, y, "7\'")

        _N8 = QPoint(self.N8.x(), self.N8.y() - 50)
        x, y = count_cross(self.N8, _N8, self.Bf, self.Cf)
        self.N8f = self.putDot(qp, x, y, "8\'")

        qp.drawLine(self.N7, self.N7f)
        qp.drawLine(self.N7f, self.N8f)

        if -(self.N7f.y() / 4) < -(self.N8f.y() / 4):
                self.AA1_visible = True
                self.AB_visible = True
                self.AC_visible = True

                self.A1C1_visible = True
                self.A1B1_visible = True

        else:
                self.BC_visible = True
                self.AB_visible = True
                self.BB1_visible = True

                self.AC_visible = True
                self.CC1_visible = True
        flag = False

#BB1 & AC
x, y = count_cross(self.B, self.B1, self.A, self.C)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.C.x() <= x <= self.A.x()) or (self.A.x() <= x <= self.C.x())) and ((self.C.y() <= y <= self.A.y()) or (self.A.y() <= y <= self.C.y())) and ((self.B.x() <= x <= self.B1.x()) or (self.B1.x() <= x <= self.B.x())) and ((self.B.y() <= y <= self.B1.y()) or (self.B1.y() <= y <= self.B.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N7 = self.putDot(qp, x, y, "7\'\' \u2261 8\'\'") #BB1
        self.N8 = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #AC
        
        _N7 = QPoint(self.N7.x(), self.N7.y() - 50)
        x, y = count_cross(self.N7, _N7, self.Bf, self.B1f)
        self.N7f = self.putDot(qp, x, y, "7\'")

        _N8 = QPoint(self.N8.x(), self.N8.y() - 50)
        x, y = count_cross(self.N8, _N8, self.Af, self.Cf)
        self.N8f = self.putDot(qp, x, y, "8\'")

        qp.drawLine(self.N7, self.N7f)
        qp.drawLine(self.N7f, self.N8f)

        if -(self.N7f.y() / 4) < -(self.N8f.y() / 4):
                self.BB1_visible = True
                self.AB_visible = True
                self.BC_visible = True

                self.B1C1_visible = True
                self.A1B1_visible = True

        else:
                self.AC_visible = True
                self.AB_visible = True
                self.AA1_visible = True

                self.BC_visible = True
                self.CC1_visible = True
        flag = False

#CC1 & AB
x, y = count_cross(self.C1, self.C, self.A, self.B)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.B.x() <= x <= self.A.x()) or (self.A.x() <= x <= self.B.x())) and ((self.B.y() <= y <= self.A.y()) or (self.A.y() <= y <= self.B.y())) and ((self.C.x() <= x <= self.C1.x()) or (self.C1.x() <= x <= self.C.x())) and ((self.C.y() <= y <= self.C1.y()) or (self.C1.y() <= y <= self.C.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N7 = self.putDot(qp, x, y, "7\'\' \u2261 8\'\'") #CC1
        self.N8 = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #AB

        _N7 = QPoint(self.N7.x(), self.N7.y() - 50)
        x, y = count_cross(self.N7, _N7, self.Cf, self.C1f)
        self.N7f = self.putDot(qp, x, y, "7\'")

        _N8 = QPoint(self.N8.x(), self.N8.y() - 50)
        x, y = count_cross(self.N8, _N8, self.Af, self.Bf)
        self.N8f = self.putDot(qp, x, y, "8\'")

        qp.drawLine(self.N7, self.N7f)
        qp.drawLine(self.N7f, self.N8f)

        if -(self.N7f.y() / 4) < -(self.N8f.y() / 4):
                self.CC1_visible = True
                self.AC_visible = True
                self.BC_visible = True

                self.A1C1_visible = True
                self.B1C1_visible = True

        else:
                self.AB_visible = True
                self.AC_visible = True
                self.AA1_visible = True

                self.BC_visible = True
                self.BB1_visible = True
        flag = False

"""
        self.solution_queue.put(code)


        code = """
pen.setWidth(2)
if self.AB_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.A, self.B)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.A, self.B)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.A, self.B)

if self.AC_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.A, self.C)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.A, self.C)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.A, self.C)

if self.BC_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.B, self.C)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.B, self.C)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.B, self.C)

if self.A1B1_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.A1, self.B1)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.A1, self.B1)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.A1, self.B1)

if self.B1C1_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.B1, self.C1)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.B1, self.C1)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.B1, self.C1)

if self.A1C1_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.A1, self.C1)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.A1, self.C1)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.A1, self.C1)

if self.AA1_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.A, self.A1)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.A, self.A1)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.A, self.A1)

if self.BB1_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.B, self.B1)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.B, self.B1)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.B, self.B1)

if self.CC1_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.C, self.C1)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.C, self.C1)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.C, self.C1)

"""
        self.solution_queue.put(code)


#Frontal vision
#--------------------------------------------------------------------------
        code = """
self.ABf_visible = False
self.ACf_visible = False
self.BCf_visible = False

self.A1B1f_visible = False
self.A1C1f_visible = False
self.B1C1f_visible = False

self.AA1f_visible = False
self.BB1f_visible = False
self.CC1f_visible = False

pen.setWidth(1)
pen.setColor(Qt.black)
qp.setPen(pen)


if (self.C1f.y() / 4) < (self.A1f.y() / 4) and (self.C1f.y() / 4) < (self.B1f.y() / 4):
        
        qp.drawLine(self.A1f, self.B1f)
        self.A1B1f_visible = True

        
        if -(self.A1f.x() / 4) > -(self.B1f.x() / 4):
                if -(self.C1f.x() / 4) > -(self.A1f.x() / 4):
                        qp.drawLine(self.A1f, self.C1f)
                        self.A1C1f_visible = True

                        qp.drawLine(self.Cf, self.C1f)
                        self.CC1f_visible = True

                        qp.drawLine(self.Bf, self.B1f)
                        self.BB1f_visible = True

                        qp.drawLine(self.Bf, self.Cf)
                        self.BCf_visible = True
                        flag1 = False

                elif -(self.C1f.x() / 4) < -(self.B1f.x() / 4):
                        qp.drawLine(self.B1f, self.C1f)
                        self.B1C1f_visible = True

                        qp.drawLine(self.Cf, self.C1f)
                        self.CC1f_visible = True

                        qp.drawLine(self.Af, self.A1f)
                        self.AA1f_visible = True

                        qp.drawLine(self.Af, self.Cf)
                        self.ACf_visible = True
                        flag1 = False

                elif -(self.A1f.x() / 4) > -(self.C1f.x() / 4) > -(self.B1f.x() / 4):
                        qp.drawLine(self.Af, self.A1f)
                        self.AA1f_visible = True

                        qp.drawLine(self.Bf, self.B1f)
                        self.BB1f_visible = True

                        qp.drawLine(self.Af, self.Cf)
                        self.ACf_visible = True

                        qp.drawLine(self.Bf, self.Cf)
                        self.BCf_visible = True
                        flag1 = False

        if -(self.B1f.x() / 4) > -(self.A1f.x() / 4):
                if -(self.C1f.x() / 4) > -(self.B1f.x() / 4):
                        qp.drawLine(self.B1f, self.C1f)
                        self.B1C1f_visible = True

                        qp.drawLine(self.Cf, self.C1f)
                        self.CC1f_visible = True

                        qp.drawLine(self.Af, self.A1f)
                        self.AA1f_visible = True

                        qp.drawLine(self.Af, self.Cf)
                        self.ACf_visible = True
                        flag1 = False

                elif -(self.C1f.x() / 4) < -(self.A1f.x() / 4):
                        qp.drawLine(self.A1f, self.C1f)
                        self.A1C1f_visible = True

                        qp.drawLine(self.Cf, self.C1f)
                        self.CC1f_visible = True

                        qp.drawLine(self.Bf, self.B1f)
                        self.BB1f_visible = True

                        qp.drawLine(self.Bf, self.Cf)
                        self.BCf_visible = True
                        flag1 = False

                elif -(self.B1f.x() / 4) > -(self.C1f.x() / 4) > -(self.A1f.x() / 4):
                        qp.drawLine(self.Af, self.A1f)
                        self.AA1f_visible = True

                        qp.drawLine(self.Bf, self.B1f)
                        self.BB1f_visible = True

                        qp.drawLine(self.Af, self.Cf)
                        self.ACf_visible = True

                        qp.drawLine(self.Bf, self.Cf)
                        self.BCf_visible = True
                        flag1 = False

if (self.A1f.y() / 4) < (self.C1f.y() / 4) and (self.A1f.y() / 4) < (self.B1f.y() / 4):
        
        qp.drawLine(self.C1f, self.B1f)
        B1C1f_visible = True

        
        if -(self.C1f.x() / 4) > -(self.B1f.x() / 4):
                if -(self.A1f.x() / 4) > -(self.C1f.x() / 4):
                        qp.drawLine(self.A1f, self.C1f)
                        self.A1C1f_visible = True

                        qp.drawLine(self.Af, self.A1f)
                        self.AA1f_visible = True

                        qp.drawLine(self.Bf, self.B1f)
                        self.BB1f_visible = True

                        qp.drawLine(self.Af, self.Bf)
                        self.ABf_visible = True
                        flag1 = False

                elif -(self.A1f.x() / 4) < -(self.B1f.x() / 4):
                        qp.drawLine(self.A1f, self.B1f)
                        self.A1Bf_visible = True

                        qp.drawLine(self.Cf, self.C1f)
                        self.CC1f_visible = True

                        qp.drawLine(self.Af, self.A1f)
                        self.AA1f_visible = True

                        qp.drawLine(self.Af, self.Cf)
                        self.ACf_visible = True
                        flag1 = False

                elif -(self.C1f.x() / 4) > -(self.A1f.x() / 4) > -(self.B1f.x() / 4):
                        qp.drawLine(self.Cf, self.C1f)
                        self.CC1f_visible = True

                        qp.drawLine(self.Bf, self.B1f)
                        self.BB1f_visible = True

                        qp.drawLine(self.Af, self.Cf)
                        self.ACf_visible = True

                        qp.drawLine(self.Af, self.Bf)
                        self.ABf_visible = True
                        flag1 = False

        if -(self.B1f.x() / 4) > -(self.C1f.x() / 4):
                if -(self.A1f.x() / 4) > -(self.B1f.x() / 4):
                        qp.drawLine(self.A1f, self.B1f)
                        self.A1B1f_visible = True

                        qp.drawLine(self.Cf, self.C1f)
                        self.CC1f_visible = True

                        qp.drawLine(self.Af, self.A1f)
                        self.AA1f_visible = True

                        qp.drawLine(self.Af, self.Cf)
                        self.ACf_visible = True
                        flag1 = False

                elif -(self.A1f.x() / 4) < -(self.C1f.x() / 4):
                        qp.drawLine(self.A1f, self.C1f)
                        self.A1C1f_visible = True

                        qp.drawLine(self.Af, self.A1f)
                        self.AA1f_visible = True

                        qp.drawLine(self.Bf, self.B1f)
                        self.BB1f_visible = True

                        qp.drawLine(self.Af, self.Bf)
                        self.ABf_visible = True
                        flag1 = False

                elif -(self.B1f.x() / 4) > -(self.A1f.x() / 4) > -(self.C1f.x() / 4):
                        qp.drawLine(self.Bf, self.B1f)
                        self.BB1f_visible = True

                        qp.drawLine(self.Cf, self.C1f)
                        self.CC1f_visible = True

                        qp.drawLine(self.Af, self.Cf)
                        self.ACf_visible = True

                        qp.drawLine(self.Af, self.Bf)
                        self.ABf_visible = True
                        flag1 = False

if (self.B1f.y() / 4) < (self.C1f.y() / 4) and (self.B1f.y() / 4) < (self.A1f.y() / 4):
        qp.drawLine(self.A1f, self.C1f)
        self.A1C1f_visible = True

        
        if -(self.A1f.x() / 4) > -(self.C1f.x() / 4):
                if -(self.B1f.x() / 4) > -(self.A1f.x() / 4):
                        qp.drawLine(self.A1f, self.B1f)
                        self.A1B1f_visible = True

                        qp.drawLine(self.Bf, self.B1f)
                        self.BB1f_visible = True

                        qp.drawLine(self.Cf, self.C1f)
                        self.CC1f_visible = True

                        qp.drawLine(self.Bf, self.Cf)
                        self.BCf_visible = True
                        flag1 = False

                elif -(self.B1f.x() / 4) < -(self.C1f.x() / 4):
                        qp.drawLine(self.B1f, self.C1f)
                        self.B1C1f_visible = True

                        qp.drawLine(self.Af, self.A1f)
                        self.AA1f_visible = True

                        qp.drawLine(self.Bf, self.B1f)
                        self.BB1f_visible = True

                        qp.drawLine(self.Af, self.Bf)
                        self.ABf_visible = True
                        flag1 = False

                elif -(self.A1f.x() / 4) > -(self.B1f.x() / 4) > -(self.C1f.x() / 4):
                        qp.drawLine(self.Cf, self.C1f)
                        self.CC1f_visible = True

                        qp.drawLine(self.Af, self.A1f)
                        self.AA1f_visible = True

                        qp.drawLine(self.Af, self.Bf)
                        self.ABf_visible = True

                        qp.drawLine(self.Bf, self.Cf)
                        self.BCf_visible = True
                        flag1 = False

        if -(self.C1f.x() / 4) > -(self.A1f.x() / 4):
                if -(self.B1f.x() / 4) > -(self.C1f.x() / 4):
                        print("YAY")
                        qp.drawLine(self.B1f, self.C1f)
                        self.B1C1f_visible = True

                        qp.drawLine(self.Bf, self.B1f)
                        self.BB1f_visible = True

                        qp.drawLine(self.Af, self.A1f)
                        self.AA1f_visible = True

                        qp.drawLine(self.Bf, self.Af)
                        self.ABf_visible = True
                        flag1 = False

                elif -(self.B1f.x() / 4) < -(self.A1f.x() / 4):
                        print("YAY")
                        qp.drawLine(self.A1f, self.B1f)
                        self.A1B1f_visible = True

                        qp.drawLine(self.Bf, self.B1f)
                        self.BB1f_visible = True

                        qp.drawLine(self.Cf, self.C1f)
                        self.CC1f_visible = True

                        qp.drawLine(self.Bf, self.Cf)
                        self.BCf_visible = True
                        flag1 = False

                elif -(self.C1f.x() / 4) > -(self.B1f.x() / 4) > -(self.A1f.x() / 4):
                        print("YAY")
                        qp.drawLine(self.Af, self.A1f)
                        self.AA1f_visible = True

                        qp.drawLine(self.Cf, self.C1f)
                        self.CC1f_visible = True 

                        qp.drawLine(self.Bf, self.Cf)
                        self.BCf_visible = True

                        qp.drawLine(self.Af, self.Bf)
                        self.ABf_visible = True
                        flag1 = False
"""
        self.solution_queue.put(code)


        code = """
flag = True
#ABf & A1C1f
x, y = count_cross(self.Af, self.Bf, self.A1f, self.C1f)
if flag and ((self.A1f.x() <= x <= self.C1f.x()) or (self.C1f.x() <= x <= self.A1f.x())) and ((self.A1f.y() <= y <= self.C1f.y()) or (self.C1f.y() <= y <= self.A1f.y())) and ((self.Af.x() <= x <= self.Bf.x()) or (self.Bf.x() <= x <= self.Af.x())) and ((self.Af.y() <= y <= self.Bf.y()) or (self.Bf.y() <= y <= self.Af.y())):
        
        self.N9f = self.putDot(qp, x, y, "9\' \u2261 10\'") # ABf
        self.N10f = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #A1C1f
        
        _N9 = QPoint(self.N9f.x(), self.N9f.y() + 50)
        x, y = count_cross(self.N9f, _N9, self.A, self.B)
        self.N9 = self.putDot(qp, x, y, "9\'\'")

        _N10 = QPoint(self.N10f.x(), self.N10f.y() + 50)
        x, y = count_cross(self.N10f, _N10, self.A1, self.C1)
        self.N10 = self.putDot(qp, x, y, "10\'\'")

        qp.drawLine(self.N9f, self.N9)
        qp.drawLine(self.N9, self.N10)

        if (self.N9.y() / 4) < (self.N10.y() / 4):
                self.ABf_visible = True
                self.ACf_visible = True
                self.AA1f_visible = True

                self.BCf_visible = True
                self.BB1f_visible = True

        else:
                self.A1C1f_visible = True
                self.A1B1f_visible = True
                self.AA1f_visible = True

                self.B1C1f_visible = True
                self.CC1f_visible = True

        flag = False

#ABf & B1C1f
x, y = count_cross(self.Af, self.Bf, self.B1f, self.C1f)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.B1f.x() <= x <= self.C1f.x()) or (self.C1f.x() <= x <= self.B1f.x())) and ((self.B1f.y() <= y <= self.C1f.y()) or (self.C1f.y() <= y <= self.B1f.y())) and ((self.Af.x() <= x <= self.Bf.x()) or (self.Bf.x() <= x <= self.Af.x())) and ((self.Af.y() <= y <= self.Bf.y()) or (self.Bf.y() <= y <= self.Af.y())):
        x = -(x / 4)
        y = -(y / 4)

        self.N9f = self.putDot(qp, x, y, "9\' \u2261 10\'") #ABf
        self.N10f = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #B1C1f

        _N9 = QPoint(self.N9f.x(), self.N9f.y() + 50)
        x, y = count_cross(self.N9f, _N9, self.A, self.B)
        self.N9 = self.putDot(qp, x, y, "9\'\'")

        _N10 = QPoint(self.N10f.x(), self.N10f.y() + 50)
        x, y = count_cross(self.N10f, _N10, self.B1, self.C1)
        self.N10 = self.putDot(qp, x, y, "10\'\'")

        qp.drawLine(self.N9f, self.N9)
        qp.drawLine(self.N9, self.N10)

        if (self.N9.y() / 4) < (self.N10.y() / 4):
                self.ABf_visible = True
                self.ACf_visible = True
                self.AA1f_visible = True

                self.BCf_visible = True
                self.BB1f_visible = True

        else:
                self.B1C1f_visible = True
                self.A1B1f_visible = True
                self.BB1f_visible = True

                self.A1C1f_visible = True
                self.CC1f_visible = True


        flag = False

#ABf & CC1f
x, y = count_cross(self.Af, self.Bf, self.C1f, self.Cf)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.C1f.x() <= x <= self.Cf.x()) or (self.Cf.x() <= x <= self.C1f.x())) and ((self.C1f.y() <= y <= self.Cf.y()) or (self.Cf.y() <= y <= self.C1f.y())) and ((self.Af.x() <= x <= self.Bf.x()) or (self.Bf.x() <= x <= self.Af.x())) and ((self.Af.y() <= y <= self.Bf.y()) or (self.Bf.y() <= y <= self.Af.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N9f = self.putDot(qp, x, y, "9\' \u2261 10\'") #AB
        self.N10f = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #CC1

        _N9 = QPoint(self.N9f.x(), self.N9f.y() + 50)
        x, y = count_cross(self.N9f, _N9, self.A, self.B)
        self.N9 = self.putDot(qp, x, y, "9\'\'")

        _N10 = QPoint(self.N10f.x(), self.N10f.y() + 50)
        x, y = count_cross(self.N10f, _N10, self.C, self.C1)
        self.N10 = self.putDot(qp, x, y, "10\'\'")

        qp.drawLine(self.N9f, self.N9)
        qp.drawLine(self.N9, self.N10)

        if (self.N9.y() / 4) < (self.N10.y() / 4):
                self.ABf_visible = True
                self.ACf_visible = True
                self.AA1f_visible = True

                self.BCf_visible = True
                self.BB1f_visible = True

        else:
                self.CC1f_visible = True
                self.A1C1f_visible = True
                self.B1C1f_visible = True

                self.ACf_visible = True
                self.BCf_visible = True

        flag = False

#ACf & C1B1f
x, y = count_cross(self.Af, self.Cf, self.C1f, self.B1f)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.B1f.x() <= x <= self.C1f.x()) or (self.C1f.x() <= x <= self.B1f.x())) and ((self.B1f.y() <= y <= self.C1f.y()) or (self.C1f.y() <= y <= self.B1f.y())) and ((self.Af.x() <= x <= self.C1f.x()) or (self.C1f.x() <= x <= self.Af.x())) and ((self.A1f.y() <= y <= self.C1f.y()) or (self.C1f.y() <= y <= self.A1f.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N9f = self.putDot(qp, x, y, "9\' \u2261 10\'") #A1C1
        self.N10f = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #BC
        
        _N9 = QPoint(self.N9f.x(), self.N9f.y() + 50)
        x, y = count_cross(self.N9f, _N9, self.A1, self.C1)
        self.N9 = self.putDot(qp, x, y, "9\'\'")

        _N10 = QPoint(self.N10f.x(), self.N10f.y() + 50)
        x, y = count_cross(self.N10f, _N10, self.B, self.C)
        self.N10 = self.putDot(qp, x, y, "10\'\'")

        qp.drawLine(self.N9f, self.N9)
        qp.drawLine(self.N9, self.N10)

        if (self.N9.y() / 4) < (self.N10.y() / 4):
                self.A1C1f_visible = True
                self.A1B1f_visible = True
                self.AA1f_visible = True

                self.B1C1f_visible = True
                self.CC1f_visible = True

        else:
                self.BCf_visible = True
                self.ABf_visible = True
                self.BB1f_visible = True

                AC_vislbe = True
                self.CC1f_visible = True

        flag = False

#ACf & A1B1f
x, y = count_cross(self.Af, self.Cf, self.A1f, self.B1f)
x = -(x * 4)
y = -(y * 4) 
if flag and ((self.B1f.x() <= x <= self.A1f.x()) or (self.A1f.x() <= x <= self.B1f.x())) and ((self.B1f.y() <= y <= self.A1f.y()) or (self.A1f.y() <= y <= self.B1f.y())) and ((self.Af.x() <= x <= self.Cf.x()) or (self.Cf.x() <= x <= self.Af.x())) and ((self.Af.y() <= y <= self.Cf.y()) or (self.Cf.y() <= y <= self.Af.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N9f = self.putDot(qp, x, y, "9\' \u2261 10\'") #ACf
        self.N10f = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #A1B1f

        _N9 = QPoint(self.N9f.x(), self.N9f.y() + 50)
        x, y = count_cross(self.N9f, _N9, self.A, self.C)
        self.N9 = self.putDot(qp, x, y, "9\'\'")

        _N10 = QPoint(self.N10f.x(), self.N10f.y() + 50)
        x, y = count_cross(self.N10f, _N10, self.A1, self.B1)
        self.N10 = self.putDot(qp, x, y, "10\'\'")

        qp.drawLine(self.N9f, self.N9)
        qp.drawLine(self.N9, self.N10)

        if (self.N9.y() / 4) < (self.N10.y() / 4):
                self.ACf_visible = True
                self.ABf_visible = True
                self.AA1f_visible = True

                self.BCf_visible = True
                self.CC1f_visible = True

        else:
                self.A1B1f_visible = True
                self.A1C1f_visible = True
                self.AA1f_visible = True

                self.B1C1_visible = True
                self.BB1f_visible = True

        flag = False

#ACf & BB1f
x, y = count_cross(self.Af, self.Cf, self.B1f, self.Bf)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.Bf.x() <= x <= self.B1f.x()) or (self.B1f.x() <= x <= self.Bf.x())) and ((self.Bf.y() <= y <= self.B1f.y()) or (self.B1f.y() <= y <= self.Bf.y())) and ((self.Af.x() <= x <= self.Cf.x()) or (self.Cf.x() <= x <= self.Af.x())) and ((self.Af.y() <= y <= self.Cf.y()) or (self.Cf.y() <= y <= self.Af.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N9f = self.putDot(qp, x, y, "9\' \u2261 10\'") #ACf
        self.N10f = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #BB1f

        _N9 = QPoint(self.N9f.x(), self.N9f.y() + 50)
        x, y = count_cross(self.N9f, _N9, self.A, self.C)
        self.N9 = self.putDot(qp, x, y, "9\'\'")

        _N10 = QPoint(self.N10f.x(), self.N10f.y() + 50)
        x, y = count_cross(self.N10f, _N10, self.B, self.B1)
        self.N10 = self.putDot(qp, x, y, "10\'\'")

        qp.drawLine(self.N9f, self.N9)
        qp.drawLine(self.N9, self.N10)

        if (self.N9.y() / 4) < (self.N10.y() / 4):
                self.ACf_visible = True
                self.ABf_visible = True
                self.AA1f_visible = True

                self.BCf_visible = True
                self.CC1f_visible = True

        else:
                self.BB1f_visible = True
                self.A1B1f_visible = True
                self.B1C1f_visible = True

                self.ABf_visible = True
                self.BCf_visible = True

        flag = False

#BCf & A1B1f
x, y = count_cross(self.Bf, self.Cf, self.A1f, self.B1f)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.B1f.x() <= x <= self.A1f.x()) or (self.A1f.x() <= x <= self.B1f.x())) and ((self.B1f.y() <= y <= self.A1f.y()) or (self.A1f.y() <= y <= self.B1f.y())) and ((self.Bf.x() <= x <= self.Cf.x()) or (self.Cf.x() <= x <= self.Bf.x())) and ((self.Bf.y() <= y <= self.Cf.y()) or (self.Cf.y() <= y <= self.Bf.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N9f = self.putDot(qp, x, y, "9\' \u2261 10\'") #BCf
        self.N10f = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #A1B1f
        
        _N9 = QPoint(self.N9f.x(), self.N9f.y() + 50)
        x, y = count_cross(self.N9f, _N9, self.B, self.C)
        self.N9 = self.putDot(qp, x, y, "9\'\'")

        _N10 = QPoint(self.N10f.x(), self.N10f.y() + 50)
        x, y = count_cross(self.N10f, _N10, self.A1, self.B1)
        self.N10 = self.putDot(qp, x, y, "10\'\'")

        qp.drawLine(self.N9f, self.N9)
        qp.drawLine(self.N9, self.N10)

        if (self.N9.y() / 4) < (self.N10.y() / 4):
                self.BCf_visible = True
                self.ABf_visible = True
                self.BB1f_visible = True

                self.ACf_visible = True
                self.CC1f_visible = True

        else:
                self.A1B1f_visible = True
                self.A1C1f_visible = True
                self.AA1f_visible = True

                self.B1C1f_visible = True
                self.BB1f_visible = True

        flag = False

#BCf & A1C1f
x, y = count_cross(self.Bf, self.Cf, self.A1f, self.C1f)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.C1f.x() <= x <= self.A1f.x()) or (self.A1f.x() <= x <= self.C1f.x())) and ((self.C1f.y() <= y <= self.A1f.y()) or (self.A1f.y() <= y <= self.C1f.y())) and ((self.Bf.x() <= x <= self.Cf.x()) or (self.Cf.x() <= x <= self.Bf.x())) and ((self.Bf.y() <= y <= self.Cf.y()) or (self.Cf.y() <= y <= self.Bf.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N9f = self.putDot(qp, x, y, "9\' \u2261 10\'") #BCf
        self.N10f = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #A1C1f

        _N9 = QPoint(self.N9f.x(), self.N9f.y() + 50)
        x, y = count_cross(self.N9f, _N9, self.B, self.C)
        self.N9 = self.putDot(qp, x, y, "9\'\'")

        _N10 = QPoint(self.N10f.x(), self.N10f.y() + 50)
        x, y = count_cross(self.N10f, _N10, self.A1, self.C1)
        self.N10 = self.putDot(qp, x, y, "10\'\'")

        qp.drawLine(self.N9f, self.N9)
        qp.drawLine(self.N9, self.N10)

        if (self.N9.y() / 4) < (self.N10.y() / 4):
                self.BCf_visible = True
                self.ABf_visible = True
                self.BB1f_visible = True

                self.ACf_visible = True
                self.CC1f_visible = True

        else:
                self.A1C1f_visible = True
                self.A1B1f_visible = True
                self.AA1f_visible = True

                self.B1C1f_visible = True
                self.CC1f_visible = True
        flag = False

#BCf & AA1f
x, y = count_cross(self.Bf, self.Cf, self.Af, self.A1f)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.A1f.x() <= x <= self.Af.x()) or (self.Af.x() <= x <= self.A1f.x())) and ((self.A1f.y() <= y <= self.Af.y()) or (self.Af.y() <= y <= self.A1f.y())) and ((self.Bf.x() <= x <= self.Cf.x()) or (self.Cf.x() <= x <= self.Bf.x())) and ((self.Bf.y() <= y <= self.Cf.y()) or (self.Cf.y() <= y <= self.Bf.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N9f = self.putDot(qp, x, y, "9\' \u2261 10\'") #BCf
        self.N10f = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #AA1f

        _N9 = QPoint(self.N9f.x(), self.N9f.y() + 50)
        x, y = count_cross(self.N9f, _N9, self.B, self.C)
        self.N9 = self.putDot(qp, x, y, "9\'\'")

        _N10 = QPoint(self.N10f.x(), self.N10f.y() + 50)
        x, y = count_cross(self.N10f, _N10, self.A, self.A1)
        self.N10 = self.putDot(qp, x, y, "10\'\'")

        qp.drawLine(self.N9f, self.N9)
        qp.drawLine(self.N9, self.N10)

        if (self.N9.y() / 4) < (self.N10.y() / 4):
                self.BCf_visible = True
                self.ABf_visible = True
                self.BB1f_visible = True

                self.ACf_visible = True
                self.CC1f_visible = True

        else:
                self.AA1f_visible = True
                self.A1B1f_visible = True
                self.A1C1f_visible = True

                self.ACf_visible = True
                self.ABf_visible = True
        flag = False

#AA1f & B1C1f
x, y = count_cross(self.B1f, self.C1f, self.Af, self.A1f)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.C1f.x() <= x <= self.B1f.x()) or (self.B1f.x() <= x <= self.C1f.x())) and ((self.C1f.y() <= y <= self.B1f.y()) or (self.B1f.y() <= y <= self.C1f.y())) and ((self.Af.x() <= x <= self.A1f.x()) or (self.A1f.x() <= x <= self.Af.x())) and ((self.Af.y() <= y <= self.A1f.y()) or (self.A1f.y() <= y <= self.Af.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N9f = self.putDot(qp, x, y, "9\' \u2261 10\'") #AA1f
        self.N10f = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #B1C1f

        _N9 = QPoint(self.N9f.x(), self.N9f.y() + 50)
        x, y = count_cross(self.N9f, _N9, self.A, self.A1)
        self.N9 = self.putDot(qp, x, y, "9\'\'")

        _N10 = QPoint(self.N10f.x(), self.N10f.y() + 50)
        x, y = count_cross(self.N10f, _N10, self.B1, self.C1)
        self.N10 = self.putDot(qp, x, y, "10\'\'")

        qp.drawLine(self.N9f, self.N9)
        qp.drawLine(self.N9, self.N10)

        if (self.N9.y() / 4) < (self.N10.y() / 4):
                self.AA1f_visible = True
                self.ABf_visible = True
                self.ACf_visible = True

                self.A1C1f_visible = True
                self.A1B1f_visible = True

        else:
                self.B1C1f_visible = True
                self.A1B1f_visible = True
                self.BB1f_visible = True

                self.A1C1f_visible = True
                self.CC1f_visible = True
        flag = False

#BB1f & A1C1f
x, y = count_cross(self.Bf, self.B1f, self.A1f, self.C1f)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.C1f.x() <= x <= self.A1f.x()) or (self.A1f.x() <= x <= self.C1f.x())) and ((self.C1f.y() <= y <= self.A1f.y()) or (self.A1f.y() <= y <= self.C1f.y())) and ((self.Bf.x() <= x <= self.B1f.x()) or (self.B1f.x() <= x <= self.Bf.x())) and ((self.Bf.y() <= y <= self.B1f.y()) or (self.B1f.y() <= y <= self.Bf.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N9f = self.putDot(qp, x, y, "9\' \u2261 10\'") #BB1f
        self.N10f = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #A1C1f
        
        _N9 = QPoint(self.N9f.x(), self.N9f.y() + 50)
        x, y = count_cross(self.N9f, _N9, self.B, self.B1)
        self.N9 = self.putDot(qp, x, y, "9\'\'")

        _N10 = QPoint(self.N10f.x(), self.N10f.y() + 50)
        x, y = count_cross(self.N10f, _N10, self.A1, self.C1)
        self.N10 = self.putDot(qp, x, y, "10\'\'")

        qp.drawLine(self.N9f, self.N9)
        qp.drawLine(self.N9, self.N10)

        if (self.N9.y() / 4) < (self.N10.y() / 4):
                self.BB1f_visible = True
                self.ABf_visible = True
                self.BCf_visible = True

                self.B1C1f_visible = True
                self.A1B1f_visible = True

        else:
                self.A1C1f_visible = True
                self.A1B1f_visible = True
                self.AA1f_visible = True

                self.B1C1f_visible = True
                self.CC1f_visible = True
        flag = False

#CC1f & A1B1f
x, y = count_cross(self.C1f, self.Cf, self.A1f, self.B1f)
x = -(x * 4)
y = -(y * 4)
if flag and ((self.B1f.x() <= x <= self.A1f.x()) or (self.A1f.x() <= x <= self.B1f.x())) and ((self.B1f.y() <= y <= self.A1f.y()) or (self.A1f.y() <= y <= self.B1f.y())) and ((self.Cf.x() <= x <= self.C1f.x()) or (self.C1f.x() <= x <= self.Cf.x())) and ((self.Cf.y() <= y <= self.C1f.y()) or (self.C1f.y() <= y <= self.Cf.y())):
        x = -(x / 4)
        y = -(y / 4)
        self.N9f = self.putDot(qp, x, y, "9\' \u2261 10\'") #CC1f
        self.N10f = self.putDot(qp, x, y, " ", dot_visible=False, let_visible=False) #A1B1f

        _N9 = QPoint(self.N9f.x(), self.N9f.y() + 50)
        x, y = count_cross(self.N9f, _N9, self.C, self.C1)
        self.N9 = self.putDot(qp, x, y, "9\'\'")

        _N10 = QPoint(self.N10f.x(), self.N10f.y() + 50)
        x, y = count_cross(self.N10f, _N10, self.A1, self.B1)
        self.N10 = self.putDot(qp, x, y, "10\'\'")

        qp.drawLine(self.N9f, self.N9)
        qp.drawLine(self.N9, self.N10)

        if (self.N9.y() / 4) < (self.N10.y() / 4):
                self.CC1f_visible = True
                self.ACf_visible = True
                self.BCf_visible = True

                self.A1C1f_visible = True
                self.B1C1f_visible = True

        else:
                self.A1B1f_visible = True
                self.A1C1f_visible = True
                self.AA1f_visible = True

                self.B1C1f_visible = True
                self.BB1f_visible = True

        flag = False

"""
        self.solution_queue.put(code)


        code = """
pen.setWidth(2)
if self.ABf_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.Af, self.Bf)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.Af, self.Bf)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.Af, self.Bf)

if self.ACf_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.Af, self.Cf)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.Af, self.Cf)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.Af, self.Cf)

if self.BCf_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.Bf, self.Cf)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.Bf, self.Cf)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.Bf, self.Cf)

if self.A1B1f_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.A1f, self.B1f)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.A1f, self.B1f)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.A1f, self.B1f)

if self.B1C1f_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.B1f, self.C1f)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.B1f, self.C1f)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.B1f, self.C1f)

if self.A1C1f_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.A1f, self.C1f)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.A1f, self.C1f)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.A1f, self.C1f)

if self.AA1f_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.Af, self.A1f)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.Af, self.A1f)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.Af, self.A1f)

if self.BB1f_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.Bf, self.B1f)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.Bf, self.B1f)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.Bf, self.B1f)

if self.CC1f_visible:
        pen.setColor(Qt.black)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.Cf, self.C1f)
else:
        pen.setColor(Qt.white)
        pen.setStyle(Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.Cf, self.C1f)

        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.Cf, self.C1f)

"""
        self.solution_queue.put(code)

#--------------------------------------------------------------------------
        


    def next_frame(self):
        if not self.solution_queue.empty():

                chunk = self.solution_queue.get()

                return chunk

        else:
                return "self.hide()\nsys.exit()"


'''

        code = """

"""
        self.solution_queue.put(code)

        code = """
if -(self.N9.y() / 4) > -(self.N10.y() / 4):
        
        pen.setWidth(2)  
        pen.setColor(Qt.white)
        qp.setPen(pen)
        qp.drawLine(self.N7line[0], self.N7line[1])

        pen.setWidth(2)
        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.N7line[0], self.N7line[1])
else:
        pen.setWidth(2)
        pen.setColor(Qt.white)
        qp.setPen(pen)
        qp.drawLine(self.N8line[0], self.N8line[1])

        pen.setWidth(2)
        pen.setColor(Qt.black)
        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(self.N8line[0], self.N8line[1])
"""
        self.solution_queue.put(code)

'''
                
