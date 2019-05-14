from maya import cmds, OpenMaya


def getUParam(pnt=[], crv=None):
    point = OpenMaya.MPoint(pnt[0], pnt[1], pnt[2])
    curveFn = OpenMaya.MFnNurbsCurve(getDagPath(crv))
    paramUtill = OpenMaya.MScriptUtil()
    paramPtr = paramUtill.asDoublePtr()
    isOnCurve = curveFn.isPointOnCurve(point)
    if isOnCurve == True:
        curveFn.getParamAtPoint(point, paramPtr, OpenMaya.MSpace.kObject)

    else:
        point = curveFn.closestPoint(point, paramPtr, 0.001, OpenMaya.MSpace.kObject)
        curveFn.getParamAtPoint(point, paramPtr, 0.001, OpenMaya.MSpace.kObject)
    param = paramUtill.getDouble(paramPtr)
    return param


def getDagPath(objectName):
    if isinstance(objectName, list) == True:
        oNodeList = []
        for o in objectName:
            selectionList = OpenMaya.MSelectionList()
            selectionList.add(o)
            oNode = OpenMaya.MDagPath()
            selectionList.getDagPath(0, oNode)
            oNodeList.append(oNode)
        return oNodeList
    else:
        selectionList = OpenMaya.MSelectionList()
        selectionList.add(objectName)
        oNode = OpenMaya.MDagPath()
        selectionList.getDagPath(0, oNode)
        return oNode


def getLongestSide(vert):
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0
    minZ = 0
    maxZ = 0

    start = True
    for v in verts:
        nowPos = cmds.pointPosition(v, w=1)
        print nowPos
        if start:
            minX = nowPos[0]
            maxX = nowPos[0]
            minY = nowPos[1]
            maxY = nowPos[1]
            minZ = nowPos[2]
            maxZ = nowPos[2]
            start = False
        else:
            if nowPos[0] < minX:
                minX = nowPos[0]
            if nowPos[0] > maxX:
                maxX = nowPos[0]
            if nowPos[1] < minY:
                minY = nowPos[1]
            if nowPos[1] > maxY:
                maxY = nowPos[1]
            if nowPos[2] < minZ:
                minZ = nowPos[2]
            if nowPos[2] > maxZ:
                maxZ = nowPos[2]

    valX = maxX - minX
    valY = maxY - minY
    valZ = maxZ - minZ
    valArray = [abs(valX), abs(valY), abs(valZ)]
    valArray.sort()

    if valArray[-1] == valX:
        return 0
    if valArray[-1] == valY:
        return 1
    if valArray[-1] == valZ:
        return 2


def getVertsByEdge(sel):
    vertArray = []
    # sel = cmds.ls(sl=1, fl=1)
    if sel:
        if '.e[' in sel[0]:
            name = sel[0].split('.')[0]
            result = cmds.polyInfo(sel, ev=1)
            for r in result:
                rsp = r.split(' ')
                rsp = filter(None, rsp)
                checkA = '{}.vtx[{}]'.format(name, rsp[-2])
                if not (checkA in vertArray):
                    vertArray.append(checkA)
                checkB = '{}.vtx[{}]'.format(name, rsp[-3])
                if not (checkB in vertArray):
                    vertArray.append(checkB)
            return vertArray
        else:
            return False
    else:
        return False


def createSurfaceByEdge(lenth=0.5, sel=[], delCurve=True, delMiddle=True):
    lenth = 0.5
    curveMpos = []
    curveApos = []
    curveBpos = []

    if sel:
        sortKey = getLongestSide(sel)
        for i in sel:
            pos = cmds.xform(i, q=1, ws=1, t=1)
            curveMpos.append(pos)
            moveA = cmds.moveVertexAlongDirection(i, n=lenth)
            posA = cmds.xform(i, q=1, ws=1, t=1)
            curveApos.append(posA)
            moveB = cmds.moveVertexAlongDirection(i, n=-2 * lenth)
            posB = cmds.xform(i, q=1, ws=1, t=1)
            curveBpos.append(posB)
            cmds.xform(i, ws=1, t=pos)
            # reset
        # curveApos.sort()
        sortA = sorted(curveApos, key=lambda x: x[sortKey])
        curveA = cmds.curve(d=3, p=sortA)
        # curveBpos.sort()
        sortB = sorted(curveBpos, key=lambda x: x[sortKey])
        curveB = cmds.curve(d=3, p=sortB)
        # curveMpos.sort()
        sortM = sorted(curveMpos, key=lambda x: x[sortKey])
        curveM = cmds.curve(d=3, p=sortM)
        theSurf = cmds.loft(curveA, curveB, ch=1, u=1, c=0, ar=1, d=3, ss=1, rn=0, po=0, rsn=True)
        cmds.delete(theSurf, ch=1)
        if delCurve:
            cmds.delete(curveA)
            cmds.delete(curveB)
        if delMiddle:
            cmds.delete(curveM)
        return [theSurf[0], curveM]
    else:
        return False


def getSurface(selection):
    if selection:
        returns = False
        if len(selection) == 1:
            shapes = cmds.listRelatives(selection[0], s=1)
            if cmds.objectType(shapes[0]) == 'nurbsSurface':
                returns = selection[0]

        else:
            edgeSel = True
            for i in selection:
                if not ('.e[' in i):
                    edgeSel = False
            if edgeSel:
                verts = getVertsByEdge(selection)
                returns = createSurfaceByEdge(sel=verts)[0]
            else:
                print 'list not clean'
        return returns


def createSecondCtrl(newName, number=1):
    zero = ''

    for i in range(number):
        sec_name = '{}_0{}_sel'.format(newName, str(i))
        sec_ctrl = cmds.curve(n=sec_name, d=1, p=(
        [-1, 1, 1], [-1, 1, -1], [1, 1, -1], [1, 1, 1], [-1, 1, 1], [-1, -1, 1], [-1, -1, -1], [-1, 1, -1], [-1, 1, 1],
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [1, 1, -1], [1, -1, -1], [1, -1, 1], [1, -1, -1], [-1, -1, -1]),
                              k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        skin_jnt = cmds.joint(n='{}_0{}_jnt'.format(newName, str(i)), p=[0, 0, 0])
        sdk = cmds.group(sec_name, n='{}_0{}_sdk'.format(newName, str(i)))
        mix = cmds.group(sdk, n='{}_0{}_mix'.format(newName, str(i)))
        zero = cmds.group(mix, n='{}_0{}_pos'.format(newName, str(i)))
        # cmds.xform(zero,ws=1,t=pos)

    return zero


def createMuscleChain(partName, scaleCtrl, sKey=0):
    # sTemp = createSurfaceByEdge(sel=verts)
    # cmds.parent(sTemp[0], scaleCtrl)
    # cmds.rename(sTemp[0], partName+'_surf')
    # surf = partName+'_surf'

    sel = cmds.ls(sl=1, fl=1)
    surfback = getSurface(sel)
    surf = ''
    shape = ''
    useCurve = False
    if isinstance(surback, list):
        surf = surfback[0]
        shape = cmds.listRelatives(surfback[1], s=1)[0]
        useCurve = True
    else:
        surf = surfback

    surfShape = cmds.listRelatives(surf, s=1)[0]
    storeGrp = cmds.group(empty=1, n=surf + "_point_grp")
    for count, p in enumerate(verts):
        pos = cmds.xform(p, q=1, ws=1, t=1)
        val = round((float(count) * 0.01), 2)
        if useCurve:
            val = getUParam(pos, shape)

        pofName = surf + "_pointOnCurve" + str(count)
        pofNode = cmds.createNode('pointOnSurfaceInfo', n=pofName)
        ptName = surf + "_point" + str(count)
        ctrl = createSecondCtrl(ptName)
        cmds.parent(ctrl, storeGrp)
        # storeGrp.append(ctrl)

        cmds.addAttr(ctrl, ln='position', at='double', min=0, dv=0, keyable=1)
        cmds.connectAttr('%s.worldSpace[0]' % surfShape, '%s.inputSurface' % pofNode, f=1)
        cmds.connectAttr('%s.position' % pofNode, '%s.translate' % ctrl, f=1)
        cmds.connectAttr('%s.position' % ctrl, '%s.parameterU' % pofNode, f=1)
        cmds.setAttr("%s.parameterV" % pofNode, 0.5)
        cmds.setAttr("%s.position" % ctrl, val)

        nameAC = cmds.createNode('aimConstraint', p=ctrl, n='%s_AimConstraint' % ctrl)
        cmds.setAttr(nameAC + '.tg[0].tw', 1)
        cmds.setAttr(nameAC + '.a', 0, 1, 0)
        cmds.setAttr(nameAC + '.u', 0, 0, 1)
        cmds.setAttr(nameAC + '.v', k=0)
        cmds.setAttr(nameAC + '.tx', k=0)
        cmds.setAttr(nameAC + '.ty', k=0)
        cmds.setAttr(nameAC + '.tz', k=0)
        cmds.setAttr(nameAC + '.rx', k=0)
        cmds.setAttr(nameAC + '.ry', k=0)
        cmds.setAttr(nameAC + '.rz', k=0)
        cmds.setAttr(nameAC + '.sx', k=0)
        cmds.setAttr(nameAC + '.sy', k=0)
        cmds.setAttr(nameAC + '.sz', k=0)

        cmds.connectAttr('%s.n' % pofNode, '%s.tg[0].tt' % nameAC)
        cmds.connectAttr('%s.tv' % pofNode, '%s.wu' % nameAC)
        cmds.connectAttr('%s.constraintRotateX' % nameAC, '%s.rotateX' % ctrl)
        cmds.connectAttr('%s.constraintRotateY' % nameAC, '%s.rotateY' % ctrl)
        cmds.connectAttr('%s.constraintRotateZ' % nameAC, '%s.rotateZ' % ctrl)
        cmds.connectAttr((scaleCtrl + ".scale"), (ctrl + ".scale"), f=1)

    if useCurve:
        cmds.delete(surfback[1])


def createSingleCtrl(selNode):
    if cmds.objExists(selNode):
        sec_name = '{}_sel'.format(selNode)
        pos = cmds.xform(selNode, q=1, ws=1, t=1)
        sec_ctrl = cmds.curve(n=sec_name, d=1,
                              p=[(0, 1, 0), (0, 0.92388, 0.382683), (0, 0.707107, 0.707107), (0, 0.382683, 0.92388),
                                 (0, 0, 1), (0, -0.382683, 0.92388), (0, -0.707107, 0.707107), (0, -0.92388, 0.382683),
                                 (0, -1, 0), (0, -0.92388, -0.382683), (0, -0.707107, -0.707107),
                                 (0, -0.382683, -0.92388), (0, 0, -1), (0, 0.382683, -0.92388),
                                 (0, 0.707107, -0.707107), (0, 0.92388, -0.382683), (0, 1, 0), (0.382683, 0.92388, 0),
                                 (0.707107, 0.707107, 0), (0.92388, 0.382683, 0), (1, 0, 0), (0.92388, -0.382683, 0),
                                 (0.707107, -0.707107, 0), (0.382683, -0.92388, 0), (0, -1, 0),
                                 (-0.382683, -0.92388, 0), (-0.707107, -0.707107, 0), (-0.92388, -0.382683, 0),
                                 (-1, 0, 0), (-0.92388, 0.382683, 0), (-0.707107, 0.707107, 0), (-0.382683, 0.92388, 0),
                                 (0, 1, 0), (0, 0.92388, -0.382683), (0, 0.707107, -0.707107), (0, 0.382683, -0.92388),
                                 (0, 0, -1), (-0.382683, 0, -0.92388), (-0.707107, 0, -0.707107),
                                 (-0.92388, 0, -0.382683), (-1, 0, 0), (-0.92388, 0, 0.382683),
                                 (-0.707107, 0, 0.707107), (-0.382683, 0, 0.92388), (0, 0, 1), (0.382683, 0, 0.92388),
                                 (0.707107, 0, 0.707107), (0.92388, 0, 0.382683), (1, 0, 0), (0.92388, 0, -0.382683),
                                 (0.707107, 0, -0.707107), (0.382683, 0, -0.92388), (0, 0, -1)],
                              k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                                 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
                                 46, 47, 48, 49, 50, 51, 52])
        skin_jnt = cmds.joint(n='{}_jnt'.format(selNode), p=[0, 0, 0])
        sdk = cmds.group(sec_name, n='{}_sdk'.format(selNode))
        mix = cmds.group(sdk, n='{}_mix'.format(selNode))
        zero = cmds.group(mix, n='{}_pos'.format(selNode))
        cmds.xform(zero, ws=1, t=pos)

        return zero
    else:
        return False


def mirrorPositionLoc():
    locators = cmds.ls('*_positionLoc')
    for l in locators:
        if l[0] == 'r':
            theCopy = cmds.duplicate(l)[0]
            newname = 'l' + theCopy[1:-1]
            val_x = cmds.getAttr(l + '.tx')
            cmds.setAttr(theCopy + '.tx', val_x * -1)
            cmds.rename(theCopy, newname)


createMuscleChain('r_cheek', 'mainCtrl')
'''
locators = cmds.ls('*_positionLoc')
for i in locators:
    createSingleCtrl(i)
'''