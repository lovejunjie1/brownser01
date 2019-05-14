import maya.cmds as cmds
def NameClashDetect(): 
    clashingNames = []
    mayaResolvedName = []
    allDagNodes = cmds.ls(dag = 1)
    for node in allDagNodes: 
        if len(node.split("|")) > 1: 
            mayaResolvedName.append(node) 
            clashingNames.append(node.split("|")[-1]) 
            print "Name clash found: " + node 
            print "UI name: " + clashingNames[-1] 
            print ''
    return mayaResolvedName
    
    
NameClashDetect()
