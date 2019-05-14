# -*- coding:gbk -*-
import maya.cmds as cmds
import maya.mel as mel
import shutil
import datetime
import time
import _winreg
import json
import maya.OpenMayaUI as OpenMayaUI

import Qt
from Qt import QtWidgets as qw,QtGui,QtCore


if Qt.IsPySide:
    from shiboken import wrapInstance
if Qt.IsPySide2:
    from shiboken2 import wrapInstance


class assetManager_confirmTool(qw.QMainWindow):
    checkClicked = QtCore.Signal(list)
    confirmClicked = QtCore.Signal(list)
    workName = ''
    jsonPath = ''
    searchPath = ''
    titleName = 'confirmDialog'
    localPath = ''
    serverPath = ''

    def __init__(self, parent=None):
        super(assetManager_confirmTool, self).__init__(parent)
        # ------Style Set----------------------------
        self.m_DragPosition = self.pos()
        self.setWindowTitle(self.titleName)
        self.resize(600, 480)
        self.move(0, 0)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet('QWidget{background:rgb(68,68,68)}')
        self.pathDict = getAssetManagerPath()

    def createUI(self):

        self.mainWidget = qw.QWidget(self)
        self.mainWidget.setAttribute(QtCore.Qt.WA_SetStyle)
        # -----close Btn Set----------------
        mv = qw.QVBoxLayout()
        th = qw.QHBoxLayout()

        Xbtn = qw.QPushButton('x')
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())

        Xbtn.clicked.connect(self.Cl_Ui)
        th.addWidget(Xbtn)
        th.addStretch(1)
        # ----TitleLabel-----------------------
        TitleLab = qw.QLabel(self.workName + ' confirm')
        TitleLab.setFixedHeight(20)
        TitleLab.setFixedWidth(140)
        TitleLab.setStyleSheet(Mstyle.QLabel(fontSize='12px'))
        th.addWidget(TitleLab)
        th.addStretch(1)
        mv.addLayout(th)

        # ------main items-----------------------
        codec = QtCore.QTextCodec.codecForName("GB2312")

        splitter = qw.QSplitter()
        splitter.setGeometry(0, 20, 0, 0)
        splitter.setOrientation(QtCore.Qt.Horizontal)
        splitter.setObjectName("splitter")
        mv.addWidget(splitter)
        # create spliter over.

        wid_left = qw.QWidget(self)
        wid_left.resize(self.width() * 0.35, self.height())
        wid_left.setParent(splitter)

        leftV = qw.QVBoxLayout()
        wid_left.setLayout(leftV)

        leftH = qw.QHBoxLayout()

        self.btnGrp = qw.QButtonGroup()
        self.btnGrp.setExclusive(True)
        self.highTool = qw.QPushButton('high')
        self.highTool.setAutoExclusive(True)
        self.highTool.setCheckable(True)
        self.highTool.setChecked(True)
        self.highTool.setToolTip('aa')
        self.highTool.setFixedHeight(20)
        self.highTool.setStyleSheet(Mstyle.QPushButton(kw='radiobutton'))
        self.btnGrp.addButton(self.highTool, 0)

        self.lowTool = qw.QPushButton('low')
        self.lowTool.setAutoExclusive(True)
        self.lowTool.setCheckable(True)
        self.lowTool.setToolTip('bb')
        self.lowTool.setFixedHeight(20)
        self.lowTool.setStyleSheet(Mstyle.QPushButton(kw='radiobutton'))
        self.btnGrp.addButton(self.lowTool, 1)

        leftH.addWidget(self.highTool)
        leftH.addWidget(self.lowTool)
        leftV.addLayout(leftH)

        self.LE = qw.QListWidget()
        self.LE.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LE.setSortingEnabled(True)
        self.LE.setStyleSheet(Mstyle.QListWidget(fontSize='12px') + 'QListWidget{outline:0px;}')
        leftV.addWidget(self.LE)

        # lef list create over.
        mdGrp = qw.QGroupBox('detail')
        mdGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        mdGrp.resize(self.width() * 0.65, self.height())
        mdGrp.setParent(splitter)

        Vbox = qw.QVBoxLayout()
        mdGrp.setLayout(Vbox)

        Hbox1 = qw.QHBoxLayout()
        Hbox1.setAlignment(QtCore.Qt.AlignHCenter)
        self.iconLab = qw.QLabel()
        Hbox1.addWidget(self.iconLab)

        self.nameLab = qw.QLabel('name')
        self.nameLab.setFixedHeight(20)
        self.nameLab.setStyleSheet(Mstyle.QLabel(fontSize='15px') + 'QLabel {background:transparent;}')
        Hbox1.addWidget(self.nameLab)
        # pathDict self.iconLab
        msgGrp = qw.QGroupBox('Message:')
        msgGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        msgVbox = qw.QVBoxLayout()
        msgGrp.setLayout(msgVbox)
        Vbox.addWidget(msgGrp)
        self.msgLab = qw.QLabel('', msgGrp)
        self.msgLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        msgVbox.addWidget(self.msgLab)

        artGrp = qw.QGroupBox('Artist:')
        artGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        artVbox = qw.QVBoxLayout()
        artGrp.setLayout(artVbox)
        Vbox.addWidget(artGrp)
        self.artLab = qw.QLabel('', artGrp)
        self.artLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        artVbox.addWidget(self.artLab)

        machGrp = qw.QGroupBox('Machine:')
        machGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        machVbox = qw.QVBoxLayout()
        machGrp.setLayout(machVbox)
        Vbox.addWidget(machGrp)
        self.machLab = qw.QLabel('', machGrp)
        self.machLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        machVbox.addWidget(self.machLab)

        confirmMsgGrp = qw.QGroupBox('left confirm message:')
        confirmMsgGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        confirmMsgVbox = qw.QVBoxLayout()
        confirmMsgGrp.setLayout(confirmMsgVbox)
        Vbox.addWidget(confirmMsgGrp)
        self.confirmMsgLab = qw.QLabel('this function not install', confirmMsgGrp)
        self.confirmMsgLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        confirmMsgVbox.addWidget(self.confirmMsgLab)

        feedbackGrp = qw.QGroupBox('write feed back:')
        feedbackGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        feedbackVbox = qw.QVBoxLayout()
        feedbackGrp.setLayout(feedbackVbox)
        Vbox.addWidget(feedbackGrp)
        self.feedbackLab = qw.QLabel('this function not install', feedbackGrp)
        self.feedbackLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + 'QLabel {background:transparent;}')
        feedbackVbox.addWidget(self.feedbackLab)

        picGrp = qw.QGroupBox('picture:')
        picGrp.resize(self.width() * 0.65, 50)
        picGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        picVbox = qw.QVBoxLayout()
        picVbox.setAlignment(QtCore.Qt.AlignHCenter)
        picGrp.setLayout(picVbox)
        self.imageLab = qw.QLabel()
        picVbox.addWidget(self.imageLab)

        hbox2 = qw.QHBoxLayout()
        self.BtnA1 = qw.QPushButton('check')
        self.BtnA1.setStyleSheet(Mstyle.QPushButton(kw='b'))
        self.BtnA1.setEnabled(False)
        self.BtnA2 = qw.QPushButton('confirm')
        self.BtnA2.setStyleSheet(Mstyle.QPushButton(kw='off'))
        self.BtnA2.setEnabled(False)
        hbox2.addWidget(self.BtnA1)
        hbox2.addWidget(self.BtnA2)

        Vbox.addLayout(Hbox1)
        Vbox.addWidget(picGrp)
        Vbox.addWidget(msgGrp)
        Vbox.addWidget(artGrp)
        Vbox.addWidget(machGrp)
        Vbox.addWidget(confirmMsgGrp)
        Vbox.addWidget(feedbackGrp)
        Vbox.addStretch(1)
        Vbox.addLayout(hbox2)
        self.mainWidget.setLayout(mv)

        self.fillListWidget()  # fill List Widget
        # ------main btn connect----------------------------

        self.highTool.clicked.connect(self.fillListWidget)
        self.lowTool.clicked.connect(self.fillListWidget)
        self.BtnA1.clicked.connect(self.BtnA1Fn)
        self.BtnA2.clicked.connect(self.BtnA2Fn)
        self.LE.currentItemChanged.connect(self.changeItemFn)

    # --------main function--------------
    def changeItemFn(self, item):
        message = ''
        artist = ''
        machine = ''
        name = 'name'

        if item:
            self.jsonPath = ''
            self.picPath = ''
            self.maPath = ''
            iCount = self.LE.count()
            itemArray = []
            for i in range(iCount):
                itemArray.append(int(self.LE.item(i).toolTip()))
            itemArray.sort()

            str = item.toolTip()
            name = '%s-%s-%s %s:%s:%s' % (str[0:4], str[4:6], str[6:8], str[8:10], str[10:12], str[12:14])
            iconImage = qw.QImage(self.picPath)
            self.iconPath = self.pathDict['icon']
            if int(str) == itemArray[-1]:
                iconImage.load(self.iconPath + '\\new.png')
            else:
                iconImage.load(self.iconPath + '\\file.png')
            iconPixmap = qw.QPixmap.fromImage(iconImage)
            self.iconLab.setPixmap(iconPixmap)

            # pathDict self.iconLab

            items = os.listdir(self.fullPath + str)
            sceenshot = ''
            mafile = ''

            jsonArray = []
            for i in items:
                tempPath = self.fullPath + str + '\\' + i
                if os.path.isfile(tempPath):
                    if '.png' in i:
                        self.picPath = tempPath
                    if '.ma' in i:
                        self.maPath = tempPath
                    if '.json' in i:
                        jsonArray.append(tempPath)

                        self.jsonPath = tempPath
                else:
                    pass
                    # mel.eval('print "file maybe changed after submit"')

            if len(jsonArray) > 1:
                for i in jsonArray:
                    if 'timeNode.json' in i:
                        self.jsonPath = i

            if os.path.exists(self.picPath):
                theImage = qw.QImage(self.picPath)
                imagePixmap = qw.QPixmap.fromImage(theImage)
                imagePixmap = imagePixmap.scaledToWidth(300)
                self.imageLab.setPixmap(imagePixmap)
            else:
                imagePixmap = qw.QPixmap()
                self.imageLab.setPixmap(imagePixmap)
            self.BtnA1.setEnabled(True)

            if os.path.exists(self.jsonPath):
                jDict = self.loadJson(self.jsonPath)
                if type(jDict) == dict:
                    message = jDict['lastUpload']['message']
                    machine = jDict['lastUpload']['machine']
                    artist = jDict['lastUpload']['artist']
        else:
            self.BtnA1.setEnabled(False)
            self.BtnA2.setEnabled(False)
            self.BtnA2.setStyleSheet(Mstyle.QPushButton(kw='off'))
            imagePixmap = qw.QPixmap()
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
            self.lowTool.setVisible(False)
            self.highTool.setVisible(False)

        Qarray = []
        if self.fullPath:
            items = os.listdir(self.fullPath)
            lastItem = ''
            for i in items:
                Qitem = qw.QListWidgetItem()
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

    def doSomething(self, event):
        martix = qw.QMatrix()
        rootPath = cmds.workspace(q=1, rd=1) + 'temp'
        if event.button() == QtCore.Qt.LeftButton:
            self.sceenRtn = self.saveScenceImage(rootPath)
        if event.button() == QtCore.Qt.RightButton:
            self.sceenRtn = self.saveScenceImage(rootPath, isFront=False)
        if event.button() == QtCore.Qt.RightButton or event.button() == QtCore.Qt.LeftButton:
            if self.sceenRtn:
                self.theImage = qw.QImage(self.sceenRtn)
                scaleX = 130.0 / self.theImage.width()
                martix.scale(scaleX, scaleX)
                self.theImage = self.theImage.transformed(martix)
                self.imagePixmap = qw.QPixmap.fromImage(self.theImage)
                self.imageLab.setPixmap(self.imagePixmap)
                self.isSubmitPic = True

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

        self.BtnA2.setEnabled(True)
        self.BtnA2.setStyleSheet(Mstyle.QPushButton())
        self.checkClicked.emit(['check', self.picPath, self.maPath, self.msgLab.text()])

    def BtnA2Fn(self):
        typeKey = ''
        if self.btnGrp.checkedId() == 0:
            typeKey = 'high'
        else:
            typeKey = 'low'

        self.confirmClicked.emit([typeKey, self.picPath, self.maPath, self.msgLab.text()])
        self.Cl_Ui()

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

    def Op_Ui(self):
        self.show()

    def Cl_Ui(self):
        self.deleteLater()
        self.close()

    def resizeEvent(self, e):
        self.mainWidget.resize(e.size())

if __name__ == '__main__':
    assetManager_confirmTool()
# cleanUIRT = assetManager_confirmTool()
# cleanUIRT.searchPath = 'W:\\project\\PIG\\asset\\MODEL\\Char\\testCha\\uploadTemp'
# cleanUIRT.localPath = 'D:\\localLibrary\\PIG'
# cleanUIRT.serverPath = 'W:\\project\\PIG'
# cleanUIRT.workName = 'testCha'

# cleanUIRT.createUI()
# cleanUIRT.fillListWidget()
# cleanUIRT.Op_Ui()

# cleanUIRT.Cl_Ui()