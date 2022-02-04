import pygame
import requests
import sys
import finding_map
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


WIDTH, HEIGHT = 300, 300
WINDOW_NAME = "MapsAPI"
FULLSCREEN = False
api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
coordinates = (0, 0)
X, Y = (0, 0)


class PyQtWindow(QMainWindow, finding_map.Ui_MainWindow):
    def __init__(self, width, height, window_name="NO_NAME"):
        super().__init__()
        super().setupUi(self)
        self.pushButton.clicked.connect(self.exit)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


sys.excepthook = except_hook

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = PyQtWindow(WIDTH, HEIGHT, WINDOW_NAME)
    ex.show()
    sys.exit(app.exec())
