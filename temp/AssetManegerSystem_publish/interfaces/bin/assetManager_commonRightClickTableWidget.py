from Qt import QtWidgets as qw,QtGui,QtCore
from interfaces.scripts.userSetup import getAssetManagerPath

class assetManager_commonRightClickTableWidget(qw.QTableWidget):
    choosed = QtCore.Signal(str)
    nowSelectionLevel = 0

    def setup(self):
        self.pathList = getAssetManagerPath()
        self.initPath = self.pathList['main']
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.setSelectionMode(self.ExtendedSelection)
        
        iconPath = self.pathList['icon']
        self.contextMenu = qw.QMenu(self)
        self.contextMenu.setStyleSheet(Mstyle.QMenu())
        
    def showContextMenu(self, pos):
        self.contextMenu.exec_(qw.QCursor.pos())  # show menu on cursor pos

    def actionAFn(self):
        sender = self.sender()
        self.choosed.emit(sender.text())


    def addButton(self,actionName,actionIcon):
        iconPath = self.pathList['icon']
        actionA = self.contextMenu.addAction(qw.QIcon(iconPath + '\\' + actionIcon), actionName)
        actionA.triggered.connect(self.actionAFn)