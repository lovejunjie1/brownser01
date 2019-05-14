# -*- coding: utf-8 -*-
import os,sys,zipfile,time,getpass,datetime,json
import httplib
sys.path.append(r'D:\AssetManegerSystem_publish\data')
from PyQt4 import QtGui,QtCore
from PyQt4 .QtCore import Qt
import redBlackStyleSheet_0_10 as RBStyle
Mstyle = RBStyle.RedBlackStyleSheet()


class produceRefreshServerTool(QtGui.QWidget):
    titleName = 'MD refresh Server Tool v0.10'
    widgetHeight = 400
    widgetWidth = 600
    initPath = ''
    rootPath = 'W:\\project'
    labRed = 'QLabel {color:red;}'
    labBlue = 'QLabel {color:green;}'
    labYellow = 'QLabel {color:yellow;}'
    jsonPath = ''

    def __init__(self, *args, **kwargs):
        super(QtGui.QWidget, self).__init__(*args, **kwargs)

        self.resize(self.widgetHeight,self.widgetWidth)
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle(self.titleName)
        self.createUI()

        driver = ''
        pathtext = str(self.rootPathText.text())
        if '\\' in pathtext:
            driver = pathtext.split('\\')[0]
        jsonDir = '\\'.join([driver,'project','PIG','asset','PRODUCE','LOG','refreshServer'])
        checkPath = os.path.exists(jsonDir)
        if not checkPath:
            os.makedirs(jsonDir)
        self.jsonPath = jsonDir+'\\LOG.json'
        checkJson = os.path.exists(self.jsonPath)
        if not checkJson:
            epList = []
            self.saveJson(epList,self.jsonPath)


    def createUI(self):
        mainVBox = QtGui.QVBoxLayout()
        self.setLayout(mainVBox)
        rootHBox = QtGui.QHBoxLayout()
        rootPathBtn = QtGui.QPushButton()
        rootPathBtn.setStyleSheet(Mstyle.QPushButton())
        rootPathBtn.setText('>>')
        rootPathBtn.setFixedWidth(125)
        self.rootPathText = QtGui.QLineEdit()
        self.rootPathText.setStyleSheet(Mstyle.QLineEdit())
        self.rootPathText.setText(self.rootPath)
        rootHBox.addWidget(rootPathBtn)
        rootHBox.addWidget(self.rootPathText)

        mainVBox.addLayout(rootHBox)
        comboBoxStyle = ('QComboBox{border:1px solid gray;border-radius:8px;padding-left:4px;;min-width:6em;}'
                         'QComboBox:on {padding-top:3px;padding-left:4px;}'   
                         'QComboBox::drop-down {subcontrol-origin: padding;subcontrol-position: top right;width:15px;'
                         'border-left-width:1px;border-left-color: darkgray;border-left-style: solid;/* just a single line */'
                         'border-top-right-radius:3px;border-bottom-right-radius:3px;}'
                         'QComboBox::down-arrow {image: url(D:/rig_manager_box/icon/writer_icon/arrowDown.png);}'
                         'QComboBox::down-arrow:on {top:1px;left:1px;}'
                         'QComboBox QAbstractItemView{border:1px solid darkgray;selection-background-color: lightgray;}'
                         'QScrollBar {border: 0px solid grey;background: #89d962;width: 8px;}'
                         'QScrollBar::handle {background: #89d962;min-height: 20px;border-radius:4px;}'
                         )
        pathHbox = QtGui.QHBoxLayout()
        self.sectionA = QtGui.QComboBox()
        self.sectionA.setStyleSheet(comboBoxStyle)
        self.sectionA.setToolTip('project name')
        self.sectionB = QtGui.QComboBox()
        self.sectionB.setStyleSheet(comboBoxStyle)
        self.sectionB.setToolTip('type name')
        self.sectionB.setEnabled(False)
        self.sectionC = QtGui.QComboBox()
        self.sectionC.setStyleSheet(comboBoxStyle)
        self.sectionC.setToolTip('department name')
        self.sectionC.setEnabled(False)
        self.sectionD = QtGui.QComboBox()
        self.sectionD.setStyleSheet(comboBoxStyle)
        self.sectionD.setToolTip('class name')
        self.sectionD.setEnabled(False)
        self.sectionE = QtGui.QComboBox()
        self.sectionE.setStyleSheet(comboBoxStyle)
        self.sectionE.setToolTip('plus section')
        self.sectionE.setEnabled(False)

        pathHbox.addWidget(self.sectionA)
        pathHbox.addWidget(self.sectionB)
        pathHbox.addWidget(self.sectionC)
        pathHbox.addWidget(self.sectionD)
        pathHbox.addWidget(self.sectionE)
        mainVBox.addLayout(pathHbox)

        self.mainList = QtGui.QListWidget()
        self.mainList.setStyleSheet(Mstyle.QListWidget(fontSize='12px'))
        self.mainList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        mainVBox.addWidget(self.mainList)

        self.pathLab = QtGui.QLabel()
        self.pathLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + self.labRed)
        self.pathLab.setText(self.rootPath)
        mainVBox.addWidget(self.pathLab)

        buttonHbox = QtGui.QHBoxLayout()
        buttonPack = QtGui.QPushButton()
        buttonPack.setStyleSheet(Mstyle.QPushButton())
        buttonPack.setFixedHeight(25)
        buttonPack.setText('Package')
        buttonReplace = QtGui.QPushButton()
        buttonReplace.setStyleSheet(Mstyle.QPushButton(kw='b'))
        buttonReplace.setFixedHeight(25)
        buttonReplace.setText('Replace')

        buttonHbox.addWidget(buttonPack)
        buttonHbox.addWidget(buttonReplace)
        mainVBox.addLayout(buttonHbox)

        self.sectionA.currentIndexChanged.connect(self.itemchange)
        self.sectionB.currentIndexChanged.connect(self.itemchange)
        self.sectionC.currentIndexChanged.connect(self.itemchange)
        self.sectionD.currentIndexChanged.connect(self.itemchange)
        self.sectionE.currentIndexChanged.connect(self.itemchange)

        self.mainList.itemSelectionChanged.connect(self.listchange)
        rootPathBtn.clicked.connect(self.startFn)

        buttonPack.clicked.connect(self.packageFn)
        buttonReplace.clicked.connect(self.replaceFn)

    def replaceFn(self):
        print 'replace'
        pathtext = str(self.rootPathText.text())
        driver = 'pathtext'
        if '\\' in pathtext:
            driver = pathtext.split('\\')[0]

        filename = str(QtGui.QFileDialog.getOpenFileName(self, 'Open file', './'))
        if filename:
            z = zipfile.ZipFile(filename, 'r')
            lst = z.infolist()

            progress = QtGui.QProgressDialog(self.trUtf8("更新文件中......"), \
                                       self.trUtf8("取消"), 0, len(lst), self)
            progress.setWindowModality(Qt.WindowModal)

            nowTime = time.time()
            ClassicDate = time.strftime(" %Y-%m-%d %H:%M:%S ", time.localtime(nowTime))
            logFile = self.loadJson(self.jsonPath)
            logFile.append('[ replace ]' + ClassicDate + ' ' + filename)
            for count, item in enumerate(lst):
                fullPath = driver + '/' + item.filename
                check = os.path.exists(fullPath)

                if check:
                    os.remove(fullPath)
                z.extract(item, driver)
                dt = datetime.datetime(
                    item.date_time[0],
                    item.date_time[1],
                    item.date_time[2],
                    item.date_time[3],
                    item.date_time[4],
                    item.date_time[5]
                    )
                time2 = dt.timetuple()
                ConverTime2 = time.mktime(time2)
                #print ConverTime2
                os.utime(driver + '/' + item.filename, (ConverTime2, ConverTime2))
                logFile.append('[ update ]' + getpass.getuser() + ' ' + item.filename)
                progress.setValue(count)

            self.saveJson(logFile, self.jsonPath)

            progress.setValue(len(lst))
            progress.setParent(None)

    def packageFn(self):
        print 'package'
        deskTop = os.path.join(os.path.expanduser("~"), 'Desktop','uploadFile')
        checkExt = os.path.exists(deskTop)
        if not checkExt:
            os.makedirs(deskTop)
        nowTime = time.time()
        nowdate = time.strftime("%Y_%m_%d_%H_%M_%S_", time.localtime(nowTime))
        ClassicDate = time.strftime(" %Y-%m-%d %H:%M:%S ", time.localtime(nowTime))
        nowFileName = nowdate + getpass.getuser()+'.zip'
        labArray = []
        labT = str(self.pathLab.text())
        if '\n' in labT:
            labArray = labT.split('\n')
        else:
            labArray.append(labT)

        zipMain = zipfile.ZipFile(deskTop+os.sep+nowFileName, 'w')
        zipArray = []
        for a in labArray:
            for fpathe, dirs, fs in os.walk(a):
                if 'archive' in fpathe:
                    continue
                for f in fs:
                    zipArray.append(os.path.join(fpathe, f))
        progress = QtGui.QProgressDialog(self.trUtf8("打包文件中......"), \
                                         self.trUtf8("取消"), 0, len(zipArray), self)
        progress.setWindowModality(Qt.WindowModal)

        logFile = self.loadJson(self.jsonPath)
        logFile.append('[ package ]'+ClassicDate+' '+nowFileName)
        for count,za in enumerate(zipArray):
            zipMain.write(za)
            logFile.append('[ add ]' + getpass.getuser() + ' ' + za)
            progress.setValue(count)
        self.saveJson(logFile, self.jsonPath)

        progress.setValue(len(zipArray))
        progress.setParent(None)
        zipMain.close()
        os.startfile(deskTop)

    def startFn(self):
        self.sectionA.clear()
        self.sectionA.setEnabled(True)
        path = str(self.rootPathText.text())
        files = os.listdir(path)
        for i in files:
            self.sectionA.addItem(i)

        self.sectionB.setEnabled(True)
        self.sectionC.setEnabled(False)
        self.sectionC.clear()
        self.sectionD.setEnabled(False)
        self.sectionD.clear()
        self.sectionE.setEnabled(False)
        self.sectionE.clear()
        self.mainList.setEnabled(False)
        self.mainList.clear()

    def listchange(self):
        sels = self.mainList.selectedItems()
        selections = []
        for s in sels:
            selections.append(self.finalPath + '\\' + str(s.text()))
        selStr = '\n'.join(selections)

        self.pathLab.setText(selStr)

        self.pathLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + self.labBlue)

    def itemchange(self):
        sender = self.sender()
        colorArray = [Qt.black,Qt.darkRed,Qt.darkYellow,Qt.darkBlue,Qt.darkGreen,Qt.darkCyan,Qt.darkMagenta,Qt.darkGray,Qt.gray,Qt.blue]
        sender.setAutoFillBackground(True)
        sender.setBackgroundRole(QtGui.QPalette.Base)

        msg = sender.toolTip()
        Rpth = str(self.rootPathText.text())
        selA = str(self.sectionA.currentText())
        selB = str(self.sectionB.currentText())
        selC = str(self.sectionC.currentText())
        selD = str(self.sectionD.currentText())
        self.finalPath = '\\'.join([Rpth, selA, selB, selC, selD])
        '''
        selE = str(self.sectionE.currentText())
        isShot = False
        if selB == 'shot':
            self.finalPath = '\\'.join([Rpth, selA, selB, selC, selD, selE])
            isShot = True
        else:
            self.finalPath = '\\'.join([Rpth, selA, selB, selC, selD])
        '''
        if msg == 'project name':
            self.sectionB.setEnabled(True)
            self.sectionB.clear()
            self.sectionC.setEnabled(False)
            self.sectionC.clear()
            self.sectionD.setEnabled(False)
            self.sectionD.clear()
            self.sectionE.setEnabled(False)
            self.sectionE.clear()
            self.mainList.setEnabled(False)
            self.mainList.clear()


            files = os.listdir(self.finalPath)
            for i in files:
                self.sectionB.addItem(i)
            for i in range(len(files)):
                self.sectionB.setItemData(i, QtGui.QColor(colorArray[i]), Qt.BackgroundRole)
        if msg == 'type name':
            self.sectionC.setEnabled(True)
            self.sectionC.clear()
            self.sectionD.setEnabled(False)
            self.sectionD.clear()
            self.sectionE.setEnabled(False)
            self.sectionE.clear()
            self.mainList.setEnabled(False)
            self.mainList.clear()

            files = os.listdir(self.finalPath)
            for i in files:
                self.sectionC.addItem(i)
            for i in range(len(files)):
                self.sectionC.setItemData(i, QtGui.QColor(colorArray[i]), Qt.BackgroundRole)
        if msg == 'department name':
            self.sectionD.setEnabled(True)
            self.sectionD.clear()
            self.sectionE.setEnabled(False)
            self.sectionE.clear()

            files = os.listdir(self.finalPath)
            for i in files:
                self.sectionD.addItem(i)
            for i in range(len(files)):
                self.sectionD.setItemData(i, QtGui.QColor(colorArray[i]), Qt.BackgroundRole)
        if msg == 'class name':
            self.mainList.setEnabled(True)

            self.mainList.clear()
            files = os.listdir(self.finalPath)
            for i in files:
                self.mainList.addItem(i)
            '''
            if isShot:
                self.sectionE.setEnabled(True)
                self.mainList.setEnabled(False)
                self.mainList.clear()

                files = os.listdir(self.finalPath)
                for i in files:
                    self.sectionE.addItem(i)
                for i in range(len(files)):
                    self.sectionE.setItemData(i, QtGui.QColor(colorArray[i]), Qt.BackgroundRole)
            else:
                self.mainList.setEnabled(True)

                self.mainList.clear()
                files = os.listdir(self.finalPath)
                for i in files:
                    self.mainList.addItem(i)
                    
        if msg == 'plus section':
            self.mainList.setEnabled(True)
            self.mainList.clear()
            files = os.listdir(self.finalPath)
            for i in files:
                self.mainList.addItem(i)
            '''
        self.pathLab.setText(self.finalPath)
        pathExist = os.path.exists(self.finalPath)
        if pathExist:

            self.pathLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + self.labYellow)
        else:
            self.pathLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + self.labRed)

    def loadJson(self, path):
        file_object = open(path, 'r')
        data = json.load(file_object)
        return data

    def saveJson(self, data, path):
        jsonDump = json.dumps(data)
        file_object = open(path, 'w')
        file_object.write(jsonDump)
        file_object.close()

    def Op_Ui(self):
        self.show()

    def Cl_Ui(self):
        self.deleteLater()
        self.close()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet('QWidget {background-color:rgb(68,68,68);color:rgb(206,206,206)}')

    ui = produceRefreshServerTool()
    ui.Op_Ui()
    sys.exit(app.exec_())
