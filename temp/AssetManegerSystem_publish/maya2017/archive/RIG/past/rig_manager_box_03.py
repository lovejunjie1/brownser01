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



def copytree(src, dst, symlinks=False):
    names = os.listdir(src)
    if not os.path.isdir(dst):
        os.makedirs(dst)
          
    errors = []
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                shutil.copytree(srcname, dstname, symlinks)
            else:
                if os.path.isdir(dstname):
                    os.rmdir(dstname)
                elif os.path.isfile(dstname):
                    os.remove(dstname)
                shutil.copy2(srcname, dstname)
            # XXX What about devices, sockets etc.?
        except (IOError, os.error) as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except OSError as err:
            errors.extend(err.args[0])
    try:
        shutil.copystat(src, dst)
    except WindowsError:
        # can't copy file access times on Windows
        pass
    except OSError as why:
        errors.extend((src, dst, str(why)))
    if errors:
        raise shutil.Error(errors) 
        
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
    isTab=False
    localPath=''
    serverPath=''
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
        self.loadConfig()
        
        self.createTitleBar()
        self.createPicture()
        self.createSplitter()

    def loadConfig(self):

        pathSet=self.initPath+'\\data\\path.json'

        pathDict=self.loadJson(pathSet)
        self.localPath=pathDict['local']
        self.serverPath=pathDict['server']


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
        allowArray=['ma']
        self.vWid=QtGui.QWidget()
        self.vWid.setMinimumWidth(self.widgetWidth*0.1)
        self.vWid.resize(self.widgetWidth*0.5,self.widgetWidth-self.L2)

        vBox=QtGui.QVBoxLayout()
        vBox.setSpacing(0)
        vBox.setContentsMargins(0,0,0,0)
        
        
        LE=QtGui.QLineEdit()
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


    def LEtextChangedFn(self):
        sender=self.sender()
        nowTxt = sender.text()
        #print self.treeWid.
        
        
        '''
        Idx=self.QTwidget.currentIndex()
        pageN = self.QTwidget.tabText(Idx)
        #dNode=self.UIitems[pageN]
        cwd=self.QTwidget.widget(Idx)
        pageType = cwd.statusTip()
        if '_list' in pageType:
            itemArray=[]
            for i in range(self.list.count()):
                itemArray.append(self.list.item(i))
            for d in itemArray:
                if self.LE.text().lower() in d.fileName.lower():
                    d.setHidden (0)
                else:
                    d.setHidden (1)
        elif '_block' in pageType:
            dTemp=cwd.children()
            dNode=[]
            for d in dTemp:
                if type(d)==dragToolButton:
                    dNode.append(d)
            for d in dNode:
                if self.LE.text().lower() in d.fileName.lower():
                    d.show()
                else:
                    d.hide()
            
            if self.LE.text()=='':
                for i in dNode:
                    i.show()  
        '''

 
    def createPicture(self):
        if self.isPicture==True:
            self.mPixmap=QtGui.QPixmap()
            self.mPixmap.load('d:/test.png')
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
            
            rp = self.serverPath+'\\'+cItm.text(0)+'\\process\\'+ctime+'\\'
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
            
        if self.isTab:
            self.pTree.clear()
            rP=self.serverPath+'\\'+itm.text(0)+'\\process\\'
            paEx = os.path.exists(rP)
            if paEx:
                fs=self.getFolders(path=rP)
                for f in fs:
                    itm=QtGui.QTreeWidgetItem()
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
        if not self.isTab:
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






