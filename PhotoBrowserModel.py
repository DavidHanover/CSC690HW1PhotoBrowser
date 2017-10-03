from PyQt5.QtGui import QPixmap

class pbModel():
    def __init__(self):
        super().__init__()
        self.index = 0
        self.mode = 0

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