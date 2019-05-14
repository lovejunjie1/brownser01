def skinPassSel():
    allobj=cmds.ls(sl=1)
    if(len(allobj)<2):
        cmds.error('please sel two objects.skined first.')
        return False
    else:
        skinO=allobj[0]
        targetO=allobj[1:]
        baseSkinCls=mel.eval('findRelatedSkinCluster("'+skinO+'")')
        if baseSkinCls!='':
            jotSkin=cmds.listConnections(baseSkinCls+'.matrix')
            for t in targetO:
                targetSkinCls=cmds.skinCluster(jotSkin, t,tsb=True,sm=2)
                cmds.copySkinWeights( ss=baseSkinCls, ds=targetSkinCls[0], noMirror=True,influenceAssociation='closestJoint',surfaceAssociation='closestPoint')
                print (skinO+"====skinWeight has passed to===="+t)
        else:
            print 'first object have no skinCluster node.'
            return False
    cmds.select(cl=1)
    return True
    
skinPassSel()