
def propRig_bigRing(userDefined=0):
    
    sel=cmds.ls(sl=1)
    objName=''
    if userDefined:
        result = cmds.promptDialog(title='name of prop',message='please enter prop name:',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
        
        if result == 'OK':
        	objName = cmds.promptDialog(query=True, text=True)
    else:
        filePath = cmds.file( query=True, sn=True)
        
        spStr1=filePath.split('prop')
        spStr2=spStr1[-1].split('rig')
        
        objName=spStr2[0][1:-1]
        
        if objName=='':
            result = cmds.promptDialog(title='name of prop',message='please enter prop name:',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
            
            if result == 'OK':
            	objName = cmds.promptDialog(query=True, text=True)
    
    
    
    modelGrp=cmds.group(empty=1,n='Model')
    mainGrp=cmds.group(empty=1,n='prop_'+objName+'_all_grp')
    
    mainCir=cmds.circle(ch=1,o=1,nr=(0,1,0),r=20,n=objName+'_main_Ctrl')
    cmds.setAttr((mainCir[0]+'.overrideEnabled'),1)
    cmds.setAttr((mainCir[0]+'.overrideColor'),17)
    mcGrp=cmds.group(mainCir,n=objName+'_main_Grp')
    mcSDK=cmds.group(mcGrp,n=objName+'_main_SDK')
    mcZero=cmds.group(mcSDK,n=objName+'_main_Zero')
    
    
    flyCir=cmds.circle(ch=1,o=1,nr=(0,1,0),r=18,n=objName+'_fly_Ctrl')
    cmds.setAttr((flyCir[0]+'.overrideEnabled'),1)
    cmds.setAttr((flyCir[0]+'.overrideColor'),14)
    fcGrp=cmds.group(flyCir,n=objName+'_fly_Grp')
    fcSDK=cmds.group(fcGrp,n=objName+'_fly_SDK')
    fcZero=cmds.group(fcSDK,n=objName+'_fly_Zero')
    
    mainJnt=cmds.joint(p=(0,0,0),n=objName+'_main_jnt')
    cmds.setAttr((mainJnt+'.radius'),15)
    
    cmds.parent(modelGrp,mainGrp)
    cmds.parent(fcZero,mainCir[0])
    cmds.parent(mcZero,mainGrp)
    cmds.parent(mainJnt,flyCir[0])
    if sel:
        cmds.parent(sel,modelGrp)
    else:
        print 'no selection'
        
propRig_bigRing()