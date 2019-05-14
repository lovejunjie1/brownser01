from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtWebKit import QWebView, QWebPage
import os, sys, time, shutil, json
filePath = os.path.realpath(__file__)
filePathsp = filePath.split('AssetManegerSystem_publish')

path = filePathsp[0] + '\\AssetManegerSystem_publish'
if not path in sys.path: sys.path.append(path)
if not path + '\\data' in sys.path: sys.path.append(path + '\\data')
if not path + '\\win\\bin' in sys.path: sys.path.append(path + '\\win\\bin')
if not path + '\\win\\CONCEPT' in sys.path: sys.path.append(path + '\\win\\CONCEPT')
#sys.path.append(filePath)

import script
import redBlackStyleSheet_0_10 as RBStyle

Mstyle = RBStyle.RedBlackStyleSheet()
Mstyle.setIconPath(script.getAssetManagerPath()['icon'])

import userLoginUI02_Qt as userLoginUI
import docWriter_reader3_win as docWriter_reader
import docWriter_writter8_win as docWriter_writter
import PassWordDataBank
import assetManager_HTML

'''
class SplashScreen(QtGui.QSplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__(QtGui.QPixmap(script.getAssetManagerPath()['icon'] + '\\loading.png'),
                                           Qt.WindowStaysOnTopHint)  

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
            newOpacity = self.windowOpacity() - 0.02 
            if newOpacity < 0:
                break
            self.setWindowOpacity(newOpacity)
            t += 1
            time.sleep(0.04)
'''

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



class assetManagerBoxUI_win_baseClass(QtGui.QWidget , assetManager_HTML.assetManager_HTML):
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

        super(assetManagerBoxUI_win_baseClass, self).__init__(*args, **kwargs)
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

    def searchNote(self, theStr):

        itmCount = self.comLE.count()
        for i in range(itmCount):
            itmCell = self.comLE.item(i)
            if str(theStr).lower() in str(itmCell.text()).lower():  # .encode('utf-8')
                itmCell.setHidden(False)
            else:
                itmCell.setHidden(True)

    def readNote(self):
        if self.comLE.currentItem():
            filedata = ''
            noteDir = self.serverPath + '\\asset\\' + self.departmentName + '\\' + self.nowTreePage + '\\' + self.nowSelMainTreeItem.text(
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
        #itemNode = self.nowSelMainTreeItem
        TEmain = docWriter_writter.textEditorMain()
        TEmain.itemName = self.nowSelMainTreeItem.text(0)
        TEmain.savePath = self.serverPath + '\\asset\\' + self.departmentName + '\\' + self.nowTreePage + '\\' + self.nowSelMainTreeItem.text(
            0) + '\\note'
        TEmain.screenDllPath = self.initPath + '\\win\\bin\\PrScrn.dll'
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


    def loadGeneralPageData(self):
        pass

    def loadHTMLHistoryData(self):

        changeTabItm = self.nowSelMainTreeItem
        producePath = str(self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + changeTabItm.text(
                0))
        if not os.path.exists(producePath):
            os.makedirs(producePath)

        if type(changeTabItm) != str:
            historypath = producePath + '\\history.html'
            if (os.path.exists(historypath)):
                historydata = open(historypath)
                codec = QtCore.QTextCodec.codecForName('utf-8')
                itmString = codec.toUnicode(historydata.read())
                self.qweb.setHtml(itmString, QtCore.QUrl(historypath))
            else:

                userName = self.getUser()
                innerMsg = '[ CONCEPT ] {} create history'.format(userName)
                htmlMsg = self.HTML_createMsg(innerMsg, userName, '', side=1, initPath=self.initPath)
                self.HTML_addMsg(historypath, str(htmlMsg))
                self.qweb.setHtml(htmlMsg, QtCore.QUrl(historypath))
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

        self.conceptPath = self.serverPath + '\\asset\\CONCEPT\\' + self.nowTreePage + '\\' + changeTabItm.text(
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
        itmsCount = self.treeWid.topLevelItemCount()
        for i in range(itmsCount):
            theNode = self.treeWid.topLevelItem(i)
            if nowTxt in str(theNode.text(0)).lower():
                theNode.setHidden(False)
            else:
                theNode.setHidden(True)

    def linkFn(self, url):
        print 'use .write reader open .write file to check infomations'
        print url

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

