import maya.cmds as cmds
import maya.mel as mel
from PySide2 import QtWidgets,QtCore,QtGui
from PySide2.QtCore import Qt

class assetManager_RightClickTreeWidget(QtWidgets.QTreeWidget):
    classDict = {}
    def __init__(self, parent=None):
        super(assetManager_RightClickTreeWidget, self).__init__(parent)
        self.pathList = getAssetManagerPath()
        self.initPath = self.pathList['main']
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.setSelectionMode(self.ExtendedSelection)

    def setNodeDict(self,dict):
        self.classDict = dict

    def showContextMenu(self, pos):
        iconPath = self.pathList['icon']

        self.contextMenu = QtWidgets.QMenu(self)
        self.contextMenu.setStyleSheet(Mstyle.QMenu())

        if self.currentItem().parent():
            actionA = self.contextMenu.addAction(QtGui.QIcon(iconPath + "\\brush.png"), u'rename')
            actionA.triggered.connect(self.actionAFn)
            actionB = self.contextMenu.addAction(QtGui.QIcon(iconPath + "\\search.png"), u'sel_shader')
            actionB.triggered.connect(self.actionBFn)

        self.contextMenu.exec_(QtGui.QCursor.pos())  # show menu on cursor pos

    def checkName(self,Name):
        ans = [False,'']
        tag = ['dif','spc','bmp','nor','dis','sss','gls','msk','trs','met','ros','trns','refle','refra','opa']
        spName = Name.split('.')
        fileName = ''
        if len(spName)>2:
            ans[1] = 'too many "." in '+fileName
            return ans
        elif len(spName)<2:
            ans[1] = 'no picture type in '+fileName
            return ans
        else:
            if spName[-1].lower() in ['jpg','png','exr']:
                fileName = spName[0]
            else:
                ans[1] = 'file type error,it must be .jpg or .png or .exr'
                return ans

        spFile = fileName.split('_')
        if len(spFile) > 3:
            ans[1] = 'too many "_" in ' + fileName + '\nTip : [chaName]_[partName]_[tag]'
        elif len(spFile) < 3:
            ans[1] = 'name length not enough.\nTip : [chaName]_[partName]_[tag]'
        elif len(spFile) == 3:
            if spFile[-1] in tag:
                ans[0] = True
                ans[1] = 'pass'
            else:
                ans[1] = 'tag name <' + spFile[-1] + '> not legal.\n Tip : dif,spc,bmp,nor,dis,sss,gls,msk,trs\nmet,ros,trns,refle,refra,opa'
        return ans

    def actionAFn(self):
        ans = [False,'please input name']
        name = ''
        while not ans[0]:
            inputDialog = QtWidgets.QInputDialog()

            inputDialog.setWindowFlags(Qt.WindowStaysOnTopHint)
            name,ok = inputDialog.getText(self,"inputName",ans[1],
                                           QtWidgets.QLineEdit.Normal,'chaname_partname_tag')
            if ok and (len(name)!=0):
                ans = self.checkName(name)

            else:
                ans = [True,'skip']
        if name:
            crrItm = self.currentItem()
            crrTxt = crrItm.text(0)
            #typeName = crrTxt.split('.')[-1]
            curTt = crrItm.toolTip(0)
            curNd = self.classDict[curTt]
            baseDir = os.path.dirname(curTt)
            newPath = baseDir+'\\'+name

            crrItm.setText(0,name)
            crrItm.setToolTip(0,newPath)
            listDir = os.listdir(baseDir)
            if crrTxt in listDir:
                os.rename(curTt,newPath)
            else:
                print 'file not exists'
            cmds.setAttr(curNd+'.fileTextureName',newPath,type='string')
        else:
            print 'cancel'

    def actionBFn(self):
        crrItm = self.currentItem()
        crrTxt = crrItm.text(1)
        print crrTxt
        cmds.select(cl=1)
        cmds.select(crrTxt)


class assetManager_shaderCheckList(QtWidgets.QMainWindow):
    UITitle = 'writerReaderUI'
    x = 400
    y = 750
    textWin = ''
    mian = ''
    continueSignal = QtCore.Signal(list)

    def __init__(self, parent=None):
        # ------Style Set----------------------------

        super(assetManager_shaderCheckList, self).__init__(parent)
        self.m_DragPosition = self.pos()
        self.resize(self.x, self.y)
        self.move(402, 200)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setWindowTitle(self.UITitle)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setStyleSheet('QWidget:{background:rgb(68,68,68);}')
        self.CreateUI()
        #self.sortByPath()
        self.sortByName()

    def CreateUI(self):
        self.mian = QtWidgets.QWidget(self)
        self.mian.resize(self.x, self.y)
        self.mian.setAttribute(Qt.WA_StyledBackground)
        self.mian.setStyleSheet('QWidget{background:rgb(68, 68, 68);border-radius: 12px}')
        # close Btn Set
        Vbox = QtWidgets.QVBoxLayout()

        Xbtn = QtWidgets.QPushButton('x')
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())
        Xbtn.clicked.connect(self.Cl_Ui)

        listBtn = QtWidgets.QPushButton('name')
        listBtn.setFixedHeight(28)
        listBtn.setFixedWidth(88)
        listBtn.setStyleSheet(Mstyle.QPushButton(kw='radiobutton'))

        pathBtn = QtWidgets.QPushButton('path')
        pathBtn.setFixedHeight(28)
        pathBtn.setFixedWidth(88)
        pathBtn.setStyleSheet(Mstyle.QPushButton(kw='radiobutton'))

        self.btnGrp = QtWidgets.QButtonGroup(self)
        self.btnGrp.addButton(listBtn,0)
        self.btnGrp.addButton(pathBtn,1)

        Hbox = QtWidgets.QHBoxLayout()
        Hbox.addWidget(Xbtn)
        Hbox.addStretch(1)
        Hbox.addWidget(listBtn)
        Hbox.addWidget(pathBtn)
        Vbox.addLayout(Hbox)

        self.textWin = assetManager_RightClickTreeWidget(self.mian)
        self.textWin.setHeaderLabels(['name','infomation'])
        self.textWin.setColumnWidth(0, 270)
        self.textWin.setStyleSheet(Mstyle.QTreeWidget(kw='b') + Mstyle.QScrollBar())
        Vbox.addWidget(self.textWin)
        self.mian.setLayout(Vbox)


        btHbox = QtWidgets.QHBoxLayout()
        btnCon = QtWidgets.QPushButton()
        btnCon.setStyleSheet(Mstyle.QPushButton(kw='on'))
        btnCon.setFixedWidth(125)
        btnCon.setFixedHeight(25)
        btnCon.setText('continue')

        btHbox.addStretch(1)
        btHbox.addWidget(btnCon)
        Vbox.addLayout(btHbox)

        self.btnGrp.buttonClicked[int].connect(self.changeList)
        btnCon.pressed.connect(self.continueFn)
    # ------------define swtich--------------------

    def addFn(self):

        inputDialog = QtWidgets.QInputDialog()

        inputDialog.setWindowFlags(Qt.WindowStaysOnTopHint)
        name,ok = inputDialog.getText(self,"inputName",'type in new charactor name',
                                       QtWidgets.QLineEdit.Normal,'')
        if ok:
            findID = self.chaSel.findText(name)
            if findID<0:
                self.chaSel.addItem(name)
                count = self.chaSel.count()-1
                self.chaSel.setCurrentIndex(count)

            else:
                self.chaSel.setCurrentIndex(findID)

        else:
            print False

    def continueFn(self):
        notPass = False
        count = self.textWin.topLevelItemCount()
        for c in range(count):
            ti = self.textWin.topLevelItem(c)
            if ti.text(0) == 'wrongNamed':
                self.textWin.expandItem(ti)
                notPass = True
            else:
                self.textWin.collapseItem(ti)

        if notPass:
            return False
        else:
            nodeList = self.getTextureInFile()
            self.continueSignal.emit(nodeList)
            self.Cl_Ui()

    def changeList(self,ID):
        self.textWin.clear()
        if ID == 1:
            self.sortByPath()
        elif ID == 0:
            self.sortByName()

    def getTextureInFile(self,rtnDict=False,sort=True):
        fileNodes = cmds.ls(type='file')
        if rtnDict:
            pathDict = {}
            for i in fileNodes:
                filePath = cmds.getAttr(i+'.fileTextureName')
                if sort:
                    pathDict.update({filePath: i})
                else:
                    pathDict.update({i: filePath})
            return pathDict
        else:
            pathArray = []
            for i in fileNodes:
                filePath = cmds.getAttr(i+'.fileTextureName')
                pathArray.append(filePath)
            return pathArray

    def sortByPath(self):
        fileArray = self.getTextureInFile(rtnDict=True,sort=False)
        tipDict = {}
        dict = {}
        for (d, fa) in fileArray.items():
            # for fa in fileArray.keys():
            dirPath = os.path.dirname(fa)
            dirname = os.path.basename(fa)
            tipDict.update({dirname:fa})
            if dirPath in dict.keys():
                dict[dirPath].append([dirname, d, fa])
            else:
                dict.update({dirPath:[[dirname, d, fa]]})

        self.addItmInQTreeWidget(dict, tip=tipDict)

    def sortByName(self):
        fileArray = self.getTextureInFile(rtnDict=True, sort=False)
        tipDict = {}
        dict = {}
        for (d, fa) in fileArray.items():
            dirname = os.path.basename(fa)
            tipDict.update({dirname: fa})
            ans = self.textWin.checkName(dirname)
            if ans[0]:
                spname = dirname.split('_')
                Pname = '_'.join(spname[:-1])
                if Pname in dict.keys():
                    dict[Pname].append([dirname, d, fa])
                else:
                    dict.update({Pname: [[dirname, d, fa]]})
            else:
                if 'wrongNamed' in dict.keys():
                    dict['wrongNamed'].append([dirname, d, fa])
                else:
                    dict.update({'wrongNamed': [[dirname, d, fa]]})
        self.addItmInQTreeWidget(dict, tip=tipDict)

    def addItmInQTreeWidget(self, dict, tip={}):
        for i in dict.keys():
            topItm = QtWidgets.QTreeWidgetItem()

            topItm.setText(0, i)
            if i in tip.keys():
                topItm.setToolTip(0, tip[i])

            strLen = str(len(dict[i]))
            topItm.setText(1, strLen)
            for t in dict[i]:
                subItm = QtWidgets.QTreeWidgetItem()
                subItm.setText(0, t[0])
                if t[0] in tip.keys():
                    subItm.setToolTip(0, t[2])

                    nameCheck = self.textWin.checkName(t[0])[0]
                    if nameCheck:
                        subItm.setTextColor(0, QtGui.QColor(75,220,80))
                    else:
                        subItm.setTextColor(0, QtGui.QColor(220,220,80))

                    realFilePath = os.path.dirname(tip[t[0]])
                    if os.path.exists(realFilePath):
                        lsDir = os.listdir(realFilePath)
                        if not(t[0] in lsDir):
                            subItm.setTextColor(0, QtGui.QColor(220,75,80))
                    else:
                        subItm.setTextColor(0, QtGui.QColor(220, 75, 80))
                    subItm.setText(1, t[1])

                topItm.addChild(subItm)
            self.textWin.addTopLevelItem(topItm)
            topItm.setExpanded(True)
        self.textWin.setNodeDict(self.getTextureInFile(rtnDict = True))

    def Op_Ui(self):
        self.move(0,0)
        self.show()

    def Cl_Ui(self):
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

    def resizeEvent(self, event):
        self.mian.resize(self.width(), self.height())
        # self.textWin.resize(self.width(), self.height()-25)

#mopImportRT=assetManager_shaderCheckList()
#mopImportRT.Op_Ui()
# cleanUIRT.Cl_Ui()