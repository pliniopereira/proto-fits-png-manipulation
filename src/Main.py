#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QGroupBox, QMessageBox

from src.layout.Layout import set_hbox, set_lvbox


class ProtoFitsHeaders(QWidget):
    def __init__(self, parent=None):
        super(ProtoFitsHeaders, self).__init__(parent)

        self.info_1 = None
        self.info_2 = None
        self.info_3 = None

        self.btn_1 = None
        self.btn_2 = None
        self.btn_3 = None
        self.btn_4 = None

        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        grid.addWidget(self.create_group(), 1, 0)
        self.setLayout(grid)

        self.button_settings()

        self.setWindowTitle("Proto - Fit and png Headers")
        self.resize(60, 60)
        self.show()

    def create_group(self):
        group_box = QGroupBox("&Fits Manipulation")

        self.info_1 = QtWidgets.QLabel("info_1:", self)
        self.info_1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        self.info_2 = QtWidgets.QLabel('info_2:', self)
        
        self.info_3 = QtWidgets.QLabel("info_3")
        self.info_3.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.info_3.setMinimumWidth(60)

        self.btn_1 = QtWidgets.QPushButton('btn_1', self)

        self.btn_2 = QtWidgets.QPushButton('btn_2', self)

        self.btn_3 = QtWidgets.QPushButton('btn_3', self)
        self.btn_4 = QtWidgets.QPushButton('btn_4', self)

        group_box.setLayout(set_lvbox(set_hbox(self.info_1),
                                      set_hbox(self.info_2, self.info_3, stretch2=1),
                                      set_hbox(self.btn_1),
                                      set_hbox(self.btn_2),
                                      set_hbox(self.btn_3),
                                      set_hbox(self.btn_4)))
        return group_box

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def fill_combo_1(self):
        self.set_combo.addItem("1", 1)
        self.set_combo.addItem("2", 2)
        self.set_combo.addItem("3", 3)
        self.set_combo.addItem("4", 4)
        self.set_combo.addItem("5", 5)
        self.set_combo.addItem("6", 6)

    def button_settings(self):
        self.btn_1.clicked.connect(self.func_1)
        self.btn_2.clicked.connect(self.func_2)

        self.btn_3.clicked.connect(self.func_3)
        self.btn_4.clicked.connect(self.func_4)

    def func_1(self):
        pass

    def func_2(self):
        pass

    def func_3(self):
        pass

    def func_4(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProtoFitsHeaders()
    sys.exit(app.exec_())
