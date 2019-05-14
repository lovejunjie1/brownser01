import sys
from PySide import QtCore, QtGui
from PySide.QtCore import Qt
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin


class assetManager_RigMirrorToolRightClickTableWidget(QtGui.QTableWidget):
    choosed = QtCore.Signal(list)

    def setup(self):
        self.pathList = getAssetManagerPath()
        self.initPath = self.pathList['main']
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.setSelectionMode(self.ExtendedSelection)

    def showContextMenu(self, pos):
        iconPath = self.pathList['icon']

        self.contextMenu = QtGui.QMenu(self)
        self.contextMenu.setStyleSheet(Mstyle.QMenu())

        actionA = self.contextMenu.addAction(QtGui.QIcon(iconPath + 'save.png'), u'select driver')
        actionA.triggered.connect(self.actionAFn)
        actionB = self.contextMenu.addAction(QtGui.QIcon(iconPath + 'save.png'), u'select driven')
        actionB.triggered.connect(self.actionBFn)

        self.contextMenu.exec_(QtGui.QCursor.pos())  # show menu on cursor pos

    def actionAFn(self):
        reArray = []
        for i in self.selectedItems():
            theTxt = i.text()
            if not (theTxt.isdigit()):
                reArray.append(theTxt)
        self.choosed.emit(['driver', reArray])

    def actionBFn(self):
        reArray = []
        for i in self.selectedItems():
            theTxt = i.text()
            if not (theTxt.isdigit()):
                reArray.append(theTxt)
        self.choosed.emit(['driven', reArray])
