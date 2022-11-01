#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import random
from PySide2.QtCore import Qt, QPoint
from PySide2.QtGui import QPainter, QBrush, QPen, QPolygon
from PySide2.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3adaHue4")
        self.setGeometry(80, 140, 300, 287)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.darkCyan)
        painter.drawRect(80, 140, 140, 120)
        painter.setBrush((QBrush(Qt.white)))
        painter.setBrush((QBrush(Qt.darkCyan)))
        points = QPolygon([
            QPoint(260, 140),
            QPoint(150, 43),
            QPoint(40, 140)
        ])
        painter.drawPolygon(points)
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        painter.setPen(QPen(Qt.darkYellow, 3, Qt.SolidLine))
        painter.drawEllipse(200, 3, 55, 55)
        self.drawGrass(painter)

    def drawGrass(self, painter):
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.green, 2, Qt.SolidLine))
        painter.setBrush(Qt.green)
        for i in range(30):
            painter.drawArc(random.randint(1, 8), 180, i * 10, 280, 0 * 100, random.randint(35, 65) * 10)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
