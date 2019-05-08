#theItem
from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2
import sys
import os
import logging
import spoilerItem

logger = logging.getLogger('gridWid_Log')  
logger.setLevel(logging.INFO)  


class gridWidget(qw.QWidget):
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
        self.setFixedSize(baseWid*val,baseHet*val)


    def setModule(self,_type='_assets'):
        if _type == '_assets':
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

    def addToList(self,inputData):
        if inputData:
            addList = []
            if isinstance(inputData,str):
                #print 'dir',inputData
                if os.path.exists(inputData):
                    addList = os.listdir(inputData)
                else:
                    addList = [inputData]

            elif isinstance(inputData,list):
                
                addList = inputData

            else:
                raise ValueError('only accept <list,string,stringPath>')

            addList.sort()
            for i in addList:
                theItem = qw.QListWidgetItem()
                theItem.setText(i)
                self.mainList.addItem(theItem)
                #self.shotSub.append(i)
        else:
            return False


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
                    logger.warning( 'key is invalid' + str(key))
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

    def setSubListDefaultSelect(self,inputStr):
        if inputStr:
            if isinstance(inputStr,str):
                for i in range(self.mainList.count()):
                    if inputStr.lower() == self.mainList.item(i).text().lower():
                        self.mainList.setCurrentRow(i)
                        break
            elif isinstance(inputStr,int):
                if inputStr > self.mainList.count():
                    inputStr = self.mainList.count()
                if inputStr < 0:
                    inputStr = 0
                self.mainList.setCurrentRow(inputStr)


    def setupUi(self):

        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setBold(True)
        

        
        #self.setFrameShape(qw.QFrame.StyledPanel)
        #self.setFrameShadow(qw.QFrame.Raised)
        #self.setObjectName(("frame"))


        mainH = qw.QHBoxLayout(self)
        mainH.setContentsMargins(3,10,3,3)
        mainH.setSpacing(1)

        self.setLayout(mainH)


        leftV = qw.QVBoxLayout(self)
        mainH.addLayout(leftV)

        self.depDict = dict(self.baseDict)

        self.assetPage = spoilerItem.FrameDialog()
        self.assetPage.setupLayout(title="Assets")
        
        leftV.addWidget(self.assetPage)

        for i in self.assetList:
            thePushButton = qw.QPushButton()
            thePushButton.setCheckable(True)
            thePushButton.setText(i)
            thePushButton.clicked.connect(self.emitTheSignal)
            #thePushButton.setEnabled(False)
            self.assetPage.addWidget(thePushButton)
            self.depDict[i] = thePushButton


        self.shotPage = spoilerItem.FrameDialog()
        self.shotPage.setupLayout(title="Sequences")
        
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
        if not self.mainList.currentItem():
            return False
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
        logger.debug( 'Mouse in!')
        #print dir(self.timer)
        self.timer.stop()
        try:
            self.closeAni.stop()
            self.setWindowOpacity(1)
        except AttributeError:
            
            self.setWindowOpacity(1)
    def leaveEvent(self, event):
        logger.debug( 'Mouse out!')
        self.timer  = QtCore.QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.start(5)
        self.timer.timeout.connect(self.closeAnimation)

    def closeAnimation(self):
        logger.debug( 'close ui')
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

    #gg.setShotSub(['seq001','seq003','seq022','seq005'])
    gg.setModule('shot')
    gg.setSubList('seq022')
    #gg.setLeftVisable(False)
    #gg.setLeftVisable(True)
    gg.Op_Ui()
    

    gg.raise_()
    try:
        sys.exit(app.exec_())
    except: pass
