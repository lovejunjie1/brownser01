import maya.cmds as cmds
def createSecondCtrl(newName,number=1):
    zero=''

    for i in range(number):
        sec_name='{}_sel'.format(newName)
        sec_ctrl=cmds.curve(n=sec_name,d=1,p=([-1,1,1],[-1,1,-1],[1,1,-1],[1,1,1],[-1,1,1],[-1,-1,1],[-1,-1,-1],[-1,1,-1],[-1,1,1],[-1,-1,1],[1,-1,1],[1,1,1],[1,1,-1],[1,-1,-1],[1,-1,1],[1,-1,-1],[-1,-1,-1]),k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        #skin_jnt=cmds.joint(n='{}_jnt'.format(newName,str(i)),p=[0,0,0])
        sdk=cmds.group(sec_name,n='{}_sdk'.format(newName))
        mix=cmds.group(sdk,     n='{}_mix'.format(newName))
        zero=cmds.group(mix,     n='{}_pos'.format(newName))
        #cmds.xform(zero,ws=1,t=pos)

    return [zero,mix,sdk,sec_name]

def createMirrorLocator():
    feetRO = cmds.spaceLocator(n = 'feetR_out')
    feetRI = cmds.spaceLocator(n = 'feetR_in')
    
    feetLO = cmds.spaceLocator(n = 'feetL_out')
    feetLI = cmds.spaceLocator(n = 'feetI_in')
    
    mdnodeOutTra = cmds.createNode('multiplyDivide',n='mirrorFeetOutTranslate_multi')
    mdnodeOutRot = cmds.createNode('multiplyDivide',n='mirrorFeetRotation_multi')
    
    cmds.connectAttr(feetRO[0] + '.translate',mdnodeOutTra + '.input1',f=1)
    cmds.connectAttr(mdnodeOutTra + '.output',feetLO[0] + '.translate',f=1)
    cmds.setAttr(mdnodeOutTra + '.input2X',-1)
    cmds.connectAttr(feetRO[0] + '.rotate',mdnodeOutRot + '.input1',f=1)
    cmds.connectAttr(mdnodeOutRot + '.output',feetLO[0] + '.rotate',f=1)
    cmds.setAttr(mdnodeOutRot + '.input2Y',-1)
    cmds.setAttr(mdnodeOutRot + '.input2Z',-1)
    
    
    
    mdnodeInTra = cmds.createNode('multiplyDivide',n='mirrorFeetInTranslate_multi')
    mdnodeInRot = cmds.createNode('multiplyDivide',n='mirrorFeetInRotation_multi')
    
    cmds.connectAttr(feetRI[0] + '.translate',mdnodeInTra + '.input1',f=1)
    cmds.connectAttr(mdnodeInTra + '.output',feetLI[0] + '.translate',f=1)
    cmds.setAttr(mdnodeInTra + '.input2X',-1)
    cmds.connectAttr(feetRI[0] + '.rotate',mdnodeInRot + '.input1',f=1)
    cmds.connectAttr(mdnodeInRot + '.output',feetLI[0] + '.rotate',f=1)
    cmds.setAttr(mdnodeInRot + '.input2Y',-1)
    cmds.setAttr(mdnodeInRot + '.input2Z',-1)
    
    return [feetRO[0],feetRI[0],feetLO[0],feetLI[0],mdnodeOutTra,mdnodeOutRot,mdnodeInTra,mdnodeInRot]

def createSideFeetCtrl(data,Rside = 'RollOffsetHeelLeg_R',Lside = 'RollOffsetHeelLeg_L'):
    tarLayer = Rside
    tarLayerP = cmds.listRelatives(tarLayer,p=1)[0]
    
    tar = data[0]
    tarM = cmds.xform(tar,q=1,ws=1,m=1)
    
    outGrp = createSecondCtrl('outRollOffsetHeelLeg_R')
    cmds.xform(outGrp[0],ws=1,m=tarM)
    cmds.parent(outGrp[0],tarLayerP)
    cmds.parent(tarLayer,outGrp[-1])
    
    tarLayer = outGrp[0]
    tar = data[1]
    tarM = cmds.xform(tar,q=1,ws=1,m=1)
    
    inGrp = createSecondCtrl('inRollOffsetHeelLeg_R')
    cmds.xform(inGrp[0],ws=1,m=tarM)
    cmds.parent(inGrp[0],tarLayerP)
    cmds.parent(tarLayer,inGrp[-1])
    
    #right feet over



    tarLayer = Lside
    tarLayerP = cmds.listRelatives(tarLayer,p=1)[0]
    
    tar = data[2]
    tarM = cmds.xform(tar,q=1,ws=1,m=1)
    
    outGrp = createSecondCtrl('outRollOffsetHeelLeg_L')
    cmds.xform(outGrp[0],ws=1,m=tarM)
    cmds.parent(outGrp[0],tarLayerP)
    cmds.parent(tarLayer,outGrp[-1])
    
    tarLayer = outGrp[0]
    tar = data[3]
    tarM = cmds.xform(tar,q=1,ws=1,m=1)
    
    inGrp = createSecondCtrl('inRollOffsetHeelLeg_L')
    cmds.xform(inGrp[0],ws=1,m=tarM)
    cmds.parent(inGrp[0],tarLayerP)
    cmds.parent(tarLayer,inGrp[-1])
    
    #left feet over
    
    cmds.delete(data)
    
    
#theData = createMirrorLocator()

#createSideFeetCtrl(theData,Lside = 'RollOffsetHeel_L',Rside = 'RollOffsetHeel_R')