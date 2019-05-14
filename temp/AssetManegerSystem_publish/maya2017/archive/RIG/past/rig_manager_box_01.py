import sys,os,time,json,shutil,random
import pathConfig
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
    
    
    
class dragToolListWidget(QtGui.QListWidget):
    mainSize=0
    onPress=False
    iArray=[]
    isDrag=False
    def __init__(self,parent = None):  
        super(dragToolListWidget,self).__init__(parent) 
    
        self.createContextMenu()    
    def wheelEvent(self, e):
        if self.onPress:
            nowSt = self.styleSheet()
            tempsp=nowSt.split(';')
            for n in tempsp:
                if 'font-size:' in n:
                    nsp=n.split(':')
                    self.mainSize=int(nsp[1][0:-2])
                    self.mainSize=self.mainSize+(e.delta()/120 )
       
            self.setStyleSheet(Mstyle.ListWidgetStyle(fontSize=str(self.mainSize)+'px',bordRad='0px'))
            self.setIconSize(QtCore.QSize(self.mainSize*2,self.mainSize*2))
            
            
            if self.count() != len(self.iArray):
                self.iArray=[]
                for i in range(self.count()):
                    self.iArray.append(self.item(i))
            
            for i in self.iArray:
                i.setSizeHint (QtCore.QSize(self.mainSize*2,self.mainSize*2))

        super(dragToolListWidget, self).wheelEvent(e)

    def mouseMoveEvent(self, e): 
        if e.buttons() != QtCore.Qt.LeftButton:
            return;
        
        if not self.isDrag:
            return;
        #print 'in event'  
        initPath=getScriptPath()  
        cNode=self.currentItem()
        path=initPath+'\\pulg_ins\\'+cNode.pageName+'\\'+cNode.fileName
        #print path
        mimeData = QtCore.QMimeData();
        url=QtCore.QUrl.fromLocalFile(QtCore.QFileInfo(path).absoluteFilePath());
        mimeData.setUrls([url])
        self.drag = QtGui.QDrag(self);
        self.drag.setMimeData(mimeData);
        self.drag.setHotSpot(e.pos() - self.rect().topLeft());
        self.drag.exec_(Qt.CopyAction);
        e.accept(); 


   
    def  keyPressEvent(self,e):
        if e.key()==QtCore.Qt.Key_Control:
            self.onPress=True
            
    def keyReleaseEvent(self,e):
        self.onPress=False
        
    def mouseDoubleClickEvent(self,e): 
        initPath=getScriptPath()
        cNode=self.currentItem()
        fullUrl=initPath+'\\pulg_ins\\'+cNode.pageName+'\\'+cNode.fileName
        self.runCommand(p=fullUrl)


    def runCommand(self,p=''):
        theUrl=''
        if p!='':
            theUrl=p
        else:
            initPath=getScriptPath()
            theUrl=initPath+'\\pulg_ins\\'+self.pageName+'\\'+self.fileName

        check=theUrl.split('.')[-1]
        if check=='py' or check=='pyc':
            execfile(theUrl)
        if check=='txt':
            os.startfile(theUrl)
            #os.system('notepad '+theUrl)
        if check=='mel':
            melcommand='source "'+theUrl+'"'
            units=melcommand.split('\\')
            melcommand='/'.join(units)
            #print melcommand
            mel.eval(melcommand)   
        if check=='ma':
            result = cmds.confirmDialog(
            		title='Open File',
            		message='Do you wanna open file?',
            		button=['OK', 'Cancel'],
            		defaultButton='OK',
            		cancelButton='Cancel',
            		dismissString='Cancel')

            if result == 'OK':
            	print 'openFile'
            	
            	
    def createContextMenu(self):      
        self.setContextMenuPolicy(Qt.CustomContextMenu)    
        self.customContextMenuRequested.connect(self.showContextMenu)  
        #print Mstyle.MenuStyle() 
        
        iniPath=getScriptPath()
        iconPath=iniPath+'\\icon\\'
        self.contextMenu = QtGui.QMenu(self) 
        self.contextMenu.setStyleSheet(Mstyle.MenuStyle())   
        actionA = self.contextMenu.addAction(QtGui.QIcon(iconPath+"more.png"),u'run')    
        self.actionB = self.contextMenu.addAction(QtGui.QIcon(iconPath+"more.png"),u'open')    
        self.actionC = self.contextMenu.addAction(QtGui.QIcon(iconPath+"more.png"),u'history')   
        #add sub menu
        self.second = self.contextMenu.addMenu(QtGui.QIcon(iconPath+"floder.png"),u"more")   
        #self.second.setMask(mask)
        self.actionD = self.second.addAction(QtGui.QIcon(iconPath+"more.png"),u'actionA')  
        self.actionE = self.second.addAction(QtGui.QIcon(iconPath+"more.png"),u'actionB') 
        self.actionF = self.second.addAction(QtGui.QIcon(iconPath+"more.png"),u'actionC')  
        self.actionF = self.second.addAction(QtGui.QIcon(iconPath+"more.png"),u'actionD')  
        
        actionA.triggered.connect(self.actionAFn)
        
    def showContextMenu(self, pos):    
        self.contextMenu.exec_(QtGui.QCursor.pos()) #show menu on cursor pos        	
    def actionAFn(self):
        initPath=getScriptPath()
        cNode=self.currentItem()
        fullUrl=initPath+'\\pulg_ins\\'+cNode.pageName+'\\'+cNode.fileName
        self.runCommand(p=fullUrl)   
        
        

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
    pixmapPath='D:/test.png'
    L2=0
    isPicture=False
    isTree=False
    isTab=True
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
        
        self.createTitleBar()
        self.createPicture()
        self.createSplitter()

        #mImage=QtGui.QImage()
        #mImage.load("D:/test.png");
        
        #mPainter=QtGui.QPainter(self)
    def createSplitter(self):

        self.splitter = QtGui.QSplitter(self)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.splitter.setGeometry(0,self.L2,0,0)
        self.splitter.resize(self.widgetWidth,self.widgetWidth*0.6)
        if self.isTree:
            tree=self.createTree()
            tree.setParent(self.splitter)
        if self.isTab:
            self.createTab()
            self.tabWid.setParent(self.splitter)

        
    def createTab(self):
        self.tabWid=QtGui.QTabWidget()
        self.tabWid.setMinimumWidth(self.widgetWidth*0.1)
        self.tabWid.setMinimumHeight(self.widgetWidth*0.6)
        
        processWid=QtGui.QWidget()
        pwVB=QtGui.QVBoxLayout()
        
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
          
        hisWid=QtGui.QWidget()
        self.tabWid.addTab(hisWid,'history')

                 
        if self.shMn1act.isChecked():
            wid=QtGui.QWidget()
            self.tabWid.addTab(wid,'concept')
        
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

        
        submitBtn.pressed.connect(self.submitBtnFn)
        
        
    def createTree(self):

        self.vWid=QtGui.QWidget()
        self.vWid.setMinimumWidth(self.widgetWidth*0.1)
        self.vWid.resize(self.widgetWidth*0.5,self.widgetWidth-self.L2)

        vBox=QtGui.QVBoxLayout()
        vBox.setSpacing(0)
        vBox.setContentsMargins(0,0,0,0)
        
        
        LE=QtGui.QLineEdit()
        vBox.addWidget(LE)
        
        
        self.treeWid=QtGui.QTreeWidget()
        self.treeWid.setHeaderHidden(1)
        
        sPath=r'D:\data\temp\Rigging'
        folders=self.getFolders(path=sPath)
        defaultSize=QtCore.QSize(18,18)
        for f in folders:
            itm=QtGui.QTreeWidgetItem()
            itm.setText(0,f)
            itm.setSizeHint(0,defaultSize)
            files=self.getFiles(sPath+'\\'+f)
            for fl in files:
                citm=QtGui.QTreeWidgetItem()
                citm.setText(0,fl)
                citm.setSizeHint(0,defaultSize)
                itm.addChild(citm)
            self.treeWid.addTopLevelItem (itm)
        
        vBox.addWidget(self.treeWid)
        self.vWid.setLayout(vBox)
        self.treeWid.currentItemChanged.connect(self.treeWidChangedFn)
        return self.vWid

      
    def createPicture(self):
        if self.isPicture==True:
            self.mPixmap=QtGui.QPixmap()
            self.mPixmap.load(self.pixmapPath)
            self.mPixmap=self.mPixmap.scaledToWidth(self.widgetWidth)
    
            self.labPic=QtGui.QLabel('',self)
            self.labPic.setPixmap(self.mPixmap)
            self.labPic.setMinimumWidth(self.widgetWidth)
            self.labPic.setGeometry(0,25,0,self.mPixmap.height())
            self.L2=self.mPixmap.height()+25
        else:
            self.L2=25
            
           
    def createTitleBar(self):
        qmb=QtGui.QMenuBar(self)
        
        fileMn=QtGui.QMenu('Login',qmb)
        qmb.addMenu(fileMn)
        fileMn1act = fileMn.addAction('log - In')
        fileMn2act = fileMn.addAction('log - Out')
        fileMn.addSeparator()#--------------------

        
        shMn=QtGui.QMenu('File-Link',qmb)
        qmb.addMenu(shMn)
        self.shMn1act=QtGui.QAction("Concept", shMn, checkable=True)
        self.shMn1act.setChecked(True)
        shMn.addAction(self.shMn1act)
        self.shMn2act = QtGui.QAction("Model", shMn, checkable=True)
        self.shMn2act.setChecked(True)
        shMn.addAction(self.shMn2act)
        shMn.addSeparator()

        toolMn=QtGui.QMenu('Tool',qmb)
        qmb.addMenu(toolMn)
        tool1act = toolMn.addAction("Tool1")
        tool2act = toolMn.addAction("Tool2")
        

        aboutMn=QtGui.QMenu('About',qmb)
        qmb.addMenu(aboutMn)
        about1act = aboutMn.addAction("about author")
        about2act = aboutMn.addAction("how to use")
        
        
    def submitBtnFn(self):
        cItm = self.treeWid.currentItem()
        if cItm:
            ctime = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) 
            rp = 'D:\\data\\temp\\Rigging\\'+cItm.text(0)+'\\process\\'+ctime+'\\'
            paEx = os.path.exists(rp)
            if not paEx:
                os.makedirs(rp)
                pass
            cmds.file(rename=rp+'PIG_cha_'+cItm.text(0)+'_rig_low.ma')
            cmds.file(save=1)
            
    def treeWidChangedFn(self):
        sender=self.sender()
        itm=sender.currentItem()
        if itm.parent():
            itm=itm.parent()
            
         
        self.pTree.clear()
        rP='D:\\data\\temp\\Rigging\\'+itm.text(0)+'\\process\\'
        paEx = os.path.exists(rP)
        if paEx:
            fs=self.getFolders(path=rP)

            
            for f in fs:
                itm=QtGui.QTreeWidgetItem()
                print 
                itm.setText(0,(f[0:4]+'-'+f[4:6]+'-'+f[6:8]+' '+f[8:10]+':'+f[10:12]+':'+f[-2:]))
                self.pTree.addTopLevelItem (itm)
                fl=self.getFiles(path=rP+f)
                print fl

         


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
            
 
    #-------------------- ui functions -------------
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
                  
    def refreshListHeight(self):
        
        dockSize=self.size()
        self.widgetHeight=dockSize.height()-5
        self.widgetWidth=dockSize.width()
        if self.isPicture:
            self.mPixmap=self.mPixmap.scaledToWidth(self.widgetWidth)
    
            self.labPic.setPixmap(self.mPixmap)
            self.labPic.resize(self.mPixmap.width(),self.mPixmap.height())
            
            self.L2=self.mPixmap.height()+25
        else:
            self.L2=25
        
        self.splitter.setGeometry(0,self.L2,0,0)
        self.splitter.setMinimumWidth(self.widgetWidth)
        self.splitter.setMinimumHeight(self.widgetHeight-self.L2)

    #------ button functions ------------------------------

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
        self.refreshListHeight()
        
        pass
        
    def dragEnterEvent(self,e):
        if(e.mimeData().hasFormat("text/uri-list")):
            e.acceptProposedAction() 
            
    def mousePressEvent(self,e):  
        if (e.button() == Qt.LeftButton):
            pass
            #drag = QtGui.QDrag(self)  
            #data = QtGui.QMimeData
            #e.setMimeData(data)
            #e.exec(Qt.MoveAction)
    def mouseReleaseEvent(self,e):  
        if self.isPicture:
            self.mPixmap.load(self.pixmapPath)
            self.mPixmap=self.mPixmap.scaledToWidth(self.widgetWidth)  
            self.labPic.setPixmap(self.mPixmap)  
            pass
        
        
        
    def dropEvent(self,e):
        if not self.searchBtn2.isChecked:
            return
        urls = e.mimeData().urls()
        if len(urls)==0:
            return

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

  
    def closeEvent(self,e):
        self.deleteLater()
        
    #------------widget enter--------------      
    def Op_Ui(self):
        self.show()
        self.setDockableParameters(dockable=True,floating=False,area='left')
        self.raise_()

            
RigManaBUI=RigManagerBoxUI()
RigManaBUI.Op_Ui()






