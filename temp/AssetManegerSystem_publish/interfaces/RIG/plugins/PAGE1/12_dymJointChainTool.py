#-*- coding:gb2312 -*-
import sys,shiboken
from PySide import QtCore,QtGui
from PySide.QtCore import Qt
from maya.OpenMayaUI import MQtUtil
import maya.cmds as cmds
import maya.mel as mel


class dymJointChain_Fn(QtCore.QObject):
    def FY_MakeJointChainDynamic(self,all_bone):
        num_bone=len(all_bone)
        
        if num_bone==0:
            cmds.warning('NO')
        else:
            n_crv=all_bone[0]+'_crv'
            cv='curve -d 1'
            for id,a in enumerate(all_bone):
                pos_bone=cmds.joint(a,q=1,p=1)
                cv+=(' -p '+str(pos_bone[0])+' '+str(pos_bone[1])+' '+str(pos_bone[2])+' ')
            cCrv=mel.eval(cv)
            cmds.rename(cCrv,n_crv)
            mel.eval('makeCurvesDynamicHairs 1 0 1')
            
            temp_aaa = cmds.listRelatives(n_crv,p=1)
            temp_bbb = cmds.listConnections (temp_aaa[0]+".outHair")
            hair_Syst = cmds.rename(temp_bbb[0],("hairsystem_"+all_bone[0]))
            foll_hair = cmds.rename(temp_aaa[0],("follicle_"+all_bone[0]))
            hair_foll_grp = cmds.listRelatives (foll_hair,p=1)
            rot_bone=cmds.xform(all_bone[0],ws=1,q=1,ro=1)
            pos_bone2 = cmds.joint(all_bone[0],q=1,p=1)
            loc_JNT = cmds.spaceLocator(p=[0,0,0],n=("LOC_"+all_bone[0]))
    		
            cmds.xform(loc_JNT[0],ws=1,t=pos_bone2)
            cmds.xform(loc_JNT[0],ws=1,ro=rot_bone)
            
            foll_s = cmds.listRelatives(foll_hair,s=1)
            hairsys_s = cmds.listRelatives(hair_Syst,s=1)
    		
            cmds.setAttr ((foll_s[0]+".pointLock"),1)
            cmds.setAttr ((hairsys_s[0]+".stiffness"),0.001)
            cmds.setAttr ((foll_hair+".visibility"),0)
            cmds.setAttr ((hair_Syst+".visibility"),0)
    
            temp_crgp = cmds.listRelatives(all_bone[0],p=1)
            if temp_crgp:
                cmds.parent(temp_crgp[0],foll_hair,hair_Syst,loc_JNT)
            else:
                cmds.parent(all_bone[0],foll_hair,hair_Syst,loc_JNT)
                
            cmds.select(hair_Syst)
            mel.eval('convertHairSelection \"current\";')
            outCrv=cmds.rename("out_crv_"+all_bone[0])
            outCrvP=cmds.listRelatives(outCrv,p=1)
            cmds.delete(hair_foll_grp[0])
            
            mainGrp=cmds.group(empty=1,n="LOC_"+all_bone[0]+"_grp")
            cmds.xform(mainGrp,ws=1,t=pos_bone2)
            cmds.xform(mainGrp,ws=1,ro=rot_bone)
            
            ikH=cmds.ikHandle(sj=all_bone[0],ee=all_bone[-1],c=outCrv,sol='ikSplineSolver',ccv=False,ns=4,n="hair_IKH_"+all_bone[0])
            cmds.setAttr (("hair_IKH_"+all_bone[0]+".visibility"),0)
            cmds.setAttr ((outCrv+".visibility"),0)
            cmds.setAttr ((all_bone[-1]+".visibility"),0)
            
            
            cmds.delete(outCrvP)
            cmds.parent(loc_JNT,mainGrp)
            cmds.parent(ikH[0],loc_JNT)
            cmds.parent(outCrv,mainGrp)
            return [mainGrp,loc_JNT,all_bone[0],outCrv,hair_Syst,hair_foll_grp[0]]
    
    def duplicateJnts(self,jntName):
        #sel = cmds.ls(sl=1)
        #jntName = inputRoot
        cmds.select(cl=1)
        cmds.select(jntName)
        cmds.SelectHierarchy()
        origJnts=cmds.ls(sl=1)
        
        zeroName=cmds.duplicate(jntName,rr=1,n=jntName + '_zero_jnts',rc=1)
        cmds.setAttr(zeroName[0]+'.visibility',0)
        cmds.select(zeroName)
        cmds.SelectHierarchy()
        zeroTemp=cmds.ls(sl=1)
        
        sdkName=cmds.duplicate(jntName,rr=1,n=jntName + '_sdk_jnts',rc=1)
        cmds.setAttr(sdkName[0]+'.visibility',0)
        cmds.select(sdkName)
        cmds.SelectHierarchy()
        sdkTemp=cmds.ls(sl=1)
        #for i in sdkTemp:
        #    cmds.setAttr(i+'.radius',0)
        
        dymName=cmds.duplicate(jntName,rr=1,n=jntName + '_dym_jnts',rc=1)
        cmds.setAttr(dymName[0]+'.visibility',0)
        cmds.select(dymName)
        cmds.SelectHierarchy()
        dymTemp=cmds.ls(sl=1)
        
        
        zeroJnts=zeroTemp
        sdkJnts=sdkTemp
        dymJnts=dymTemp
        for jnt,zero,sdk,dym,ID in zip(origJnts,zeroTemp,sdkTemp,dymTemp,range(len(origJnts))):
            zeroJnts[ID]=cmds.rename(zero,jnt+'_dymChain_record')
            sdkJnts[ID]=cmds.rename(sdk,jnt+'_dymChain_sdk')
            dymJnts[ID]=cmds.rename(dym,jnt+'_dymChain_dym')
    
        return [origJnts,zeroTemp,sdkTemp,dymTemp]
    
    
    def createCtrl(self,theName,kw='a'):
        returnObj=''
        if kw=='a':
            returnObj=cmds.curve(n=theName+'_ctrl',d=1,p=[(-2,0,-2),(2,0,-2),(2,0,2),(-2,0,2),(-2,0,-2)],k=[0,1,2,3,4])  
            cmds.setAttr(returnObj+'.overrideEnabled',1)
            cmds.setAttr(returnObj+'.overrideColor',13)
        if kw=='b':
            returnObj=cmds.curve(n=theName,d=1,p=[(0,0,2),(0,0,1.001092),(0,0.383101,0.924889),(0,0.707879,0.707879),(0,0.924889,0.383101),(0,1.001092,0),(0,2,0),(0,1.001092,0),(0,0.924889,-0.383101),(0,0.707879,-0.707879),(0,0.383101,-0.924889),(0,0,-1.001092),(0,0,-2),(0,0,-1.001092),(0,-0.383101,-0.924889),(0,-0.707879,-0.707879),(0,-0.924889,-0.383101),(0,-1.001092,0),(0,-2,0),(0,-1.001092,0),(0,-0.924889,0.383101),(0,-0.707879,0.707879),(0,-0.383101,0.924889),(0,0,1.001092),(-0.383101,0,0.924889),(-0.707879,0,0.707879),(-0.924889,0,0.383101),(-1.001092,0,0),(-2,0,0),(-1.001092,0,0),(-0.924889,0,-0.383101),(-0.707879,0,-0.707879),(-0.383101,0,-0.924889),(0,0,-1.001092),(0.383101,0,-0.924889),(0.707879,0,-0.707879),(0.924889,0,-0.383101),(1.001092,0,0),(2,0,0),(1.001092,0,0),(0.924889,0.383101,0),(0.707879,0.707879,0),(0.383101,0.924889,0),(0,1.001092,0),(-0.383101,0.924889,0),(-0.707879,0.707879,0),(-0.924889,0.383101,0),(-1.001092,0,0),(-0.924889,-0.383101,0),(-0.707879,-0.707879,0),(-0.383101,-0.924889,0),(0,-1.001092,0),(0.383101,-0.924889,0),(0.707879,-0.707879,0),(0.924889,-0.383101,0),(1.001092,0,0),(0.924889,0,0.383101),(0.707879,0,0.707879),(0.383101,0,0.924889),(0,0,1.001092),(0,0,0),(0,0,-1.001092),(0,0,0),(1.001092,0,0),(0,0,0),(-1.001092,0,0),(0,0,0),(0,-1.001092,0),(0,0,0),(0,1.001092,0)],k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69])
            cmds.setAttr(returnObj+'.overrideEnabled',1)
            cmds.setAttr(returnObj+'.overrideColor',17)
        grp = cmds.group(returnObj,n=theName + '_dymChain_Grp') 
        sdk = cmds.group(grp,n=theName + '_dymChain_SDK') 
        zero = cmds.group(sdk,n=theName + '_dymChain_Zero') 
        return [zero,sdk,grp,returnObj]
        
    #start here
    def createDymSystem(self,inputRoot,isEvery = False):
        #sel = cmds.ls(sl=1)
        dupArray = self.duplicateJnts(inputRoot)
        oriJnt = dupArray[0]
        zeroJnt = dupArray[1]
        sdkJnt = dupArray[2]
        dymJnt = dupArray[3] 
        #duplicate joints

        dymRtn = self.FY_MakeJointChainDynamic(dymJnt) 
        newNuc = '' 
        if isEvery:
            newNuc=cmds.createNode('nucleus',n = inputRoot + '_dymChain_nucleus')
            cmds.select(dymRtn[4])
            mel.eval('assignNSolver \"'+newNuc+'\"')

            #reassign neclues to input neclues.

        #dymanic joint
        
        getM = cmds.xform(inputRoot,q=1,ws=1,m=1)
        mainCtrl = self.createCtrl(inputRoot)
        
        cmds.addAttr(mainCtrl[-1],ln = 'switch',at='double',min = 0.0,max = 1.0,dv = 0.0,k=1)
        cmds.setAttr(mainCtrl[-1] + '.switch',l=1)
        cmds.addAttr(mainCtrl[-1],ln="ctrlJnt",at="enum",en="none:dym:key:",k=1)
        
        cmds.addAttr(mainCtrl[-1],ln = 'justiceValue',at='double',min = 0.0,max = 1.0,dv = 0.0,k=1)
        cmds.setAttr(mainCtrl[-1] + '.justiceValue',l=1)
        for i in range(len(oriJnt)):
            dValue = round(float(i+1)/len(oriJnt),2)
            cmds.addAttr(mainCtrl[-1],ln = 'attr' + str(i),at='double',min = 0.0,max = 1.0,dv = dValue,k=1)
        # create mainCtrl
        
        cmds.xform(mainCtrl[0],ws=1,m=getM)
        sdkGrp = cmds.group(n=sdkJnt[0] + '_dymChain_grp',empty=1)
        cmds.xform(sdkGrp,ws=1,m=getM)
        cmds.parent(sdkJnt[0],sdkGrp)
        recordGrp = cmds.group(n=zeroJnt[0] + '_dymChain_grp',empty=1)
        cmds.xform(recordGrp,ws=1,m=getM)
        cmds.parent(zeroJnt[0],recordGrp)
        
        jntAllGrp = cmds.group(sdkGrp,recordGrp,dymRtn[0],n=inputRoot + '_dymChain_joints_all_grp')
        
        cmds.parentConstraint(mainCtrl[-1],dymRtn[1])
        cmds.parentConstraint(mainCtrl[-1],sdkGrp)
        cmds.parentConstraint(mainCtrl[-1],recordGrp)
        #control joints
        
        for i in range(len(dymJnt)):
            dataJnt = dymJnt[i]
            toJnt = sdkJnt[i]
            ctrlAttr = mainCtrl[-1] + '.attr' + str(i)
                
            rotNode = cmds.createNode('multiplyDivide',n = dataJnt + '_multiplyDivide_rotate')
            cmds.connectAttr(dataJnt + '.rotate',rotNode + '.input1',f=1)
            cmds.connectAttr(ctrlAttr,rotNode + '.input2X',f=1)
            cmds.connectAttr(ctrlAttr,rotNode + '.input2Y',f=1)
            cmds.connectAttr(ctrlAttr,rotNode + '.input2Z',f=1)
            cmds.connectAttr(rotNode + '.output',toJnt + '.rotate',f=1)
        #finish dymJoint damping
        
        preBldArray = []
        nxtBldArray = []
        nowParent = ''
        topGrp = ''
        theDriver = mainCtrl[-1] + '.ctrlJnt'
        for i in range(len(oriJnt)-1):
            
            newCtrl = self.createCtrl('FK_dymChain_' + oriJnt[i],kw='b')
            theM = cmds.xform(oriJnt[i],q=1,ws=1,m=1)
            cmds.xform(newCtrl[0],ws=1,m=theM)
            cmds.parentConstraint(newCtrl[-1],oriJnt[i])
            cmds.scaleConstraint(newCtrl[-1],oriJnt[i])
            if nowParent:
                cmds.parent(newCtrl[0],nowParent)
            else:
                topGrp = newCtrl[0]
            nowParent = newCtrl[-1]
            #finish set
            #blendColors
    
            the_1_2_blend = cmds.createNode('condition',n=oriJnt[i] + '_sec1_sec2_Condition')
            cmds.connectAttr(theDriver,the_1_2_blend + '.firstTerm',f=1)
            cmds.setAttr(the_1_2_blend + ".secondTerm",1)
            cmds.connectAttr(sdkJnt[i] + '.rotate',the_1_2_blend + '.colorIfTrue',f=1)
            cmds.connectAttr(zeroJnt[i] + '.rotate',the_1_2_blend + '.colorIfFalse',f=1)
            
            
            the_0_1_blend = cmds.createNode('condition',n=oriJnt[i] + '_sec0_other_Condition')
            cmds.connectAttr(theDriver,the_0_1_blend + '.firstTerm',f=0)
            cmds.setAttr(the_0_1_blend + ".secondTerm",0)
            cmds.setAttr(the_0_1_blend + ".colorIfTrue",0,0,0,type = 'double3')
            cmds.connectAttr(the_1_2_blend + '.outColor',the_0_1_blend + '.colorIfFalse',f=1)
            
            
            cmds.connectAttr(the_0_1_blend + '.outColor',newCtrl[1] + '.rotate',f=1)
    
        cmds.parentConstraint(mainCtrl[-1],topGrp)
        cmds.scaleConstraint(mainCtrl[-1],topGrp)
        #collect driven infomations
            
        cmds.setAttr(theDriver,0)  
            
        #make a switch to control
        if newNuc:
            cmds.group(mainCtrl[0],jntAllGrp,topGrp,newNuc,n=oriJnt[0] + '_dymJointChain_all_grp')
        else:
            cmds.group(mainCtrl[0],jntAllGrp,topGrp,n=oriJnt[0] + '_dymJointChain_all_grp')
            
    def resetValues(self):
        sel = cmds.ls(sl=1)
        
        for s in sel:
            Attrs = cmds.listAttr(s,ud=1)
            if 'justiceValue' in Attrs:
                theArray = [i for i in Attrs if 'attr' == i[:4]]
                for i in range(len(theArray)):
                    dValue = round(float(i+1)/len(theArray),2)
                    cmds.setAttr(s +  '.attr' + str(i),dValue)
             
    def selHairSys(self):
        
        sel = cmds.ls(sl=1)[0]
        
        c1 = sel.replace('_ctrl','_dymChain_dym')
        
        hairSys = 'hairsystem_' + c1
        
        if cmds.objExists(hairSys):
            cmds.select(hairSys)
        else:
            cmds.warning(hairSys +' not found')
 

    def recordDymToRecord(self):
        sel = cmds.ls(sl=1)[0]
        if sel:
            recordRoot = sel.replace('_ctrl','_dymChain_record')
            
            if cmds.objExists(recordRoot):
                minTime = cmds.playbackOptions(q=1,minTime=1)
                maxTime = cmds.playbackOptions(q=1,maxTime=1)
                feedback = cmds.confirmDialog(m='do you want to record \n' + sel + ' ?\ntime:\nfrom ' + str(minTime) + 'f to ' + str(maxTime) + 'f ?',button = ['yes','no'])
                if feedback == 'yes':
                    
                    cmds.select(recordRoot)
                    cmds.SelectHierarchy()
                    recordJnts=cmds.ls(sl=1,type='joint')
                    dict = {}
                    for i in recordJnts:
                        dymJnt = i.replace('_record','_dym')
                        if cmds.objExists(dymJnt):
                            dict.update({i:dymJnt})
                    
                    for t in range(int(minTime),int(maxTime)):
                        cmds.currentTime(t)
                        for key,itm in dict.items():
                            fromRot = cmds.xform(itm,q=1,os=1,ro=1)
                            cmds.xform(key,os=1,ro=fromRot)
                            cmds.setKeyframe(key,at = 'rotateX')
                            cmds.setKeyframe(key,at = 'rotateY')
                            cmds.setKeyframe(key,at = 'rotateZ')
                    cmds.setAttr(sel + '.ctrlJnt' , 2)
            else:
                print 'selection node is not the dymchain root ctontrller'              
#newNuc=cmds.createNode('nucleus')
#dymSys = dymJointChain_Fn()
#dymSys.createDymSystem('joint8',isEvery = True)





class DymChainUI_RIG_TOOL(QtGui.QDialog,dymJointChain_Fn):
    opreateVertsDialog=None
    titleName='Dymnamic JointChain'
    widgetHeight=280
    widgetWidth=380
    def createUI(self):
        self.cleanOpenWindow()
        #------window parent Set----------------------------
        self.m_DragPosition=self.pos()
        self.setWindowFlags( Qt.WindowStaysOnTopHint)
        self.setStyleSheet(Mstyle.QWidget())
        self.resize(self.widgetWidth,self.widgetHeight)
        self.setWindowTitle(self.titleName)
        self.setParent(getMayaWindow())
        codec = QtCore.QTextCodec.codecForName("GB2312")
        #-----main Set----------------    
        mv = QtGui.QVBoxLayout()
        self.setLayout(mv)


        #------function Set-----------------------
        HZ = QtGui.QHBoxLayout()
        mv.addLayout(HZ)

        
        Xbtn=QtGui.QPushButton('x',self)
        Xbtn.setGeometry(0,0,0,0)
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())
        Xbtn.clicked.connect(self.Cl_Ui)
        HZ.addWidget(Xbtn)
        
        #TitleLabel
        TitleLab=QtGui.QLabel(self.titleName,self)
        TitleLab.setFixedHeight(20)
        TitleLab.setFixedWidth(140)
        TitleLab.setStyleSheet(Mstyle.QLabel(fontSize = '12px'))
        HZ.addStretch(1)
        HZ.addWidget(TitleLab)
        HZ.addStretch(1)

        
        HA = QtGui.QHBoxLayout()
        mv.addLayout(HA)
        self.inputLE=QtGui.QLineEdit(self)
        #self.inputLE.setGeometry(20,20,0,0)
        self.inputLE.setEnabled(True)
        self.inputLE.setFixedHeight(20)
        #self.inputLE.setFixedWidth(self.widgetWidth*0.75)
        self.inputLE.setStyleSheet(Mstyle.QLineEdit())   
        HA.addWidget(self.inputLE)
        
        self.BtnA1=QtGui.QPushButton('<<<',self)
        self.BtnA1.setGeometry(self.widgetWidth*0.81,20,0,0)
        self.BtnA1.setEnabled(True)
        self.BtnA1.setFixedHeight(20)
        self.BtnA1.setFixedWidth(50)
        self.BtnA1.setStyleSheet(Mstyle.QPushButton())    
        HA.addWidget(self.BtnA1)    
        
        HB = QtGui.QHBoxLayout()
        mv.addLayout(HB)
        
        self.BtnA2=QtGui.QPushButton('Create',self)
        self.BtnA2.setGeometry(self.widgetWidth*0.65,45,0,0)
        self.BtnA2.setEnabled(True)
        self.BtnA2.setFixedHeight(20)
        self.BtnA2.setFixedWidth(115)
        self.BtnA2.setStyleSheet(Mstyle.QPushButton())   
        
        
        self.groupMsg=QtGui.QGroupBox ('message',self)
        self.groupMsg.setGeometry(20,70,0,0)
        self.groupMsg.setFixedHeight(140)
        #self.groupMsg.setFixedWidth(self.widgetWidth*0.9)
        self.groupMsg.setStyleSheet(Mstyle.QGroupBox())   
        mv.addWidget(self.groupMsg)
        
        labMsg = codec.toUnicode('single:\n    every dym joint chain share one nuclues node\neveryOne:\n    each dym joint chain have there own nuclues.\nrecord:\n    record dym joint trail and switch ctrl jnt to "key"')
        
        self.lab=QtGui.QLabel (labMsg,self.groupMsg)
        self.lab.setGeometry(20,10,0,0)
        self.lab.setFixedHeight(120)
        self.lab.setFixedWidth(self.widgetWidth*0.8)
        self.lab.setStyleSheet('QLabel{background:transparent;font-size:14px;color:#DDDDDD}')   
        #self.lab.setTextFormat (QtGui.QFont('Microsoft YaHei', 55, QtGui.QFont.Bold))
        
        mv.addStretch(1)

        #------- radio button UI----------------------

        StateBtnSpace = 3
        
        self.StateBaseWidth=105     
        self.StateShrikWidth=85
        
        self.StateBtnWd=self.StateBaseWidth-StateBtnSpace
        self.StateBtnShrkWd=self.StateShrikWidth-StateBtnSpace
        
        self.StateBtnA1=QtGui.QPushButton('everyOne',self)
        self.StateBtnA1.setEnabled(True)
        self.StateBtnA1.setFixedHeight(20)
        self.StateBtnA1.setFixedWidth(self.StateBtnShrkWd)
        self.StateBtnA1.setStyleSheet(Mstyle.QPushButton(kw='off'))
        HB.addWidget(self.StateBtnA1)
        
        self.StateBtnA2=QtGui.QPushButton('single',self)
        self.StateBtnA2.setEnabled(True)
        self.StateBtnA2.setFixedHeight(20)
        self.StateBtnA2.setFixedWidth(self.StateBtnWd)
        self.StateBtnA2.setStyleSheet(Mstyle.QPushButton(kw='b'))
        HB.addWidget(self.StateBtnA2)
        HB.addStretch(1)
        HB.addWidget(self.BtnA2)
        
        self.StateBtnA1.clicked.connect(self.StateFunctionA1)
        self.StateBtnA2.clicked.connect(self.StateFunctionA2)
        
        
        HC = QtGui.QHBoxLayout()
        mv.addLayout(HC)
        
        resetBtn=QtGui.QPushButton("reset Attr's",self)
        resetBtn.setEnabled(True)
        resetBtn.setFixedHeight(20)
        resetBtn.setFixedWidth(100)
        resetBtn.setStyleSheet(Mstyle.QPushButton())
        HC.addWidget(resetBtn)
        
        recordBtn=QtGui.QPushButton("record",self)
        recordBtn.setEnabled(True)
        recordBtn.setFixedHeight(20)
        recordBtn.setFixedWidth(100)
        recordBtn.setStyleSheet(Mstyle.QPushButton(kw='b'))
        HC.addWidget(recordBtn)
        
        selHairBtn=QtGui.QPushButton("sel hairSys",self)
        selHairBtn.setEnabled(True)
        selHairBtn.setFixedHeight(20)
        selHairBtn.setFixedWidth(100)
        selHairBtn.setStyleSheet(Mstyle.QPushButton())
        HC.addWidget(selHairBtn)
        #------connect----------------------------
        
        self.BtnA1.clicked.connect(self.BtnA1Fn)
        self.BtnA2.clicked.connect(self.BtnA2Fn)
        selHairBtn.clicked.connect(self.selHairSys)
        recordBtn.clicked.connect(self.recordDymToRecord)
        resetBtn.clicked.connect(self.resetValues)        
    #------- radio button functions----------------------
    def StateFunctionA1(self):

        self.StateBtnA1.setFixedWidth(self.StateBtnWd)
        self.StateBtnA2.setFixedWidth(self.StateBtnShrkWd)

        self.StateBtnA1.setStyleSheet(Mstyle.QPushButton())
        self.StateBtnA2.setStyleSheet(Mstyle.QPushButton(kw='off'))

    def StateFunctionA2(self):

        self.StateBtnA1.setFixedWidth(self.StateBtnShrkWd)
        self.StateBtnA2.setFixedWidth(self.StateBtnWd)

        self.StateBtnA1.setStyleSheet(Mstyle.QPushButton(kw='off'))
        self.StateBtnA2.setStyleSheet(Mstyle.QPushButton(kw='b'))

    #--------function--------------
    def BtnA1Fn(self):
        self.jointArray=cmds.ls(sl=1,type='joint')
        theStr=','.join(self.jointArray)
        self.inputLE.setText(theStr)
        
        
    def BtnA2Fn(self):
        sw=False
        if self.StateBtnA1.width() == self.StateBtnWd:
            sw=True
            
        if self.inputLE.text():
            oArray=self.inputLE.text().split(',')
            for j in oArray:
                self.createDymSystem(j,isEvery = sw)
    #----------------------------------

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
   
    def cleanOpenWindow(self):
        gmw = getMayaWindow()
        for g in gmw.children():
            try:
                Tit = g.windowTitle()
                if Tit == self.titleName:
                    g.close()
                    g.setParent(None)
            except:
                pass

        
    def Op_Ui(self):
        self.show()
    def Cl_Ui(self):
        self.deleteLater()
        
    def closeEvent(self, event):  
        self.deleteLater()
            
dymJointUIRT=DymChainUI_RIG_TOOL()
dymJointUIRT.setWindowFlags( Qt.WindowStaysOnTopHint)
dymJointUIRT.createUI()
dymJointUIRT.Op_Ui()



#dymJointUIRT.Cl_Ui()



