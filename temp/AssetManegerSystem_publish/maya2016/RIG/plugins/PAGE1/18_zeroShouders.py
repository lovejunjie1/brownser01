def aboutValue(iValue):
    rValue=0
    if iValue>45:
        rValue=90
    elif iValue<-45:
        rValue=-90
    else:
        rValue=0
    return rValue

def zeroCtrlRoot(target,targetC,targetP):
    cmds.parent(target,w=1)
    cmds.parent(targetC,w=1)
    
    av=cmds.getAttr(target+'.rx')
    cmds.setAttr(target+'.rx',aboutValue(av))
    
    av=cmds.getAttr(target+'.ry')
    cmds.setAttr(target+'.ry',aboutValue(av))  
      
    av=cmds.getAttr(target+'.rz')
    cmds.setAttr(target+'.rz',aboutValue(av))
    
    targetP2=cmds.listRelatives(target,c=1)[0]
    cmds.parent(targetC,targetP2)
    cmds.parent(target,targetP)
def zeroShoulders():
    data=[
    ['FKExtraScapula1_L','FKXScapula1_L','FKOffsetScapula1_L'],
    ['FKExtraScapula1_R','FKXScapula1_R','FKOffsetScapula1_R'],
    ['FKExtraScapula_L','FKXScapula_L','FKOffsetScapula_L'],
    ['FKExtraScapula_R','FKXScapula_R','FKOffsetScapula_R']
    ]
    for g in data:
        zeroCtrlRoot(g[0],g[1],g[2])
        
zeroShoulders()