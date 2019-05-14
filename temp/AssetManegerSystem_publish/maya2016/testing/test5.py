import sys
from PySide.QtGui import (QPainter, QPen, QWidget)
from PySide.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.resize(400, 300)
        self.move(100, 100)
        self.setWindowTitle("draw board 4.0")

        self.setMouseTracking(False)

        self.pos_xy = []

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)

        if len(self.pos_xy) > 1:
            point_start = self.pos_xy[0]
            for pos_tmp in self.pos_xy:
                point_end = pos_tmp

                if point_end == (-1, -1):
                    point_start = (-1, -1)
                    continue
                if point_start == (-1, -1):
                    point_start = point_end
                    continue

                painter.drawLine(point_start[0], point_start[1], point_end[0], point_end[1])
                point_start = point_end
        painter.end()

    def mouseMoveEvent(self, event):
        pos_tmp = (event.pos().x(), event.pos().y())
        self.pos_xy.append(pos_tmp)

        self.update()

    def mouseReleaseEvent(self, event):

        pos_test = (-1, -1)
        self.pos_xy.append(pos_test)

        self.update()


if __name__ == "__main__":
    pyqt_learn = Example()
    pyqt_learn.show()