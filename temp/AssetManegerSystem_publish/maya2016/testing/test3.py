from PySide.QtCore import Qt, QRect

from PySide import QtGui, QtCore

class editGraphicsPixmapItem(QtGui.QGraphicsPixmapItem):

    def __init__(self, image = 'D:\\AssetManegerSystem_publish\\icon\\lifeStyle18.png', pos=[0, 0]):
        QtGui.QGraphicsPixmapItem.__init__(self)
        self.setFlags(self.ItemIsSelectable | self.ItemIsMovable)

        self.pickCheckColor = ' 0 , 255 , 0 '
        self.disableColor = '55 , 55 , 55'
        self.setPos(pos[0], pos[1])
        self.setImage(image)
        self.ItemScale = 1
        self.ItemScaleHover = 1.2
        self.hoverColor = '128 , 200 , 128 '
        self.hoverScale = 10
        self.selectedColor = '255 , 0 , 0 '

    def Image(self):
        return self.ImageFile

    def setImage(self, image):
        self.ImageFile = image
        pix = QtGui.QPixmap(self.ImageFile)
        self.setPixmap(pix)
        self.setOffset(-pix.width() / 2, -pix.height() / 2)

    def hoverEnterEvent(self, e):
        self.HoverIn = True
        self.setScale(self.ItemScaleHover)
        self.update()
        self.setCursor(Qt.PointingHandCursor)
        e.accept()

    def hoverLeaveEvent(self, e):
        self.HoverIn = False
        self.setScale(self.ItemScale)
        self.update()
        self.setCursor(Qt.ArrowCursor)
        e.accept()

    def executeCommand(self):
        cmds.select('pCube1', tgl=True)

class FlashItem(QtGui.QGraphicsItem):
    def __init__(self):
        super(FlashItem, self).__init__()
        # self.timer = QtGui.QTimer()
        self.flash = True
        # self.setFlag(self.ItemIsMovable)
        self.setFlags(self.ItemIsSelectable | self.ItemIsMovable)
        self.selectedColor = '255 , 0 , 0 '

    def boundingRect(self):
        adjust = 2
        return QtCore.QRectF(-10 - adjust, -10 - adjust, 43 + adjust, 43 + adjust)

    def paint(self, painter, option, widget):
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.darkGray)
        painter.drawEllipse(-7, -7, 40, 40)

        painter.setPen(QtGui.QPen(Qt.black, 0))
        painter.setBrush(Qt.yellow)
        painter.drawEllipse(-10, -10, 40, 40)

    def mousePressEvent(self, e):
        self.selectionPaint = True
        self.update()
        e.accept()
        QtGui.QGraphicsItem.mousePressEvent(self, e)

    def mouseReleaseEvent(self, e):
        self.executeCommand()
        e.accept()

        QtGui.QGraphicsItem.mouseReleaseEvent(self, e)

    def hoverEnterEvent(self, e):
        self.HoverIn = True
        self.setScale(1.3)
        self.update()
        self.setCursor(Qt.PointingHandCursor)
        e.accept()

    def hoverLeaveEvent(self, e):
        self.HoverIn = False
        self.setScale(1.0)
        self.update()
        self.setCursor(Qt.ArrowCursor)
        e.accept()

    def executeCommand(self):
        cmds.select('pSphere1', tgl=True)

        # def boundingRect(self):
        #    return QtCore.QRectF(self.BorderWidth(), self.BorderWidth(), self.BorderWidth(), self.BorderWidth())


class StarItem(QtGui.QGraphicsItem):
    def __init__(self):
        super(StarItem, self).__init__()
        self.fix = QtGui.QPixmap()
        self.fix.load('D:\\AssetManegerSystem_publish\\icon\\lifeStyle18.png')
        self.setFlags(self.ItemIsSelectable | self.ItemIsMovable)
        self.setAcceptHoverEvents(True)

    def boundingRect(self):
        return QtCore.QRectF(-self.fix.width() / 2, -self.fix.height() / 2, self.fix.width(), self.fix.height())

    def paint(self, painter, option, widget):
        painter.drawPixmap(self.boundingRect().topLeft(), self.fix)

    def mousePressEvent(self, e):
        self.selectionPaint = True
        self.update()
        e.accept()
        QtGui.QGraphicsItem.mousePressEvent(self, e)

    def mouseReleaseEvent(self, e):
        self.executeCommand()
        e.accept()

        QtGui.QGraphicsItem.mouseReleaseEvent(self, e)

    def hoverEnterEvent(self, e):
        self.HoverIn = True
        self.setScale(1.3)
        self.update()
        self.setCursor(Qt.PointingHandCursor)
        e.accept()

    def hoverLeaveEvent(self, e):
        self.HoverIn = False
        self.setScale(1.0)
        self.update()
        self.setCursor(Qt.ArrowCursor)
        e.accept()

    def executeCommand(self):
        cmds.select('sq02_sc04_sh0030_100f_139f_fps24', tgl=True)


class pickerScene(QtGui.QGraphicsScene):
    def __init__(self, parent=None):
        super(pickerScene, self).__init__(parent)
        self.setSceneRect(0, 0, 210, 335)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(108, 108, 108)))

        self.hoverColor = '128 , 200 , 128 '
        self.ActiveItem = []

        imageItm = editGraphicsPixmapItem(pos=[20,20])
        self.addItem(imageItm)

        shapeItm = StarItem()
        shapeItm.setPos(50, 60)
        shapeItm.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.addItem(shapeItm)

        pixmapItm = FlashItem()
        pixmapItm.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        pixmapItm.setPos(50, 100)
        self.addItem(pixmapItm)

    def resetItemColor(self):
        AllItems = self.items()
        for item in AllItems:
            print item

    def setColorToActive(self, ActiceItems):
        AllItems = self.items()
        for item in AllItems:
            print item

    def reSelectItem(self):
        self.clearSelection()
        # self.resetItemColor()
        # self.setColorToActive(self.ActiveItem)
        self.selectItem(self.ActiveItem)


class pickView(QtGui.QGraphicsView):
    def __init__(self):
        QtGui.QGraphicsView.__init__(self)
        self.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        self.setViewportUpdateMode(QtGui.QGraphicsView.BoundingRectViewportUpdate)

    def mouseReleaseEvent(self, event):
        self.scene().update()
        items = self.scene().selectedItems()
        if items:
            for i in items:
                i.executeCommand()
        else:
            cmds.select(cl=1)

        event.ignore()
        QtGui.QGraphicsView.mouseReleaseEvent(self, event)

    def mousePressEvent(self, event):
        event.ignore()
        QtGui.QGraphicsView.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.scene().update()
        QtGui.QGraphicsView.mouseMoveEvent(self, event)


PS = pickerScene()
Pview = pickView()

Pview.setScene(PS)
Pview.setStyleSheet("border:none; background:transparent;")
Pview.show()

