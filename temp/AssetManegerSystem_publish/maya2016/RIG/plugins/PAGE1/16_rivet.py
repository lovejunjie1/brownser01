import maya.mel as mel

def rivet():    
    type = ''
    data = ''
    namePOSI = ''
    
    check1=cmds.filterExpand(sm=32)
    if check1:
        type = 'polyEdge'
        data = check1
    else:
        check2 = cmds.filterExpand(sm=41)
        if check2:
            type = 'surfacePoint'
            data = check2
        else:
            check3 = cmds.filterExpand(sm=31)
            if check3:
                type = 'polyVtx'
                data = check3
            else:
                print 'nothing selected'
    if type:
        if type == 'polyEdge':
            if len(data)!=2:
                cmds.error('must have two edges was selected')
                return False
            
            nameObject=str(data[0]).split('.')[0]
            e1=str(data[0]).split('.')[1][2:-1]
            e2=str(data[1]).split('.')[1][2:-1]
            
            nameCFME1=cmds.createNode('curveFromMeshEdge',n='rivetCurveFromMeshEdge1')
            cmds.setAttr(nameCFME1+'.ihi',1)
            mel.eval('setAttr ".ei[0]"  '+str(e1)+';')
            
            nameCFME2=cmds.createNode('curveFromMeshEdge',n='rivetCurveFromMeshEdge2')
            cmds.setAttr(nameCFME2+'.ihi',1)
            mel.eval('setAttr ".ei[0]"  '+str(e2)+';')
            
            nameLoft=cmds.createNode('loft',n='rivetLoft1')
            mel.eval('setAttr -s 2 ".ic";')
            cmds.setAttr(nameLoft+'.u',1)
            cmds.setAttr(nameLoft+'.rsn',1)
            
            namePOSI=cmds.createNode('pointOnSurfaceInfo',n='rivetPointOnSurfaceInfo1')
            cmds.setAttr(namePOSI+'.turnOnPercentage',1)
            cmds.setAttr(namePOSI+'.parameterU',0.5)
            cmds.setAttr(namePOSI+'.parameterV',0.5)
            
            cmds.connectAttr((nameLoft + ".os"),(namePOSI + ".is"),f=1)
            cmds.connectAttr((nameCFME1 + ".oc"),(nameLoft + ".ic[0]"),f=1)
            cmds.connectAttr((nameCFME2 + ".oc"),(nameLoft + ".ic[1]"),f=1)
            cmds.connectAttr((nameObject + ".w"),(nameCFME1 + ".im"),f=1)
            cmds.connectAttr((nameObject + ".w"),(nameCFME2 + ".im"),f=1)
                
                
        if type == 'surfacePoint':
            if len(data)>0:
                if len(data)!=1:
                    cmds.error('just need select one point')
                    return False
                nameObject=str(data[0]).split('.')[0]
                u=str(data[0]).split('[')[1][0:-1]
                v=str(data[0]).split('[')[2][0:-1]
                namePOSI=cmds.createNode('pointOnSurfaceInfo',n='rivetPointOnSurfaceInfo1')
                cmds.setAttr(namePOSI+'.turnOnPercentage',0)
                cmds.setAttr(namePOSI+'.parameterU',float(u))
                cmds.setAttr(namePOSI+'.parameterV',float(v))
                cmds.connectAttr(nameObject + ".ws",namePOSI + ".is",f=1)
    
        if type == 'polyVtx':
            locArray = []
            for i in data:
                nameLocator = cmds.createNode('transform',n="rivet1")
                locArray.append(nameLocator)
                cmds.createNode('locator',n=nameLocator+'Shape',p=nameLocator)
                cmds.select(cl=1)
                cmds.select(i)
                cmds.select(nameLocator,add=1)
                mel.eval('doCreatePointOnPolyConstraintArgList 2 {   "0" ,"0" ,"0" ,"1" ,"" ,"1" ,"0" ,"0" ,"0" ,"0" };')
            cmds.select(locArray)
            return locArray
        
        if type in ['surfacePoint','polyEdge']:
                
            nameLocator = cmds.createNode('transform',n="rivet1")
            cmds.createNode('locator',n=nameLocator+'Shape',p=nameLocator)
            nameAC=cmds.createNode('aimConstraint',p=nameLocator,n=nameLocator+"_rivetAimConstraint1")
            cmds.setAttr(nameAC+'.tg[0].tw',1)
            cmds.setAttr(nameAC+'.a',0,1,0,type='double3')
            cmds.setAttr(nameAC+'.u',0,0,1,type='double3')
            cmds.setAttr(nameAC+'.v',k=0)
            cmds.setAttr(nameAC+'.tx',k=0)
            cmds.setAttr(nameAC+'.ty',k=0)
            cmds.setAttr(nameAC+'.tz',k=0)
            cmds.setAttr(nameAC+'.rx',k=0)
            cmds.setAttr(nameAC+'.ry',k=0)
            cmds.setAttr(nameAC+'.rz',k=0)
            cmds.setAttr(nameAC+'.sx',k=0)
            cmds.setAttr(nameAC+'.sy',k=0)
            cmds.setAttr(nameAC+'.sz',k=0)
            
            
            cmds.connectAttr (namePOSI + ".position",nameLocator + ".translate")
            cmds.connectAttr (namePOSI + ".n",nameAC + ".tg[0].tt")
            cmds.connectAttr (namePOSI + ".tv",nameAC + ".wu")
            cmds.connectAttr (nameAC + ".crx",nameLocator + ".rx")
            cmds.connectAttr (nameAC + ".cry",nameLocator + ".ry")
            cmds.connectAttr (nameAC + ".crz",nameLocator + ".rz")
            
            cmds.select(nameLocator,r=1)
            return (nameLocator)

    else:
        pass

rivet()