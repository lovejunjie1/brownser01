import sys, os, time, json, shutil, random, math
import maya.cmds as cmds
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import Qt
from Qt import QtWidgets as qw,QtCore,QtGui
if Qt.IsPySide:
    from shiboken import wrapInstance
    
if Qt.IsPySide2:
    from shiboken2 import wrapInstance
import maya.OpenMayaUI as OpenMayaUI

from data.redBlackStyleSheet_0_10 import RedBlackStyleSheet  
Mstyle = RedBlackStyleSheet()
from interfaces.scripts.userSetup import getAssetManagerPath
AMS_pathDict = getAssetManagerPath()

def getMayaWindow():
    """
    Get Maya window
    :return: maya wnd
    """
    mayaMainWindowPtr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(mayaMainWindowPtr), qw.QWidget)

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
        gmw = getMayaWindow()
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
        self.setStyleSheet(Mstyle.QWidget())
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
        mainGrp.setStyleSheet(Mstyle.QGroupBox())

        dirs = os.listdir(self.iconPath + '\\toolBoxUI')
        files = []
        for d in dirs:
            if os.path.isfile(os.path.join(self.iconPath + '\\toolBoxUI', d)):
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
            combiePath = self.iconPath + '\\toolBoxUI\\' + f
            Btn.setIcon(QtGui.QIcon(combiePath))
            Btn.setIconSize(QtCore.QSize(32, 32))
            Btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
            Btn.setAutoRaise(True)
            Btn.clicked.connect(self.BtnA1Fn)
            Btn.setStyleSheet(Mstyle.QToolButton())
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
            checkPath = self.iconPath + '\\toolBoxUI\\definedIcon\\' + inputStr + '.png'

            ext = os.path.isfile(checkPath)
            if ext:
                isAuto = False
            else:
                isAuto = True
                isDef = False

        elif not isAuto and not isDef and not isFull:
            isAuto = True

        if isBaseRoot:
            returnIcon = QtGui.QIcon(self.iconPath + '\\toolBoxUI\\' + inputStr)

        elif isDef:
            iconPath = self.iconPath + '\\toolBoxUI\\definedIcon\\' + inputStr + '.png'
            returnIcon = QtGui.QIcon(iconPath)

        elif isAuto:
            sum = 0
            for i in str(inputStr):
                num = ord(i)
                sum = sum + num
            random.seed(sum)
            rValue = random.random()
            # sum all char number of ASCII.random it to calculate the seed
            dirs = os.listdir(self.iconPath + '\\toolBoxUI')
            files = []
            for d in dirs:
                if os.path.isfile(os.path.join(self.iconPath + '\\toolBoxUI', d)):
                    files.append(d)
            # collect all picture in folder

            count = len(files)
            cnt = int(count * rValue)
            returnIcon = QtGui.QIcon(self.iconPath + '\\toolBoxUI\\' + files[cnt])
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

            self.setStyleSheet(Mstyle.QListWidget(fontSize=str(self.mainSize) + 'px', bordRad='0px'))
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
        self.drag.exec_(Qt.CopyAction)
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
        self.setContextMenuPolicy(Qt.CustomContextMenu)
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
        self.contextMenu.exec_(QtGui.QCursor.pos())  # show menu on cursor pos

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
            return;
        if not self.isDrag:
            return;

        # initPath='D:\\Lighting_tool_box'
        path = self.pluginsPath + '\\' + self.pageName + '\\' + self.fileName
        mimeData = QtCore.QMimeData();
        url = QtCore.QUrl.fromLocalFile(QtCore.QFileInfo(path).absoluteFilePath());
        mimeData.setUrls([url])
        self.drag = qw.QDrag(self);
        self.drag.setMimeData(mimeData);
        self.drag.setHotSpot(e.pos() - self.rect().topLeft());
        self.drag.exec_(Qt.CopyAction);
        e.accept();


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
        self.drag = QtGui.QDrag(self)
        self.drag.setMimeData(mimeData)
        self.drag.setHotSpot(e.pos() - self.rect().topLeft())
        self.drag.exec_(Qt.CopyAction)
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
        self.contextMenu.setStyleSheet(Mstyle.QMenu())
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
        self.contextMenu.exec_(QtGui.QCursor.pos())  # show menu on cursor pos


class detailGroupBox(qw.QGroupBox, chooseIcon):
    fileName = ''
    jsonPath = ''
    iconPath = ''
    pName = ''
    x = 150
    y = 120
    defaultTxt = '......'
    pluginsPath = ''

    # saveSignal = QtCore.Signal(str)
    def __init__(self, parent=None):
        qw.QGroupBox.__init__(self)

        self.setTitle('detail')
        self.setGeometry(5, 20, 0, 0)

        self.Btn = dragToolButton(self)
        self.sLabel0 = qw.QLabel(self)
        self.sLabel1 = qw.QLabel(self)
        self.sBtn1 = qw.QToolButton(self)
        self.sBtn2 = qw.QToolButton(self)
        self.sBtn3 = qw.QToolButton(self)
        self.sBtn4 = qw.QToolButton(self)
        self.sBtn5 = qw.QToolButton(self)
        self.sBtn6 = qw.QToolButton(self)
        self.dataEdit = qw.QTextEdit(self)

    def setPath(self, pageName):
        self.Btn.pageName = pageName
        self.setTitle('detail_' + pageName)

    def CreateUI(self):
        self.setStyleSheet(Mstyle.QGroupBox())

        self.Btn.iconPath = self.iconPath
        self.Btn.pluginsPath = self.pluginsPath
        self.Btn.setFixedSize(100, 100)
        self.Btn.setGeometry(5, 15, 0, 0)
        self.Btn.setIcon(QtGui.QIcon(self.chooseIcon('r')))
        self.Btn.setIconSize(QtCore.QSize(100, 100))
        self.Btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.Btn.setAutoRaise(True)
        self.Btn.setAcceptDrops(True)
        self.Btn.isBig = True

        self.sLabel0.setGeometry(110, 10, 0, 0)
        self.sLabel0.setStyleSheet(Mstyle.QLabel(fontSize='15px', lang='c'))

        self.sLabel1.setGeometry(110, 95, 0, 0)
        self.sLabel1.setFixedSize(30, 20)

        self.sBtn1.setGeometry(300, 97, 0, 0)
        self.sBtn1.setFixedSize(20, 20)
        self.sBtn1.setText('lockEdit')
        self.sBtn1.setToolTip('lock & edit texing block')
        self.sBtn1.setIcon(QtGui.QIcon(self.chooseIcon('lock', isDef=True)))
        self.sBtn1.setIconSize(QtCore.QSize(16, 16))
        self.sBtn1.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.sBtn1.setAutoRaise(True)

        self.sBtn2.setGeometry(280, 97, 0, 0)
        self.sBtn2.setFixedSize(20, 20)
        self.sBtn2.setText('save')
        self.sBtn2.setToolTip('save texing block')
        self.sBtn2.setIcon(QtGui.QIcon(self.chooseIcon('save', isDef=True)))
        self.sBtn2.setIconSize(QtCore.QSize(16, 16))
        self.sBtn2.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.sBtn2.setAutoRaise(True)

        self.sBtn3.setGeometry(140, 97, 0, 0)
        self.sBtn3.setFixedSize(20, 20)
        self.sBtn3.setText('clock')
        self.sBtn3.setToolTip('display histroy')
        self.sBtn3.setIcon(QtGui.QIcon(self.chooseIcon('clock', isDef=True)))
        self.sBtn3.setIconSize(QtCore.QSize(16, 16))
        self.sBtn3.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.sBtn3.setAutoRaise(True)
        self.sBtn3.setCheckable(True)

        self.sBtn4.setGeometry(160, 97, 0, 0)
        self.sBtn4.setFixedSize(20, 20)
        self.sBtn4.setText('chinese')
        self.sBtn4.setToolTip('display chinese document')
        self.sBtn4.setIcon(QtGui.QIcon(self.chooseIcon('chinese', isDef=True)))
        self.sBtn4.setIconSize(QtCore.QSize(16, 16))
        self.sBtn4.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.sBtn4.setAutoRaise(True)
        self.sBtn4.setCheckable(True)

        self.sBtn5.setGeometry(180, 97, 0, 0)
        self.sBtn5.setFixedSize(20, 20)
        self.sBtn5.setText('english')
        self.sBtn5.setToolTip('display english document')
        self.sBtn5.setIcon(QtGui.QIcon(self.chooseIcon('english', isDef=True)))
        self.sBtn5.setIconSize(QtCore.QSize(16, 16))
        self.sBtn5.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.sBtn5.setAutoRaise(True)
        self.sBtn5.setCheckable(True)
        self.sBtn5.setChecked(True)

        self.sBtn6.setGeometry(200, 97, 0, 0)
        self.sBtn6.setFixedSize(20, 20)
        self.sBtn6.setText('korea')
        self.sBtn6.setToolTip('display korea document')
        self.sBtn6.setIcon(QtGui.QIcon(self.chooseIcon('korea', isDef=True)))
        self.sBtn6.setIconSize(QtCore.QSize(16, 16))
        self.sBtn6.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.sBtn6.setAutoRaise(True)
        self.sBtn6.setCheckable(True)

        self.dataEdit.setReadOnly(True)
        self.dataEdit.setUndoRedoEnabled(True)
        self.dataEdit.setFixedSize(225, 60)
        self.dataEdit.setGeometry(110, 35, 0, 0)
        self.dataEdit.setStyleSheet(Mstyle.QTextEdit(kw='a', lang='c', fontSize='12px'))

        self.sBtn1.clicked.connect(self.swithWritable)
        self.sBtn2.clicked.connect(self.saveHelp)
        self.sBtn3.clicked.connect(self.swithHistroy)

        self.sBtn4.clicked.connect(self.sBtn4Fn)
        self.sBtn5.clicked.connect(self.sBtn5Fn)
        self.sBtn6.clicked.connect(self.sBtn6Fn)

    def sBtn4Fn(self):
        check = self.sender().isChecked()
        if check:
            self.sBtn6.setChecked(False)
            self.sBtn5.setChecked(False)
        else:
            self.sender().setChecked(True)

        eText = self.dataEdit
        tNode = self.Btn
        tx = self.title().split('_')[1]

        attrDict = {}
        itemDict = {}
        data = self.loadJson(self.jsonPath)
        if tx in data.keys():
            itemDict = data[tx]
            if tNode.fileName in itemDict.keys():
                attrDict = itemDict[tNode.fileName]

        txtValue = self.defaultTxt
        if attrDict:
            if 'ch' in attrDict.keys():
                txtValue = attrDict['ch']

        eText.setText(txtValue)

    def sBtn5Fn(self):
        check = self.sender().isChecked()
        if check:
            self.sBtn4.setChecked(False)
            self.sBtn6.setChecked(False)
        else:
            self.sender().setChecked(True)

        eText = self.dataEdit
        tNode = self.Btn
        tx = self.title().split('_')[1]

        attrDict = {}
        itemDict = {}
        data = self.loadJson(self.jsonPath)
        if tx in data.keys():
            itemDict = data[tx]
            if tNode.fileName in itemDict.keys():
                attrDict = itemDict[tNode.fileName]

        txtValue = self.defaultTxt
        if attrDict:
            if 'en' in attrDict.keys():
                txtValue = attrDict['en']

        eText.setText(txtValue)

    def sBtn6Fn(self):
        check = self.sender().isChecked()
        if check:
            self.sBtn4.setChecked(False)
            self.sBtn5.setChecked(False)
        else:
            self.sender().setChecked(True)

        eText = self.dataEdit
        tNode = self.Btn
        tx = self.title().split('_')[1]

        attrDict = {}
        data = self.loadJson(self.jsonPath)
        if tx in data.keys():
            itemDict = data[tx]
            if tNode.fileName in itemDict.keys():
                attrDict = itemDict[tNode.fileName]

        txtValue = self.defaultTxt
        if attrDict:
            if 'ko' in attrDict.keys():
                txtValue = attrDict['ko']

        eText.setText(txtValue)

    def resumeLastLang(self):
        nowText = ''
        lang = ''
        pageName = self.Btn.pageName
        fullName = self.fileName
        jsonPath = self.jsonPath

        data = self.loadJson(jsonPath)
        if pageName in data.keys():
            if fullName in data[pageName].keys():
                # print data[pageName].keys()
                if 'lastLang' in data[pageName][fullName].keys():
                    lang = data[pageName][fullName]['lastLang']
                    nowText = data[pageName][fullName][lang]
        if lang == 'en':
            self.sBtn5Fn()
        if lang == 'ch':
            self.sBtn4Fn()
        if lang == 'ko':
            self.sBtn6Fn()
        self.dataEdit.setText(nowText)

    def setText(self):
        pageName = self.Btn.pageName
        fullName = self.fileName
        nowText = '........'
        jsonPath = self.jsonPath
        data = self.loadJson(jsonPath)
        if pageName in data.keys():
            if fullName in data[pageName].keys():
                # print data[pageName].keys()
                if 'en' in data[pageName][fullName].keys():
                    nowText = data[pageName][fullName]['en']

        self.dataEdit.setText(nowText)

    def text(self):
        return self.dataEdit.text()

    def setFileName(self, theName):
        if not ('.' in theName):
            self.sLabel0.setText(theName)
            self.sLabel1.setText('none')
        else:
            spStr = theName.split('.')
            sp = '.'.join(spStr[0:-1])
            self.sLabel1.setText(spStr[-1])
            self.sLabel0.setText(sp)

        self.Btn.setToolTip(theName)
        self.Btn.fileName = theName
        self.fileName = theName

    def getFileName(self):
        return self.fileName

    def setDetailIcon(self, theIconPath):
        self.Btn.setIcon(QtGui.QIcon(
            self.chooseIcon(theIconPath[0], isAuto=theIconPath[1], isDef=theIconPath[2], isBaseRoot=theIconPath[3])))
        self.Btn.iconName = theIconPath

    def detailIcon(self):
        return self.Btn.iconName

    def setX(self, xValue):
        self.x = xValue
        self.setFixedSize(self.x, self.y)
        self.sLabel0.setFixedSize(self.x * 0.64, 20)

    # ---------------------

    def swithWritable(self):
        sender = self.sender()
        eText = self.dataEdit
        check = eText.isReadOnly()
        if check:
            eText.setReadOnly(False)
            sender.setIcon(self.chooseIcon('unlock', isDef=True))
            eText.setStyleSheet(Mstyle.QTextEdit(kw='b', lang='c', fontSize='12px'))
        else:
            eText.setReadOnly(True)
            sender.setIcon(self.chooseIcon('lock', isDef=True))
            eText.setStyleSheet(Mstyle.QTextEdit(kw='a', lang='c', fontSize='12px'))

    def swithHistroy(self):
        sender = self.sender()
        mBtn = self.Btn
        eText = self.dataEdit
        pageName = self.title().split('_')[1]

        nowText = self.defaultTxt
        fullName = self.fileName

        kt = 'en'
        isCh = self.sBtn4.isChecked()
        if isCh: kt = 'ch'
        isKo = self.sBtn6.isChecked()
        if isKo: kt = 'ko'
        jsonPath = self.jsonPath
        data = self.loadJson(jsonPath)

        if pageName in data.keys():
            if fullName in data[pageName].keys():
                # print data[pageName].keys()
                if kt in data[pageName][fullName].keys():
                    nowText = data[pageName][fullName][kt]

        check = sender.isChecked()
        f = self.pluginsPath + '\\' + pageName + '\\' + fullName

        mtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(f)))
        ctime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(f)))
        hisTex = 'modify : ' + mtime + '\ncreate : ' + ctime + '\ncreator:unknow'

        if check:
            sender.setIcon(self.chooseIcon('clock_fill', isDef=True))
            eText.setText(hisTex)
        else:
            sender.setIcon(self.chooseIcon('clock', isDef=True))
            eText.setText(nowText)

    def saveHelp(self):
        sender = self.sender()
        eText = self.dataEdit
        tNode = self.Btn
        tx = self.title().split('_')[1]

        attrDict = {}
        itemDict = {}
        data = self.loadJson(self.jsonPath)
        if tx in data.keys():
            itemDict = data[tx]
            if tNode.fileName in itemDict.keys():
                attrDict = itemDict[tNode.fileName]

        attrDict.update({'icon': tNode.iconName})
        isEn = self.sBtn5.isChecked()
        isCh = self.sBtn4.isChecked()
        isKo = self.sBtn6.isChecked()
        if isEn:
            attrDict.update({'en': eText.toPlainText()})
            attrDict.update({'lastLang': 'en'})
        if isCh:
            attrDict.update({'ch': eText.toPlainText()})
            attrDict.update({'lastLang': 'ch'})
        if isKo:
            attrDict.update({'ko': eText.toPlainText()})
            attrDict.update({'lastLang': 'ko'})

        attrDict.update({'history': 'nothing!'})
        itemDict.update({tNode.fileName: attrDict})
        data.update({tNode.pageName: itemDict})

        if not os.path.exists(self.jsonPath):
            self.saveJson({}, self.jsonPath)

        self.saveJson(data, self.jsonPath)

    # ------event rewrite-----------

    def saveJson(self, data, path):
        jsonDump = json.dumps(data)
        file_object = open(path, 'w')
        file_object.write(jsonDump)
        file_object.close()

    def loadJson(self, path):
        file_object = open(path, 'r')
        data = json.load(file_object)
        return data


class MDtoolBoxUI(MayaQWidgetDockableMixin, qw.QDialog, chooseIcon):
    titleName = 'MDtoolBoxUI'
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
        self.cleanOpenWindow()
        super(MDtoolBoxUI, self).__init__(parent=parent)
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle(self.titleName)
        self.setFixedWidth(self.widgetWidth)
        self.setAcceptDrops(True)

        self.localPath = r'D:\Program Files\figo\CommonToolBox_Local'
        self.localJson = self.localPath + '\\log.json'

        if not os.path.exists(self.localPath):
            os.makedirs(self.localPath)
        if not os.path.exists(self.localJson):
            self.saveJson({'current': 'model'}, self.localJson)

        currentData = self.loadJson(self.localJson)
        current = currentData['current']

        self.pathDict = AMS_pathDict
        self.initPath = self.pathDict['main']
        self.iconPath = self.pathDict['icon']
        self.jsonPath = self.pathDict['data'] + '\\appHelps.json'
        self.pluginsPath = self.pathDict[current.lower()] + '\\plugins'
        self.createForm()
        self.createUI()

        if self.isShowDetail:
            Idx = self.QTwidget.currentIndex()
            pageN = self.QTwidget.tabText(Idx)
            print 'fffffff'
            print self.UIitems
            if self.UIitems[pageN]:
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
        self.searchGb.setFixedSize(self.widgetWidth * 0.98, 50)
        self.searchGb.setGeometry(5, 135, 5, 5)
        searchLy = qw.QHBoxLayout(self)

        searchLab = qw.QLabel('search : ', self)
        searchLy.addWidget(searchLab)
        self.LE = qw.QLineEdit('', self)
        self.LE.setStyleSheet(Mstyle.QLineEdit(kw='c', lang='c'))
        searchLy.addWidget(self.LE)

        s1Mn = qw.QMenu()
        s1Mnact1 = qw.QAction('List Form', s1Mn)
        s1Mn.addAction(s1Mnact1)
        s1Mnact2 = qw.QAction('Block Form', s1Mn)
        s1Mn.addAction(s1Mnact2)

        searchBtn1 = qw.QToolButton(self)
        searchBtn1.setFixedSize(20, 20)
        searchBtn1.setToolTip('change widget form')

        searchBtn1.setIcon(self.chooseIcon('more', isDef=True))
        searchBtn1.setIconSize(QtCore.QSize(20, 20))
        searchBtn1.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        searchBtn1.setAutoRaise(True)
        searchBtn1.setMenu(s1Mn)
        searchBtn1.setPopupMode(searchBtn1.InstantPopup)
        searchLy.addWidget(searchBtn1)

        self.searchBtn2 = qw.QToolButton(self)
        self.searchBtn2.setToolTip('on/off drag mode')
        self.searchBtn2.setFixedSize(20, 20)
        self.searchBtn2.setIcon(self.chooseIcon('drag', isDef=True))
        self.searchBtn2.setIconSize(QtCore.QSize(20, 20))
        self.searchBtn2.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.searchBtn2.setAutoRaise(True)
        self.searchBtn2.setCheckable(True)
        searchLy.addWidget(self.searchBtn2)

        searchBtn3 = qw.QToolButton(self)
        searchBtn3.setFixedSize(20, 20)
        searchBtn3.setToolTip('open current folder')
        searchBtn3.setIcon(self.chooseIcon('floder', isDef=True))
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
        searchBtn4.setIcon(self.chooseIcon('activity', isDef=True))
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
        self.QTwidget.setGeometry(5, 175, 5, 5)
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
        self.QTwidget.setGeometry(5, 50, 5, 5)
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
        self.QTwidget.setMinimumSize(self.widgetWidth * 0.98, self.widgetHeight * 0.2)
        self.QTwidget.setGeometry(5, self.tabY, 5, 5)
        self.QTwidget.setTabPosition(qw.QTabWidget.West)
        self.QTwidget.setStyleSheet(Mstyle.QTabWidget())
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
        listWd.setAttribute(QtCore.Qt.WA_StyledBackground)
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
        self.list.setStyleSheet(Mstyle.QListWidget(fontSize=str(itemSize) + 'px', bordRad='0px'))
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
        epScroll.setWidget(epWd)
        epScroll.setStyleSheet(Mstyle.QScrollBar() + 'QScrollArea {background:rgb(109,109,109);border:0;}')

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

        widHeight = (int(len(flns) / spacing) + 1) * 95

        epWd.setFixedSize((spacing) * 105, widHeight)
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
        if os.path.exists(self.pluginsPath):
            dirs = os.listdir(self.pluginsPath)
            floder = []
            for d in dirs:
                if (not os.path.isfile(os.path.join(self.pluginsPath, d))) and d != 'data':
                    floder.append(d)
            return floder
        else:
            raise IOError(self.pluginsPath + ' not exists!!')
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
        if self.widgetHeight > 300:
            self.QTwidget.setFixedSize(int(self.widgetWidth * 0.98), int(self.widgetHeight - dHeight))

        Idx = self.QTwidget.currentIndex()
        cwd = self.QTwidget.widget(Idx)
        if '_list' in cwd.statusTip():
            cwd.children()[0].setFixedSize(int(self.widgetWidth * 0.875), int(self.widgetHeight - dHeight))

    # ------ button functions ------------------------------

    def fileMn1actFn(self):
        print 'change icon'
        iconUI = chooseIconByUserUI()
        iconUI.setParent(getMayaWindow())
        # D:\AssetManegerSystem_publish\icon\avarter
        iconUI.iconPath = self.iconPath
        iconUI.CreateUI()
        iconUI.posX = QtGui.QCursor.pos().x()
        iconUI.posY = QtGui.QCursor.pos().y()
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
        if Idx and cwd:
            if '_list' in cwd.statusTip():
                cwd.children()[0].setFixedSize(int(self.widgetWidth * 0.875), int(self.widgetHeight - 180))

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
        self.refreshListHeight(dHeight=self.tabY)

    def dragEnterEvent(self, e):
        if (e.mimeData().hasFormat("text/uri-list")):
            e.acceptProposedAction()

    def mousePressEvent(self, e):
        if (e.button() == QtCore.Qt.LeftButton):
            pass
            # drag = qw.QDrag(self)
            # data = qw.QMimeData
            # e.setMimeData(data)
            # e.exec(QtCore.Qt.MoveAction)

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

    def closeEvent(self, e):
        self.deleteLater()
        
    def deleteControl(self, control):

        if cmds.workspaceControl(control, q=True, exists=True):
            cmds.workspaceControl(control, e=True, close=True)
            cmds.deleteUI(control, control=True)
            
    # ------------widget enter--------------
    def Op_Ui(self):
        ans = cmds.about(version=True)
        if int(ans)>2016:
            self.setObjectName("MyMainDockingWindow")

            # The deleteInstances() dose not remove the workspace control, and we need to remove it manually
            workspaceControlName = self.objectName() + 'WorkspaceControl'
            self.deleteControl(workspaceControlName)

            # this class is inheriting MayaQWidgetDockableMixin.show(), which will eventually call maya.cmds.workspaceControl.
            # I'm calling it again, since the MayaQWidgetDockableMixin dose not have the option to use the "tabToControl" flag,
            # which was the only way i found i can dock my window next to the channel controls, attributes editor and modelling toolkit.
            self.show(dockable=True, area='right', floating=False)
            
            cmds.workspaceControl(workspaceControlName, e=True, ttc=["AttributeEditor", -1], wp="preferred", mw=self.widgetWidth)

            self.raise_()

        else:
            self.show()
            self.setDockableParameters(dockable=True, floating=False, area='left')
            self.raise_()


def main():
    
    MDtoolBUI = MDtoolBoxUI()
    MDtoolBUI.Op_Ui()
    
    
    
#if __name__ == '__main__':
    
#MDtoolBUI = MDtoolBoxUI()
#MDtoolBUI.Op_Ui()






