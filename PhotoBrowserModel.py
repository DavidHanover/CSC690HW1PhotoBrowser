
class PhotoBrowserModel():
    def __init__(self):
        # Store labels
        self.labels = []

        # Store pixmaps
        self.pixmaps = []

        #create pixmap indexes
        self.indexes = []
        for i in range(0, 5, 1):
            self.indexes.append(i)


    def addPx(self, nP):
        self.pixmaps.append(nP)

    def addLb(self, nL):
        self.labels.append(nL)