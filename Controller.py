from CSC690HW1PhotoBrowser import View

class Control(View.Display):
    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == 16777235:
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

                self.labels[self.index] \
                    .setPixmap(self.pixmaps[self.indexes[self.index]]
                               .scaled(self.labels[self.index]
                                       .size(), Qt.KeepAspectRatio))

        if event.key() == 16777237:

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
                    self.pixmaps[self.indexes[i]] \
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
                if self.index != -1:
                    self.sound1.play()

                # if you reach the left end, wrap around, and
                if self.index == -1:
                    self.index = 4
                    self.sound2.play()

                    # decrement the pixmap indexes by five
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
                self.selectionMorpher(tmp)

        if event.key() == 16777236:

            # zoomed mode, just increment by one, & play sound
            self.sound1.play()
            if self.mode == 1:
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
                if self.index != 5:
                    self.sound1.play()
                # if you reach right end, wrap around, play sound2, and
                if self.index == 5:
                    self.index = 0
                    self.sound2.play()
                    # increment the pixmap indexes by five
                    for i in range(0, 5, 1):
                        for i in range(0, 5, 1):
                            self.indexes[i] += 1
                            if self.indexes[i] == 10:
                                self.indexes[i] = 0
                    # reset all the pixmaps and make sure they're scaled
                    for i in range(0, 5, 1):
                        self.labels[i].setPixmap \
                            (self.pixmaps[self.indexes[i]]
                             .scaled(self.labels[i].size(), Qt.KeepAspectRatio))
                self.selectionMorpher(tmp)

        if event.key() == 44:
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

        if event.key() == 46:
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