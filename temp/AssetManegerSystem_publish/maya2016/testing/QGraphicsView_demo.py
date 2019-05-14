from PySide.QtCore import Qt, QRect

from PySide import QtGui, QtCore

class editGraphicsPixmapItem(QtGui.QGraphicsPixmapItem):

    def __init__(self, image = 'D:\\AssetManegerSystem_publish\\icon\\lifeStyle18.png', pos=[0, 0]):
        super(editGraphicsPixmapItem, self).__init__()
        #QtGui.QGraphicsPixmapItem.__init__(self)
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
        self.__itmName__ = ''

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

    def setName(self,data):
        self.itmName = data

    def executeCommand(self):
        if self.itmName :
            cmds.select(self.itmName, tgl=True)


class pickerScene(QtGui.QGraphicsScene):
    def __init__(self, parent=None):
        super(pickerScene, self).__init__(parent)
        self.setSceneRect(0, 0, 210, 335)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(108, 108, 108)))
        self.jobNum = 0

    def setMayaFeedBack(self, state):
        if state == True:
            self.jobNum = cmds.scriptJob(event=['SelectionChanged', self.updateItems])
        else:
            try:
                cmds.scriptJob(kill=self.jobNum)
            except:
                pass

    def updateItems(self):
        objList = ls(sl=True)
        selectionList = []

        for obj in objList:
            selectionList.append(obj)
            print obj
        '''
        allItems = self.items()
        for item in allItems:
            if item.itmName in selectionList:
                item.setToSelected(True)
        '''

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

    def closeEvent(self, event):
        try:
            self.scene().setMayaFeedBack(False)
        except:
            pass

    def MayaSelFeedBack(self, state):
        if state:
            self.scene().setMayaFeedBack(True)
        else:
            self.scene().setMayaFeedBack(False)




PS = pickerScene()
imageItm = editGraphicsPixmapItem(pos=[20,20])
imageItm.setName('pSphere1')
PS.addItem(imageItm)

shapeItm = editGraphicsPixmapItem(image = r'D:\AssetManegerSystem_publish\icon\star.png' ,pos = [50,60])
shapeItm.setName('pCube1')
PS.addItem(shapeItm)


Pview = pickView()

Pview.setScene(PS)
#Pview.MayaSelFeedBack(False)
Pview.setStyleSheet("border:none; background:transparent;")
Pview.show()

