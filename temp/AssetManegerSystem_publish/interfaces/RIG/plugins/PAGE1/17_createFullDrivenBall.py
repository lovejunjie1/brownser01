class human_driverSys():
    def setupDrivenBall(self,inputData):
        #inputData=[target,setSphere,setloc,isParentRot]
        RotType=inputData[3]
        
        target=inputData[0]
        targetParent=cmds.listRelatives(target,parent=1)[0]
        
        setSphere=inputData[1]
        SphereParent=cmds.listRelatives(setSphere,parent=1)[0]
        cmds.parent(setSphere,target)
        cmds.xform(setSphere,os=1,t=(0,0,0))
        cmds.xform(setSphere,os=1,ro=(0,0,0))
        cmds.parent(setSphere,SphereParent)
            
        sepStr=setSphere.split('_')
        if sepStr[1]=='L':
            cmds.rotate('-90deg','180deg',0,setSphere,r=1,os=1)
        else:
            cmds.rotate('-90deg',0,0,setSphere,r=1,os=1)
        locCv=setSphere+'.cv[3][5]'
        locPos=cmds.xform(locCv,q=1,ws=1,t=1)  
        setLoc=inputData[2]
        cmds.xform(setLoc,ws=1,t=locPos)
        
        cmds.parentConstraint(target,setLoc,mo=1)
        cmds.pointConstraint(target,(setSphere),mo=1)
        cmds.orientConstraint(targetParent,(setSphere),mo=1)
    
    
    def createBodySys(self):
        cmds.select(cl=1)      
        bodysys = cmds.group(n='body_driversys',empty=1)
        
        cmds.setAttr(bodysys + '.tx',k=0,l=1)
        cmds.setAttr(bodysys + '.ty',k=0,l=1)
        cmds.setAttr(bodysys + '.tz',k=0,l=1)
        cmds.setAttr(bodysys + '.rx',k=0,l=1)
        cmds.setAttr(bodysys + '.ry',k=0,l=1)
        cmds.setAttr(bodysys + '.rz',k=0,l=1)
        cmds.setAttr(bodysys + '.sx',k=0,l=1)
        cmds.setAttr(bodysys + '.sy',k=0,l=1)
        cmds.setAttr(bodysys + '.sz',k=0,l=1)
        cmds.setAttr(bodysys + '.v',k=0,l=1)
        return bodysys
        
    def addAttrsToDirversysFromSphere(self):
        spheres = []
        alltrans = cmds.ls(type='transform')
        for at in alltrans:
            array = ["up_blend","below_blend","front_blend","back_blend","front_up_blend","back_up_blend","front_below_blend","back_below_blend"]
            attrs = cmds.listAttr(at,ud=1)
            if attrs:
                intersection =  list(set(attrs).intersection(set(array)))
                if len(intersection) == len(array):
                    spheres.append(at)
    
        for i in spheres:
            attrs = cmds.listAttr(i,ud=1)
            title = i.replace('_sphere','')
            cmds.addAttr(bodysys,ln = title,at = "enum",en = "------:",k=1)
            cmds.setAttr(bodysys + '.' + title,l=1)
            for at in attrs:
                if at[-5:] == '_Hide' or at == 'blend':
                    continue
                cmds.addAttr(bodysys,ln = at + '_' + title,at = "float",min = 0.0,max = 1.0,dv=0.0,k=1)
                fixat = str(at)
                if '_R_' in i:
                    if 'front' in at:
                        fixat = at.replace('front','back')
                    elif 'back' in at:
                        fixat = at.replace('back','front')
                cmds.connectAttr((i + "." + fixat),(bodysys + '.' + at + '_' + title),f=1)
            
            
    def create1AxisDriverAttr(self,bodysys,partName,dvSide = 1):
        cmds.addAttr(bodysys,ln = 'range_' + partName,at = "enum",en = "------:",k=1)
        cmds.setAttr(bodysys + '.range_' + partName,l=1) 
        cmds.addAttr(bodysys,ln = 'first_rot_' + partName ,at = "float",min = -360.0,max = 360.0,dv=0.0*dvSide,k=1)
        cmds.setAttr(bodysys + '.first_rot_' + partName,l=1) 
        cmds.addAttr(bodysys,ln = 'seconed_rot_' + partName ,at = "float",min = -360.0,max = 360.0,dv=90.0*dvSide,k=1)
        cmds.setAttr(bodysys + '.seconed_rot_' + partName,l=1) 
        cmds.addAttr(bodysys,ln = 'third_rot_' + partName ,at = "float",min = -360.0,max = 360.0,dv=120.0*dvSide,k=1)
        cmds.setAttr(bodysys + '.third_rot_' + partName,l=1) 
        
        cmds.addAttr(bodysys,ln = partName + 'L',at = "enum",en = "------:",k=1)
        cmds.setAttr(bodysys + '.' + partName +'L',l=1) 
        cmds.addAttr(bodysys,ln = 'fore_' + partName +'L' ,at = "float",min = 0.0,max = 1.0,dv=0.0,k=1)
        cmds.addAttr(bodysys,ln = 'below_' + partName +'L' ,at = "float",min = 0.0,max = 1.0,dv=0.0,k=1)
        
        cmds.addAttr(bodysys,ln = partName + 'R',at = "enum",en = "------:",k=1)
        cmds.setAttr(bodysys + '.' + partName +'R',l=1) 
        cmds.addAttr(bodysys,ln = 'fore_' + partName +'R' ,at = "float",min = 0.0,max = 1.0,dv=0.0,k=1)
        cmds.addAttr(bodysys,ln = 'below_' + partName +'R' ,at = "float",min = 0.0,max = 1.0,dv=0.0,k=1)
    
    
    
    
    def connect1AxisDriverAttr(self,partName,toArray,isInverse = False,nodeSide = ['fore','below'],nodeLayer = [['first','seconed'],['seconed','third']]):
        for ns in range(2):
        
            belowRangeNode = cmds.createNode('setRange',n= partName +'_' + nodeSide[ns] + '_setRange')
            cmds.setAttr(belowRangeNode + '.minX',0)
            cmds.setAttr(belowRangeNode + '.maxX',1)
            cmds.setAttr(belowRangeNode + '.minY',0)
            cmds.setAttr(belowRangeNode + '.maxY',1)
            
            cmds.connectAttr((bodysys + "."+nodeLayer[ns][0]+"_rot_" + partName),(belowRangeNode + '.oldMinX'),f=1)
            cmds.connectAttr((bodysys + "."+nodeLayer[ns][0]+"_rot_" + partName),(belowRangeNode + '.oldMinY'),f=1)
            
            cmds.connectAttr((bodysys + "."+nodeLayer[ns][1]+"_rot_" + partName),(belowRangeNode + '.oldMaxX'),f=1)
            cmds.connectAttr((bodysys + "."+nodeLayer[ns][1]+"_rot_" + partName),(belowRangeNode + '.oldMaxY'),f=1)
            if isInverse:   
                 
                multiNode = cmds.createNode('multiplyDivide',n= partName +'_value_multiply')
                cmds.connectAttr((toArray[0] + '.rotateZ'),(multiNode + '.input1X'),f=1)
                cmds.setAttr(multiNode + '.input2X',-1)
                cmds.connectAttr((toArray[1] + '.rotateZ'),(multiNode + '.input1Y'),f=1)
                cmds.setAttr(multiNode + '.input2Y',-1)
                #multiply input value with -1.
            
                cmds.connectAttr((multiNode + '.outputX'),(belowRangeNode + '.valueX'),f=1)
                cmds.connectAttr((multiNode + '.outputY'),(belowRangeNode + '.valueY'),f=1)
            else:
                cmds.connectAttr((toArray[0] + '.rotateZ'),(belowRangeNode + '.valueX'),f=1)
                cmds.connectAttr((toArray[1] + '.rotateZ'),(belowRangeNode + '.valueY'),f=1)
            
            cmds.connectAttr((belowRangeNode + '.outValueX'),(bodysys + '.' + nodeSide[ns] + '_' + partName + 'L'),f=1)
            cmds.connectAttr((belowRangeNode + '.outValueY'),(bodysys + '.' + nodeSide[ns] + '_' + partName + 'R'),f=1)
    
    
    def createAnkleDriverAttr(self):
        if cmds.objExists('Ankle_L') and cmds.objExists('Ankle_R'):
            cmds.setAttr('Ankle_L.rotateOrder',2)
            cmds.setAttr('Ankle_R.rotateOrder',2)
            partName = 'ankle'
            cmds.addAttr(bodysys,ln = 'range_' + partName,at = "enum",en = "------:",k=1)
            cmds.setAttr(bodysys + '.range_' + partName,l=1) 
            cmds.addAttr(bodysys,ln = 'front_rot_' + partName ,at = "float",min = 0.0,max = 360.0,dv=40.0,k=1)
            cmds.setAttr(bodysys + '.front_rot_' + partName,l=1) 
            cmds.addAttr(bodysys,ln = 'back_rot_' + partName ,at = "float",min = 0.0,max = 360.0,dv=90.0,k=1)
            cmds.setAttr(bodysys + '.back_rot_' + partName,l=1) 
            
            
            cmds.addAttr(bodysys,ln = partName + 'L',at = "enum",en = "------:",k=1)
            cmds.setAttr(bodysys + '.' + partName +'L',l=1) 
            cmds.addAttr(bodysys,ln = 'front_' + partName +'L' ,at = "float",min = 0.0,max = 1.0,dv=0.0,k=1)
            cmds.addAttr(bodysys,ln = 'back_' + partName +'L' ,at = "float",min = 0.0,max = 1.0,dv=0.0,k=1)
            
            cmds.addAttr(bodysys,ln = partName + 'R',at = "enum",en = "------:",k=1)
            cmds.setAttr(bodysys + '.' + partName +'R',l=1) 
            cmds.addAttr(bodysys,ln = 'front_' + partName +'R' ,at = "float",min = 0.0,max = 1.0,dv=0.0,k=1)
            cmds.addAttr(bodysys,ln = 'back_' + partName +'R' ,at = "float",min = 0.0,max = 1.0,dv=0.0,k=1)
            #ready the attributes
            
            
            ankleMultiNode = cmds.createNode('multiplyDivide',n= partName +'_rot_multiply')
            cmds.connectAttr(('Ankle_L.rotateZ'),(ankleMultiNode + '.input1X'),f=1)
            cmds.setAttr(ankleMultiNode + '.input2X',-1)
            cmds.connectAttr(('Ankle_R.rotateZ'),(ankleMultiNode + '.input1Y'),f=1)
            cmds.setAttr(ankleMultiNode + '.input2Y',-1)
            #multiply input value with -1.
            
            
            ankleInputLClamp = cmds.createNode('clamp',n= partName +'_inputL_clamp')
            
            cmds.connectAttr(('Ankle_L.rotateZ'),(ankleInputLClamp + '.inputR'),f=1)
            cmds.connectAttr((bodysys + ".front_rot_" + partName),(ankleInputLClamp + '.maxR'),f=1)
            cmds.setAttr(ankleInputLClamp + '.minR',0)
            
            cmds.connectAttr((ankleMultiNode + '.outputX'),(ankleInputLClamp + '.inputG'),f=1)
            cmds.connectAttr((bodysys + ".back_rot_" + partName),(ankleInputLClamp + '.maxG'),f=1)
            cmds.setAttr(ankleInputLClamp + '.minG',0)
            
            #left side value clamp
            
            ankleInputRClamp = cmds.createNode('clamp',n= partName +'_inputR_clamp')
            
            cmds.connectAttr(('Ankle_R.rotateZ'),(ankleInputRClamp + '.inputR'),f=1)
            cmds.connectAttr((bodysys + ".front_rot_" + partName),(ankleInputRClamp + '.maxR'),f=1)
            cmds.setAttr(ankleInputRClamp + '.minR',0)
            
            cmds.connectAttr((ankleMultiNode + '.outputY'),(ankleInputRClamp + '.inputG'),f=1)
            cmds.connectAttr((bodysys + ".back_rot_" + partName),(ankleInputRClamp + '.maxG'),f=1)
            cmds.setAttr(ankleInputRClamp + '.minG',0)
            
            #right side value clamp
            
            
            ankleRangeNodeL = cmds.createNode('setRange',n= partName +'_ankleL_setRange')
            cmds.setAttr(ankleRangeNodeL + '.minX',0)
            cmds.setAttr(ankleRangeNodeL + '.maxX',1)
            cmds.setAttr(ankleRangeNodeL + '.minY',0)
            cmds.setAttr(ankleRangeNodeL + '.maxY',1)
            cmds.setAttr(ankleRangeNodeL + '.oldMinX',0)
            cmds.setAttr(ankleRangeNodeL + '.oldMinY',0)
            
            cmds.connectAttr((bodysys + ".front_rot_" + partName),(ankleRangeNodeL + '.oldMaxX'),f=1)
            cmds.connectAttr((bodysys + ".back_rot_" + partName),(ankleRangeNodeL + '.oldMaxY'),f=1)
            
            cmds.connectAttr((ankleInputLClamp + ".outputR"),(ankleRangeNodeL + '.valueX'),f=1)
            cmds.connectAttr((ankleInputLClamp + ".outputG"),(ankleRangeNodeL + '.valueY'),f=1)
            
            cmds.connectAttr((ankleRangeNodeL + '.outValueX'),(bodysys + '.front_' + partName + 'L'),f=1)
            cmds.connectAttr((ankleRangeNodeL + '.outValueY'),(bodysys + '.back_' + partName + 'L'),f=1)
            
            #left side range connection
            
            ankleRangeNodeR = cmds.createNode('setRange',n= partName +'_ankleR_setRange')
            cmds.setAttr(ankleRangeNodeR + '.minX',0)
            cmds.setAttr(ankleRangeNodeR + '.maxX',1)
            cmds.setAttr(ankleRangeNodeR + '.minY',0)
            cmds.setAttr(ankleRangeNodeR + '.maxY',1)
            cmds.setAttr(ankleRangeNodeR + '.oldMinX',0)
            cmds.setAttr(ankleRangeNodeR + '.oldMinY',0)
            
            cmds.connectAttr((bodysys + ".front_rot_" + partName),(ankleRangeNodeR + '.oldMaxX'),f=1)
            cmds.connectAttr((bodysys + ".back_rot_" + partName),(ankleRangeNodeR + '.oldMaxY'),f=1)
            
            cmds.connectAttr((ankleInputRClamp + ".outputR"),(ankleRangeNodeR + '.valueX'),f=1)
            cmds.connectAttr((ankleInputRClamp + ".outputG"),(ankleRangeNodeR + '.valueY'),f=1)
            
            cmds.connectAttr((ankleRangeNodeR + '.outValueX'),(bodysys + '.front_' + partName + 'R'),f=1)
            cmds.connectAttr((ankleRangeNodeR + '.outValueY'),(bodysys + '.back_' + partName + 'R'),f=1)
            
            #right side range connection
        else:
            print 'Ankle_L and AnkleR not exists'
    
    
    def startup(self):
        if cmds.objExists('body_driversys'):
            print 'exists .skip'
        else:
            ask=cmds.confirmDialog( title='tips', message='do you want do step 1?', button=['yes','cancel'])
            dict = getAssetManagerPath()
            if ask=='yes':
            
                importPath=dict['bin']+'/library/driven_ball_twoLeg.ma'
                cmds.file(importPath,i=True,type='mayaAscii',pmt=False,rer=True)
                cmds.scriptEditorInfo(ch=True)
                
            ask=cmds.confirmDialog( title='tips', message='do you want do step 2?', button=['yes','cancel'])
            if ask=='yes':
                cmds.setAttr('FKIKLeg_R.FKIKBlend',0)
                cmds.setAttr('FKIKLeg_L.FKIKBlend',0)
                cmds.setAttr('FKIKArm_R.FKIKBlend',0)
                cmds.setAttr('FKIKArm_L.FKIKBlend',0)
                mainData=[
                    ['Neck_M','Neck_sphere','Neck_aimLoc',1],
                    ['Head_M','Head_sphere','Head_aimLoc',1],
                    
                    ['Wrist_L','Wrist_L_sphere','Wrist_L_aimLoc',1],
                    ['Wrist_R','Wrist_R_sphere','Wrist_R_aimLoc',1],
                    
                    ['Shoulder_L','Shoulder_L_sphere','Shoulder_L_aimLoc',2],
                    ['Shoulder_R','Shoulder_R_sphere','Shoulder_R_aimLoc',2],
                    
                    ['Hip_L','Hip_L_sphere','Hip_L_aimLoc',2],
                    ['Hip_R','Hip_R_sphere','Hip_R_aimLoc',2],
                     
                    ['Scapula_L','Scapula_L_sphere','Scapula_L_aimLoc',3],
                    ['Scapula_R','Scapula_R_sphere','Scapula_R_aimLoc',3],
                    
                    ['Scapula1_L','Scapula1_L_sphere','Scapula1_L_aimLoc',3],
                    ['Scapula1_R','Scapula1_R_sphere','Scapula1_R_aimLoc',3]]
                
                for md in mainData:
                    self.setupDrivenBall(md)
            
            
            
                    
            bodysys = self.createBodySys()
            #cmds.setAttr(bodysys + '.isHistoricallyInteresting',0)
            
            partName = 'elbow'
            self.create1AxisDriverAttr(bodysys,'elbow')
            self.create1AxisDriverAttr(bodysys,'knee')
            
            partName = 'elbow'
            toArray = ['Elbow_L','Elbow_R']
            self.connect1AxisDriverAttr(partName,toArray)
            partName = 'knee'
            toArray = ['Knee_L','Knee_R']
            self.connect1AxisDriverAttr(partName,toArray,isInverse=True)
            self.createAnkleDriverAttr()
            self.addAttrsToDirversysFromSphere()

HDS = human_driverSys()
HDS.startup()
  
        