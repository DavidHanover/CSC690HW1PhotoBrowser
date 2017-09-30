#import sys
import Model, Controller
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import Qt, QUrl


class Display(Model.window):

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 1600, 900)
        self.setStyleSheet("background-color: skyblue")

    # Loop for initializing labels
        spacingNum  = 50

        for i in range (0, 5, 1):
            self.labels[i].resize(300, 300)
            self.labels[i].move(spacingNum, 150)
            self.labels[i].setStyleSheet("border: 10px solid purple")
            spacingNum += 302

    # Set initial pixmaps to labels
        for i in range(0, 5, 1):
            self.pixmaps[i] = self.pixmaps[i].scaled(self.labels[i].size(), Qt.KeepAspectRatio)
            self.labels[i].setPixmap(self.pixmaps[i])

        self.sound1 = QSoundEffect()
        self.sound2 = QSoundEffect()
        self.sound1.setSource(QUrl.fromLocalFile('Click1.wav'))
        self.sound2.setSource(QUrl.fromLocalFile('Click2.wav'))

        def selectionMorpher(self, prev):
            # not totally sure why i made this its own function....
            #  but it changes the highlight color, and changes the previous color back to normal
            self.labels[prev].setStyleSheet("border: 10px solid purple")
            self.labels[self.index].setStyleSheet("border: 10px solid orange")