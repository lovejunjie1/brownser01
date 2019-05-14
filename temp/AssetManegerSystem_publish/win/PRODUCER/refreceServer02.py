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
    rootPath = 'Z:\\project'
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


        self.mainList = QtGui.QTreeWidget()
        self.mainList.setStyleSheet('QTreeWidget {border:0px}')
        self.mainList.setHeaderHidden(True)
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

        self.mainList.itemSelectionChanged.connect(self.listchange)
        self.mainList.itemDoubleClicked.connect(self.treeDoubleClickFn)
        self.mainList.itemExpanded.connect(self.loadNextLayer)
        rootPathBtn.clicked.connect(self.startFn)

        buttonPack.clicked.connect(self.packageFn)
        buttonReplace.clicked.connect(self.replaceFn)

    def treeDoubleClickFn(self,itm):
        if self.isControlPress:
            os.startfile(itm.toolTip(0))

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Control:
            self.isControlPress = True
    def keyReleaseEvent(self, QKeyEvent):
        self.isControlPress = False

    def loadNextLayer(self,nowItm):
        print nowItm.text(0)
        nowCount = nowItm.childCount()
        for i in range(nowCount):
            nextItm = nowItm.child(i)
            thirdLayerFiles = os.listdir(nextItm.toolTip(0))
            needNext = True
            for t in thirdLayerFiles:
                ans = os.path.isfile(nextItm.toolTip(0) + '\\' + t)
                if ans:
                    needNext = False
                    break

            if needNext and thirdLayerFiles:
                childArray = []
                for t in range(nextItm.childCount()):
                    childArray.append(nextItm.child(t).text(0))
                for tlf in thirdLayerFiles:
                    if not (tlf in childArray):
                        thdItm = QtGui.QTreeWidgetItem()
                        thdItm.setText(0,tlf)
                        thdItm.setToolTip(0,nextItm.toolTip(0) + '\\' + tlf)
                        nextItm.addChild(thdItm)

    def replaceFn(self):
        print 'replace'
        pathtext = str(self.rootPathText.text())
        driver = 'pathtext'
        if '\\' in pathtext:
            driver = pathtext.split('\\')[0]

        if not (os.path.exists(pathtext)):
            os.makedirs(pathtext)

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
            uploadInfo = []
            for count, item in enumerate(lst):
                fullPath = driver + '/' + item.filename
                uploadInfo.append(fullPath)

                if os.path.isfile(fullPath):
                    fatherPath = os.path.dirname(fullPath)
                    if not os.path.exists(fatherPath):
                        os.makedirs(fatherPath)

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

            dataCount = len(uploadInfo)
            if dataCount > 30:
                uploadInfo = uploadInfo[:30]
            strInfo = '\n'.join(uploadInfo)
            self.pathLab.setText('replace finish.\n' + strInfo + '\ntotal ' + str(dataCount) + ' files')
            self.pathLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + self.labYellow)

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
        #print labArray

        zipArray = []
        for a in labArray:
            for fpathe, dirs, fs in os.walk(a):
                if 'archive' in fpathe:
                    continue
                for f in fs:
                    if f != 'Thumbs.db':
                        zipArray.append(os.path.join(fpathe, f))
        if zipArray:
            zipMain = zipfile.ZipFile(deskTop + os.sep + nowFileName, 'w')
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


            self.pathLab.setText('package finish.please upload to BaiDuCloud disk right now.')
            self.pathLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + self.labYellow)
        else:
            self.pathLab.setText('selection folder is empty,no file in it.')
            self.pathLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + self.labYellow)

    def startFn(self):
        self.mainList.clear()
        path = str(self.rootPathText.text())
        files = os.listdir(path)
        for i in files:
            addItm = QtGui.QTreeWidgetItem ()
            addItm.setText(0,i)
            addItm.setToolTip(0,path + '\\' + i)
            self.mainList.addTopLevelItem(addItm)
            nextFiles = os.listdir(path + '\\' + i)
            if nextFiles:
                for nf in nextFiles:
                    nextItm = QtGui.QTreeWidgetItem ()
                    nextItm.setText(0,nf)
                    nextItm.setToolTip(0,path + '\\' + i + '\\' + nf)
                    addItm.addChild(nextItm)



    def listchange(self):
        sels = self.mainList. selectedItems()
        selections = []
        for s in sels:
            selections.append(str(s.toolTip(0)))

        filterSelections = []
        for check in selections:
            father_path = os.path.abspath(os.path.dirname(check) + os.path.sep + ".")
            father_path2 = os.path.abspath(os.path.dirname(father_path) + os.path.sep + ".")
            father_path3 = os.path.abspath(os.path.dirname(father_path2) + os.path.sep + ".")
            father_path4 = os.path.abspath(os.path.dirname(father_path3) + os.path.sep + ".")
            father_path5 = os.path.abspath(os.path.dirname(father_path4) + os.path.sep + ".")
            father_path6 = os.path.abspath(os.path.dirname(father_path5) + os.path.sep + ".")
            father_path7 = os.path.abspath(os.path.dirname(father_path6) + os.path.sep + ".")

            check1 = father_path in selections
            check2 = father_path2 in selections
            check3 = father_path3 in selections
            check4 = father_path4 in selections
            check5 = father_path5 in selections
            check6 = father_path6 in selections
            check7 = father_path7 in selections

            if not (check1 or check2 or check3 or check4 or check5 or check6 or check7):
                filterSelections.append(check)
        selStr = '\n'.join(filterSelections)

        self.pathLab.setText(selStr)

        self.pathLab.setStyleSheet(Mstyle.QLabel(fontSize='12px') + self.labBlue)

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
