from PyQt5.QtGui import QPixmap
import requests

class pbModel():
    def __init__(self):
        super().__init__()
        self.index = 0
        self.mode = 0
        self.numPixmaps = 10;
        self.locations = ["Donut1.jpg", "Donut2.jpg", "Donut3.jpg",
                          "Donut4.jpg", "Donut5.jpg", "Donut6.jpg",
                          "Donut7.jpg", "Donut8.jpg", "Donut9.jpg",
                          "Donut10.jpg"]

        # Create pixmaps   CHANGE DONUT NAMES IF YOU WISH TO SUBSTITUTE TEST PICTURES
        self.pixmap1 = QPixmap(self.locations[0])
        self.pixmap2 = QPixmap(self.locations[1])
        self.pixmap3 = QPixmap(self.locations[2])
        self.pixmap4 = QPixmap(self.locations[3])
        self.pixmap5 = QPixmap(self.locations[4])
        self.pixmap6 = QPixmap(self.locations[5])
        self.pixmap7 = QPixmap(self.locations[6])
        self.pixmap8 = QPixmap(self.locations[7])
        self.pixmap9 = QPixmap(self.locations[8])
        self.pixmap10 = QPixmap(self.locations[9])

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