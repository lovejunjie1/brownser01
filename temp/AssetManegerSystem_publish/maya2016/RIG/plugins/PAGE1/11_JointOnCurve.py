import maya.cmds as cmds
from PySide import QtCore,QtGui
from PySide.QtCore import Qt
import sys
import shiboken

import maya.OpenMayaUI as OpenMayaUI
def getMayaWindow():
    """
    Get Maya window
    :return: maya wnd
    """
    mayaMainWindowPtr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(mayaMainWindowPtr), QtGui.QWidget)
    
class JointOnCurveUI_RIG_TOOL(QtGui.QMainWindow):
    UITitle='JointOnCurveUI_RIG_TOOL'
    x=260
    y=100
    
    def createUI(self):
        #------Style Set----------------------------
        self.m_DragPosition=self.pos()
        
        self.resize(self.x,self.y)
        self.move(402,350)
        self.setWindowFlags(Qt.SubWindow|Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setStyleSheet(Mstyle.QWidget())
        mian=QtGui.QWidget(self)
        mian.resize(self.x,self.y)
        #-----close Btn Set----------------                                                 
        Xbtn=QtGui.QPushButton('x',mian)
        Xbtn.setGeometry(0,0,0,0)
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())
        
        Xbtn.clicked.connect(self.Cl_Ui)
        
        #-----TitleLabel-----------------------
        TitleLab=QtGui.QLabel('create joint base on curve',mian)
        TitleLab.setGeometry(40,5,0,0)
        TitleLab.setFixedHeight(20)
        TitleLab.setFixedWidth(170)
        TitleLab.setStyleSheet(Mstyle.QLabel(fontSize='11px'))


        #------main btn-----------------------


        
        self.BtnA1=QtGui.QPushButton('joint',mian)
        self.BtnA1.setGeometry(20,60,0,0)
        self.BtnA1.setEnabled(True)
        self.BtnA1.setFixedHeight(20)
        self.BtnA1.setFixedWidth(60)
        self.BtnA1.setStyleSheet(Mstyle.QPushButton())    
        
        self.BtnA2=QtGui.QPushButton('chain',mian)
        self.BtnA2.setGeometry(85,60,0,0)
        self.BtnA2.setEnabled(True)
        self.BtnA2.setFixedHeight(20)
        self.BtnA2.setFixedWidth(60)
        self.BtnA2.setStyleSheet(Mstyle.QPushButton())        
   
        self.sb=QtGui.QSpinBox(mian)
        self.sb.setGeometry(170,60,0,0)
        self.sb.setEnabled(True)
        self.sb.setFixedHeight(20)
        self.sb.setFixedWidth(60)
        self.sb.setValue(10)
        #------main btn connect----------------------------
        
        self.BtnA1.clicked.connect(self.BtnA1Fn)
        self.BtnA2.clicked.connect(self.BtnA2Fn)
        #------radio btn----------------------------
        StateBasePosX = 20
        StateBasePosY = 30
        StateBtnSpace = 3
        
        self.StateShrikHeight=15
        self.StateBaseHeight=20
           
        self.StateBaseWidth=85   
        self.StateShrikWidth=65
        
        self.StateBtnWd=self.StateBaseWidth-StateBtnSpace
        self.StateBtnShrkWd=self.StateShrikWidth-StateBtnSpace
        
        self.StateSectionA=[(StateBasePosX,StateBasePosY,0,0),
                            (StateBasePosX+self.StateBaseWidth,StateBasePosY,0,0),
                            (StateBasePosX+self.StateBaseWidth+self.StateShrikWidth,StateBasePosY,0,0)] 
                                   
        self.StateSectionB=[(StateBasePosX,StateBasePosY,0,0),
                            (StateBasePosX+self.StateShrikWidth,StateBasePosY,0,0),
                            (StateBasePosX+self.StateShrikWidth+self.StateBaseWidth,StateBasePosY,0,0)]  
                                  
        self.StateSectionC=[(StateBasePosX,StateBasePosY,0,0),
                            (StateBasePosX+self.StateShrikWidth,StateBasePosY,0,0),
                            (StateBasePosX+self.StateShrikWidth+self.StateShrikWidth,StateBasePosY,0,0)]
                            
        self.StateBtnA1=QtGui.QPushButton('EP',mian)
        self.StateBtnA1.setGeometry(self.StateSectionA[0][0],self.StateSectionA[0][1],0,0)
        self.StateBtnA1.setEnabled(True)
        self.StateBtnA1.setFixedHeight(self.StateBaseHeight)
        self.StateBtnA1.setFixedWidth(self.StateBtnWd)
        self.StateBtnA1.setStyleSheet(Mstyle.QPushButton())
        
        self.StateBtnA2=QtGui.QPushButton('s_CV',mian)
        self.StateBtnA2.setGeometry(self.StateSectionA[1][0],self.StateSectionA[1][1],0,0)
        self.StateBtnA2.setEnabled(True)
        self.StateBtnA2.setFixedHeight(self.StateBaseHeight)
        self.StateBtnA2.setFixedWidth(self.StateBtnShrkWd)
        self.StateBtnA2.setStyleSheet(Mstyle.QPushButton(kw='off'))
        
        self.StateBtnA3=QtGui.QPushButton('f_CV',mian)
        self.StateBtnA3.setGeometry(self.StateSectionA[2][0],self.StateSectionA[2][1],0,0)
        self.StateBtnA3.setEnabled(True)
        self.StateBtnA3.setFixedHeight(self.StateBaseHeight)
        self.StateBtnA3.setFixedWidth(self.StateBtnShrkWd)
        self.StateBtnA3.setStyleSheet(Mstyle.QPushButton(kw='off'))
        
        self.StateBtnA1.clicked.connect(self.StateFunctionA1)
        self.StateBtnA2.clicked.connect(self.StateFunctionA2)
        self.StateBtnA3.clicked.connect(self.StateFunctionA3)
        
        pass
    #------- radio button functions----------------------
    def StateFunctionA1(self):
        self.StateBtnA1.setGeometry(self.StateSectionA[0][0],self.StateSectionA[0][1],0,0)
        self.StateBtnA2.setGeometry(self.StateSectionA[1][0],self.StateSectionA[1][1],0,0)
        self.StateBtnA3.setGeometry(self.StateSectionA[2][0],self.StateSectionA[2][1],0,0)
        
        self.StateBtnA1.setFixedWidth(self.StateBtnWd)
        self.StateBtnA2.setFixedWidth(self.StateBtnShrkWd)
        self.StateBtnA3.setFixedWidth(self.StateBtnShrkWd)
        
        self.StateBtnA1.setStyleSheet(Mstyle.QPushButton())
        self.StateBtnA2.setStyleSheet(Mstyle.QPushButton(kw='off'))
        self.StateBtnA3.setStyleSheet(Mstyle.QPushButton(kw='off'))
        
    def StateFunctionA2(self):
        self.StateBtnA1.setGeometry(self.StateSectionB[0][0],self.StateSectionB[0][1],0,0)
        self.StateBtnA2.setGeometry(self.StateSectionB[1][0],self.StateSectionB[1][1],0,0)
        self.StateBtnA3.setGeometry(self.StateSectionB[2][0],self.StateSectionB[2][1],0,0)
        
        self.StateBtnA1.setFixedWidth(self.StateBtnShrkWd)
        self.StateBtnA2.setFixedWidth(self.StateBtnWd)
        self.StateBtnA3.setFixedWidth(self.StateBtnShrkWd)
        
        self.StateBtnA1.setStyleSheet(Mstyle.QPushButton(kw='off'))
        self.StateBtnA2.setStyleSheet(Mstyle.QPushButton())
        self.StateBtnA3.setStyleSheet(Mstyle.QPushButton(kw='off'))
        
    def StateFunctionA3(self):
        self.StateBtnA1.setGeometry(self.StateSectionC[0][0],self.StateSectionC[0][1],0,0)
        self.StateBtnA2.setGeometry(self.StateSectionC[1][0],self.StateSectionC[1][1],0,0)
        self.StateBtnA3.setGeometry(self.StateSectionC[2][0],self.StateSectionC[2][1],0,0)
        
        self.StateBtnA1.setFixedWidth(self.StateBtnShrkWd)
        self.StateBtnA2.setFixedWidth(self.StateBtnShrkWd)
        self.StateBtnA3.setFixedWidth(self.StateBtnWd)
        
        self.StateBtnA1.setStyleSheet(Mstyle.QPushButton(kw='off'))
        self.StateBtnA2.setStyleSheet(Mstyle.QPushButton(kw='off'))
        self.StateBtnA3.setStyleSheet(Mstyle.QPushButton())
    def StateAction(self):
        if self.StateBtnA1.width()==self.StateBtnWd:
            #print 'A'
            return 1
        if self.StateBtnA2.width()==self.StateBtnWd:
            #print 'B'
            return 2
            
        if self.StateBtnA3.width()==self.StateBtnWd:
            #print 'C'
            return 3
    #--------main function--------------
    def BtnA1Fn(self):
        if self.StateAction()==1:
            self.wp_jointsOnCurves_doIt('joint',self.sb.value(),cvEp='ep',smartCV=True)
        elif self.StateAction()==2:
            self.wp_jointsOnCurves_doIt('joint',self.sb.value(),cvEp='cv',smartCV=True)
        elif self.StateAction()==3:
            self.wp_jointsOnCurves_doIt('joint',self.sb.value(),cvEp='cv',smartCV=False)
    def BtnA2Fn(self):
        if self.StateAction()==1:
            self.wp_jointsOnCurves_doIt('jointChain',self.sb.value(),cvEp='ep',smartCV=True)
        elif self.StateAction()==2:
            self.wp_jointsOnCurves_doIt('jointChain',self.sb.value(),cvEp='cv',smartCV=True)
        elif self.StateAction()==3:
            self.wp_jointsOnCurves_doIt('jointChain',self.sb.value(),cvEp='cv',smartCV=False)
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
        
    def wp_jointsOnCurves_doIt(self,types,NumberOfJoints,cvEp='ep',smartCV=True): 
        curves= cmds.ls(sl=1,long=1)
        NumberOfCurves = len(curves)
        #smartCV=False  #skip second and last second cv point.
        for i in curves:
        #i=curves[0]
            iShape=cmds.listRelatives(i,s=1)
            if cmds.objectType(iShape[0],isType="nurbsCurve"):
                numTokens=i.split("|")
                myObj = numTokens[-1]
                OriginalCurveName_ = i
                cmds.select(i,r=1)
                newCurve_ = cmds.duplicate(smartTransform=1)
                cmds.select(newCurve_[0])
                cmds.makeIdentity(apply=True,t=1,r=1,s=1,n=0) 
                if (types == "jointChain"):
                    numberOfSpans = NumberOfJoints-1
                elif (types == "joint"):
                    numberOfSpans = NumberOfJoints - 1
                cmds.rebuildCurve(newCurve_[0],ch=1,rpo=1,rt=0,end=1,kr=0,kcp=0,kep=1,kt=0,s=numberOfSpans,d=3,tol=0.01)
                NumberOfSpans = cmds.getAttr (newCurve_[0] + ".spans")
                NumberOfEP =0
                if cvEp=='ep':
                    NumberOfEP=NumberOfSpans + 1
                elif cvEp=='cv':
                    NumberOfDegree=cmds.getAttr (newCurve_[0] + ".degree")
                    NumberOfEP=NumberOfDegree+NumberOfSpans
                ep_0 = newCurve_[0] + "."+cvEp+"[0]"
                tempCluster = cmds.cluster(ep_0)
                cluster_xyz = cmds.xform(tempCluster[1],q=1,rp=1,ws=1)   
                cmds.select(cl=1)
                RootJoint=''
                if (types == "jointChain"):
                    RootJoint = cmds.joint(p=cluster_xyz,n= (myObj + "_jointChain"))
                elif (types == "joint"):
                    RootJoint = cmds.joint(p=cluster_xyz,n= (myObj + "_joint"))
                
                cmds.delete(tempCluster[1])
                singleArray=[RootJoint]
                BaseJoint = RootJoint
                for j in range(NumberOfEP):
                    j=j+1 
                    if j<NumberOfEP :
                        if smartCV==True:
                            if (cvEp=='cv' and j==1) or (cvEp=='cv' and j==(NumberOfEP-2)):
                                continue
                        ep_0 = newCurve_[0] + "."+cvEp+"[" + str(j) + "]"
                        tempCluster = cmds.cluster (ep_0)	
                        cluster_xyz = cmds.xform(tempCluster[1], q=1 ,rp=1,ws=1)
                    
                        newJoint = newJoint = cmds.joint(p=cluster_xyz)
                        singleArray.append(newJoint)
                        if (types == "jointChain") :
                            cmds.parent(newJoint,BaseJoint)
                            BaseJoint = newJoint
                        elif (types == "joint") :
                            cmds.parent(newJoint,w=1)
                        cmds.delete (tempCluster[1])
            
                if (types == "jointChain"):
                    cmds.select(RootJoint,r=1)
                    cmds.joint(e=1,oj='xyz',secondaryAxisOrient='yup',ch=1,zso=1)
                    for count,sa in enumerate(singleArray):
                        cmds.rename(sa,myObj+'_jointChain'+str(count))
                elif (types=='joint'):
                    tempGrp=cmds.group(empty=1,n=myObj+'_joint_grp')
                    for count,sa in enumerate(singleArray):
                        cmds.parent(sa,tempGrp)
                        cmds.rename(sa,myObj+'_joint'+str(count))
                cmds.delete(newCurve_[0])
                
    def Op_Ui(self):
        self.show()
    def Cl_Ui(self):
        self.close()
    def closeEvent(self, event):
        #print type(self)
        self.deleteLater()  
                    
JointOnCurveUIRT=JointOnCurveUI_RIG_TOOL()
JointOnCurveUIRT.createUI()
JointOnCurveUIRT.setParent(getMayaWindow())
JointOnCurveUIRT.Op_Ui()
#JointOnCurveUIRT.Cl_Ui()