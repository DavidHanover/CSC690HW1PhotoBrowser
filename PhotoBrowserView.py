# File: [PhotoBrowser.py]
# By: [David Hanover]
# Date: [9-16-2017]
# Compile: [Python]
# Usage: [Run with Python]
# System: [Running on Windows10 64bit, AMD Ryzen 7 chipset  AND Intel i7-6500u chipset]
# Description: [Browses a selection of images titled "Donut1.jpg"
# through "Donut10.jpg" located in the same folder as PhotoBrowserView.py]
#
# NOTE: If you wish to substitute test pictures for the Donut.jpgs, change
# the strings in the QPixmap arguments that start at Line 56.
#
# For now, the program only works with 10 pictures, but that can be easily changed in the future

import sys
import PhotoBrowserModel
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QSoundEffect


class Window(QWidget):
    def __init__(self, pBM):
        super().__init__()
        self.photoBM = pBM

        self.title = 'PyQt5 Photo Browser'
        self.index = 0
        self.mode = 0
        self.initUI()

        self.selectionMorpher(0)

        # Store labels
        self.labels = []

        # Create labels
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.label5 = QLabel(self)

        self.Width = 1600;
        self.widthSelector()
        self.Length = ((self.Width/4)*3)


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 1600, 900)
        self.setStyleSheet("background-color: skyblue")


        # Loop for initializing labels
        spacingNum = 50

        for i in range (0, 5, 1):
            self.labels[i].resize(300, 300)
            self.labels[i].move(spacingNum, 150)
            self.labels[i].setStyleSheet("border: 10px solid purple")
            spacingNum += 302

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



        self.OGpixmaps = self.pixmaps

        # Set initial pixmaps to labels
        for i in range(0, 5, 1):
            self.pixmaps[i] = self.pixmaps[i].scaled(self.labels[i].size(), Qt.KeepAspectRatio)
            self.labels[i].setPixmap(self.pixmaps[i])



        self.show()

        self.sound1 = QSoundEffect()
        self.sound2 = QSoundEffect()
        self.sound1.setSource(QUrl.fromLocalFile('Click1.wav'))
        self.sound2.setSource(QUrl.fromLocalFile('Click2.wav'))

    def widthSelector(self):
        newWidth = input('Enter desired width:')
        self.Width = newWidth

    def selectionMorpher(self, prev):
        # not totally sure why i made this its own function....
        #  but it changes the highlight color, and changes the previous color back to normal
        self.labels[prev].setStyleSheet("border: 10px solid purple")
        self.labels[self.index].setStyleSheet("border: 10px solid orange")

    def keyPressEvent(self, event):
        print(event.key())
        if event.key()==16777235:
            # when up is hit, change mode if not already in mode 1 & play sound2
            if self.mode == 0:
                self.mode = 1
                self.sound2.play()
                # then resize label
                self.labels[self.index].resize(800, 800)
                self.labels[self.index].move(400, 50)
                # resize all other labels to be invisible
                i = self.index + 1
                while True:
                    if i == 5:
                        i = 0
                    if i == self.index:
                        break
                    self.labels[i].resize(0, 0)
                    i += 1

                self.labels[self.index]\
                    .setPixmap(self.pixmaps[self.indexes[self.index]]
                               .scaled(self.labels[self.index]
                                       .size(), Qt.KeepAspectRatio))

        if event.key()==16777237:


            # when down is hit, toggle mode back to normal if not already & play sound1
            if self.mode == 1:
                self.mode = 0
                self.sound1.play()

                spacingNum = 50

                # Reset the size and positions of all the labels,
                # using code copied from initUI
                for i in range(0, 5, 1):
                    self.labels[i].resize(300, 300)
                    self.labels[i].move(spacingNum, 150)
                    self.labels[i].setStyleSheet("border: 10px solid purple")
                    spacingNum += 302
            self.labels[self.index].setStyleSheet("border: 10px solid orange")

            # Reset the size of all the pixmaps back to normal
            for i in range(0, 5, 1):
                self.pixmaps[self.indexes[i]] = \
                    self.pixmaps[self.indexes[i]]\
                        .scaled(self.labels[i].size(), Qt.KeepAspectRatio)

                self.labels[i].setPixmap(self.pixmaps[self.indexes[i]])

        if event.key() == 16777234:

            # in zoomed mode, just change the pixmap you're currently viewing & play sound
            # IMO it's not a big deal, but this shifts the entire order in regular mode as well
            if self.mode == 1:
                self.sound1.play()
                for i in range(0, 5, 1):
                    self.indexes[i] -= 1
                    if self.indexes[i] == -1:
                        self.indexes[i] = 9

                for i in range(0, 5, 1):
                    self.labels[i].setPixmap \
                        (self.pixmaps[self.indexes[i]]
                         .scaled(self.labels[i].size(), Qt.KeepAspectRatio))


            # in regular mode, however, wait until you're at the edge, and then change them all by five
            if self.mode == 0:
                tmp = self.index
                self.index -= 1
                if self.index!= -1:
                    self.sound1.play()


                # if you reach the left end, wrap around, and
                if self.index == -1:
                    self.index = 4
                    self.sound2.play()

                    # decrement the pixmap indexes by five
                    for i in range (0, 5, 1):
                        for i in range (0, 5, 1):
                            self.indexes[i]-=1
                            if self.indexes[i]==-1:
                                self.indexes[i]=9

                    # reset all the pixmaps and make sure they're scaled
                    for i in range (0, 5, 1):
                        self.labels[i].setPixmap\
                            (self.pixmaps[self.indexes[i]]
                             .scaled(self.labels[i].size(), Qt.KeepAspectRatio))
                self.selectionMorpher(tmp)

        if event.key() == 16777236:

            # zoomed mode, just increment by one, & play sound
            if self.mode == 1:
                self.sound1.play()
                for i in range(0, 5, 1):
                    self.indexes[i] += 1
                    if self.indexes[i] == 10:
                        self.indexes[i] = 0

                for i in range(0, 5, 1):
                    self.labels[i].setPixmap \
                        (self.pixmaps[self.indexes[i]]
                         .scaled(self.labels[i].size(), Qt.KeepAspectRatio))

            # regular mode, increment by one & play sound 1
            if self.mode == 0:
                tmp = self.index
                self.index += 1
                if self.index!=5:
                    self.sound1.play()
                # if you reach right end, wrap around, play sound2, and
                if self.index == 5:
                    self.index = 0
                    self.sound2.play()
                    # increment the pixmap indexes by five
                    for i in range (0, 5, 1):
                        for i in range (0, 5, 1):
                            self.indexes[i]+=1
                            if self.indexes[i]==10:
                                self.indexes[i]=0
                    # reset all the pixmaps and make sure they're scaled
                    for i in range (0, 5, 1):
                        self.labels[i].setPixmap\
                            (self.pixmaps[self.indexes[i]]
                             .scaled(self.labels[i].size(), Qt.KeepAspectRatio))
                self.selectionMorpher(tmp)

        if event.key()==44:
            # if carrot left is hit, decrement the pixmap indexes by five
            self.sound2.play()
            for i in range(0, 5, 1):
                for i in range(0, 5, 1):
                    self.indexes[i] -= 1
                    if self.indexes[i] == -1:
                        self.indexes[i] = 9

            # reset all the pixmaps and make sure they're scaled
            for i in range(0, 5, 1):
                self.labels[i].setPixmap \
                    (self.pixmaps[self.indexes[i]]
                     .scaled(self.labels[i].size(), Qt.KeepAspectRatio))


        if event.key()==46:
            # if carrot right is hit, decrement the pixmap indexes by five
            self.sound2.play()
            for i in range(0, 5, 1):
                for i in range(0, 5, 1):
                    self.indexes[i] -= 1
                    if self.indexes[i] == -1:
                        self.indexes[i] = 9

            # reset all the pixmaps and make sure they're scaled
            for i in range(0, 5, 1):
                self.labels[i].setPixmap \
                    (self.pixmaps[self.indexes[i]]
                     .scaled(self.labels[i].size(), Qt.KeepAspectRatio))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())