#-*- coding:gbk -*-
#import sys
#sys.path.append('D:\\rig_manager_box\\')
import maya.cmds as cmds
import maya.mel as mel
from PySide import QtCore,QtGui
from PySide.QtCore import Qt
from data.redBlackStyleSheet08 import RedBlackStyleSheet
Mstyle=RedBlackStyleSheet()
import os.path
import shutil,datetime,time,_winreg,urllib,shutil,sys
import rig_manager_box_pathConfig as pathConfig

def getScriptPath():
    orgPath = pathConfig.currFile_Path
    return orgPath
   
def getMayaWindow():
	"""
	Get Maya window
	:return: maya wnd
	"""
	mayaMainWindowPtr = OpenMayaUI.MQtUtil.mainWindow()
	return wrapInstance(long(mayaMainWindowPtr), QtGui.QWidget)   



class Rig_confirm_TOOL(QtGui.QMainWindow ):
    checkClicked=QtCore.Signal(list)
    confirmClicked=QtCore.Signal(list)
    
    searchPath='Z:\\project\\pig\\asset\\RIG\\Char\\12ypig\\uploadTemp\\'
    
    def __init__(self, parent = getMayaWindow()):

        super(Rig_confirm_TOOL, self).__init__(parent)
        #------Style Set----------------------------

        #QtGui.QWidget.__init__(self)
        self.m_DragPosition=self.pos()
        
        self.resize(600,480)
        self.move(0,0)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setMouseTracking(True)
        #self.setStyleSheet(Mstyle.mainWidgetStyle())
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.Widget | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowStaysOnTopHint)
        
        self.setStyleSheet('QWidget{background:rgb(68,68,68)}')
        
        #self.createUI()
        
        
    def createUI(self):
        
        mainWid=QtGui.QWidget(self)
        mainWid.setAttribute(Qt.WA_SetStyle)
        mainWid.resize(self.width(),self.height())
        #-----close Btn Set----------------    
        mv=QtGui.QVBoxLayout()
        th=QtGui.QHBoxLayout() 
                                         
        Xbtn=QtGui.QPushButton('x')
        #Xbtn.setGeometry(0,0,0,0)
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())
        
        Xbtn.clicked.connect(self.Cl_Ui)
        th.addWidget(Xbtn)
        th.addStretch(1)
        #-----TitleLabel-----------------------
        TitleLab=QtGui.QLabel('Rig confirm')
        #TitleLab.setGeometry(40,5,0,0)
        TitleLab.setFixedHeight(20)
        TitleLab.setFixedWidth(140)
        TitleLab.setStyleSheet(Mstyle.LabelStyle(fontSize='12px'))
        th.addWidget(TitleLab)
        th.addStretch(1)
        mv.addLayout(th)
        mainWid.setLayout(mv)


        #------main items-----------------------
        codec = QtCore.QTextCodec.codecForName("GB2312")
        
        splitter = QtGui.QSplitter()
        splitter.setGeometry(0,20,0,0)
        splitter.setOrientation(Qt.Horizontal)
        splitter.setObjectName("splitter")
        splitter.resize(self.width(),self.height())
        mv.addWidget(splitter)

        
        
        wid_left=QtGui.QWidget(self)
        wid_left.resize(self.width()*0.35, self.height())
        wid_left.setParent(splitter)
        
        wid=QtGui.QWidget(self)
        wid.resize(self.width()*0.65, self.height())
        wid.setParent(splitter)
        
        leftV=QtGui.QVBoxLayout()
        
        leftH=QtGui.QHBoxLayout()
        
        self.btnGrp=QtGui.QButtonGroup()
        self.btnGrp.setExclusive (True)
        highTool=QtGui.QPushButton('high')
        highTool.setAutoExclusive (True)
        highTool.setCheckable (True)
        highTool.setChecked(True)
        highTool.setToolTip('aa')
        #highTool.setIcon(QtGui.QIcon('D:\\Lighting_tool_box\\icon\\activity.png'))
        self.btnGrp.addButton (highTool,0)
        
        lowTool=QtGui.QPushButton('low')
        lowTool.setAutoExclusive (True)
        lowTool.setCheckable (True)
        lowTool.setToolTip('bb')
        #lowTool.setIcon(QtGui.QIcon('D:\\Lighting_tool_box\\icon\\activity.png'))
        self.btnGrp.addButton (lowTool,1)
        
        leftH.addWidget(highTool)
        leftH.addWidget(lowTool)
        
        leftV.addLayout(leftH)
        
        self.LE=QtGui.QListWidget()
        #self.LE.addItems(['aa','aa','aa','aa','aa'])
        leftV.addWidget(self.LE)
        wid_left.setLayout(leftV)
        
        Vbox=QtGui.QVBoxLayout()
        Hbox1=QtGui.QHBoxLayout()
        
        lBtn=QtGui.QPushButton('<<')
        rBtn=QtGui.QPushButton('>>')
        
        nameLab=QtGui.QLabel('name')
        nameLab.setGeometry(40,5,0,0)
        nameLab.setFixedHeight(20)
        nameLab.setFixedWidth(140)
        nameLab.setStyleSheet(Mstyle.LabelStyle(fontSize='12px')) 
        
        Hbox1.addWidget(lBtn)
        Hbox1.addWidget(nameLab)
        Hbox1.addWidget(rBtn)
        Vbox.addLayout(Hbox1)
        
        
        t2Lab=QtGui.QLabel('Message:')
        t2Lab.setGeometry(40,5,0,0)
        t2Lab.setFixedHeight(20)
        t2Lab.setFixedWidth(140)
        t2Lab.setStyleSheet(Mstyle.LabelStyle(fontSize='15px')) 
        Vbox.addWidget(t2Lab)
        
        
        self.imageLab=QtGui.QLabel('name')
        self.theImage=QtGui.QImage()
        
        self.imagePixmap=QtGui.QPixmap.fromImage(self.theImage) 
        self.imagePixmap=self.imagePixmap.scaledToWidth(300)
        self.imageLab.setPixmap(self.imagePixmap)
        Vbox.addWidget(self.imageLab)
        
        Vbox.addStretch(1)
        
        hbox2=QtGui.QHBoxLayout()
        self.BtnA1=QtGui.QPushButton('check')
        self.BtnA2=QtGui.QPushButton('confirm')
        hbox2.addWidget(self.BtnA1)
        hbox2.addWidget(self.BtnA2)
        Vbox.addLayout(hbox2)
        
        wid.setLayout(Vbox)
        
        
        #------main btn connect----------------------------

        self.BtnA1.clicked.connect(self.BtnA1Fn)
        self.BtnA2.clicked.connect(self.BtnA2Fn)


    #--------main function--------------
    def fillListWidget(self):
        fullPath=self.searchPath
        if self.btnGrp.checkedId ()==0:
            fullPath=fullPath+'\\high\\'
        else:
            fullPath=fullPath+'\\low\\'
        os.listdir(fullPath)
        
    def doSomething(self,event):
        martix = QtGui.QMatrix() 
        rootPath=cmds.workspace(q=1,rd=1)+'temp'
        if event.button()==Qt.LeftButton:
            self.sceenRtn=self.saveScenceImage(rootPath)           
        if event.button()==Qt.RightButton:
            self.sceenRtn=self.saveScenceImage(rootPath,isFront=False) 
        if event.button()==Qt.RightButton or event.button()==Qt.LeftButton:
            if self.sceenRtn:
                self.theImage=QtGui.QImage(self.sceenRtn)
                scaleX=130.0/self.theImage.width()
                martix.scale(scaleX,scaleX)
                self.theImage=self.theImage.transformed(martix)
                self.imagePixmap=QtGui.QPixmap.fromImage(self.theImage) 
                self.imageLab.setPixmap(self.imagePixmap)
                self.isSubmitPic=True
                #self.CheckBoxMainFn()

    def BtnA1Fn(self):
        self.checkClicked.emit(['l','check'])
        print 'sinal check'
        

    def BtnA2Fn(self):
        
        self.confirmClicked.emit(['h','confirm'])
        print 'sinal confirm'
        
    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton or event.button()==Qt.RightButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
            
    def mouseMoveEvent(self,QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()
    def mouseReleaseEvent(self,QMouseEvent):
        self.m_drag=False
        
    
    def Op_Ui(self):
        self.show()
    def Cl_Ui(self):
        self.deleteLater()
        self.close()
            
cleanUIRT=Rig_confirm_TOOL()
cleanUIRT.Op_Ui()

#cleanUIRT.Cl_Ui()

