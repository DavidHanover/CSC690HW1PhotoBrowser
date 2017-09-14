import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image display'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 1600, 900)
        self.setStyleSheet("background-color: skyblue")

        # Create a label
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)
        self.label5 = QLabel(self)
        self.labels = [self.label1, self.label2, self.label3, self.label4, self.label5]
        spacingNum = 50
        for i in range (0, 5, 1):
            self.labels[i].resize(300, 300)
            self.labels[i].move(spacingNum, 150)
            self.labels[i].setStyleSheet("border: 10px solid purple")
            spacingNum += 302



        # load image from file
        #pixmap = QPixmap('Donut1.jpg')
        # attach image to label
        #label.setPixmap(pixmap)
        self.show()

    def keyPressEvent(self, event):
        print(event.key())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())