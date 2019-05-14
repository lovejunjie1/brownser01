import sys,os,time,json,shutil,random,sqlite3,getpass
path='D://rig_manager_box'
if not path  in sys.path:sys.path.append(path)
import rig_manager_box_pathConfig as pathConfig
from bin.class_editWindowsWithShot06 import textEditorMain
import maya.cmds as cmds
import maya.OpenMayaUI as OpenMayaUI
from shiboken import wrapInstance
from PySide import QtGui, QtCore
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from PySide import QtCore,QtGui
from PySide.QtCore import Qt
from data.redBlackStyleSheet08 import RedBlackStyleSheet
from PySide.QtCore import Qt, QRect  
Mstyle=RedBlackStyleSheet()
from PySide.QtWebKit import QWebView,QWebPage

dir(QWebView)

        
def getMayaWindow():
	"""
	Get Maya window
	:return: maya wnd
	"""
	mayaMainWindowPtr = OpenMayaUI.MQtUtil.mainWindow()
	return wrapInstance(long(mayaMainWindowPtr), QtGui.QWidget)


       
def getScriptPath():
    orgPath = pathConfig.currFile_Path
    return orgPath



class userLoginUI(QtGui.QMainWindow):
    resultSinal = QtCore.Signal(list)
    UITitle='userLoginUI'
    x=250
    y=150
    result=''
    iconPath=''
    def __init__(self, parent = None):

        
        #------Style Set----------------------------

        super(userLoginUI, self).__init__(parent)
        self.m_DragPosition=self.pos()
        self.setFixedHeight(self.y)
        self.setFixedWidth(self.x)
        #self.resize(self.x,self.y)
        
        self.setWindowFlags(Qt.SubWindow|Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setStyleSheet(Mstyle.mainWidgetStyle())
        self.setWindowTitle(self.UITitle)
        
        self.CreateLogin()

        
    def CreateLogin(self):
        #mian=QtGui.QWidget(self)
        #mian.resize(self.x,self.y)
        #close Btn Set                                       
        Xbtn=QtGui.QPushButton('x',self)
        Xbtn.setGeometry(0,0,0,0)
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())
        Xbtn.clicked.connect(self.Cl_Ui)
        
        #TitleLabel
        TitleLab=QtGui.QLabel(self.UITitle,self)
        TitleLab.setGeometry(40,5,0,0)
        TitleLab.setFixedHeight(20)
        TitleLab.setFixedWidth(140)
        TitleLab.setStyleSheet(Mstyle.LabelStyle(fontSize='12px'))

        #cha sel
        mainGrp=QtGui.QGroupBox('login',self)
        mainGrp.setGeometry(10,25,0,0)
        mainGrp.setFixedHeight(self.y*0.8)
        mainGrp.setFixedWidth(self.x*0.9)
        mainGrp.setStyleSheet(Mstyle.GroupBoxStyle())
        
        okBtn=QtGui.QPushButton('OK',mainGrp)
        okBtn.setGeometry(20,85,0,0)
        okBtn.setFixedHeight(20)
        okBtn.setFixedWidth(80)
        okBtn.setStyleSheet(Mstyle.pushBtnStyle(kw='on'))
        
        cancelBtn=QtGui.QPushButton('cancel',mainGrp)
        cancelBtn.setGeometry(120,85,0,0)
        cancelBtn.setFixedHeight(20)
        cancelBtn.setFixedWidth(80)
        cancelBtn.setStyleSheet(Mstyle.pushBtnStyle(kw='b'))
        
        
        userLab=QtGui.QLabel('user',mainGrp)
        userLab.setGeometry(10,20,0,0)
        userLab.setFixedHeight(20)
        userLab.setFixedWidth(40)
        userLab.setStyleSheet('QLabel{background:transparent;font-size:15px}')
        userLab.setAlignment(Qt.AlignRight)
        
        
        passwordLab=QtGui.QLabel('pass',mainGrp)
        passwordLab.setGeometry(10,50,0,0)
        passwordLab.setFixedHeight(20)
        passwordLab.setFixedWidth(40)
        passwordLab.setStyleSheet('QLabel{background:transparent;font-size:15px}')
        passwordLab.setAlignment(Qt.AlignRight)
        
        self.userLE=QtGui.QLineEdit(mainGrp)
        #self.userLE.setText('user')
        self.userLE.setGeometry(60,20,0,0)
        self.userLE.setFixedHeight(20)
        self.userLE.setFixedWidth(self.x*0.6)
        self.userLE.setStyleSheet(Mstyle.LineEditStyle(fontSize='15px'))
        
        self.passwordLE=QtGui.QLineEdit(mainGrp)
        #self.passwordLE.setText('password')
        self.passwordLE.setGeometry(60,50,0,0)
        self.passwordLE.setFixedHeight(20)
        self.passwordLE.setFixedWidth(self.x*0.6)
        self.passwordLE.setStyleSheet(Mstyle.LineEditStyle(fontSize='15px'))
        self.passwordLE.setEchoMode(self.passwordLE.Password)

        self.userLE.selectionChanged.connect(self.pwLEFn)
        self.passwordLE.selectionChanged.connect(self.pwLEFn)
        
        okBtn.clicked.connect(self.BtnA1Fn)
        cancelBtn.clicked.connect(self.Cl_Ui)
        Xbtn.clicked.connect(self.Cl_Ui)
    #--------------button Fns-----------------------------
    def pwLEFn(self):
        sender=self.sender()
        sender.setText('')
    
    def BtnA1Fn(self):
        self.resultSinal.emit([self.userLE.text(),self.passwordLE.text()])
        self.Cl_Ui()

    #--------------FUNCTIONS-----------------------------


              
    #--------------edit event-----------------------------
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

    #------------define swtich--------------------
    def Op_Ui(self):
        self.move(QtGui.QCursor.pos())
        self.show()
        
        
    def Cl_Ui(self):
        self.close()
        self.deleteLater()








class PassWordDataBank():
    initPath=''
    dataBasePath=''
    
    def __init__(self):
        self.initPath=getScriptPath()
        self.dataBasePath=self.initPath+'\\data\\user_data.db'
    
    def val(self,name,pw):
        #name = raw_input("\u7528\u6237\u540d")
        data = self.showdate(name)
        if data:
            passworld = pw
            if data[2] == passworld:
                print "pass word confirm"
                return True
            else:
                print"pass word refuse"
                return False
        else:
            print"pass word empty"
            return False
     
    
    
    def showdate(self,username):
        sql = self.bankInit()
        data = sql.execute("select * from user where name='%s'"% username).fetchone()
        sql.close()
        return data
    
    
    def bankInit(self):
        dataExt=os.path.exists(self.dataBasePath)
        sql=''
        if not dataExt:
            sql = sqlite3.connect(self.dataBasePath)
            sql.execute(
                """create table if not exists
                %s(
                %s integer primary key autoincrement,
                %s varchar(128),
                %s varchar(128))"""
                % ('user',
                   'id',
                   'name',
                   'passworld'))
            sql.close()
        else:
            sql = sqlite3.connect(self.dataBasePath)
            
        return sql
    
    def register(self,input_name,input_passworld): 
        sql=self.bankInit()
        data = sql.execute("select * from user where name='%s'" % input_name).fetchone()
        if not data:
            sql.execute("insert into user(name,passworld) values(?,?)",
                        (input_name,input_passworld))
            sql.commit()
            cmds.warning( "create user success")
            sql.close()
        else:
            cmds.warning( "user already exsits")

  
class dragToolListWidget(QtGui.QTreeWidget):
    onPress=True
    iArray=[]
    isDrag=True
    serverPath=''
    localPath=''
    
    def __init__(self,parent = None):  
        super(dragToolListWidget,self).__init__(parent) 
        self.initPath=getScriptPath()
        self.setContextMenuPolicy(Qt.CustomContextMenu)    
        self.customContextMenuRequested.connect(self.showContextMenu)   
        self.setSelectionMode(self.ExtendedSelection)  
        
    def wheelEvent(self, e):
        if self.onPress:
            nowSize=self.topLevelItem(0).sizeHint(0).width()
            rollSize= nowSize+(e.delta()/120 )
            count = self.topLevelItemCount()
            for i in range(count):
                cNode=self.topLevelItem(i)
                cNode.setSizeHint(0,QtCore.QSize(rollSize,rollSize))
                cCount = cNode.childCount()
                for c in range(cCount):
                    cNode.child(c).setSizeHint(0,QtCore.QSize(rollSize,rollSize))
                    
        super(dragToolListWidget, self).wheelEvent(e)

        
    def mouseMoveEvent(self, e): 
        if e.buttons() != QtCore.Qt.LeftButton:
            return;
        if not self.isDrag:
            return;
        cNodes = self.selectedItems()
        pathArray=[]
        for c in cNodes:
            path=''
            nodeName=c.text(0)
            if '.' in nodeName:
                path=self.serverPath+'\\'+c.parent().text(0)+'\\'+nodeName
            else:
                path=self.serverPath+'\\'+nodeName
            url=QtCore.QUrl.fromLocalFile(QtCore.QFileInfo(path).absoluteFilePath());
            pathArray.append(url)
            
        mimeData = QtCore.QMimeData();
        mimeData.setUrls(pathArray)
        self.drag = QtGui.QDrag(self);
        self.drag.setMimeData(mimeData);
        self.drag.setHotSpot(e.pos() - self.rect().topLeft());
        self.drag.exec_(Qt.CopyAction);
        e.accept(); 
        

   
    def keyPressEvent(self,e):
        if e.key()==QtCore.Qt.Key_Control:
            self.onPress=True
        
            
    def keyReleaseEvent(self,e):
        self.onPress=False
        
    def mouseDoubleClickEvent(self,e): 
        cNode=self.currentItem()
        self.setItemExpanded (cNode,True)
        e.accept(); 
  
    def showContextMenu(self, pos):    
        iconPath=self.initPath+'\\icon\\'
        
        self.contextMenu = QtGui.QMenu(self) 
        self.contextMenu.setStyleSheet(Mstyle.MenuStyle()) 
        
        if self.currentItem().parent():

            actionA = self.contextMenu.addAction(QtGui.QIcon(iconPath+"drag.png"),u'refrence')   
            actionA.triggered.connect(self.actionAFn) 
            actionB = self.contextMenu.addAction(QtGui.QIcon(iconPath+"floder.png"),u'open') 
            actionB.triggered.connect(self.actionBFn)  
              
        actionC = self.contextMenu.addAction(QtGui.QIcon(iconPath+"CommboBoxArrow.png"),u'dowload')   
        actionC.triggered.connect(self.actionCFn) 

        
        self.contextMenu.exec_(QtGui.QCursor.pos()) #show menu on cursor pos  
                  	
    def actionAFn(self):
        cNode=self.selectedItems()
        pathArray=[]
        if len(cNode)>1:
            tempArray=[]
            tails=''
            for i in cNode:
                if i.parent():
                    itm=i.text(0)
                    tails=tails+itm+'\n'
                    tempArray.append(i.parent().text(0)+'\\'+itm)
                    
            msg= '{} files selected\nDo you wanna refrence them all?\n\n'.format(str(len(tempArray)))+tails
            
            ans=cmds.confirmDialog(title='confirm',m=msg,b=['yes','no'],cancelButton='no',defaultButton='no')
            if ans == 'yes':
                pathArray=tempArray
        else:
            if cNode[0].parent():
                pathArray.append(cNode[0].parent().text(0)+'\\'+cNode[0].text(0))
        if pathArray:
            for p in pathArray:
                sp=p.split('\\')
                
                cmds.file( self.serverPath+'\\'+p, reference=True, type='mayaAscii', namespace=sp[0])
        else:
            cmds.confirmDialog(m='no useful data was selected')
    def actionBFn(self):
        cArray=self.selectedItems()
        if len(cArray)!=1:
            cmds.confirmDialog('need sel only 1 item')
        else:
            ci=cArray[0]
            if ci.parent():
                cPath=self.serverPath+'\\'+ci.parent().text(0)+'\\'+ci.text(0)
                cmds.file(f=1,new=1)
                cmds.file(cPath,open=1,f=1)

                          	
    def actionCFn(self):
        cArrays=self.selectedItems()
        for cNode in cArrays:
            if cNode.parent():
                iscopy=True
                Spath=self.serverPath+'\\'+cNode.parent().text(0)+'\\'+cNode.text(0)
                Lpath=self.localPath+'\\'+cNode.parent().text(0)+'\\'+cNode.text(0)
                Lexits=os.path.exists(self.localPath+'\\'+cNode.parent().text(0))
                if not Lexits:
                    os.makedirs(self.localPath+'\\'+cNode.parent().text(0))
                Fexits=os.path.exists(self.localPath+'\\'+cNode.parent().text(0)+'\\'+cNode.text(0))
                if Fexits:
                    ans=cmds.confirmDialog(title='confirm',m='{} is exists.do you wanna replace?'.format(cNode.text(0)),b=['yes','no'],cancelButton='no',defaultButton='no')
                    if ans=='no':
                        iscopy=False
                if iscopy:
                    shutil.copyfile(Spath,Lpath)
    
            else:
                
                Spath=self.serverPath+'\\'+cNode.text(0)
                Lpath=self.localPath+'\\'+cNode.text(0)
                Lexits=os.path.exists(Lpath)
                if Lexits:
                    ans=cmds.confirmDialog(title='confirm',m='{} is exists.do you wanna replace?'.format(cNode.text(0)),b=['yes','no'],cancelButton='no',defaultButton='no')
                    if ans=='yes':
                        print 'replace copy'
                        os.system ("xcopy /s /c /r /i /y %s %s" % (Spath, Lpath))
                    #os.system('cp -R {} {}'.format(Spath,Lpath))
                else:
                    shutil.copytree(Spath,Lpath)


class chooseIcon(QtCore.QObject):
    #class figoIcon(QtGui.QIcon):

    def chooseIcon(self,inputStr,isAuto=True,isDef=False,isBaseRoot=False):
        returnIcon=''
        initPath=getScriptPath()
        
        if isBaseRoot:
            ext=os.path.isfile(initPath+'\\'+inputStr) 
            if ext:
                isAuto=False
                isDef=False
            else:
                isAuto=True
                isDef=False
                isBaseRoot=False
        elif isDef:
            iconPath=initPath+'\\icon\\definedIcon\\'+inputStr+'.png'
            ext=os.path.isfile(iconPath)
            if ext:
                isAuto=False
            else:
                isAuto=True
                isDef=False
        elif not isAuto and not isDef and not isFull:
            isAuto=True
             
        
        if isBaseRoot:
            returnIcon=QtGui.QIcon(initPath+'\\'+inputStr)
        elif isDef:
            iconPath=initPath+'\\icon\\definedIcon\\'+inputStr+'.png'
            returnIcon=QtGui.QIcon(iconPath)
        elif isAuto:
            sum=0
            
            for i in str(inputStr):
                #print i
                num=ord(i)
                sum=sum+num
            random.seed(sum)
            rValue=random.random()
            
            iconPath=initPath+'\\icon\\'
            dirs=os.listdir(iconPath)
            files=[]
            for d in dirs:
                if  os.path.isfile(os.path.join(iconPath,d)):
                    files.append(d)
            count=len(files)
            cnt=int(count*rValue)
            returnIcon=QtGui.QIcon(iconPath+files[cnt])
        return returnIcon 


class RigManagerBoxUI(MayaQWidgetDockableMixin, QtGui.QDialog ,chooseIcon):
    titleName='RigManagerBoxUI'
    widgetHeight=750
    widgetWidth=350
    initPath=''
    UIitems={}
    #pixmapPath='D:/test.png'
    L2=0
    isPicture=False
    isTree=True
    isTab=True
    localPath=''
    serverPath=''
    nowPicPath=''
    keepLogin='Login'
    localSetPath='D:\\Program Files\\figo\\RigManaBox_Local\\'
    def __init__(self, parent=getMayaWindow()):
        self.cleanOpenWindow()
        super(RigManagerBoxUI, self).__init__(parent=parent)
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle(self.titleName)
        self.setMinimumWidth(self.widgetWidth)
        self.setMaximumWidth(self.widgetWidth*3)
        self.setAcceptDrops(True)
        
        self.initPath=getScriptPath()
        self.nowPicPath = self.initPath+'\\data\\currentPic.png'
        
        self.loadConfig()
        
        self.createTitleBar()
        self.createPicture()
        self.createSplitter()

    def loadConfig(self):
        if not os.path.exists(self.localSetPath):
            os.makedirs(self.localSetPath)
        if not os.path.exists(self.localSetPath+'localSet.json'):
            self.saveJson({},self.localSetPath+'localSet.json')
            
        localSetDict=self.loadJson(self.localSetPath+'localSet.json')
        if 'user' in localSetDict.keys():
            self.keepLogin=localSetDict['user']

        
        pathSet=self.initPath+'\\data\\path.json'
        pathDict=self.loadJson(pathSet)
        self.localPath=pathDict['local']
        self.serverPath=pathDict['server']
        
        #loadServerConfig

        #loadLocalConfig

            
           
    def createTitleBar(self):
        qmb=QtGui.QMenuBar(self)
        
        self.fileMn=QtGui.QMenu(self.keepLogin,qmb)
        qmb.addMenu(self.fileMn)
        fileMn1act = self.fileMn.addAction('login')
        self.fileMn2act = self.fileMn.addAction('regist')
        fileMn3act = self.fileMn.addAction('exit')
        #fileMn.setTitle('ggg')
        self.fileMn.addSeparator()#--------------------
        #dir(QtGui.QAction)
        
        shMn=QtGui.QMenu('Layout',qmb)
        qmb.addMenu(shMn)
        self.shMn1act=QtGui.QAction("Picture", shMn, checkable=True)
        self.shMn1act.setChecked(False)
        shMn.addAction(self.shMn1act)
        self.shMn2act = QtGui.QAction("FileList", shMn, checkable=True)
        self.shMn2act.setChecked(True)
        shMn.addAction(self.shMn2act)
        self.shMn3act = QtGui.QAction("MoreInfo", shMn, checkable=True)
        self.shMn3act.setChecked(True)
        shMn.addAction(self.shMn3act)
        shMn.addSeparator()

        toolMn=QtGui.QMenu('Tool',qmb)
        qmb.addMenu(toolMn)
        tool1act = toolMn.addAction("Tool1")
        tool2act = toolMn.addAction("Tool2")
        

        aboutMn=QtGui.QMenu('About',qmb)
        qmb.addMenu(aboutMn)
        about1act = aboutMn.addAction("about author")
        about2act = aboutMn.addAction("how to use")
        
        
        self.shMn1act.changed.connect(self.shMn1actFn)
        self.shMn2act.changed.connect(self.shMn2actFn)
        self.shMn3act.changed.connect(self.shMn3actFn)
        
        fileMn1act.triggered.connect(self.loginFn)
        self.fileMn2act.triggered.connect(self.registFn)
        fileMn3act.triggered.connect(self.exitFn)
        #layoutMn=QtGui.QMenu('Layout',qmb)

    def loginFn(self):
        
        #sender=self.sender()
        logUI=userLoginUI()
        logUI.setParent(self)
        logUI.Op_Ui()
        logUI.resultSinal.connect(self.loginFnReFn)

    def loginFnReFn(self,str):
        passWordDB=PassWordDataBank()
        isConfirm=passWordDB.val(str[0],str[1])
        if isConfirm:
            self.fileMn.setTitle(str[0])
            cs = self.fileMn.children()
            for c in cs:
                if 'regist' == c.text() or 'login' == c.text():
                    c.setVisible(False)
        localSetDict=self.loadJson(self.localSetPath+'localSet.json')
        localSetDict.update({'user':str[0]})
        self.saveJson(localSetDict,self.localSetPath+'localSet.json')

    def registFn(self):
        user=''
        password=''
        result = cmds.promptDialog( title='Register',message='Enter UserName:',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
        if result == 'OK':
            user = cmds.promptDialog(query=True, text=True)
            PWresult = cmds.promptDialog( title='Register',message='Enter PassWord:',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
            if PWresult == 'OK':
                password = cmds.promptDialog(query=True, text=True)
                passWordDB=PassWordDataBank()
                passWordDB.register(user,password)


    def exitFn(self):
        sender=self.sender()
        #print sender.text()
        sender.parent().setTitle('Login')
        cs = self.fileMn.children()
        for c in cs:
            if 'regist' == c.text() or 'login' == c.text():
                c.setVisible(True)
        localSetDict=self.loadJson(self.localSetPath+'localSet.json')
        localSetDict.update({'user':'Login'})
        self.saveJson(localSetDict,self.localSetPath+'localSet.json')
           
    def createPicture(self):
        self.mPixmap=QtGui.QPixmap()
        self.mPixmap.load(self.nowPicPath)

        self.labPic=QtGui.QLabel('',self)
        self.labPic.setPixmap(self.mPixmap)
        self.labPic.setMinimumWidth(self.widgetWidth)
        
        self.scroll=QtGui.QScrollArea(self)
        self.scroll.setWidget(self.labPic)
        self.scroll.setMinimumHeight(self.widgetWidth*0.59)
        self.scroll.setGeometry(0,25,0,self.mPixmap.height())
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        if self.shMn1act.isChecked()==True:
            self.labPic.setVisible(True)
            self.L2=self.mPixmap.height()+25
        else:
            self.labPic.setVisible(False)
            self.L2=25



    def createSplitter(self):

        self.splitter = QtGui.QSplitter(self)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter.setGeometry(0,self.L2,0,0)
        self.splitter.resize(self.widgetWidth,self.widgetWidth*0.6)
        
        tree=self.createTree()
        tree.setParent(self.splitter)
        tree.setVisible(self.isTree)
        
        self.createTab()
        self.tabWid.setParent(self.splitter)
        self.tabWid.setVisible(self.isTab)
        
        



        
    def createTab(self):
        self.tabWid=QtGui.QTabWidget()
        self.tabWid.setMinimumWidth(self.widgetWidth*0.1)
        self.tabWid.setMinimumHeight(self.widgetWidth*0.6)
        self.tabWid.setTabPosition(QtGui.QTabWidget.West)
        self.tabWid.setContentsMargins (0,0,0,0)
        
        
        #---page0----
        msgWid=QtGui.QWidget()
        msgWid.setAttribute(Qt.WA_StyledBackground)
        msgVB=QtGui.QVBoxLayout()
        
        titleHB=QtGui.QHBoxLayout()
        preBtn=QtGui.QPushButton('<--')
        chaLab=QtGui.QLabel('charactorName')
        nextBtn=QtGui.QPushButton('-->')
        titleHB.addWidget(preBtn)
        titleHB.addStretch  (1)
        titleHB.addWidget(chaLab)
        titleHB.addStretch  (1)
        titleHB.addWidget(nextBtn)
        msgVB.addLayout(titleHB)
        
        
        modelGrp=QtGui.QGroupBox('model')
        modelGrp.setMaximumHeight(80)
        modGVB=QtGui.QVBoxLayout()
        modGHB1=QtGui.QHBoxLayout()
        modGHB2=QtGui.QHBoxLayout()
        #modGHB3=QtGui.QHBoxLayout()
        
        
        lab2=QtGui.QLabel('High : ',msgWid)
        modGHB1.addWidget(lab2) 
        modGHB1.addStretch  (1)       
        lab2data=QtGui.QLabel('17-09-13 18:19:54',msgWid)
        modGHB1.addWidget(lab2data)
        modGHB1.addStretch  (1)
        highupBtn=QtGui.QPushButton('update')
        modGHB1.addWidget(highupBtn)
        
        lab2=QtGui.QLabel('Low  : ',msgWid)
        modGHB2.addWidget(lab2) 
        modGHB2.addStretch  (1)       
        lab2data=QtGui.QLabel('17-09-13 18:19:54',msgWid)
        modGHB2.addWidget(lab2data)
        modGHB2.addStretch  (1)
        highupBtn=QtGui.QPushButton('update')
        modGHB2.addWidget(highupBtn)
        
        modGVB.addLayout(modGHB1)
        modGVB.addLayout(modGHB2)
        modelGrp.setLayout(modGVB)
        msgVB.addWidget(modelGrp)

        
        infoGrp=QtGui.QGroupBox('infomation')
        infoGrp.setMaximumHeight(150)
        infoGVB=QtGui.QVBoxLayout()
        
        infoGHB1=QtGui.QHBoxLayout()
        lab4=QtGui.QLabel('Artist : ',msgWid)
        lab4data=QtGui.QLabel('wonderMan',msgWid)
        infoGHB1.addWidget(lab4)
        infoGHB1.addWidget(lab4data)
        infoGHB1.addStretch  (1)
        
        infoGHB2=QtGui.QHBoxLayout()
        lab5=QtGui.QLabel('Passing : ',msgWid)
        lab5data=QtGui.QLabel('xx days',msgWid)
        infoGHB2.addWidget(lab5)
        infoGHB2.addWidget(lab5data)
        infoGHB2.addStretch  (1)
        
        infoGHB3=QtGui.QHBoxLayout()
        lab6=QtGui.QLabel('StartDate : ',msgWid)
        lab6data=QtGui.QLabel('2017-08-02 11:21:42',msgWid)
        infoGHB3.addWidget(lab6)
        infoGHB3.addWidget(lab6data)
        infoGHB3.addStretch  (1)
        
        infoGHB4=QtGui.QHBoxLayout()
        lab7=QtGui.QLabel('ConfirmDate : ',msgWid)
        lab7data=QtGui.QLabel('',msgWid)
        infoGHB4.addWidget(lab7)
        infoGHB4.addWidget(lab7data)
        infoGHB4.addStretch  (1)
        
        infoGHB5=QtGui.QHBoxLayout()
        lab8=QtGui.QLabel('Machine : ',msgWid)
        lab8data=QtGui.QLabel('mdsh017',msgWid)
        infoGHB5.addWidget(lab8)
        infoGHB5.addWidget(lab8data)
        infoGHB5.addStretch  (1)
        infoGVB.addLayout(infoGHB1)
        infoGVB.addLayout(infoGHB2)
        infoGVB.addLayout(infoGHB3)
        infoGVB.addLayout(infoGHB4)
        infoGVB.addLayout(infoGHB5)
        infoGrp.setLayout(infoGVB)
        msgVB.addWidget(infoGrp)

        
        stateGrp=QtGui.QGroupBox('state')
        stateGrp.setMaximumHeight(80)
        stateGrp.setStyleSheet('QGroupBox{color:red;background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0.1 transparent,stop: 0.4 red,stop: 0.8 red,stop: 1.0 transparent)}')
        stateGVB=QtGui.QVBoxLayout()
        
        lab2=QtGui.QLabel('waiting for : Figo',msgWid)
        stateGVB.addWidget(lab2) 
        
        lab2=QtGui.QLabel('there is a editText here ',msgWid)
        stateGVB.addWidget(lab2) 
        stateGVB.addStretch  (1)       
        
        stateGrp.setLayout(stateGVB)
        msgVB.addWidget(stateGrp)
        
        commentGrp=QtGui.QGroupBox('comment')
        comVB=QtGui.QVBoxLayout()
        comVB.setContentsMargins (0,0,0,0)
        comVB.setSpacing (0)
        
        comLE=QtGui.QListWidget()
        comLineE=QtGui.QLineEdit()
        
        comVB.addWidget(comLE)
        comVB.addWidget(comLineE)
        commentGrp.setLayout(comVB)
        msgVB.addWidget(commentGrp)
        
        msgWid.setLayout(msgVB)
        
        self.tabWid.addTab(msgWid,'general')
        #---page1----
        processWid=QtGui.QWidget()
        processWid.setAttribute(Qt.WA_StyledBackground)
        '''
        pwVB=QtGui.QVBoxLayout()
        pwVB.setContentsMargins (0,0,0,0)
        pwVB.setSpacing (0)
        
        
        dir(QtGui.QVBoxLayout)
        
        self.pTree=QtGui.QTreeWidget()
        self.pTree.setHeaderHidden(1)
        pwVB.addWidget(self.pTree)
        
        replyBtn=QtGui.QPushButton('reply')
        pwVB.addWidget(replyBtn)
        viewBtn=QtGui.QPushButton('view')
        pwVB.addWidget(viewBtn)
        submitBtn=QtGui.QPushButton('submit')
        pwVB.addWidget(submitBtn)
        confirmHighBtn=QtGui.QPushButton('confirmHigh')
        pwVB.addWidget(confirmHighBtn)
        confirmLowBtn=QtGui.QPushButton('confirmLow')
        pwVB.addWidget(confirmLowBtn)
        #replyBtn=QtGui.QPushButton('reply')
        
        
        processWid.setLayout(pwVB)
        '''
        self.tabWid.addTab(processWid,'process')
        #---page1 end----
        
        #---page2----
        hisWid=QtGui.QWidget()
        self.tabWid.addTab(hisWid,'history')
        hisVB=QtGui.QVBoxLayout()
        hisVB.setContentsMargins (0,0,0,0)
        hisVB.setSpacing (0)
        
        
        qweb=QWebView()
        qweb.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
        #qpage=QWebPage()
        fffpath=r'Z:\project\pig\asset\PRODUCE\Char\monkeyking\history.html'
        fffdata=open(fffpath)
         
        #qpage.currentFrame().setHtml(fffdata.read(),QtCore.QUrl("d://"));
        qweb.setHtml(fffdata.read(),QtCore.QUrl("d://"));
        #qweb.setPage(qpage)
        hisVB.addWidget(qweb)
        hisWid.setLayout(hisVB)
        qweb.linkClicked.connect(self.linkFn)
        #---page2 end----  
        
        #---page3----

        wid=QtGui.QWidget()
        self.tabWid.addTab(wid,'concept')
        #---page3 end----
        
        #---page4----
        if self.shMn2act.isChecked():
            
            modWid=QtGui.QWidget()
            modVB=QtGui.QVBoxLayout()
        
            vb1=QtGui.QVBoxLayout()
            hb1=QtGui.QHBoxLayout()
            highLabN=QtGui.QLabel('highName')
            highLabT=QtGui.QLabel('highTime')
            vb1.addWidget(highLabN)
            vb1.addWidget(highLabT)
            hb1.addLayout(vb1)
            upBtn=QtGui.QPushButton('check')
            upBtn.setFixedSize(40,40)
            hb1.addWidget(upBtn)
            modVB.addLayout(hb1)
            
            vb2=QtGui.QVBoxLayout()
            hb2=QtGui.QHBoxLayout()
            lowLabN=QtGui.QLabel('lowName')
            lowLabT=QtGui.QLabel('lowTime')
            vb2.addWidget(lowLabN)
            vb2.addWidget(lowLabT)
            hb2.addLayout(vb2)
            upBtn2=QtGui.QPushButton('check')
            upBtn2.setFixedSize(40,40)
            hb2.addWidget(upBtn2)
            modVB.addLayout(hb2)
            modVB.addStretch(1)

            modWid.setLayout(modVB)
            self.tabWid.addTab(modWid,'model')

        #---page4 end----
        #replyBtn.pressed.connect(self.replyBtnFn)
        #submitBtn.pressed.connect(self.submitBtnFn)
        #self.pTree.currentItemChanged .connect(self.pTreeChangeFn)
        
    def linkFn(self,url):
        print 'action'
        print url    
    def createTree(self):
        allowArray=['ma']
        self.vWid=QtGui.QWidget()
        self.vWid.setMinimumWidth(self.widgetWidth*0.1)
        self.vWid.resize(self.widgetWidth*0.5,self.widgetWidth-self.L2)

        vBox=QtGui.QVBoxLayout()
        vBox.setSpacing(0)
        vBox.setContentsMargins(0,0,0,0)
        
        
        LE=QtGui.QLineEdit()
        LE.setAlignment (Qt.AlignHCenter)
        LE.setStyleSheet(Mstyle.LineEditStyle(kw='c',lang='c'))
        vBox.addWidget(LE)
        
        
        self.treeWid=dragToolListWidget()
        self.treeWid.serverPath=self.serverPath
        self.treeWid.localPath=self.localPath
        self.treeWid.setHeaderHidden(1)
        
        #sPath=r'D:\data\temp\Rigging'
        folders=self.getFolders(path=self.serverPath)
        defaultSize=QtCore.QSize(18,18)
        for f in folders:
            itm=QtGui.QTreeWidgetItem()
            itm.setText(0,f)
            itm.setSizeHint(0,defaultSize)
            files=self.getFiles(self.serverPath+'\\'+f)
            for fl in files:
                flsp=fl.split('.')[-1]
                if flsp in allowArray:
                    citm=QtGui.QTreeWidgetItem()
                    citm.setText(0,fl)
                    citm.setSizeHint(0,defaultSize)
                    itm.addChild(citm)
            self.treeWid.addTopLevelItem (itm)
        
        vBox.addWidget(self.treeWid)
        self.vWid.setLayout(vBox)
        self.treeWid.currentItemChanged.connect(self.treeWidChangedFn)
        LE.textChanged.connect(self.LEtextChangedFn)
        return self.vWid

                
        
    #------ button functions ------------------------------    
    def shMn1actFn(self):
        dockSize=self.size()
        sender=self.sender()
        state=sender.isChecked() 
        node=self.scroll
        if state:
            self.isPicture=True
            node.setVisible(True)
            self.L2=(dockSize.width()*0.57)+30
        else:
            self.isPicture=False
            node.setVisible(False)
            self.L2=25
            
        
        self.splitter.setGeometry(0,self.L2,0,0) 
        self.splitter.resize(dockSize.width(),dockSize.height()-self.L2)
        self.labPic.setGeometry(0,25,0,self.mPixmap.height())


       
    def shMn2actFn(self):
        sender=self.sender()
        state=sender.isChecked()
        print sender.text()
        if state:
            self.isTree=True
            self.treeWid.setVisible(True)
        else:
            self.isTree=False
            self.treeWid.setVisible(False)
            
            
    def shMn3actFn(self):
        sender=self.sender()
        state=sender.isChecked()
        #print sender.currentItem().text(0)

        if state:
            self.isTab=True
            self.tabWid.setVisible(True)
        else:
            self.isTab=False
            self.tabWid.setVisible(False)
        
    def pTreeChangeFn(self):
        sender=self.sender()
        #print sender
        if sender.currentItem():
            print sender.currentItem().text(0)
         
    def submitBtnFn(self):
        cItm = self.treeWid.currentItem()
        if cItm:
            ctime = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) 
            
            rp = self.serverPath+'\\'+cItm.text(0)+'\\process\\'+ctime+'_'+ctime+'_smt\\'
            paEx = os.path.exists(rp)
            if not paEx:
                os.makedirs(rp)
                pass
            cmds.file(rename=rp+'PIG_cha_'+cItm.text(0)+'_rig_low.ma')
            cmds.file(save=1)
            
            #print ctime
            
            localJsp=self.serverPath+'\\'+cItm.text(0)+'\\set.json'
            if not os.path.exists(localJsp):
                self.saveJson({'highTime':ctime})
            else:
                self.updateJson('highTime',ctime,localJsp)
            
            
    def replyBtnFn(self):
        itm=self.pTree.currentItem()
        if itm:
            if itm.parent():
                itm=itm.parent()
            self.pItm=itm
            #print 
            
        TEmain=textEditorMain()
        TEmain.setWindowTitle(self.pItm.toolTip(0)+'_'+self.treeWid.currentItem().text(0))
        TEmain.saveSignal.connect(self.replyAnsFn)
        TEmain.show()
        
    def replyAnsFn(self,str):
        reAns=cmds.confirmDialog( title='already saved,do you...', message='Reply file already upload,do you wanna close dialog?', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )
        if reAns=='Yes':
            sender = self.sender()
            sender.close()
        verCode=sender.windowTitle().split('_')[0]
        Charactor=sender.windowTitle().split('_')[-1]
        ctime = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))       
        rp = self.serverPath+'\\'+Charactor+'\\process\\'+verCode+'_'+ctime+'_rpl\\'
        pCheck=os.path.exists(rp)
        if not pCheck:
            os.makedirs(rp)
        
        filename=os.path.basename(str)
        uPath=rp+filename
        shutil.copyfile(str,uPath)
        #saveSignal    
    def treeWidChangedFn(self):
        changeTabItm=''
        sender=self.sender()
        itm=sender.currentItem()
        if itm.parent():
            changeTabItm=itm.parent()
        else:
            changeTabItm=itm

        if self.isTab:
            '''
            self.pTree.clear()
            rP=self.serverPath+'\\'+itm.text(0)+'\\process\\'
            paEx = os.path.exists(rP)
            if paEx:
                fs=self.getFolders(path=rP)
                for f in fs:
                    fl=self.getFiles(path=rP+f)
                    itm=QtGui.QTreeWidgetItem()
                    itm.setToolTip (0,f)
                    spf=f.split('_')
                    f=spf[0]
                    itm.setText(0,(spf[-1]+' : '+f[0:4]+'-'+f[4:6]+'-'+f[6:8]+' '+f[8:10]+':'+f[10:12]+':'+f[-2:]))
                    
                    self.pTree.addTopLevelItem (itm)
                    
                    for lf in fl:
                        subitm=QtGui.QTreeWidgetItem()
                        subitm.setText(0,lf)
                        itm.addChild(subitm)
                    '''
                    
                    
                    
        if self.isPicture:
            filePath=self.serverPath+'\\'+changeTabItm.text(0)+'\\'
            files=self.getFiles(filePath)
            hasPic=[]
            for f in files:
                if '.png' in f:
                    hasPic.append(filePath+f)
    
            if hasPic:         
                if itm.parent():  
                    useDefault = True
                    itmsp=itm.text(0).split('.')
                    for i in hasPic:
                        if itmsp[0] in i:
                            self.nowPicPath = i
                            useDefault=False
                    if useDefault:
                        self.nowPicPath = hasPic[0]
                    
                else:
                    self.nowPicPath = hasPic[0]
            else:
                self.nowPicPath = self.initPath+'\\data\\currentPic.png'
                        
            dockSize=self.size()
            self.widgetHeight=dockSize.height()-5
            self.widgetWidth=dockSize.width()
            
            self.mPixmap.load(self.nowPicPath)
            self.mPixmap=self.mPixmap.scaledToWidth(self.widgetWidth)
            self.labPic.setPixmap(self.mPixmap)
            self.labPic.setGeometry(0,25,0,self.mPixmap.height())
            self.scroll.resize(self.widgetWidth,self.widgetWidth*0.57)


    def LEtextChangedFn(self):
        sender=self.sender()
        nowTxt = sender.text()
        itmsCount=self.treeWid.topLevelItemCount()
        for i in range(itmsCount):
            theNode=self.treeWid.topLevelItem(i)
            if nowTxt in theNode.text(0):
                theNode.setHidden(False)
            else:
                theNode.setHidden(True)
                
    #-------------------- ui functions -------------      


    def getFiles(self,path=''):
        skipArray=['__init__.py','__init__.pyc','Thumbs.db']
        dirs=os.listdir(path)
        files=[]
        for d in dirs:
            if  os.path.isfile(os.path.join(path,d)):
                if not(d in skipArray):
                    files.append(d)
        return files
          
    def getFolders(self,path=''):
        dirs=os.listdir(path)
        floder=[]
        for d in dirs:
            if (not os.path.isfile(os.path.join(path,d))) and d!='data':
                floder.append(d)
        return floder    
        
    def spFn(self):
        sender=self.sender()
        wd=sender.widget(0).width()
        for c in sender.widget(0).children():
            oh=c.height()
            if oh>20:
                oh=sender.widget(0).height()-20
            c.resize(wd,oh)
            
 

    def cleanOpenWindow(self):
        gmw=getMayaWindow()
        for g in gmw.children():
            try:
                Tit=g.windowTitle()
                if Tit==self.titleName:
                    g.close()
                    g.setParent(None)
            except:
                pass  
                  

    #-------------json--------------
    def updateJson(self,key,data,path):

        file_object = open(path,'r')
        data=json.load(file_object)
        data.update({key:data})
        jsonDump=json.dumps(data)
        file_object = open(path, 'w')
        file_object.write(jsonDump)
        file_object.close()


    def loadJson(self,path):
        file_object = open(path,'r')
        data=json.load(file_object)
        return data
          
    def saveJson(self,data,path):
        jsonDump=json.dumps(data)
        file_object = open(path, 'w')
        file_object.write(jsonDump)
        file_object.close()
        
        
        #gg.initPath+'\\appHelp.json'

    def loadJson(self,path):
        file_object = open(path,'r')
        data=json.load(file_object)
        return data
    #------event rewrite-----------
    
    def dockCloseEventTriggered(self):
        """
        Handle stuff when the dock is closed
        """
        self.close()
        self.deleteLater()
   
    def resizeEvent(self,e):
        
        dockSize=self.size()
        self.widgetHeight=dockSize.height()-5
        self.widgetWidth=dockSize.width()
        if self.isPicture:
            self.mPixmap=self.mPixmap.scaledToWidth(self.widgetWidth)
            self.labPic.setPixmap(self.mPixmap)
            self.labPic.resize(self.mPixmap.width(),self.mPixmap.height())
            self.scroll.resize(self.widgetWidth,self.widgetWidth*0.57)
            self.L2=self.scroll.height()+25
        else:
            self.L2=25
        
        self.splitter.setGeometry(0,self.L2,0,0)
        self.splitter.resize(self.widgetWidth,self.widgetHeight-self.L2)
        
        
    def dragEnterEvent(self,e):
        if(e.mimeData().hasFormat("text/uri-list")):
            e.acceptProposedAction() 
            
    def mousePressEvent(self,e):  
        if (e.button() == Qt.LeftButton):
            pass

    def mouseReleaseEvent(self,e):  
        if self.isPicture:
            self.mPixmap.load(self.nowPicPath)
            self.mPixmap=self.mPixmap.scaledToWidth(self.widgetWidth)  
            self.labPic.setPixmap(self.mPixmap)  
            pass
        
        
        
    def dropEvent(self,e):
        if not self.isTab:
            return
        urls = e.mimeData().urls()
        if len(urls)==0:
            return
        '''
        Idx=self.QTwidget.currentIndex()
        cwd=self.QTwidget.widget(Idx)
        pageName = self.QTwidget.tabText(Idx)
        pageType = cwd.statusTip() 
        
        targetUrl=self.initPath+'\\pulg_ins\\'+pageName+'\\'
        for url in urls:
            strUrl=url.path()[1:]
            inputName = str(strUrl).split('/')[-1]
            fromUrl='\\'.join(strUrl.split('/'))
            shutil.copyfile(fromUrl,targetUrl+inputName)

        if '_list' in cwd.statusTip():
            self.s1Mnact1Fn()
        if '_block' in cwd.statusTip():
            self.s1Mnact2Fn()
        '''
  
    def closeEvent(self,e):
        self.deleteLater()
        
    #------------widget enter--------------      
    def Op_Ui(self):
        self.show()
        self.setDockableParameters(dockable=True,floating=False,area='left')
        self.raise_()

            
RigManaBUI=RigManagerBoxUI()
RigManaBUI.Op_Ui()






