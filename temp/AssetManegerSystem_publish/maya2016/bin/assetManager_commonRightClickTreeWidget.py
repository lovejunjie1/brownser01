class assetManager_commonRightClickTreeWidget(QtGui.QTreeWidget):
    choosed = QtCore.Signal(str)
    onPress = False
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
        self.getNowLevel()
        acts = self.contextMenu.actions()
        for a in acts:
            if str(self.nowSelectionLevel) == str(a.toolTip()):
                a.setVisible(True)
            else:
                a.setVisible(False)
        self.contextMenu.exec_(QtGui.QCursor.pos())  # show menu on cursor pos

    def actionAFn(self):
        sender = self.sender()
        self.choosed.emit(sender.text())

    def wheelEvent(self, e):
        if self.onPress:
            nowSize = self.topLevelItem(0).sizeHint(0).width()
            rollSize = nowSize + (e.delta() / 120)
            count = self.topLevelItemCount()
            for i in range(count):
                cNode = self.topLevelItem(i)
                cNode.setSizeHint(0, QtCore.QSize(rollSize, rollSize))
                cCount = cNode.childCount()
                for c in range(cCount):
                    cNode.child(c).setSizeHint(0, QtCore.QSize(rollSize, rollSize))

        else:
            e.ignore()

    def addButton(self, actionName, actionIcon, lv=0):
        iconPath = self.pathList['icon']
        actionA = self.contextMenu.addAction(QtGui.QIcon(iconPath + '\\' + actionIcon), actionName)
        actionA.setToolTip(str(lv))
        actionA.triggered.connect(self.actionAFn)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Control:
            self.onPress = True

    def mouseDoubleClickEvent(self, e):
        cNode = self.currentItem()
        self.setItemExpanded(cNode, True)
        e.accept()

    def getNowLevel(self):
        itm = self.currentItem()
        if itm:
            tempParent = itm
            self.nowSelectionLevel = 0
            for i in range(5):
                tempParent = tempParent.parent()
                if tempParent:
                    self.nowSelectionLevel += 1
                else:
                    break
