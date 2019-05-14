import sys,os,time,json,shutil,random
path='D://rig_manager_box'
if not path  in sys.path:sys.path.append(path)
import rig_manager_box_pathConfig as pathConfig
import maya.cmds as cmds
import maya.OpenMayaUI as OpenMayaUI
from shiboken import wrapInstance
from PySide import QtGui, QtCore
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
from PySide import QtCore,QtGui
from PySide.QtCore import Qt
from data.redBlackStyleSheet07 import RedBlackStyleSheet
from PySide.QtCore import Qt, QRect  
Mstyle=RedBlackStyleSheet()



        
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
    
#dir(dragToolListWidget)   
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
        pathSet=self.initPath+'\\data\\path.json'
        pathDict=self.loadJson(pathSet)
        self.localPath=pathDict['local']
        self.serverPath=pathDict['server']
        
        #loadServerConfig
        
        
        #loadLocalConfig

            
           
    def createTitleBar(self):
        qmb=QtGui.QMenuBar(self)
        
        fileMn=QtGui.QMenu('Login',qmb)
        qmb.addMenu(fileMn)
        fileMn1act = fileMn.addAction('login')
        fileMn2act = fileMn.addAction('regist')
        fileMn3act = fileMn.addAction('exit')
        #fileMn.setTitle('ggg')
        fileMn.addSeparator()#--------------------
        #dir(QtGui.QAction)
        
        shMn=QtGui.QMenu('Layout',qmb)
        qmb.addMenu(shMn)
        self.shMn1act=QtGui.QAction("Picture", shMn, checkable=True)
        self.shMn1act.setChecked(True)
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
        fileMn2act.triggered.connect(self.registFn)
        fileMn3act.triggered.connect(self.exitFn)
        #layoutMn=QtGui.QMenu('Layout',qmb)

    def loginFn(self):
        sender=self.sender()
        print sender.text()
        print (sender.parent().title())

    def registFn(self):
        sender=self.sender()
        print sender.text()
        print (sender.parent().title())

    def exitFn(self):
        sender=self.sender()
        print sender.text()
        print (sender.parent().title())
        
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
        lab1=QtGui.QLabel('name : ',msgWid)
        msgVB.addWidget(lab1)
        
        lab2=QtGui.QLabel('high time : ',msgWid)
        msgVB.addWidget(lab2)
        
        lab3=QtGui.QLabel('low time : ',msgWid)
        msgVB.addWidget(lab3)
        
        lab4=QtGui.QLabel('artist : ',msgWid)
        msgVB.addWidget(lab4)
        
        lab5=QtGui.QLabel('state : ',msgWid)
        msgVB.addWidget(lab5)
        
        lab6=QtGui.QLabel('others : ',msgWid)
        msgVB.addWidget(lab6)
        
        msgVB.addStretch  (1)
        
        msgWid.setLayout(msgVB)
        
        self.tabWid.addTab(msgWid,'general')
        #---page1----
        processWid=QtGui.QWidget()
        processWid.setAttribute(Qt.WA_StyledBackground)
        #processWid.setStyleSheet('QWidget{background:rgb(255,0,0)}')
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
        
        self.tabWid.addTab(processWid,'process')
        #---page1 end----
        
        #---page2----
        hisWid=QtGui.QWidget()
        self.tabWid.addTab(hisWid,'history')

        #---page2 end----  
        
        #---page3----
        if self.shMn1act.isChecked():
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
        
        submitBtn.pressed.connect(self.submitBtnFn)
        self.pTree.currentItemChanged .connect(self.pTreeChangeFn)
        
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
        print sender.currentItem().text(0)

        if state:
            self.isTab=True
            self.tabWid.setVisible(True)
        else:
            self.isTab=False
            self.tabWid.setVisible(False)
        
    def pTreeChangeFn(self):
        sender=self.sender()
        print sender.currentItem().text(0)
         
    def submitBtnFn(self):
        cItm = self.treeWid.currentItem()
        if cItm:
            ctime = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) 
            
            rp = self.serverPath+'\\'+cItm.text(0)+'\\process\\submit_'+ctime+'_'+ctime+'\\'
            paEx = os.path.exists(rp)
            if not paEx:
                os.makedirs(rp)
                pass
            cmds.file(rename=rp+'PIG_cha_'+cItm.text(0)+'_rig_low.ma')
            cmds.file(save=1)
            
            
            
    def treeWidChangedFn(self):
        changeTabItm=''
        sender=self.sender()
        itm=sender.currentItem()
        if itm.parent():
            changeTabItm=itm.parent()
        else:
            changeTabItm=itm

        if self.isTab:
            self.pTree.clear()
            rP=self.serverPath+'\\'+itm.text(0)+'\\process\\'
            paEx = os.path.exists(rP)
            if paEx:
                fs=self.getFolders(path=rP)
                for f in fs:
                    fl=self.getFiles(path=rP+f)
                    itm=QtGui.QTreeWidgetItem()
                    spf=f.split('_')
                    f=spf[1]
                    itm.setText(0,(spf[0]+' : '+f[0:4]+'-'+f[4:6]+'-'+f[6:8]+' '+f[8:10]+':'+f[10:12]+':'+f[-2:]))
                    self.pTree.addTopLevelItem (itm)
                    
                    for lf in fl:
                        subitm=QtGui.QTreeWidgetItem()
                        subitm.setText(0,lf)
                        itm.addChild(subitm)
                    
                    
                    
                    
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
        #setHidden
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






