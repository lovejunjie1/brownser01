#-*- coding:gbk -*-
import sys,os,time,json,shutil,sqlite3,random,getpass,datetime
path='D://rig_manager_box'
if not path  in sys.path:sys.path.append(path)
import rig_manager_box_pathConfig as pathConfig
import maya.cmds as cmds
import maya.OpenMayaUI as OpenMayaUI
import bin.userLoginUI02 as userLoginUI
#import bin.PassWordDataBank as pwdata
from shiboken import wrapInstance
from PySide import QtGui, QtCore
#from bin.class_editWindowsWithShot06 import textEditorMain
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from data.redBlackStyleSheet08 import RedBlackStyleSheet
from PySide.QtCore import Qt, QRect  
#Mstyle=RedBlackStyleSheet()
from PySide.QtWebKit import QWebView,QWebPage
import bin.rigUploadUI06 as rigUploadUI
import bin.rigConfirmUI09 as rigConfirmUI
from bin import docWriter_reader3
from bin import docWriter_writter6

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
    

class PassWordDataBank():
    initPath=''
    dataBasePath=''
    
    def __init__(self):
        self.initPath=getScriptPath()
        self.dataBasePath=self.initPath+'\\data\\user_data.db'
    
    def val(self,name,pw):
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


class clickLabel(QtGui.QLabel):
    def mousePressEvent(self,e):
        if (e.button() == Qt.LeftButton):
            os.system(self.toolTip())

class dragToolListWidget(QtGui.QTreeWidget):
    onPress=False
    iArray=[]
    isDrag=False
    RigPath=''
    localPath=''
    radGrp=''
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
                path=self.RigPath+'\\'+c.parent().text(0)+'\\'+nodeName
            else:
                path=self.RigPath+'\\asset\\RIG\\'+nodeName
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
        if e.key()==QtCore.Qt.Key_Alt:
            self.isDrag=True
        
            
    def keyReleaseEvent(self,e):
        self.onPress=False
        self.isDrag=False
        
    def mouseDoubleClickEvent(self,e): 
        cNode=self.currentItem()
        self.setItemExpanded (cNode,True)
        e.accept()
  
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
                pagename=''
                checkID=self.radGrp.checkedId()
                if checkID==0:
                    pagename='Char'
                if checkID==1:
                    pagename='Prop'
                if checkID==2:
                    pagename='Env'
                cmds.file( self.RigPath+'\\'+pagename+'\\'+p, reference=True, type='mayaAscii', namespace=sp[0])
        else:
            cmds.confirmDialog(m='no useful data was selected')
    def actionBFn(self):
        cArray=self.selectedItems()
        if len(cArray)!=1:
            cmds.confirmDialog('need sel only 1 item')
        else:
            ci=cArray[0]
            if ci.parent():
                pagename=''
                checkID=self.radGrp.checkedId()
                if checkID==0:
                    pagename='Char'
                if checkID==1:
                    pagename='Prop'
                if checkID==2:
                    pagename='Env'
                cPath=self.RigPath+'\\'+pagename+'\\'+ci.parent().text(0)+'\\'+ci.text(0)
                cmds.file(f=1,new=1)
                cmds.file(cPath,open=1,f=1)

                          	
    def actionCFn(self):
        cArrays=self.selectedItems()
        for cNode in cArrays:
            if cNode.parent():
                iscopy=True
                Spath=self.RigPath+'\\'+cNode.parent().text(0)+'\\'+cNode.text(0)
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
                
                Spath=self.RigPath+'\\'+cNode.text(0)
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


class RigManagerBoxUI(QtGui.QDialog ,MayaQWidgetDockableMixin, chooseIcon):
    titleName='RigManagerBoxUI'
    widgetHeight=750
    widgetWidth=600
    initPath=''
    UIitems={}
    #pixmapPath='D:/test.png'
    L2=0
    #isPicture=False
    isTree=True
    isTab=True
    localPath=''
    serverPath=''
    nowPicPath=''
    keepLogin='Login'
    localSetPath='D:\\Program Files\\figo\\RigManaBox_Local\\'
    nowTreePage='Char'
    nowLowModel=''
    nowHighModel=''
    nowHighModelLocal=''
    nowLowModelLocal=''
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
        #self.createPicture()
        self.createSplitter()

        if self.keepLogin!='Login':
            cs = self.fileMn.children()
            for c in cs:
                if 'regist' == c.text() or 'login' == c.text():
                    c.setVisible(False)


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
        #self.shMn1act=QtGui.QAction("Picture", shMn, checkable=True)
        #self.shMn1act.setChecked(False)
        #shMn.addAction(self.shMn1act)
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
        
        
        #self.shMn1act.changed.connect(self.shMn1actFn)
        self.shMn2act.changed.connect(self.shMn2actFn)
        self.shMn3act.changed.connect(self.shMn3actFn)
        
        fileMn1act.triggered.connect(self.loginFn)
        self.fileMn2act.triggered.connect(self.registFn)
        fileMn3act.triggered.connect(self.exitFn)
        #layoutMn=QtGui.QMenu('Layout',qmb)

    def createPicture(self):
        '''
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
        '''
        pass


    def createSplitter(self):

        self.splitter = QtGui.QSplitter(self)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter.setGeometry(0,self.L2,0,0)
        self.splitter.resize(self.widgetWidth,self.widgetWidth*0.6)
        
        self.createTab()
        self.createTree()
                
        self.vWid.setParent(self.splitter)
        self.vWid.setVisible(self.isTree)
        self.tabWid.setParent(self.splitter)
        self.tabWid.setVisible(self.isTab)
        
    def createTab(self):
        self.tabWid=QtGui.QTabWidget()
        self.tabWid.setStyleSheet(Mstyle.tabWidgetStyle())
        self.tabWid.setMinimumWidth(self.widgetWidth*0.1)
        self.tabWid.setMinimumHeight(self.widgetWidth*0.6)
        self.tabWid.setTabPosition(QtGui.QTabWidget.West)
        self.tabWid.setContentsMargins (0,0,0,0)
        
        
        #---page0----
        
        msgWid=self.createGeneralPage()
        msgWid.setAttribute(Qt.WA_StyledBackground)
        msgWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-top-right-radius: 12px;  border-bottom-left-radius: 12px;border-bottom-right-radius: 12px; }')
        msgWid.setAttribute(Qt.WA_DeleteOnClose)
        self.tabWid.addTab(msgWid,'general')
        #---page1----
        commonWid=QtGui.QWidget()
        commonWid.setAttribute(Qt.WA_StyledBackground)
        commonWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        commonWid.setAttribute(Qt.WA_DeleteOnClose)

        comVB=QtGui.QVBoxLayout()
        comVB.setContentsMargins (0,0,0,0)
        comVB.setSpacing (0)
        
        
        comHbox=QtGui.QHBoxLayout()
        comHbox.setContentsMargins (0,0,0,0)
        comHbox.setSpacing (0)
        
        comWriteBtn=QtGui.QPushButton('write')
        comWriteBtn.setStyleSheet(Mstyle.pushBtnStyle(kw='c'))
        comWriteBtn.setToolTip('write')
        comWriteBtn.setFixedHeight(40)
        
        comEditBtn=QtGui.QPushButton('edit')
        comEditBtn.setStyleSheet(Mstyle.pushBtnStyle(kw='c'))
        comEditBtn.setToolTip('write')
        comEditBtn.setFixedHeight(40)
        comEditBtn.setEnabled(True)
        
        comReadBtn=QtGui.QPushButton('Read')
        comReadBtn.setStyleSheet(Mstyle.pushBtnStyle(kw='c'))
        comReadBtn.setToolTip('write')
        comReadBtn.setFixedHeight(40)
        
        comHbox.addWidget(comWriteBtn)
        comHbox.addWidget(comEditBtn)
        comHbox.addWidget(comReadBtn)
        
        self.comLE=QtGui.QListWidget()
        self.comLE.verticalScrollBar().setStyleSheet('QScrollBar{      background:transparent; width:4px;border-radius:5px; }'
                            'QScrollBar::handle                 {background:rgb(245,75,57); border-radius:5px; }'
                            'QScrollBar::handle:hover           {background:rgb(255,95,77);border-radius:5px; }'
                            'QScrollBar::handle:pressed         {background:rgb(205,53,43);}'
                            'QScrollBar::sub-line               {background:transparent;}'
                            'QScrollBar::add-line               {background:transparent;}' 
                            'QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical{background:transparent;border-radius:5px;}')
        self.comLE.setIconSize(QtCore.QSize(48,48))
        self.comLE.setLayoutMode(QtGui.QListWidget.Batched)
        
        comLineE=QtGui.QLineEdit()
        comLineE.setText('search bar')
        comLineE.setAlignment (Qt.AlignHCenter)
        comLineE.setFixedHeight(24)
        comLineE.setStyleSheet(Mstyle.LineEditStyle(fontSize='14px',bordRad='12px',kw='d',lang='c'))
        
        comVB.addWidget(comLineE)
        comVB.addWidget(self.comLE)
        comVB.addLayout(comHbox)
        commonWid.setLayout(comVB)
        self.tabWid.addTab(commonWid,'note')
        
        #---page1 end----
        
        hisWid=QtGui.QWidget()
        hisWid.setAttribute(Qt.WA_StyledBackground)
        hisWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        hisWid.setAttribute(Qt.WA_DeleteOnClose)
        self.tabWid.addTab(hisWid,'history')
        hisVB=QtGui.QVBoxLayout()
        hisVB.setContentsMargins (0,0,0,0)
        hisVB.setSpacing (0)
        
        blanklabelup=QtGui.QLabel()
        blanklabelup.setFixedHeight(24)
        blanklabelbelow=QtGui.QLabel()
        blanklabelbelow.setFixedHeight(24)
        self.qweb=QWebView()
        self.qweb.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.NonCosmeticDefaultPen|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.qweb.setStyleSheet('QWebView{-webkit-border-radius: 26px}'
)
        self.qweb.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
        #webViewWidget->settings()->setUserStyleSheetUrl( QUrl("qrc:/style.css") );
        hisVB.addWidget(blanklabelup)
        hisVB.addWidget(self.qweb)
        hisVB.addWidget(blanklabelbelow)
        hisWid.setLayout(hisVB)
        self.qweb.linkClicked.connect(self.linkFn)
        
        #---page2 end----  
        
        ConceptWid=QtGui.QWidget()
        ConceptWid.setAttribute(Qt.WA_StyledBackground)
        ConceptWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        ConceptWid.setAttribute(Qt.WA_DeleteOnClose)
        
        self.conceptHbox=QtGui.QGridLayout()
        
        ConceptWid.setLayout(self.conceptHbox)
        self.tabWid.addTab(ConceptWid,'concept')
        
        #---page3 end----

        #replyBtn.pressed.connect(self.replyBtnFn)
        #submitBtn.pressed.connect(self.submitBtnFn)
        #self.pTree.currentItemChanged .connect(self.pTreeChangeFn)
        self.tabWid.currentChanged .connect(self.tabWidChangedFn)
        comWriteBtn.clicked.connect(self.openEidtWindow)
        comEditBtn.clicked.connect(self.loadNoteListData)
        comReadBtn.clicked.connect(self.readNote)
        comLineE.cursorPositionChanged.connect(self.clearSreachBar)
        
        comLineE.textChanged.connect(self.searchNote)
        
    def clearSreachBar(self):
        sender=self.sender()
        if sender.text()=='search bar':
            sender.setText('')
            
    def searchNote(self,str):
        #print str
        itmCount=self.comLE.count()
        for i in range(itmCount):
            itmCell=self.comLE.item(i)
            if str in itmCell.text(): #.encode('utf-8')
                itmCell.setHidden(False)
                #print itmCell.text()
            else:
                itmCell.setHidden(True)
                
    def readNote(self):
        itemNode=''
        if self.treeWid.currentItem ().parent():
            itemNode=self.treeWid.currentItem ().parent()
        else:
            itemNode=self.treeWid.currentItem ()
        
        filedata=''
        noteDir=self.serverPath+'\\asset\\RIG\\'+self.nowTreePage+'\\'+itemNode.text(0)+'\\note\\'+self.comLE.currentItem ().toolTip()
        listdir=os.listdir(noteDir) 
        for i in listdir:
            if '.writer' in i:
                with open(noteDir+'\\'+i,"rt") as file:
                    filedata=file.read().decode('utf-8')
        thewidget=docWriter_reader3.writerReaderUI()  
        #thewidget.setParent(getMayaWindow())
        thewidget.move(0,0)        
        thewidget.setText(filedata)
        thewidget.show()
        raise
        #thewidget.exec_()

        pass
        #print filedata
   
        
    def openEidtWindow(self):
        itemNode=''
        if self.treeWid.currentItem ().parent():
            itemNode=self.treeWid.currentItem ().parent()
        else:
            itemNode=self.treeWid.currentItem ()
        
        TEmain = docWriter_writter6.textEditorMain()
        TEmain.itemName=itemNode.text(0)
        TEmain.savePath=self.serverPath+'\\asset\\RIG\\'+self.nowTreePage+'\\'+itemNode.text(0)+'\\note'
        TEmain.initUI()
        TEmain.setParent(self)
        TEmain.move(0,0)
        TEmain.resize(self.width(),self.height())
        
        TEmain.show()

    def createGeneralPage(self):
        msgWid=QtGui.QWidget()
        msgWid.setAttribute(Qt.WA_StyledBackground)
        msgWid.setAttribute(Qt.WA_DeleteOnClose)
        msgVB=QtGui.QVBoxLayout()
        
        titleHB=QtGui.QHBoxLayout()
        preBtn=QtGui.QPushButton('<--')
        preBtn.setStyleSheet(Mstyle.pushBtnStyle())
        
        preBtn.setToolTip('pre item')
        chaLab=QtGui.QLabel('charactorName')
        chaLab.setStyleSheet(Mstyle.LabelStyle(fontSize='20px'))
        nextBtn=QtGui.QPushButton('-->')
        nextBtn.setStyleSheet(Mstyle.pushBtnStyle())
        nextBtn.setToolTip('next item')
        titleHB.addWidget(preBtn)
        titleHB.addStretch  (1)
        titleHB.addWidget(chaLab)
        titleHB.addStretch  (1)
        titleHB.addWidget(nextBtn)
        msgVB.addLayout(titleHB)
        
        
        Pixmap=QtGui.QPixmap()
        Pixmap.load(self.nowPicPath)
        Pixmap=Pixmap.scaledToWidth(300)
        
        picHbox=QtGui.QHBoxLayout()
        plabPic=QtGui.QLabel('',self)
        plabPic.setToolTip('pic')
        plabPic.setPixmap(Pixmap)
        plabPic.setMaximumWidth(300)
        plabPic.resize(Pixmap.width(),Pixmap.height())
        picHbox.addWidget(plabPic)
        msgVB.addLayout(picHbox)
        
        modelGrp=QtGui.QGroupBox('model')
        modelGrp.setStyleSheet(Mstyle.GroupBoxStyle(kw='b'))
        modelGrp.setMaximumHeight(120)
        modGVB=QtGui.QVBoxLayout()
        modGVB.setContentsMargins (5,5,5,5)
        modGVB.setSpacing (4)
        modGHB1=QtGui.QHBoxLayout()
        modGHB2=QtGui.QHBoxLayout()
        modGHB3=QtGui.QHBoxLayout()
        modGHB4=QtGui.QHBoxLayout()
        
        
        labModHigh=QtGui.QLabel('Serve-H : ',msgWid)
        labModHigh.setStyleSheet(Mstyle.LabelStyle(fontSize='10px',kw='b'))
        modGHB1.addWidget(labModHigh) 
        modGHB1.addStretch  (1)       
        labModHighdata=QtGui.QLabel('',msgWid)
        labModHighdata.setToolTip('highDate')
        labModHighdata.setStyleSheet(Mstyle.LabelStyle(fontSize='10px',kw='b'))
        modGHB1.addWidget(labModHighdata)
        modGHB1.addStretch  (1)
        
        labModLow=QtGui.QLabel('Local_H  : ',msgWid)
        labModLow.setStyleSheet(Mstyle.LabelStyle(fontSize='10px',kw='b'))
        modGHB2.addWidget(labModLow) 
        modGHB2.addStretch  (1)       
        labModLowdata=QtGui.QLabel('',msgWid)
        labModLowdata.setToolTip('highDateLocal')
        labModLowdata.setStyleSheet(Mstyle.LabelStyle(fontSize='10px',kw='b'))
        modGHB2.addWidget(labModLowdata)
        modGHB2.addStretch  (1)
        
        modGHB22=QtGui.QHBoxLayout()
        highupBtn=QtGui.QPushButton('update')
        highupBtn.setStyleSheet(Mstyle.pushBtnStyle(bordRad='8px'))
        highupBtn.setToolTip('highUpdate')
        highreBtn=QtGui.QPushButton('refrence')
        highreBtn.setStyleSheet(Mstyle.pushBtnStyle(bordRad='8px',kw='b'))
        highreBtn.setToolTip('highRefrence')
        modGHB22.addWidget(highupBtn)
        modGHB22.addWidget(highreBtn)
        
        
        labModLow=QtGui.QLabel('Serve-L  : ',msgWid)
        
        labModLow.setStyleSheet(Mstyle.LabelStyle(fontSize='10px',kw='b'))
        modGHB3.addWidget(labModLow) 
        modGHB3.addStretch  (1)       
        labModLowdata=QtGui.QLabel('',msgWid)
        labModLowdata.setStyleSheet(Mstyle.LabelStyle(fontSize='10px',kw='b'))
        labModLowdata.setToolTip('lowDate')
        modGHB3.addWidget(labModLowdata)
        modGHB3.addStretch  (1)
        
        labModLow=QtGui.QLabel('Local_L  : ',msgWid)
        labModLow.setStyleSheet(Mstyle.LabelStyle(fontSize='10px',kw='b'))
        modGHB4.addWidget(labModLow) 
        modGHB4.addStretch  (1)       
        labModLowdata=QtGui.QLabel('',msgWid)
        labModLowdata.setToolTip('lowDateLocal')
        labModLowdata.setStyleSheet(Mstyle.LabelStyle(fontSize='10px',kw='b'))
        modGHB4.addWidget(labModLowdata)
        modGHB4.addStretch  (1)
        
        
        modGHB44=QtGui.QHBoxLayout()
        lowupBtn=QtGui.QPushButton('update')
        lowupBtn.setStyleSheet(Mstyle.pushBtnStyle(bordRad='8px'))
        lowupBtn.setToolTip('lowUpdate')
        lowreBtn=QtGui.QPushButton('refrence')
        lowreBtn.setStyleSheet(Mstyle.pushBtnStyle(bordRad='8px',kw='b'))
        lowreBtn.setToolTip('lowRefrence') 
        modGHB44.addWidget(lowupBtn)
        modGHB44.addWidget(lowreBtn)

        modGVB.addLayout(modGHB3)
        modGVB.addLayout(modGHB4)
        modGVB.addLayout(modGHB44)        
        modGVB.addLayout(modGHB1)
        modGVB.addLayout(modGHB2)
        modGVB.addLayout(modGHB22)
        modelGrp.setLayout(modGVB)
        msgVB.addWidget(modelGrp)

        
        infoGrp=QtGui.QGroupBox('infomation')
        infoGrp.setStyleSheet(Mstyle.GroupBoxStyle(kw='b'))
        infoGrp.setMaximumHeight(150)
        infoGVB=QtGui.QVBoxLayout()
        
        
        lastmsgHB=QtGui.QHBoxLayout()  
        labLastMsgTitle=QtGui.QLabel('LastMsg : ',msgWid)
        labLastMsgTitle.setStyleSheet(Mstyle.LabelStyle(fontSize='10px',kw='b'))
        labLastMsg=QtGui.QLabel('',msgWid)
        
        labLastMsg.setToolTip('lastmsg')
        labLastMsg.setStyleSheet(Mstyle.LabelStyle(fontSize='13px',kw='b',lang='c'))
        lastmsgHB.addWidget(labLastMsgTitle)
        lastmsgHB.addWidget(labLastMsg)
        lastmsgHB.addStretch  (1)
        
        infoGHB1=QtGui.QHBoxLayout()
        lab4=QtGui.QLabel('Artist : ',msgWid)
        lab4.setStyleSheet(Mstyle.LabelStyle(fontSize='10px',kw='b'))
        lab4data=QtGui.QLabel('',msgWid)
        lab4data.setToolTip('artist')
        lab4data.setStyleSheet(Mstyle.LabelStyle(fontSize='13px',kw='b'))
        infoGHB1.addWidget(lab4)
        infoGHB1.addWidget(lab4data)
        infoGHB1.addStretch  (1)
        
        infoGHB2=QtGui.QHBoxLayout()
        lab5=QtGui.QLabel('Passing : ',msgWid)
        lab5.setStyleSheet(Mstyle.LabelStyle(fontSize='10px',kw='b'))
        lab5data=QtGui.QLabel('none days',msgWid)
        lab5data.setStyleSheet(Mstyle.LabelStyle(fontSize='13px',kw='b'))
        lab5data.setToolTip('passing')
        infoGHB2.addWidget(lab5)
        infoGHB2.addWidget(lab5data)
        infoGHB2.addStretch  (1)
        
        infoGHB3=QtGui.QHBoxLayout()
        lab6=QtGui.QLabel('StartDate :     ',msgWid)
        lab6.setStyleSheet(Mstyle.LabelStyle(fontSize='10px',kw='b'))
        lab6data=QtGui.QLabel('',msgWid)
        lab6data.setStyleSheet(Mstyle.LabelStyle(fontSize='13px',kw='b'))
        lab6data.setToolTip('startdate')
        infoGHB3.addWidget(lab6)
        infoGHB3.addWidget(lab6data)
        infoGHB3.addStretch  (1)
        
        infoGHB4=QtGui.QHBoxLayout()
        lab7=QtGui.QLabel('ConfirmDate : ',msgWid)
        lab7.setStyleSheet(Mstyle.LabelStyle(fontSize='10px',kw='b'))
        lab7data=QtGui.QLabel('',msgWid)
        lab7data.setToolTip('confirmdate')
        lab7data.setStyleSheet(Mstyle.LabelStyle(fontSize='13px',kw='b'))
        infoGHB4.addWidget(lab7)
        infoGHB4.addWidget(lab7data)
        infoGHB4.addStretch  (1)
        
        infoGHB5=QtGui.QHBoxLayout()
        lab8=QtGui.QLabel('Machine : ',msgWid)
        lab8.setStyleSheet(Mstyle.LabelStyle(fontSize='10px',kw='b'))
        lab8data=QtGui.QLabel('',msgWid)
        lab8data.setStyleSheet(Mstyle.LabelStyle(fontSize='13px',kw='b'))
        lab8data.setToolTip('machine')
        infoGHB5.addWidget(lab8)
        infoGHB5.addWidget(lab8data)
        infoGHB5.addStretch  (1)
        
        infoGVB.addLayout(lastmsgHB)
        infoGVB.addLayout(infoGHB1)
        infoGVB.addLayout(infoGHB2)
        infoGVB.addLayout(infoGHB3)
        infoGVB.addLayout(infoGHB4)
        infoGVB.addLayout(infoGHB5)
        infoGrp.setLayout(infoGVB)
        msgVB.addWidget(infoGrp)
        
        
        oprGrp=QtGui.QGroupBox('opreate')
        oprGrp.setStyleSheet(Mstyle.GroupBoxStyle(kw='b'))
        oprGrp.setMaximumHeight(150)
        oprGVB=QtGui.QVBoxLayout()
        
        oprGHB1=QtGui.QHBoxLayout()
        oprbtn_uploadLow=QtGui.QPushButton('upload',msgWid)
        oprbtn_uploadLow.setFixedHeight(25)
        oprbtn_uploadLow.setStyleSheet(Mstyle.pushBtnStyle(bordRad='12px'))
        oprbtn_uploadLow.setToolTip('open upload window')
        #oprbtn_uploadHigh=QtGui.QPushButton('uploadHigh',msgWid)
        #oprbtn_uploadHigh.setToolTip('High')
        oprGHB1.addWidget(oprbtn_uploadLow)
        #oprGHB1.addWidget(oprbtn_uploadHigh)
        
        oprGHB2=QtGui.QHBoxLayout()
        oprbtn_confirmLow=QtGui.QPushButton('Confirm',msgWid)
        oprbtn_confirmLow.setFixedHeight(25)
        oprbtn_confirmLow.setStyleSheet(Mstyle.pushBtnStyle(bordRad='12px',kw='b'))
        oprbtn_confirmLow.setToolTip('open confirm window')
        #oprbtn_confirmHigh=QtGui.QPushButton('ConfirmHigh',msgWid)
        #oprbtn_confirmHigh.setToolTip('Confirm_High')
        oprGHB2.addWidget(oprbtn_confirmLow)
        #oprGHB2.addWidget(oprbtn_confirmHigh)
        
        oprGVB.addLayout(oprGHB1)
        oprGVB.addLayout(oprGHB2)
        oprGrp.setLayout(oprGVB)
        msgVB.addWidget(oprGrp)
        #msgVB.addWidget(stateGrp)
        msgVB.addStretch  (1) 
         
        msgWid.setLayout(msgVB)
        
        lowupBtn.clicked.connect(self.copyModelToRigFn)
        highupBtn.clicked.connect(self.copyModelToRigFn)
        preBtn.clicked.connect(self.aboveItemFn)
        nextBtn.clicked.connect(self.belowItemFn)
        
        oprbtn_uploadLow.clicked.connect(self.oprbtn_openUploadFn)
        #oprbtn_uploadHigh.clicked.connect(self.oprbtn_openUploadHighFn)
        oprbtn_confirmLow.clicked.connect(self.oprbtn_confirmFn)
        #oprbtn_confirmHigh.clicked.connect(self.oprbtn_confirmHighFn)
        
        highreBtn.clicked.connect(self.refrenceModelFn)
        lowreBtn.clicked.connect(self.refrenceModelFn)
         
        return msgWid
        
    def refrenceModelFn(self):
        itemNode=''
        if self.treeWid.currentItem ().parent():
            itemNode=self.treeWid.currentItem ().parent()
        else:
            itemNode=self.treeWid.currentItem ()
        
        path=self.serverPath+'\\asset\\RIG\\'+self.nowTreePage+'\\'+itemNode.text(0)+'\\DownloadModel\\'
        
        keyword=''
        if 'low' in self.sender().toolTip():
            keyword='low'
        else:
            keyword='high'
            
        dirs=os.listdir(path)
        for i in dirs:
            if keyword in i:
                path=path+i
                
        if os.path.exists(path):
            cmds.file( path, reference=True, type='mayaAscii', namespace='mod')
        else:
            cmds.confirmDialog(m='file not exists,you need update file from pre-department')
            
    def oprbtn_openUploadFn(self):
        rigUp=rigUploadUI.Rig_submit_TOOL()
        rigUp.setParent(self)
        rigUp.Op_Ui()
        rigUp.lowClicked.connect(self.oprbtn_uploadFn)
        rigUp.highClicked.connect(self.oprbtn_uploadFn)
        
        
    def oprbtn_uploadFn(self,list):
        localtime=time.localtime(time.time())
        nowtime=time.strftime("%Y%m%d%H%M%S", localtime) 
        tyStr=''
        if self.nowTreePage=='Char':
            tyStr='cha'
        else:
            tyStr=self.nowTreePage.lower() 
        
        itemNode=''
        if self.treeWid.currentItem ().parent():
            itemNode=self.treeWid.currentItem ().parent()
        else:
            itemNode=self.treeWid.currentItem ()
        
        servSp= self.serverPath.split('\\')
        servSp.append('asset')
        servSp.append('RIG')
        servSp.append(self.nowTreePage)
        servSp.append(itemNode.text(0))
        servSp.append('uploadTemp')   
        servPath=''   
              
        localSp= self.localPath.split('\\')
        localSp.append(self.nowTreePage)
        localSp.append(itemNode.text(0))
        localSp.append('uploadTemp')
        localPath='' 
        
        buttonKey=''
        
        if list[0]=='l':
            buttonKey='low'
            filename='PIG_'+tyStr+'_'+itemNode.text(0)+'_rig_low.ma'
            
            servSp.append('low')
            servSp.append(nowtime)
            servPath='\\'.join(servSp) 
            os.makedirs(servPath)

            localSp.append('low')
            localSp.append(nowtime)
            localPath='\\'.join(localSp)
            os.makedirs(localPath)
            
        if list[0]=='h':
            buttonKey='high'
            filename='PIG_'+tyStr+'_'+itemNode.text(0)+'_rig_high.ma'
            
            servSp.append('high')
            servSp.append(nowtime)
            servPath='\\'.join(servSp) 
            os.makedirs(servPath)

            localSp.append('high')
            localSp.append(nowtime)
            localPath='\\'.join(localSp)
            os.makedirs(localPath)
        
        #print servPath+'\\'+filename
        #print localPath+'\\'+filename
        shutil.copyfile(list[1], localPath+'\\sceenshot.png')
        shutil.copystat(list[1], localPath+'\\sceenshot.png')
        
        
        shutil.copyfile(list[1], servPath+'\\sceenshot.png')
        shutil.copystat(list[1], servPath+'\\sceenshot.png')
        
        self.saveJson(list[2],localPath+'\\message.json')
        self.saveJson(list[2],servPath+'\\message.json')
        
        
        
        
        cmds.file( rename=servPath+'\\'+filename)
        cmds.file( save=True, type='mayaAscii' )
        
        cmds.file( rename=localPath+'\\'+filename)
        cmds.file( save=True, type='mayaAscii' )
        ans=cmds.confirmDialog(title='confirm',m='upload finished\ndo you wanna clean the state?',b=['clean','keep'],cancelButton='keep',defaultButton='clean')
        if ans == 'clean':
            cmds.file(new=1)
        #print self.sender()
        

            
        historypath=self.serverPath+'\\asset\\PRODUCE\\'+self.nowTreePage+'\\'+itemNode.text(0)+'\\history.html'
        if not (os.path.exists(historypath)):
            self.HTML_CreateEmptyStyle(historypath)
        
        userName=self.fileMn.title()
        if userName.lower()=='login':
            ans=cmds.confirmDialog(title='confirm',m='user not login,do you wanna user machine ID or input by yourself.',b=['machineID','input'],cancelButton='machineID',defaultButton='machineID')
            if ans == 'machineID':
                userName=getpass.getuser()
            elif ans == 'input':
                try:
                    userName=raw_input()
                except EOFError:
                    userName=getpass.getuser()

        
        innerMsg='[ RIG ][ '+buttonKey+' ] upload <br> updateTime : '+time.strftime("%Y-%m-%d %H:%M:%S", localtime) +'<br>update by '+userName
        htmlMsg=self.HTML_createMsg(innerMsg,userName,'',side=1,initPath=self.initPath) 
        self.HTML_addMsg(historypath,htmlMsg)

        


        
    def oprbtn_confirmFn(self):
        if self.treeWid.currentItem ():
            itemNode=''
            if self.treeWid.currentItem ().parent():
                itemNode=self.treeWid.currentItem ().parent()
            else:
                itemNode=self.treeWid.currentItem ()
            tyStr=''
            if self.nowTreePage=='Char':
                tyStr='cha'
            else:
                tyStr=self.nowTreePage.lower() 
                
            servSp= self.serverPath.split('\\')
            servSp.append('asset')
            servSp.append('RIG')
            servSp.append(self.nowTreePage)
            servSp.append(itemNode.text(0))
            servSp.append('uploadTemp')   
            servPath='\\'.join(servSp)
            
            confirm=rigConfirmUI.Rig_confirm_TOOL()
            confirm.setParent(self)
            confirm.searchPath=servPath
            confirm.workName=itemNode.text(0)
            confirm.createUI()
            confirm.fillListWidget()
            confirm.Op_Ui()
            
            confirm.confirmClicked.connect(self.confirmFn)
        else:
            print 'need select item first'

    def confirmFn(self,list):
        sp1=list[1].split('\\')
        fileName=os.path.basename(list[2])
        
        pathsp=sp1[0:-4]
        path='\\'.join(pathsp)+'\\'
        
        theDict=self.loadJson(path+'infomation.json')
        strTime= time.strftime("%m-%d %H:%M:%S %Y", time.localtime(time.time()))  
        theDict['confirmDate'].append(strTime)
        
        sDate=theDict['startDate'][1]
        spSD = sDate.split(' ')
        daySD=int(spSD[0].split('-')[1])
        monSD=int(spSD[0].split('-')[0])
        yearSD=int(spSD[-1])
        nowdate=time.strftime("%m-%d-%Y", time.localtime(time.time())  )
        dayND=int(nowdate.split('-')[1])
        monND=int(nowdate.split('-')[0])
        yearND=int(nowdate.split('-')[2])
        d1 = datetime.datetime(yearSD, monSD, daySD)
        d2 = datetime.datetime(yearND, monND, dayND)
        passs=str((d2-d1).days)+' days'
        theDict['passing']=passs
        
        if not('message' in theDict.keys()):
            theDict.update({'message':['empty']})
        theDict['message'].append(list[3])
        
        self.saveJson(theDict,path+'infomation.json')
        #infomation update over
        if os.path.exists(path+sp1[-1]):
            os.remove(path+sp1[-1])
        
        shutil.copyfile(list[1], path+sp1[-1])
        shutil.copystat(list[1], path+sp1[-1])
        
        if os.path.exists(path+fileName):
            os.remove(path+fileName)
        #_UNKNOWN_REF_NODE_
        
        refs = cmds.ls(type='reference')
        if refs:
            refstr='\n'.join(refs)
            ans=cmds.confirmDialog(title='confirm',m=refstr+'\nrefrence nodes in scene,do you wanna clean?',b=['clean','keep'],cancelButton='keep',defaultButton='clean')
            if ans == 'clean':
                for i in refs:
                    rFile = cmds.referenceQuery(i, f=True)
                    cmds.file(rFile, importReference=True)
        
        cmds.file(rename=path+fileName)
        cmds.file( save=True, type='mayaAscii' )
        
        ans=cmds.confirmDialog(title='confirm',m='confirm finished\ndo you wanna clean the state?',b=['clean','keep'],cancelButton='keep',defaultButton='clean')
        if ans == 'clean':
            cmds.file(new=1)
        
        #confirm over

        changeTabItm=''
        if self.treeWid.currentItem ().parent():
            changeTabItm=self.treeWid.currentItem ().parent()
        else:
            changeTabItm=self.treeWid.currentItem ()
            
        historypath=self.serverPath+'\\asset\\PRODUCE\\'+self.nowTreePage+'\\'+changeTabItm.text(0)+'\\history.html'
        if not (os.path.exists(historypath)):
            self.HTML_CreateEmptyStyle(historypath)
        
        userName=self.fileMn.title()
        if userName.lower()=='login':
            ans=cmds.confirmDialog(title='confirm',m='user not login,do you wanna user machine ID or input by yourself.',b=['machineID','input'],cancelButton='machineID',defaultButton='machineID')
            if ans == 'machineID':
                userName=getpass.getuser()
            elif ans == 'input':
                try:
                    userName=raw_input()
                except EOFError:
                    userName=getpass.getuser()
        tempArray=theDict['artist']
        tempArray.remove('none')
        artString=','.join(tempArray)
        
        innerMsg='[ RIG ][ '+list[0]+' ] confirm the file <br> days : '+passs+'<br>startTime : '+sDate+'<br>artist : '+artString+'<br>confirm by '+userName
        htmlMsg=self.HTML_createMsg(innerMsg,userName,'',side=1,initPath=self.initPath) 
        self.HTML_addMsg(historypath,htmlMsg)
        
      
        
    def createTree(self):
        
        self.vWid=QtGui.QWidget()
        self.vWid.setMinimumWidth(self.widgetWidth*0.1)
        self.vWid.resize(self.widgetWidth*0.5,self.widgetWidth-self.L2)

        vBox=QtGui.QVBoxLayout()
        vBox.setSpacing(0)
        vBox.setContentsMargins(0,0,0,0)
        
        radHBox=QtGui.QHBoxLayout()
        
        
        rad1=QtGui.QPushButton('cha')
        rad1.setFixedHeight(25)
        rad1.setStyleSheet(Mstyle.pushBtnStyle(kw='radiobutton',bordRad='6px'))
        rad1.setAutoExclusive (True)
        rad1.setCheckable (True)
        rad1.setToolTip('charactor page')
        #rad1=QtGui.QRadioButton ('C')
        rad1.setChecked(True)
        radHBox.addWidget(rad1)
        
        rad2=QtGui.QPushButton('prop')
        rad2.setFixedHeight(25)
        rad2.setStyleSheet(Mstyle.pushBtnStyle(kw='radiobutton',bordRad='6px'))
        #rad2=QtGui.QRadioButton ('P')
        rad2.setAutoExclusive (True)
        rad2.setCheckable (True)
        rad2.setToolTip('prop page')
        radHBox.addWidget(rad2)
        
        rad3=QtGui.QPushButton('env')
        rad3.setFixedHeight(25)
        rad3.setStyleSheet(Mstyle.pushBtnStyle(kw='radiobutton',bordRad='6px'))
        #rad3=QtGui.QRadioButton ('E')
        rad3.setAutoExclusive (True)
        rad3.setCheckable (True)
        rad3.setToolTip('everioment page')
        radHBox.addWidget(rad3)
        
        
        
        self.radGrp=QtGui.QButtonGroup()
        self.radGrp.setExclusive (True)
        self.radGrp.addButton(rad1,0)
        self.radGrp.addButton(rad2,1)
        self.radGrp.addButton(rad3,2)
        
        
        LE=QtGui.QLineEdit()
        LE.setAlignment (Qt.AlignHCenter)
        LE.setStyleSheet(Mstyle.LineEditStyle(kw='d',lang='c'))
        
        
        
        self.treeWid=dragToolListWidget()
        self.treeWid.verticalScrollBar().setStyleSheet('QScrollBar{      background:transparent; width:4px;border-radius:5px; }'
                                    'QScrollBar::handle                 {background:rgb(245,75,57); border-radius:5px; }'
                                    'QScrollBar::handle:hover           {background:rgb(255,95,77);border-radius:5px; }'
                                    'QScrollBar::handle:pressed         {background:rgb(205,53,43);}'
                                    'QScrollBar::sub-line               {background:transparent;}'
                                    'QScrollBar::add-line               {background:transparent;}' 
                                    'QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical{background:transparent;border-radius:5px;}')
        #self.treeWid.setAlternatingRowColors(True)
        self.treeWid.setStyleSheet( 'QTreeWidget{outline:0;background-color:rgb(68,68,68);border:0px;}'
                                    'QTreeWidget::item{gridline-color: rgba(255, 255, 255, 255);padding-left:5px;background-color: transparent;color: rgb(180, 180, 180);}'
                                    'QTreeView::item:open {background-color: rgb(108,108,108);color: rgb(210, 210, 210);}'
                                    'QTreeWidget::item:hover{color: rgb(255, 255, 255);}'
                                    'QTreeWidget::item:selected{background-color: rgb(108,108,108);color: rgb(210, 210, 210);}'
                                    'QTreeView::branch {gridline-color: rgba(255, 255, 255, 255);background-color: rgb(68,68,68);}'
                                    'QTreeView::branch:hover {image: url(branch-open.png);}'
                                    'QTreeView::branch:open {image: url(branch-open.png);}'
                                    'QTreeView::branch:closed:has-children {image: url(branch-closed.png);}'
                                    'QTreeView::indicator:checked {background-color:rgb(255,0,0);image: url(path);}'
                                    'QTreeView::indicator:unchecked {background-color:rgb(0,0,255);image: url(path);} '
                                    )
        self.treeWid.RigPath=self.serverPath+'\\asset\\RIG'
        self.treeWid.localPath=self.localPath
        self.treeWid.setHeaderHidden(1)
        self.treeWid.radGrp=self.radGrp

        self.createTreeList()
        vBox.addLayout(radHBox)
        vBox.addWidget(LE)
        vBox.addWidget(self.treeWid)
        self.leftArray=[LE,rad1,rad2,rad3]
        self.vWid.setLayout(vBox)
        
        self.treeWid.currentItemChanged.connect(self.treeWidChangedFn)
        LE.textChanged.connect(self.LEtextChangedFn)
        rad3.clicked.connect(self.radClickFn)
        rad2.clicked.connect(self.radClickFn)
        rad1.clicked.connect(self.radClickFn)
        

        self.treeWid.setCurrentItem (self.treeWid.itemAt(0,0))
        return self.vWid


 
    def createTreeList(self,page='Char'): 
        allowArray=['ma']         
        folders=self.getFolders(path=(self.serverPath+'\\asset\\RIG\\'+page))
        defaultSize=QtCore.QSize(18,18)
        self.treeWid.clear()
        for f in folders:
            itm=QtGui.QTreeWidgetItem()
            itm.setText(0,f)
            itm.setSizeHint(0,defaultSize)
            files=self.getFiles(self.serverPath+'\\asset\\RIG\\'+page+'\\'+f)
            for fl in files:
                flsp=fl.split('.')[-1]
                if flsp in allowArray:
                    citm=QtGui.QTreeWidgetItem()
                    citm.setText(0,fl)
                    citm.setSizeHint(0,defaultSize)
                    itm.addChild(citm)
            self.treeWid.addTopLevelItem (itm)
    #------ button functions ------------------------------    

    def loginFn(self):
        logUI=userLoginUI.userLoginUI()
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
        pass
        
    def exitFn(self):
        sender=self.sender()
        sender.parent().setTitle('Login')
        cs = self.fileMn.children()
        for c in cs:
            if 'regist' == c.text() or 'login' == c.text():
                c.setVisible(True)
        localSetDict=self.loadJson(self.localSetPath+'localSet.json')
        localSetDict.update({'user':'Login'})
        self.saveJson(localSetDict,self.localSetPath+'localSet.json')
           
           
    def radClickFn(self):
        nowsel=self.radGrp.checkedId()
        if nowsel==0:
            self.createTreeList(page='Char')
            self.nowTreePage='Char'
            #self.serverPath=self.serverPath+'\\Char'
            #folder='char'
        elif nowsel==1:
            self.createTreeList(page='Prop')
            self.nowTreePage='Prop'
            #self.serverPath=self.serverPath+'\\Prop'
            #folder='prop'
        elif nowsel==2:
            self.createTreeList(page='Env')
            self.nowTreePage='Env'
            #self.serverPath=self.serverPath+'\\Env'
            #folder='env'

    def aboveItemFn(self):
        node = self.treeWid.itemAbove(self.treeWid.currentItem())
        if node:
            self.treeWid.setCurrentItem(node)
    def belowItemFn(self):
        node = self.treeWid.itemBelow(self.treeWid.currentItem())
        if node:
            self.treeWid.setCurrentItem(node)



    def tabWidChangedFn(self):
        itemNode=''
        if self.treeWid.currentItem ().parent():
            itemNode=self.treeWid.currentItem ().parent()
        else:
            itemNode=self.treeWid.currentItem ()
            
        nowTab = self.tabWid.currentIndex()
        if nowTab==0:
            self.loadGeneralPageData(itemNode)
        if nowTab==1:
            self.loadNoteListData()
        if nowTab==2:
            self.loadHTMLHistoryData(itemNode)
        if nowTab==3:
            self.loadConceptPictureData(itemNode)
            
    def linkFn(self,url):
        print 'use .write reader open .write file to check infomations'
        print url             
    
    
    def shMn1actFn(self):
        pass
        '''
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

        '''
       
    def shMn2actFn(self):
        sender=self.sender()
        state=sender.isChecked()
        #print sender.text()
        if state:
            self.isTree=True
            self.vWid.setVisible(True)
        else:
            self.isTree=False
            self.vWid.setVisible(False)
            
            
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
            
            
    def copyModelToRigFn(self):
        sender=self.sender()
        buttonKey=''
        if 'low' in sender.toolTip():
            buttonKey='low'
            if self.nowLowModel:
                if os.path.exists(self.nowHighModelLocal):
                    os.system ("xcopy /s /c /r /i /y %s %s" % (self.nowLowModel, self.nowLowModelLocal))
                else:
                    shutil.copyfile(self.nowLowModel, self.nowLowModelLocal)
                    shutil.copystat(self.nowLowModel, self.nowLowModelLocal)
            else:
                print 'low file not exists'
                return False
        if 'high' in sender.toolTip():
            buttonKey='high'
            if self.nowHighModel:
                if os.path.exists(self.nowHighModelLocal):
                    os.system ("xcopy /s /c /r /i /y %s %s" % (self.nowHighModel, self.nowHighModelLocal))
                else:
                    shutil.copyfile(self.nowHighModel, self.nowHighModelLocal)
                    shutil.copystat(self.nowHighModel, self.nowHighModelLocal)
            else:
                print 'high file not exists'
                return False
                
        itm=self.treeWid.currentItem()
        changeTabItm=''
        if itm.parent():
            changeTabItm=itm.parent()
        else:
            changeTabItm=itm
                  
        infoPath=self.serverPath+'\\asset\\RIG\\'+self.nowTreePage+'\\'+changeTabItm.text(0)+'\\infomation.json'
        dict=self.loadJson(infoPath)
        
        artName=''
        if self.fileMn.title().lower()!='login':
            artName=self.fileMn.title()
        else:
            artName=getpass.getuser()
        if not(artName in dict['artist']):
            dict['artist'].append(artName)
        
        sDate=time.strftime("%m-%d %H:%M:%S %Y", time.localtime(time.time()))  
        dict['startDate'].append(sDate)
        dict['machine'].append( getpass.getuser())  
        self.saveJson(dict,infoPath)          
                    
                    

        self.loadGeneralPageData(itm)
        #general function over
        
        
        historypath=self.serverPath+'\\asset\\PRODUCE\\'+self.nowTreePage+'\\'+changeTabItm.text(0)+'\\history.html'
        if not (os.path.exists(historypath)):
            self.HTML_CreateEmptyStyle(historypath)
        
        userName=self.fileMn.title()
        if userName.lower()=='login':
            ans=cmds.confirmDialog(title='confirm',m='user not login,do you wanna user machine ID or input by yourself.',b=['machineID','input'],cancelButton='machineID',defaultButton='machineID')
            if ans == 'machineID':
                userName=getpass.getuser()
            elif ans == 'input':
                try:
                    userName=raw_input()
                except EOFError:
                    userName=getpass.getuser()
                    
        innerMsg='[ RIG ][ '+buttonKey+' ] copy the model from model path to rig path'
        htmlMsg=self.HTML_createMsg(innerMsg,userName,'',side=1,initPath=self.initPath) 
        self.HTML_addMsg(historypath,htmlMsg)
        
        #html message over
        return True
        
    def loadGeneralPageData(self,changeTabItm):
            
        preBtn=''
        nextBtn=''
        picLabel=''
        titleLabel=''
        
        
        hDate=''
        lDate=''
        hDateLoc=''
        lDateLoc=''
        
        artistlab=''
        passinglab=''
        startdatelab=''
        confirmdatelab=''
        machinelab=''
        lastmsglab=''
        for c in self.tabWid.currentWidget().children():
            if type(c)==QtGui.QPushButton:
                if c.toolTip()=='pre item':
                    preBtn=c
                if c.toolTip()=='next item':
                    nextBtn=c
            if type(c)==QtGui.QLabel:
                
                if c.toolTip()=='pic':
                    picLabel=c
                    
                    
                else:
                    titleLabel=c
            if type(c)==QtGui.QGroupBox:
                if c.title()=='model':
                    for cc in c.children():
                        if type(cc)!=QtGui.QVBoxLayout:
                            if cc.toolTip()=='highDate':
                                hDate=cc
                            elif cc.toolTip()=='lowDate':
                                lDate=cc
                            elif cc.toolTip()=='highDateLocal':
                                hDateLoc=cc
                            elif cc.toolTip()=='lowDateLocal':
                                lDateLoc=cc
                                
                if c.title()=='infomation':
                    for cc in c.children():
                        if type(cc)!=QtGui.QVBoxLayout:
                            if cc.toolTip()=='artist':
                                artistlab=cc
                            if cc.toolTip()=='passing':
                                passinglab=cc
                            if cc.toolTip()=='startdate':
                                startdatelab=cc
                            if cc.toolTip()=='confirmdate':
                                confirmdatelab=cc
                            if cc.toolTip()=='machine':
                                machinelab=cc  
                            if cc.toolTip()=='lastmsg':
                                lastmsg=cc                
        #from widget , load every lab in variable,over
        
        filePath=self.serverPath+'\\asset\\RIG\\'+self.nowTreePage+'\\'+changeTabItm.text(0)+'\\'
        files=self.getFiles(filePath)
        hasPic=[]
        for f in files:
            if '.png' in f:
                hasPic.append(filePath+f)
            
        if hasPic: 
            self.nowPicPath = hasPic[0]
        else:
            self.nowPicPath = self.initPath+'\\data\\currentPic.png'  
        picLabel.pixmap().load(self.nowPicPath)
        scalePic=picLabel.pixmap().scaledToWidth(300)
        picLabel.setPixmap(scalePic)
        
        #load picmap under folder over
        
        #load title label     
        titleLabel.setText(changeTabItm.text(0))
        #load model info
        lFile=''
        hFile=''     
        sp = self.serverPath.split('\\')
        sp.append('asset')
        sp.append('MODEL')
        sp.append(self.nowTreePage)
        sp.append(changeTabItm.text(0))
        modelPath='\\'.join(sp)
        mFiles=os.listdir(modelPath)
        for m in mFiles:
            if m[-3:]=='.ma':
                if '_high' in m:
                    hFile=modelPath+'\\'+m
                    self.nowHighModel=hFile
                if '_low' in m:
                    lFile=modelPath+'\\'+m
                    self.nowLowModel=lFile
                                                           
                    
        sp = self.serverPath.split('\\')
        sp.append('asset')
        sp.append('RIG')
        sp.append(self.nowTreePage)
        sp.append(changeTabItm.text(0))
        sp.append('DownloadModel')
        rigPath='\\'.join(sp)
        if os.path.exists(rigPath):
            Ctype=self.nowTreePage.lower()
            if Ctype=='char':
                Ctype='cha'
            lowArray=['PIG',Ctype,changeTabItm.text(0),'mod','low.ma']
            lowName='_'.join(lowArray)
            self.nowLowModelLocal=rigPath+'\\'+lowName
            
            highArray=['PIG',Ctype,changeTabItm.text(0),'mod','high.ma']
            highName='_'.join(highArray)
            self.nowHighModelLocal=rigPath+'\\'+highName
            
            if os.path.exists(self.nowLowModelLocal):
                strTime= time.strftime("%m-%d %H:%M:%S %Y", time.localtime(os.path.getmtime(self.nowLowModelLocal)))  
                lDateLoc.setText(strTime)  
            else:
                lDateLoc.setText('') 
                
            if os.path.exists(self.nowHighModelLocal):
                strTime= time.strftime("%m-%d %H:%M:%S %Y", time.localtime(os.path.getmtime(self.nowHighModelLocal)))  
                hDateLoc.setText(strTime)  
            else:
                hDateLoc.setText('') 
                
                
        else:
            os.makedirs(rigPath)
        
        if hFile:
            strTime= time.strftime("%m-%d %H:%M:%S %Y", time.localtime(os.path.getmtime(hFile)))  
            hDate.setText(strTime)  
        else:
            hDate.setText('')  
            
        if lFile:
            strTime= time.strftime("%m-%d %H:%M:%S %Y", time.localtime(os.path.getmtime(lFile)))  
            lDate.setText(strTime)  
        else:
            lDate.setText('')
            
        #load model infomations over
            
        #load infomation
        infoPath=self.serverPath+'\\asset\\RIG\\'+self.nowTreePage+'\\'+changeTabItm.text(0)+'\\infomation.json'
                    
        isExt=os.path.exists(infoPath)
        art=''
        passs=''
        sDate=''
        cDate=''
        machin=''
        msg=''
        if isExt:
            dict=self.loadJson(infoPath)
            art=dict['artist'][-1]
            
            if 'message' in dict.keys():
                if len(dict['message'])<=1:
                    msg='empty'
                else:
                    msg=dict['message'][-1]
            else:
                msg='empty'
            
            if len(dict['startDate'])<=1:
                sDate=dict['startDate'][0]
                passs='none days'
            else:
                sDate=dict['startDate'][1]
                if dict['passing']!='':
                    passs=dict['passing']
                else:
                    spSD = sDate.split(' ')
                    daySD=int(spSD[0].split('-')[1])
                    monSD=int(spSD[0].split('-')[0])
                    yearSD=int(spSD[-1])
                    nowdate=time.strftime("%m-%d-%Y", time.localtime(time.time())  )
                    dayND=int(nowdate.split('-')[1])
                    monND=int(nowdate.split('-')[0])
                    yearND=int(nowdate.split('-')[2])
                    d1 = datetime.datetime(yearSD, monSD, daySD)
                    d2 = datetime.datetime(yearND, monND, dayND)
                    passs=str((d2-d1).days)+' days'
            
            if len(dict['confirmDate'])<=1:
                cDate=dict['confirmDate'][0]
            else:
                cDate=dict['confirmDate'][-1]
            machin=dict['machine'][-1]
        else:
            emptyDict={'artist':['none'],'passing':'','startDate':['notStart'],'confirmDate':['notConfirm'],'machine':['empty'],'message':['empty']}
            self.saveJson(emptyDict,infoPath)
        
        artistlab.setText(art) 
        passinglab.setText(passs) 
        startdatelab.setText(sDate) 
        confirmdatelab.setText(cDate) 
        machinelab.setText(machin)  
        lastmsg.setText(msg)   
        #load infomations over 
        pass
        
    def loadHTMLHistoryData(self,changeTabItm):
        if type(changeTabItm)!=str:
            historypath=self.serverPath+'\\asset\\PRODUCE\\'+self.nowTreePage+'\\'+changeTabItm.text(0)+'\\history.html'
            if (os.path.exists(historypath)):
                historydata=open(historypath)
                self.qweb.setHtml(historydata.read(),QtCore.QUrl(self.serverPath+'\\asset\\RIG\\'+self.nowTreePage+'\\'+changeTabItm.text(0)+'\\note'))
            else:
                self.qweb.setHtml('','')
        pass  
    def loadConceptPictureData(self,changeTabItm):
        
        #load concept pictures
        
        self.clearLayout(self.conceptHbox)
        
        conceptPath=self.serverPath+'\\asset\\CONCEPT\\'+self.nowTreePage+'\\'+changeTabItm.text(0)
        isConceptExt=os.path.exists(conceptPath)
        
        pixmapArray=[]
        if isConceptExt:
            temps=os.listdir(conceptPath)
            for i in temps:
                isf=os.path.isfile(conceptPath+'\\'+i)
                if isf:
                    pixmap=QtGui.QPixmap()
                    pixmap.load(conceptPath+'\\'+i)
                    pixlab=clickLabel()
                    pixlab.setFixedWidth(120)
                    pixlab.setFixedHeight(120)
                    pixlab.setPixmap(pixmap.scaledToWidth(120))
                    pixlab.setToolTip(conceptPath+'\\'+i)
                    #pixlab.linkActivated.connect(self.openPic)
                    pixmapArray.append(pixlab)
        row=0         
        for count,i in enumerate(pixmapArray):
            colum=count%3
            row=count/3
            self.conceptHbox.addWidget(i,row,colum)
            
            
        
        self.conceptHbox.setRowStretch(row+1,1)
        pass
        
    def loadNoteListData(self):
        colorArray=[
        [12,112,143],
        [151,56,84],
        [79,70,136],
        [134,83,70],
        [44,85,110],
        [140,43,100],
        [89,128,70],
        [155,141,63],
        [68,137,114],
        [149,85,43]
        
        ]
        #every value plus 100 is original color
        self.comLE.clear()
        itemNode=''
        if self.treeWid.currentItem ().parent():
            itemNode=self.treeWid.currentItem ().parent()
        else:
            itemNode=self.treeWid.currentItem ()

        noteDir=self.serverPath+'\\asset\\RIG\\'+self.nowTreePage+'\\'+itemNode.text(0)+'\\note'
        if os.path.exists(noteDir):
            folders=os.listdir(noteDir)
            count=0
            for f in folders:
                cn=count%10
                pngs=[]
                toolTipPath=''
                files=os.listdir(noteDir+'\\'+f)
                for fi in files:
                    if '.json' in fi:
                        toolTipPath=noteDir+'\\'+f+'\\'+fi
                    if '.png' in fi:
                        pngs.append(noteDir+'\\'+f+'\\'+fi)
                iconPath=''
                if pngs:
                    iconPath=pngs[0]
                else:
                    iconPath=self.initPath+'\\icon\\lifeStyle18.png'
                icn=QtGui.QIcon(iconPath)
                
                toolTip='no pre common in path'
                if toolTipPath:
                    with open(toolTipPath,"rt") as file:
                        toolTip=file.read().decode('utf-8')
    
                linearGradient=QtGui.QLinearGradient(60, 50, 200, 200)
                linearGradient.setColorAt(0, Qt.transparent)
                linearGradient.setColorAt(0.79, Qt.transparent)
                linearGradient.setColorAt(0.8, QtGui.QColor(200,200,200))
                linearGradient.setColorAt(0.84, QtGui.QColor(200,200,200))
                linearGradient.setColorAt(0.85, QtGui.QColor(colorArray[cn][0],colorArray[cn][1],colorArray[cn][2]));
                linearGradient.setColorAt(1.0, QtGui.QColor(colorArray[cn][0],colorArray[cn][1],colorArray[cn][2]));
                
                regf='{}-{}-{} {}:{}:{}'.format(f[0:4],f[4:6],f[6:8],f[8:10],f[10:12],f[12:14])
                regf+=' | '+toolTip[:100]
                itm=QtGui.QListWidgetItem()
                itm.setText(regf)
                itm.setSizeHint(QtCore.QSize(225,48))
                itm.setIcon(icn)
                itm.setToolTip(f)
                itm.setBackground(QtGui.QBrush(linearGradient))
                self.comLE.addItem(itm)
                count+=1
                #dir(QtGui.QListWidgetItem)
            #QListWidgetItem 
        pass
    def clearLayout(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()   
        pass
        
    def treeWidChangedFn(self):
        changeTabItm=''
        sender=self.sender()
        itm=sender.currentItem()
        if itm:
            if itm.parent():
                changeTabItm=itm.parent()
            else:
                changeTabItm=itm
    
            if self.isTab:
                nowTab = self.tabWid.currentIndex()
                if nowTab==0:
                    self.loadGeneralPageData(changeTabItm)
                if nowTab==1:
                    self.loadNoteListData()
                if nowTab==2:
                    self.loadHTMLHistoryData(changeTabItm)
                if nowTab==3:
                    self.loadConceptPictureData(changeTabItm)
            '''
            if self.isPicture:
                filePath=self.serverPath+'\\asset\\RIG\\'+self.nowTreePage+'\\'+changeTabItm.text(0)+'\\'
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
                
            '''
        pass
        
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
        
    def HTML_CreateEmptyStyle(self,historyPath):
        style=(
            '<style type="text/css">  \n' 
            '.iconPicL{position: relative;margin-left: 25px;float: left;} \n'
            '.iconPicR{position: relative;margin-right: 25px;float: right;} \n'
            '.timeDiv{font-family:Verdana;color:white;height:10px;text-align:center;margin:0 auto}   \n' 
            '.bubbleDiv{width: 100%;  margin: 0;  border: 0px solid #4a4f58;  }  \n'    
            '.bubbleItem{word-break:break-all;font-family:microsoft YaHei;font-size:15px;width: 100%;}  \n'    
            '.bubble{max-width: 260px;position: relative;line-height: 20px;padding-left: 10px;padding-top: 0px;padding-bottom: 0px;border-radius: 7px;margin-top: 0px;padding-right: 10px;display: inline-block;} \n'     
            '.leftBubble{position: relative;margin-left: 25px;border: 1px solid #00b6b6;background-color: #f8fdfc;}   \n'   
            '.leftBubble .bottomLevel{position: absolute;top: 5px;left: -10px;border-top: 10px solid #00b6b6;border-left: 10px solid transparent;}     \n' 
            '.leftBubble .topLevel{position: absolute;top: 6px;left: -8px;border-top: 10px solid #f8fdfc;border-left: 10px solid transparent;z-index: 100;  }   \n'   
            '.rightBubble{position: relative;margin-right: 25px;float: right;border: 1px solid #aaa;background-color: #f8fdfc;}    \n'  
            '.rightBubble .bottomLevel{position: absolute;bottom: 6px;right: -10px;border-bottom: 10px solid #aaa;border-right: 10px solid transparent;}  \n'    
            '.rightBubble .topLevel{position: absolute;bottom: 7px;right: -8px;border-bottom: 10px solid #fff;border-right: 10px solid transparent;z-index: 100;}   \n'   
            '.clearfix:after {visibility: hidden;display: block;font-size: 0;content: " ";clear: both;height: 0;  } \n'        
            'img{max-width:300px;margin:5px 0;}\n'
            '</style>\n'
            '<div class="bubbleDiv">\n'
            '</div>\n'
            )
        reportnew = open(historyPath, 'w')  
        reportnew.write(style)  
        reportnew.close() 
        return style
    
    
    
    def HTML_addMsg(self,htmlpath,message):
        #htmlPath is this type of data.
        #r'Z:\project\pig\asset\PRODUCE\Char\monkeyking\history.html' 
        #self.historyPath=htmlpath
        if not os.path.exists(htmlpath):
            self.HTML_CreateEmptyStyle()
            
        htmlFile = open(htmlpath,'r')
        line = []  
        for i in htmlFile.readlines():  
            line.append(i)
        htmlFile.close()
        
        line.insert(-1,message)
        
        s = ''.join(line)  
        reportnew = open(htmlpath, 'w')  
        reportnew.write(s)  
        reportnew.close() 
        
    def HTML_createMsg(self,contect,user,pictures,side=1,initPath='D:\\figo_tool_box'): 
        pic='' 
        if pictures:
            #pictures is a array type data like ['D:\\xxx\\xxx\xxx.png','D:\\xxx\\xxx\xxx.png']
            if len(pictures)>=3:
                for p in pictures[:3]:
                    pic+='<img src=\"{}\" width=\"100\" height=\"100\" />'.format(p)
            else:
                for p in pictures:
                    pic+='<img src=\"{}\" width=\"100\" height=\"100\" />'.format(p)
                
        sentionsA=''
        sentionsB=''
        
        
        avarterArray=os.listdir(initPath+'\\icon\\avarter')
        countstr=''
        for i in user:
            countstr+=str(ord(i))
        
        random.seed(int(countstr))
        usePic=initPath+'\\icon\\avarter\\'+avarterArray[int(random.random()*len(avarterArray))]
        
        if side>0:
            sentionsA='<div class="bubbleItem clearfix"> <p><div class=timeDiv>'
            sentionsB='</div></p> <div><img class=iconPicR src="'+usePic+'" width="50" height="50" /></div>  <span class="bubble rightBubble"><strong>['
        elif side<0:
            sentionsA='<div class="bubbleItem"> <p><div class=timeDiv>'
            sentionsB='</div></p>  <div><img class=iconPicL src="'+usePic+'" width="50" height="50" /></div> <span class="bubble leftBubble"><strong>['
        else:
            sentionsA='<div class="bubbleItem"> <p><div class=timeDiv>'
            sentionsB='</div></p>   <span class="bubble leftBubble"><strong>['   
                
                
        message=sentionsA
        message+=QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        message+=sentionsB
        message+=user
        message+=']:</strong><br>'
        message+=contect
        message+='<br>'
        message+=pic
        message+='<span class="bottomLevel"></span>  <span class="topLevel"></span>  </span>  </div> \n'
        return message
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
        '''
        if self.isPicture:
            self.mPixmap=self.mPixmap.scaledToWidth(self.widgetWidth)
            self.labPic.setPixmap(self.mPixmap)
            self.labPic.resize(self.mPixmap.width(),self.mPixmap.height())
            self.scroll.resize(self.widgetWidth,self.widgetWidth*0.57)
            self.L2=self.scroll.height()+25
        else:
            self.L2=25
        '''
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
        pass
        '''
        if self.isPicture:
            self.mPixmap.load(self.nowPicPath)
            self.mPixmap=self.mPixmap.scaledToWidth(self.widgetWidth)  
            self.labPic.setPixmap(self.mPixmap)  
            pass
        '''
        
        
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






