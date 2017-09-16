import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image display'
        self.index = 0
        self.mode = 0
        self.initUI()

        self.selectionMorpher(0)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 1600, 900)
        self.setStyleSheet("background-color: skyblue")

        # Create labels
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.label5 = QLabel(self)

        # Store labels
        self.labels = [self.label1, self.label2, self.label3, self.label4, self.label5]

        # Loop for initializing labels
        spacingNum  = 50

        for i in range (0, 5, 1):
            self.labels[i].resize(300, 300)
            self.labels[i].move(spacingNum, 150)
            self.labels[i].setStyleSheet("border: 10px solid purple")
            spacingNum += 302

        # Create pixmaps
        pixmap1 = QPixmap("Donut1.jpg")
        pixmap2 = QPixmap("Donut2.jpg")
        pixmap3 = QPixmap("Donut3.jpg")
        pixmap4 = QPixmap("Donut4.jpg")
        pixmap5 = QPixmap("Donut5.jpg")
        pixmap6 = QPixmap("Donut6.jpg")
        pixmap7 = QPixmap("Donut7.jpg")
        pixmap8 = QPixmap("Donut8.jpg")
        pixmap9 = QPixmap("Donut9.jpg")
        pixmap10 = QPixmap("Donut10.jpg")

        # Store pixmaps
        pixmaps = [pixmap1, pixmap2, pixmap3, pixmap4, pixmap5, pixmap6, pixmap7, pixmap8, pixmap9, pixmap10]

        self.show()


    def selectionMorpher(self, prev):
        self.labels[prev].setStyleSheet("border: 10px solid purple")
        self.labels[self.index].setStyleSheet("border: 10px solid orange")

    def keyPressEvent(self, event):
        print(event.key())
        if event.key()==16777235:
            if self.mode == 0:
                self.mode = 1
                self.labels[self.index].resize(1250, 650)
                self.labels[self.index].move(100, 100)
                i = self.index + 1
                while True:
                    if i == 5:
                        i = 0
                    if i == self.index:
                        break
                    self.labels[i].resize(0, 0)
                    i += 1


        if event.key()==16777237:
            if self.mode == 1:
                self.mode = 0

                spacingNum = 50

                for i in range(0, 5, 1):
                    self.labels[i].resize(300, 300)
                    self.labels[i].move(spacingNum, 150)
                    self.labels[i].setStyleSheet("border: 10px solid purple")
                    spacingNum += 302
            self.labels[self.index].setStyleSheet("border: 10px solid orange")

        if event.key()==16777234:
            tmp = self.index
            self.index -= 1
            if self.index == -1:
                self.index = 4
            self.selectionMorpher(tmp)
        if event.key() == 16777236:
            tmp = self.index
            self.index += 1
            if self.index == 5:
                self.index = 0
            self.selectionMorpher(tmp)

        if event.key()==87:
            print(self.index)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())