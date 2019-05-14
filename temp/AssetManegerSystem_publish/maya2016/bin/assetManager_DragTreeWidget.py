from PySide import QtGui, QtCore
from PySide.QtCore import Qt


class waitingBar(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.resize(300, 50)
        self.setWindowTitle('Waiting')
        self.move(810, 490)
        self.show()

    def setText(self, message):
        self.setWindowTitle(message)


class assetManager_DragTreeWidget(QtGui.QTreeWidget):
    onPress = False
    iArray = []
    RigPath = ''
    localPath = ''
    radGrp = ''
    actionpressed = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(assetManager_DragTreeWidget, self).__init__(parent)
        self.pathList = getAssetManagerPath()
        self.initPath = self.pathList['main']
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.setSelectionMode(self.ExtendedSelection)

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

        super(assetManager_DragTreeWidget, self).wheelEvent(e)

    def mouseMoveEvent(self, e):
        if e.buttons() != QtCore.Qt.LeftButton:
            return

        if not self.isDrag:
            return
        cNode = self.currentItem()
        path = cNode.filePath
        mimeData = QtCore.QMimeData()
        url = QtCore.QUrl.fromLocalFile(QtCore.QFileInfo(path).absoluteFilePath())
        mimeData.setUrls([url])
        self.dragStruct = QtGui.QDrag(self)
        self.dragStruct.setMimeData(mimeData)
        self.dragStruct.setHotSpot(e.pos() - self.rect().topLeft())
        self.dragStruct.exec_(Qt.CopyAction)
        e.accept()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Control:
            self.onPress = True

    def keyReleaseEvent(self, e):
        self.onPress = False
        self.isDrag = False

    def mouseDoubleClickEvent(self, e):
        cNode = self.currentItem()
        self.setItemExpanded(cNode, True)
        e.accept()

    def showContextMenu(self, pos):
        iconPath = self.pathList['icon']

        self.contextMenu = QtGui.QMenu(self)
        self.contextMenu.setStyleSheet(Mstyle.QMenu())

        if self.currentItem().parent():
            actionA = self.contextMenu.addAction(QtGui.QIcon(iconPath + "drag.png"), u'refrence')
            actionA.triggered.connect(self.actionAFn)
            actionB = self.contextMenu.addAction(QtGui.QIcon(iconPath + "floder.png"), u'open')
            actionB.triggered.connect(self.actionBFn)

        actionC = self.contextMenu.addAction(QtGui.QIcon(iconPath + "CommboBoxArrow.png"), u'dowload')
        actionC.triggered.connect(self.actionCFn)

        self.contextMenu.exec_(QtGui.QCursor.pos())  # show menu on cursor pos

    def actionAFn(self):
        cNode = self.selectedItems()
        pathArray = []
        if len(cNode) > 1:
            tempArray = []
            tails = ''
            for i in cNode:
                if i.parent():
                    itm = i.text(0)
                    tails = tails + itm + '\n'
                    tempArray.append(i.parent().text(0) + '\\' + itm)

            msg = '{} files selected\nDo you wanna refrence them all?\n\n'.format(str(len(tempArray))) + tails

            ans = cmds.confirmDialog(title='confirm', m=msg, b=['yes', 'no'], cancelButton='no', defaultButton='no')
            if ans == 'yes':
                pathArray = tempArray
        else:
            if cNode[0].parent():
                pathArray.append(cNode[0].parent().text(0) + '\\' + cNode[0].text(0))
        if pathArray:
            for p in pathArray:
                sp = p.split('\\')
                pagename = ''
                checkID = self.radGrp.checkedId()
                if checkID == 0:
                    pagename = 'Char'
                if checkID == 1:
                    pagename = 'Prop'
                if checkID == 2:
                    pagename = 'Env'
                cmds.file(self.RigPath + '\\' + pagename + '\\' + p, reference=True, type='mayaAscii', namespace=sp[0])
        else:
            cmds.confirmDialog(m='no useful data was selected')
        self.actionpressed.emit('A')

    def actionBFn(self):
        cArray = self.selectedItems()
        if len(cArray) != 1:
            cmds.confirmDialog('need sel only 1 item')
        else:
            tipsWin = waitingBar()
            time.sleep(1)
            strTime = time.strftime("%Y_%m_%d %H_%M_%S ", time.localtime(time.time()))
            ci = cArray[0]
            if ci.parent():
                pagename = ''
                checkID = self.radGrp.checkedId()
                if checkID == 0:
                    pagename = 'Char'
                if checkID == 1:
                    pagename = 'Prop'
                if checkID == 2:
                    pagename = 'Env'
                cPath = self.RigPath + '\\' + pagename + '\\' + ci.parent().text(0) + '\\' + ci.text(0)
                Lpath = self.localPath + '\\' + pagename + '\\' + ci.parent().text(0) + '\\'
                if not (os.path.exists(Lpath)):
                    os.makedirs(Lpath)
                Lpath += strTime
                Lpath += ci.text(0)
                tipsWin.setText('copy file...')
                shutil.copyfile(cPath, Lpath)
                shutil.copystat(cPath, Lpath)
                tipsWin.setText('open file...')

                cmds.file(f=1, new=1)
                try:
                    cmds.file(Lpath, open=1, f=1)
                except:
                    pass
                self.actionpressed.emit('B')

    def actionCFn(self):
        cArray = self.selectedItems()
        if len(cArray) != 1:
            cmds.confirmDialog('need sel only 1 item')
        else:
            tipsWin = waitingBar()
            time.sleep(1)
            strTime = time.strftime("%Y_%m_%d %H_%M_%S ", time.localtime(time.time()))
            ci = cArray[0]
            if ci.parent():
                pagename = ''
                checkID = self.radGrp.checkedId()
                if checkID == 0:
                    pagename = 'Char'
                if checkID == 1:
                    pagename = 'Prop'
                if checkID == 2:
                    pagename = 'Env'
                cPath = self.RigPath + '\\' + pagename + '\\' + ci.parent().text(0) + '\\' + ci.text(0)
                Lpath = self.localPath + '\\' + pagename + '\\' + ci.parent().text(0) + '\\'
                if not (os.path.exists(Lpath)):
                    os.makedirs(Lpath)
                Lpath += strTime
                Lpath += ci.text(0)
                tipsWin.setText('copy file...')
                shutil.copyfile(cPath, Lpath)
                shutil.copystat(cPath, Lpath)
                tipsWin.setText('downloading file...')

        self.actionpressed.emit('C')

