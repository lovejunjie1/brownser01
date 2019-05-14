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


#-------------RTX message--------------------
def sendRTXMessage(user,message,isTrans=False):
    message_sys=''
    if isTrans:
        message_utf=message.decode('gbk').encode("utf-8") 
        message_sys=urllib.quote(message_utf)
    else:
        message_sys=message
    localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sender=self.XML_getNiceName()
    urllib.urlopen('http://192.168.10.7:8012/sendnotify.cgi?msg='+localtime+'\n'+message_sys+'&receiver='+user+'&title=from:'+sender)
    #self.message=('submit:'+filename+'\nfile://'+self.serverPath+'\nmessage:'+self.message)
    #self.sendRTXMessage(self.reviever,self.message)
    #send RTX message


class Rig_submit_TOOL(QtGui.QMainWindow):
    highClicked=QtCore.Signal(list)
    lowClicked=QtCore.Signal(list)
    RigSubmitDialog=None
    isSubmitPic=False
    
    #resultSinal = QtCore.Signal(str)
    
    #saveImageSignal=QtCore.Signal(str)
    def __init__(self, parent = None):

        super(Rig_submit_TOOL, self).__init__(parent)
        #------Style Set----------------------------

        #QtGui.QWidget.__init__(self)
        self.m_DragPosition=self.pos()
        
        self.resize(460,600)
        self.move(0,0)
        self.setWindowFlags(Qt.SubWindow|Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setStyleSheet(Mstyle.mainWidgetStyle())
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        
        self.createUI()
        
        
    def createUI(self):
        #-----close Btn Set----------------                                                 
        Xbtn=QtGui.QPushButton('x',self)
        Xbtn.setGeometry(0,0,0,0)
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())
        
        Xbtn.clicked.connect(self.Cl_Ui)
        
        #-----TitleLabel-----------------------
        TitleLab=QtGui.QLabel('Rig upload',self)
        TitleLab.setGeometry(40,5,0,0)
        TitleLab.setFixedHeight(20)
        TitleLab.setFixedWidth(140)
        TitleLab.setStyleSheet(Mstyle.LabelStyle(fontSize='12px'))


        #------main items-----------------------
        codec = QtCore.QTextCodec.codecForName("GB2312")
        groupBoxAMsg = codec.toUnicode("提交留言：")
        
        self.groupBoxA=QtGui.QGroupBox(groupBoxAMsg,self)
        self.groupBoxA.setGeometry(20,40,0,0)
        self.groupBoxA.setFixedHeight(500)
        self.groupBoxA.setFixedWidth(410)
        #self.groupBoxA.setStyleSheet(Mstyle.QGroupBoxStyleA)
        
        warningLabMsg = codec.toUnicode("请帮助检查场景中需要避免的问题，这将为下游提供很大帮助")
        warningLab=QtGui.QLabel(warningLabMsg,self.groupBoxA)
        warningLab.setGeometry(10,110,0,0)
        warningLab.setFixedHeight(20)
        warningLab.setFixedWidth(390)
        warningLab.setStyleSheet('QLabel {font-family:Verdana;font-size:14px;}')
        
        self.QSclArea=QtGui.QScrollArea(self.groupBoxA)
        self.QSclArea.setFixedHeight(360)
        self.QSclArea.setFixedWidth(390)
        self.QSclArea.setGeometry(10,130,0,0)
        self.QSclArea.setStyleSheet(Mstyle.SclAreaStyle())
        
        self.msgWidget=QtGui.QWidget(self.groupBoxA)
        self.msgWidget.setFixedHeight(490)
        self.msgWidget.setFixedWidth(370)
        self.msgWidget.setGeometry(0,0,0,0)
        self.QSclArea.setWidget(self.msgWidget)
       
        self.imageLab=QtGui.QLabel('',self.groupBoxA)
        self.imageLab.setGeometry(250,20,0,0)
        self.imageLab.setFixedHeight(80)
        self.imageLab.setFixedWidth(130)
        default404=''
        for i in sys.path:
            check=os.path.isfile(getScriptPath()+'\\data\\404NotFound.png') 
            if check:
                default404=getScriptPath()+'\\data\\404NotFound.png'
        self.imagePixmap=QtGui.QPixmap(default404)  
        self.imageLab.setPixmap(self.imagePixmap)
        self.imageLab.mousePressEvent = self.doSomething
        
        self.TEA1=QtGui.QTextEdit(self.groupBoxA)
        self.TEA1.setGeometry(10,20,0,0)
        self.TEA1.setFixedHeight(80)
        self.TEA1.setFixedWidth(220)
        self.TEA1.setStyleSheet(Mstyle.TextEditStyle())        
        
        

        xpos=5
        ypos=5  
        yfix=-30
        rowLen=10  
        self.CheckBoxArray=[]
        messageArray=["禁止使用blendshape和骨骼蒙皮以外的方式对模型进行绑定\n（如：直接约束模型或对模型使用父子关系）",
        "禁止出现绑定文件命名不规范的情况\n    禁止出现类似joint1,curve1,pCube1等的默认命名\n    禁止出现重名物件\n    禁止出现不是用规定层级制作的绑定文件",
        "禁止出现控制器属性不归默认参数的情况",
        "禁止出现控制器属性有key帧的情况",
        "不参与ABC缓存的模型禁止放在Geometry组中\n    包括wrap产生的base物件，禁止放在Geometry组中",
        "禁止永久隐藏参与渲染的模型",
        "禁止绑定解算文件中出现双节点，多节点模型物体",
        "禁止出现各版本绑定之间命名不统一的情况（区分大小写）",
        "绑定修改后，禁止随意变动层级导致原有动画不能继承",
        "禁止出现未通知制片确认就进行上传的情况"
        ]
        lenArray=[40,60,60,40,40,40,40,40,40,40] 
        lastLen=0
        self.checkCount=0
        for itm,len in zip(messageArray,lenArray):
            CheckBoxA1Msg = codec.toUnicode(itm)
            CheckBoxA1=QtGui.QCheckBox(CheckBoxA1Msg,self.msgWidget)
            CheckBoxA1.setGeometry(xpos,yfix+len+lastLen,0,0)
            CheckBoxA1.setFixedHeight(len)
            CheckBoxA1.setFixedWidth(390)
            CheckBoxA1.setStyleSheet(Mstyle.CheckBoxStyle())
            lastLen=len+lastLen+ypos
            self.CheckBoxArray.append(CheckBoxA1)
            CheckBoxA1.stateChanged.connect(self.CheckBoxMainFn)
            self.checkCount+=1
        self.msgWidget.setFixedHeight(lastLen+20)
                                      
        BtnA1Msg = codec.toUnicode("提交高绑")
        self.BtnA1=QtGui.QPushButton(BtnA1Msg,self)
        self.BtnA1.setGeometry(110,560,0,0)
        self.BtnA1.setEnabled(True)
        self.BtnA1.setFixedHeight(20)
        self.BtnA1.setFixedWidth(80)
        self.BtnA1.setStyleSheet(Mstyle.pushBtnStyle(kw='off',lang='c'))  
        
        BtnA2Msg = codec.toUnicode("提交低绑 ")
        self.BtnA2=QtGui.QPushButton(BtnA2Msg,self)
        self.BtnA2.setGeometry(20,560,0,0)
        self.BtnA2.setEnabled(True)
        self.BtnA2.setFixedHeight(20)
        self.BtnA2.setFixedWidth(80)
        self.BtnA2.setStyleSheet(Mstyle.pushBtnStyle(kw='off',lang='c'))    
        
        checkLabTitle=('0 of '+str(self.checkCount+1)+' items checked')
        self.checkLab=QtGui.QLabel(checkLabTitle,self)
        self.checkLab.setGeometry(310,560,0,0)
        self.checkLab.setFixedHeight(20)
        self.checkLab.setFixedWidth(130)
        #------main btn connect----------------------------

        self.BtnA1.clicked.connect(self.BtnA1Fn)
        self.BtnA2.clicked.connect(self.BtnA2Fn)


    #--------main function--------------
    def saveScenceImage(self,path,isFront=True):
        
        tempPath='D:\\Program Files\\figo\\RigManaBox_Local\\cutpic\\'
        if not(os.path.exists(tempPath)):
            os.makedirs(tempPath)
        dirs=os.listdir(tempPath)
        number=str(len(dirs))
        fullPath=tempPath+'tempCut'+number+'.0001.png'
        camShape=''
        if isFront:
            mel.eval('dR_DoCmd("viewFront")')
            camShape='frontShape'
        else:
            modelName=(cmds.getPanel(wf=True))
            if 'modelPanel' in modelName:
                type = cmds.modelPanel(modelName, q=True, cam=True)
                camShape=cmds.listRelatives(type,s=1)[0]
            else:
                cmds.confirmDialog(m='need select view panel first')
                return False
        ans=cmds.confirmDialog(title='confirm',m='do you wanna auto fit view?',b=['auto','manual'],cancelButton='manual',defaultButton='auto')
        if ans == 'auto':
            cmds.viewFit(camShape,all=1)
        cmds.playblast(st=1,et=1,format='image',filename=(tempPath+'tempCut'+number),clearCache=1,viewer=0,showOrnaments=1,percent=100,compression='png',quality=100)
        
        #elf.saveImageSignal.emit(fullPath)
        return fullPath
        
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
    def CheckBoxMainFn(self):
        checkState=[self.isSubmitPic]
        if self.isSubmitPic:
            count=1
        else:
            count=0
        for i in self.CheckBoxArray:
            checkState.append( i.isChecked())
            if i.isChecked()==True:
                count+=1
        if False in checkState:
            self.BtnA1.setEnabled(False)
            self.BtnA2.setEnabled(False)
            self.BtnA1.setStyleSheet(Mstyle.pushBtnStyle(kw='off',lang='c'))    
            self.BtnA2.setStyleSheet(Mstyle.pushBtnStyle(kw='off',lang='c'))  
        else:
            self.BtnA1.setEnabled(True)
            self.BtnA2.setEnabled(True)
            self.BtnA1.setStyleSheet(Mstyle.pushBtnStyle(kw='on',lang='c'))    
            self.BtnA2.setStyleSheet(Mstyle.pushBtnStyle(kw='b',lang='c')) 

        self.checkLab.setText((str(count)+' of '+str(self.checkCount+1)+' items checked'))
        
    def BtnA1Fn(self):
        self.highClicked.emit(['h',self.sceenRtn,self.TEA1.toPlainText()])
        #print 'sinal send'

    def BtnA2Fn(self):
        self.lowClicked.emit(['l',self.sceenRtn,self.TEA1.toPlainText()])
        #print 'sinal send'
        
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
            
#cleanUIRT=Rig_submit_TOOL()
#cleanUIRT.Op_Ui()

