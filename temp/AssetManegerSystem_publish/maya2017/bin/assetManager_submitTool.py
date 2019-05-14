# -*- coding:gbk -*-
# file upload UI
# figo

# 2017-11-15 16:19:07
# modify the input and message display part,now the UI could work for every department.
# add getNotifyFromTxt

import maya.cmds as cmds
import maya.mel as mel
from PySide2 import QtCore, QtGui,QtWidgets
from PySide2.QtCore import Qt

import os.path
import shutil, datetime, time, _winreg, urllib, shutil, sys

# -------------RTX message--------------------
def sendRTXMessage(user, message, isTrans=False):
    message_sys = ''
    if isTrans:
        message_utf = message.decode('gbk').encode("utf-8")
        message_sys = urllib.quote(message_utf)
    else:
        message_sys = message
    localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sender = self.XML_getNiceName()
    urllib.urlopen(
        'http://192.168.10.7:8012/sendnotify.cgi?msg=' + localtime + '\n' + message_sys + '&receiver=' + user + '&title=from:' + sender)
    # self.message=('submit:'+filename+'\nfile://'+self.serverPath+'\nmessage:'+self.message)
    # self.sendRTXMessage(self.reviever,self.message)
    # send RTX message


class assetManager_submitTool(QtWidgets.QWidget):
    highClicked = QtCore.Signal(list)
    lowClicked = QtCore.Signal(list)
    RigSubmitDialog = None
    isSubmitPic = False

    messageArray = []
    lenArray = []

    iconPath = ''
    def __init__(self, parent=None):

        super(assetManager_submitTool, self).__init__(parent)
        # ------Style Set----------------------------
        self.m_DragPosition = self.pos()

        self.resize(460, 800)
        self.move(0, 0)
        self.setWindowFlags(Qt.SubWindow | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.setStyleSheet(
            'QWidget {background-color :rgb(68,68,68);border:0px solid rgb(143,143,143);color:rgb(206,206,206);}')
        self.iconPath = getAssetManagerPath()['icon']

    def getNotifyFromTxt(self, txtPath):
        file_object = open(txtPath, 'r')
        array = file_object.readlines()
        dataArray = []
        dataLen = []
        for count, a in enumerate(array):
            utfStr = ''
            if count != len(array):
                utfStr = a.decode('utf-8')[:-2]
            else:
                utfStr = a.decode('utf-8')
            if utfStr[0] == ' ':
                dataArray[-1] += ('\n    ' + utfStr)
                dataLen[-1] += 25
            else:
                dataArray.append(utfStr)
                dataLen.append(25)

        self.messageArray = dataArray
        self.lenArray = dataLen
        return [dataArray, dataLen]

    def createUI(self):
        mainVbox = QtWidgets.QVBoxLayout()
        # -----close Btn Set----------------
        Xbtn = QtWidgets.QPushButton('x', self)
        Xbtn.setGeometry(0, 0, 0, 0)
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())

        Xbtn.clicked.connect(self.Cl_Ui)

        # -----TitleLabel-----------------------
        TitleLab = QtWidgets.QLabel('upload check list', self)
        TitleLab.setGeometry(40, 5, 0, 0)
        TitleLab.setFixedHeight(20)
        TitleLab.setFixedWidth(140)
        TitleLab.setStyleSheet(Mstyle.QLabel(fontSize='12px'))

        line1HBox = QtWidgets.QHBoxLayout()
        line1HBox.addWidget(Xbtn)
        line1HBox.addStretch(1)
        line1HBox.addWidget(TitleLab)
        line1HBox.addStretch(1)
        mainVbox.addLayout(line1HBox)
        # ------main items-----------------------
        codec = QtCore.QTextCodec.codecForName("GB2312")
        groupBoxAMsg = codec.toUnicode("提交留言：")

        self.groupBoxA = QtWidgets.QGroupBox(groupBoxAMsg, self)
        grpVbox = QtWidgets.QVBoxLayout()
        self.groupBoxA.setLayout(grpVbox)
        self.groupBoxA.setStyleSheet(Mstyle.QGroupBox())

        mainVbox.addWidget(self.groupBoxA)

        warningLabMsg = codec.toUnicode("请帮助检查场景中需要避免的问题，这将为下游提供很大帮助")
        warningLab = QtWidgets.QLabel(warningLabMsg, self.groupBoxA)
        warningLab.setGeometry(10, 110, 0, 0)
        warningLab.setFixedHeight(20)
        warningLab.setFixedWidth(390)
        warningLab.setStyleSheet('QLabel {font-family:Verdana;font-size:14px;}')

        self.QSclArea = QtWidgets.QScrollArea(self.groupBoxA)
        self.QSclArea.setStyleSheet(Mstyle.QScrollBar() + 'QWidget {background-color:transparent;}')

        self.msgWidget = QtWidgets.QWidget(self.groupBoxA)
        self.msgWidget.resize(2000, 2000)
        self.QSclArea.setWidget(self.msgWidget)

        self.imageLab = QtWidgets.QLabel('', self.groupBoxA)
        self.imageLab.setFixedHeight(80)
        self.imageLab.setFixedWidth(130)
        default404 = ''
        for i in sys.path:
            check = os.path.isfile(self.iconPath + '\\404NotFound.png')
            if check:
                default404 = self.iconPath + '\\404NotFound.png'
        self.imagePixmap = QtGui.QPixmap(default404)
        self.imageLab.setPixmap(self.imagePixmap)
        self.imageLab.mousePressEvent = self.doSomething

        self.TEA1 = QtWidgets.QTextEdit(self.groupBoxA)
        self.TEA1.setGeometry(10, 20, 0, 0)
        self.TEA1.setFixedHeight(80)
        #self.TEA1.setFixedWidth(220)
        self.TEA1.setStyleSheet(Mstyle.QTextEdit(kw='b'))

        xpos = 5
        ypos = 5
        yfix = -30
        rowLen = 10
        self.CheckBoxArray = []
        msgVbox = QtWidgets.QVBoxLayout()
        lastLen = 10
        self.checkCount = 0
        for itm, len in zip(self.messageArray, self.lenArray):
            CheckBoxA1 = QtWidgets.QCheckBox(itm)
            msgVbox.addWidget(CheckBoxA1)
            CheckBoxA1.setGeometry(xpos, yfix + len + lastLen, 0, 0)
            CheckBoxA1.setFixedHeight(len)
            CheckBoxA1.setFixedWidth(390)
            CheckBoxA1.setStyleSheet(
                Mstyle.QCheckBox() + 'QCheckBox::indicator:unchecked {color:red;background-color:rgb(68,68,68);width: 13px;height: 13px;} '
                                     'QCheckBox::indicator:checked {background-color:rgb(130,216,155)}')
            lastLen = len + lastLen + ypos
            self.CheckBoxArray.append(CheckBoxA1)
            CheckBoxA1.stateChanged.connect(self.CheckBoxMainFn)
            self.checkCount += 1
        self.msgWidget.setFixedHeight(lastLen + 20)
        self.msgWidget.setLayout(msgVbox)

        boxLine1 = QtWidgets.QHBoxLayout()
        boxLine1.addWidget(self.TEA1)
        boxLine1.addWidget(self.imageLab)
        grpVbox.addLayout(boxLine1)
        grpVbox.addWidget(warningLab)
        grpVbox.addWidget(self.QSclArea)

        BtnA1Msg = codec.toUnicode("upload high")
        self.BtnA1 = QtWidgets.QPushButton(BtnA1Msg, self)
        self.BtnA1.setEnabled(True)
        self.BtnA1.setFixedHeight(20)
        self.BtnA1.setFixedWidth(120)
        self.BtnA1.setStyleSheet(Mstyle.QPushButton(kw='off', lang='c'))

        BtnA2Msg = codec.toUnicode("first upload")
        self.BtnA2 = QtWidgets.QPushButton(BtnA2Msg, self)
        self.BtnA2.setEnabled(True)
        self.BtnA2.setFixedHeight(20)
        self.BtnA2.setFixedWidth(120)
        self.BtnA2.setStyleSheet(Mstyle.QPushButton(kw='off', lang='c'))

        checkLabTitle = ('0 of ' + str(self.checkCount + 1) + ' items checked')
        self.checkLab = QtWidgets.QLabel(checkLabTitle, self)
        self.checkLab.setFixedHeight(20)
        self.checkLab.setFixedWidth(130)

        line3HBox = QtWidgets.QHBoxLayout()
        line3HBox.addWidget(self.BtnA2)
        line3HBox.addWidget(self.BtnA1)
        line3HBox.addStretch(1)
        line3HBox.addWidget(self.checkLab)
        mainVbox.addLayout(line3HBox)
        # ------main btn connect----------------------------
        self.setLayout(mainVbox)

        self.BtnA1.clicked.connect(self.BtnA1Fn)
        self.BtnA2.clicked.connect(self.BtnA2Fn)

    # --------main function--------------
    def saveScenceImage(self, path, isFront=True):

        tempPath = 'D:\\Program Files\\figo\\AssetManaBox_Local\\cutpic\\'
        if not (os.path.exists(tempPath)):
            os.makedirs(tempPath)
        dirs = os.listdir(tempPath)
        number = str(len(dirs))
        fullPath = tempPath + 'tempCut' + number + '.0001.png'
        camShape = ''
        if isFront:
            mel.eval('dR_DoCmd("viewFront")')
            camShape = 'frontShape'
        else:
            modelName = (cmds.getPanel(wf=True))
            if 'modelPanel' in modelName:
                type = cmds.modelPanel(modelName, q=True, cam=True)
                camShape = cmds.listRelatives(type, s=1)[0]
            else:
                cmds.confirmDialog(m='need select view panel first')
                return False

        reply = QtWidgets.QMessageBox.information(self,
                                                  "confirm",
                                                  ('do you wanna auto fit view?'),
                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:

            cmds.viewFit(camShape, all=1)
        cmds.playblast(st=1, et=1, format='image', filename=(tempPath + 'tempCut' + number), clearCache=1, viewer=0,
                       showOrnaments=1, percent=100, compression='png', quality=100)

        return fullPath

    def doSomething(self, event):
        martix = QtGui.QMatrix()
        rootPath = cmds.workspace(q=1, rd=1) + 'temp'
        if event.button() == Qt.LeftButton:
            self.sceenRtn = self.saveScenceImage(rootPath)
        if event.button() == Qt.RightButton:
            self.sceenRtn = self.saveScenceImage(rootPath, isFront=False)
        if event.button() == Qt.MiddleButton:

            self.sceenRtn ,filetype = QtWidgets.QFileDialog.getOpenFileName(self,"select Picture","D:/","PNG file (*.png);;Jpeg Files (*.jpg);;Jpeg Files (*.jpeg)")
        if event.button() == Qt.RightButton or event.button() == Qt.LeftButton or event.button() == Qt.MiddleButton:
            if self.sceenRtn:
                self.theImage = QtGui.QImage(self.sceenRtn)
                scaleX = 130.0 / self.theImage.width()
                martix.scale(scaleX, scaleX)
                self.theImage = self.theImage.transformed(martix)
                self.imagePixmap = QtGui.QPixmap.fromImage(self.theImage)
                self.imageLab.setPixmap(self.imagePixmap)
                self.isSubmitPic = True

    def CheckBoxMainFn(self):
        checkState = [self.isSubmitPic]
        if self.isSubmitPic:
            count = 1
        else:
            count = 0
        for i in self.CheckBoxArray:
            checkState.append(i.isChecked())
            if i.isChecked() == True:
                count += 1
        if False in checkState:
            self.BtnA1.setEnabled(False)
            self.BtnA2.setEnabled(False)
            self.BtnA1.setStyleSheet(Mstyle.QPushButton(kw='off', lang='c'))
            self.BtnA2.setStyleSheet(Mstyle.QPushButton(kw='off', lang='c'))
        else:
            self.BtnA1.setEnabled(True)
            self.BtnA2.setEnabled(True)
            self.BtnA1.setStyleSheet(Mstyle.QPushButton(kw='on', lang='c'))
            self.BtnA2.setStyleSheet(Mstyle.QPushButton(kw='b', lang='c'))

        self.checkLab.setText((str(count) + ' of ' + str(self.checkCount + 1) + ' items checked'))

    def BtnA1Fn(self):
        self.highClicked.emit(['h', self.sceenRtn, self.TEA1.toPlainText()])
        # print 'sinal send'
        self.Cl_Ui()

    def BtnA2Fn(self):
        self.lowClicked.emit(['l', self.sceenRtn, self.TEA1.toPlainText()])
        # print 'sinal send'
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

#cleanUIRT=assetManager_submitTool()
#cleanUIRT.getNotifyFromTxt(r'Z:\AssetManegerSystem_publish\maya\RIG\notify.txt')
#cleanUIRT.createUI()
#cleanUIRT.Op_Ui()















