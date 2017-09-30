import sys
import Model
import View

class Control(View.Display):
    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == 16777235:
            # when up is hit, change mode if not already in mode 1 & play sound2
            if View.Display.mode == 0:
                View.Display.mode = 1
                View.Display.sound2.play()
                # then resize label
                View.Display.labels[View.Display.index].resize(800, 800)
                View.Display.labels[View.Display.index].move(400, 50)
                # resize all other labels to be invisible
                i = View.Display.index + 1
                while True:
                    if i == 5:
                        i = 0
                    if i == View.Display.index:
                        break
                        View.Display.labels[i].resize(0, 0)
                    i += 1

                    View.Display.labels[View.Display.index] \
                    .setPixmap(View.Display.pixmaps[View.Display.indexes[View.Display.index]]
                               .scaled(View.Display.labels[View.Display.index]
                                       .size(), Qt.KeepAspectRatio))

        if event.key() == 16777237:

            # when down is hit, toggle mode back to normal if not already & play sound1
            if View.Display.mode == 1:
                View.Display.mode = 0
                View.Display.sound1.play()

                spacingNum = 50

                # Reset the size and positions of all the labels,
                # using code copied from initUI
                for i in range(0, 5, 1):
                    View.Display.labels[i].resize(300, 300)
                    View.Display.labels[i].move(spacingNum, 150)
                    View.Display.labels[i].setStyleSheet("border: 10px solid purple")
                    spacingNum += 302
            View.Display.labels[View.Display.index].setStyleSheet("border: 10px solid orange")

            # Reset the size of all the pixmaps back to normal
            for i in range(0, 5, 1):
                View.Display.pixmaps[View.Display.indexes[i]] = \
                    View.Display.pixmaps[View.Display.indexes[i]] \
                        .scaled(View.Display.labels[i].size(), Qt.KeepAspectRatio)

                View.Display.labels[i].setPixmap(View.Display.pixmaps[View.Display.indexes[i]])

        if event.key() == 16777234:

            # in zoomed mode, just change the pixmap you're currently viewing & play sound
            # IMO it's not a big deal, but this shifts the entire order in regular mode as well
            if View.Display.mode == 1:
                View.Display.sound1.play()
                for i in range(0, 5, 1):
                    View.Display.indexes[i] -= 1
                    if View.Display.indexes[i] == -1:
                        View.Display.indexes[i] = 9

                for i in range(0, 5, 1):
                    View.Display.labels[i].setPixmap \
                        (View.Display.pixmaps[View.Display.indexes[i]]
                         .scaled(View.Display.labels[i].size(), Qt.KeepAspectRatio))

            # in regular mode, however, wait until you're at the edge, and then change them all by five
            if View.Display.mode == 0:
                tmp = View.Display.index
                View.Display.index -= 1
                if View.Display.index != -1:
                    View.Display.sound1.play()

                # if you reach the left end, wrap around, and
                if View.Display.index == -1:
                    View.Display.index = 4
                    View.Display.sound2.play()

                    # decrement the pixmap indexes by five
                    for i in range(0, 5, 1):
                        for i in range(0, 5, 1):
                            View.Display.indexes[i] -= 1
                            if View.Display.indexes[i] == -1:
                                View.Display.indexes[i] = 9

                    # reset all the pixmaps and make sure they're scaled
                    for i in range(0, 5, 1):
                        View.Display.labels[i].setPixmap \
                            (View.Display.pixmaps[View.Display.indexes[i]]
                             .scaled(View.Display.labels[i].size(), Qt.KeepAspectRatio))
                View.Display.selectionMorpher(tmp)

        if event.key() == 16777236:

            # zoomed mode, just increment by one, & play sound
            View.Display.sound1.play()
            if View.Display.mode == 1:
                for i in range(0, 5, 1):
                    View.Display.indexes[i] += 1
                    if View.Display.indexes[i] == 10:
                        View.Display.indexes[i] = 0

                for i in range(0, 5, 1):
                    View.Display.labels[i].setPixmap \
                        (View.Display.pixmaps[View.Display.indexes[i]]
                         .scaled(View.Display.labels[i].size(), Qt.KeepAspectRatio))

            # regular mode, increment by one & play sound 1
            if View.Display.mode == 0:
                tmp = View.Display.index
                View.Display.index += 1
                if View.Display.index != 5:
                    View.Display.sound1.play()
                # if you reach right end, wrap around, play sound2, and
                if View.Display.index == 5:
                    View.Display.index = 0
                    View.Display.sound2.play()
                    # increment the pixmap indexes by five
                    for i in range(0, 5, 1):
                        for i in range(0, 5, 1):
                            View.Display.indexes[i] += 1
                            if View.Display.indexes[i] == 10:
                                View.Display.indexes[i] = 0
                    # reset all the pixmaps and make sure they're scaled
                    for i in range(0, 5, 1):
                        View.Display.labels[i].setPixmap \
                            (View.Display.pixmaps[View.Display.indexes[i]]
                             .scaled(View.Display.labels[i].size(), Qt.KeepAspectRatio))
                View.Display.selectionMorpher(tmp)

        if event.key() == 44:
            # if carrot left is hit, decrement the pixmap indexes by five
            View.Display.sound2.play()
            for i in range(0, 5, 1):
                for i in range(0, 5, 1):
                    View.Display.indexes[i] -= 1
                    if View.Display.indexes[i] == -1:
                        View.Display.indexes[i] = 9

            # reset all the pixmaps and make sure they're scaled
            for i in range(0, 5, 1):
                View.Display.labels[i].setPixmap \
                    (View.Display.pixmaps[View.Display.indexes[i]]
                     .scaled(View.Display.labels[i].size(), Qt.KeepAspectRatio))

        if event.key() == 46:
            # if carrot right is hit, decrement the pixmap indexes by five
            View.Display.sound2.play()
            for i in range(0, 5, 1):
                for i in range(0, 5, 1):
                    View.Display.indexes[i] -= 1
                    if View.Display.indexes[i] == -1:
                        View.Display.indexes[i] = 9

            # reset all the pixmaps and make sure they're scaled
            for i in range(0, 5, 1):
                View.Display.labels[i].setPixmap \
                    (View.Display.pixmaps[View.Display.indexes[i]]
                     .scaled(View.Display.labels[i].size(), Qt.KeepAspectRatio))