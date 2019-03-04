#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

addPathArray = [r'D:\gitLab\ssToolShelf',r'C:\gitLab\ssToolShelf',r'C:\Python27\Lib\site-packages']
for pt in addPathArray:
    if not pt in sys.path:
        #sys.path.append(pt)
        pass


import sys, os, time, json, shutil, random, math

from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2

if IsPySide:
    from shiboken import wrapInstance
elif IsPySide2:
    from shiboken2 import wrapInstance

try:
    import maya.OpenMayaUI as omui
    import maya.OpenMaya as om
    import pymel.core as pm
    import pymel.core.datatypes as dt
    import maya.cmds as cmds
    import maya.mel as mel
    # from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
    from Qt.QtCore import QRect

    def getMayaWindow():
        ptr = omui.MQtUtil.mainWindow()
        return wrapInstance(long(ptr), qw.QWidget)

    MayaParent = getMayaWindow()
except:
    MayaParent = ''

import bin.Mstyle_RB as Mstyle_RB

Mstyle = Mstyle_RB.RedBlackStyleSheet()



class chooseIconByUserUI(qw.QMainWindow):
    resultSinal = QtCore.Signal(str)
    UITitle = 'chooseIconByUserUI'
    x = 800
    y = 800
    result = ''
    iconPath = ''
    posX = 0
    posY = 0

    def __init__(self, parent=None):
        # ------close old window-----------------------------
        gmw = MayaParent
        for g in gmw.children():
            try:
                Tit = g.windowTitle()
                if Tit == self.UITitle:
                    g.close()
                    g.setParent(None)
            except:
                pass

        # ------Style Set----------------------------

        super(chooseIconByUserUI, self).__init__(parent)
        self.m_DragPosition = self.pos()
        self.setFixedHeight(self.y)
        self.setFixedWidth(self.x)

        self.setWindowFlags(QtCore.Qt.SubWindow | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        # self.setStyleSheet(Mstyle.QWidget())
        self.setWindowTitle(self.UITitle)

    def CreateUI(self):

        mian = qw.QWidget(self)
        mian.resize(self.x, self.y)
        # close Btn Set
        Xbtn = qw.QPushButton('x', mian)
        Xbtn.setGeometry(0, 0, 0, 0)
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())
        Xbtn.clicked.connect(self.Cl_Ui)

        # TitleLabel
        TitleLab = qw.QLabel(self.UITitle, mian)
        TitleLab.setGeometry(40, 5, 0, 0)
        TitleLab.setFixedHeight(20)
        TitleLab.setFixedWidth(140)
        TitleLab.setStyleSheet(Mstyle.QLabel(fontSize='12px'))

        # cha sel
        mainGrp = qw.QGroupBox('Pick Icon', mian)
        mainGrp.setGeometry(10, 25, 0, 0)
        mainGrp.setFixedHeight(self.y)
        mainGrp.setFixedWidth(self.x * 0.97)
        # mainGrp.setStyleSheet(Mstyle.QGroupBox())

        dirs = os.listdir(self.iconPath )
        files = []
        for d in dirs:
            if os.path.isfile(os.path.join(self.iconPath , d)):
                files.append(d)
        Gy = qw.QGridLayout(self)
        mainGrp.setLayout(Gy)

        val = math.sqrt(len(files))
        maxH = int(val)
        maxV = maxH + 1

        for count, f in enumerate(files):
            y = count % maxH
            x = count / maxH
            Btn = qw.QToolButton(self)
            Btn.setFixedSize(32, 32)
            Btn.setToolTip(f)
            combiePath = self.iconPath + '\\' + f
            Btn.setIcon(QtGui.QIcon(combiePath))
            Btn.setIconSize(QtCore.QSize(32, 32))
            Btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
            Btn.setAutoRaise(True)
            Btn.clicked.connect(self.BtnA1Fn)
            # Btn.setStyleSheet(Mstyle.QToolButton())
            Gy.addWidget(Btn, x, y)

        fixHeight = maxV * 64
        fixWidth = maxH * 64
        mian.setFixedSize(fixWidth, fixHeight)
        self.setFixedSize(fixWidth, fixHeight)
        mainGrp.setFixedSize(fixWidth * 0.95, fixHeight * 0.88)

    # --------------button Fns-----------------------------

    def BtnA1Fn(self):
        sender = self.sender()
        self.result = self.iconPath + '\\toolBoxUI\\' + sender.toolTip()
        self.resultSinal.emit(self.result)
        self.Cl_Ui()

    # --------------FUNCTIONS-----------------------------

    # --------------edit event-----------------------------
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton or event.button() == QtCore.Qt.RightButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and QtCore.Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

    def closeEvent(self, event):
        self.deleteLater()
    # ------------define swtich--------------------

    def Op_Ui(self):
        self.move(self.posX, self.posY)
        self.show()

    def Cl_Ui(self):
        self.close()


class chooseIcon(QtCore.QObject):
    # class figoIcon(QtGui.QIcon):
    # initPath = ''
    def chooseIcon(self, inputStr, isAuto=True, isDef=False, isBaseRoot=False):
        returnIcon = ''
        # initPath='D:\\Lighting_tool_box'

        if isBaseRoot:
            ext = os.path.isfile(self.iconPath + '\\toolBoxUI\\' + inputStr)
            if ext:
                isAuto = False
                isDef = False
            else:
                isAuto = True
                isDef = False
                isBaseRoot = False

        elif isDef:
            checkPath = self.iconPath + '\\ui\\' + inputStr + '.png'

            ext = os.path.isfile(checkPath)
            if ext:
                isAuto = False
            else:
                isAuto = True
                isDef = False

        elif not isAuto and not isDef and not isFull:
            isAuto = True

        if isBaseRoot:
            returnIcon = QtGui.QIcon(self.iconPath + '\\' + inputStr)

        elif isDef:
            iconPath = self.iconPath + '\\ui\\' + inputStr + '.png'
            returnIcon = QtGui.QIcon(iconPath)

        elif isAuto:
            sum = 0
            for i in str(inputStr):
                num = ord(i)
                sum = sum + num
            random.seed(sum)
            rValue = random.random()
            # sum all char number of ASCII.random it to calculate the seed
            dirs = os.listdir(self.iconPath)
            files = []
            for d in dirs:
                if os.path.isfile(os.path.join(self.iconPath, d)):
                    files.append(d)
            # collect all picture in folder

            count = len(files)
            cnt = int(count * rValue)
            returnIcon = QtGui.QIcon(self.iconPath + '\\' + files[cnt])
        return returnIcon


class dragToolListWidget(qw.QListWidget):
    mainSize = 0
    onPress = False
    iArray = []
    isDrag = False
    pluginsPath = ''
    iconPath = ''

    def __init__(self, parent=None):
        super(dragToolListWidget, self).__init__(parent)

        self.createContextMenu()

    def wheelEvent(self, e):
        if self.onPress:
            nowSt = self.styleSheet()
            tempsp = nowSt.split(';')
            for n in tempsp:
                if 'font-size:' in n:
                    nsp = n.split(':')
                    self.mainSize = int(nsp[1][0:-2])
                    self.mainSize = self.mainSize + (e.delta() / 120)

            # self.setStyleSheet(Mstyle.QListWidget(fontSize=str(self.mainSize) + 'px', bordRad='0px'))
            self.setIconSize(QtCore.QSize(self.mainSize * 2, self.mainSize * 2))

            if self.count() != len(self.iArray):
                self.iArray = []
                for i in range(self.count()):
                    self.iArray.append(self.item(i))

            for i in self.iArray:
                i.setSizeHint(QtCore.QSize(self.mainSize * 2, self.mainSize * 2))

        super(dragToolListWidget, self).wheelEvent(e)

    def mouseMoveEvent(self, e):
        if e.buttons() != QtCore.Qt.LeftButton:
            return

        if not self.isDrag:
            return

        cNode = self.currentItem()
        path = self.pluginsPath + '\\' + cNode.pageName + '\\' + cNode.fileName

        mimeData = QtCore.QMimeData()
        url = QtCore.QUrl.fromLocalFile(QtCore.QFileInfo(path).absoluteFilePath())
        mimeData.setUrls([url])
        self.drag = qw.QDrag(self)
        self.drag.setMimeData(mimeData)
        self.drag.setHotSpot(e.pos() - self.rect().topLeft())
        self.drag.exec_(QtCore.Qt.CopyAction)
        e.accept()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Control:
            self.onPress = True

    def keyReleaseEvent(self, e):
        self.onPress = False

    def mouseDoubleClickEvent(self, e):
        cNode = self.currentItem()
        fullUrl = self.pluginsPath + '\\' + cNode.pageName + '\\' + cNode.fileName
        self.runCommand(p=fullUrl)

    def runCommand(self, p=''):
        theUrl = ''
        if p != '':
            theUrl = p
        else:
            theUrl = self.pluginsPath + '\\' + self.pageName + '\\' + self.fileName

        check = theUrl.split('.')[-1]
        if check == 'py' or check == 'pyc':
            execfile(theUrl)
        if check == 'txt':
            os.startfile(theUrl)
        if check == 'mel':
            melcommand = 'source "' + theUrl + '"'
            units = melcommand.split('\\')
            melcommand = '/'.join(units)
            # print melcommand
            mel.eval(melcommand)
        if check == 'ma':
            result = cmds.confirmDialog(
                title='Open File',
                message='Do you wanna open file?',
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
                dismissString='Cancel')

            if result == 'OK':
                print 'openFile'

    def createContextMenu(self):
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        # print Mstyle.QMenu()


        self.contextMenu = qw.QMenu(self)
        self.contextMenu.setStyleSheet(Mstyle.QMenu())
        actionA = self.contextMenu.addAction(QtGui.QIcon(self.iconPath + "more.png"), u'run')
        self.actionB = self.contextMenu.addAction(QtGui.QIcon(self.iconPath + "more.png"), u'open')
        self.actionC = self.contextMenu.addAction(QtGui.QIcon(self.iconPath + "more.png"), u'history')
        # add sub menu
        self.second = self.contextMenu.addMenu(QtGui.QIcon(self.iconPath + "floder.png"), u"more")
        # self.second.setMask(mask)
        self.actionD = self.second.addAction(QtGui.QIcon(self.iconPath + "more.png"), u'actionA')
        self.actionE = self.second.addAction(QtGui.QIcon(self.iconPath + "more.png"), u'actionB')
        self.actionF = self.second.addAction(QtGui.QIcon(self.iconPath + "more.png"), u'actionC')
        self.actionF = self.second.addAction(QtGui.QIcon(self.iconPath + "more.png"), u'actionD')

        actionA.triggered.connect(self.actionAFn)

    def showContextMenu(self, pos):
        self.contextMenu.exec_(qw.QCursor.pos())  # show menu on cursor pos

    def actionAFn(self):
        # initPath='D:\\Lighting_tool_box'
        cNode = self.currentItem()
        fullUrl = self.pluginsPath + '\\' + cNode.pageName + '\\' + cNode.fileName
        self.runCommand(p=fullUrl)


class dragToolListItem(qw.QListWidgetItem):
    # initPath inhert by parent
    pageName = ''
    iconName = ''
    fileName = ''
    isDrag = False
    initPath = ''

    def mouseMoveEvent(self, e):
        if e.buttons() != QtCore.Qt.LeftButton:
            return
        if not self.isDrag:
            return

        # initPath='D:\\Lighting_tool_box'
        path = self.pluginsPath + '\\' + self.pageName + '\\' + self.fileName
        mimeData = QtCore.QMimeData()
        url = QtCore.QUrl.fromLocalFile(QtCore.QFileInfo(path).absoluteFilePath())
        mimeData.setUrls([url])
        self.drag = qw.QDrag(self)
        self.drag.setMimeData(mimeData)
        self.drag.setHotSpot(e.pos() - self.rect().topLeft())
        self.drag.exec_(QtCore.Qt.CopyAction)
        e.accept()


class dragToolButton(qw.QToolButton, chooseIcon):
    # initPath inhert by parent
    pageName = ''
    iconName = ['', True, False, False]
    fileName = ''
    theText = ''
    isBig = False
    isDrag = False
    pluginsPath = ''
    iconPath = ''

    def __init__(self, parent=None):
        super(dragToolButton, self).__init__(parent)

        self.createContextMenu()
        self.count = 0

    def mouseMoveEvent(self, e):
        # print dir(e)
        # tt=dir(e)
        # GrabKeyboard
        # KeyPress
        # UngrabKeyboard
        if e.buttons() != QtCore.Qt.LeftButton:
            return
        if not self.isDrag:
            return

        path = self.pluginsPath + '\\' + self.pageName + '\\' + self.fileName
        mimeData = QtCore.QMimeData()
        url = QtCore.QUrl.fromLocalFile(QtCore.QFileInfo(path).absoluteFilePath())
        mimeData.setUrls([url])
        self.drag = qw.QDrag(self)
        self.drag.setMimeData(mimeData)
        self.drag.setHotSpot(e.pos() - self.rect().topLeft())
        self.drag.exec_(QtCore.Qt.CopyAction)
        e.accept()

    def mouseDoubleClickEvent(self, e):
        self.runCommand()

    def runCommand(self, p=''):
        theUrl = self.pluginsPath + '\\' + self.pageName + '\\' + self.fileName
        check = self.fileName.split('.')[-1]
        if check == 'py' or check == 'pyc':
            execfile(theUrl)

        if check == 'txt':
            os.startfile(theUrl)

        if check == 'mel':
            melcommand = 'source "' + theUrl + '"'
            units = melcommand.split('\\')
            melcommand = '/'.join(units)
            mel.eval(melcommand)

        if check == 'ma':
            result = cmds.confirmDialog(
                title='Open File',
                message='Do you wanna open file?',
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
                dismissString='Cancel')

            if result == 'OK':
                print 'openFile'

    def createContextMenu(self):
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        # print Mstyle.QMenu()


        self.contextMenu = qw.QMenu(self)
        # self.contextMenu.setStyleSheet(Mstyle.QMenu())
        self.actionA = self.contextMenu.addAction(QtGui.QIcon(self.iconPath + "more.png"), u'run')
        self.actionB = self.contextMenu.addAction(QtGui.QIcon(self.iconPath + "more.png"), u'open')
        self.actionC = self.contextMenu.addAction(QtGui.QIcon(self.iconPath + "more.png"), u'history')
        # add sub menu
        self.second = self.contextMenu.addMenu(QtGui.QIcon(self.iconPath + "floder.png"), u"more")
        # self.second.setMask(mask)
        self.actionD = self.second.addAction(QtGui.QIcon(self.iconPath + "more.png"), u'actionA')
        self.actionE = self.second.addAction(QtGui.QIcon(self.iconPath + "more.png"), u'actionB')
        self.actionF = self.second.addAction(QtGui.QIcon(self.iconPath + "more.png"), u'actionC')
        self.actionF = self.second.addAction(QtGui.QIcon(self.iconPath + "more.png"), u'actionD')

    def showContextMenu(self, pos):
        self.contextMenu.exec_(qw.QCursor.pos())  # show menu on cursor pos

class customIconSystem(QtCore.QObject):
    customIconPath = ''
    def setIconPath(self,inputStr):

        self.customIconPath = inputStr

    def getIcon(self,iconName,subs=[]):
        returnIcon = ''

        workPath = self.customIconPath
        if subs:
            addPath = os.sep.join(subs)
            workPath = os.path.join(self.customIconPath,addPath)


        dirs = os.listdir(workPath)
        files = ''
        for d in dirs:
            if os.path.isfile(os.path.join(workPath, d)):
                files = d
                break

        if files:
            returnIcon = QtGui.QIcon(files)
        else:
            pixmap = qw.QPixmap(60, 60)
            pixmap.fill()
            painter = qw.QPainter(pixmap)
            painter.setBrush(QtCore.Qt.white)
            painter.drawRect(5, 10, 50, 30)
            painter.end()

            returnIcon = QtGui.QIcon(pixmap)

        return returnIcon

class FigoToolBox(qw.QMainWindow, customIconSystem):
    WINDOW_OBJECT_NAME = 'FigoToolBox'
    widgetHeight = 750
    widgetWidth = 350
    tabY = 175

    DetailBox = ''
    isShowDetail = True

    pathDict = {}
    iconPath = ''
    initPath = ''
    jsonPath = ''
    pluginsPath = ''

    UIitems = {}

    def __init__(self, parent=None):
        # self.cleanOpenWindow()
        super(FigoToolBox, self).__init__(parent=parent)
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle(self.WINDOW_OBJECT_NAME)
        #self.setFixedWidth(self.widgetWidth)
        self.setAcceptDrops(True)
        self.initData()

        self.localPath = ''
        for i in sys.path:
            testFile = os.path.join(i,'ssToolShelf_path.py')
            pathCheck = os.path.exists(testFile)
            if pathCheck:
                print ' start at' + '*-' * 10  
                print i
                print '*-' * 10  
                self.localPath = i

        #self.localPath = r'D:\Program Files\figo\CommonToolBox_Local'
        self.localJson = self.localPath + '\\bin\\log.json'

        if not os.path.exists(self.localJson):
            self.saveJson({'current': 'model'}, self.localJson)

        currentData = self.loadJson(self.localJson)
        current = currentData['current']
        
        #self.pathDict = getAssetManagerPath()
        self.initPath = self.localPath
        self.iconPath = self.localPath + '\\icons'
        #self.jsonPath = self.pathDict['data'] + '\\appHelps.json'
        self.pluginsPath =  self.localPath + '\\depository'
        self.setIconPath(self.iconPath)
        self.createForm()
        
        mainUI = self.createUI()
        mv = qw.QVBoxLayout()
        self.setLayout(mv)
        mv.addWidget(mainUI)

        self.isShowDetail = False
        if self.isShowDetail:
            Idx = self.QTwidget.currentIndex()
            pageN = self.QTwidget.tabText(Idx)
            dNode = self.UIitems[pageN][0]
            self.updateDetail(dNode.pageName, dNode.iconName, dNode.fileName)
        else:
            self.searchGb.setGeometry(5, 10, 5, 5)
            self.QTwidget.setGeometry(5, 50, 5, 5)
            self.tabY = 50
            if self.DetailBox:
                print 'is show {}'.format(self.DetailBox.isShow())
            else:
                print 'detail is close now. skip.'
        '''

        '''

    def createForm(self):
        qmb = qw.QMenuBar(self)

        fileMn = qw.QMenu('file', qmb)
        qmb.addMenu(fileMn)

        fileMn1act = fileMn.addAction('change Detail Icon')
        fileMn.addSeparator()  # --------------------
        # fileMn2 = qw.QMenu('change department', qmb)
        fileMn2 = qw.QMenu('change department', qmb)
        fileMn.addMenu(fileMn2)

        MODELact = fileMn2.addAction("MODEL")
        RIGact = fileMn2.addAction("RIG")
        TEXTUREact = fileMn2.addAction("TEXTURE")
        SHADEact = fileMn2.addAction("SHADE")
        ANIMATEact = fileMn2.addAction("ANIMATE")
        RENDERact = fileMn2.addAction("RENDER")
        COMPact = fileMn2.addAction("COMP")

        shMn = qw.QMenu('show/hide', qmb)
        qmb.addMenu(shMn)
        shMn1act = shMn.addAction("show Detail")
        shMn2act = shMn.addAction("hide Detail")
        shMn.addSeparator()

        aboutMn = qw.QMenu('about', qmb)
        qmb.addMenu(aboutMn)
        about1act = aboutMn.addAction("about author")
        about2act = aboutMn.addAction("how to use")

        # -----------------------------

        self.searchGb = qw.QWidget(self)
        #self.searchGb.setFixedHeight(50)
        self.searchGb.setGeometry(5, 135, 5, 5)
        searchLy = qw.QHBoxLayout(self)

        searchLab = qw.QLabel('search : ', self)
        searchLy.addWidget(searchLab)
        self.LE = qw.QLineEdit('', self)
        #self.LE.setStyleSheet(Mstyle.QLineEdit(kw='c', lang='c'))
        searchLy.addWidget(self.LE)

        s1Mn = qw.QMenu()
        s1Mnact1 = qw.QAction('List Form', s1Mn)
        s1Mn.addAction(s1Mnact1)
        s1Mnact2 = qw.QAction('Block Form', s1Mn)
        s1Mn.addAction(s1Mnact2)

        searchBtn1 = qw.QToolButton(self)
        searchBtn1.setFixedSize(20, 20)
        searchBtn1.setToolTip('change widget form')

        searchBtn1.setIcon(self.getIcon('more', subs=['ui']))
        searchBtn1.setIconSize(QtCore.QSize(20, 20))
        searchBtn1.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        searchBtn1.setAutoRaise(True)
        searchBtn1.setMenu(s1Mn)
        searchBtn1.setPopupMode(searchBtn1.InstantPopup)
        searchLy.addWidget(searchBtn1)

        self.searchBtn2 = qw.QToolButton(self)
        self.searchBtn2.setToolTip('on/off drag mode')
        self.searchBtn2.setFixedSize(20, 20)
        self.searchBtn2.setIcon(self.getIcon('drag', subs=['ui']))
        self.searchBtn2.setIconSize(QtCore.QSize(20, 20))
        self.searchBtn2.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.searchBtn2.setAutoRaise(True)
        self.searchBtn2.setCheckable(True)
        searchLy.addWidget(self.searchBtn2)

        searchBtn3 = qw.QToolButton(self)
        searchBtn3.setFixedSize(20, 20)
        searchBtn3.setToolTip('open current folder')
        searchBtn3.setIcon(self.getIcon('floder', subs=['ui']))
        searchBtn3.setIconSize(QtCore.QSize(20, 20))
        searchBtn3.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        searchBtn3.setAutoRaise(True)
        searchLy.addWidget(searchBtn3)

        sortMn = qw.QMenu()
        sortMnact1 = qw.QAction('Time +', sortMn)
        sortMn.addAction(sortMnact1)
        sortMnact2 = qw.QAction('Time -', sortMn)
        sortMn.addAction(sortMnact2)
        sortMn.addSeparator()
        # --------------------
        sortMnact3 = qw.QAction('Name +', sortMn)
        sortMn.addAction(sortMnact3)
        sortMnact4 = qw.QAction('Name -', sortMn)
        sortMn.addAction(sortMnact4)

        searchBtn4 = qw.QToolButton(self)
        searchBtn4.setFixedSize(20, 20)
        searchBtn4.setToolTip('sort items')
        searchBtn4.setIcon(self.getIcon('activity', subs=['ui']))
        searchBtn4.setIconSize(QtCore.QSize(20, 20))
        searchBtn4.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        searchBtn4.setAutoRaise(True)
        searchBtn4.setMenu(sortMn)
        searchBtn4.setPopupMode(searchBtn4.InstantPopup)
        searchLy.addWidget(searchBtn4)

        self.searchGb.setLayout(searchLy)

        fileMn1act.triggered.connect(self.fileMn1actFn)
        MODELact.triggered.connect(self.changeDepartmentFn)
        RIGact.triggered.connect(self.changeDepartmentFn)
        TEXTUREact.triggered.connect(self.changeDepartmentFn)
        SHADEact.triggered.connect(self.changeDepartmentFn)
        ANIMATEact.triggered.connect(self.changeDepartmentFn)
        RENDERact.triggered.connect(self.changeDepartmentFn)
        COMPact.triggered.connect(self.changeDepartmentFn)

        s1Mnact1.triggered.connect(self.s1Mnact1Fn)
        s1Mnact2.triggered.connect(self.s1Mnact2Fn)
        self.searchBtn2.clicked.connect(self.searchBtn2Fn)
        searchBtn3.clicked.connect(self.searchBtn3Fn)
        searchBtn4.clicked.connect(self.searchBtn4Fn)
        self.LE.textChanged.connect(self.LEtextChangedFn)

        sortMnact1.triggered.connect(self.searchBtn4Fn)
        sortMnact2.triggered.connect(self.searchBtn4Fn)
        sortMnact3.triggered.connect(self.searchBtn4Fn)
        sortMnact4.triggered.connect(self.searchBtn4Fn)

        shMn1act.triggered.connect(self.shMn1actFn)
        shMn2act.triggered.connect(self.shMn2actFn)

        about1act.triggered.connect(self.about1actFn)
        about2act.triggered.connect(self.about2actFn)

    def about1actFn(self):
        qw.QMessageBox.information(self, "Author", ('Auther: figo\nE-mail: 276415977@qq.com'),
                                      qw.QMessageBox.Yes, qw.QMessageBox.Yes)

    def about2actFn(self):
        qw.QMessageBox.information(self, "help", (r'Z:\temp\figo\help\how to use tool box.mp4'),
                                      qw.QMessageBox.Yes, qw.QMessageBox.Yes)

    def shMn1actFn(self):
        self.isShowDetail = True
        Idx = self.QTwidget.currentIndex()
        pageN = self.QTwidget.tabText(Idx)
        dNode = self.UIitems[pageN][0]
        self.updateDetail(dNode.pageName, dNode.iconName, dNode.fileName)
        self.searchGb.setGeometry(5, 135, 5, 5)
        #self.QTwidget.setGeometry(5, 175, 5, 5)
        # self.tabY=175
        self.tabY = 175
        self.refreshListHeight(dHeight=self.tabY)

    def shMn2actFn(self):
        try:
            self.DetailBox.setParent(None)
        except:
            pass

        self.isShowDetail = False
        self.DetailBox = ''
        self.searchGb.setGeometry(5, 10, 5, 5)
        #self.QTwidget.setGeometry(5, 50, 5, 5)
        # self.tabY=175
        self.tabY = 50
        self.refreshListHeight(dHeight=self.tabY)

    def changeDepartmentFn(self):
        sender = self.sender()
        key = sender.text().lower()
        if key in self.pathDict.keys():

            self.pluginsPath = self.pathDict[sender.text().lower()] + '\\plugins'
            if not (os.path.exists(self.pluginsPath)):
                os.makedirs(self.pluginsPath + '\\PAGE1')
            # delete all tab.and create new tab.
            mainCount = self.QTwidget.count()
            for i in range(mainCount):
                self.QTwidget.removeTab(0)

            floders = self.getFloder()
            for f in floders:
                page = self.createPage(f)
                self.QTwidget.addTab(page[0], f)

                currentData = self.loadJson(self.localJson)
                currentData['current'] = sender.text().lower()
                self.saveJson(currentData, self.localJson)


        else:
            cmds.warning(key + ' not support for this version of maya')

    def createUI(self, winType='block'):
        self.QTwidget = qw.QTabWidget(self)
        #self.QTwidget.setMinimumSize(self.widgetWidth * 0.98, self.widgetHeight * 0.2)
        self.QTwidget.setGeometry(5, self.tabY, 5, 5)
        self.QTwidget.setTabPosition(qw.QTabWidget.West)
        #self.QTwidget.setStyleSheet(Mstyle.QTabWidget())
        floders = self.getFloder()
        self.UIitems = {}

        if winType == 'block':
            for f in floders:
                page = self.createPage(f)
                self.QTwidget.addTab(page[0], f)
                self.UIitems.update(page[1])
        elif winType == 'list':
            for f in floders:
                page = self.createListPage(f)
                self.QTwidget.addTab(page[0], f)
                self.UIitems.update(page[1])
        self.QTwidget.currentChanged.connect(self.QTwidgetFn)
        return self.QTwidget

    def createListPage(self, floderName, sort='nameF'):
        pageItems = []
        listWd = qw.QWidget(self)
        listWd.setAttribute(Qt.WA_StyledBackground)
        listWd.setStatusTip(floderName + '_list')
        sty = ''
        if self.searchBtn2.isChecked():
            sty = ('QWidget {background:rgb(109,109,109);border: 3px solid rgb(159,219,173)}')
        else:
            sty = ('QWidget {background:rgb(109,109,109)}')
        listWd.setStyleSheet(sty)
        listLy = qw.QVBoxLayout()
        listWd.setLayout(listLy)

        itemSize = 15
        self.list = dragToolListWidget(listWd)
        self.list.pluginsPath = self.pluginsPath
        self.list.iconPath = self.iconPath
        self.list.setIconSize(QtCore.QSize(itemSize * 2, itemSize * 2))
        #self.list.setStyleSheet(Mstyle.QListWidget(fontSize=str(itemSize) + 'px', bordRad='0px'))
        self.list.setGeometry(20, 10, 0, 0)
        listLy.addWidget(self.list)
        flns = []
        flnsTemp = self.getFiles(floderName)

        if sort == 'nameF':
            flns = self.bubbleSort_name(flnsTemp, isRevert=False)
        if sort == 'nameR':
            flns = self.bubbleSort_name(flnsTemp, isRevert=True)
        if sort == 'timeF':
            flns = self.bubbleSort_time(flnsTemp, isRevert=False, filePath=self.pluginsPath + '\\' + floderName + '\\')
        if sort == 'timeR':
            flns = self.bubbleSort_time(flnsTemp, isRevert=True, filePath=self.pluginsPath + '\\' + floderName + '\\')

        for f in flns:
            itm = dragToolListItem(f)
            itm.setSizeHint(QtCore.QSize(itemSize * 2, itemSize * 2))
            itm.initPath = self.pluginsPath + '\\' + f + '\\'
            itm.pageName = floderName
            itm.fileName = f
            getIcon = False
            jsonPath = self.jsonPath
            data = self.loadJson(jsonPath)
            if floderName in data.keys():
                if f in data[floderName].keys():
                    if 'icon' in data[floderName][f].keys():
                        iconData = data[floderName][f]['icon']
                        itm.iconName = iconData
                        itm.setIcon(
                            self.chooseIcon(iconData[0], isAuto=iconData[1], isDef=iconData[2], isBaseRoot=iconData[3]))
                        getIcon = True
            if not getIcon:
                itm.iconName = [f, True, False, False]
                itm.setIcon(self.chooseIcon(f))
            itemPath = self.pluginsPath + '\\' + floderName + '\\' + f
            mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(itemPath)))
            hisTex = f + '\n' + mtime
            itm.setToolTip(hisTex)
            pageItems.append(itm)
            self.list.addItem(itm)
        self.list.currentItemChanged.connect(self.btnAction)

        return [listWd, {floderName: pageItems}]

    def createPage(self, floderName, spacing=3, sort='nameF'):
        x = 0
        y = 0
        pageItems = []
        sty = ''
        if self.searchBtn2.isChecked():
            sty = ('QWidget {background:rgb(109,109,109);border: 3px solid rgb(159,219,173)}')
        else:
            sty = ('QWidget {background:rgb(109,109,109)}')
            # preset over

        epWd = qw.QWidget(self)
        epWd.setAttribute(QtCore.Qt.WA_StyledBackground)
        epWd.setStatusTip(floderName + '_block')
        epWd.setToolTip('block')
        epWd.setStyleSheet(sty)

        epScroll = qw.QScrollArea(self)
        #epScroll.resize(500,600)
        epScroll.setWidget(epWd)
        #epScroll.setStyleSheet(Mstyle.QScrollBar() + 'QScrollArea {background:rgb(109,109,109);border:0;}')

        Gy = qw.QGridLayout(epWd)
        Gy.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        flns = []
        flnsTemp = self.getFiles(floderName)

        if sort == 'nameF':
            flns = self.bubbleSort_name(flnsTemp, isRevert=False)
        if sort == 'nameR':
            flns = self.bubbleSort_name(flnsTemp, isRevert=True)
        if sort == 'timeF':
            flns = self.bubbleSort_time(flnsTemp, isRevert=False, filePath=self.pluginsPath + '\\' + floderName + '\\')
        if sort == 'timeR':
            flns = self.bubbleSort_time(flnsTemp, isRevert=True, filePath=self.pluginsPath + '\\' + floderName + '\\')

        for count, f in enumerate(flns):
            y = count % spacing
            x = count / spacing
            Btn = dragToolButton()
            Btn.iconPath = self.iconPath
            Btn.setText(self.regularNameLen(f))

            itemPath = self.pluginsPath + '\\' + floderName + '\\' + f
            mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(itemPath)))
            hisTex = f + '\n' + mtime
            Btn.setToolTip(hisTex)
            Btn.setIconSize(QtCore.QSize(48, 48))
            Btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
            Btn.setAutoRaise(True)
            Btn.setAcceptDrops(True)
            Btn.pluginsPath = self.pluginsPath
            Btn.pageName = floderName
            Btn.fileName = f
            Btn.clicked.connect(self.btnAction)

            getIcon = False
            '''
            jsonPath = self.jsonPath
            data = self.loadJson(jsonPath)
            if floderName in data.keys():
                if f in data[floderName].keys():
                    if 'icon' in data[floderName][f].keys():
                        iconData = data[floderName][f]['icon']
                        Btn.iconName = iconData
                        Btn.setIcon(
                            self.chooseIcon(iconData[0], isAuto=iconData[1], isDef=iconData[2], isBaseRoot=iconData[3]))
                        getIcon = True
            if not getIcon:
                Btn.iconName = [f, True, False, False]
                Btn.setIcon(self.chooseIcon(f))

            Gy.addWidget(Btn, x, y, QtCore.Qt.AlignCenter)
            pageItems.append(Btn)
            '''
        widHeight = (int(len(flns) / spacing) + 1) * 95
        print 'create page'
        epWd.resize((spacing) * 105, widHeight)
        epWd.setLayout(Gy)
        return [epScroll, {floderName: pageItems}]

    # -------------------- ui functions -------------

    def updateDetail(self, pageName, iconArray, fileName):
        try:
            self.DetailBox.setParent(None)
        except:
            pass

        if self.DetailBox or self.isShowDetail:
            self.DetailBox = detailGroupBox(self)
            self.DetailBox.pluginsPath = self.pluginsPath
            self.DetailBox.jsonPath = self.jsonPath
            self.DetailBox.iconPath = self.iconPath
            self.DetailBox.setPath(pageName)
            self.DetailBox.setFileName(fileName)
            self.DetailBox.setText()
            self.DetailBox.setX(self.widgetWidth * 0.98)
            self.DetailBox.CreateUI()
            self.DetailBox.setDetailIcon(iconArray)
            self.DetailBox.setParent(self)
            # self.DetailBox.saveSignal.connect(self.saveSignalFn)
            self.DetailBox.show()
        pass

    def bubbleSort_time(self, InputArray, isRevert=False, filePath=''):
        array = InputArray
        for s in range(len(array)):
            for x in range(1, len(array)):
                # print 'x is {},x-1 is {}'.format(filePath+array[x],filePath+array[x-1])
                mt = os.path.getmtime(filePath + array[x])
                lt = os.path.getmtime(filePath + array[x - 1])

                if isRevert:
                    if mt > lt:
                        b = array[x]
                        array[x] = array[x - 1]
                        array[x - 1] = b
                else:
                    if mt < lt:
                        b = array[x]
                        array[x] = array[x - 1]
                        array[x - 1] = b
        return array

    def bubbleSort_name(self, InputArray, isRevert=False):
        array = InputArray
        '''
        for s in range(len(array)):
            for x in range(1, len(array)):
                nowCount = 0
                mt = ord(array[x].lower()[nowCount])
                lt = ord(array[x - 1].lower()[nowCount])
                while mt == lt:
                    nowCount = nowCount + 1
                    mt = ord(array[x].lower()[nowCount])
                    lt = ord(array[x - 1].lower()[nowCount])
                if isRevert:
                    if mt > lt:
                        b = array[x]
                        array[x] = array[x - 1]
                        array[x - 1] = b
                else:
                    if mt < lt:
                        b = array[x]
                        array[x] = array[x - 1]
                        array[x - 1] = b
        '''
        return array

    def getFiles(self, floderName):
        # print self.pluginsPath
        # print floderName
        path = self.pluginsPath + '\\' + floderName
        dirs = os.listdir(path)
        files = []
        for d in dirs:
            if os.path.isfile(os.path.join(path, d)):
                if d != '__init__.py' and d != '__init__.pyc':
                    files.append(d)

        return files

    def getFloder(self):
        # path=self.initPath+'\\pulg_ins'
        dirs = os.listdir(self.pluginsPath)
        floder = []
        for d in dirs:
            if (not os.path.isfile(os.path.join(self.pluginsPath, d))) and d != 'data':
                floder.append(d)
        return floder

    def getMate(self, target, menberIndex):
        sender = target
        for page in self.UIitems:
            for item in page:
                if sender in item:
                    return item[menberIndex]

    def regularNameLen(self, str, lenth=16):
        showStr = ''
        if len(str) > lenth:
            showStr = str[0:lenth - 2] + '...'
        else:
            showStr = str
        return showStr

    def refreshListHeight(self, dHeight=180):
        dockSize = self.size()
        self.widgetHeight = dockSize.height() - 5
        #if self.widgetHeight > 300:
            #self.QTwidget.setFixedSize(int(self.widgetWidth * 0.98), int(self.widgetHeight - dHeight))

        Idx = self.QTwidget.currentIndex()
        cwd = self.QTwidget.widget(Idx)
        #if '_list' in cwd.statusTip():
        #    cwd.children()[0].setFixedSize(int(self.widgetWidth * 0.875), int(self.widgetHeight - dHeight))

    # ------ button functions ------------------------------

    def fileMn1actFn(self):
        print 'change icon'
        iconUI = chooseIconByUserUI()
        iconUI.setParent(MayaParent)
        # D:\AssetManegerSystem_publish\icon\avarter
        iconUI.iconPath = self.iconPath
        iconUI.CreateUI()
        iconUI.posX = qw.QCursor.pos().x()
        iconUI.posY = qw.QCursor.pos().y()
        iconUI.resultSinal.connect(self.iconUIRlt)  # use sinal deliver data ,from sub to main
        iconUI.Op_Ui()

    def iconUIRlt(self, data):
        print data
        if self.DetailBox:
            pData = os.path.basename(data)
            self.DetailBox.setDetailIcon([pData, False, False, True])
            Idx = self.QTwidget.currentIndex()
            pageName = self.QTwidget.tabText(Idx)
            cwd = self.QTwidget.widget(Idx)
            if '_block' in cwd.statusTip():
                for c in cwd.children():
                    if type(c) == dragToolButton:
                        if self.DetailBox.Btn.fileName == c.fileName:
                            c.setIcon(self.chooseIcon(pData, isBaseRoot=True))
            if '_list' in cwd.statusTip():
                itemArray = []
                for i in range(self.list.count()):
                    itemArray.append(self.list.item(i))
                for d in itemArray:
                    if self.DetailBox.Btn.fileName == d.fileName:
                        d.setIcon(self.chooseIcon(pData, isBaseRoot=True))
        else:
            print 'detail is close now. skip.'

    def QTwidgetFn(self):
        Idx = self.QTwidget.currentIndex()
        cwd = self.QTwidget.widget(Idx)
        #if Idx and cwd:
            #if '_list' in cwd.statusTip():
                #cwd.children()[0].setFixedSize(int(self.widgetWidth * 0.875), int(self.widgetHeight - 180))

    def searchBtn3Fn(self):
        Idx = self.QTwidget.currentIndex()
        pageName = self.QTwidget.tabText(Idx)
        os.startfile(self.pluginsPath + '\\' + pageName)

    def searchBtn2Fn(self):
        sender = self.sender()
        tCount = self.QTwidget.count()
        items = []
        if sender.isChecked():
            for i in range(tCount):
                cwd = self.QTwidget.widget(i)
                cwd.setStyleSheet('QWidget {background:rgb(109,109,109);border: 3px solid rgb(159,219,173)}')
        else:
            for i in range(tCount):
                cwd = self.QTwidget.widget(i)
                cwd.setStyleSheet('QWidget {background:rgb(109,109,109)}')

    def s1Mnact1Fn(self):
        Idx = self.QTwidget.currentIndex()
        pageName = self.QTwidget.tabText(Idx)
        cwd = self.QTwidget.widget(Idx)
        pageType = cwd.statusTip()

        self.QTwidget.removeTab(Idx)
        ans = self.createListPage(pageName)
        self.QTwidget.insertTab(Idx, ans[0], pageName)
        self.QTwidget.setCurrentIndex(Idx)

    def s1Mnact2Fn(self):
        Idx = self.QTwidget.currentIndex()
        pageName = self.QTwidget.tabText(Idx)
        cwd = self.QTwidget.widget(Idx)
        pageType = cwd.statusTip()

        self.QTwidget.removeTab(Idx)
        ans = self.createPage(pageName)
        self.QTwidget.insertTab(Idx, ans[0], pageName)
        self.QTwidget.setCurrentIndex(Idx)

    def searchBtn4Fn(self):
        sk = ''
        sender = self.sender()
        keyStr = sender.text()
        if keyStr == 'Name +':
            sk = 'nameF'
        if keyStr == 'Name -':
            sk = 'nameR'
        if keyStr == 'Time +':
            sk = 'timeF'
        if keyStr == 'Time -':
            sk = 'timeR'

        Idx = self.QTwidget.currentIndex()
        pageName = self.QTwidget.tabText(Idx)
        cwd = self.QTwidget.widget(Idx)
        pageType = cwd.statusTip()

        if '_list' in pageType:
            self.QTwidget.removeTab(Idx)
            ans = self.createListPage(pageName, sort=sk)
            self.QTwidget.insertTab(Idx, ans[0], pageName)
            self.QTwidget.setCurrentIndex(Idx)

        if '_block' in pageType:
            self.QTwidget.removeTab(Idx)
            ans = self.createPage(pageName, sort=sk)
            self.QTwidget.insertTab(Idx, ans[0], pageName)
            self.QTwidget.setCurrentIndex(Idx)

    def LEtextChangedFn(self):
        Idx = self.QTwidget.currentIndex()
        pageN = self.QTwidget.tabText(Idx)
        # dNode=self.UIitems[pageN]
        cwd = self.QTwidget.widget(Idx)
        if type(cwd) == qw.QScrollArea:
            cc = cwd.widget()
            if cc.toolTip() == 'block':
                cwd = cc

        pageType = cwd.statusTip()
        if '_list' in pageType:
            itemArray = []
            for i in range(self.list.count()):
                itemArray.append(self.list.item(i))
            for d in itemArray:
                if self.LE.text().lower() in d.fileName.lower():
                    d.setHidden(0)
                else:
                    d.setHidden(1)
        elif '_block' in pageType:
            dTemp = cwd.children()
            dNode = []
            for d in dTemp:
                if type(d) == dragToolButton:
                    dNode.append(d)
            for d in dNode:
                if self.LE.text().lower() in d.fileName.lower():
                    d.show()
                else:
                    d.hide()

            if self.LE.text() == '':
                for i in dNode:
                    i.show()

    def btnAction(self):
        Btn = self.sender()
        # print Btn
        if self.searchBtn2.isChecked():
            Btn.isDrag = True
        else:
            Btn.isDrag = False
        if type(Btn) == dragToolListWidget:
            Btn = self.sender().currentItem()
            # print Btn

        self.updateDetail(Btn.pageName, Btn.iconName, Btn.fileName)

    # -------------json--------------

    def saveJson(self, data, path):
        jsonDump = json.dumps(data)
        file_object = open(path, 'w')
        file_object.write(jsonDump)
        file_object.close()
        # gg.initPath+'\\appHelp.json'

    def loadJson(self, path):
        file_object = open(path, 'r')
        data = json.load(file_object)
        return data

    # ------event rewrite-----------

    def dockCloseEventTriggered(self):
        """
        Handle stuff when the dock is closed
        """
        self.close()
        self.deleteLater()

    def resizeEvent(self, e):
        pass
        # self.refreshListHeight(dHeight=self.tabY)

    def dragEnterEvent(self, e):
        if (e.mimeData().hasFormat("text/uri-list")):
            e.acceptProposedAction()

    def mousePressEvent(self, e):
        pass
        #if (e.button() == Qt.LeftButton):
        #    pass
            # drag = qw.QDrag(self)
            # data = qw.QMimeData
            # e.setMimeData(data)
            # e.exec(Qt.MoveAction)

    def dropEvent(self, e):
        if not self.searchBtn2.isChecked:
            return
        urls = e.mimeData().urls()
        if len(urls) == 0:
            return

        Idx = self.QTwidget.currentIndex()
        cwd = self.QTwidget.widget(Idx)
        pageName = self.QTwidget.tabText(Idx)
        pageType = cwd.statusTip()

        targetUrl = self.pluginsPath + '\\' + pageName + '\\'
        for url in urls:
            strUrl = url.path()[1:]
            inputName = str(strUrl).split('/')[-1]
            fromUrl = '\\'.join(strUrl.split('/'))
            shutil.copyfile(fromUrl, targetUrl + inputName)

        if '_list' in cwd.statusTip():
            self.s1Mnact1Fn()
        if '_block' in cwd.statusTip():
            self.s1Mnact2Fn()




    # ------------widget enter--------------
    def Op_Ui(self):
        self.show()
        #self.setDockableParameters(dockable=True, floating=False, area='left')
        self.raise_()


    def readSettings(self):
        self.dataSettings.beginGroup('customToolWindowSettings_mainWindow')
        windowGeometry = self.dataSettings.value('window_geometry')
        windowState = self.dataSettings.value('window_state')
        self.restoreGeometry(windowGeometry)
        self.restoreState(windowState)
        self.dataSettings.endGroup()

    def writeSettings(self):
        self.dataSettings.beginGroup('customToolWindowSettings_mainWindow')
        self.dataSettings.setValue('window_geometry', self.saveGeometry())
        self.dataSettings.setValue('window_state', self.saveState())
        self.dataSettings.endGroup()

    def closeEvent(self,event):
        self.deleteLater()
        self.writeSettings()

    def initData(self):
        self.dataSettings = QtCore.QSettings("customToolWindowSettings", "customToolWindowSettings")

#MDtoolBUI = FigoToolBox()
#MDtoolBUI.Op_Ui()


def main():
    '''
    program start function
    '''
    app = qw.QApplication.instance()
    if not app:
        app = qw.QApplication([])

    for widget in app.topLevelWidgets():
        if widget.objectName() == FigoToolBox.WINDOW_OBJECT_NAME:
            widget.close()
            widget.deleteLater()
    try:
        window = FigoToolBox(parent=MayaParent)
    except:
        window = FigoToolBox()
    window.show()

    window.raise_()
    try:
        sys.exit(app.exec_())
    except: pass


if __name__ == '__main__':
    # main()

    app = qw.QApplication.instance()
    if not app:
        app = qw.QApplication([])

    #dtest = detailGroupBox()
    #dtest.setFile(r'D:\AssetManegerSystem_publish\maya2016\COMMON\common_tool_box.py')
    #dtest.show()
    #dtest.resize(400, 200)
    #dtest.raise_()
        
    dtest = FigoToolBox()
    #dtest.setFile(r'D:\AssetManegerSystem_publish\maya2016\COMMON\common_tool_box.py')
    dtest.Op_Ui()
    #dtest.resize(400, 200)
    #dtest.raise_()
    try:
        sys.exit(app.exec_())
    except: pass




