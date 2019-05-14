allbone=cmds.ls(type='joint')
for ab in allbone:
    cmds.setAttr(ab+".drawStyle",l=0)
    cmds.setAttr(ab+".drawStyle", 0)