import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import copy
import time


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.oldRect = 0
        self.flag = False
        self.first = True
        self.f_hi = True
        self.ur = 0
        self.spisok = []
        self.x = 0
        self.y = 0
        self.o_rez = 0
        self.k_rez = 0
        self.tur = 0
        self.oldx = 0
        self.oldy = 0
        self.poz1_x = 0
        self.poz1_y = 0
        self.poz2_x = 0
        self.poz2_y = 0
        self.oldFigures = None
        self.scene = QGraphicsScene()
        self.graphics_view = QGraphicsView()
        self.graphics_view.setScene(self.scene)
        self.graphics_view.setSceneRect(0, 0, 800, 800)
        self.setCentralWidget(self.graphics_view)
        self.pole = [[0, 3, 0, 3, 0, 3, 0, 3],
                     [3, 0, 3, 0, 3, 0, 3, 0],
                     [0, 3, 0, 3, 0, 3, 0, 3],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 1, 0, 1, 0, 1, 0],
                     [0, 1, 0, 1, 0, 1, 0, 1],
                     [1, 0, 1, 0, 1, 0, 1, 0]]
        self.initui()

    def initui(self):
        self.setGeometry(300, 100, 802, 802)
        self.setWindowTitle('chess')
        self.show()

    def paintEvent(self, e):
        if self.flag:  # рисуем прямоугольник выделенную ячейку
            if self.oldRect != 0:
                self.scene.removeItem(self.oldRect)
            Rect = QGraphicsRectItem(self.x, self.y, 100, 100)
            Rect.setPen(QPen(Qt.red, 2, ))
            self.scene.addItem(Rect)
            self.flag = False
            self.oldRect = Rect

        else:
            if self.first:  # если первый запуск то рисуем шахматную доску
                for i in range(8):
                    for j in range(8):
                        if (8 - i + 1 + j) % 2 == 0:
                            Rect = QGraphicsRectItem(i * 100, j * 100, 100, 100)
                            Rect.setBrush(QColor(101, 67, 33))

                        else:
                            Rect = QGraphicsRectItem(i * 100, j * 100, 100, 100)
                            Rect.setBrush(QColor(255, 255, 255))
                        self.scene.addItem(Rect)

                pawnW1 = QGraphicsPixmapItem(QPixmap('1.png').scaled(99, 99))
                self.scene.addItem(pawnW1)
                pawnW1.setOffset(0, 500)
                pawnW2 = QGraphicsPixmapItem(QPixmap('1.png').scaled(99, 99))
                self.scene.addItem(pawnW2)
                pawnW2.setOffset(200, 500)
                pawnW3 = QGraphicsPixmapItem(QPixmap('1.png').scaled(99, 99))
                self.scene.addItem(pawnW3)
                pawnW3.setOffset(400, 500)
                pawnW4 = QGraphicsPixmapItem(QPixmap('1.png').scaled(99, 99))
                self.scene.addItem(pawnW4)
                pawnW4.setOffset(600, 500)
                pawnW5 = QGraphicsPixmapItem(QPixmap('1.png').scaled(99, 99))
                self.scene.addItem(pawnW5)
                pawnW5.setOffset(100, 600)
                pawnW6 = QGraphicsPixmapItem(QPixmap('1.png').scaled(99, 99))
                self.scene.addItem(pawnW6)
                pawnW6.setOffset(300, 600)
                pawnW7 = QGraphicsPixmapItem(QPixmap('1.png').scaled(99, 99))
                self.scene.addItem(pawnW7)
                pawnW7.setOffset(500, 600)
                pawnW8 = QGraphicsPixmapItem(QPixmap('1.png').scaled(99, 99))
                self.scene.addItem(pawnW8)
                pawnW8.setOffset(700, 600)
                pawnW10 = QGraphicsPixmapItem(QPixmap('1.png').scaled(99, 99))
                self.scene.addItem(pawnW10)
                pawnW10.setOffset(0, 700)
                pawnW11 = QGraphicsPixmapItem(QPixmap('1.png').scaled(99, 99))
                self.scene.addItem(pawnW11)
                pawnW11.setOffset(200, 700)
                pawnW12 = QGraphicsPixmapItem(QPixmap('1.png').scaled(99, 99))
                self.scene.addItem(pawnW12)
                pawnW12.setOffset(400, 700)
                pawnW13 = QGraphicsPixmapItem(QPixmap('1.png').scaled(99, 99))
                self.scene.addItem(pawnW13)
                pawnW13.setOffset(600, 700)

                pawnW14 = QGraphicsPixmapItem(QPixmap('2.png').scaled(99, 99))
                self.scene.addItem(pawnW14)
                pawnW14.setOffset(100, 0)
                pawnW15 = QGraphicsPixmapItem(QPixmap('2.png').scaled(99, 99))
                self.scene.addItem(pawnW15)
                pawnW15.setOffset(300, 0)
                pawnW16 = QGraphicsPixmapItem(QPixmap('2.png').scaled(99, 99))
                self.scene.addItem(pawnW16)
                pawnW16.setOffset(500, 0)
                pawnW17 = QGraphicsPixmapItem(QPixmap('2.png').scaled(99, 99))
                self.scene.addItem(pawnW17)
                pawnW17.setOffset(700, 0)
                pawnW18 = QGraphicsPixmapItem(QPixmap('2.png').scaled(99, 99))
                self.scene.addItem(pawnW18)
                pawnW18.setOffset(0, 100)
                pawnW19 = QGraphicsPixmapItem(QPixmap('2.png').scaled(99, 99))
                self.scene.addItem(pawnW19)
                pawnW19.setOffset(200, 100)
                pawnW20 = QGraphicsPixmapItem(QPixmap('2.png').scaled(99, 99))
                self.scene.addItem(pawnW20)
                pawnW20.setOffset(400, 100)
                pawnW21 = QGraphicsPixmapItem(QPixmap('2.png').scaled(99, 99))
                self.scene.addItem(pawnW21)
                pawnW21.setOffset(600, 100)
                pawnW22 = QGraphicsPixmapItem(QPixmap('2.png').scaled(99, 99))
                self.scene.addItem(pawnW22)
                pawnW22.setOffset(100, 200)
                pawnW23 = QGraphicsPixmapItem(QPixmap('2.png').scaled(99, 99))
                self.scene.addItem(pawnW23)
                pawnW23.setOffset(300, 200)
                pawnW24 = QGraphicsPixmapItem(QPixmap('2.png').scaled(99, 99))
                self.scene.addItem(pawnW24)
                pawnW24.setOffset(500, 200)
                pawnW25 = QGraphicsPixmapItem(QPixmap('2.png').scaled(99, 99))
                self.scene.addItem(pawnW25)
                pawnW25.setOffset(700, 200)
                self.first = False

    def mousePressEvent(self, event):
        self.x = int(event.pos().x() / 100) * 100
        self.y = int(event.pos().y() / 100) * 100
        self.flag = True

        serh = True
        it = self.graphics_view.items(self.x + 50, self.y + 50)
        for k in it:
            if str(type(k)) == "<class 'PyQt5.QtWidgets.QGraphicsPixmapItem'>":
                self.oldFigures = k
                serh = False
        if serh is not None and self.oldFigures is not None:
            self.oldFigures.setOffset(self.x, self.y)
            self.oldFigures = None

        self.oldx = self.x
        self.oldy = self.y
        self.update()
        self.pozici_2()

    def pozici_2(self):
        x, y = self.x // 100, self.y // 100
        if self.pole[y][x] == 1 or self.pole[y][x] == 2:
            self.poz1_x, self.poz1_y = x, y
        else:
            if self.poz1_x != -1:
                self.poz2_x, self.poz2_y = x, y
                if self.f_hi:
                    self.hod_igroka()
                    if not self.f_hi:
                        self.hod_kompjutera()
                self.poz1_x = -1

    def hod_kompjutera(self):
        self.proverka_hk()
        if self.n2_spisok:
            kh = len(self.n2_spisok)
            th = random.randint(0, kh - 1)
            dh = len(self.n2_spisok[th])
            for h in self.n2_spisok:
                h = h
            for i in range(dh - 1):
                self.hod()
            self.n2_spisok = []
            self.f_hi = True
        s_k, s_i = self.skan()
        if not s_i:
            self.s = 2
            self.soobsenie()
        elif not s_k:
            self.s = 1
            self.soobsenie()
        elif self.f_hi and not (self.spisok_hi()):
            self.s = 3
            self.soobsenie()
        elif not self.f_hi and not self.spisok_hk():
            self.s = 3
            self.soobsenie()

    def spisok_hk(self):
        self.spisok = self.prosmotr_hodov_k1()
        if not self.spisok:
            self.spisok = self.prosmotr_hodov_k2()

    def proverka_hk(self):
        global l_rez
        if not self.spisok:
            self.spisok = self.spisok_hk()
        if self.spisok:
            k_pole = self.pole.copy()
            for self.poz1_x, self.poz1_y in self.spisok:
                t_spisok = self.hod()
                if t_spisok:
                    self.proverka_hk()
                else:
                    self.proverka_hi()
                    if self.tur == 1:
                        t_rez = self.o_rez / self.k_rez
                        if not (self.n2_spisok):
                            self.n2_spisok = (
                                self.n_spisok + ((self.poz1_x, self.poz1_y), (self.poz2_x, self.poz2_y)),)
                            l_rez = t_rez
                        else:
                            if t_rez == l_rez:
                                self.n2_spisok = self.n2_spisok + (
                                    self.n_spisok + ((self.poz1_x, self.poz1_y), (self.poz2_x, self.poz2_y)),)
                            if t_rez > l_rez:
                                self.n2_spisok = ()
                                self.n2_spisok = (
                                    self.n_spisok + ((self.poz1_x, self.poz1_y), (self.poz2_x, self.poz2_y)),)
                                l_rez = t_rez
                        self.o_rez = 0
                        self.k_rez = 0
                self.pole = copy.deepcopy(k_pole)
        else:
            s_k, s_i = self.skan()
            self.o_rez += (s_k - s_i)
            self.k_rez += 1

    def spisok_hi(self):
        self.prosmotr_hodov_i1()
        if not self.spisok:
            self.prosmotr_hodov_i2()

    def proverka_hi(self):
        if not self.spisok:
            self.spisok_hi()
        if self.spisok:
            k_pole = copy.deepcopy(self.pole)
            for self.poz1_x, self.poz1_y in self.spisok:
                t_spisok = self.hod()
                if t_spisok:
                    self.proverka_hi()
                else:
                    if self.tur < self.ur:
                        self.proverka_hk()
                    else:
                        s_k, s_i = self.skan()
                        self.o_rez += (s_k - s_i)
                        self.k_rez += 1

                self.pole = copy.deepcopy(k_pole)
        else:
            s_k, s_i = self.skan()
            self.o_rez += (s_k - s_i)
            self.k_rez += 1

    def skan(self):
        s_i = 0
        s_k = 0
        for i in range(8):
            for ii in self.pole[i]:
                if ii == 1: s_i += 1
                if ii == 2: s_i += 3
                if ii == 3: s_k += 1
                if ii == 4: s_k += 3
        return s_k, s_i

    def hod_igroka(self):
        self.f_hi = False
        self.spisok_hi()
        if self.spisok:
            if (self.poz1_x, self.poz1_y) and (self.poz2_x, self.poz2_y) in self.spisok:
                t_spisok = self.hod()
                if t_spisok:
                    self.f_hi = True
            else:
                self.f_hi = True
        self.update()

    def hod(self):
        if self.poz2_y == 0 and self.pole[self.poz1_y][self.poz1_x] == 1:
            self.pole[self.poz1_y][self.poz1_x] = 2
        if self.poz2_y == 7 and self.pole[self.poz1_y][self.poz1_x] == 3:
            self.pole[self.poz1_y][self.poz1_x] = 4
        self.pole[self.poz2_y][self.poz2_x] = self.pole[self.poz1_y][self.poz1_x]
        self.pole[self.poz1_y][self.poz1_x] = 0
        kx = ky = 1
        if self.poz1_x < self.poz2_x: kx = -1
        if self.poz1_y < self.poz2_y: ky = -1
        x_poz, y_poz = self.poz2_x, self.poz2_y
        while (self.poz1_x != x_poz) or (self.poz1_y != y_poz):
            x_poz += kx
            y_poz += ky
            if self.pole[y_poz][x_poz] != 0:
                self.pole[y_poz][x_poz] = 0
                if self.pole[self.poz2_y][self.poz2_x] == 3 or self.pole[self.poz2_y][self.poz2_x] == 4:
                    self.prosmotr_hodov_k1p()
                elif self.pole[self.poz2_y][self.poz2_x] == 1 or self.pole[self.poz2_y][self.poz2_x] == 2:
                    self.prosmotr_hodov_i1p()

    def prosmotr_hodov_i1p(self):
        if self.pole[self.y][self.x] == 1:
            for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
                if 0 <= self.y + iy + iy <= 7 and 0 <= self.x + ix + ix <= 7:
                    if self.pole[self.y + iy][self.x + ix] == 3 or self.pole[self.y + iy][self.x + ix] == 4:
                        if self.pole[self.y + iy + iy][self.x + ix + ix] == 0:
                            self.spisok.append(
                                ((self.x, self.y), (self.x + ix + ix, self.y + iy + iy)))  # запись хода в конец списка
        if self.pole[self.y][self.x] == 2:  # пешка с короной
            for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
                osh = 0  # определение правильности хода
                for i in range(1, 8):
                    if 0 <= self.y + iy * i <= 7 and 0 <= self.x + ix * i <= 7:
                        if osh == 1:
                            self.spisok.append(
                                ((self.x, self.y), (self.x + ix * i, self.y + iy * i)))  # запись хода в конец списка
                        if self.pole[self.y + iy * i][self.x + ix * i] == 3 or self.pole[self.y + iy * i][
                            self.x + ix * i] == 4:
                            osh += 1
                        if self.pole[self.y + iy * i][self.x + ix * i] == 1 or self.pole[self.y + iy * i][
                            self.x + ix * i] == 2 or osh == 2:
                            if osh > 0: self.spisok.pop()  # удаление хода из списка
                            break

    def prosmotr_hodov_i2(self):  # проверка наличия остальных ходов
        for self.y in range(8):  # сканируем всё поле
            for self.x in range(8):
                if self.pole[self.y][self.x] == 1:  # пешка
                    for ix, iy in (-1, -1), (1, -1):
                        if 0 <= self.y + iy <= 7 and 0 <= self.x + ix <= 7:
                            if self.pole[self.y + iy][self.x + ix] == 0:
                                self.spisok.extend(((self.x, self.y),
                                                    (self.x + ix, self.y + iy)))  # запись хода в конец списка
                            if self.pole[self.y + iy][self.x + ix] == 3 or self.pole[self.y + iy][self.x + ix] == 4:
                                if 0 <= self.y + iy * 2 <= 7 and 0 <= self.x + ix * 2 <= 7:
                                    if self.pole[self.y + iy * 2][self.x + ix * 2] == 0:
                                        self.extend.append(
                                            ((self.x, self.y), (self.x + ix * 2, self.y + iy * 2)))  # запись хода в конец списка
                if self.pole[self.y][self.x] == 2:  # пешка с короной
                    for ix, iy in (-1, -1), (-1, 1), (1, -1), (1, 1):
                        osh = 0  # определение правильности хода
                        for i in range(1, 8):
                            if 0 <= self.y + iy * i <= 7 and 0 <= self.x + ix * i <= 7:
                                if self.pole[self.y + iy * i][self.x + ix * i] == 0:
                                    self.spisok.extend(((self.x, self.y), (
                                        self.x + ix * i, self.y + iy * i)))  # запись хода в конец списка
                                if self.pole[self.y + iy * i][self.x + ix * i] == 3 or self.pole[self.y + iy * i][
                                    self.x + ix * i] == 4:
                                    osh += 1
                                if self.pole[self.y + iy * i][self.x + ix * i] == 1 or self.pole[self.y + iy * i][
                                    self.x + ix * i] == 2 or osh == 2:
                                    break

    def prosmotr_hodov_i1(self):  # проверка наличия обязательных ходов
        self.spisok = []  # список ходов
        for self.y in range(8):  # сканируем всё поле
            for self.x in range(8):
                self.prosmotr_hodov_i1p()

    def soobsenie(self):
        if self.s == 1:
            exit(0)
        if self.s == 2:
            exit(0)
        if self.s == 3:
            exit(0)


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
