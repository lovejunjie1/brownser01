#Qt_renderElement
import maya.cmds as cmds
from PySide import QtCore,QtGui
from PySide.QtCore import Qt
import maya.mel as mel
#import sys
#sys.path.append('D:/figo')
from redBlackStyleSheet05 import RedBlackStyleSheet as Mstyle

class renderSetTool():
    IDNumber=1
    MatNumber=1
    oData=[
    '-----basic-----',
    'castsShadows',
    'receiveShadows',
    'motionBlur',
    'primaryVisibility',
    'smoothShading',
    'visibleInReflections',
    'visibleInRefractions',
    '-----vray-----',
    'vray_subdivision',
    'vray_subquality',
    'vray_displacement',
    'vray_opensubdiv',
    'vray_roundedges',
    'vray_objectID',
    'vray_user_attributes'
    ]
    secOne=[]
    secTwo=[]
    def __init__(self):
        breakOne=False
        breakTwo=False
        
        for i in self.oData:
            if i=='-----vray-----':
                breakOne=False
                breakTwo=True
                
            if i=='-----basic-----':
                breakOne=True
                
            if breakOne:
                self.secOne.append(i)
                
            if breakTwo:
                self.secTwo.append(i)
        self.secOne.remove('-----basic-----')
        self.secTwo.remove('-----vray-----')
        
    def closeOption(self,arrayOption):
        oprObj=cmds.ls(sl=1, dag=1, lf=1,s=1)
        if oprObj:
            for oprOption in arrayOption:
                if oprOption in self.secOne:
                    for i in oprObj:
                        cmds.setAttr(i+'.'+oprOption,0)
                    self.showMessage(('close '+oprOption))
                    print(('close '+oprOption))  
                if oprOption in self.secTwo:
                    for i in oprObj:
                        cmds.vray("addAttributesFromGroup", i, oprOption, 0)
                    self.showMessage(('remove '+oprOption))
                    print(('remove '+oprOption))  
        else:
            self.showMessage('nothing was selected')
            print 'nothing was selected'
            
            
    def openOption(self,arrayOption):
        oprObj=cmds.ls(sl=1, dag=1, lf=1,s=1)
        if oprObj:
            for oprOption in arrayOption:
                if oprOption in self.secOne:
                    for i in oprObj:
                        cmds.setAttr(i+'.'+oprOption,1)
                    self.showMessage(('open '+oprOption))  
                    print(('open '+oprOption))  
                if oprOption in self.secTwo:
                    for i in oprObj:
                        cmds.vray("addAttributesFromGroup", i, oprOption, 1) 
                    self.showMessage(('add '+oprOption))  
                    print(('add '+oprOption))   
        else:
            self.showMessage('nothing was selected')
            print 'nothing was selected'
            
            
            
    def Create_ID(self):
        selection = cmds.ls(sl=1,dag=1,lf=1,s=1)
        
        checkNumber=self.IDNumber
        isExist=0
        FoundProperty=''
        getObjID=cmds.ls(type='VRayObjectProperties')
        for go in getObjID:
            checkVal=cmds.getAttr('%s.objectID' % go)
            
            if checkVal is checkNumber:
                isExist=1
                FoundProperty=go
        #check number exist
        if isExist:
            isContinue=cmds.confirmDialog( title='NumberExist', 
            message='Number is Exist,Do ya wanna Merge?', 
            button=['Yes','Merge','No'], 
            defaultButton='No', 
            cancelButton='No', 
            dismissString='No' )
            #print (isContinue)
            if isContinue == 'No':
                self.showMessage("cancel defined ID")   
                return False
                
            if isContinue == 'Merge':
                cmds.sets(selection,include=FoundProperty)
                
                self.showMessage(('merge ObjectID: '+str(self.IDNumber)))
                
                print ("merge ObjectID: " + str(self.IDNumber)) 
                 
                self.IDNumber = self.IDNumber + 1
                
                return self.IDNumber

        cmds.select(selection)
        selection = mel.eval('vray objectProperties add_single')
        #add vrayobjectproperties node
        
        sel=cmds.ls(sl=1)
        VP=cmds.listConnections(sel[0],type='VRayObjectProperties')
        if VP:
            cmds.setAttr(  (VP[0] + ".objectIDEnabled"),1)
            cmds.setAttr(  (VP[0] + ".objectID"),self.IDNumber)
                    
            cmds.rename (VP[0],("vrayobjectproperties_ID" + str(self.IDNumber)))
        
            if (cmds.objExists("ObjectID_temp_layer")!= 1):
                cmds.createDisplayLayer(name="ObjectID_temp_layer",number=1,nr=1)
                
            cmds.editDisplayLayerMembers('ObjectID_temp_layer',sel,noRecurse=1)
            
            self.showMessage(('Create ObjectID: ' + str(self.IDNumber)))   
            
            print ("Create ObjectID: " + str(self.IDNumber))  
            
            self.IDNumber = self.IDNumber + 1
            return self.IDNumber
        else:
            print 'Fail'
            return self.IDNumber
            
            
    def Remove_objectID(self):
        sel=cmds.ls(sl=1,dag=1,lf=1)
        if sel:
            for node in sel:
                mel.eval('vray objectProperties remove')
        self.showMessage(str(len(sel))+' of object was removed')
        
    def createObjectIDPass(self):
        
        IDarray=[]
        getObjID=cmds.ls(type='VRayObjectProperties')
        for go in getObjID:
            checkVal=cmds.getAttr('%s.objectID' % go)
            IDarray.append(checkVal)  
        IDarray.sort() 
        OprArray=self.simplifyArray(IDarray)
        #print OprArray
        #get the min val and max val for objID
        
        for itm in OprArray:
            ID=itm[0]
            ID_plusOne=itm[1]
            ID_plusTwo=itm[2]
            
            newPass=mel.eval('vrayAddRenderElement MultiMatteElement')
            cmds.setAttr((newPass+'.vray_name_multimatte'),("objectID_ID"+str(ID)+"_ID"+str(ID_plusTwo)),type='string')
            cmds.setAttr((newPass+'.vray_redid_multimatte'),ID)
            cmds.setAttr((newPass+'.vray_greenid_multimatte'),ID_plusOne)
            cmds.setAttr((newPass+'.vray_blueid_multimatte'),ID_plusTwo)
            cmds.rename(newPass,("objectID_ID"+str(ID)+"_ID"+str(ID_plusTwo)))
            self.showMessage(("objectID_ID"+str(ID)+"_ID"+str(ID_plusTwo)))
    
    def createMatID(self):
        setNumber=self.MatNumber
        
        tmat=cmds.ls(sl=1,materials=1)
        if 'particleCloud1' in tmat:
            tmat.remove('particleCloud1')
        for t in tmat:
            mel.eval('vray addAttributesFromGroup '+t+' vray_material_id 1')
            cmds.setAttr(t+'.vrayMaterialId',setNumber)
        self.showMessage(('Create MatID: ' + str(setNumber)))   
        print ("Create MatID: " + str(setNumber)) 
        self.MatNumber=self.MatNumber+1
        return self.MatNumber

    def createMtlIDPass(self):        
        matID=[]
        tmat=cmds.ls(materials=1)
        if 'particleCloud1' in tmat:
            tmat.remove('particleCloud1')       
        for t in tmat:
            isExist=cmds.objExists(t+'.vrayMaterialId')
            if isExist:
                getVal=cmds.getAttr(t+'.vrayMaterialId') 
                matID.append(getVal)   
        matID.sort()
        OprArray=self.simplifyArray(matID)
        #print matID
        
        for itm in OprArray:
            ID=itm[0]
            ID_plusOne=itm[1]
            ID_plusTwo=itm[2]
            
            newPass=mel.eval('vrayAddRenderElement MultiMatteElement')
            cmds.setAttr((newPass+'.vray_name_multimatte'),("MtlID_ID"+str(ID)+"_ID"+str(ID_plusTwo)),type='string')
            cmds.setAttr((newPass+'.vray_redid_multimatte'),ID)
            cmds.setAttr((newPass+'.vray_greenid_multimatte'),ID_plusOne)
            cmds.setAttr((newPass+'.vray_blueid_multimatte'),ID_plusTwo)
            cmds.setAttr((newPass+'.vray_usematid_multimatte'),1)
            cmds.rename(newPass,("MtlID_ID"+str(ID)+"_ID"+str(ID_plusTwo)))
            self.showMessage(("MtlID_ID"+str(ID)+"_ID"+str(ID_plusTwo)))
            
    def printState(self,arrayOption):
        transDict={
                'vray_subdivision':'vraySubdivEnable',
                'vray_subquality':'vrayOverrideGlobalSubQual',
                'vray_displacement':'vrayDisplacementType',
                'vray_opensubdiv':'vrayOsdSubdivEnable',
                'vray_roundedges':'vrayRoundEdges',
                'vray_objectID':'vrayObjectID',
                'vray_user_attributes':'vrayUserAttributes'
                }
        oprObj=cmds.ls(sl=1, dag=1, lf=1,s=1)
        if oprObj:
            for i in oprObj:
                print ('>>>> '+i+' <<<<')
                for oprOption in arrayOption:
                    if oprOption in self.secOne:
                        nowValue=cmds.getAttr(i+'.'+oprOption)
                        print (oprOption+': '+str(nowValue))
        
                    if oprOption in self.secTwo:
                        isExist=cmds.objExists(i+'.'+transDict[oprOption])
                        if isExist:
                            print((oprOption+': True'))  
                        else:
                            print((oprOption+': False'))  
                print ''
        else:
            self.showMessage('nothing was selected')
            print 'nothing was selected'
            
    def simplifyArray(self,tArray):
        uniqueArray=[]
        for t in tArray:
            if not(t in uniqueArray):
                uniqueArray.append(t)
        rArray=[]
        for i in range(1,100000,3):
            ip1=i+1
            ip2=i+2
            if (i in uniqueArray) or (ip1 in uniqueArray) or (ip2 in uniqueArray):
                rArray.append([i,ip1,ip2])
        return rArray
                  
    def showMessage(self,infomation):
        cmds.inViewMessage(assistMessage=infomation,fade=True,pos="topRight",bkc=0x00FF1111,a=0.3,fst=10000)
initRenderSetTool=renderSetTool()

class Render_Set_TOOL(QtGui.QWidget):
    origPosDict={}
    MainFunctionDict={}
    opreateVertsDialog=None
    copyPasteVertDict={}
    
    def __init__(self):

        #------Style Set----------------------------

        QtGui.QWidget.__init__(self)
        self.m_DragPosition=self.pos()
        
        self.resize(180,350)
        self.move(350,200)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setStyleSheet(Mstyle.mainWidgetStyle)
        
        #-----close Btn Set----------------                                                 
        Xbtn=QtGui.QPushButton('x',self)
        Xbtn.setGeometry(0,0,0,0)
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle)
        
        Xbtn.clicked.connect(self.Cl_Ui)
        
        #-----TitleLabel set-----------------------
        TitleLab=QtGui.QLabel('Render Element (Vray)',self)
        TitleLab.setGeometry(40,5,0,0)
        TitleLab.setFixedHeight(20)
        TitleLab.setFixedWidth(140)
        TitleLab.setStyleSheet(Mstyle.QLabelStyleA)

        
        #-------matte ID set------------
        
        FAwidth=150
        FALineA=20
        FALineB=45
        FALineC=70
        FALineD=75
        
        self.groupBoxA=QtGui.QGroupBox('Matte ID',self)
        self.groupBoxA.setGeometry(15,30,0,0)
        self.groupBoxA.setFixedHeight(110)
        self.groupBoxA.setFixedWidth(FAwidth)
        self.groupBoxA.setStyleSheet(Mstyle.QGroupBoxStyleA)
        
            #----radio Btn start----
        StateBasePosX = 10
        StateBasePosY = FALineA
        StateBtnSpace = 3
        
        #self.StateShrikHeight=15
        self.StateBaseHeight=16
           
        self.StateBaseWidth=75     
        self.StateShrikWidth=55
        
        self.StateBtnWd=self.StateBaseWidth-StateBtnSpace
        self.StateBtnShrkWd=self.StateShrikWidth-StateBtnSpace
        
        self.StateSectionA=[(StateBasePosX,StateBasePosY,0,0),
                            (StateBasePosX+self.StateBaseWidth,StateBasePosY,0,0)
                            ] 
                                   
        self.StateSectionB=[(StateBasePosX,StateBasePosY,0,0),
                            (StateBasePosX+self.StateShrikWidth,StateBasePosY,0,0)
                            ]  
                                  
        self.StateBtnA1=QtGui.QPushButton('obj',self.groupBoxA)
        self.StateBtnA1.setGeometry(self.StateSectionA[0][0],self.StateSectionA[0][1],0,0)
        self.StateBtnA1.setEnabled(True)
        self.StateBtnA1.setFixedHeight(self.StateBaseHeight)
        self.StateBtnA1.setFixedWidth(self.StateBtnWd)
        self.StateBtnA1.setStyleSheet(Mstyle.btnOnStyle)
        
        self.StateBtnA2=QtGui.QPushButton('mat',self.groupBoxA)
        self.StateBtnA2.setGeometry(self.StateSectionA[1][0],self.StateSectionA[1][1],0,0)
        self.StateBtnA2.setEnabled(True)
        self.StateBtnA2.setFixedHeight(self.StateBaseHeight)
        self.StateBtnA2.setFixedWidth(self.StateBtnShrkWd)
        self.StateBtnA2.setStyleSheet(Mstyle.btnOffStyle)
        
        self.StateBtnA1.clicked.connect(self.StateFunctionA1)
        self.StateBtnA2.clicked.connect(self.StateFunctionA2)
            #----radio Btn over----
        
        self.IDLab=QtGui.QLabel('number',self.groupBoxA)
        self.IDLab.setGeometry(10,FALineB,0,0)
        self.IDLab.setFixedHeight(20)
        self.IDLab.setFixedWidth(40)
        self.IDLab.setStyleSheet(Mstyle.QLabelStyleA)
                            
        self.IDlineEt=QtGui.QLineEdit(self.groupBoxA)
        self.IDlineEt.setGeometry(55,FALineB,0,0)
        self.IDlineEt.setText('1')
        self.IDlineEt.setTextMargins (0,0,15,0)
        self.IDlineEt.setAlignment(Qt.AlignRight)
        self.IDlineEt.setFixedHeight(20)
        self.IDlineEt.setFixedWidth(80)
        self.IDlineEt.setStyleSheet(Mstyle.QLineEditStyleB)

        self.BtnAdd=QtGui.QPushButton('+',self.groupBoxA)
        self.BtnAdd.setGeometry(5,FALineD,0,0)
        self.BtnAdd.setEnabled(True)
        self.BtnAdd.setFixedHeight(20)
        self.BtnAdd.setFixedWidth(FAwidth*0.25)
        self.BtnAdd.setStyleSheet(Mstyle.btnOnStyle)  
         
        self.BtnRemove=QtGui.QPushButton('-',self.groupBoxA)
        self.BtnRemove.setGeometry(5+FAwidth*0.25,FALineD,0,0)
        self.BtnRemove.setEnabled(True)
        self.BtnRemove.setFixedHeight(20)
        self.BtnRemove.setFixedWidth(FAwidth*0.25)
        self.BtnRemove.setStyleSheet(Mstyle.btnOnStyleB)   
        
        self.BtnPass=QtGui.QPushButton('Pass',self.groupBoxA)
        self.BtnPass.setGeometry(5+FAwidth*0.5,FALineD,0,0)
        self.BtnPass.setEnabled(True)
        self.BtnPass.setFixedHeight(20)
        self.BtnPass.setFixedWidth(FAwidth*0.4)
        self.BtnPass.setStyleSheet(Mstyle.btnOnStyle)   
        
 
        #------main btn set-----------------------
        Chlx=15
        Chly=130
        Chloffsety=20
        
        self.Chlheight=20
        self.ChlBtnWidth=150
        
        self.BtnA1=QtGui.QPushButton('+',self)
        self.BtnA1.setGeometry(Chlx,Chly+Chloffsety*8.5,0,0)
        self.BtnA1.setEnabled(True)
        self.BtnA1.setFixedHeight(self.Chlheight)
        self.BtnA1.setFixedWidth(self.ChlBtnWidth*0.3)
        self.BtnA1.setStyleSheet(Mstyle.btnOnStyle)    
        
        self.BtnA2=QtGui.QPushButton('Print',self)
        self.BtnA2.setGeometry(Chlx+self.ChlBtnWidth*0.3,Chly+Chloffsety*8.5,0,0)
        self.BtnA2.setEnabled(True)
        self.BtnA2.setFixedHeight(self.Chlheight)
        self.BtnA2.setFixedWidth(self.ChlBtnWidth*0.4)
        self.BtnA2.setStyleSheet(Mstyle.btnOnStyleB)

        self.BtnA3=QtGui.QPushButton('-',self)
        self.BtnA3.setGeometry(Chlx+self.ChlBtnWidth*0.7,Chly+Chloffsety*8.5,0,0)
        self.BtnA3.setEnabled(True)
        self.BtnA3.setFixedHeight(self.Chlheight)
        self.BtnA3.setFixedWidth(self.ChlBtnWidth*0.3)
        self.BtnA3.setStyleSheet(Mstyle.btnOnStyle)

        
        self.Qlist=QtGui.QListWidget(self)
        self.Qlist.setGeometry(Chlx,Chly+Chloffsety*1,0,0)
        self.Qlist.setFixedHeight(self.Chlheight*7)
        self.Qlist.setFixedWidth(self.ChlBtnWidth)
        self.Qlist.addItems(initRenderSetTool.oData)
        self.Qlist.setSortingEnabled(True)
        self.Qlist.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.Qlist.setStyleSheet(Mstyle.QListWidgetStyleA)   


 
        
        
        #------main btn connect----------------------------
        
        self.BtnA1.clicked.connect(self.BtnA1Fn)
        self.BtnA3.clicked.connect(self.BtnA3Fn)
        self.BtnA2.clicked.connect(self.BtnA2Fn)
        self.BtnAdd.clicked.connect(self.BtnAddFn)
        self.BtnRemove.clicked.connect(self.BtnRemoveFn)
        self.IDlineEt.textChanged.connect(self.IDlineEtFn)
        self.BtnPass.clicked.connect(self.BtnPassFn)
        #--------- default value set-----------------
        #thenumber=int( self.IDlineEt.text())
        initRenderSetTool.IDNumber=1
        initRenderSetTool.MatNumber=1
    #-------main funcion----------------
    def BtnPassFn(self):
        if self.StateBtnA1.width()==self.StateBtnWd:
            checkVal=cmds.confirmDialog(t='Are you ready?',m='Do ya wanna Create ObjID pass?',b=['yes','no'])
            if checkVal=='yes':
                initRenderSetTool.createObjectIDPass()
        else:
            checkVal=cmds.confirmDialog(t='Are you ready?',m='Do ya wanna Create MtlID pass?',b=['yes','no'])
            if checkVal=='yes':
                initRenderSetTool.createMtlIDPass()
                
    def IDlineEtFn(self):
        if self.StateBtnA1.width()==self.StateBtnWd:
            if self.IDlineEt.text()!='':
                thenumber=int( self.IDlineEt.text())
                initRenderSetTool.IDNumber=thenumber
                #print self.IDlineEt.text()
                cmds.inViewMessage(assistMessage=('Set Obj ID : '+str(thenumber)),fade=True,pos="topCenter",bkc=0x00FF1111,a=0.3,fst=10000)
        else:
            if self.IDlineEt.text()!='':
                thenumber=int( self.IDlineEt.text())
                initRenderSetTool.MatNumber=thenumber
                #print self.IDlineEt.text()
                cmds.inViewMessage(assistMessage=('Set Mat ID : '+str(thenumber)),fade=True,pos="topCenter",bkc=0x00FF1111,a=0.3,fst=10000)

    def BtnAddFn(self):
        if self.StateBtnA1.width()==self.StateBtnWd:
            newID=initRenderSetTool.Create_ID()
            self.IDlineEt.setText(str(newID))
        else:
            newID=initRenderSetTool.createMatID()
            self.IDlineEt.setText(str(newID))
            
    def BtnRemoveFn(self):
        initRenderSetTool.Remove_objectID()
        
    def BtnA1Fn(self):
        getSel=self.Qlist.selectedItems()
        ConvertList=[]
        for g in getSel:
            tt=g.text()
            ConvertList.append(tt)
        if ConvertList:
            initRenderSetTool.openOption(ConvertList)
        else:
            print 'no options has be seleced'
            
    def BtnA3Fn(self):
        getSel=self.Qlist.selectedItems()
        ConvertList=[]
        for g in getSel:
            tt=g.text()
            ConvertList.append(tt)
        if ConvertList:
            initRenderSetTool.closeOption(ConvertList)
        else:
            print 'no options has be seleced'
        
            
    def BtnA2Fn(self):
        
        getSel=self.Qlist.selectedItems()
        ConvertList=[]
        for g in getSel:
            tt=g.text()
            ConvertList.append(tt)
        initRenderSetTool.printState(ConvertList)
        
    #-------radio Btn funcion---------
    def StateFunctionA1(self):
        self.StateBtnA1.setGeometry(self.StateSectionA[0][0],self.StateSectionA[0][1],0,0)
        self.StateBtnA2.setGeometry(self.StateSectionA[1][0],self.StateSectionA[1][1],0,0)

        self.StateBtnA1.setFixedWidth(self.StateBtnWd)
        self.StateBtnA2.setFixedWidth(self.StateBtnShrkWd)

        self.StateBtnA1.setStyleSheet(Mstyle.btnOnStyle)
        self.StateBtnA2.setStyleSheet(Mstyle.btnOffStyle)
        
        self.IDlineEt.setText(str(initRenderSetTool.IDNumber))
        #change the number on UI

    def StateFunctionA2(self):
        self.StateBtnA1.setGeometry(self.StateSectionB[0][0],self.StateSectionB[0][1],0,0)
        self.StateBtnA2.setGeometry(self.StateSectionB[1][0],self.StateSectionB[1][1],0,0)

        self.StateBtnA1.setFixedWidth(self.StateBtnShrkWd)
        self.StateBtnA2.setFixedWidth(self.StateBtnWd)

        self.StateBtnA1.setStyleSheet(Mstyle.btnOffStyle)
        self.StateBtnA2.setStyleSheet(Mstyle.btnOnStyleB)
        self.IDlineEt.setText(str(initRenderSetTool.MatNumber))
        #change the number on UI
        
    #--------widget function--------------

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
        if self.opreateVertsDialog is None:
            self.opreateVertsDialog=Render_Set_TOOL()
        self.opreateVertsDialog.show()
    def Cl_Ui(self):
        self.close()
            
#houqiyaodeRT=Render_Set_TOOL()
#houqiyaodeRT.Op_Ui()

