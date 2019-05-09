#theItem
from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2
import sys
import os
import logging
logger = logging.getLogger('dataItem_Log') 
logger.setLevel(logging.INFO) 

qssString = ''

class hoverToolButton(qw.QToolButton):

    def enterEvent(self, event):
        self.parent().setStyleSheet('QLabel[userCommon=yes]  {font-family:"Arial";color: #DDDDDD;background-color:transparent;}')
        #print 'Mouse in!'
    def leaveEvent(self, event):
        self.parent().setStyleSheet('QLabel[userCommon=yes]  {font-family:"Arial";color: #333333;background-color:transparent;}')
        #print 'Mouse out!'


class dataButton(qw.QFrame):
    clicked = QtCore.Signal(dict)

    played = QtCore.Signal(dict)

    addChart = QtCore.Signal(dict)

    defaultPicKey = 'thum.jpg'
    defaultMovKey = 'thum.gif'
    '''
    _infoDict = {
    'dataType':'',
    'sizeLevel':1,
    'dep':'',
    'name':'',
    'varient':'',
    'path':'',
    'showType':''
    }
    '''

    def __init__(self,dep,varient,name,path,dataType,sizeLevel=3,showType='jpg',parent=''):
        super(dataButton,self).__init__()
        sizeDict = {
        0:[120,90],
        1:[240,180],
        2:[360,270],
        3:[480,360]
        }
        self._infoDict = {
        'dataType':'',
        'sizeLevel':1,
        'dep':'',
        'name':'',
        'varient':'',
        'path':''
        }
        #print 111,self._infoDict
        self.setupUi()
        self.setSize(sizeDict[sizeLevel][0],sizeDict[sizeLevel][1])
        self.setPicture(path)
        self.setName(name)

        #print 333,self._infoDict
        self.setVarient(varient)
        self.setDep(dep)
        self.setDataType(dataType)
        self.font.setPointSize(72)
        self.setStyleSheet('QLabel[userCommon=yes]  {font-family:"Arial";color: #333333;background-color:transparent;}')

        #print 222,self._infoDict

    def setPicture(self,basePath):
        if os.path.exists(basePath):
            collect = os.listdir(basePath)
            picVal = ''
            for col in collect:
                if self.defaultPicKey in col:
                    picVal = basePath + '/' + col


            thepic = QtGui.QPixmap(picVal)
            thepic = thepic.scaled(self.width(),self.height())
            print self.width(),self.height()
            self.pushButton.setIcon(QtGui.QIcon(thepic))
            self.pushButton.setIconSize(QtCore.QSize(self.width(),self.height()))
            thedir = os.path.dirname(picVal)
            self._infoDict['path'] = thedir

    def setWidth(self,val):
        print 'setWidth',val
        self.setFixedWidth(val)
        self.pushButton.setFixedWidth(val)
        self.playButton.setFixedWidth(val*0.15)
        #self.playButton.setIconSize(self.playButton.size())
        self.addToChartButton.setFixedWidth(val*0.15)
        #self.addToChartButton.setIconSize(self.addToChartButton.size())


    def setHeight(self,val):
        logger.debug( 'setHeight ' + str(val))
        self.setFixedHeight(val)
        self.pushButton.setFixedHeight(val)
        self.playButton.setFixedHeight(val*0.15)
        self.playButton.setIconSize(QtCore.QSize(val*0.15,val*0.15))
        self.addToChartButton.setFixedHeight(val*0.15)
        self.addToChartButton.setIconSize(QtCore.QSize(val*0.07,val*0.07))
        #self.addToChartButton.setIconSize(self.addToChartButton.size())

        self.devLab.setFixedHeight(val*0.11)
        self.verLab.setFixedHeight(val*0.11)
        self.nameLab.setFixedHeight(val*0.13)
        #self.devLab.setStyleSheet('QLabel {font-size:%s px;}' % str(int(val*0.1)))
        #self.verLab.setStyleSheet('QLabel {font-size:%s px;}' % str(int(val*0.1)))
        #self.nameLab.setStyleSheet('QLabel {font-size:%s px;}' % str(int(val*0.1)))

    def setSize(self,wd,ht):
        self.setWidth(wd)
        self.setHeight(ht)
        
        

    def setName(self,val):
        self.setObjectName(val+"_box")
        self.nameLab.setText(val)
        self._infoDict['name'] = val

    def setDep(self,val,_color = '#9C9997'):
        self.devLab.setText(val)
        self.devLab.setProperty('dep',val.lower())
        #self.devLab.setStyleSheet('QLabel  {font-family:"Arial";color: #FFFFFF;background-color:%s}' % _color)

        self._infoDict['dep'] = val

    def setVarient(self,val):
        self.verLab.setText(val)
        self._infoDict['varient'] = val

    def setDataType(self,val):
        self.dataTypeLab.setText(val)
        self._infoDict['dataType'] = val


    def setupUi(self):

        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setBold(True)
        

        
        self.setFrameShape(qw.QFrame.StyledPanel)
        self.setFrameShadow(qw.QFrame.Raised)
        #self.setObjectName(("frame"))

        self.pushButton = hoverToolButton(self)
        self.pushButton.setObjectName('itemPushButton')
        self.pushButton.setMouseTracking(True)
        self.pushButton.clicked.connect(self.clickAction)
        
        #self.pushButton.setFixedSize(240,160)


        self.Vlay = qw.QVBoxLayout()
        #print dir(self.Vlay)
        self.Vlay.setContentsMargins(3,10,3,3)
        self.Vlay.setSpacing(1)
        self.setLayout(self.Vlay)

        self.Hlay1 = qw.QHBoxLayout()
        
        self.Hlay1.setSpacing(0)

        self.devLab = qw.QLabel(self)
        self.devLab.setEnabled(False)
        self.devLab.setObjectName(("devLab"))
        #self.devLab.setStyleSheet('QLabel  {font-family:"Arial";color: #FFFFFF;}')
        self.devLab.setFont(self.font)
        self.devLab.setProperty('userCommon','no')
        self.devLab.setAlignment(QtCore.Qt.AlignCenter)
        self.Hlay1.addWidget(self.devLab)

        self.dataTypeLab = qw.QLabel(self)
        self.dataTypeLab.setEnabled(False)
        self.dataTypeLab.setFont(self.font)
        self.dataTypeLab.setObjectName(("dataTypeLab"))

        self.dataTypeLab.setProperty('userCommon','yes')
        #self.dataTypeLab.setStyleSheet('QLabel  {font-family:"Arial";background-color:transparent;color: #FFFFFF;}')
        self.Hlay1.addWidget(self.dataTypeLab)
        self.Vlay.addLayout(self.Hlay1)


        self.HlayName = qw.QHBoxLayout()
        spaceLab = qw.QLabel(self)
        spaceLab.setText('  ')
        spaceLab.setProperty('userCommon','yes')
        self.HlayName.addWidget(spaceLab)
        
        self.HlayName.setSpacing(2)


        self.nameLab = qw.QLabel(self)
        self.nameLab.setEnabled(False)
        self.nameLab.setFont(self.font)
        self.nameLab.setObjectName(("nameLab"))
        self.nameLab.setProperty('userCommon','yes')
        #self.nameLab.setStyleSheet('QLabel  {font-family:"Arial";background-color:transparent;color: #FFFFFF;}')
        self.HlayName.addWidget(self.nameLab)

        spaceLab2 = qw.QLabel(self)
        spaceLab2.setText(' - ')
        spaceLab2.setProperty('userCommon','yes')
        self.HlayName.addWidget(spaceLab2)


        self.verLab = qw.QLabel(self)
        self.verLab.setEnabled(False)
        self.verLab.setFont(self.font)
        self.verLab.setObjectName(("verLab"))
        self.verLab.setProperty('userCommon','yes')
        #self.verLab.setStyleSheet('QLabel  {font-family:"Arial";background-color:transparent;color: #FFFFFF;}')
        self.HlayName.addWidget(self.verLab)
        self.HlayName.addStretch()
        self.Vlay.addLayout(self.HlayName)


        self.Hlay2 = qw.QHBoxLayout()
        self.addToChartButton = qw.QPushButton(self)
        self.addToChartButton.setObjectName(("addToChartButton"))
        #self.addToChartButton.setText('+')
        self.addToChartButton.setIcon(QtGui.QIcon(':/icon/plus.png'))
        self.addToChartButton.setIconSize(self.addToChartButton.size())
        self.addToChartButton.clicked.connect(self.addchartAction)
        self.addToChartButton.setStyleSheet('QPushButton {background-color:transparent;}')

        self.Hlay2.addWidget(self.addToChartButton)
        self.Hlay2.addStretch()

        self.Vlay.addStretch()

        self.playButton = qw.QPushButton(self)
        self.playButton.setObjectName(("playButton"))
        #self.playButton.setText('>')
        self.playButton.setIcon(QtGui.QIcon(':/icon/play.png'))
        self.playButton.setIconSize(self.playButton.size())
        self.playButton.clicked.connect(self.playAction)
        self.playButton.setStyleSheet('QPushButton {background-color:transparent;}')

        self.Hlay2.addWidget(self.playButton)
        self.Vlay.addLayout(self.Hlay2)

        if not(IsPySide2 or IsPySide):
            self.Hlay2.setMargin(0)
            self.Hlay1.setMargin(0)
    def clickAction(self):
        logger.info('click')
        logger.debug(self._infoDict)
        self.clicked.emit(self._infoDict)

    def playAction(self):
        logger.info('play')
        self.played.emit(self._infoDict)

    def addchartAction(self):
        logger.info( 'addchart')
        self.addChart.emit(self._infoDict)

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




	gg = dataButton('LookDev','default','001003hello','D:/unit/asset/Main','Charactor')
	gg.Op_Ui()
	

    gg.raise_()
    try:
        sys.exit(app.exec_())
    except: pass
