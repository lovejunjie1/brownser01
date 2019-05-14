#-*- coding:gbk -*-
#import sys
#sys.path.append('D:\\rig_manager_box\\')
import maya.cmds as cmds
from PySide import QtCore,QtGui
from PySide.QtCore import Qt
from data.redBlackStyleSheet08 import RedBlackStyleSheet
Mstyle=RedBlackStyleSheet()
import os.path
import shutil,datetime,time,_winreg
import rig_manager_box_pathConfig as pathConfig
import maya.OpenMayaUI as OpenMayaUI
from shiboken import wrapInstance

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
    workName=''
    searchPath='Z:\\project\\pig\\asset\\RIG\\Char\\12ypig\\uploadTemp\\'
    titleName='confirmDialog'
    def __init__(self, parent = getMayaWindow()):
        self.cleanOpenWindow()
        super(Rig_confirm_TOOL, self).__init__(parent)
        #------Style Set----------------------------

        #QtGui.QWidget.__init__(self)
        self.m_DragPosition=self.pos()
        self.setWindowTitle(self.titleName)
        self.resize(600,480)
        self.move(0,0)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setMouseTracking(True)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.Widget | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowStaysOnTopHint)
        
        self.setStyleSheet('QWidget{background:rgb(68,68,68)}')
        
        #self.createUI()
    def cleanOpenWindow(self):
        gmw=getMayaWindow()
        for g in gmw.children():
            try:
                Tit=g.windowTitle()
                if Tit==self.titleName:
                    g.close()
                    g.deleteLater()
                    g.setParent(None)
            except:
                pass     
        
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
        TitleLab=QtGui.QLabel(self.workName+' confirm')
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
        
        #lBtn=QtGui.QPushButton('<<')
        #rBtn=QtGui.QPushButton('>>')
        
        self.nameLab=QtGui.QLabel('name')
        self.nameLab.setAlignment (Qt.AlignHCenter)
        self.nameLab.setFixedHeight(20)
        #self.nameLab.setFixedWidth(140)
        self.nameLab.setStyleSheet(Mstyle.LabelStyle(fontSize='15px')) 
        
        #Hbox1.addWidget(lBtn)
        Hbox1.addWidget(self.nameLab)
        #Hbox1.addWidget(rBtn)
        Vbox.addLayout(Hbox1)
        
        
        t2Lab=QtGui.QLabel('Message:')
        t2Lab.setGeometry(40,5,0,0)
        t2Lab.setFixedHeight(20)
        t2Lab.setFixedWidth(140)
        t2Lab.setStyleSheet(Mstyle.LabelStyle(fontSize='15px')) 
        Vbox.addWidget(t2Lab)
        
        self.msgLab=QtGui.QLabel('')
        self.msgLab.setGeometry(0,0,0,0)
        #self.msgLab.setFixedHeight(20)
        #self.msgLab.setFixedWidth(140)
        self.msgLab.setStyleSheet(Mstyle.LabelStyle(fontSize='12px')) 
        Vbox.addWidget(self.msgLab)
        
        
        self.imageLab=QtGui.QLabel()

        Vbox.addWidget(self.imageLab)
        
        Vbox.addStretch(1)
        
        hbox2=QtGui.QHBoxLayout()
        self.BtnA1=QtGui.QPushButton('check')
        self.BtnA1.setEnabled(False)
        self.BtnA2=QtGui.QPushButton('confirm')
        self.BtnA2.setEnabled(False)
        hbox2.addWidget(self.BtnA1)
        hbox2.addWidget(self.BtnA2)
        Vbox.addLayout(hbox2)
        
        wid.setLayout(Vbox)
        
        self.fillListWidget() #fill List Widget
        #------main btn connect----------------------------

        highTool.clicked.connect(self.fillListWidget)
        lowTool.clicked.connect(self.fillListWidget)
        self.BtnA1.clicked.connect(self.BtnA1Fn)
        self.BtnA2.clicked.connect(self.BtnA2Fn)
        self.LE.currentItemChanged .connect(self.changeItemFn)

    #--------main function--------------
    def changeItemFn(self,item):
        if item:
            if item.parent():
                item=item.parent()
            iCount=self.LE.count()
            itemArray=[]
            for i in range(iCount):
                itemArray.append(int(self.LE.item(i).toolTip()))
            itemArray.sort()
            
            str=item.toolTip()
            newText='%s-%s-%s %s:%s:%s' % (str[0:4],str[4:6],str[6:8],str[8:10],str[10:12],str[12:14])
            if int(str)==itemArray[-1]:
                newText=' [new] '+newText
            self.nameLab.setText(newText)
            
            items=os.listdir(self.fullPath+str)
            sceenshot=''
            mafile=''
            for i in items:
                if '.png' in i:
                    self.picPath=self.fullPath+str+'\\'+i
                if '.ma' in i:
                    self.maPath=self.fullPath+str+'\\'+i
                if '.json' in i:
                    self.jsonPath=self.fullPath+str+'\\'+i
            if os.path.exists(self.picPath):
                theImage=QtGui.QImage(self.picPath)
                imagePixmap=QtGui.QPixmap.fromImage(theImage) 
                imagePixmap=imagePixmap.scaledToWidth(300)
                self.imageLab.setPixmap(imagePixmap)
            else:
                imagePixmap=QtGui.QPixmap() 
                self.imageLab.setPixmap(imagePixmap)
            self.BtnA1.setEnabled(True)
            #self.BtnA2.setEnabled(True)
            
            if os.path.exists(self.jsonPath):
                self.msgLab.setText(self.loadJson(self.jsonPath))
            else:
                self.msgLab.setText('empty')
        else:
            self.BtnA1.setEnabled(False)
            self.BtnA2.setEnabled(False)
            imagePixmap=QtGui.QPixmap() 
            self.imageLab.setPixmap(imagePixmap)
            self.nameLab.setText('name')
            
    def fillListWidget(self):
        self.LE.clear()
        self.fullPath=self.searchPath
        if self.btnGrp.checkedId ()==0:
            self.fullPath=self.fullPath+'\\high\\'
        else:
            self.fullPath=self.fullPath+'\\low\\'
        items=os.listdir(self.fullPath)
        Qarray=[]
        for i in items:
            Qitem=QtGui.QListWidgetItem()
            newText='%s-%s-%s %s:%s:%s' % (i[0:4],i[4:6],i[6:8],i[8:10],i[10:12],i[12:14])
            Qitem.setText(newText)
            Qitem.setToolTip(i)
            Qarray.append(Qitem)
            self.LE.addItem(Qitem)
        
        
        
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
        self.checkClicked.emit(['check',self.picPath,self.maPath])
        cmds.file(self.maPath,open=1,f=1)
        self.BtnA2.setEnabled(True)

    def BtnA2Fn(self):
        self.confirmClicked.emit(['confirm',self.picPath,self.maPath,self.msgLab.text()])
        self.Cl_Ui()
        #print 'sinal confirm'
        
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
            
#cleanUIRT=Rig_confirm_TOOL()
#cleanUIRT.createUI()
#cleanUIRT.Op_Ui()

#cleanUIRT.Cl_Ui()

