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
    def __init__(self):
        super().__init__()
        super().setupUi(self)

    def next(self):
        coordinates = (int(self.lineEdit.text()), int(self.lineEdit_2.text()))
        X, Y = int(self.lineEdit.text()), int(self.lineEdit_2.text())
        return self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(),\
               self.lineEdit_4.text()


def find_map():
    app = QApplication(sys.argv)
    ex = PyQtWindow()
    ex.show()
    sys.exit(app.exec())


class Programme:
    def __init__(self, width, height, window_name="NO_NAME", fullscreen=False):
        self.isWindowOpen = True
        self.width = width
        self.height = height
        pygame.init()
        if not fullscreen:
            pygame.display.set_mode((width, height))
        else:
            pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(window_name)

    def loop(self):
        while self.isWindowOpen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isWindowOpen = False
            pygame.display.flip()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    window = Programme(WIDTH, HEIGHT, WINDOW_NAME, FULLSCREEN)
    find_map()
