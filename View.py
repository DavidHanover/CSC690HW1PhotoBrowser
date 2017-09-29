from CSC690HW1PhotoBrowser import Model
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import Qt, QUrl


class Display(Model.Window):

    def initUI(self):
        Model.Window.setWindowTitle(self.title)
        Model.Window.setGeometry(100, 100, 1600, 900)
        Model.Window.setStyleSheet("background-color: skyblue")

    # Loop for initializing labels
        spacingNum  = 50

        for i in range (0, 5, 1):
            Model.Window.labels[i].resize(300, 300)
            Model.Window.labels[i].move(spacingNum, 150)
            Model.Window.labels[i].setStyleSheet("border: 10px solid purple")
            spacingNum += 302

    # Set initial pixmaps to labels
        for i in range(0, 5, 1):
            Model.Window.pixmaps[i] = self.pixmaps[i].scaled(self.labels[i].size(), Qt.KeepAspectRatio)
            Model.Window.labels[i].setPixmap(self.pixmaps[i])

        Model.Window.sound1 = QSoundEffect()
        Model.Window.sound2 = QSoundEffect()
        Model.Window.sound1.setSource(QUrl.fromLocalFile('Click1.wav'))
        Model.Window.sound2.setSource(QUrl.fromLocalFile('Click2.wav'))