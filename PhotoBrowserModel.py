
class PhotoBrowserModel():
    def __init__(self):


        # Store pixmaps
        self.pixmaps = []
        self.selectedIndex = 0
        self.leftPixmap = 0

    def addPx(self, nP):
        self.pixmaps.append(nP)
