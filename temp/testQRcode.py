from PyQt4 import QtGui, QtCore 
import qrcode 

class Image(qrcode.image.base.BaseImage): 
    def __init__(self, border, width, box_size): 
     self.border = border 
     self.width = width 
     self.box_size = box_size 
     size = (width + border * 2) * box_size 
     self._image = QtGui.QImage(
      size, size, QtGui.QImage.Format_RGB16) 
     self._image.fill(QtCore.Qt.white) 

    def pixmap(self): 
     return QtGui.QPixmap.fromImage(self._image) 

    def drawrect(self, row, col): 
     painter = QtGui.QPainter(self._image) 
     painter.fillRect(
      (col + self.border) * self.box_size, 
      (row + self.border) * self.box_size, 
      self.box_size, self.box_size, 
      QtCore.Qt.black) 

    def save(self, stream, kind=None): 
     pass 


if __name__ == '__main__': 

    qrcode.make(text, image_factory=Image).pixmap()