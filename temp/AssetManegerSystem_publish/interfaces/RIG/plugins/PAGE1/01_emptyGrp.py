
def emptyGrps():
    if cmds.objExists('model_grp'):
        mgrp='model_grp'
    else:
        mgrp=cmds.group(empty=1,n='model_grp')
        
    if cmds.objExists('doNotTouch_grp'):
        dgrp='doNotTouch_grp'
    else:
        dgrp=cmds.group(empty=1,n='doNotTouch_grp')
        
    if cmds.objExists('rig_grp'):
        rgrp='rig_grp'
    else:
        rgrp=cmds.group(empty=1,n='rig_grp')
        
    if cmds.objExists('c_*_all_grp'):
        maingrp=cmds.ls('c_*_all_grp')[0]
    else:
        maingrp=cmds.group(empty=1,n='c_xxx_all_grp')
    try:
        cmds.parent(mgrp,maingrp)
    except:
        pass
    try:
        cmds.parent(dgrp,maingrp)
    except:
        pass
    try:
        cmds.parent(rgrp,maingrp)
    except:
        pass
        
emptyGrps()