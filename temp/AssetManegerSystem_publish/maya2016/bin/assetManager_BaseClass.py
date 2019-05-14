# -*- coding:utf-8 -*-
# rig manager tool
# figo
# 2017-11-15 16:26:58
# alpha version finish,and there alot of work need to fix
# 1.concept display error
# 2.main tree widget icon not display
# 3.noteUI is no icon display
# 2017-12-20 17:33:43
# alpha release 0.01
# remake the open funcion at left list.now we download the file to local path and open.not straitly open yet.
# after confirmed.we refrensh left list and right area
# when we uploaded a file.the window will automaticlly closed now.
# when we uploaded a file.artist and machine infomation will update.
# 2018-1-8 16:57:21 important update
# change the load method.
# include assetManager_writterUI.py
# include assetManager_userLoginUI.py
# include assetManager_readerUI.py
# include assetManager_submitTool.py


import sys, os, time, json, shutil, sqlite3, random, getpass, datetime
import maya.cmds as cmds

from shiboken import wrapInstance
from PySide import QtGui, QtCore
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from PySide.QtCore import Qt, QRect
from PySide.QtWebKit import QWebView, QWebPage


class clickLabel(QtGui.QLabel):
    def mousePressEvent(self, e):
        if (e.button() == Qt.LeftButton):
            os.startfile(self.toolTip())


class assetManager_BaseClass(QtGui.QDialog, MayaQWidgetDockableMixin,assetManager_HTML):
    titleName = ''
    widgetHeight = 950
    widgetWidth = 600
    initPath = ''
    UIitems = {}
    isTree = True  # show Tree
    isTab = True  # show Tab
    localPath = ''
    serverPath = ''
    nowPicPath = ''
    keepLogin = 'Login'
    localSetPath = ''
    nowTreePage = 'Char'
    departmentName = 'MODEL'
    GWid = ''  # general tab page widget
    L2 = 25

    def __init__(self, parent=None):

        self.extraInit()
        self.titleName = self.departmentName + '_AssetManager_Tool'

        self.cleanOpenWindow()

        super(assetManager_BaseClass, self).__init__(parent=parent)
        self.setWindowFlags(QtCore.Qt.Tool | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle(self.titleName)
        self.setMinimumWidth(self.widgetWidth)
        self.setMaximumWidth(self.widgetWidth * 3)
        self.setAcceptDrops(True)

        self.initPath = getAssetManagerPath()['main']
        self.iconPath = getAssetManagerPath()['icon']
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

    def cleanOpenWindow(self):
        gmw = getMayaWindow()
        for g in gmw.children():
            try:
                Tit = g.windowTitle()
                if Tit == self.titleName:
                    g.close()
                    g.setParent(None)
            except:
                pass

    def loadConfig(self):
        pathSet = self.initPath + '\\data\\path.json'
        #print pathSet
        pathDict = self.loadJson(pathSet)
        #print pathDict
        self.localSetPath = pathDict['localSetPath'] + '\\AssetManaSys_Local\\'
        if not os.path.exists(self.localSetPath):
            print 'localSetPath' + self.localSetPath
            print 'ready to make localSetPath'
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
        #print self.allProjects
        #print self.projectName

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

    def projectChangeFn(self,theAct):
        #print theAct
        #print theAct.text()
        jsonP = self.localSetPath + 'localSet.json'
        jsonDict = self.loadJson(jsonP)
        jsonDict.update({'project': theAct.text()})
        self.saveJson(jsonDict, jsonP)

        ans = QtGui.QMessageBox.information( self, "project Changed",
                                                  ('project changed to ' + str(theAct.text()) + '\nplease restart toolkit'),
                                                  QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if QtGui.QMessageBox.Yes == ans:

            #self.deleteLater()
            self.close()
        #if ans == QtGui.QMessageBox.Yes:

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
        self.createConceptTab()

        self.tabWid.currentChanged.connect(self.tabWidChangedFn)

    def createGeneralTab(self):
        self.GWid = QtGui.QWidget()
        self.GWid.setAttribute(Qt.WA_StyledBackground)
        self.GWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        self.GWid.setAttribute(Qt.WA_DeleteOnClose)

        self.tabWid.addTab(self.GWid, 'general')

    def createConceptTab(self):
        ConceptWid = QtGui.QWidget()
        ConceptWid.setAttribute(Qt.WA_StyledBackground)
        ConceptWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        ConceptWid.setAttribute(Qt.WA_DeleteOnClose)

        self.conceptHbox = QtGui.QGridLayout()

        ConceptWid.setLayout(self.conceptHbox)
        self.tabWid.addTab(ConceptWid, 'concept')

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
        #self.qweb.settings().setDefaultTextEncoding('utf-8')
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
        comLineE.cursorPositionChanged.connect(self.clearSearchBar)
        comLineE.textChanged.connect(self.searchNote)

    def clearSearchBar(self):
        sender = self.sender()
        if sender.text() == 'search bar':
            sender.setText('')

    def searchNote(self, str):
        itmCount = self.comLE.count()
        for i in range(itmCount):
            itmCell = self.comLE.item(i)
            if str in itmCell.text():  # .encode('utf-8')
                itmCell.setHidden(False)
            else:
                itmCell.setHidden(True)

    def readNote(self):
        itemNode = ''
        if self.treeWid.currentItem().parent():
            itemNode = self.treeWid.currentItem().parent()
        else:
            itemNode = self.treeWid.currentItem()

        filedata = ''
        noteDir = self.serverPath + '\\asset\\' + self.departmentName + '\\' + self.nowTreePage + '\\' + itemNode.text(
            0) + '\\note\\' + self.comLE.currentItem().toolTip()
        listdir = os.listdir(noteDir)
        for i in listdir:
            if '.writer' in i:
                with open(noteDir + '\\' + i, "rt") as file:
                    filedata = file.read().decode('utf-8')
        thewidget = assetManager_readerUI()
        thewidget.move(0, 0)
        thewidget.setText(filedata)
        thewidget.show()
        raise

    def openEidtWindow(self):
        itemNode = self.nowSelMainTreeItem

        TEmain = assetManager_writterUI()
        TEmain.itemName = itemNode.text(0)
        TEmain.savePath = self.serverPath + '\\asset\\' + self.departmentName + '\\' + self.nowTreePage + '\\' + itemNode.text(
            0) + '\\note'
        TEmain.initUI()
        TEmain.setParent(self)
        TEmain.move(0, 0)
        TEmain.resize(self.width(), self.height())
        TEmain.saveSignal.connect(self.writterSavedFn)
        TEmain.show()

    def writterSavedFn(self,data):
        print data
        self.loadNoteListData()

    def createTree(self):

        self.vWid = QtGui.QWidget()
        self.vWid.setMinimumWidth(self.widgetWidth * 0.1)
        #self.vWid.resize(self.widgetWidth * 0.5, self.widgetWidth - self.L2)

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

        self.treeWid = assetManager_DragTreeWidget()
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

        self.treeWid.actionpressed.connect(self.treeActionFn)
        self.treeWid.currentItemChanged.connect(self.treeWidChangedFn)
        LE.textChanged.connect(self.LEtextChangedFn)
        rad3.clicked.connect(self.radClickFn)
        rad2.clicked.connect(self.radClickFn)
        rad1.clicked.connect(self.radClickFn)

        self.treeWid.setCurrentItem(self.treeWid.itemAt(0, 0))
        return self.vWid

    def treeActionFn(self, str):
        pass

    def createTreeList(self, page='Char'):
        allowArray = ['ma']
        TreePath = self.serverPath + '\\asset\\' + self.departmentName + '\\' + page
        print 'treePath : ' + TreePath
        if not os.path.exists(TreePath):
            print 'ready to make treePath'
            os.makedirs(TreePath)
        folders = self.getFolders(path=(TreePath))
        defaultSize = QtCore.QSize(18, 18)
        self.treeWid.clear()
        for f in folders:
            itm = QtGui.QTreeWidgetItem()
            itm.setText(0, f)
            itm.setSizeHint(0, defaultSize)
            itemPath = self.serverPath + '\\asset\\' + self.departmentName + '\\' + page + '\\' + f
            itm.setToolTip(0, itemPath)
            files = self.getFiles(itemPath)
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
        logUI = assetManager_userLoginUI()
        logUI.setParent(self)
        logUI.Op_Ui()
        logUI.resultSinal.connect(self.loginFnReFn)

    def loginFnReFn(self, str):
        passWordDB = PassWordDataBank()
        isConfirm = passWordDB.val(str[0], str[1])
        if isConfirm:
            self.fileMn.setTitle(str[0])
            cs = self.fileMn.children()
            for c in cs:
                if 'regist' == c.text() or 'login' == c.text():
                    c.setVisible(False)
        localSetDict = self.loadJson(self.localSetPath + 'localSet.json')
        localSetDict.update({'user': str[0]})
        self.saveJson(localSetDict, self.localSetPath + 'localSet.json')

    def registFn(self):
        user = ''
        password = ''
        result = cmds.promptDialog(title='Register', message='Enter UserName:', button=['OK', 'Cancel'],
                                   defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')
        if result == 'OK':
            user = cmds.promptDialog(query=True, text=True)
            PWresult = cmds.promptDialog(title='Register', message='Enter PassWord:', button=['OK', 'Cancel'],
                                         defaultButton='OK', cancelButton='Cancel', dismissString='Cancel')
            if PWresult == 'OK':
                password = cmds.promptDialog(query=True, text=True)
                passWordDB = PassWordDataBank()
                passWordDB.register(user, password)
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
        elif nowItem == 'concept':
            self.loadConceptPictureData()

    def linkFn(self, url):
        print 'use .write reader open .write file to check infomations'
        print url

    def shMn1actFn(self):
        pass

    def shMn2actFn(self):
        sender = self.sender()
        state = sender.isChecked()
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

    def loadGeneralPageData(self):
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

        # load concept pictures
        changeTabItm = self.nowSelMainTreeItem
        self.clearLayout(self.conceptHbox)

        conceptPath = self.serverPath + '\\asset\\CONCEPT\\' + self.nowTreePage + '\\' + changeTabItm.text(0)
        isConceptExt = os.path.exists(conceptPath)

        pixmapArray = []
        if isConceptExt:
            temps = os.listdir(conceptPath)
            for i in temps:
                isf = os.path.isfile(conceptPath + '\\' + i)
                if isf:
                    if '.jpg' in i:
                        pixmap = QtGui.QPixmap()
                        pixmap.load(conceptPath + '\\' + i)
                        pixlab = clickLabel()
                        pixlab.setFixedWidth(120)
                        pixlab.setFixedHeight(120)
                        pixlab.setPixmap(pixmap.scaledToWidth(120))
                        pixlab.setToolTip(conceptPath + '\\' + i)
                        # pixlab.linkActivated.connect(self.openPic)
                        pixmapArray.append(pixlab)
        if pixmapArray:
            row = 0
            for count, i in enumerate(pixmapArray):
                colum = count % 3
                row = count / 3
                self.conceptHbox.addWidget(i, row, colum)

            self.conceptHbox.setRowStretch(row + 1, 1)
            pass


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
        nowTxt = sender.text()
        itmsCount = self.treeWid.topLevelItemCount()
        for i in range(itmsCount):
            theNode = self.treeWid.topLevelItem(i)
            if nowTxt in theNode.text(0):
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

    def dockCloseEventTriggered(self):
        """
        Handle stuff when the dock is closed
        self.close()
        self.deleteLater()
        """
        pass

    def resizeEvent(self, e):

        dockSize = self.size()
        self.widgetHeight = dockSize.height() - 5
        self.widgetWidth = dockSize.width()

        self.L2 = 25
        self.splitter.setGeometry(0, self.L2, 0, 0)
        self.splitter.resize(self.widgetWidth, self.widgetHeight - self.L2)

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

    def closeEvent(self, e):
        pass

    # ------------widget enter--------------
    def Op_Ui(self):
        #self.manual_init()
        self.show()


#ABC = assetManager_BaseClass()
#ABC.Op_Ui()