# File: [PhotoBrowser.py]
# By: [David Hanover]
# Date: [9-16-2017]
# Compile: [Python]
# Usage: [Run with Python]
# System: [Running on Windows10 64bit, AMD Ryzen 7 chipset  AND Intel i7-6500u chipset]
# Description: [Browses a selection of images titled "Donut1.jpg"
# through "Donut10.jpg" located in the same folder as Model.py]
#
# NOTE: If you wish to substitute test pictures for the Donut.jpgs, change
# the strings in the QPixmap arguments that start at Line 56.
#
# For now, the program only works with 10 pictures, but that can be easily changed in the future

import sys
from CSC690HW1PhotoBrowser import View, Controller
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QAction, QLineEdit, QMessageBox, QMainWindow
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QUrl, pyqtSlot, QCoreApplication



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Photo Browser'
        self.index = 0
        self.mode = 0
        self.initUI()

        self.selectionMorpher(0)

        # Create labels
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.label5 = QLabel(self)

        # Store labels
        self.labels = [self.label1, self.label2, self.label3, self.label4, self.label5]



        # Create pixmaps   CHANGE DONUT NAMES IF YOU WISH TO SUBSTITUTE TEST PICTURES
        self.pixmap1 = QPixmap("Donut1.jpg")
        self.pixmap2 = QPixmap("Donut2.jpg")
        self.pixmap3 = QPixmap("Donut3.jpg")
        self.pixmap4 = QPixmap("Donut4.jpg")
        self.pixmap5 = QPixmap("Donut5.jpg")
        self.pixmap6 = QPixmap("Donut6.jpg")
        self.pixmap7 = QPixmap("Donut7.jpg")
        self.pixmap8 = QPixmap("Donut8.jpg")
        self.pixmap9 = QPixmap("Donut9.jpg")
        self.pixmap10 = QPixmap("Donut10.jpg")

        # Store pixmaps
        self.pixmaps = [self.pixmap1, self.pixmap2, self.pixmap3,
                        self.pixmap4, self.pixmap5, self.pixmap6,
                        self.pixmap7, self.pixmap8, self.pixmap9,
                        self.pixmap10]



        # Can't figure out how to access a QLabel's pixmap, so create array of
        # indexes to keep track of pixmaps
        self.indexes = []
        for i in range(0, 5, 1):
            self.indexes.append(i)

        self.show()




    def selectionMorpher(self, prev):
        # not totally sure why i made this its own function....
        #  but it changes the highlight color, and changes the previous color back to normal
        self.labels[prev].setStyleSheet("border: 10px solid purple")
        self.labels[self.index].setStyleSheet("border: 10px solid orange")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window = Display(window)
    sys.exit(app.exec_())