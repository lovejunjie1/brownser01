class assetManager_commonRightClickTableWidget(QtGui.QTableWidget):
    choosed = QtCore.Signal(str)
    nowSelectionLevel = 0

    def setup(self):
        self.pathList = getAssetManagerPath()
        self.initPath = self.pathList['main']
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.setSelectionMode(self.ExtendedSelection)
        
        iconPath = self.pathList['icon']
        self.contextMenu = QtGui.QMenu(self)
        self.contextMenu.setStyleSheet(Mstyle.QMenu())
        
    def showContextMenu(self, pos):
        self.contextMenu.exec_(QtGui.QCursor.pos())  # show menu on cursor pos

    def actionAFn(self):
        sender = self.sender()
        self.choosed.emit(sender.text())


    def addButton(self,actionName,actionIcon):
        iconPath = self.pathList['icon']
        actionA = self.contextMenu.addAction(QtGui.QIcon(iconPath + '\\' + actionIcon), actionName)
        actionA.triggered.connect(self.actionAFn)