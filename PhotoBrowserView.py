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
import pickle
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QListWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QSoundEffect


class pbView(QWidget):
    def __init__(self, pbM):
        super().__init__()
        self.title = 'PyQt5 Photo Browser'

        self.wid = 1200
        if len(sys.argv) > 1:
            self.wid = int(sys.argv[1])
            if self.wid > 1200 or self.wid < 900:
                self.wid = 1200
        self.len = int(self.wid*0.75)

        self.buttonSzX = int(self.wid * 0.083)
        self.buttonSzY = int(self.len * 0.061)

        self.spacingNum  = int(self.wid*0.03125)
        self.labSiz = int(self.wid*0.1875)
        self.ySpace = int(self.len * 0.3)
        self.bigLabSiz = int(self.wid*0.5)

        self.pbModel = pbM

        self.mdTxbx = QLineEdit(self)
        self.mdTxbx.move(10, self.len-120)

        self.srchTxbx = QLineEdit(self)
        self.srchTxbx.move(0, (self.len-100-(self.buttonSzY)))

        self.srLenTxbx = QLineEdit(self)
        self.srLenTxbx.move(self.wid-(self.wid/4), (self.len-100-(self.buttonSzY)))
        self.MaxSrchRslts = QLabel (self)
        self.MaxSrchRslts.setText( "Max Search Results:")
        self.MaxSrchRslts.move(self.wid-(self.wid/4)-125, (self.len-90-(self.buttonSzY)))
        self.MaxSrchRslts.setFocusPolicy(Qt.NoFocus)

        self.textWid = int(self.wid*0.233)
        self.textLen = int(self.len*0.045)

        self.srLenTxbx.resize(self.wid/4, self.textLen)
        self.mdTxbx.resize(self.textWid, self.textLen)
        self.srchTxbx.resize(self.wid/2, self.textLen)

        self.mdTxbx.setFocusPolicy(Qt.ClickFocus)
        self.srLenTxbx.setFocusPolicy(Qt.ClickFocus)
        self.srchTxbx.setFocusPolicy(Qt.ClickFocus)
        self.mdTxbx.setStyleSheet("background-color: orange")

        self.mdTxbx.setVisible(False)
        self.srchTxbx.setVisible(True)

        self.metaLists = []
        for j in range (0, 10, 1):
            self.metaLists.append([])

        self.tempList = []
        self.loadMetaData()

        self.pListWidg = QListWidget(self)

        self.pLWwidth = int(self.wid*0.167)
        self.pLWlength = int (self.len*0.056)

        self.pListWidg.resize(self.pLWwidth, self.len-self.pLWlength)

        self.pLWmoveX = int(self.wid*0.208)
        self.pLWmovey = int(self.len*0.028)

        self.pListWidg.move(self.wid-self.pLWmoveX, self.pLWmovey)
        self.pListWidg.setVisible(False)

        self.tListWidg = QListWidget(self)

        self.tLWwidth = int(self.wid*0.17)
        self.tLWlength = int(self.len*0.18)

        self.tListWidg.resize(self.tLWwidth, self.len-175)

        self.tLWmoveX = int(self.wid*0.0417)
        self.tLWmoveY = int(self.len*0.028)

        self.tListWidg.move(self.tLWmoveX, self.tLWmoveY)
        self.tListWidg.setVisible(False)


        self.initUI()

        self.selectionMorpher(0)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, self.wid, self.len)
        self.setStyleSheet("background-color: skyblue")

        # Create labels
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.label5 = QLabel(self)

        self.label1.setFocusPolicy(Qt.ClickFocus)
        self.label2.setFocusPolicy(Qt.ClickFocus)
        self.label3.setFocusPolicy(Qt.ClickFocus)
        self.label4.setFocusPolicy(Qt.ClickFocus)
        self.label5.setFocusPolicy(Qt.ClickFocus)

        # Store labels
        self.labels = [self.label1, self.label2, self.label3, self.label4, self.label5]

        # Loop for initializing labels

        for i in range (0, 5, 1):
            self.labels[i].resize(self.labSiz, self.labSiz)
            self.labels[i].move(self.spacingNum, self.ySpace)
            self.labels[i].setStyleSheet("border: 10px solid purple")
            self.spacingNum += (self.labSiz+2)

        self.show()

        self.sound1 = QSoundEffect()
        self.sound2 = QSoundEffect()
        self.sound1.setSource(QUrl.fromLocalFile('Click1.wav'))
        self.sound2.setSource(QUrl.fromLocalFile('Click2.wav'))

        self.enterMD = QPushButton('Enter', self)
        self.enterMD.clicked.connect(self.addMtdt)
        self.saveMD = QPushButton('Save', self)
        self.saveMD.clicked.connect(self.saveMtdt)

        self.testB = QPushButton('Test', self)
        self.saveB = QPushButton('Save', self)
        self.exitB = QPushButton('Exit', self)
        self.deleteB = QPushButton('Delete', self)
        self.searchB = QPushButton('Search', self)



        self.enterMD.resize(self.buttonSzX, self.buttonSzY)
        self.saveMD.resize(self.buttonSzX, self.buttonSzY)

        self.testB.resize(self.buttonSzX, self.buttonSzY)
        self.saveB.resize(self.buttonSzX, self.buttonSzY)
        self.exitB.resize(self.buttonSzX, self.buttonSzY)
        self.deleteB.resize(self.buttonSzX, self.buttonSzY)
        self.searchB.resize(self.buttonSzX, self.buttonSzY)

        self.buttonMoveY = int(self.len*0.083)
        self.enterMoveX = int (self.wid*0.021)
        self.saveMoveX = int(self.wid*0.125)

        self.enterMD.move(self.enterMoveX, self.len - self.buttonMoveY)
        self.saveMD.move(self.saveMoveX, self.len - self.buttonMoveY)

        self.testB.move(0, self.len-100)
        self.saveB.move(self.buttonSzX, self.len-100)
        self.exitB.move(self.buttonSzX*2, self.len-100)
        self.deleteB.move(self.buttonSzX*3, self.len-100)
        self.searchB.move(self.buttonSzX*4, self.len-100)

        self.enterMD.setFocusPolicy(Qt.NoFocus)
        self.saveMD.setFocusPolicy(Qt.NoFocus)

        self.testB.setFocusPolicy(Qt.NoFocus)
        self.saveB.setFocusPolicy(Qt.NoFocus)
        self.exitB.setFocusPolicy(Qt.NoFocus)
        self.deleteB.setFocusPolicy(Qt.NoFocus)
        self.searchB.setFocusPolicy(Qt.NoFocus)

        self.enterMD.setStyleSheet("background-color: Orange")
        self.saveMD.setStyleSheet("background-color: Orange")

        self.testB.setStyleSheet("background-color: Orange")
        self.saveB.setStyleSheet("background-color: Orange")
        self.exitB.setStyleSheet("background-color: Orange")
        self.deleteB.setStyleSheet("background-color: Orange")
        self.searchB.setStyleSheet("background-color: Orange")

        self.enterMD.setVisible(False)
        self.saveMD.setVisible(False)

        self.testB.setVisible(True)
        self.saveB.setVisible(True)
        self.exitB.setVisible(True)
        self.deleteB.setVisible(True)
        self.searchB.setVisible(True)

    def addMtdt(self):
        self.tListWidg.addItem(self.mdTxbx.text())
        self.tempList.append(self.mdTxbx.text())


    def saveMtdt(self):
        for g in range (len(self.tempList), 0, -1):
            self.metaLists[self.pbModel.indexes[self.pbModel.index]].append(self.tempList.pop())
            self.pListWidg.clear()
            self.pListWidg.addItems(self.metaLists[self.pbModel.indexes[self.pbModel.index]])
            self.tListWidg.clear()
            self.saveMetaData()




    def selectionMorpher(self, prev):
        # not totally sure why i made this its own function....
        #  but it changes the highlight color, and changes the previous color back to normal
        self.labels[prev].setStyleSheet("border: 10px solid purple")
        self.labels[self.pbModel.index].setStyleSheet("border: 10px solid orange")

    def saveMetaData(self):

        md1 = open("metaData.p", 'wb')
        pickle.dump(self.metaLists, md1)

        # md1 = open("metaData1.p")
        # pickle.dump(self.metaLists[0], md1)
        # md2 = open("metaData2.p")
        # pickle.dump(self.metaLists[1], md2)
        # md3 = open("metaData3.p")
        # pickle.dump(self.metaLists[0], md3)
        # md4 = open("metaData4.p")
        # pickle.dump(self.metaLists[0], md4)
        # md5 = open("metaData5.p")
        # pickle.dump(self.metaLists[0], md5)
        # md6 = open("metaData6.p")
        # pickle.dump(self.metaLists[0], md6)
        # md7 = open("metaData7.p")
        # pickle.dump(self.metaLists[0], md7)
        # md8 = open("metaData8.p")
        # pickle.dump(self.metaLists[0], md8)
        # md9 = open("metaData9.p")
        # pickle.dump(self.metaLists[0], md9)
        # md10 = open("metaData10.p")
        # pickle.dump(self.metaLists[0], md10)

    def loadMetaData(self):

        md1 = open("metaData.p", 'rb')
        self.metaLists = pickle.load(md1)

        # md1 = open("metaData1.p")
        # pickle.dump(self.metaLists[0], md1)
        # md2 = open("metaData2.p")
        # pickle.dump(self.metaLists[1], md2)
        # md3 = open("metaData3.p")
        # pickle.dump(self.metaLists[0], md3)
        # md4 = open("metaData4.p")
        # pickle.dump(self.metaLists[0], md4)
        # md5 = open("metaData5.p")
        # pickle.dump(self.metaLists[0], md5)
        # md6 = open("metaData6.p")
        # pickle.dump(self.metaLists[0], md6)
        # md7 = open("metaData7.p")
        # pickle.dump(self.metaLists[0], md7)
        # md8 = open("metaData8.p")
        # pickle.dump(self.metaLists[0], md8)
        # md9 = open("metaData9.p")
        # pickle.dump(self.metaLists[0], md9)
        # md10 = open("metaData10.p")
        # pickle.dump(self.metaLists[0], md10)



    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == 16777235:
            # when up is hit, change mode if not already in mode 1 & play sound2
            if self.pbModel.mode == 0:
                self.pbModel.mode = 1
                self.sound2.play()
                self.enterMD.setVisible(True)
                self.saveMD.setVisible(True)

                self.mdTxbx.setVisible(True)
                self.srchTxbx.setVisible(False)
                self.srLenTxbx.setVisible(False)
                self.MaxSrchRslts.setVisible(False)

                self.pListWidg.setVisible(True)
                self.tListWidg.setVisible(True)

                self.testB.setVisible(False)
                self.saveB.setVisible(False)
                self.exitB.setVisible(False)
                self.deleteB.setVisible(False)
                self.searchB.setVisible(False)

                self.pListWidg.addItems(self.metaLists[self.pbModel.indexes[self.pbModel.index]])
                # then resize label
                self.labels[self.pbModel.index].resize(self.bigLabSiz, self.bigLabSiz)
                self.labels[self.pbModel.index].move(int(self.wid*0.25), int(self.wid*0.03125))
                # resize all other labels to be invisible
                i = self.pbModel.index + 1
                while True:
                    if i == 5:
                        i = 0
                    if i == self.pbModel.index:
                        break
                    self.labels[i].resize(0, 0)
                    i += 1

                self.labels[self.pbModel.index]\
                    .setPixmap(self.pbModel.pixmaps[self.pbModel.indexes[self.pbModel.index]]
                               .scaled(self.labels[self.pbModel.index]
                                       .size(), Qt.KeepAspectRatio))

        if event.key() == 16777237:

            # when down is hit, toggle mode back to normal if not already & play sound1
            if self.pbModel.mode == 1:
                self.pbModel.mode = 0
                self.sound1.play()
                self.saveMD.setVisible(False)
                self.enterMD.setVisible(False)
                self.srLenTxbx.setVisible(True)
                self.MaxSrchRslts.setVisible(True)

                self.mdTxbx.setVisible(False)
                self.srchTxbx.setVisible(True)

                self.pListWidg.setVisible(False)
                self.tListWidg.setVisible(False)

                self.testB.setVisible(True)
                self.saveB.setVisible(True)
                self.exitB.setVisible(True)
                self.deleteB.setVisible(True)
                self.searchB.setVisible(True)

                self.pListWidg.clear()
                self.tListWidg.clear()

                spacingNum = int(self.wid*0.03125)

                # Reset the size and positions of all the labels,
                # using code copied from initUI
                for i in range(0, 5, 1):
                    self.labels[i].resize(self.labSiz, self.labSiz)
                    self.labels[i].move(spacingNum, self.ySpace)
                    self.labels[i].setStyleSheet("border: 10px solid purple")
                    spacingNum += self.labSiz+2
            self.labels[self.pbModel.index].setStyleSheet("border: 10px solid orange")

            # Reset the size of all the pixmaps back to normal
            for i in range(0, 5, 1):
                self.pbModel.pixmaps[self.pbModel.indexes[i]] = \
                    self.pbModel.pixmaps[self.pbModel.indexes[i]]\
                        .scaled(self.labels[i].size(), Qt.KeepAspectRatio)

                self.labels[i].setPixmap(self.pbModel.pixmaps[self.pbModel.indexes[i]])

        if event.key() == 16777234:

            # in zoomed mode, just change the pixmap you're currently viewing & play sound
            # IMO it's not a big deal, but this shifts the entire order in regular mode as well
            if self.pbModel.mode == 1:
                self.sound1.play()
                for i in range(0, 5, 1):
                    self.pbModel.indexes[i] -= 1
                    if self.pbModel.indexes[i] == -1:
                        self.pbModel.indexes[i] = 9

                for i in range(0, 5, 1):
                    self.labels[i].setPixmap \
                        (self.pbModel.pixmaps[self.pbModel.indexes[i]]
                         .scaled(self.labels[i].size(), Qt.KeepAspectRatio))

                self.pListWidg.clear()
                self.pListWidg.addItems(self.metaLists[self.pbModel.indexes[self.pbModel.index]])

            # in regular mode, however, wait until you're at the edge, and then change them all by five
            if self.pbModel.mode == 0:
                tmp = self.pbModel.index
                self.pbModel.index -= 1
                if self.pbModel.index!= -1:
                    self.sound1.play()


                # if you reach the left end, wrap around, and
                if self.pbModel.index == -1:
                    self.pbModel.index = 4
                    self.sound2.play()

                    # decrement the pixmap indexes by five
                    for i in range (0, 5, 1):
                        for i in range (0, 5, 1):
                            self.pbModel.indexes[i]-=1
                            if self.pbModel.indexes[i]==-1:
                                self.pbModel.indexes[i]=9

                    # reset all the pixmaps and make sure they're scaled
                    for i in range (0, 5, 1):
                        self.labels[i].setPixmap\
                            (self.pbModel.pixmaps[self.pbModel.indexes[i]]
                             .scaled(self.labels[i].size(), Qt.KeepAspectRatio))
                self.selectionMorpher(tmp)

        if event.key() == 16777236:

            # zoomed mode, just increment by one, & play sound
            if self.pbModel.mode == 1:
                self.sound1.play()
                for i in range(0, 5, 1):
                    self.pbModel.indexes[i] += 1
                    if self.pbModel.indexes[i] == 10:
                        self.pbModel.indexes[i] = 0

                for i in range(0, 5, 1):
                    self.labels[i].setPixmap \
                        (self.pbModel.pixmaps[self.pbModel.indexes[i]]
                         .scaled(self.labels[i].size(), Qt.KeepAspectRatio))

                self.pListWidg.clear()
                self.pListWidg.addItems(self.metaLists[self.pbModel.indexes[self.pbModel.index]])

            # regular mode, increment by one & play sound 1
            if self.pbModel.mode == 0:
                tmp = self.pbModel.index
                self.pbModel.index += 1
                if self.pbModel.index!=5:
                    self.sound1.play()
                # if you reach right end, wrap around, play sound2, and
                if self.pbModel.index == 5:
                    self.pbModel.index = 0
                    self.sound2.play()
                    # increment the pixmap indexes by five
                    for i in range (0, 5, 1):
                        for i in range (0, 5, 1):
                            self.pbModel.indexes[i]+=1
                            if self.pbModel.indexes[i]==10:
                                self.pbModel.indexes[i]=0
                    # reset all the pixmaps and make sure they're scaled
                    for i in range (0, 5, 1):
                        self.labels[i].setPixmap\
                            (self.pbModel.pixmaps[self.pbModel.indexes[i]]
                             .scaled(self.labels[i].size(), Qt.KeepAspectRatio))
                self.selectionMorpher(tmp)

        if event.key()==44:
            # if carrot left is hit, decrement the pixmap indexes by five
            self.sound2.play()
            for i in range(0, 5, 1):
                for i in range(0, 5, 1):
                    self.pbModel.indexes[i] -= 1
                    if self.pbModel.indexes[i] == -1:
                        self.pbModel.indexes[i] = 9

            if self.pbModel.mode==1:
                self.pListWidg.clear()
                self.pListWidg.addItems(self.metaLists[self.pbModel.indexes[self.pbModel.index]])

            # reset all the pixmaps and make sure they're scaled
            for i in range(0, 5, 1):
                self.labels[i].setPixmap \
                    (self.pbModel.pixmaps[self.pbModel.indexes[i]]
                     .scaled(self.labels[i].size(), Qt.KeepAspectRatio))


        if event.key()==46:
            # if carrot right is hit, decrement the pixmap indexes by five
            self.sound2.play()
            for i in range(0, 5, 1):
                for i in range(0, 5, 1):
                    self.pbModel.indexes[i] -= 1
                    if self.pbModel.indexes[i] == -1:
                        self.pbModel.indexes[i] = 9

            if self.pbModel.mode == 1:
                self.pListWidg.clear()
                self.pListWidg.addItems(self.metaLists[self.pbModel.indexes[self.pbModel.index]])

            # reset all the pixmaps and make sure they're scaled
            for i in range(0, 5, 1):
                self.labels[i].setPixmap \
                    (self.pbModel.pixmaps[self.pbModel.indexes[i]]
                     .scaled(self.labels[i].size(), Qt.KeepAspectRatio))



class buttons(QPushButton):
    def __init__(self, pbM):
        super().__init__()





if __name__ == '__main__':

    app = QApplication(sys.argv)
    myView = pbView(PhotoBrowserModel.pbModel())

    # Set initial pixmaps to labels
    for i in range(0, 5, 1):
        myView.pbModel.pixmaps[i] = myView.pbModel.pixmaps[i].scaled(myView.labels[i].size(), Qt.KeepAspectRatio)
        myView.labels[i].setPixmap(myView.pbModel.pixmaps[i])

    sys.exit(app.exec_())