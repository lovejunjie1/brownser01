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
from PySide.phonon import *

class clickLabel(QtGui.QLabel):
    def mousePressEvent(self, e):
        if (e.button() == Qt.LeftButton):
            os.startfile(self.toolTip())


class HoverRadioButton(QtGui.QRadioButton):
    def __init__(self, parent=None):
        QtGui.QRadioButton.__init__(self, parent)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.setChecked(True)



class shotManager_BaseClass(QtGui.QDialog, MayaQWidgetDockableMixin, assetManager_HTML):
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
    nowTreePage = ''
    departmentName = 'LAYOUT'
    GWid = ''  # general tab page widget
    L2 = 25
    nowSelection = ''
    nowSelectionToolTip = ''
    lastCheckID = 0
    bigType = 'filmP'
    fpsList = ['game : 15 fps','film : 24 fps','pal : 25 fps','ntsc : 30 fps','show : 48 fps','palf : 50 fps','ntscf : 60 fps']
    def __init__(self, parent=None):

        self.extraInit()
        self.titleName = self.departmentName + '_ShotManager_Tool'

        self.cleanOpenWindow()

        super(shotManager_BaseClass, self).__init__(parent=parent)
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
        self.createCameraAssistTab()

        self.tabWid.currentChanged.connect(self.tabWidChangedFn)

    def createGeneralTab(self):
        self.GWid = QtGui.QWidget()
        self.GWid.setAttribute(Qt.WA_StyledBackground)
        self.GWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        self.GWid.setAttribute(Qt.WA_DeleteOnClose)

        self.tabWid.addTab(self.GWid, 'general')
        mv = QtGui.QVBoxLayout()
        self.GWid.setLayout(mv)

        h1 = QtGui.QHBoxLayout()
        mv.addLayout(h1)
        self.seqTitle = QtGui.QLabel('sequenceTitle')
        self.seqTitle.setStyleSheet(Mstyle.QLabel(fontSize='12px'))
        h1.addStretch(1)
        h1.addWidget(self.seqTitle)
        h1.addStretch(1)

        h2 = QtGui.QHBoxLayout()
        mv.addLayout(h2)
        self.shotTitle = QtGui.QLabel('shotTitle')
        self.shotTitle.setStyleSheet(Mstyle.QLabel(fontSize='12px'))
        h2.addStretch(1)
        h2.addWidget(self.shotTitle)

        '''
        #player start
        
        self.media = Phonon.MediaObject()
        self.media.setCurrentSource(Phonon.MediaSource('D:\\data\\movies\\playblast.avi'))

        vwidget = Phonon.VideoWidget(self.GWid)
        vwidget.setAspectRatio(Phonon.VideoWidget.AspectRatioAuto)





        Phonon.createPath(self.media, vwidget)

        aOutput = Phonon.AudioOutput(Phonon.VideoCategory)
        Phonon.createPath(self.media, aOutput)
        #vwidget.show()
        
        seekSlider = Phonon.SeekSlider()
        seekSlider.setMediaObject(self.media)
        self.media.play()
        #player = Phonon.VideoPlayer(Phonon.VideoCategory, self.GWid)
        #player.load(Phonon.MediaSource('D:\\dfp.mp3'))

        player = Phonon.VideoPlayer(Phonon.VideoCategory, self.GWid)

        player.play('D:\\data\\movies\\playblast.avi')
        
        mv.addWidget(vwidget)
        mv.addWidget(seekSlider)
        mv.addWidget(player)
        
        #player.play()
        #player.setFixedSize(200,200)
        #mv.addStretch(1)

        #player over
        '''
        self.imageTable = QtGui.QTabWidget()
        self.imageTable.setStyleSheet(Mstyle.QTabWidget(kw='a') + "QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ")
        self.imageTable.setFixedHeight(200)
        self.imageTable.setTabPosition(QtGui.QTabWidget.West)
        self.imageTable.setContentsMargins(0, 0, 0, 0)
        mv.addWidget(self.imageTable)

        # describeWid page ===================================

        describeWid = QtGui.QWidget()
        describeWid.setAttribute(Qt.WA_StyledBackground)
        describeWid.setStyleSheet('QWidget{background:rgb(89,89,89);border-radius: 12px}')
        describeHbox = QtGui.QHBoxLayout()
        describeWid.setLayout(describeHbox)


        imageSV = QtGui.QVBoxLayout()
        describeHbox.addLayout(imageSV)

        describeLab = QtGui.QLabel('some describes will apear in there')
        describeHbox.addWidget(describeLab)

        desPic = QtGui.QPixmap()


        self.imageTable.addTab(describeWid, 'describe')

        # imageWid page ===================================

        imageWid = QtGui.QWidget()
        imageWid.setAttribute(Qt.WA_StyledBackground)
        imageWid.setStyleSheet('QWidget{background:rgb(89,89,89);border-radius: 12px}')
        imageHbox = QtGui.QHBoxLayout()
        imageWid.setLayout(imageHbox)


        imageSV = QtGui.QVBoxLayout()
        imageHbox.addLayout(imageSV)

        self.bGrp = QtGui.QButtonGroup()

        radbtn1 = HoverRadioButton()
        radbtn1.setChecked(True)
        imageSV.addWidget(radbtn1)
        self.bGrp.addButton(radbtn1,0)

        radbtn2 = HoverRadioButton()
        self.bGrp.addButton(radbtn2,1)
        imageSV.addWidget(radbtn2)

        radbtn3 = HoverRadioButton()
        self.bGrp.addButton(radbtn3,2)
        imageSV.addWidget(radbtn3)

        self.picLab = QtGui.QLabel('pictureLabel')
        imageHbox.addWidget(self.picLab)

        self.imageTable.addTab(imageWid, 'image')

        # videoWid page ======================================

        videoWid = QtGui.QWidget()
        videoWid.setAttribute(Qt.WA_StyledBackground)
        videoWid.setStyleSheet('QWidget{background:rgb(89,89,89);border-radius: 12px}')
        videoVbox = QtGui.QVBoxLayout()
        videoWid.setLayout(videoVbox)

        viLab = QtGui.QLabel('videoLabel')
        videoVbox.addWidget(viLab)
        self.imageTable.addTab(videoWid, 'video')

        # self.imageTable over =============================================


        self.infoTable = QtGui.QTabWidget()
        self.infoTable.setStyleSheet(Mstyle.QTabWidget(kw='c') + "QTabBar::tab::disabled {width: 0px; height: 0px; margin: 0px; padding: 0px; border: none;} ")
        #self.infoTable.setFixedHeight(200)

        mv.addWidget(self.infoTable)
        # shot list page ==================================

        shotListWid = QtGui.QWidget()
        shotListWid.setAttribute(Qt.WA_StyledBackground)
        shotListWid.setStyleSheet('QWidget{background:rgb(89,89,89);border-radius: 12px}')
        self.infoTable.addTab(shotListWid, 'shots')


        # video list page ==================================

        videoListWid = QtGui.QWidget()
        videoListWid.setAttribute(Qt.WA_StyledBackground)
        videoListWid.setStyleSheet('QWidget{background:rgb(89,89,89);border-radius: 12px}')
        self.infoTable.addTab(videoListWid, 'videos')



        # normal info page===============================

        infoWid = QtGui.QWidget()
        infoWid.setAttribute(Qt.WA_StyledBackground)
        infoWid.setStyleSheet('QWidget{background:rgb(89,89,89);border-radius: 12px}')
        self.infoTable.addTab(infoWid, 'info')

        infoVbox = QtGui.QVBoxLayout()
        infoWid.setLayout(infoVbox)


        lastmsgHB = QtGui.QHBoxLayout()
        labLastMsgTitle = QtGui.QLabel('LastMsg : ', infoWid)
        labLastMsgTitle.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.lastmsg = QtGui.QLabel('', infoWid)

        self.lastmsg.setToolTip('lastmsg')
        self.lastmsg.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b', lang='c'))
        lastmsgHB.addWidget(labLastMsgTitle)
        lastmsgHB.addWidget(self.lastmsg)
        lastmsgHB.addStretch(1)

        infoGHB1 = QtGui.QHBoxLayout()
        lab4 = QtGui.QLabel('Artist : ', infoWid)
        lab4.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.artistlab = QtGui.QLabel('', infoWid)
        self.artistlab.setToolTip('artist')
        self.artistlab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        infoGHB1.addWidget(lab4)
        infoGHB1.addWidget(self.artistlab)
        infoGHB1.addStretch(1)

        infoGHB2 = QtGui.QHBoxLayout()
        lab5 = QtGui.QLabel('Passing : ', infoWid)
        lab5.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.passinglab = QtGui.QLabel('none days', infoWid)
        self.passinglab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        self.passinglab.setToolTip('passing')
        infoGHB2.addWidget(lab5)
        infoGHB2.addWidget(self.passinglab)
        infoGHB2.addStretch(1)

        infoGHB3 = QtGui.QHBoxLayout()
        lab6 = QtGui.QLabel('StartDate :     ', infoWid)
        lab6.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.startdatelab = QtGui.QLabel('', infoWid)
        self.startdatelab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        self.startdatelab.setToolTip('startdate')
        infoGHB3.addWidget(lab6)
        infoGHB3.addWidget(self.startdatelab)
        infoGHB3.addStretch(1)

        infoGHB6 = QtGui.QHBoxLayout()
        lab11 = QtGui.QLabel('UploadDate : ', infoWid)
        lab11.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.updatedatelab = QtGui.QLabel('', infoWid)
        self.updatedatelab.setToolTip('uploaddate')
        self.updatedatelab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        infoGHB6.addWidget(lab11)
        infoGHB6.addWidget(self.updatedatelab)
        infoGHB6.addStretch(1)

        infoGHB4 = QtGui.QHBoxLayout()
        lab7 = QtGui.QLabel('ConfirmData : ', infoWid)
        lab7.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.confirmdatelab = QtGui.QLabel('', infoWid)
        self.confirmdatelab.setToolTip('confirmdate')
        self.confirmdatelab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        infoGHB4.addWidget(lab7)
        infoGHB4.addWidget(self.confirmdatelab)
        infoGHB4.addStretch(1)

        infoGHB5 = QtGui.QHBoxLayout()
        lab8 = QtGui.QLabel('Machine : ', infoWid)
        lab8.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.machinelab = QtGui.QLabel('', infoWid)
        self.machinelab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        self.machinelab.setToolTip('machine')
        infoGHB5.addWidget(lab8)
        infoGHB5.addWidget(self.machinelab)
        infoGHB5.addStretch(1)

        infoVbox.addLayout(lastmsgHB)
        infoVbox.addLayout(infoGHB1)
        infoVbox.addLayout(infoGHB2)
        infoVbox.addLayout(infoGHB3)
        infoVbox.addLayout(infoGHB6)
        infoVbox.addLayout(infoGHB4)
        infoVbox.addLayout(infoGHB5)

        # camera info page ===================================================
        CameraInfoWid = QtGui.QWidget()
        CameraInfoWid.setAttribute(Qt.WA_StyledBackground)
        CameraInfoWid.setStyleSheet('QWidget{background:rgb(89,89,89);border-radius: 12px}')
        self.infoTable.addTab(CameraInfoWid, 'camera')

        CameraInfoVbox = QtGui.QVBoxLayout()
        CameraInfoWid.setLayout(CameraInfoVbox)

        camNameHB = QtGui.QHBoxLayout()
        camNameTitle = QtGui.QLabel('camera : ', CameraInfoWid)
        camNameTitle.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.camName = QtGui.QLabel('', CameraInfoWid)

        self.camName.setToolTip('camera name')
        self.camName.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b', lang='c'))
        camNameHB.addWidget(camNameTitle)
        camNameHB.addWidget(self.camName)
        camNameHB.addStretch(1)

        CameraInfoVbox.addLayout(camNameHB)

        # asset list page ===================================================
        addAssetWid = QtGui.QWidget()
        addAssetWid.setAttribute(Qt.WA_StyledBackground)
        addAssetWid.setStyleSheet('QWidget{background:rgb(89,89,89);border-radius: 12px}')

        #addAssetWid.setMaximumHeight(420)
        assetGVB = QtGui.QVBoxLayout()
        addAssetWid.setLayout(assetGVB)
        mv.addWidget(addAssetWid)

        self.assetTable = QtGui.QTableWidget()
        self.assetTable.setColumnCount(5)
        self.assetTable.setRowCount(1)
        self.assetTable.setHorizontalHeaderLabels(['dep','type', 'assetName', 'ver','ref'])
        #self.assetTable.horizontalHeader().setStretchLastSection(True)
        self.assetTable.horizontalHeader().setResizeMode(2,QtGui.QHeaderView.Stretch)
        #self.assetTable.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.assetTable.setColumnWidth(0, 40)
        self.assetTable.setColumnWidth(1, 40)
        self.assetTable.setColumnWidth(3, 40)
        self.assetTable.setColumnWidth(4, 40)
        self.assetTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.assetTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.assetTable.verticalHeader().setDefaultSectionSize(30)
        assetGVB.addWidget(self.assetTable)

        assetHbox = QtGui.QHBoxLayout()
        assetGVB.addLayout(assetHbox)

        addbutton = QtGui.QToolButton()
        addbutton.setFixedSize(16, 16)
        addbutton.setToolTip('add item')
        combiePath = self.iconPath + '\\plus.png'
        addbutton.setIcon(QtGui.QIcon(combiePath))
        addbutton.setIconSize(QtCore.QSize(16, 16))
        addbutton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        addbutton.setAutoRaise(True)
        addbutton.setStyleSheet(Mstyle.QToolButton())

        assetHbox.addWidget(addbutton)

        removebutton = QtGui.QToolButton()
        removebutton.setFixedSize(16, 16)
        removebutton.setToolTip('remove item')
        combiePath = self.iconPath + '\\minus.png'
        removebutton.setIcon(QtGui.QIcon(combiePath))
        removebutton.setIconSize(QtCore.QSize(16, 16))
        removebutton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        removebutton.setAutoRaise(True)
        removebutton.setStyleSheet(Mstyle.QToolButton())
        assetHbox.addWidget(removebutton)
        assetHbox.addStretch()


        changebutton = QtGui.QPushButton('change')
        changebutton.setFixedSize(60,16)
        changebutton.setStyleSheet(Mstyle.QPushButton())
        assetHbox.addWidget(changebutton)

        copybutton = QtGui.QPushButton('copy')
        copybutton.setFixedSize(60,16)
        copybutton.setStyleSheet(Mstyle.QPushButton())
        assetHbox.addWidget(copybutton)

        pastebutton = QtGui.QPushButton('paste')
        pastebutton.setFixedSize(60,16)
        pastebutton.setStyleSheet(Mstyle.QPushButton())
        assetHbox.addWidget(pastebutton)

        f5button = QtGui.QToolButton()
        f5button.setFixedSize(16, 16)
        f5button.setToolTip('refresh list and file')
        combiePath = self.iconPath + '\\refresh.png'
        f5button.setIcon(QtGui.QIcon(combiePath))
        f5button.setIconSize(QtCore.QSize(16, 16))
        f5button.setToolButtonStyle(Qt.ToolButtonIconOnly)
        f5button.setAutoRaise(True)
        f5button.setStyleSheet(Mstyle.QToolButton())
        assetHbox.addWidget(f5button)


        versionbutton = QtGui.QToolButton()
        versionbutton.setFixedSize(16, 16)
        versionbutton.setToolTip('version change')
        combiePath = self.iconPath + '\\changes.png'
        versionbutton.setIcon(QtGui.QIcon(combiePath))
        versionbutton.setIconSize(QtCore.QSize(16, 16))
        versionbutton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        versionbutton.setAutoRaise(True)
        versionbutton.setStyleSheet(Mstyle.QToolButton())
        assetHbox.addWidget(versionbutton)

        refbutton = QtGui.QToolButton()
        refbutton.setFixedSize(16, 16)
        refbutton.setToolTip('reference file in file')
        combiePath = self.iconPath + '\\reference.png'
        refbutton.setIcon(QtGui.QIcon(combiePath))
        refbutton.setIconSize(QtCore.QSize(16, 16))
        refbutton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        refbutton.setAutoRaise(True)
        refbutton.setStyleSheet(Mstyle.QToolButton())
        assetHbox.addWidget(refbutton)

        assetHbox2 = QtGui.QHBoxLayout()
        assetGVB.addLayout(assetHbox2)


        self.infoTable.addTab(addAssetWid, 'asset')

        # camera assist over =============================================

        self.keyGrp = QtGui.QGroupBox('keyframe')
        self.keyGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        self.keyGrp.setMaximumHeight(150)
        keyGVB = QtGui.QVBoxLayout()


        keyGHB1 = QtGui.QHBoxLayout()

        self.keyspin3 = QtGui.QSpinBox()
        self.keyspin3.setSuffix(' f')
        self.keyspin3.setToolTip('time range start')
        self.keyspin3.setValue(100)
        self.keyspin3.setMinimum(100)
        self.keyspin3.setMaximum(100)
        self.keyspin3.setEnabled(True)
        self.keyspin3.setStyleSheet(Mstyle.QSpinBox())
        keyGHB1.addWidget(self.keyspin3)

        keyLab1 = QtGui.QLabel(' to ')
        keyLab1.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent}')
        keyGHB1.addWidget(keyLab1)

        self.keyspin1 = QtGui.QSpinBox()
        self.keyspin1.setSuffix(' f')
        self.keyspin1.setToolTip('time range end')
        self.keyspin1.setMinimum(101)
        self.keyspin1.setMaximum(10000)
        self.keyspin1.setValue(200)
        self.keyspin1.setStyleSheet(Mstyle.QSpinBox())
        keyGHB1.addWidget(self.keyspin1)
        keyGHB1.addStretch()

        self.keyspin2 = QtGui.QSpinBox()
        self.keyspin2.setSuffix(' f')
        self.keyspin2.setToolTip('time range count')
        self.keyspin2.setMinimum(1)
        self.keyspin2.setMaximum(10000)
        self.keyspin2.setValue(self.keyspin1.value()-self.keyspin3.value())
        self.keyspin2.setStyleSheet(Mstyle.QSpinBox())
        keyGHB1.addWidget(self.keyspin2)

        keyLab2 = QtGui.QLabel('frames ')
        keyLab2.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent}')
        keyGHB1.addWidget(keyLab2)

        keysetBtn = QtGui.QPushButton('set')
        keysetBtn.setFixedSize(40, 20)
        keysetBtn.setStyleSheet(Mstyle.QPushButton(bordRad='9px'))
        keysetBtn.setToolTip('set keyframe range and rename camera')
        keyGHB1.addWidget(keysetBtn)

        keyGHB2 = QtGui.QHBoxLayout()

        self.fpsspin = QtGui.QComboBox()
        self.fpsspin.addItems(self.fpsList)
        self.fpsspin.setFixedWidth(90)
        self.fpsspin.setToolTip('fps')
        self.fpsspin.setCurrentIndex(1)
        self.fpsspin.setStyleSheet(Mstyle.QComboBox()+'QComboBox{padding-left:4px}')
        keyGHB2.addWidget(self.fpsspin)

        cameraSetBtn = QtGui.QPushButton('camera create/select', self.GWid)
        cameraSetBtn.setFixedHeight(20)
        cameraSetBtn.setStyleSheet(Mstyle.QPushButton(kw='b', bordRad='10px'))
        cameraSetBtn.setToolTip('open confirm window')
        keyGHB2.addWidget(cameraSetBtn)

        keyGVB.addLayout(keyGHB1)
        keyGVB.addLayout(keyGHB2)
        self.keyGrp.setLayout(keyGVB)
        mv.addWidget(self.keyGrp)

        # ================================================================

        self.oprGrp = QtGui.QGroupBox('opreate')
        self.oprGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        self.oprGrp.setMaximumHeight(150)
        oprGVB = QtGui.QVBoxLayout()

        oprGHB1 = QtGui.QHBoxLayout()
        oprbtn_upload = QtGui.QPushButton('upload', self.GWid)
        oprbtn_upload.setFixedHeight(25)
        oprbtn_upload.setStyleSheet(Mstyle.QPushButton(bordRad='12px'))
        oprbtn_upload.setToolTip('open upload window')
        oprGHB1.addWidget(oprbtn_upload)

        oprGHB2 = QtGui.QHBoxLayout()
        oprbtn_confirm = QtGui.QPushButton('confirm', self.GWid)
        oprbtn_confirm.setFixedHeight(25)
        oprbtn_confirm.setStyleSheet(Mstyle.QPushButton(kw='b', bordRad='12px'))
        oprbtn_confirm.setToolTip('open confirm window')
        oprGHB2.addWidget(oprbtn_confirm)

        oprGVB.addLayout(oprGHB1)
        oprGVB.addLayout(oprGHB2)
        self.oprGrp.setLayout(oprGVB)
        mv.addWidget(self.oprGrp)

        #mv.addStretch()


        #self.assetTable.cellPressed.connect(self.cellActiveFn)
        radbtn1.toggled.connect(self.changePictureFn)
        radbtn2.toggled.connect(self.changePictureFn)
        radbtn3.toggled.connect(self.changePictureFn)

        f5button.clicked.connect(self.f5Fn)
        versionbutton.clicked.connect(self.versionChangeFn)
        addbutton.clicked.connect(self.assetAddFn)
        removebutton.clicked.connect(self.assetRemoveFn)
        refbutton.clicked.connect(self.refrenceFn)
        #fixbutton.clicked.connect(self.saveAssetListFn)

        #pastebutton.clicked.connect(self.assetListSaveFn)

        self.keyspin1.valueChanged.connect(self.changeKeyRangeFn)
        self.keyspin2.valueChanged.connect(self.changeKeyRangeFn)
        self.keyspin3.valueChanged.connect(self.changeKeyRangeFn)

        keysetBtn.clicked.connect(self.setKeyframesFn)

        cameraSetBtn.clicked.connect(self.cameraCreateFn)

        oprbtn_upload.clicked.connect(self.oprbtn_openUploadFn)
        oprbtn_confirm.clicked.connect(self.oprbtn_openConfirmFn)

    def oprbtn_openConfirmFn(self):
        if self.treeWid.currentItem():
            itemNode = self.nowSelMainTreeItem

            servSp = self.serverPath.split('\\')
            servSp.append(self.bigType)
            servSp.append(self.departmentName)
            servSp.append(self.nowTreePage)
            servSp.append(self.nowSelMainTreeItem.text(0))
            servSp.append(self.nowSelection)
            servSp.append('uploadTemp')
            servPath = '\\'.join(servSp)
            print servPath
            if os.path.exists(servPath):
                confirm = assetManager_confirmTool_shotDepartment()
                confirm.setParent(self)
                confirm.searchPath = servPath
                confirm.workName = itemNode.text(0)
                confirm.createUI()
                confirm.fillListWidget()
                confirm.localPath = self.localPath
                confirm.serverPath = self.serverPath
                confirm.Op_Ui()
                confirm.BtnA2.setEnabled(True)
                confirm.resize(self.width(), self.height())
                confirm.confirmClicked.connect(self.confirmFn)
                confirm.checkClicked.connect(self.confirmCheckFn)
            else:
                print 'no upload log.can not open confirm dialog'
        else:
            print 'need select item first'

    def getSceneCameraName(self):
        allCam = cmds.ls(type='camera')
        theCam = ''
        for i in allCam:
            if self.nowSelection in i:
                theCam = i
        return theCam

    def showHideHUD(self, switch=True):
        if switch:
            def getArtistName():
                userName = str(self.fileMn.title())
                if userName.lower() == 'login':
                    userName = getpass.getuser()
                return userName

            def getMachineName():
                machineName = getpass.getuser()
                return machineName

            def getDate():
                uploadTime = time.localtime(time.time())
                linedate = time.strftime("%Y-%m-%d %H:%M:%S", uploadTime)
                return linedate

            try:
                cmds.headsUpDisplay('displayCurrentTime', rem=True)
            except:
                pass

            try:
                cmds.headsUpDisplay('displayArtist', rem=True)
            except:
                pass

            try:
                cmds.headsUpDisplay('displayMachine', rem=True)
            except:
                pass

            try:
                cmds.headsUpDisplay('displayDate', rem=True)
            except:
                pass

            cmds.headsUpDisplay('displayCurrentTime', section=5, b=1, blockSize='large', label='currentFrame',
                                labelFontSize='large', pre='currentFrame', dataFontSize='large')
            cmds.headsUpDisplay('displayArtist', section=5, b=2, blockSize='large', label='artist', labelFontSize='large',
                                dataFontSize='large', c=getArtistName)
            cmds.headsUpDisplay('displayMachine', section=5, b=3, blockSize='large', label='machine', labelFontSize='large',
                                dataFontSize='large', c=getMachineName)
            cmds.headsUpDisplay('displayDate', section=5, b=4, blockSize='large', label='date', labelFontSize='large',
                                dataFontSize='large', c=getDate)
        else:
            cmds.headsUpDisplay('displayCurrentTime', rem=True)
            cmds.headsUpDisplay('displayArtist', rem=True)
            cmds.headsUpDisplay('displayMachine', rem=True)
            cmds.headsUpDisplay('displayDate', rem=True)

    def oprbtn_openUploadFn(self):
        cameraName = self.getSceneCameraName()
        if cameraName:
            startKey = int(self.keyspin3.value())
            endKey = int(self.keyspin1.value())
            rangeKey = self.keyspin2.value()
            midKey = int(rangeKey * 0.5) + startKey
            print 'the cut array to input : ' + str([startKey, midKey, endKey])
            self.setKeyframesFn()

            self.showHideHUD()

            submitTool = assetManager_submitTool()
            submitTool.getNotifyFromTxt(self.initPath + '\\maya2016\\' + self.departmentName + '\\notify.txt')
            submitTool.usePlayBlast = True
            submitTool.cutArray = [startKey, midKey, endKey]
            submitTool.cameraName = cameraName
            submitTool.createUI()
            submitTool.setParent(self)
            #submitTool.BtnA2.setVisible(False)
            submitTool.BtnA1.setText('upload_all')
            submitTool.BtnA1.setEnabled(False)
            submitTool.BtnA2.setText('upload_camera')
            submitTool.BtnA2.setEnabled(False)
            submitTool.Op_Ui()
            '''
            animation = QtCore.QPropertyAnimation(submitTool, "geometry")
            animation.setDuration(2000)
            print self.widgetWidth
            print self.widgetHeight
            animation.setStartValue(QtCore.QRect(self.widgetWidth, self.widgetHeight, 800, 800))
            print 's'
            animation.setKeyValueAt(0.7, QtCore.QRect(self.widgetWidth*0.2, self.widgetHeight*0.2, self.widgetWidth, self.widgetHeight))
            print '1'
            animation.setKeyValueAt(0.8, QtCore.QRect(self.widgetWidth*0.1, self.widgetHeight*0.1, self.widgetWidth, self.widgetHeight))
            print '2'
            animation.setEndValue(QtCore.QRect(0, 0, self.widgetWidth, self.widgetHeight))
            print 'e'
            # animation.setEasingCurve(QEasingCurve.OutBounce)
            animation.start()
            print 'run'
            '''
            submitTool.lowClicked.connect(self.oprbtn_uploadFn)
            submitTool.highClicked.connect(self.oprbtn_uploadFn)
            submitTool.resize(self.width(), self.height())
        else:
            cmds.warning('no correct camera in shot : ' + self.nowSelection)

    def AEcalculateFOV(self, camShape):
        import math
        focalStr = camShape + '.focalLength'
        horStr = camShape + '.horizontalFilmAperture'
        focal = cmds.getAttr(focalStr)
        aperture = cmds.getAttr(horStr)
        fov = (0.5 * aperture) / (focal * 0.03937)
        fov = 2.0 * math.atan(fov)
        fov = 57.29578 * fov
        return fov

    def oprbtn_uploadFn(self, data):
        print data

        changeTabItm = self.nowSelMainTreeItem

        reply = QtGui.QMessageBox.information(self,
                                              "double check",
                                              ("upload to\n" + str(changeTabItm.text(0))),
                                              QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        # double check

        if reply == QtGui.QMessageBox.Yes:
            userName = str(self.fileMn.title())
            if userName.lower() == 'login':
                userName = getpass.getuser()

            self.showHideHUD(switch=False)
            # close HUD
            followPathArray = [self.bigType,
                               self.departmentName,
                               self.nowTreePage,
                               self.nowSelMainTreeItem.text(0)
                               ]
            if self.nowSelectionLevel == 1:
                followPathArray.append(self.nowSelection)
            # collection path elements.

            uploadTime = time.localtime(time.time())
            linedate = time.strftime("%Y%m%d%H%M%S", uploadTime)
            # upload Time

            followPathArray.append('uploadTemp')
            followPathArray.append(linedate)
            # collecion path time

            followPathString = '\\'.join(followPathArray)
            fullServerPath = self.serverPath + '\\' + followPathString
            print 'fullServerPath:' + fullServerPath
            fullLocalPath = self.localPath + '\\' + followPathString
            print 'fullLocalPath:' + fullLocalPath
            # combie path,local and server

            if not os.path.exists(fullLocalPath):
                os.makedirs(fullLocalPath)
            # confirm local path

            cmds.select(cl=1)
            cameraName = self.getSceneCameraName()
            cmds.select(cameraName)
            cameraFilePath = fullLocalPath + '\\' + cameraName + '.ma'
            #print 'cameraFilePath:' + cameraFilePath
            cmds.file(cameraFilePath, force=1, options='v=0;', typ='mayaAscii', pr=1, es=1)
            cmds.select(cl=1)
            # camera

            allfileName = self.nowSelection
            allfilePath = fullLocalPath + '\\' + allfileName + '.ma'
            #print 'allfilePath:' + allfilePath
            cmds.file(rename=allfilePath)
            cmds.file(save=True, type='mayaAscii')
            # file

            assetListPath = fullLocalPath + '\\assetList.json'
            self.saveAssetListFn(definedPath=assetListPath)
            # assetList

            countFrame = self.keyspin2.value()
            startFrame = self.keyspin3.value()
            endFrame = self.keyspin1.value()
            fpsTempStr = self.fpsspin.currentText()
            sptemp = fpsTempStr.split(' ')
            fpsStr = sptemp[0]

            keyFramePath = fullLocalPath + '\\keyFrame.json'
            keyDict = {'startKey': startFrame, 'endKey': endFrame, 'length': countFrame, 'fps': fpsTempStr}
            self.saveJson(keyDict, keyFramePath)
            # keyFrame

            previewPath = fullLocalPath + '\\' + cameraName[:-5] + '.avi'
            shutil.copyfile(data[3], previewPath)
            shutil.copystat(data[3], previewPath)
            # preview

            # theAudios = cmds.ls(type='audio')
            # export audio informations

            picturePathArray = []
            for count, i in enumerate(data[1]):
                picPath = fullLocalPath + '\\cutPicture'+str(count)+'.png'
                shutil.copyfile(i, picPath)
                shutil.copystat(i, picPath)
                picturePathArray.append(picPath)
            # preview pictures

            infoUploadPath = fullLocalPath + '\\timeNode.json'
            stringDate = time.strftime("%Y-%m-%d %H:%M:%S", uploadTime)
            dataDict = {'artist': userName, 'date': stringDate, 'machine': getpass.getuser(), 'message': data[2],
                        'type': 'upload'}

            followPathArray = [self.localPath,
                               self.bigType,
                               self.departmentName,
                               self.nowTreePage,
                               self.nowSelMainTreeItem.text(0),
                               self.nowSelection
                               ]
            infoMainPath = '\\'.join(followPathArray) + '\\timeNode.json'
            dict = self.loadJson(infoMainPath)
            dict['lastUpload'] = dataDict
            dict['log'].append(dataDict)
            self.saveJson(dict, infoUploadPath)

            localPathArray = list(picturePathArray)
            localPathArray.append(previewPath)
            localPathArray.append(keyFramePath)
            localPathArray.append(assetListPath)
            localPathArray.append(allfilePath)
            localPathArray.append(cameraFilePath)
            localPathArray.append(infoUploadPath)
            # print 'localPathArray : ' + str(localPathArray)
            if not os.path.exists(fullServerPath):
                os.makedirs(fullServerPath)

            for lpa in localPathArray:
                sp = lpa.replace(fullLocalPath, fullServerPath)
                # print sp
                shutil.copy2(lpa, sp)
            # copy local to server

            iPlanes = cmds.ls(type='imagePlane')

            # ips = cmds.select(iPlanes[0])
            pathArray = {}
            for i in iPlanes:
                thePath = cmds.getAttr(i + '.imageName')
                print thePath
                if ':' in thePath:
                    pathArray.update({i: thePath})
                else:
                    prePath = cmds.workspace(q=True, rd=True)
                    if prePath == '/':
                        cmds.warning('please reset project path')
                    else:
                        pathArray.update({i: prePath + '/' + thePath})


            self.makeLog('upload', uploadTime, userName)

        '''

            producePath = self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + changeTabItm.text(0)
            if not (os.path.exists(producePath)):
                os.makedirs(producePath)
            historypath = producePath + '\\history.html'
            if not (os.path.exists(historypath)):
                self.HTML_CreateEmptyStyle(historypath)
            # make sure produce folder

            innerMsg = '[ ' + self.departmentName + ' ][ upload ] ' + ' <br> updateTime : ' + time.strftime(
                "%Y-%m-%d %H:%M:%S",
                uploadTime) + '<br>update by ' + userName
            htmlMsg = self.HTML_createMsg(innerMsg, userName, '', side=1, initPath=self.initPath)
            self.HTML_addMsg(historypath, htmlMsg)
            # history data update over

            self.loadGeneralPageData()
        '''


    def confirmCheckFn(self, signData):
        pass

    def confirmFn(self, cData):
        followPathArray = [self.serverPath,
                           self.bigType,
                           self.departmentName,
                           self.nowTreePage,
                           self.nowSelMainTreeItem.text(0),
                           self.nowSelection
                           ]

        mainPath = '\\'.join(followPathArray)
        # collection path elements.

        confirmTime = time.localtime(time.time())
        linedate = time.strftime("%Y-%m-%d %H:%M:%S", confirmTime)
        # confirm Time

        tempFilePath = cData[1]
        typeFilterArray = ['avi', 'ma', 'json', 'png']

        mainArray = []
        confirmArray = []
        confirmFiles = os.listdir(tempFilePath)
        for i in confirmFiles:
            spi = i.split('.')
            if spi[-1] in confirmFiles:
                confirmArray.append(tempFilePath + '\\' + i)
                mainArray.append(mainPath + '\\' + i)
        print '---- confirm array ----'
        print confirmArray

        for count,ca in enumerate(confirmArray):
            if os.path.exists(mainArray[count]):
                try:
                    os.remove(mainPathFile)
                except:
                    cmds.warning(mainPathFile + 'cannot update,access denial')
                    continue
            shutil.copy2(confirmArray[count], mainArray[count])

        userName = self.fileMn.title()
        if userName.lower() == 'login':
            ans = cmds.confirmDialog(title='confirm',
                                     m='user not login,do you wanna user machine ID or input by yourself.',
                                     b=['machineID', 'input'], cancelButton='machineID', defaultButton='machineID')
            if ans == 'machineID':
                userName = getpass.getuser()
            elif ans == 'input':
                try:
                    userName = raw_input()
                except EOFError:
                    userName = getpass.getuser()

        tempTimeNode = tempFilePath + '\\timeNode.json'
        mainTimeNode = mainPath + '\\timeNode.json'
        dict = self.loadJson(mainTimeNode)

        dataDict = {'artist': userName, 'date': linedate, 'machine': getpass.getuser(),
                    'message': dict['lastUpload']['message'], 'type': 'confirm'}

        dict['lastConfirm'] = dataDict
        dict['log'].append(dataDict)

        self.saveJson(dict, tempTimeNode)
        self.saveJson(dict, mainTimeNode)

        self.makeLog('confirm', confirmTime, userName)
        self.loadGeneralPageData()
        pathArrayAnimate = [self.serverPath, self.bigType,'ANIMATION', self.nowTreePage, itemNode.text(0)]
        animatePath = '\\'.join(pathArrayAnimate)
        print 'animatePath : ' + animatePath
        #if not os.path.exists(animatePath):
        #    os.makedirs(animatePath)

    def makeLog(self, theType, theTime, theUser, extraMsg = '', pathType='B'):
        PDPathArray = []
        if pathType == 'B':
            PDPathArray = [self.serverPath,
                           self.bigType,
                           'PRODUCE',
                           self.nowTreePage,
                           self.nowSelMainTreeItem.text(0),
                           self.nowSelection
                           ]

        producePath = '\\'.join(PDPathArray)
        if not (os.path.exists(producePath)):
            os.makedirs(producePath)
        historypath = producePath + '\\history.html'
        if not (os.path.exists(historypath)):
            self.HTML_CreateEmptyStyle(historypath)

        regularTime = time.strftime("%Y-%m-%d %H:%M:%S",theTime)

        innerMsg = ''
        if theType == 'confirm':
            innerMsg = '[ ' + self.departmentName + ' ][ confirm ] ' \
                       + ' <br> confirmTime : ' + regularTime \
                       + ' <br> confirm by ' + theUser

        elif theType == 'upload':
            innerMsg = '[ ' + self.departmentName + ' ][ upload ] ' \
                       + ' <br> updateTime : ' + str(regularTime) \
                       + ' <br> update by ' + theUser

        htmlMsg = self.HTML_createMsg(innerMsg, theUser, '', side=1, initPath=self.initPath)
        self.HTML_addMsg(historypath, htmlMsg)
        # history data saved.


    def cameraCreateFn(self):
        fpsTempStr = self.fpsspin.currentText()
        sptemp = fpsTempStr.split(' ')
        fpsStr = sptemp[0]
        valueDict = {'game': '15',
                     'film': '24',
                     'pal': '25',
                     'ntsc': '30',
                     'show': '48',
                     'palf': '50',
                     'ntscf': '60'
                     }

        cameraName = self.nowSelection + '_' + str(self.keyspin3.value()) + 'f_' + str(self.keyspin1.value()) + 'f_fps' + valueDict[fpsStr]

        allCam = cmds.ls(type='camera')
        theCam = ''
        for i in allCam:
            if self.nowSelection in i:
                theCam = i

        if theCam:
            cmds.select(theCam)
        else:
            camFilePath = getAssetManagerPath()['data'] + '\\kupCam.ma'
            if os.path.exists(camFilePath):
                defaultName = 'camera_all_grp'
                cmds.file(camFilePath, i=True, type='mayaAscii')
                import maya.mel as mel
                cmds.select(defaultName)
                mel.eval('searchReplaceNames "camera" "' + cameraName + '" "hierarchy"')


        #camFilePath = getAssetManagerPath()['data'] + '\\kupCam.ma'

    def cameraLinkFn(self):
        allCam = cmds.ls(type='camera')
        theCam = ''
        for i in allCam:
            if self.nowSelection in i:
                theCam = i
                self.cameraSetLab.setText(self.nowSelection)
        if theCam:
            attrArray = ['Camera Name',
                         'Angle of View',
                         'Focal Lenth',
                         'Near Clip Plane',
                         'Far  Clip Plane',
                         'Film Gate',
                         'Film Aspect Ratio Hor',
                         'Film Aspect Ratio Ver'
                         ]

            itm = self.attrTable.item(0, 1)
            itm.setText(theCam)

            FOV = self.AEcalculateFOV(theCam)
            itm = self.attrTable.item(1, 1)
            itm.setText(str(FOV))

            focalLenth = cmds.getAttr(theCam + '.focalLength')
            itm = self.attrTable.item(2, 1)
            itm.setText(str(focalLenth))

            nClip = cmds.getAttr(theCam + '.nearClipPlane')
            itm = self.attrTable.item(3, 1)
            itm.setText(str(nClip))

            fClip = cmds.getAttr(theCam + '.farClipPlane')
            itm = self.attrTable.item(4, 1)
            itm.setText(str(fClip))


            horAperture = cmds.getAttr(theCam + '.horizontalFilmAperture')
            itm = self.attrTable.item(5, 1)
            itm.setText(str(horAperture))

            verAperture = cmds.getAttr(theCam + '.verticalFilmAperture')
            itm = self.attrTable.item(6, 1)
            itm.setText(str(verAperture))

        '''
        for count, aa in enumerate(attrArray):
            itm = self.attrTable.item(count,1)

            itm.setText(attrArray[i])
        '''

    def saveAssetListFn(self,definedPath=''):
        #print self.nowSelectionToolTip
        #self.assetListPath = self.nowSelectionToolTip + '\\assetList.json'

        filePath = ''
        if definedPath:
            filePath = definedPath
        else:
            filePath = self.assetListPath

        if not os.path.exists(filePath):
            emptyArray = []
            self.saveJson(emptyArray, filePath)

        #jsonArray = self.loadJson(self.assetListPath)
        jsonArray = []
        nowRC = self.assetTable.rowCount() - 1
        for i in range(nowRC):
            nameItm = self.assetTable.item(i, 2)
            if nameItm:
                jsonArray.append(nameItm.toolTip())
        if jsonArray:
            self.saveJson(jsonArray, filePath)

    def setKeyframesFn(self):
        countFrame = self.keyspin2.value()
        startFrame = self.keyspin3.value()
        endFrame = self.keyspin1.value()
        fpsTempStr = self.fpsspin.currentText()
        sptemp = fpsTempStr.split(' ')
        fpsStr = sptemp[0]

        cmds.currentUnit(time=fpsStr)
        cmds.playbackOptions(max=endFrame)
        cmds.playbackOptions(aet=endFrame)
        cmds.playbackOptions(min=0)
        cmds.playbackOptions(ast=startFrame)
        cmds.warning('fps set to ' + fpsTempStr)

        keyDict = {'startKey': startFrame, 'endKey': endFrame, 'length': countFrame, 'fps': fpsTempStr}
        self.saveJson(keyDict, self.keyFramePath)


        theCam = self.getSceneCameraName()
        if theCam:
            theCamGrp = theCam[:-5] + '_all_grp'
            valueDict = {'game': '15',
                         'film': '24',
                         'pal': '25',
                         'ntsc': '30',
                         'show': '48',
                         'palf': '50',
                         'ntscf': '60'
                         }
            newName = self.nowSelection + '_' + str(startFrame) + 'f_' + str(endFrame) + 'f_fps' + valueDict[fpsStr]
            import maya.mel as mel
            cmds.select(cl=1)
            cmds.select(theCamGrp)
            mel.eval('searchReplaceNames "' + theCam[:-5] + '" "' + newName + '" "hierarchy"')
            cmds.select(newName)
        else:
            cmds.warning('no correct camera in shot : ' + self.nowSelection)

    def changeKeyRangeFn(self):
        sender = self.sender()
        senderType = sender.toolTip()
        startVal = self.keyspin3.value()
        endVal = self.keyspin1.value()
        countVal = self.keyspin2.value()

        if str(senderType) in ['time range start','time range end']:
            if endVal <= startVal:
                endVal = startVal + 1

            newCount = endVal - startVal
            self.keyspin2.setValue(newCount)

        elif senderType == 'time range count':
            newEnd = startVal + countVal
            self.keyspin1.setValue(newEnd)

    def changePictureFn(self):
        if self.bGrp.checkedId()!= self.lastCheckID:
            self.lastCheckID = self.bGrp.checkedId()
            print self.bGrp.checkedId()
            self.picLab.setText('picture ' + str(self.lastCheckID))

    def assetRemoveFn(self):
        cr = self.assetTable.currentRow()
        self.assetTable.removeRow(cr)
        self.saveAssetListFn()


    '''
    def assetListSaveFn(self):
        if self.nowSelectionLevel == 1:
            nowRC = self.assetTable.rowCount()-1
            dataArray = []
            for i in range(nowRC):
                cellDict = {'dep': '', 'type': '', 'assetName': '', 'toolTip': '', 'ver': '', 'refNode': ''}
    
                nameItm = self.assetTable.item(i, 2)
                cellDict['assetName'] = nameItm.text()
                cellDict['toolTip'] = nameItm.toolTip()
    
                depItm = self.assetTable.item(i, 0)
                cellDict['dep'] = depItm.text()
    
                typeItm = self.assetTable.item(i, 1)
                cellDict['type'] = typeItm.text()
    
                verItm = self.assetTable.item(i, 3)
                cellDict['ver'] = verItm.text()
    
                refItm = self.assetTable.item(i, 4)
                cellDict['refNode'] = refItm.toolTip()
    
                dataArray.append(cellDict)
        print dataArray
        print self.nowSelectionToolTip
        print self.nowSelectionLevel
    '''

    def versionChangeFn(self):
        cr = self.assetTable.currentRow()
        verItm = self.assetTable.item(cr, 3)
        checkItm = self.assetTable.item(cr, 4)
        nameItm = self.assetTable.item(cr, 2)
        nameToolTip = nameItm.toolTip()
        ver = verItm.text()
        newVer = 'high'
        newToolTip = ''
        refNode = checkItm.toolTip()
        #print nameToolTip
        #print ver
        #print 'ver change: '
        if ver == 'high':
            newVer = 'low'
            newToolTip = nameToolTip.replace('_high.', '_low.')
        else:
            newToolTip = nameToolTip.replace('_low.', '_high.')

        #print newVer
        #print newToolTip
        #print refNode
        verItm.setText(newVer)
        nameItm.setToolTip(newToolTip)

        self.assetTable.setItem(cr, 3, verItm)
        self.assetTable.setItem(cr, 2, nameItm)
        cmds.file(newToolTip, loadReference=refNode)
        #references = cmds.ls(type='reference')
        #print references
        #print ''
        self.f5Fn()
        self.saveAssetListFn()

    def isCharactorInFile(self,itm):
        references = cmds.ls(type='reference')
        returnStr = ['no',False]
        refDict = {}
        refArray = []
        for r in references:
            try:
                ref = cmds.referenceQuery(r, filename=True)
                refDict.update({ref:r})
                #print 'ref : ' + ref
                refArray.append(ref)

            except:
                pass
        #W:/project/PIG/asset/RIG/Char/AnQi/PIG_cha_AnQi_rig_low.ma
        theToolTip = itm.toolTip()

        tt = os.path.dirname(theToolTip)
        sptt = tt.split('\\')

        thePath = '/'.join(sptt)
        theName = os.path.basename(theToolTip)

        for re in refArray:
            rePath = os.path.dirname(re)
            if thePath == rePath:
                theNode = refDict[re]
                returnStr = ['dif', theNode]
                reName = os.path.basename(re)
                if '{' and '}' in reName:
                    reName = reName.split('{')[0]
                    #print 'fix name:' + theName
                if reName == theName:
                    returnStr = ['yes', theNode]
                    break

        return returnStr

    def f5Fn(self):
        nowRC = self.assetTable.rowCount()-1
        for rc in range(nowRC):
            checkItm = self.assetTable.item(rc, 2)
            isExists = self.isCharactorInFile(checkItm)
            print 'isExists : ' + str(isExists)
            theItm = self.assetTable.item(rc, 4)
            if isExists[0] == 'yes':
                theItm.setBackground(QtGui.QBrush(QtGui.QColor(95, 175, 17)))
                theItm.setForeground(QtGui.QBrush(QtGui.QColor(50, 50, 50)))
            elif isExists[0] == 'no':
                theItm.setBackground(QtGui.QBrush(QtGui.QColor(235, 75, 57)))
                theItm.setForeground(QtGui.QBrush(QtGui.QColor(50, 50, 50)))
            elif isExists[0] == 'dif':
                theItm.setBackground(QtGui.QBrush(QtGui.QColor(207, 200, 16)))
                theItm.setForeground(QtGui.QBrush(QtGui.QColor(50, 50, 50)))
            theItm.setText(isExists[0])
            theItm.setToolTip(str(isExists[1]))
            #print isExists[1]


    def refrenceFn(self):
        cr = self.assetTable.currentRow()+1
        if cr:
            theItm = self.assetTable.item(cr-1, 2)
            if theItm:
                theToolTip = theItm.toolTip()
                theBaseName = os.path.basename(theToolTip)
                spBaseName = theBaseName.split('_')
                theName = spBaseName[2]
                theType = spBaseName[3]
                cmds.file(theToolTip, reference=True, type='mayaAscii', namespace=theName + '_' + theType)
            self.f5Fn()

    def assetAddFn(self):
        theUI = selectCharactor_ANIM_TOOL()
        theUI.serverPath = self.serverPath
        theUI.setParent(self)
        theUI.Op_Ui()
        theUI.resize(self.width(), self.height())
        theUI.move(0, 0)
        theUI.addClicked.connect(self.assetAdditemFn)

    def assetAdditemFn(self, sig):
        #print 'assetAdditmFn sig: ' + sig
        nowRow = self.assetTable.rowCount()
        baseName = os.path.basename(sig)
        isDiffrent = True
        for i in range(nowRow):
            checkItm = self.assetTable.item(i, 2)
            if checkItm:
                checkName = checkItm.toolTip()
                if checkName == sig:
                    isDiffrent = False

        if isDiffrent:
            self.assetTable.setRowCount(nowRow+1)
            spBn = baseName.split('_')

            nameItm = QtGui.QTableWidgetItem()
            nameItm.setText(spBn[2])
            nameItm.setTextAlignment(Qt.AlignCenter)
            nameItm.setToolTip(sig)
            self.assetTable.setItem(nowRow-1, 2, nameItm)

            typeDict = {'cha': QtGui.QBrush(QtGui.QColor(108, 166, 128)),
                        'prop': QtGui.QBrush(QtGui.QColor(108, 121, 128)),
                        'env': QtGui.QBrush(QtGui.QColor(143, 116, 89))}
            typeItm = QtGui.QTableWidgetItem()
            typeItm.setText(spBn[1])
            typeItm.setTextAlignment(Qt.AlignCenter)
            self.assetTable.setItem(nowRow-1, 1, typeItm)
            typeItm.setBackground(typeDict[spBn[1]])


            depDict = {'rig': QtGui.QBrush(QtGui.QColor(108, 86, 108)),
                        'mod': QtGui.QBrush(QtGui.QColor(70, 64, 128))}
            depItm = QtGui.QTableWidgetItem()
            depItm.setText(spBn[3])
            depItm.setTextAlignment(Qt.AlignCenter)
            self.assetTable.setItem(nowRow-1, 0, depItm)
            depItm.setBackground(depDict[spBn[3]])

            verItm = QtGui.QTableWidgetItem()
            verItm.setText(spBn[4].split('.')[0])
            verItm.setTextAlignment(Qt.AlignCenter)
            self.assetTable.setItem(nowRow - 1, 3, verItm)

            stateItm = QtGui.QTableWidgetItem()
            stateItm.setTextAlignment(Qt.AlignCenter)
            self.assetTable.setItem(nowRow - 1, 4, stateItm)

            isExists = self.isCharactorInFile(nameItm)
            if isExists[0] == 'yes':
                stateItm.setBackground(QtGui.QBrush(QtGui.QColor(95, 175, 17)))
                stateItm.setForeground(QtGui.QBrush(QtGui.QColor(50, 50, 50)))
            elif isExists[0] == 'no':
                stateItm.setBackground(QtGui.QBrush(QtGui.QColor(235, 75, 57)))
                stateItm.setForeground(QtGui.QBrush(QtGui.QColor(50, 50, 50)))
            elif isExists[0] == 'dif':
                stateItm.setBackground(QtGui.QBrush(QtGui.QColor(207, 200, 16)))
                stateItm.setForeground(QtGui.QBrush(QtGui.QColor(50, 50, 50)))
            stateItm.setText(isExists[0])
            stateItm.setToolTip(str(isExists[1]))
            self.saveAssetListFn()
        else:
            cmds.warning('same itm,skip')

    def createConceptTab(self):
        ConceptWid = QtGui.QWidget()
        ConceptWid.setAttribute(Qt.WA_StyledBackground)
        ConceptWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        ConceptWid.setAttribute(Qt.WA_DeleteOnClose)

        self.conceptHbox = QtGui.QGridLayout()

        ConceptWid.setLayout(self.conceptHbox)
        self.tabWid.addTab(ConceptWid, 'storyBoard')

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
        self.qweb.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)

        hisVB.addWidget(blanklabelup)
        hisVB.addWidget(self.qweb)
        hisVB.addWidget(blanklabelbelow)
        hisWid.setLayout(hisVB)
        self.qweb.linkClicked.connect(self.linkFn)

    def createCameraAssistTab(self):
        cameraAssistWid = QtGui.QWidget()
        cameraAssistWid.setAttribute(Qt.WA_StyledBackground)
        cameraAssistWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        cameraAssistWid.setAttribute(Qt.WA_DeleteOnClose)
        self.tabWid.addTab(cameraAssistWid, 'camera')

        mv = QtGui.QVBoxLayout()
        cameraAssistWid.setLayout(mv)

        h1 = QtGui.QHBoxLayout()
        self.cameraSetLab = QtGui.QLabel('null', cameraAssistWid)
        self.cameraSetLab.setFixedHeight(20)
        self.cameraSetLab.setStyleSheet(Mstyle.QPushButton(kw='b', bordRad='10px'))
        self.cameraSetLab.setToolTip('open confirm window')
        h1.addWidget(self.cameraSetLab)

        mv.addLayout(h1)

        attrArray = ['Camera Name',
                     'Angle of View',
                     'Focal Lenth',
                     'Near Clip Plane',
                     'Far  Clip Plane',
                     'Film Gate',
                     'Film Aspect Ratio Hor',
                     'Film Aspect Ratio Ver',
                     ]

        self.attrTable = QtGui.QTableWidget()
        mv.addWidget(self.attrTable)
        self.attrTable.setStyleSheet(Mstyle.QTabWidget())
        self.attrTable.setColumnCount(3)

        self.attrTable.setRowCount(len(attrArray))
        for i in range(len(attrArray)):
            self.attrTable.setRowHeight(i, 20)
            attr = attrArray[i]
            itm = QtGui.QTableWidgetItem()
            itm.setText(attrArray[i])
            self.attrTable.setItem(i, 0, itm)

            dataitm = QtGui.QTableWidgetItem()
            dataitm.setText('0')
            self.attrTable.setItem(i, 1, dataitm)

            if attr == 'Film Gate':
                dataitm = QtGui.QComboBox()
                comboList = ['User',
                             '16mm Theatrical',
                             'Super 16mm',
                             '35mm Academy',
                             '35mm TV Projection',
                             '35mm Full Aperture',
                             '35mm 1.85 Projection',
                             '35mm Anamorphic',
                             '70mm Projection',
                             'VistaVision',
                             'Imax'
                             ]
                dataitm.addItems(comboList)
                self.attrTable.setCellWidget(i, 1, dataitm)
            else:
                pass
        self.attrTable.setHorizontalHeaderLabels(['attribute', 'value', 'others'])
        self.attrTable.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Stretch)

        self.attrTable.setColumnWidth(0, 130)
        self.attrTable.setColumnWidth(2, 40)

        h2 = QtGui.QHBoxLayout()
        cameraSetBtn = QtGui.QPushButton('camera create/select/connect/refresh', cameraAssistWid)
        cameraSetBtn.setFixedHeight(20)
        cameraSetBtn.setStyleSheet(Mstyle.QPushButton(kw='b', bordRad='10px'))
        cameraSetBtn.setToolTip('open confirm window')
        h2.addWidget(cameraSetBtn)

        mv.addLayout(h2)


        '''
        attributeGrp = QtGui.QGroupBox('Attribute')
        mv.addWidget(attributeGrp)
        attributeGrp.setStyleSheet(Mstyle.QGroupBox(kw = 'b'))
        grpVbox = QtGui.QVBoxLayout()
        attributeGrp.setLayout(grpVbox)

        h1 = QtGui.QHBoxLayout()
        attr1Lab = QtGui.QLabel('attr1')
        h1.addWidget(attr1Lab)

        text1 = QtGui.QLineEdit()
        h1.addWidget(text1)
        grpVbox.addLayout(h1)
        '''
        cameraSetBtn.clicked.connect(self.cameraLinkFn)

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
        itemNode = self.nowSelMainTreeItem

        followPathArray = [self.bigType,
                           self.departmentName,
                           self.nowTreePage,
                           self.nowSelMainTreeItem.text(0)
                           ]
        if self.nowSelectionLevel == 1:
            followPathArray.append(self.nowSelection)
        else:
            followPathArray.append('dataFolder')
        followPathArray.append('note')
        followPathArray.append(self.comLE.currentItem().toolTip())

        followPathString = '\\'.join(followPathArray)

        filedata = ''
        noteDir = self.serverPath + '\\' + followPathString
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
        followPathArray = [self.bigType,
                           self.departmentName,
                           self.nowTreePage,
                           self.nowSelMainTreeItem.text(0)
                           ]
        if self.nowSelectionLevel == 1:
            followPathArray.append(self.nowSelection)
        else:
            followPathArray.append('dataFolder')
        followPathArray.append('note')

        followPathString = '\\'.join(followPathArray)

        TEmain = assetManager_writterUI()
        TEmain.itemName = self.nowSelection
        TEmain.savePath = self.serverPath + '\\' + followPathString
        TEmain.initUI()
        TEmain.setParent(self)
        TEmain.move(0, 0)
        TEmain.resize(self.width(), self.height())
        TEmain.saveSignal.connect(self.writterSavedFn)
        TEmain.show()

    def writterSavedFn(self, data):
        # print data
        self.loadNoteListData()

    def createTree(self):
        self.vWid = QtGui.QWidget()
        self.vWid.setMinimumWidth(self.widgetWidth * 0.1)
        self.vWid.resize(self.widgetWidth * 0.5, self.widgetWidth - self.L2)

        vBox = QtGui.QVBoxLayout()
        vBox.setSpacing(0)
        vBox.setContentsMargins(0, 0, 0, 0)
        '''
        radHBox = QtGui.QHBoxLayout()

        rad1 = QtGui.QPushButton('sequence')
        rad1.setFixedHeight(25)
        rad1.setStyleSheet(Mstyle.QPushButton(kw='radiobutton', bordRad='6px'))
        rad1.setAutoExclusive(True)
        rad1.setCheckable(True)
        rad1.setToolTip('sequence page')
        rad1.setChecked(True)
        radHBox.addWidget(rad1)

        rad2 = QtGui.QPushButton('others')
        rad2.setFixedHeight(25)
        rad2.setStyleSheet(Mstyle.QPushButton(kw='radiobutton', bordRad='6px'))
        rad2.setAutoExclusive(True)
        rad2.setCheckable(True)
        rad2.setToolTip('others page')
        radHBox.addWidget(rad2)

        self.radGrp = QtGui.QButtonGroup()
        self.radGrp.setExclusive(True)
        self.radGrp.addButton(rad1, 0)
        self.radGrp.addButton(rad2, 1)
        '''
        leftComboBox = QtGui.QComboBox()
        leftComboPath = self.serverPath + '\\' + self.bigType + '\\' + self.departmentName
        leftComboFolders = self.getFolders(leftComboPath)
        self.nowTreePage = leftComboFolders[0]
        leftComboBox.addItems(leftComboFolders)

        LE = QtGui.QLineEdit()
        LE.setAlignment(Qt.AlignHCenter)
        LE.setStyleSheet(Mstyle.QLineEdit(kw='d', lang='c'))


        self.treeWid = assetManager_commonRightClickTreeWidget()
        self.treeWid.verticalScrollBar().setStyleSheet(Mstyle.QScrollBar())
        self.treeWid.setStyleSheet(Mstyle.QTreeWidget())
        self.treeWid.setup()
        self.treeWid.setSortingEnabled(True)
        self.treeWid.setHeaderHidden(1)
        self.treeWid.addButton('add scene', 'brush.png')
        self.treeWid.addButton('add shot', 'brush.png')
        self.treeWid.addButton('open shot', 'file.png', lv=1)
        self.treeWid.addButton('reference shot', 'file.png', lv=1)
        self.treeWid.addButton('insert shot', 'brush.png', lv=1)
        self.treeWid.addButton('delete select', 'cross.png', lv=1)
        self.treeWid.addButton('copy asset list', 'file.png', lv=1)
        self.treeWid.addButton('paste asset list', 'file.png', lv=1)
        self.treeWid.addButton('refresh', 'file.png')

        self.createTreeList(page=self.nowTreePage)

        projectLabel = QtGui.QLabel()
        projectLabel.setText(self.projectName)
        projectLabel.setStyleSheet(Mstyle.QLabel(fontSize='32px') + 'QLabel {color:rgb(20,20,20)}')
        projectLabel.setFixedHeight(32)
        projectLabel.setAlignment(Qt.AlignCenter)


        #vBox.addLayout(radHBox)
        vBox.addWidget(leftComboBox)
        vBox.addWidget(LE)
        vBox.addWidget(self.treeWid)
        vBox.addWidget(projectLabel)
        #self.leftArray = [LE, rad1, rad2]  # [LE, rad1, rad2, rad3]
        self.vWid.setLayout(vBox)

        self.treeWid.choosed.connect(self.treeActionFn)
        self.treeWid.currentItemChanged.connect(self.treeWidChangedFn)
        LE.textChanged.connect(self.LEtextChangedFn)
        #rad2.clicked.connect(self.leftComboboxChangeFn)
        #rad1.clicked.connect(self.leftComboboxChangeFn)
        leftComboBox.currentIndexChanged[str].connect(self.leftComboboxChangeFn)

        self.treeWid.setCurrentItem(self.treeWid.itemAt(0, 0))
        return self.vWid

    def treeActionFn(self, theStr):
        actionLogPath = self.serverPath + '\\' + self.bigType + '\\PRODUCE\\log\\' + self.departmentName + '\\listAction'
        if not os.path.exists(actionLogPath):
            os.makedirs(actionLogPath)
        jsonLogFile = '\\listAction.json'
        if not os.path.exists(actionLogPath + jsonLogFile):
            print 'not exists'
            emptyArray = []
            self.saveJson(emptyArray, actionLogPath + jsonLogFile)
        logJson = self.loadJson(actionLogPath + jsonLogFile)
        # load list action informations

        nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        userName = self.fileMn.title()
        if userName.lower() == 'login':
            userName = getpass.getuser()
        # load time and user informations

        currentPath = self.treeWid.currentItem().toolTip(0)
        spPath = currentPath.split(os.sep)

        if theStr == 'add scene':
            scName = spPath[-1]
            sqName = spPath[-2]
            nowLevel = [self.serverPath, self.bigType, self.departmentName, self.nowTreePage]

            treeCount = self.treeWid.topLevelItemCount()
            strCount = str(treeCount+1).zfill(2)
            newScName = 'sc' + strCount
            nowLevel.append(newScName)
            newPath = '\\'.join(nowLevel)
            if not os.path.exists(newPath):
                os.makedirs(newPath)
                self.createTreeList(page=self.nowTreePage)
                os.makedirs(newPath + '\\dataFolder')
                dataDict = {'user': userName,
                            'type': theStr,
                            'scene': scName,
                            'sequence': sqName,
                            'shot': '',
                            'date': nowTime}

                logJson.append(dataDict)
            else:
                cmds.warning(newScName + ' was already exists!!')

        if theStr == 'add shot':
            scName = spPath[-1]
            sqName = spPath[-2]
            if self.treeWid.currentItem():
                seqName = self.treeWid.currentItem().text(0)
                nowLevel = self.nowSelectionToolTip.split('\\')[:-1]
                nowLevel.append(seqName)
                # print nowLevel

                ans = QtGui.QMessageBox.information(self,'direction select',
                                              'do you want to use default set?',
                                              QtGui.QMessageBox.Yes,
                                              QtGui.QMessageBox.No)

                isContunie = False
                removeArray = []

                if ans == QtGui.QMessageBox.Yes:
                    addNumber, adok = QtGui.QInputDialog.getInt(self, sqName,
                                                             'how many new shots you want \n add to >> ' + scName + ' <<',
                                                             1, 1,
                                                             100000, 1)

                    if adok:
                        currentRule = '%SQ_%SC_sh%NUM'
                        nameString = str(currentRule)

                        if '%SQ' in nameString:
                            nameString = nameString.replace('%SQ', sqName)

                        if '%SC' in nameString:
                            nameString = nameString.replace('%SC', scName)

                        removeArray = nameString.split('%NUM')

                        fullLength = 4
                        offset = 1
                        offsetStr = ''
                        if offset:
                            offsetStr = '0'.zfill(offset)
                        isContunie = True
                else:
                    currentRule, ok1 = QtGui.QInputDialog.getText(self, 'name format',
                                      'please type in the name format\n %SQ : use sequence name\n %SC : use scene name '
                                      '\n %NUM : means shot number \n eg. %SQ_%SC_sh%NUM',
                                      QtGui.QLineEdit.Normal,
                                      '%SQ_%SC_sh%NUM'
                                      )
                    if ok1:
                        fullLength, ok2 = QtGui.QInputDialog.getInt(self, 'length of number',
                                          'type in length of number',4,1,10,1
                                          )
                        if ok2:
                            offset, ok3 = QtGui.QInputDialog.getInt(self, 'offset of number',
                                              'type in offset of number\n 1 : 00052 -> 00520\n 2 : 00052 -> 05200',1,0,fullLength-3,1
                                              )
                            if ok3:
                                addNumber, ok4 = QtGui.QInputDialog.getInt(self, seqName, 'how many new shots you want \n add to >> ' + seqName + ' <<', 1, 1,
                                                                         100000, 1)

                                if ok4:
                                    offsetStr = ''
                                    if offset:
                                        offsetStr = '0'.zfill(offset)

                                    nameString = str(currentRule)

                                    if '%SQ' in nameString:
                                        nameString = nameString.replace('%SQ', sqName)

                                    if '%SC' in nameString:
                                        nameString = nameString.replace('%SC', scName)

                                    removeArray = nameString.split('%NUM')

                                    isContunie = True

                # removeArray
                # addNumber
                # nameString
                # offsetStr
                # offset
                # fullLenth
                # get all key attributes
                if isContunie:
                    startNumber = 1
                    endNumber = addNumber + 1
                    cCount = self.treeWid.currentItem().childCount()
                    if cCount:
                        maxNumber = 0
                        for i in range(cCount):
                            cName = str(self.treeWid.currentItem().child(i).text(0))
                            for rm in removeArray:
                                cName = cName.replace(str(rm), '')
                                print 'loop cName : ' + cName
                            print 'final cName : ' + cName
                            number = int(cName)
                            if maxNumber < number:
                                maxNumber = number
                        startNumber = int(str(maxNumber)[:-1]) + 1
                        endNumber = startNumber + addNumber

                    for num in range(startNumber, endNumber):
                        strNumber = str(num).zfill(fullLength - offset) + offsetStr
                        finalName = nameString.replace('%NUM', strNumber)
                        finalPath = currentPath + os.sep + finalName
                        print 'final path : ' + finalPath
                        os.makedirs(finalPath)
                        dataDict = {'user': userName,
                                    'type': theStr,
                                    'scene': scName,
                                    'sequence': sqName,
                                    'shot': finalName,
                                    'date': nowTime}
                        logJson.append(dataDict)
                # use the key attributes to slove the result.

        if theStr == 'refresh':
            self.createTreeList(page=self.nowTreePage)

        if theStr == 'insert shot':
            scName = spPath[-2]
            sqName = spPath[-3]
            addname, ok = QtGui.QInputDialog.getText(self, 'inputName',
                                                          'please type in the name',
                                                          QtGui.QLineEdit.Normal,
                                                          '%SQ_%SC_sh%NUM'
                                                          )
            if ok:
                print currentPath
                subSp = spPath[:-1]
                subSp.append(addname)
                inserPath = os.sep.join(subSp)
                if os.path.exists(inserPath):
                    cmds.warning(addname + ' is exists.')
                else:
                    os.makedirs(inserPath)
                    dataDict = {'user': userName,
                                'type': theStr,
                                'scene': scName,
                                'sequence': sqName,
                                'shot': addname,
                                'date': nowTime}
                    logJson.append(dataDict)

        if theStr == 'delete select':

            shotName = spPath[-1]
            scName = spPath[-2]
            sqName = spPath[-3]
            if os.path.exists(currentPath):
                shutil.rmtree(currentPath)
                dataDict = {'user': userName,
                            'type': theStr,
                            'scene': scName,
                            'sequence': sqName,
                            'shot': shotName,
                            'date': nowTime}
                logJson.append(dataDict)

        exArray = []
        for en in range(self.treeWid.topLevelItemCount()):
            itm = self.treeWid.topLevelItem(en)
            check = itm.isExpanded()
            if check:
                exArray.append(en)

        self.createTreeList(page=self.nowTreePage)

        for en in exArray:
            itm = self.treeWid.topLevelItem(en)
            self.treeWid.setItemExpanded(itm, True)
        self.saveJson(logJson, actionLogPath + jsonLogFile)

    def createTreeList(self, page=''):
        allowArray = ['ma']
        lv1Path = self.serverPath + '\\' + self.bigType + '\\' + self.departmentName + '\\' + page
        folders = self.getFolders(path=lv1Path)
        defaultSize = QtCore.QSize(18, 18)
        self.treeWid.clear()
        for f in folders:
            itm = QtGui.QTreeWidgetItem()
            itm.setText(0, f)
            itm.setSizeHint(0, defaultSize)
            lv2Path = lv1Path + '\\' + f
            itm.setToolTip(0, lv2Path)
            files = self.getFolders(lv2Path)
            if files:
                if 'dataFolder' in files:
                    files.remove('dataFolder')
                #files = sorted(files, key=lambda x: int(x[5:]))
                for fl in files:

                    subitm = QtGui.QTreeWidgetItem()
                    subitm.setText(0, fl)
                    subitm.setSizeHint(0, defaultSize)
                    lv3Path = lv2Path + '\\' + fl
                    subitm.setToolTip(0, lv3Path)
                    itm.addChild(subitm)
            itm.sortChildren(1, Qt.AscendingOrder)
            self.treeWid.addTopLevelItem(itm)

    # ------ button functions ------------------------------

    def leftComboboxChangeFn(self,theStr):

        nowsel = str(theStr)

        self.createTreeList(page=nowsel)
        self.nowTreePage = nowsel


    def treeWidChangedFn(self):
        sender = self.sender()
        itm = sender.currentItem()
        # print itm.text(0)
        if itm:
            self.nowSelection = itm.text(0)
            self.nowSelectionToolTip = itm.toolTip(0)
            self.assetListPath = self.nowSelectionToolTip + '\\assetList.json'
            self.keyFramePath = self.nowSelectionToolTip + '\\keyFrame.json'
            tempParent = itm
            self.nowSelectionLevel = 0
            for i in range(5):
                tempParent = tempParent.parent()
                if tempParent:
                    self.nowSelectionLevel += 1
                else:
                    break
            #self.loadGeneralPageData()
            #print self.nowSelection
            #if self.isTab:
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
            #print 'gen'
        elif nowItem == 'note':
            self.loadNoteListData()
        elif nowItem == 'history':
            self.loadHTMLHistoryData()
        elif nowItem == 'storyBoard':
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

        if self.nowSelectionLevel == 1:
            # shot level
            sptt = self.nowSelectionToolTip.split('\\')
            print sptt
            self.seqTitle.setText(sptt[-2])
            self.shotTitle.setText(sptt[-1])




            self.imageTable.setTabEnabled(0, False)
            self.imageTable.setTabEnabled(1, True)
            self.imageTable.setTabEnabled(2, True)
            self.infoTable.setTabEnabled(0, False)
            self.infoTable.setTabEnabled(1, False)
            self.infoTable.setTabEnabled(2, True)
            self.infoTable.setTabEnabled(3, True)
            self.oprGrp.setVisible(True)
            self.oprGrp.setFixedHeight(80)
            self.keyGrp.setVisible(True)
            self.keyGrp.setFixedHeight(80)

            self.animation1 = QtCore.QPropertyAnimation(self.keyGrp, "pos")
            self.animation1.setDuration(200)

            bx1 = self.keyGrp.x()
            byval = self.oprGrp.y()-90
            #byval = by1 -20
            #print by1
            self.animation1.setStartValue(QtCore.QPoint(-300, byval))
            self.animation1.setKeyValueAt(0.5, QtCore.QPoint(15, byval))
            self.animation1.setEndValue(QtCore.QPoint(bx1, byval))
            #self.animation.setEasingCurve(QtCore.QEasingCurve.OutBounce)
            self.animation1.start()


            self.animation = QtCore.QPropertyAnimation(self.oprGrp, "pos")
            self.animation.setDuration(250)

            bx = self.oprGrp.x()
            by = self.oprGrp.y()
            self.animation.setStartValue(QtCore.QPoint(-300, by))
            self.animation.setKeyValueAt(0.1, QtCore.QPoint(-300, by))
            self.animation.setKeyValueAt(0.6, QtCore.QPoint(15, by))
            self.animation.setEndValue(QtCore.QPoint(bx, by))
            #self.animation.setEasingCurve(QtCore.QEasingCurve.OutBounce)
            self.animation.start()
            # show and hide over

            #self.assetListPath = self.nowSelectionToolTip + '\\assetList.json'
            self.assetTable.clear()
            self.assetTable.setRowCount(1)
            self.assetTable.setHorizontalHeaderLabels(['dep','type', 'assetName', 'ver','ref'])

            if os.path.exists(self.assetListPath):
                assetListArray = self.loadJson(self.assetListPath)
                for asa in assetListArray:
                    print asa
                    self.assetAdditemFn(asa)
            else:
                print 'no asset list to load'
                self.assetTable.setRowCount(1)



            #self.keyFramePath = self.nowSelectionToolTip + '\\keyFrame.json'
            keyFrameDict = {'startKey': 100, 'endKey': 200, 'length': 100, 'fps': 'film : 24 fps'}
            if not os.path.exists(self.keyFramePath):
                self.saveJson(keyFrameDict, self.keyFramePath)
            keyFrameDict = self.loadJson(self.keyFramePath)

            self.keyspin1.setValue(keyFrameDict['endKey'])
            self.keyspin2.setValue(keyFrameDict['length'])
            self.keyspin3.setValue(keyFrameDict['startKey'])

            fpsIdex = 0
            for index, itm in enumerate(self.fpsList):
                if keyFrameDict['fps'] in itm:
                    fpsIdex = index
            self.fpsspin.setCurrentIndex(fpsIdex)

            infoMainPath = self.nowSelectionToolTip + '\\timeNode.json'
            isExt = os.path.exists(infoMainPath)

            art = ''
            passs = ''
            sDate = ''
            cDate = ''
            uDate = ''
            machin = ''
            msg = ''

            if isExt:
                dict = self.loadJson(infoMainPath)
                mainData = dict['log']
                if mainData:
                    art = mainData[-1]['artist']
                    msg = mainData[-1]['message']
                    machin = mainData[-1]['machine']
                    sDate = dict['firstDownload']['date']
                    cDate = dict['lastConfirm']['date']
                    uDate = dict['lastUpload']['date']

            else:

                emptyDict = {
                    'lastUpload': {'type': '', 'artist': '', 'message': '', 'machine': '', 'date': ''},
                    'lastDownload': {'type': '', 'artist': '', 'message': '', 'machine': '', 'date': ''},
                    'firstDownload': {'type': '', 'artist': '', 'message': '', 'machine': '', 'date': ''},
                    'lastConfirm': {'type': '', 'artist': '', 'message': '', 'machine': '', 'date': ''},
                    'lastWriteNote': {'type': '', 'artist': '', 'message': '', 'machine': '', 'date': ''},
                    'lastReadNote': {'type': '', 'artist': '', 'message': '', 'machine': '', 'date': ''},
                    'log': [],
                    'state': ''}
                self.saveJson(emptyDict, infoMainPath)

            self.updatedatelab.setText(uDate)
            self.artistlab.setText(art)
            self.passinglab.setText(passs)
            self.startdatelab.setText(sDate)
            self.confirmdatelab.setText(cDate)
            self.machinelab.setText(machin)
            self.lastmsg.setText(msg)

        elif self.nowSelectionLevel == 0:
            # scene level
            self.imageTable.setTabEnabled(0, True)
            self.imageTable.setTabEnabled(1, False)
            self.imageTable.setTabEnabled(2, False)
            self.infoTable.setTabEnabled(0, True)
            self.infoTable.setTabEnabled(1, True)
            self.infoTable.setTabEnabled(2, False)
            self.infoTable.setTabEnabled(3, False)
            self.oprGrp.setVisible(False)
            self.oprGrp.setFixedHeight(10)
            self.keyGrp.setVisible(False)
            self.keyGrp.setFixedHeight(10)

            # show and hide over

    def loadHTMLHistoryData(self):
        changeTabItm = self.nowSelMainTreeItem

        if type(changeTabItm) != str:
            historypath = self.serverPath + '\\' + self.bigType + '\\PRODUCE\\' + self.nowTreePage + '\\' + changeTabItm.text(
                0) + '\\history.html'
            if (os.path.exists(historypath)):
                historydata = open(historypath)
                codec = QtCore.QTextCodec.codecForName('utf-8')
                itmString = codec.toUnicode(historydata.read())
                self.qweb.setHtml(itmString, QtCore.QUrl(
                    self.serverPath + '\\' + self.bigType + '\\' + self.departmentName + '\\' + self.nowTreePage + '\\' + changeTabItm.text(
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

        followPathArray = [self.bigType,
                           self.departmentName,
                           self.nowTreePage,
                           self.nowSelMainTreeItem.text(0)
                           ]
        if self.nowSelectionLevel == 1:
            followPathArray.append(self.nowSelection)
        else:
            followPathArray.append('dataFolder')
        followPathArray.append('note')

        followPathString = '\\'.join(followPathArray)

        noteDir = self.serverPath + '\\' + followPathString
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

        conceptPath = self.serverPath + '\\' + self.bigType + '\\'+self.departmentName+'\\' + self.nowTreePage + '\\' + changeTabItm.text(0)
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
        # print path
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
        self.show()
        #self.media.play()
        self.setDockableParameters(dockable=True, floating=False, area='left')


ABC = shotManager_BaseClass()
ABC.Op_Ui()



