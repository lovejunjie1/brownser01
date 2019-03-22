#theItem
from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2
import sys
import os




class spoiler(qw.QFrame):
    #clicked = QtCore.Signal(dict)


    def __init__(self,dep,varient,name,path,sizeLevel=3,showType='jpg',parent=''):
        super(spoiler,self).__init__()
        sizeDict = {
        1:[120,90],
        2:[240,180],
        3:[480,360]
        }
        self.setupUi()
        

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




    gg = spoiler()
    gg.Op_Ui()
    

    gg.raise_()
    try:
        sys.exit(app.exec_())
    except: pass
