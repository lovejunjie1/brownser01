
def selToVisCtrl():
    swith='visable_ctrl.Model_Type'
    sel=cmds.ls(sl=1)
    for i in sel:
        sp=cmds.listRelatives(i,s=1)
        for s in sp:
            print s
            try:
                cmds.setAttr(s+'.overrideEnabled',1)
                cmds.connectAttr(swith,s+'.overrideDisplayType')
                
            except:
                print 'connected'
                
selToVisCtrl()