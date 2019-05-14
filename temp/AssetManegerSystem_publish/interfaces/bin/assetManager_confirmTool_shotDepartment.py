# -*- coding:gbk -*-
import maya.cmds as cmds
import maya.mel as mel
from PySide import QtCore, QtGui
from PySide.QtCore import Qt
import shutil
import datetime
import time
import _winreg
import json
import maya.OpenMayaUI as OpenMayaUI
from shiboken import wrapInstance

class HoverRadioButton(QtGui.QRadioButton):
    def __init__(self, parent=None):
        QtGui.QRadioButton.__init__(self, parent)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        self.setChecked(True)

class assetManager_confirmTool_shotDepartment(QtGui.QMainWindow):
    checkClicked = QtCore.Signal(list)
    confirmClicked = QtCore.Signal(list)
    workName = ''
    jsonPath = ''
    searchPath = ''
    titleName = 'confirmDialog'
    localPath = ''
    serverPath = ''

    def __init__(self, parent=None):
        super(assetManager_confirmTool_shotDepartment, self).__init__(parent)
        # ------Style Set----------------------------
        self.m_DragPosition = self.pos()
        self.setWindowTitle(self.titleName)
        self.resize(600, 480)
        self.move(0, 0)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.Widget | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet('QWidget{background:rgb(68,68,68)}')
        self.pathDict = getAssetManagerPath()

    def createUI(self):

        self.mainWidget = QtGui.QWidget(self)
        self.mainWidget.setAttribute(Qt.WA_SetStyle)
        # -----close Btn Set----------------
        mv = QtGui.QVBoxLayout()
        th = QtGui.QHBoxLayout()

        Xbtn = QtGui.QPushButton('x')
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())

        Xbtn.clicked.connect(self.Cl_Ui)
        th.addWidget(Xbtn)
        th.addStretch(1)
        # ----TitleLabel-----------------------
        TitleLab = QtGui.QLabel(self.workName + ' confirm')
        TitleLab.setFixedHeight(20)
        TitleLab.setFixedWidth(140)
        TitleLab.setStyleSheet(Mstyle.QLabel(fontSize='12px'))
        th.addWidget(TitleLab)
        th.addStretch(1)
        mv.addLayout(th)

        # ------main items-----------------------
        codec = QtCore.QTextCodec.codecForName("GB2312")

        splitter = QtGui.QSplitter()
        splitter.setGeometry(0, 20, 0, 0)
        splitter.setOrientation(Qt.Horizontal)
        splitter.setObjectName("splitter")
        mv.addWidget(splitter)
        # create spliter over.



        wid_left = QtGui.QWidget(self)
        wid_left.resize(self.width() * 0.35, self.height())
        wid_left.setParent(splitter)

        leftV = QtGui.QVBoxLayout()
        wid_left.setLayout(leftV)



        self.LE = QtGui.QListWidget()
        self.LE.setFocusPolicy(Qt.NoFocus)
        self.LE.setSortingEnabled(True)
        self.LE.setStyleSheet(Mstyle.QListWidget(fontSize='12px') + 'QListWidget{outline:0px;}')
        leftV.addWidget(self.LE)

        # lef list create over.
        mdGrp = QtGui.QGroupBox('detail')
        mdGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        mdGrp.resize(self.width() * 0.65, self.height())
        mdGrp.setParent(splitter)

        Vbox = QtGui.QVBoxLayout()
        Vbox.setContentsMargins(0, 5, 0, 5)
        mdGrp.setLayout(Vbox)

        Hbox1 = QtGui.QHBoxLayout()
        Hbox1.setAlignment(Qt.AlignHCenter)
        self.iconLab = QtGui.QLabel()
        Hbox1.addWidget(self.iconLab)

        self.nameLab = QtGui.QLabel('name')
        self.nameLab.setFixedHeight(20)
        self.nameLab.setStyleSheet(Mstyle.QLabel(fontSize='15px') + 'QLabel {background:transparent;}')
        Hbox1.addWidget(self.nameLab)
        # pathDict self.iconLab

        # --------------------------------------------------------
        self.scrollWidget = QtGui.QWidget()
        self.scrollWidget.setAttribute(Qt.WA_SetStyle)
        self.scrollWidget.setStyleSheet(Mstyle.QWidget() + 'QWidget {background:transparent;}')
        self.scrollWidget.setFixedWidth(self.width() * 0.555)

        scrollArea = QtGui.QScrollArea(mdGrp)
        scrollArea.setWidget(self.scrollWidget)
        scrollArea.setWidgetResizable(True)
        scrollArea.setStyleSheet(Mstyle.QScrollBar() + 'QScrollArea {border:0px;background:transparent;}')
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        scrollVBox = QtGui.QVBoxLayout()
        self.scrollWidget.setLayout(scrollVBox)
        # --------------------------------------------------------

        picGrp = QtGui.QGroupBox('picture:')
        picGrp.resize(self.width() * 0.65, 50)
        picGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        picVbox = QtGui.QVBoxLayout()
        picVbox.setAlignment(Qt.AlignHCenter)
        picGrp.setLayout(picVbox)

        self.imageLab = QtGui.QLabel()

        imageH = QtGui.QHBoxLayout()
        self.btnGrp = QtGui.QButtonGroup()
        self.btnGrp.setExclusive(True)

        radbtn1 = HoverRadioButton()
        radbtn1.setStyleSheet(Mstyle.QRadioButton() + 'QRadioButton {background:transparent}')
        radbtn1.setChecked(True)
        imageH.addWidget(radbtn1)
        self.btnGrp.addButton(radbtn1, 0)

        radbtn2 = HoverRadioButton()
        radbtn2.setStyleSheet(Mstyle.QRadioButton() + 'QRadioButton {background:transparent}')
        self.btnGrp.addButton(radbtn2, 1)
        imageH.addWidget(radbtn2)

        radbtn3 = HoverRadioButton()
        radbtn3.setStyleSheet(Mstyle.QRadioButton() + 'QRadioButton {background:transparent}')
        self.btnGrp.addButton(radbtn3, 2)
        imageH.addWidget(radbtn3)

        playBtn = QtGui.QPushButton()
        playBtn.setText('play preview')
        playBtn.setFixedSize(120, 20)
        playBtn.setStyleSheet(Mstyle.QPushButton())
        imageH.addWidget(playBtn)

        picVbox.addWidget(self.imageLab)
        picVbox.addLayout(imageH)

        # pictures over ------------------------------------

        msgGrp = QtGui.QGroupBox('informations:')
        msgGrp.setFixedHeight(80)
        msgGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        msgVbox = QtGui.QVBoxLayout()
        msgGrp.setLayout(msgVbox)
        Vbox.addWidget(msgGrp)

        msgH1 = QtGui.QHBoxLayout()
        msgLabTitle = QtGui.QLabel('lastMessage : ', msgGrp)
        msgLabTitle.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        self.msgLab = QtGui.QLabel('', msgGrp)
        self.msgLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        msgH1.addWidget(msgLabTitle)
        msgH1.addWidget(self.msgLab)
        msgVbox.addLayout(msgH1)

        msgH2 = QtGui.QHBoxLayout()
        artLabTitle = QtGui.QLabel('artist : ', msgGrp)
        artLabTitle.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        self.artLab = QtGui.QLabel('', msgGrp)
        self.artLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        msgH2.addWidget(artLabTitle)
        msgH2.addWidget(self.artLab)
        msgVbox.addLayout(msgH2)

        msgH3 = QtGui.QHBoxLayout()
        machLabTitle = QtGui.QLabel('machine : ', msgGrp)
        machLabTitle.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        self.machLab = QtGui.QLabel('', msgGrp)
        self.machLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        msgH3.addWidget(machLabTitle)
        msgH3.addWidget(self.machLab)
        msgVbox.addLayout(msgH3)

        # --------------------------------------------------------


        artGrp = QtGui.QGroupBox('assetList:')
        artGrp.setFixedHeight(150)
        artGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        artVbox = QtGui.QVBoxLayout()
        artGrp.setLayout(artVbox)
        Vbox.addWidget(artGrp)
        self.assetList = QtGui.QListWidget(artGrp)
        self.assetList.setStyleSheet(Mstyle.QListWidget(fontSize='12px'))
        artVbox.addWidget(self.assetList)

        # --------------------------------------------------------

        keyframeGrp = QtGui.QGroupBox('keyFrame:')
        keyframeGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        keyframeVbox = QtGui.QVBoxLayout()
        keyframeGrp.setLayout(keyframeVbox)
        Vbox.addWidget(keyframeGrp)

        keyH1 = QtGui.QHBoxLayout()
        self.startKeyLab = QtGui.QLabel('', keyframeGrp)
        self.startKeyLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        keyH1.addWidget(self.startKeyLab)

        connectKeyLab1 = QtGui.QLabel('f to')
        connectKeyLab1.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        keyH1.addWidget(connectKeyLab1)

        self.endKeyLab = QtGui.QLabel('', keyframeGrp)
        self.endKeyLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        keyH1.addWidget(self.endKeyLab)

        connectKeyLab1 = QtGui.QLabel('f ')
        connectKeyLab1.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        keyH1.addWidget(connectKeyLab1)

        self.fpsLab = QtGui.QLabel('', keyframeGrp)
        self.fpsLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        keyH1.addWidget(self.fpsLab)
        keyframeVbox.addLayout(keyH1)

        # --------------------------------------------------------

        confirmMsgGrp = QtGui.QGroupBox('left confirm message:')
        confirmMsgGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        confirmMsgVbox = QtGui.QVBoxLayout()
        confirmMsgGrp.setLayout(confirmMsgVbox)
        Vbox.addWidget(confirmMsgGrp)
        self.confirmMsgLab = QtGui.QLabel('this function not install', confirmMsgGrp)
        self.confirmMsgLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        confirmMsgVbox.addWidget(self.confirmMsgLab)

        # --------------------------------------------------------

        feedbackGrp = QtGui.QGroupBox('write feed back:')
        feedbackGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        feedbackVbox = QtGui.QVBoxLayout()
        feedbackGrp.setLayout(feedbackVbox)
        Vbox.addWidget(feedbackGrp)
        self.feedbackLab = QtGui.QLabel('this function not install', feedbackGrp)
        self.feedbackLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        feedbackVbox.addWidget(self.feedbackLab)

        # --------------------------------------------------------

        hbox2 = QtGui.QHBoxLayout()
        self.BtnA1 = QtGui.QPushButton('check')
        self.BtnA1.setStyleSheet(Mstyle.QPushButton(kw='b'))
        self.BtnA1.setEnabled(False)
        self.BtnA2 = QtGui.QPushButton('confirm')
        self.BtnA2.setStyleSheet(Mstyle.QPushButton(kw='off'))
        self.BtnA2.setEnabled(False)
        hbox2.addWidget(self.BtnA1)
        hbox2.addWidget(self.BtnA2)

        scrollVBox.addWidget(picGrp)
        scrollVBox.addWidget(msgGrp)
        scrollVBox.addWidget(artGrp)
        scrollVBox.addWidget(keyframeGrp)
        scrollVBox.addWidget(confirmMsgGrp)
        scrollVBox.addWidget(feedbackGrp)


        Vbox.addLayout(Hbox1)
        Vbox.addWidget(scrollArea)
        #Vbox.addStretch(1)
        Vbox.addLayout(hbox2)
        self.mainWidget.setLayout(mv)

        self.fillListWidget()  # fill List Widget
        # ------main btn connect----------------------------

        self.BtnA1.clicked.connect(self.BtnA1Fn)
        self.BtnA2.clicked.connect(self.BtnA2Fn)
        self.LE.currentItemChanged.connect(self.changeItemFn)
        playBtn.clicked.connect(self.playPreviewFn)

        radbtn1.toggled.connect(self.changeHoverPicFn)
        radbtn2.toggled.connect(self.changeHoverPicFn)
        radbtn3.toggled.connect(self.changeHoverPicFn)

        splitter.splitterMoved.connect(self.splitMoveFn)
    # --------main function--------------
    def splitMoveFn(self,x,y):
        rightWidth = self.width() - x - 30
        self.scrollWidget.setFixedWidth(rightWidth)

    def changeHoverPicFn(self):
        if self.picArray:
            self.picArray.sort()
            self.nowPicture = self.picArray[self.btnGrp.checkedId()]
            theImage = QtGui.QImage(self.nowPicture)
            imagePixmap = QtGui.QPixmap.fromImage(theImage)
            imagePixmap = imagePixmap.scaledToWidth(300)
            self.imageLab.setPixmap(imagePixmap)
        else:
            imagePixmap = QtGui.QPixmap()
            self.imageLab.setPixmap(imagePixmap)

    def playPreviewFn(self):
        try:
            os.startfile(self.nowPreview)
        except:
            pass

    def changeItemFn(self, item):
        message = ''
        artist = ''
        machine = ''
        name = 'name'

        if item:
            self.jsonArray = []
            self.picArray = []
            self.maArray = []
            self.aviArray = []
            self.nowPreview = ''
            self.infoPath = ''
            self.keyPath = ''
            self.infoPath = ''
            self.keyframePath = ''
            self.assetlistPath = ''
            self.nowPicture = ''
            self.maPath = ''
            self.cameraPath = ''
            iCount = self.LE.count()
            itemArray = []
            for i in range(iCount):
                itemArray.append(int(self.LE.item(i).toolTip()))
            itemArray.sort()

            theStr = item.toolTip()
            name = '%s-%s-%s %s:%s:%s' % (theStr[0:4], theStr[4:6], theStr[6:8], theStr[8:10], theStr[10:12], theStr[12:14])
            iconImage = QtGui.QImage()
            self.iconPath = self.pathDict['icon']
            if int(theStr) == itemArray[-1]:
                iconImage.load(self.iconPath + '\\new.png')
            else:
                iconImage.load(self.iconPath + '\\file.png')
            iconPixmap = QtGui.QPixmap.fromImage(iconImage)
            self.iconLab.setPixmap(iconPixmap)

            # pathDict self.iconLab

            items = os.listdir(self.fullPath + theStr)

            for i in items:
                tempPath = self.fullPath + theStr + '\\' + i
                if os.path.isfile(tempPath):
                    if '.png' in i:
                        self.picArray.append(tempPath)
                    if '.ma' in i:
                        self.maArray.append(tempPath)
                    if '.json' in i:
                        self.jsonArray.append(tempPath)
                    if '.avi' in i:
                        self.aviArray.append(tempPath)
                else:
                    pass
                    # mel.eval('print "file maybe changed after submit"')

            for i in self.maArray:
                bName = os.path.basename(i)
                spi = bName.split('_')
                if (len(spi) == 3) and ('.' in spi[-1]):
                    self.maPath = i
                elif (len(spi) == 6) and ('Shape' in spi[-1]):
                    self.cameraPath = i
            print 'maPath : ' + self.maPath
            self.picArray.sort()
            self.nowPicture = self.picArray[self.btnGrp.checkedId()]
            self.nowPreview = self.aviArray[0]
            for i in self.jsonArray:
                li = i.lower()
                if 'timeNode.json' in li:
                    self.infoPath = i
                elif 'keyframe.json' in li:
                    self.keyframePath = i
                elif 'assetlist.json' in li:
                    self.assetlistPath = i

            if self.picArray:
                theImage = QtGui.QImage(self.nowPicture)
                imagePixmap = QtGui.QPixmap.fromImage(theImage)
                imagePixmap = imagePixmap.scaledToWidth(300)
                self.imageLab.setPixmap(imagePixmap)
            else:
                imagePixmap = QtGui.QPixmap()
                self.imageLab.setPixmap(imagePixmap)
            self.BtnA1.setEnabled(True)

            if os.path.exists(self.infoPath):
                jDict = self.loadJson(self.infoPath)
                if type(jDict) == dict:
                    message = jDict['lastUpload']['message']
                    machine = jDict['lastUpload']['machine']
                    artist = jDict['lastUpload']['artist']

            self.assetList.clear()
            if os.path.exists(self.assetlistPath):
                theData = self.loadJson(self.assetlistPath)
                shortArray = []
                for i in theData:
                    shortArray.append(os.path.basename(i))
                self.assetList.addItems(shortArray)

            self.startKeyLab.setText('')
            self.endKeyLab.setText('')
            self.fpsLab.setText('')
            if os.path.exists(self.keyframePath):
                theData = self.loadJson(self.keyframePath)
                self.startKeyLab.setText(str(theData['startKey']))
                self.endKeyLab.setText(str(theData['endKey']))
                self.fpsLab.setText(str(theData['fps']))
        else:
            self.BtnA1.setEnabled(False)
            self.BtnA2.setEnabled(False)
            self.BtnA2.setStyleSheet(Mstyle.QPushButton(kw='off'))
            imagePixmap = QtGui.QPixmap()
            self.imageLab.setPixmap(imagePixmap)

        self.nameLab.setText(name)
        self.machLab.setText(machine)
        self.artLab.setText(artist)
        self.msgLab.setText(message)

    def fillListWidget(self):
        self.LE.clear()
        self.fullPath = ''
        noLevel = True

        highPath = self.searchPath + '\\high\\'
        lowPath = self.searchPath + '\\low\\'

        if os.path.exists(highPath) or os.path.exists(lowPath):
            noLevel = False

        if self.btnGrp.checkedId() == 0:
            checkPath = self.searchPath + '\\high\\'
            if os.path.exists(checkPath):
                self.fullPath = checkPath
        else:
            checkPath = self.searchPath + '\\low\\'
            if os.path.exists(checkPath):
                self.fullPath = checkPath

        if noLevel:
            self.fullPath = self.searchPath + '\\'
            #self.lowTool.setVisible(False)
            #self.highTool.setVisible(False)

        Qarray = []
        if self.fullPath:
            items = os.listdir(self.fullPath)
            lastItem = ''
            for i in items:
                Qitem = QtGui.QListWidgetItem()
                newText = '%s-%s-%s %s:%s:%s' % (i[0:4], i[4:6], i[6:8], i[8:10], i[10:12], i[12:14])
                Qitem.setText(newText)
                Qitem.setToolTip(i)
                Qarray.append(Qitem)
                self.LE.addItem(Qitem)
                lastItem = Qitem
            self.LE.setCurrentItem(lastItem)

    def loadJson(self, path):
        file_object = open(path, 'r')
        data = json.load(file_object)
        return data

    def BtnA1Fn(self):
        if self.serverPath in self.maPath:
            localFile = self.maPath.replace(self.serverPath, self.localPath)
            dirName = os.path.dirname(localFile)
            if not os.path.exists(dirName):
                os.makedirs(dirName)
            shutil.copyfile(self.maPath, localFile)
            shutil.copystat(self.maPath, localFile)
            cmds.file(localFile, open=1, f=1)
        else:
            cmds.file(self.maPath, open=1, f=1)

        self.nowCheckingItem = self.LE.currentItem()
        self.nowCheckingPath = self.nowCheckingItem.toolTip()
        self.BtnA2.setEnabled(True)
        self.BtnA2.setStyleSheet(Mstyle.QPushButton())
        self.checkClicked.emit(['check', self.nowCheckingPath])

    def BtnA2Fn(self):
        self.LE.setCurrentItem(self.nowCheckingItem)
        ans = QtGui.QMessageBox.information(self, 'double check',
                                            'do you wanna confirm this file?\n' + self.nowCheckingItem.text(),
                                            QtGui.QMessageBox.Yes,
                                            QtGui.QMessageBox.No)
        if ans == QtGui.QMessageBox.Yes:
            self.confirmClicked.emit(['confirm', self.nowCheckingPath])
            self.Cl_Ui()

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

    def Op_Ui(self):
        self.show()

    def Cl_Ui(self):
        self.deleteLater()
        self.close()

    def resizeEvent(self, e):
        self.mainWidget.resize(e.size())


# cleanUIRT = assetManager_confirmTool()
# cleanUIRT.searchPath = 'W:\\project\\PIG\\asset\\MODEL\\Char\\testCha\\uploadTemp'
# cleanUIRT.localPath = 'D:\\localLibrary\\PIG'
# cleanUIRT.serverPath = 'W:\\project\\PIG'
# cleanUIRT.workName = 'testCha'

# cleanUIRT.createUI()
# cleanUIRT.fillListWidget()
# cleanUIRT.Op_Ui()

# cleanUIRT.Cl_Ui()