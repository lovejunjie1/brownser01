def createFlyCtrl():
    flyCtrl=cmds.curve(d=1,p=((0,19,-54),(-12,7,-54),(-6,7,-54),(-6,-7,-54),(6,-7,-54),(6,7,-54),(12,7,-54),(0,19,-54 )),n='fly_Ctrl')
    cmds.setAttr(flyCtrl+".overrideEnabled",1)
    cmds.setAttr(flyCtrl+".overrideColor",14)
    flySDK=cmds.group(flyCtrl,n=(flyCtrl+'_SDK'))
    flyZero=cmds.group(flySDK,n=(flyCtrl+'_Zero'))
    flyGroup=cmds.group(flyZero,n=(flyCtrl+'_Grp'))
    rootPos=cmds.xform('RootX_M',ws=1,q=1,t=1)
    cmds.xform(flyGroup,ws=1,t=rootPos)
    bigRingA=cmds.circle(r=30,d=3,s=8,nr=(0,1,0),n='mainA_Ctrl')
    cmds.setAttr(bigRingA[0]+".overrideEnabled",1)
    cmds.setAttr(bigRingA[0]+".overrideColor",17)
    bigRingASDK=cmds.group(bigRingA[0],n=(bigRingA[0]+'_SDK'))
    bigRingAZero=cmds.group(bigRingASDK,n=(bigRingA[0]+'_Zero'))
    bigRingAGroup=cmds.group(bigRingAZero,n=(bigRingA[0]+'_Grp'))
    
    bigRingB=cmds.circle(r=25,d=3,s=8,nr=(0,1,0),n='mainB_Ctrl')
    cmds.setAttr(bigRingB[0]+".overrideEnabled",1)
    cmds.setAttr(bigRingB[0]+".overrideColor",13)
    bigRingBSDK=cmds.group(bigRingB[0],n=(bigRingB[0]+'_SDK'))
    bigRingBZero=cmds.group(bigRingBSDK,n=(bigRingB[0]+'_Zero'))
    bigRingBGroup=cmds.group(bigRingBZero,n=(bigRingB[0]+'_Grp'))
    
    cmds.parent(bigRingBGroup,bigRingA[0])
    cmds.parent(flyGroup,bigRingB[0])
    cmds.parent(bigRingAGroup,'Main')
    
    cmds.parent('FitSkeleton',flyCtrl)
    cmds.parent('MotionSystem',flyCtrl)
    cmds.parent('DeformationSystem',flyCtrl)
    
createFlyCtrl()