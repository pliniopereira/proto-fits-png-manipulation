import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QGroupBox, QMessageBox

from src.controller import Fit
from src.controller import Png
from src.layout.Layout import set_hbox, set_lvbox


class ProtoFitHeaders(QWidget):
    def __init__(self, parent=None):
        super(ProtoFitHeaders, self).__init__(parent)

        self.info_1 = None
        self.info_2 = None
        self.info_3 = None

        self.btn_select_image = None
        self.btn_show_info_png = None
        self.btn_3 = None
        self.btn_4 = None

        self.lImagesName = None
        self.eImagesName = None

        self.image_name = None

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
        group_box = QGroupBox("&Fit and Png Manipulation")

        self.info_1 = QtWidgets.QLabel("info_1", self)
        self.info_1.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignLeft)

        self.info_2 = QtWidgets.QLabel('info_2', self)
        self.info_2.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)

        self.info_3 = QtWidgets.QLabel("info_3")
        self.info_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignRight)

        self.lImagesName = QtWidgets.QLabel('Images Path:')
        self.eImagesName = QtWidgets.QLineEdit(self)
        self.eImagesName.setMinimumWidth(200)

        self.btn_select_image = QtWidgets.QPushButton('Open Image', self)

        self.btn_show_info_png = QtWidgets.QPushButton('Show Header Info', self)

        self.btn_3 = QtWidgets.QPushButton(u'btn_3', self)
        self.btn_3.setMaximumWidth(50)

        self.btn_4 = QtWidgets.QPushButton('btn_4', self)
        self.btn_4.setMaximumWidth(50)

        group_box.setLayout(set_lvbox(set_hbox(self.info_1),
                                      set_hbox(self.info_2),
                                      set_hbox(self.info_3),
                                      set_hbox(self.lImagesName, self.eImagesName, self.btn_select_image),
                                      set_hbox(self.btn_show_info_png),
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
        self.btn_select_image.clicked.connect(self.open_image)
        self.btn_show_info_png.clicked.connect(self.show_info_headers)

        self.btn_3.clicked.connect(self.func_3)
        self.btn_4.clicked.connect(self.func_4)

    def open_image(self):
        try:
            image_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Image')
            image_name = str(image_name[0])
            self.image_name = image_name
            self.eImagesName.setText(image_name)
        except Exception as e:
            print(e)

    def show_info_headers(self):
        if self.image_name[-3:] == 'png':
            Png.return_info(self.image_name)
        else:
            Fit.return_info(self.image_name)
            
    def func_3(self):
        pass

    def func_4(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProtoFitHeaders()
    sys.exit(app.exec_())
