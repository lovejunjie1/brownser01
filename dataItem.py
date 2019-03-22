#theItem
from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2
import sys
import os


qssString = ''

class hoverToolButton(qw.QToolButton):

    def enterEvent(self, event):
        print 'Mouse in!'
    def leaveEvent(self, event):
        print 'Mouse out!'


class dataButton(qw.QFrame):
    clicked = QtCore.Signal(dict)

    played = QtCore.Signal(dict)

    addChart = QtCore.Signal(dict)

    defaultPicKey = 'thum.jpg'
    defaultMovKey = 'thum.gif'
    
    infoDict = {
    'sizeLevel':1,
    'dep':'',
    'name':'',
    'varient':'',
    'path':'',
    'showType':''
    }

    def __init__(self,dep,varient,name,path,sizeLevel=3,showType='jpg',parent=''):
        super(dataButton,self).__init__()
        sizeDict = {
        1:[120,90],
        2:[240,180],
        3:[480,360]
        }
        self.setupUi()
        self.setSize(sizeDict[sizeLevel][0],sizeDict[sizeLevel][1])
        self.setPicture(path)
        self.setName(name)
        self.setVarient(varient)
        self.setDep(dep)
        self.font.setPointSize(72)


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
            self.infoDict['path'] = thedir

    def setWidth(self,val):
        print 'setWidth',val
        self.setFixedWidth(val)
        self.pushButton.setFixedWidth(val)
        self.playButton.setFixedWidth(val*0.15)
        self.addToChartButton.setFixedWidth(val*0.15)


    def setHeight(self,val):
        print 'setHeight',val
        self.setFixedHeight(val)
        self.pushButton.setFixedHeight(val)
        self.playButton.setFixedHeight(val*0.15)
        self.addToChartButton.setFixedHeight(val*0.15)

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

    def setDep(self,val,_color = '#9C9997'):
        self.devLab.setText(val)
        self.devLab.setStyleSheet('QLabel  {font-family:"Arial";color: #FFFFFF;background-color:%s}' % _color)

    def setVarient(self,val):
        self.verLab.setText(val)


    def setupUi(self):

        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setBold(True)
        

        
        self.setFrameShape(qw.QFrame.StyledPanel)
        self.setFrameShadow(qw.QFrame.Raised)
        #self.setObjectName(("frame"))

        self.pushButton = hoverToolButton(self)
        self.pushButton.setMouseTracking(True)
        self.pushButton.clicked.connect(self.clickAction)
        
        #self.pushButton.setFixedSize(240,160)


        self.Vlay = qw.QVBoxLayout()
        print dir(self.Vlay)
        self.Vlay.setContentsMargins(3,10,3,3)
        self.Vlay.setSpacing(1)
        self.setLayout(self.Vlay)

        self.Hlay1 = qw.QHBoxLayout()
        self.Hlay1.setMargin(0)
        self.Hlay1.setSpacing(0)

        self.devLab = qw.QLabel(self)
        self.devLab.setEnabled(False)
        self.devLab.setObjectName(("devLab"))
        self.devLab.setStyleSheet('QLabel  {font-family:"Arial";color: #FFFFFF;}')
        self.devLab.setFont(self.font)
        self.devLab.setAlignment(QtCore.Qt.AlignCenter)
        self.Hlay1.addWidget(self.devLab)

        self.verLab = qw.QLabel(self)
        self.verLab.setEnabled(False)
        self.verLab.setFont(self.font)
        self.verLab.setObjectName(("verLab"))
        self.verLab.setStyleSheet('QLabel  {font-family:"Arial";background-color:transparent;color: #FFFFFF;}')
        self.Hlay1.addWidget(self.verLab)
        self.Vlay.addLayout(self.Hlay1)

        self.nameLab = qw.QLabel(self)
        self.nameLab.setEnabled(False)
        self.nameLab.setFont(self.font)
        self.nameLab.setObjectName(("nameLab"))
        self.nameLab.setStyleSheet('QLabel  {font-family:"Arial";background-color:transparent;color: #FFFFFF;}')
        self.Vlay.addWidget(self.nameLab)
        self.Vlay.addStretch()

        self.Hlay2 = qw.QHBoxLayout()
        self.Hlay2.setMargin(0)
        self.addToChartButton = qw.QPushButton(self)
        self.addToChartButton.setObjectName(("addToChartButton"))
        self.addToChartButton.setText('+')
        self.addToChartButton.clicked.connect(self.addchartAction)

        self.Hlay2.addWidget(self.addToChartButton)
        self.Hlay2.addStretch()

        self.playButton = qw.QPushButton(self)
        self.playButton.setObjectName(("playButton"))
        self.playButton.setText('>')
        self.playButton.clicked.connect(self.playAction)

        self.Hlay2.addWidget(self.playButton)
        self.Vlay.addLayout(self.Hlay2)


    def clickAction(self):
        print 'click'
        self.clicked.emit(self.infoDict)

    def playAction(self):
        print 'play'
        self.played.emit(self.infoDict)

    def addchartAction(self):
        print 'addchart'
        self.addChart.emit(self.infoDict)

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




	gg = dataButton('LookDev','default','001003hello','D:/unit/asset/Main')
	gg.Op_Ui()
	

    gg.raise_()
    try:
        sys.exit(app.exec_())
    except: pass
