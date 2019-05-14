from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
import os, sys, time, shutil
filePath = os.path.realpath(__file__)
sys.path.append(filePath)
import script

class SplashScreen(QtGui.QSplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__(QtGui.QPixmap(script.getAssetManagerPath()['icon'] + '\\loading.png'),
                                           Qt.WindowStaysOnTopHint)  # 启动程序的图片

    def effect(self):
        self.setWindowOpacity(0)
        t = 0
        while t <= 50:
            newOpacity = self.windowOpacity() + 0.02
            if newOpacity > 1:
                break

            self.setWindowOpacity(newOpacity)
            self.show()
            t -= 1
            time.sleep(0.04)

        time.sleep(1)
        t = 0
        while t <= 50:
            newOpacity = self.windowOpacity() - 0.02  # 设置淡出
            if newOpacity < 0:
                break
            self.setWindowOpacity(newOpacity)
            t += 1
            time.sleep(0.04)


class clickLabel(QtGui.QLabel):
    def mousePressEvent(self, e):
        if (e.button() == Qt.LeftButton):
            os.startfile(str(self.toolTip()))


class dragToolListWidget(QtGui.QTreeWidget):
    onPress = False
    iArray = []
    isDrag = False
    RigPath = ''
    localPath = ''
    radGrp = ''

    def __init__(self, parent=None):
        super(dragToolListWidget, self).__init__(parent)
        self.initPath = script.getAssetManagerPath()['main']
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

        super(dragToolListWidget, self).wheelEvent(e)

    def mouseMoveEvent(self, e):
        if e.buttons() != QtCore.Qt.LeftButton:
            return
        if not self.isDrag:
            return
        cNodes = self.selectedItems()
        pathArray = []
        for c in cNodes:
            path = ''
            nodeName = c.text(0)
            if '.' in nodeName:
                path = self.RigPath + '\\' + c.parent().text(0) + '\\' + nodeName
            else:
                path = self.RigPath + '\\asset\\MODEL\\' + nodeName
            url = QtCore.QUrl.fromLocalFile(QtCore.QFileInfo(path).absoluteFilePath())
            pathArray.append(url)

        mimeData = QtCore.QMimeData()
        mimeData.setUrls(pathArray)
        self.drag = QtGui.QDrag(self)
        self.drag.setMimeData(mimeData)
        self.drag.setHotSpot(e.pos() - self.rect().topLeft())
        self.drag.exec_(Qt.CopyAction)
        e.accept()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Control:
            self.onPress = True
        if e.key() == QtCore.Qt.Key_Alt:
            self.isDrag = True

    def keyReleaseEvent(self, e):
        self.onPress = False
        self.isDrag = False

    def mouseDoubleClickEvent(self, e):
        pass
        '''
        cNode = self.currentItem()
        self.setItemExpanded(cNode, True)
        e.accept()
        '''

    def showContextMenu(self, pos):
        iconPath = self.initPath + '\\icon\\'

        self.contextMenu = QtGui.QMenu(self)
        self.contextMenu.setStyleSheet(Mstyle.QMenu())

        actionC = self.contextMenu.addAction(QtGui.QIcon(iconPath + "CommboBoxArrow.png"), u'dowload')
        actionC.triggered.connect(self.actionCFn)

        self.contextMenu.exec_(QtGui.QCursor.pos())  # show menu on cursor pos

    def actionCFn(self):
        '''
        download concept data to local path and open or edit it
        '''
        cArrays = self.selectedItems()
        for cNode in cArrays:
            if cNode.parent():
                iscopy = True
                Spath = self.RigPath + '\\' + cNode.parent().text(0) + '\\' + cNode.text(0)
                Lpath = self.localPath + '\\' + cNode.parent().text(0) + '\\' + cNode.text(0)
                Lexits = os.path.exists(self.localPath + '\\' + cNode.parent().text(0))
                if not Lexits:
                    os.makedirs(self.localPath + '\\' + cNode.parent().text(0))
                Fexits = os.path.exists(self.localPath + '\\' + cNode.parent().text(0) + '\\' + cNode.text(0))
                if Fexits:
                    quickMsg = QtGui.QMessageBox.question(self, "confirm",
                                                          cNode.parent().text(0) + '\nfile exists.do you want replace?',
                                                          QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel,
                                                          QtGui.QMessageBox.Ok)
                    if quickMsg == QtGui.QMessageBox.Cancel:
                        iscopy = False
                if iscopy:
                    shutil.copyfile(Spath, Lpath)

            else:

                Spath = self.RigPath + '\\' + cNode.text(0)
                Lpath = self.localPath + '\\' + cNode.text(0)
                Lexits = os.path.exists(Lpath)
                if Lexits:
                    quickMsg = QtGui.QMessageBox.question(self, "confirm",
                                                          cNode.parent().text(0) + '\nfile exists.do you want replace?',
                                                          QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel,
                                                          QtGui.QMessageBox.Ok)
                    if quickMsg == QtGui.QMessageBox.Ok:
                        os.system("xcopy /s /c /r /i /y %s %s" % (Spath, Lpath))
                else:
                    shutil.copytree(Spath, Lpath)



class ConceptManagerBoxUI(QtGui.QWidget , assetManager_HTML.assetManager_HTML):
    titleName = 'ConceptManagerBoxUI'
    widgetHeight = 750
    widgetWidth = 600
    initPath = ''
    UIitems = {}
    isTree = True
    isTab = True
    localPath = ''
    serverPath = ''
    nowPicPath = ''
    keepLogin = 'Login'
    localSetPath = ''
    nowTreePage = 'Char'
    readWidget = ''
    departmentName = 'CONCEPT'
    GWid = ''
    L2 = 25

    def __init__(self, *args, **kwargs):

        self.extraInit()
        self.titleName = self.departmentName + '_AssetManager_Tool'

        super(ConceptManagerBoxUI, self).__init__(*args, **kwargs)
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle(self.titleName)
        self.setMinimumWidth(self.widgetWidth)
        self.setMaximumWidth(self.widgetWidth * 3)
        self.setAcceptDrops(True)

        self.initPath = script.getAssetManagerPath()['main']
        self.iconPath = script.getAssetManagerPath()['icon']
        self.nowPicPath = self.iconPath + '\\currentPic.png'

        self.loadConfig()

        self.createTitleBar()
        self.createSplitter()

        if self.keepLogin != 'Login':
            cs = self.fileMn.children()
            for c in cs:
                if 'regist' == c.text() or 'login' == c.text():
                    c.setVisible(False)

    def extraInit(self):
        pass

    def loadConfig(self):
        pathSet = self.initPath + '\\data\\path.json'
        # print pathSet
        pathDict = self.loadJson(pathSet)
        # print pathDict
        self.localSetPath = pathDict['localSetPath'] + '\\AssetManaSys_Local\\'
        if not os.path.exists(self.localSetPath):
            os.makedirs(self.localSetPath)
        if not os.path.exists(self.localSetPath + 'localSet.json'):
            self.saveJson({}, self.localSetPath + 'localSet.json')

        localSetDict = self.loadJson(self.localSetPath + 'localSet.json')
        if 'user' in localSetDict.keys():
            self.keepLogin = localSetDict['user']

        self.projectName = ''
        if 'project' in localSetDict.keys():
            self.projectName = localSetDict['project']

        self.allProjects = pathDict.keys()
        self.allProjects.remove('localSetPath')

        if not self.projectName:
            self.projectName = self.allProjects[0]
        # print self.allProjects
        # print self.projectName

        self.localPath = pathDict[self.projectName]['local']
        self.serverPath = pathDict[self.projectName]['server']

        print 'local path load seccess'
        print self.localPath
        print 'server path load seccess'
        print self.serverPath
        # loadServerConfig
        # loadLocalConfig

    def createTitleBar(self):

        self.MainMenuBar = QtGui.QMenuBar(self)

        self.fileMn = QtGui.QMenu(self.keepLogin, self.MainMenuBar)
        self.MainMenuBar.addMenu(self.fileMn)
        fileMn1act = self.fileMn.addAction('login')
        self.fileMn2act = self.fileMn.addAction('regist')
        fileMn3act = self.fileMn.addAction('exit')

        self.fileMn.addSeparator()  # --------------------

        self.projectMn = QtGui.QMenu('project List', self.MainMenuBar)
        self.MainMenuBar.addMenu(self.projectMn)

        self.projectActionGrp = QtGui.QActionGroup(self)

        for i in self.allProjects:
            projectMn1act = self.projectMn.addAction(i)
            projectMn1act.setCheckable(True)
            self.projectActionGrp.addAction(projectMn1act)
            if i == self.projectName:
                projectMn1act.setChecked(True)

        self.projectMn.addSeparator()  # --------------------

        shMn = QtGui.QMenu('Layout', self.MainMenuBar)
        self.MainMenuBar.addMenu(shMn)
        self.shMn2act = QtGui.QAction("FileList", shMn, checkable=True)
        self.shMn2act.setChecked(True)
        shMn.addAction(self.shMn2act)
        self.shMn3act = QtGui.QAction("MoreInfo", shMn, checkable=True)
        self.shMn3act.setChecked(True)
        shMn.addAction(self.shMn3act)
        shMn.addSeparator()

        aboutMn = QtGui.QMenu('About', self.MainMenuBar)
        self.MainMenuBar.addMenu(aboutMn)
        about1act = aboutMn.addAction("about author")
        about2act = aboutMn.addAction("how to use")

        self.shMn2act.changed.connect(self.shMn2actFn)
        self.shMn3act.changed.connect(self.shMn3actFn)

        fileMn1act.triggered.connect(self.loginFn)
        self.fileMn2act.triggered.connect(self.registFn)
        fileMn3act.triggered.connect(self.exitFn)
        about1act.triggered.connect(self.authorFn)
        about2act.triggered.connect(self.howToUseFn)

        self.projectActionGrp.selected.connect(self.projectChangeFn)

    def projectChangeFn(self, theAct):
        # print theAct
        # print theAct.text()
        jsonP = self.localSetPath + 'localSet.json'
        jsonDict = self.loadJson(jsonP)
        jsonDict.update({'project': str(theAct.text())})
        self.saveJson(jsonDict, jsonP)

        ans = QtGui.QMessageBox.information(self, "project Changed",
                                            ('project changed to ' + str(theAct.text()) + '\nplease restart toolkit'),
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if QtGui.QMessageBox.Yes == ans:
            # self.deleteLater()
            self.close()
            # if ans == QtGui.QMessageBox.Yes:

    def authorFn(self):
        QtGui.QMessageBox.information(self, "Author", ('Auther: figo\nE-mail: 276415977@qq.com'),
                                      QtGui.QMessageBox.Yes, QtGui.QMessageBox.Yes)

    def howToUseFn(self):
        pass

    def createSplitter(self):

        self.splitter = QtGui.QSplitter(self)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter.setGeometry(0, self.L2, 0, 0)
        self.splitter.resize(self.widgetWidth, self.widgetWidth * 0.6)

        self.createTab()
        self.createTree()

        self.vWid.setParent(self.splitter)
        self.vWid.setVisible(self.isTree)
        self.tabWid.setParent(self.splitter)
        self.tabWid.setVisible(self.isTab)

    def createTab(self):
        self.tabWid = QtGui.QTabWidget()
        self.tabWid.setStyleSheet(Mstyle.QTabWidget())
        self.tabWid.setMinimumWidth(self.widgetWidth * 0.1)
        self.tabWid.setMinimumHeight(self.widgetWidth * 0.6)
        self.tabWid.setTabPosition(QtGui.QTabWidget.West)
        self.tabWid.setContentsMargins(0, 0, 0, 0)

        # ---page0----
        self.createGeneralTab()
        self.createCommonTab()
        self.createHistoryTab()
        self.createAcceptTab()

        self.tabWid.currentChanged.connect(self.tabWidChangedFn)

    def createGeneralTab(self):
        self.GWid = self.createGeneralPage()
        self.GWid.setAttribute(Qt.WA_StyledBackground)
        self.GWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        self.GWid.setAttribute(Qt.WA_DeleteOnClose)

        self.tabWid.addTab(self.GWid, 'general')

    def createAcceptTab(self):
        listWid = QtGui.QWidget()
        listWid.setAttribute(Qt.WA_StyledBackground)
        listWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        listWid.setAttribute(Qt.WA_DeleteOnClose)

        listVB = QtGui.QVBoxLayout()
        listVB.setContentsMargins(0, 0, 0, 0)
        listVB.setSpacing(0)

        listHbox = QtGui.QHBoxLayout()
        listHbox.setContentsMargins(0, 0, 0, 0)
        listHbox.setSpacing(0)

        listAcceptBtn = QtGui.QPushButton('accept')
        listAcceptBtn.setStyleSheet(Mstyle.QPushButton(kw='c'))
        listAcceptBtn.setToolTip('accept')
        listAcceptBtn.setFixedHeight(40)

        listEditBtn = QtGui.QPushButton('show')
        listEditBtn.setStyleSheet(Mstyle.QPushButton(kw='c'))
        listEditBtn.setToolTip('show')
        listEditBtn.setFixedHeight(40)
        listEditBtn.setEnabled(True)

        listRefuseBtn = QtGui.QPushButton('refuse')
        listRefuseBtn.setStyleSheet(Mstyle.QPushButton(kw='c'))
        listRefuseBtn.setToolTip('refuse')
        listRefuseBtn.setFixedHeight(40)

        listHbox.addWidget(listAcceptBtn)
        listHbox.addWidget(listEditBtn)
        listHbox.addWidget(listRefuseBtn)

        self.listLE = QtGui.QListWidget()
        self.listLE.verticalScrollBar().setStyleSheet(Mstyle.QScrollBar())
        self.listLE.setIconSize(QtCore.QSize(48, 48))
        self.listLE.setLayoutMode(QtGui.QListWidget.Batched)

        listLineE = QtGui.QLineEdit()
        listLineE.setText('search bar')
        listLineE.setAlignment(Qt.AlignHCenter)
        listLineE.setFixedHeight(24)
        listLineE.setStyleSheet(Mstyle.QLineEdit(fontSize='14px', bordRad='12px', kw='d', lang='c'))

        listVB.addWidget(listLineE)
        listVB.addWidget(self.listLE)
        listVB.addLayout(listHbox)
        listWid.setLayout(listVB)
        self.tabWid.addTab(listWid, 'List')

        listAcceptBtn.pressed.connect(self.acceptConceptFn)
        listRefuseBtn.pressed.connect(self.refuseConceptFn)
        listEditBtn.pressed.connect(self.showConceptFn)
        listLineE.cursorPositionChanged.connect(self.clearSreachBar)

        listLineE.textChanged.connect(self.searchListNote)

    def createHistoryTab(self):
        hisWid = QtGui.QWidget()
        hisWid.setAttribute(Qt.WA_StyledBackground)
        hisWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        hisWid.setAttribute(Qt.WA_DeleteOnClose)
        self.tabWid.addTab(hisWid, 'history')
        hisVB = QtGui.QVBoxLayout()
        hisVB.setContentsMargins(0, 0, 0, 0)
        hisVB.setSpacing(0)

        blanklabelup = QtGui.QLabel()
        blanklabelup.setFixedHeight(24)
        blanklabelbelow = QtGui.QLabel()
        blanklabelbelow.setFixedHeight(24)

        self.qweb = QWebView()
        self.qweb.setRenderHints(
            QtGui.QPainter.Antialiasing | QtGui.QPainter.HighQualityAntialiasing | QtGui.QPainter.NonCosmeticDefaultPen | QtGui.QPainter.SmoothPixmapTransform | QtGui.QPainter.TextAntialiasing)
        self.qweb.setStyleSheet('QWebView{-webkit-border-radius: 26px}')
        # self.qweb.settings().setDefaultTextEncoding('utf-8')
        self.qweb.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)

        hisVB.addWidget(blanklabelup)
        hisVB.addWidget(self.qweb)
        hisVB.addWidget(blanklabelbelow)
        hisWid.setLayout(hisVB)
        self.qweb.linkClicked.connect(self.linkFn)

    def createCommonTab(self):

        commonWid = QtGui.QWidget()
        commonWid.setAttribute(Qt.WA_StyledBackground)
        commonWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        commonWid.setAttribute(Qt.WA_DeleteOnClose)

        comVB = QtGui.QVBoxLayout()
        comVB.setContentsMargins(0, 0, 0, 0)
        comVB.setSpacing(0)

        comHbox = QtGui.QHBoxLayout()
        comHbox.setContentsMargins(0, 0, 0, 0)
        comHbox.setSpacing(0)

        comWriteBtn = QtGui.QPushButton('write')
        comWriteBtn.setStyleSheet(Mstyle.QPushButton(kw='c'))
        comWriteBtn.setToolTip('write')
        comWriteBtn.setFixedHeight(40)

        comEditBtn = QtGui.QPushButton('refresh')
        comEditBtn.setStyleSheet(Mstyle.QPushButton(kw='c'))
        comEditBtn.setToolTip('refresh')
        comEditBtn.setFixedHeight(40)
        comEditBtn.setEnabled(True)

        comReadBtn = QtGui.QPushButton('Read')
        comReadBtn.setStyleSheet(Mstyle.QPushButton(kw='c'))
        comReadBtn.setToolTip('Read')
        comReadBtn.setFixedHeight(40)

        comHbox.addWidget(comWriteBtn)
        comHbox.addWidget(comEditBtn)
        comHbox.addWidget(comReadBtn)

        self.comLE = QtGui.QListWidget()
        self.comLE.verticalScrollBar().setStyleSheet(Mstyle.QScrollBar())
        self.comLE.setIconSize(QtCore.QSize(48, 48))
        self.comLE.setLayoutMode(QtGui.QListWidget.Batched)

        comLineE = QtGui.QLineEdit()
        comLineE.setText('search bar')
        comLineE.setAlignment(Qt.AlignHCenter)
        comLineE.setFixedHeight(24)
        comLineE.setStyleSheet(Mstyle.QLineEdit(fontSize='14px', bordRad='12px', kw='d', lang='c'))

        comVB.addWidget(comLineE)
        comVB.addWidget(self.comLE)
        comVB.addLayout(comHbox)
        commonWid.setLayout(comVB)
        self.tabWid.addTab(commonWid, 'note')

        comWriteBtn.clicked.connect(self.openEidtWindow)
        comEditBtn.clicked.connect(self.loadNoteListData)
        comReadBtn.clicked.connect(self.readNote)
        comLineE.cursorPositionChanged.connect(self.clearSreachBar)
        comLineE.textChanged.connect(self.searchNote)

    def clearSreachBar(self):
        sender = self.sender()
        if sender.text() == 'search bar':
            sender.setText('')

    def searchListNote(self, theStr):
        print theStr
        itmCount = self.listLE.count()
        for i in range(itmCount):
            itmCell = self.listLE.item(i)
            if theStr.lower() in str(itmCell.text()).lower():  # .encode('utf-8')
                itmCell.setHidden(False)
                # print itmCell.text()
            else:
                itmCell.setHidden(True)

    def searchNote(self, theStr):

        itmCount = self.comLE.count()
        for i in range(itmCount):
            itmCell = self.comLE.item(i)
            if theStr.lower() in str(itmCell.text()).lower():  # .encode('utf-8')
                itmCell.setHidden(False)
            else:
                itmCell.setHidden(True)

    def readNote(self):
        filedata = ''
        noteDir = self.serverPath + '\\asset\\' + self.departmentName + '\\' + self.nowTreePage + '\\' + self.itemNode.text(
            0) + '\\note\\' + self.comLE.currentItem().toolTip()
        listdir = os.listdir(noteDir)
        for i in listdir:
            if '.writer' in i:
                with open(noteDir + '\\' + i, "rt") as file:
                    filedata = file.read().decode('utf-8')
        self.readWidget = docWriter_reader.writerReaderUI(self)
        # self.readwidget.setParent()
        self.readWidget.move(0, 0)
        self.readWidget.resize(self.width(), self.height())
        self.readWidget.setText(filedata)
        self.readWidget.show()

    def openEidtWindow(self):
        itemNode = self.nowSelMainTreeItem
        TEmain = docWriter_writter.textEditorMain()
        TEmain.itemName = itemNode.text(0)
        TEmain.savePath = self.serverPath + '\\asset\\' + self.departmentName + '\\' + self.nowTreePage + '\\' + itemNode.text(
            0) + '\\note'
        TEmain.initUI()
        TEmain.setParent(self)
        TEmain.move(0, 0)
        TEmain.resize(self.width(), self.height())
        TEmain.saveSignal.connect(self.writterSavedFn)
        TEmain.show()

    def writterSavedFn(self, data):
        print data
        self.loadNoteListData()

    def createTree(self):

        self.vWid = QtGui.QWidget()
        self.vWid.setMinimumWidth(self.widgetWidth * 0.1)
        # self.vWid.resize(self.widgetWidth * 0.5, self.widgetWidth)

        vBox = QtGui.QVBoxLayout()
        vBox.setSpacing(0)
        vBox.setContentsMargins(0, 0, 0, 0)

        radHBox = QtGui.QHBoxLayout()

        rad1 = QtGui.QPushButton('cha')
        rad1.setFixedHeight(25)
        rad1.setStyleSheet(Mstyle.QPushButton(kw='radiobutton', bordRad='6px'))
        rad1.setAutoExclusive(True)
        rad1.setCheckable(True)
        rad1.setToolTip('charactor page')
        rad1.setChecked(True)
        radHBox.addWidget(rad1)

        rad2 = QtGui.QPushButton('prop')
        rad2.setFixedHeight(25)
        rad2.setStyleSheet(Mstyle.QPushButton(kw='radiobutton', bordRad='6px'))
        rad2.setAutoExclusive(True)
        rad2.setCheckable(True)
        rad2.setToolTip('prop page')
        radHBox.addWidget(rad2)

        rad3 = QtGui.QPushButton('env')
        rad3.setFixedHeight(25)
        rad3.setStyleSheet(Mstyle.QPushButton(kw='radiobutton', bordRad='6px'))
        rad3.setAutoExclusive(True)
        rad3.setCheckable(True)
        rad3.setToolTip('everioment page')
        radHBox.addWidget(rad3)

        self.radGrp = QtGui.QButtonGroup()
        self.radGrp.setExclusive(True)
        self.radGrp.addButton(rad1, 0)
        self.radGrp.addButton(rad2, 1)
        self.radGrp.addButton(rad3, 2)

        LE = QtGui.QLineEdit()
        LE.setAlignment(Qt.AlignHCenter)
        LE.setStyleSheet(Mstyle.QLineEdit(kw='d', lang='c'))

        self.treeWid = dragToolListWidget()
        self.treeWid.verticalScrollBar().setStyleSheet(Mstyle.QScrollBar())
        self.treeWid.setStyleSheet(Mstyle.QTreeWidget())
        self.treeWid.RigPath = self.serverPath + '\\asset\\' + self.departmentName
        self.treeWid.localPath = self.localPath + '\\asset\\' + self.departmentName
        self.treeWid.setHeaderHidden(1)
        self.treeWid.radGrp = self.radGrp

        self.createTreeList()

        projectLabel = QtGui.QLabel()
        projectLabel.setText(self.projectName)
        projectLabel.setStyleSheet(Mstyle.QLabel(fontSize='32px') + 'QLabel {color:rgb(20,20,20)}')
        projectLabel.setFixedHeight(32)
        projectLabel.setAlignment(Qt.AlignCenter)

        vBox.addLayout(radHBox)
        vBox.addWidget(LE)
        vBox.addWidget(self.treeWid)
        vBox.addWidget(projectLabel)
        self.leftArray = [LE, rad1, rad2, rad3]
        self.vWid.setLayout(vBox)

        #self.treeWid.actionpressed.connect(self.treeActionFn)
        self.treeWid.currentItemChanged.connect(self.treeWidChangedFn)
        LE.textChanged.connect(self.LEtextChangedFn)
        rad3.clicked.connect(self.radClickFn)
        rad2.clicked.connect(self.radClickFn)
        rad1.clicked.connect(self.radClickFn)

        self.treeWid.setCurrentItem(self.treeWid.itemAt(0, 0))
        return self.vWid

    def createTreeList(self, page='Char'):
        allowArray = ['ma']
        conceptPath = (self.serverPath + '\\asset\\CONCEPT\\' + page)
        if not os.path.exists(conceptPath):
            os.makedirs(conceptPath)
        folders = self.getFolders(path=conceptPath)
        defaultSize = QtCore.QSize(18, 18)
        self.treeWid.clear()
        for f in folders:
            itm = QtGui.QTreeWidgetItem()
            itm.setText(0, f)
            itm.setSizeHint(0, defaultSize)
            files = self.getFiles(self.serverPath + '\\asset\\CONCEPT\\' + page + '\\' + f)
            for fl in files:
                flsp = fl.split('.')[-1]
                if flsp in allowArray:
                    citm = QtGui.QTreeWidgetItem()
                    citm.setText(0, fl)
                    citm.setSizeHint(0, defaultSize)
                    itm.addChild(citm)
            self.treeWid.addTopLevelItem(itm)

    # ------ button functions ------------------------------


    def loginFn(self):
        logUI = userLoginUI.userLoginUI()
        logUI.setParent(self)
        logUI.Op_Ui()
        logUI.resultSinal.connect(self.loginFnReFn)
        logUI.move(50, 50)

    def loginFnReFn(self, string):
        passWordDB = PassWordDataBank.PassWordDataBank()
        isConfirm = passWordDB.val(string[0], string[1])
        if isConfirm:
            self.fileMn.setTitle(string[0])
            cs = self.fileMn.children()
            for c in cs:
                if 'regist' == c.text() or 'login' == c.text():
                    c.setVisible(False)
        localSetDict = self.loadJson(self.localSetPath + 'localSet.json')
        localSetDict.update({'user': str(string[0])})
        self.saveJson(localSetDict, self.localSetPath + 'localSet.json')

    def registFn(self):
        textUserName, okUserName = QtGui.QInputDialog.getText(self, 'Register',
                                                              'Enter UserName:')
        if okUserName:
            textPass, okPass = QtGui.QInputDialog.getText(self, 'Register',
                                                          'Enter PassWord:')
            if okPass:
                passWordDB = PassWordDataBank.PassWordDataBank()
                passWordDB.register(str(textUserName), str(textPass))
        pass

    def exitFn(self):
        sender = self.sender()
        sender.parent().setTitle('Login')
        cs = self.fileMn.children()
        for c in cs:
            if 'regist' == c.text() or 'login' == c.text():
                c.setVisible(True)
        localSetDict = self.loadJson(self.localSetPath + 'localSet.json')
        localSetDict.update({'user': 'Login'})
        self.saveJson(localSetDict, self.localSetPath + 'localSet.json')

    # login system function over



    def radClickFn(self):
        nowsel = self.radGrp.checkedId()
        if nowsel == 0:
            self.createTreeList(page='Char')
            self.nowTreePage = 'Char'
        elif nowsel == 1:
            self.createTreeList(page='Prop')
            self.nowTreePage = 'Prop'
        elif nowsel == 2:
            self.createTreeList(page='Env')
            self.nowTreePage = 'Env'

    def aboveItemFn(self):
        node = self.treeWid.itemAbove(self.treeWid.currentItem())
        if node:
            self.treeWid.setCurrentItem(node)

    def belowItemFn(self):
        node = self.treeWid.itemBelow(self.treeWid.currentItem())
        if node:
            self.treeWid.setCurrentItem(node)

    def prePicFn(self):
        nowRow = self.picView.currentRow()
        nowRow -= 1
        if nowRow < 0:
            nowRow = 0
        self.picView.setCurrentRow(nowRow)
        self.changePicFn()

    def nextPicFn(self):
        nowRow = self.picView.currentRow()
        nowRow += 1
        if nowRow > self.picView.count():
            nowRow = self.picView.count()
        self.picView.setCurrentRow(nowRow)
        self.changePicFn()

    # arrow functions over

    def tabWidChangedFn(self):
        itemNode = ''
        if self.treeWid.currentItem().parent():
            itemNode = self.treeWid.currentItem().parent()
        else:
            itemNode = self.treeWid.currentItem()
        self.nowSelMainTreeItem = itemNode
        # print self.nowSelMainTreeItem.text(0)
        nowTab = self.tabWid.currentIndex()
        nowItem = self.tabWid.tabText(nowTab)

        if nowItem == 'general':
            self.loadGeneralPageData()
        elif nowItem == 'note':
            self.loadNoteListData()
        elif nowItem == 'history':
            self.loadHTMLHistoryData()
        elif nowItem == 'List':
            self.loadConceptPictureData()

    def linkFn(self, url):
        print 'use .write reader open .write file to check infomations'
        print url

    def shMn1actFn(self):
        pass

    def shMn2actFn(self):
        sender = self.sender()
        state = sender.isChecked()
        # print sender.text()
        if state:
            self.isTree = True
            self.vWid.setVisible(True)
        else:
            self.isTree = False
            self.vWid.setVisible(False)

    def shMn3actFn(self):
        sender = self.sender()
        state = sender.isChecked()

        if state:
            self.isTab = True
            self.tabWid.setVisible(True)
        else:
            self.isTab = False
            self.tabWid.setVisible(False)

    # tool bar function over

    def changePicFn(self):
        nowsel = self.picView.currentItem()
        if nowsel:
            spPath = os.path.split(str(nowsel.toolTip()))
            spName = spPath[-1].split('.')[0]
            nowPic = QtGui.QPixmap(spPath[0] + '\\' + spName + '_middle.jpg')

            self.plabPic.setPixmap(nowPic)
            self.plabPic.setToolTip(str(nowsel.toolTip()))

            artistlab = ''
            passinglab = ''
            startdatelab = ''
            confirmdatelab = ''
            machinelab = ''
            lastmsg = ''
            updatedatelab = ''
            for cc in self.infoGrp.children():
                if type(cc) != QtGui.QVBoxLayout and type(cc) != QtGui.QHBoxLayout:
                    if cc.toolTip() == 'artist':
                        artistlab = cc
                    if cc.toolTip() == 'passing':
                        passinglab = cc
                    if cc.toolTip() == 'startdate':
                        startdatelab = cc
                    if cc.toolTip() == 'confirmdate':
                        confirmdatelab = cc
                    if cc.toolTip() == 'machine':
                        machinelab = cc
                    if cc.toolTip() == 'lastmsg':
                        lastmsg = cc
                    if cc.toolTip() == 'updatedate':
                        updatedatelab = cc

            mainPath = os.path.dirname(str(nowsel.toolTip()))
            mainName = os.path.basename(str(nowsel.toolTip()))
            msgData = {}
            if os.path.exists(mainPath + '\\message.json'):
                msgData = self.loadJson(mainPath + '\\message.json')

            infoData = {}
            if os.path.exists(mainPath + '\\infomation.json'):
                infoData = self.loadJson(mainPath + '\\infomation.json')

            hasConfirm = False
            hasStart = False
            if mainName in msgData.keys():
                artistlab.setText(msgData[mainName][-1]['artist'])
                timeStr = msgData[mainName][-1]['updateDate']
                formTime = '{}-{}-{} {}:{}:{}'.format(timeStr[0:4], timeStr[4:6], timeStr[6:8], timeStr[8:10],
                                                      timeStr[10:12], timeStr[12:14])
                updatedatelab.setText(formTime)
                lastmsg.setText(msgData[mainName][-1]['message'])
                machinelab.setText(msgData[mainName][-1]['machine'])
            else:
                artistlab.setText('')
                updatedatelab.setText('')
                lastmsg.setText('')
                machinelab.setText('')

            if mainName in infoData.keys():
                confirmdatelab.setText(infoData[mainName])
                hasConfirm = True
            else:
                confirmdatelab.setText('')
            if 'startTime' in infoData.keys():
                startdatelab.setText(infoData['startTime'])
                hasStart = True
            else:
                startdatelab.setText('')

            passingStr = ''
            if hasStart:
                spSD = infoData['startTime'].split(' ')
                daySD = int(spSD[0].split('-')[2])
                monSD = int(spSD[0].split('-')[1])
                yearSD = int(spSD[0].split('-')[0])
                # passingStr
                if hasConfirm:
                    spED = infoData[mainName].split(' ')
                    dayED = int(spED[0].split('-')[2])
                    monED = int(spED[0].split('-')[1])
                    yearED = int(spED[0].split('-')[0])

                else:
                    nowdate = time.strftime("%m-%d-%Y", time.localtime(time.time()))
                    dayED = int(nowdate.split('-')[1])
                    monED = int(nowdate.split('-')[0])
                    yearED = int(nowdate.split('-')[2])

                d1 = datetime.datetime(yearSD, monSD, daySD)
                d2 = datetime.datetime(yearED, monED, dayED)
                passingStr = str((d2 - d1).days) + ' days'

            passinglab.setText(passingStr)

    # changed functions over

    def showConceptFn(self):
        itm = self.listLE.currentItem()

        servSp = self.serverPath.split('\\')
        servSp.append('asset')
        servSp.append('CONCEPT')
        servSp.append(self.nowTreePage)
        servSp.append(str(self.nowSelMainTreeItem.text(0)))

        servSp.append('uploadTemp')
        servSp.append(str(itm.text().split('\n')[0]))
        tempPath = '\\'.join(servSp)
        os.startfile(tempPath)

    def refuseConceptFn(self):
        itm = self.listLE.currentItem()
        emptyColor = QtGui.QColor(Qt.transparent)
        itm.setBackground(emptyColor)

        servSp = self.serverPath.split('\\')
        servSp.append('asset')
        servSp.append('CONCEPT')
        servSp.append(self.nowTreePage)
        servSp.append(str(self.nowSelMainTreeItem.text(0)))
        mainPath = '\\'.join(servSp)
        servSp.append('uploadTemp')
        servSp.append('acceptList.json')
        jsonPath = '\\'.join(servSp)
        jsonData = {}
        if os.path.exists(jsonPath):
            jsonData = self.loadJson(jsonPath)
        else:
            self.saveJson(jsonData, jsonPath)
        itmTxt = str(itm.text().split('\n')[0])
        if itmTxt in jsonData.keys():
            jsonData[itmTxt] = False
        else:
            jsonData.update({itmTxt: False})
        self.saveJson(jsonData, jsonPath)
        # save the accept infomation to acceptList.json

        tarPath = mainPath + '\\' + itmTxt
        spName = ''
        if os.path.exists(tarPath):
            os.remove(tarPath)
            spName = itmTxt.split('.')[0]

            os.remove(mainPath + '\\' + spName + '_small.jpg')
            os.remove(mainPath + '\\' + spName + '_middle.jpg')

        rDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        historypath = self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + str(
            self.nowSelMainTreeItem.text(0)) + '\\history.html'
        if not (os.path.exists(historypath)):
            self.HTML_CreateEmptyStyle(historypath)

        userName = self.getUser()
        innerMsg = '[ CONCEPT ][ refuse ] ' + spName + ' <br> refuseTime : ' + rDate + '<br>refuse by ' + userName
        htmlMsg = self.HTML_createMsg(innerMsg, userName, '', side=1, initPath=self.initPath)
        self.HTML_addMsg(historypath, str(htmlMsg))

    def acceptConceptFn(self):
        itm = self.listLE.currentItem()
        linearGradient = QtGui.QLinearGradient(60, 50, 200, 200)
        linearGradient.setColorAt(0, Qt.transparent)
        linearGradient.setColorAt(0.89, Qt.transparent)
        linearGradient.setColorAt(0.9, QtGui.QColor(200, 200, 200))
        linearGradient.setColorAt(0.94, QtGui.QColor(200, 200, 200))
        linearGradient.setColorAt(0.95, QtGui.QColor(0, 200, 0))
        linearGradient.setColorAt(1.0, QtGui.QColor(0, 200, 0))
        itm.setBackground(QtGui.QBrush(linearGradient))
        # draw color in listLE.item for green

        servSp = self.serverPath.split('\\')
        servSp.append('asset')
        servSp.append('CONCEPT')
        servSp.append(self.nowTreePage)
        servSp.append(str(self.nowSelMainTreeItem.text(0)))
        mainPath = '\\'.join(servSp)
        servSp.append('uploadTemp')
        tempPath = '\\'.join(servSp)
        servSp.append('acceptList.json')
        jsonPath = '\\'.join(servSp)
        jsonData = {}
        if os.path.exists(jsonPath):
            jsonData = self.loadJson(jsonPath)
        else:
            self.saveJson(jsonData, jsonPath)
        itmTxt = str(itm.text().split('\n')[0])
        if itmTxt in jsonData.keys():
            jsonData[itmTxt] = True
        else:
            jsonData.update({itmTxt: True})
        self.saveJson(jsonData, jsonPath)
        # save the accept infomation to acceptList.json

        sorPath = tempPath + '\\' + itmTxt
        tarPath = mainPath + '\\' + itmTxt
        if os.path.exists(tarPath):
            os.remove(tarPath)
        shutil.copyfile(sorPath, tarPath)
        shutil.copystat(sorPath, tarPath)
        # copy big picture
        spName = itmTxt.split('.')[0]

        shutil.copyfile(tempPath + '\\' + spName + '_small.jpg', mainPath + '\\' + spName + '_small.jpg')
        shutil.copystat(tempPath + '\\' + spName + '_small.jpg', mainPath + '\\' + spName + '_small.jpg')

        shutil.copyfile(tempPath + '\\' + spName + '_middle.jpg', mainPath + '\\' + spName + '_middle.jpg')
        shutil.copystat(tempPath + '\\' + spName + '_middle.jpg', mainPath + '\\' + spName + '_middle.jpg')
        # copy file to main path.

        sorLog = tempPath + '\\message.json'
        tarLog = mainPath + '\\message.json'
        if os.path.exists(tarLog):
            os.remove(tarLog)
        shutil.copyfile(sorLog, tarLog)
        shutil.copystat(sorLog, tarLog)

        msgData = self.loadJson(tarLog)
        uString = msgData[itmTxt][-1]['updateDate']
        uTime = '{}-{}-{} {}:{}:{}'.format(uString[0:4], uString[4:6], uString[6:8], uString[8:10], uString[10:12],
                                           uString[12:14])
        uUser = msgData[itmTxt][-1]['artist']
        # update the infomations to mainPath

        tarInfo = mainPath + '\\infomation.json'
        # confirm time and start time
        tarData = {}
        if os.path.exists(tarInfo):
            tarData = self.loadJson(tarInfo)
        else:
            self.saveJson(tarData, tarInfo)

        cDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        if not ('confirm' in tarData.keys()):
            tarData.update({'startTime': cDate})
        # itmTxt=str(itm.text().split('\n')[0])
        if itmTxt in tarData.keys():
            tarData[itmTxt] = cDate
        else:
            tarData.update({itmTxt: cDate})
        self.saveJson(tarData, tarInfo)
        # list page button functions over

        historypath = self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + str(
            self.nowSelMainTreeItem.text(0)) + '\\history.html'
        if not (os.path.exists(historypath)):
            self.HTML_CreateEmptyStyle(historypath)

        userName = self.getUser()
        innerMsg = '[ CONCEPT ][ confirm ] ' + spName + ' <br> updateTime : ' + uTime + '<br>update by ' + uUser + ' <br> confirmTime : ' + cDate + '<br>confirm by ' + userName
        htmlMsg = self.HTML_createMsg(innerMsg, userName, '', side=1, initPath=self.initPath)
        self.HTML_addMsg(historypath, str(htmlMsg))

        nextPartSp = self.serverPath.split('\\')
        nextPartSp.append('asset')
        nextPartSp.append('MODEL')
        nextPartSp.append(self.nowTreePage)
        nextPartSp.append(str(self.nowSelMainTreeItem.text(0)))
        npPath = '\\'.join(nextPartSp)
        if not os.path.exists(npPath):
            os.makedirs(npPath)

    def oprbtn_openUploadFn(self):
        box = dragBox.PictureUploadUI()
        box.setParent(self)
        box.Op_Ui()
        box.upload.connect(self.picUploadFn)
        box.move(0, 0)
        box.resize(self.width(), self.height())

    def copyConceptToModelFn(self):
        # print self.conceptPath
        # print self.conceptDownloadPath

        conceptArray = []
        concepttime = ''
        if os.path.exists(self.conceptPath):
            cFiles = os.listdir(self.conceptPath)
            for c in cFiles:
                if '.jpg' in c:
                    conceptArray.append(self.conceptPath + '\\' + c)
                    gettime = os.path.getmtime(self.conceptPath + '\\' + c)
                    if gettime > concepttime or concepttime == '':
                        concepttime = gettime
        else:
            pass

        modelArray = []
        modeltime = ''
        if os.path.exists(self.conceptDownloadPath):
            dFiles = os.listdir(self.conceptDownloadPath)
            for d in dFiles:
                if '.jpg' in d:
                    modelArray.append(self.conceptDownloadPath + '\\' + d)
                    gettime = os.path.getmtime(self.conceptDownloadPath + '\\' + d)
                    if gettime > modeltime or modeltime == '':
                        modeltime = gettime
        else:
            pass

        # copy the concept from CONCEPT to CONCEPT and local CONCEPT
        if modeltime == '' or concepttime > modeltime:
            files = os.listdir(self.conceptDownloadPath)
            if files:
                for f in files:
                    checkpath = self.conceptDownloadPath + '\\' + f
                    if os.path.isfile(checkpath):
                        os.remove(checkpath)
            # clear files above the path.

            timeStr = time.strftime("%Y%m%d%H%M%S", time.localtime(concepttime))
            backupPath = self.conceptDownloadPath + '\\history\\' + timeStr
            if os.path.exists(backupPath):
                files = os.listdir(backupPath)
                if files:
                    for f in files:
                        checkpath = backupPath + '\\' + f
                        if os.path.isfile(checkpath):
                            os.remove(checkpath)
            else:
                os.makedirs(backupPath)

            for c in conceptArray:
                base = os.path.basename(c)
                targetBase = backupPath + '\\' + base
                targetView = self.conceptDownloadPath + '\\' + base

                shutil.copyfile(c, targetBase)
                shutil.copystat(c, targetBase)
                shutil.copyfile(c, targetView)
                shutil.copystat(c, targetView)
            # copy to CONCEPT over



            itm = self.treeWid.currentItem()
            changeTabItm = ''
            if itm.parent():
                changeTabItm = itm.parent()
            else:
                changeTabItm = itm

            infoPath = self.serverPath + '\\asset\\CONCEPT\\' + self.nowTreePage + '\\' + changeTabItm.text(
                0) + '\\infomation.json'
            dict = self.loadJson(infoPath)

            artName = ''
            if self.fileMn.title().lower() != 'login':
                artName = self.fileMn.title()
            else:
                artName = getpass.getuser()
            if not (artName in dict['artist']):
                dict['artist'].append(artName)

            sDate = time.strftime("%m-%d %H:%M:%S %Y", time.localtime(time.time()))
            dict['startDate'].append(sDate)
            dict['machine'].append(getpass.getuser())
            self.saveJson(dict, infoPath)

            self.loadGeneralPageData()
            # load and add general page data .over


            historypath = self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + changeTabItm.text(
                0) + '\\history.html'
            if not (os.path.exists(historypath)):
                self.HTML_CreateEmptyStyle(historypath)

            userName = self.getUser()
            innerMsg = '[ CONCEPT ] {} copy the concept from concept path to model path'.format(userName)
            htmlMsg = self.HTML_createMsg(innerMsg, userName, '', side=1, initPath=self.initPath)
            self.HTML_addMsg(historypath, str(htmlMsg))

            # html message over
            return True

    def getUser(self):
        userName = str(self.fileMn.title())
        if userName.lower() == 'login':
            ans = QtGui.QMessageBox.question(self, 'no user login',
                                             'uster not login\ndoyou wanna input ustername?\nclick cancel to user machine ID',
                                             QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if ans == QtGui.QMessageBox.No:
                userName = getpass.getuser()
            elif ans == QtGui.QMessageBox.Yes:
                userName, ok3 = QtGui.QInputDialog.getText(self, 'custom name', '', QtGui.QLineEdit.Normal,
                                                           'input a name')
                if ok3:
                    if str(userName).lower() == 'login':
                        userName = getpass.getuser()
                else:
                    userName = getpass.getuser()
        return userName

    def refrenceModelFn(self):

        path = self.serverPath + '\\asset\\CONCEPT\\' + self.nowTreePage + '\\' + self.itemNode.text(
            0) + '\\DownloadConcept'

        modelArray = []
        dFiles = os.listdir(path)
        for d in dFiles:
            if '.jpg' in d:
                modelArray.append(path + '\\' + d)

        localMainPath = path.replace(self.serverPath, self.localPath)
        if not os.path.exists(localMainPath):
            os.makedirs(localMainPath)

        for i in modelArray:
            localP = i.replace(self.serverPath, self.localPath)
            if os.path.exists(localP):
                localMtime = round(os.path.getmtime(localP), 2)
                serveMtime = round(os.path.getmtime(i), 2)
                # retain two decimal places

                if localMtime != serveMtime:
                    lt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(localMtime))
                    st = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(serveMtime))
                    message = os.path.basename(
                        localP) + '\n\nwhich one do you want...?\nlocal  : {}\nserver : {}'.format(lt, st)
                    rlt = cmds.confirmDialog(m=message, b=['local', 'server'])
                    if rlt == 'server':
                        os.remove(localP)
                        shutil.copyfile(i, localP)
                        shutil.copystat(i, localP)
                        # if the times are diffrent,use dialog to choose which one do you want.
            else:
                shutil.copyfile(i, localP)
                shutil.copystat(i, localP)

        os.startfile(localMainPath)

    def picUploadFn(self, list):
        # codec = QtCore.QTextCodec.codecForName("GB2312")
        # leftMsg = unicode(codec.toUnicode(list[0]))
        # codec = QtCore.QTextCodec.codecForName("utf-8")
        # gg = codec.toUnicode(list[0])
        # print gg

        localtime = time.localtime(time.time())
        nowtime = time.strftime("%Y%m%d%H%M%S", localtime)
        tyStr = ''
        if self.nowTreePage == 'Char':
            tyStr = 'cha'
        else:
            tyStr = self.nowTreePage.lower()

        servSp = self.serverPath.split('\\')
        servSp.append('asset')
        servSp.append(self.departmentName)
        servSp.append(self.nowTreePage)
        servSp.append(str(self.nowSelMainTreeItem.text(0)))
        servSp.append('uploadTemp')
        servPath = ''

        tempPath = '\\'.join(servSp)
        if not os.path.exists(tempPath):
            os.makedirs(tempPath)

        jsonPath = tempPath + '\\message.json'
        if not os.path.exists(jsonPath):
            emptyDic = {}
            self.saveJson(emptyDic, jsonPath)

        userName = str(self.fileMn.title())
        if userName.lower() == 'login':
            userName = getpass.getuser()

        jsonData = self.loadJson(jsonPath)
        fileString = ''
        for i in list[1]:
            filename = os.path.basename(str(i))
            spName = filename.split('.')
            tarPath = tempPath + '\\' + filename
            tarMid = tempPath + '\\' + spName[0] + '_middle.jpg'
            tarSmall = tempPath + '\\' + spName[0] + '_small.jpg'
            if os.path.exists(tarPath):
                quickMsg = QtGui.QMessageBox.question(self, "Question",
                                                      filename + '\nfile exists.do you want replace?',
                                                      QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel,
                                                      QtGui.QMessageBox.Ok)
                if quickMsg == QtGui.QMessageBox.Cancel:
                    continue
                os.remove(tarPath)
                if os.path.exists(tarMid):
                    os.remove(tarMid)
                if os.path.exists(tarSmall):
                    os.remove(tarSmall)
            shutil.copyfile(i, tarPath)
            shutil.copystat(i, tarPath)
            # copy orig pic

            origPic = QtGui.QPixmap(i)
            midPic = origPic.scaledToHeight(400)
            smallPic = origPic.scaledToHeight(100)
            midPic.save(tarMid)
            smallPic.save(tarSmall)
            # scale and copy

            fileString = fileString + filename + '<br>'
            if filename in jsonData.keys():
                item = jsonData[filename]
                item.append({"updateDate": nowtime,
                             "artist": userName,
                             "machine": getpass.getuser(),
                             "message": list[0]})
                jsonData[filename] = item
            else:

                jsonData.update({filename: [{"updateDate": nowtime,
                                             "artist": userName,
                                             "machine": getpass.getuser(),
                                             "message": list[0]}]})

        self.saveJson(jsonData, jsonPath)

        historypath = self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + str(
            self.nowSelMainTreeItem.text(0)) + '\\history.html'
        if not (os.path.exists(historypath)):
            self.HTML_CreateEmptyStyle(historypath)

        userName = self.getUser()
        innerMsg = '[ CONCEPT ][ update ] upload <br>' + fileString + ' updateTime : ' + time.strftime(
            "%Y-%m-%d %H:%M:%S", localtime) + '<br>update by ' + userName + '<br> message:' + list[0]
        htmlMsg = self.HTML_createMsg(innerMsg, userName, '', side=1, initPath=self.initPath)
        self.HTML_addMsg(historypath, str(htmlMsg))

    def loadGeneralPageData(self):
        changeTabItm = self.nowSelMainTreeItem
        servDate = ''
        localDate = ''

        for c in self.tabWid.currentWidget().children():
            if type(c) == QtGui.QGroupBox:
                if c.title() == 'concept':
                    for cc in c.children():
                        if type(cc) != QtGui.QVBoxLayout:
                            if cc.toolTip() == 'print servDate':
                                servDate = cc
                            elif cc.toolTip() == 'print localDate':
                                localDate = cc

        filePath = self.serverPath + '\\asset\\CONCEPT\\' + self.nowTreePage + '\\' + str(changeTabItm.text(0)) + '\\'

        files = self.getFiles(filePath)
        hasPic = []
        for f in files:
            if '.jpg' in f:
                print f
                if (not '_middle.jpg' in f) and (not '_small.jpg' in f):
                    hasPic.append(filePath + f)

        if hasPic:
            self.nowPicPath = hasPic[0]
        else:
            self.nowPicPath = self.initPath + '\\data\\currentPic.png'

        # load title label
        self.titleLabel.setText(changeTabItm.text(0))
        # load concept info
        sp = self.serverPath.split('\\')
        sp.append('asset')
        sp.append(self.departmentName)
        sp.append(self.nowTreePage)
        sp.append(str(changeTabItm.text(0)))
        self.conceptPath = '\\'.join(sp)
        print 'conceptPath is :' + self.conceptPath
        cFiles = os.listdir(self.conceptPath)
        conceptArray = []
        concepttime = ''
        conceptStrTime = ''
        if os.path.exists(self.conceptPath):
            for c in cFiles:
                if '.jpg' in c:
                    print 'file under path: ' + c
                    conceptArray.append(self.conceptPath + '\\' + c)
                    gettime = os.path.getmtime(self.conceptPath + '\\' + c)
                    if concepttime == '':
                        concepttime = gettime
                    if gettime > concepttime:
                        concepttime = gettime
                    conceptStrTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(concepttime))
        else:
            os.makedirs(self.conceptPath)
            conceptStrTime = ''

        sp = self.serverPath.split('\\')
        sp.append('asset')
        sp.append(self.departmentName)
        sp.append(self.nowTreePage)
        sp.append(str(changeTabItm.text(0)))
        sp.append('DownloadConcept')
        self.conceptDownloadPath = '\\'.join(sp)
        print 'concept download path is :' + self.conceptDownloadPath

        modelArray = []
        modeltime = ''
        modelStrTime = ''
        if os.path.exists(self.conceptDownloadPath):
            cFiles = os.listdir(self.conceptDownloadPath)
            if cFiles:
                for c in cFiles:
                    if '.jpg' in c:
                        modelArray.append(self.conceptDownloadPath + '\\' + c)
                        gettime = os.path.getmtime(self.conceptDownloadPath + '\\' + c)
                        if modeltime == '':
                            modeltime = gettime
                        if gettime > modeltime:
                            modeltime = gettime
                        modelStrTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(modeltime))
            else:
                modelStrTime = ''

        else:
            os.makedirs(self.conceptDownloadPath)
            modelStrTime = ''

        # load concept infomations over
        self.picView.clear()
        Picsp = self.serverPath.split('\\')
        Picsp.append('asset')
        Picsp.append('CONCEPT')
        Picsp.append(self.nowTreePage)
        Picsp.append(str(changeTabItm.text(0)))
        tp = '\\'.join(Picsp)
        tf = os.listdir(tp)
        isFill = False
        for t in tf:
            Qstring = tp + '\\' + t
            if os.path.isfile(Qstring) and ('.jpg' in t):
                if (not '_middle.jpg' in t) and (not '_small.jpg' in t):
                    spName = t.split('.')[0]
                    qp = QtGui.QPixmap(tp + '\\' + spName + '_small.jpg')
                    tempIcon = QtGui.QIcon()
                    tempIcon.addPixmap(qp)
                    tempItem = QtGui.QListWidgetItem()
                    tempItem.setToolTip(Qstring)
                    tempItem.setIcon(tempIcon)
                    self.picView.addItem(tempItem)
                    isFill = True
        if isFill:
            self.picView.setCurrentRow(0)
        else:
            tempPic = QtGui.QPixmap(self.initPath + '\\data\\currentPic.png')
            self.plabPic.setPixmap(tempPic)
            self.plabPic.setToolTip('empty pic')
        # load charactor pictures over

        pass

    def loadHTMLHistoryData(self):

        changeTabItm = self.nowSelMainTreeItem

        if type(changeTabItm) != str:
            historypath = self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + changeTabItm.text(
                0) + '\\history.html'
            if (os.path.exists(historypath)):
                historydata = open(historypath)
                codec = QtCore.QTextCodec.codecForName('utf-8')
                itmString = codec.toUnicode(historydata.read())
                self.qweb.setHtml(itmString, QtCore.QUrl(
                    self.serverPath + '\\asset\\' + self.departmentName + '\\' + self.nowTreePage + '\\' + changeTabItm.text(
                        0) + '\\note'))
            else:
                self.qweb.setHtml('', '')
        pass

    def loadNoteListData(self):
        changeTabItm = self.nowSelMainTreeItem

        colorArray = [
            [12, 112, 143],
            [151, 56, 84],
            [79, 70, 136],
            [134, 83, 70],
            [44, 85, 110],
            [140, 43, 100],
            [89, 128, 70],
            [155, 141, 63],
            [68, 137, 114],
            [149, 85, 43]

        ]
        # every value plus 100 is original color
        self.comLE.clear()

        noteDir = self.serverPath + '\\asset\\' + self.departmentName + '\\' + self.nowTreePage + '\\' + changeTabItm.text(
            0) + '\\note'
        if os.path.exists(noteDir):
            folders = os.listdir(noteDir)
            count = 0
            for f in folders:
                cn = count % 10
                pngs = []
                toolTipPath = ''
                files = os.listdir(noteDir + '\\' + f)
                for fi in files:
                    if '.json' in fi:
                        toolTipPath = noteDir + '\\' + f + '\\' + fi
                    if '.png' in fi:
                        pngs.append(noteDir + '\\' + f + '\\' + fi)
                iconFile = ''
                if pngs:
                    iconFile = pngs[0]
                else:
                    iconFile = self.iconPath + '\\lifeStyle18.png'
                icn = QtGui.QIcon(iconFile)

                toolTip = 'no pre common in path'
                if toolTipPath:
                    with open(toolTipPath, "rt") as file:
                        toolTip = file.read().decode('utf-8')

                linearGradient = QtGui.QLinearGradient(60, 50, 200, 200)
                linearGradient.setColorAt(0, Qt.transparent)
                linearGradient.setColorAt(0.79, Qt.transparent)
                linearGradient.setColorAt(0.8, QtGui.QColor(200, 200, 200))
                linearGradient.setColorAt(0.84, QtGui.QColor(200, 200, 200))
                linearGradient.setColorAt(0.85, QtGui.QColor(colorArray[cn][0], colorArray[cn][1], colorArray[cn][2]));
                linearGradient.setColorAt(1.0, QtGui.QColor(colorArray[cn][0], colorArray[cn][1], colorArray[cn][2]));

                regf = '{}-{}-{} {}:{}:{}'.format(f[0:4], f[4:6], f[6:8], f[8:10], f[10:12], f[12:14])
                regf += ' | ' + toolTip[:100]
                itm = QtGui.QListWidgetItem()
                itm.setText(regf)
                itm.setSizeHint(QtCore.QSize(225, 48))
                itm.setIcon(icn)
                itm.setToolTip(f)
                itm.setBackground(QtGui.QBrush(linearGradient))
                self.comLE.addItem(itm)
                count += 1
                # dir(QtGui.QListWidgetItem)
                # QListWidgetItem
        pass

    def loadConceptPictureData(self):

        changeTabItm = self.nowSelMainTreeItem
        # load concept pictures
        # tab,page3,in a Qlistwidget to add some

        linearGradient = QtGui.QLinearGradient(60, 50, 200, 200)
        linearGradient.setColorAt(0, Qt.transparent)
        linearGradient.setColorAt(0.89, Qt.transparent)
        linearGradient.setColorAt(0.9, QtGui.QColor(200, 200, 200))
        linearGradient.setColorAt(0.94, QtGui.QColor(200, 200, 200))
        linearGradient.setColorAt(0.95, QtGui.QColor(0, 200, 0))
        linearGradient.setColorAt(1.0, QtGui.QColor(0, 200, 0))
        # define a gradient background color for accept items.


        self.listLE.clear()
        emptyItm = QtGui.QListWidgetItem()
        emptyItm.setText('empty')
        self.listLE.addItem(emptyItm)
        # default state

        self.conceptPath = self.serverPath + '\\asset\\' + self.departmentName + '\\' + self.nowTreePage + '\\' + changeTabItm.text(
            0) + '\\uploadTemp'
        isConceptExt = os.path.exists(self.conceptPath)
        msgPath = self.conceptPath + '\\message.json'
        isMsgExt = os.path.exists(msgPath)
        print 'pic path is : ' + self.conceptPath
        print 'msg path is : ' + msgPath

        if isConceptExt and isMsgExt:
            jsonData = self.loadJson(msgPath)
            acceptData = {}
            acceptPath = self.conceptPath + '\\acceptList.json'
            print 'acc path is : ' + acceptPath
            if os.path.exists(acceptPath):
                acceptData = self.loadJson(acceptPath)
            temps = os.listdir(self.conceptPath)
            if temps:
                self.listLE.clear()
                # clear default items.
                for i in temps:
                    if '.jpg' in i:
                        if (not '_middle.jpg' in i) and (not '_small.jpg' in i):
                            spName = i.split('.')[0]
                            iconPath = self.conceptPath + '\\' + spName + '_small.jpg'
                            itmData = jsonData[i][-1]
                            itmStringTmp = ''
                            for key in itmData.keys():
                                itmStringTmp += str(key) + ':' + str(itmData[key]) + '\n'
                            codec = QtCore.QTextCodec.codecForName("utf-8")
                            itmString = codec.toUnicode(itmStringTmp)

                            icn = QtGui.QIcon(iconPath)
                            itm = QtGui.QListWidgetItem()
                            itm.setText(i + '\nArtist : ' + str(itmData['artist']))
                            itm.setSizeHint(QtCore.QSize(225, 48))
                            itm.setIcon(icn)
                            itm.setToolTip(itmString)
                            if i in acceptData.keys():
                                state = acceptData[i]
                                if state:
                                    itm.setBackground(QtGui.QBrush(linearGradient))
                            self.listLE.addItem(itm)

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        pass

    def treeWidChangedFn(self):
        sender = self.sender()
        itm = sender.currentItem()
        if itm:
            if self.isTab:
                self.tabWidChangedFn()

    def LEtextChangedFn(self):
        sender = self.sender()
        nowTxt = str(sender.text()).lower()
        print nowTxt
        itmsCount = self.treeWid.topLevelItemCount()
        for i in range(itmsCount):
            theNode = self.treeWid.topLevelItem(i)
            if nowTxt in str(theNode.text(0)).lower():
                theNode.setHidden(False)
            else:
                theNode.setHidden(True)


    # -------------------- ui functions -------------


    def getFiles(self, path=''):
        skipArray = ['__init__.py', '__init__.pyc', 'Thumbs.db']
        dirs = os.listdir(path)
        files = []
        for d in dirs:
            if os.path.isfile(os.path.join(path, d)):
                if not (d in skipArray):
                    files.append(d)
        return files

    def getFolders(self, path=''):
        dirs = os.listdir(path)
        floder = []
        for d in dirs:
            if (not os.path.isfile(os.path.join(path, d))) and d != 'data':
                floder.append(d)
        return floder

    def spFn(self):
        sender = self.sender()
        wd = sender.widget(0).width()
        for c in sender.widget(0).children():
            oh = c.height()
            if oh > 20:
                oh = sender.widget(0).height() - 20
            c.resize(wd, oh)

            # -------------json--------------

    def loadJson(self, path):
        file_object = open(path, 'r')
        data = json.load(file_object)
        return data

    def saveJson(self, data, path):
        jsonDump = json.dumps(data)
        file_object = open(path, 'w')
        file_object.write(jsonDump)
        file_object.close()

    # ------event rewrite-----------

    def resizeEvent(self, e):

        dockSize = self.size()
        self.widgetHeight = dockSize.height() - 5
        self.widgetWidth = dockSize.width()

        self.L2 = 25
        self.splitter.setGeometry(0, self.L2, 0, 0)
        self.splitter.resize(self.widgetWidth, self.widgetHeight - self.L2)

        try:
            self.readWidget.resize(self.width(), self.height())
        except:
            pass

    def dragEnterEvent(self, e):
        if (e.mimeData().hasFormat("text/uri-list")):
            e.acceptProposedAction()

    def mousePressEvent(self, e):
        if (e.button() == Qt.LeftButton):
            pass

    def mouseReleaseEvent(self, e):
        pass

    def dropEvent(self, e):
        if not self.isTab:
            return
        urls = e.mimeData().urls()
        if len(urls) == 0:
            return

    def closeEvent(self, event):
        self.deleteLater()

    # ------------widget enter--------------
    def Op_Ui(self):
        self.show()
        self.resize(600, 800)
        self.move(400, 100)

    def createGeneralPage(self):
        pass
        '''
        msgWid.setLayout(msgVB)
        preBtn.clicked.connect(self.aboveItemFn)
        nextBtn.clicked.connect(self.belowItemFn)

        prePicBtn.clicked.connect(self.prePicFn)
        nextPicBtn.clicked.connect(self.nextPicFn)

        downloadConceptBtn.clicked.connect(self.copyConceptToModelFn)
        viewConceptBtn.clicked.connect(self.refrenceModelFn)
        oprbtn_uploadLow.clicked.connect(self.oprbtn_openUploadFn)

        self.picView.currentItemChanged.connect(self.changePicFn)
        return msgWid
        '''