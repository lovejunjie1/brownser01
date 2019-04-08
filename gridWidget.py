#theItem
from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2
import sys
import os

import spoilerItem



class gridWidget(qw.QFrame):
    clicked = QtCore.Signal(list)
    timer  = QtCore.QTimer()

    def __init__(self,parent=''):
        super(gridWidget,self).__init__()
        self.setWindowFlags(QtCore.Qt.SubWindow | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.baseDict = {
            'Model':'',
            'LookDev':'',
            'Rig':'',
            'Groom':'',
            'GroomMat':'',
            'RigSol':'',
            'LayoutSeq':'',
            'LayoutAni':'',
            'ShotEnv':'',
            'ShotSound':'',
            'Animation':'',
            'CFX':'',
            'FinalShotAssemble':'',
            'KeyLight':'',
            'Lighting':'',
            'Comp':'',
            'ShotDMP':'',
            'SeqDMP':''
            }


        self.assetList = [        
            'Model',
            'LookDev',
            'Rig',
            'Groom',
            'GroomMat',
            'RigSol']

        self.assetSub = [
            'Charactors',
            'Props',
            'Elements',
            'SubSceneAssemble',
            'LightRig'
            ]

        self.shotList = [
            'LayoutSeq',
            'LayoutAni',
            'ShotEnv',
            'ShotSound',
            'Animation',
            'CFX',
            'FinalShotAssemble',
            'KeyLight',
            'Lighting',
            'Comp',
            'ShotDMP',
            'SeqDMP'
            ]

        self.shotSub = [
            'seqZIP'
        ]

        self.setupUi()
        
        self.enableDict = dict(self.baseDict)
        self.setEnableList('') # clear list.set all False
        self.applyEnableList()

    def setScaleSize(self,val):

        baseHet = 400
        baseWid = 200
        self.resize(baseWid*val,baseHet*val)


    def setModule(self,_type='asset'):
        if _type == 'asset':
            self.assetPage.toggleCollapsed()
            self.shotPage.setEnabled(False)
            for i in self.assetSub:
                theItem = qw.QListWidgetItem()
                theItem.setText(i)
                self.mainList.addItem(theItem)
            self.mainList.itemClicked.connect(self.emitTheSignal)
        else:
            self.shotPage.toggleCollapsed()
            self.assetPage.setEnabled(False)
            for i in self.shotSub:
                theItem = qw.QListWidgetItem()
                theItem.setText(i)
                self.mainList.addItem(theItem)
            self.mainList.itemClicked.connect(self.emitTheSignal)


            #self.mainList.setItems()

    def setShotSub(self,inputData):
        if isinstance(inputData,str):
            print 'dir',inputData

        if isinstance(inputData,list):
            for i in inputData:
                self.shotSub.append(i)

            self.shotSub.sort()


    def printEnableList(self):
        for key,val in self.enableDict.items():
            print key,val

    def setEnableList(self,inputStr):
        if inputStr:
            if isinstance(inputStr,str):
                theKeys = self.enableDict.keys()
                for key in theKeys:
                    if key.lower() == inputStr.lower():
                        inputStr = str(key)
                        break
                if inputStr in self.enableDict.keys():
                    self.enableDict[inputStr] = True
                else:
                    print 'key is invalid',key
        else:
            for i in self.enableDict.keys():
                self.enableDict[i] = False
            
    def applyEnableList(self):

        for key,val in self.enableDict.items():
            self.depDict[key].setEnabled(val)

    def setCheckList(self,inputStr):
        if inputStr:
            if isinstance(inputStr,str):
                theKeys = self.enableDict.keys()
                for key in theKeys:
                    if key.lower() == inputStr.lower():
                        inputStr = str(key)
                        break
                if (inputStr in self.enableDict.keys()) and self.enableDict[inputStr]:
                    self.depDict[inputStr].setChecked(True)

    def setSubList(self,inputStr):
        if inputStr:
            for i in range(self.mainList.count()):
                if inputStr.lower() == self.mainList.item(i).text().lower():
                    self.mainList.setCurrentRow(i)
                    break


    def setupUi(self):

        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setBold(True)
        

        
        self.setFrameShape(qw.QFrame.StyledPanel)
        self.setFrameShadow(qw.QFrame.Raised)
        #self.setObjectName(("frame"))


        mainH = qw.QHBoxLayout(self)
        mainH.setContentsMargins(3,10,3,3)
        mainH.setSpacing(1)

        self.setLayout(mainH)


        leftV = qw.QVBoxLayout(self)
        mainH.addLayout(leftV)

        self.depDict = dict(self.baseDict)

        self.assetPage = spoilerItem.FrameLayout(title="Assets")
        
        leftV.addWidget(self.assetPage)

        for i in self.assetList:
            thePushButton = qw.QPushButton()
            thePushButton.setCheckable(True)
            thePushButton.setText(i)
            thePushButton.clicked.connect(self.emitTheSignal)
            #thePushButton.setEnabled(False)
            self.assetPage.addWidget(thePushButton)
            self.depDict[i] = thePushButton


        self.shotPage = spoilerItem.FrameLayout(title="Sequences")
        
        leftV.addWidget(self.shotPage)
        leftV.addStretch()


        for i in self.shotList:
            thePushButton = qw.QPushButton()
            thePushButton.setText(i)
            thePushButton.setCheckable(True)
            thePushButton.clicked.connect(self.emitTheSignal)
            #thePushButton.setEnabled(False)
            self.shotPage.addWidget(thePushButton)
            self.depDict[i] = thePushButton


        self.mainList = qw.QListWidget()
        mainH.addWidget(self.mainList)

        #self.pushButton.setMouseTracking(True)
        #self.pushButton.clicked.connect(self.clickAction)
        
        #self.pushButton.setFixedSize(240,160)

    def setLeftVisable(self,state):

        self.shotPage.setVisible(state)
        self.assetPage.setVisible(state)

    def emitTheSignal(self):
        valB = self.mainList.currentItem().text()
        emitArray = []
        for key,val in self.depDict.items():
            if val.isChecked():
                emitArray.append([key,valB])
        #self.depDict
        if emitArray:
            self.clicked.emit(emitArray)
            print emitArray
        else:
            print 'output invalid'

    def enterEvent(self, event):
        print 'Mouse in!'
        #print dir(self.timer)
        self.timer.stop()
        try:
            self.closeAni.stop()
            self.setWindowOpacity(1)
        except AttributeError:
            
            self.setWindowOpacity(1)
    def leaveEvent(self, event):
        print 'Mouse out!'
        self.timer  = QtCore.QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.start(5)
        self.timer.timeout.connect(self.closeAnimation)

    def closeAnimation(self):
        print 'close ui'
        self.closeAni = QtCore.QPropertyAnimation(self)
        self.closeAni.setTargetObject(self)
        self.closeAni.setPropertyName(b'windowOpacity')
        #self.closeAni.setStartValue(int(1))
        self.closeAni.setKeyValueAt(0,1)
        self.closeAni.setKeyValueAt(0.25,0.95)
        self.closeAni.setKeyValueAt(0.5,0.75)
        self.closeAni.setKeyValueAt(1,0)
        #self.closeAni.setEndValue(int(0))

        self.closeAni.setDuration(1500)

        self.closeAni.start()
        self.closeAni.finished.connect(self.Cl_Ui)

    def Cl_Ui(self):
        self.deleteLater()
        self.close()

    def Op_Ui(self):
        '''
        self.setupUi()
        self.setWidth(240)
        self.setHeight(180)
        picPath = 'D:/unit/asset/Main/CHR_WolfGirl_thum.jpg'
        self.setPicture(picPath)
        self.setName('001001XiaoHunDan')
        self.setVarient('default')
        self.setDep('LookDev')
        '''
        self.show()

if __name__ == '__main__':
    import os
    app = qw.QApplication.instance()
    if not app:
        app = qw.QApplication( [])




    gg = gridWidget()
    gg.setEnableList('CFX')
    gg.setEnableList('Animation')
    gg.applyEnableList()
    gg.setCheckList('CFX')

    gg.setShotSub(['seq001','seq003','seq022','seq005'])
    gg.setModule('shot')
    gg.setSubList('seq022')
    #gg.setLeftVisable(False)
    #gg.setLeftVisable(True)
    gg.Op_Ui()
    

    gg.raise_()
    try:
        sys.exit(app.exec_())
    except: pass
