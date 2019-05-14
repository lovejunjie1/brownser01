import sys, shiboken, math
from maya.OpenMaya import MTransformationMatrix
from PySide import QtCore, QtGui
from PySide.QtCore import Qt
from pymel.core import PyNode
import pymel.core as pm
import maya.cmds as cmds
from pymel.core.datatypes import Vector, Matrix, Point


class mopImportUI_TOOL(QtGui.QMainWindow):
    dt = {
        'FKGlobalScapulaSDK_R': ['FKGlobalScapulaSDK_R', 0],
        'FKShoulder_R': ['FKExtraShoulder_R', 0],
        'FKElbow_R': ['FKElbow_R', 0],
        'FKWrist_R': ['FKWrist_R', 0],

        'FKGlobalScapulaSDK_L': ['FKGlobalScapulaSDK_L', 0],
        'FKShoulder_L': ['FKExtraShoulder_L', 0],
        'FKElbow_L': ['FKElbow_L', 0],
        'FKWrist_L': ['FKWrist_L', 0],

        'FKNeck_M': ['FKNeck_M', 0],
        'FKHead_M': ['FKHead_M', 0],
        'FKChest_M': ['FKChest_M', 0],
        'FKSpine2_M': ['FKSpine2_M', 0],
        'FKSpine1_M': ['FKSpine1_M', 0],
        'FKRoot_M': ['FKRoot_M', 0],

        'RootX_M': ['RootX_M', 2],

        'FKHip_L': ['FKExtraHip_L', 0],
        'FKKnee_L': ['FKKnee_L', 0],
        'FKAnkle_L': ['FKAnkle_L', 0],

        'FKHip_R': ['FKExtraHip_R', 0],
        'FKKnee_R': ['FKKnee_R', 0],
        'FKAnkle_R': ['FKAnkle_R', 0]}

    titleName = 'mopImportUI_TOOL'
    x = 300
    y = 400
    lastPath = ''
    cNs = ''
    prefix = ''
    timeMin = 0
    timeMax = 100

    def cleanOpenWindow(self):
        gmw = getMayaWindow()
        for g in gmw.children():
            try:
                Tit = g.windowTitle()
                if Tit == self.titleName:
                    g.close()
                    g.setParent(None)
            except:
                pass

    def CreateUI(self):
        self.cleanOpenWindow()

        # ------Style Set----------------------------

        # super(mopImportUI_TOOL, self).__init__(parent)
        self.m_DragPosition = self.pos()
        self.resize(self.x, self.y)
        self.move(402, 350)
        self.setWindowFlags(Qt.SubWindow | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setStyleSheet(Mstyle.QWidget())
        self.setWindowTitle(self.titleName)

        self.timeMin = int(cmds.playbackOptions(q=1, min=1))
        self.timeMax = int(cmds.playbackOptions(q=1, max=1))

        mian = QtGui.QWidget(self)
        mian.resize(self.x, self.y)
        # close Btn Set
        Xbtn = QtGui.QPushButton('x', mian)
        Xbtn.setGeometry(0, 0, 0, 0)
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())
        Xbtn.clicked.connect(self.Cl_Ui)

        # TitleLabel
        TitleLab = QtGui.QLabel(self.titleName, mian)
        TitleLab.setGeometry(40, 5, 0, 0)
        TitleLab.setFixedHeight(20)
        TitleLab.setFixedWidth(140)
        TitleLab.setStyleSheet(Mstyle.QLabel(fontSize='12px'))

        # cha sel
        self.chaLab = QtGui.QGroupBox('empty charactor', mian)
        self.chaLab.setGeometry(10, 25, 0, 0)
        self.chaLab.setFixedHeight(50)
        self.chaLab.setFixedWidth(280)
        self.chaLab.setStyleSheet(Mstyle.QGroupBox())

        self.BtnA1 = QtGui.QPushButton('ImportCharact', self.chaLab)
        self.BtnA1.setGeometry(10, 20, 0, 0)
        self.BtnA1.setEnabled(True)
        self.BtnA1.setFixedHeight(20)
        self.BtnA1.setFixedWidth(120)
        self.BtnA1.setStyleSheet(Mstyle.QPushButton())

        self.BtnA3 = QtGui.QPushButton('Sel Charactor', self.chaLab)
        self.BtnA3.setGeometry(150, 20, 0, 0)
        self.BtnA3.setEnabled(True)
        self.BtnA3.setFixedHeight(20)
        self.BtnA3.setFixedWidth(120)
        self.BtnA3.setStyleSheet(Mstyle.QPushButton(kw='b'))

        # data sel
        self.dataLab = QtGui.QGroupBox('empty data', mian)
        self.dataLab.setGeometry(10, 85, 0, 0)
        self.dataLab.setFixedHeight(50)
        self.dataLab.setFixedWidth(280)
        self.dataLab.setStyleSheet(Mstyle.QGroupBox())

        self.BtnA2 = QtGui.QPushButton('ImportFBXdata', self.dataLab)
        self.BtnA2.setGeometry(10, 20, 0, 0)
        self.BtnA2.setEnabled(True)
        self.BtnA2.setFixedHeight(20)
        self.BtnA2.setFixedWidth(120)
        self.BtnA2.setStyleSheet(Mstyle.QPushButton())

        self.BtnA4 = QtGui.QPushButton('sel FBXdata', self.dataLab)
        self.BtnA4.setGeometry(150, 20, 0, 0)
        self.BtnA4.setEnabled(True)
        self.BtnA4.setFixedHeight(20)
        self.BtnA4.setFixedWidth(120)
        self.BtnA4.setStyleSheet(Mstyle.QPushButton(kw='b'))

        # time set
        timeLab = QtGui.QGroupBox('set time range', mian)
        timeLab.setGeometry(10, 140, 0, 0)
        timeLab.setFixedHeight(50)
        timeLab.setFixedWidth(280)
        timeLab.setStyleSheet(Mstyle.QGroupBox())

        self.radBtn1 = QtGui.QRadioButton('TimeRange', timeLab)
        self.radBtn1.setGeometry(10, 20, 0, 0)
        self.radBtn1.setFixedHeight(20)
        self.radBtn1.setFixedWidth(75)
        self.radBtn1.setChecked(True)
        self.radBtn1.setStyleSheet(Mstyle.QRadioButton())

        self.radBtn2 = QtGui.QRadioButton('Set', timeLab)
        self.radBtn2.setGeometry(90, 20, 0, 0)
        self.radBtn2.setFixedHeight(20)
        self.radBtn2.setFixedWidth(65)
        self.radBtn2.setStyleSheet(Mstyle.QRadioButton(kw='b'))

        self.spBox1 = QtGui.QSpinBox(timeLab)
        self.spBox1.setGeometry(130, 20, 0, 0)
        self.spBox1.setEnabled(False)
        self.spBox1.setFixedHeight(20)
        self.spBox1.setFixedWidth(45)
        self.spBox1.setRange(0, 10000)
        self.spBox1.setSuffix('f')
        self.spBox1.setStyleSheet(Mstyle.QSpinBox())

        self.tLab = QtGui.QLabel('to', timeLab)
        self.tLab.setGeometry(185, 20, 0, 0)
        self.tLab.setFixedHeight(20)
        self.tLab.setFixedWidth(65)

        self.spBox2 = QtGui.QSpinBox(timeLab)
        self.spBox2.setGeometry(200, 20, 0, 0)
        self.spBox2.setEnabled(False)
        self.spBox2.setFixedHeight(20)
        self.spBox2.setFixedWidth(65)
        self.spBox2.setSuffix('f')
        self.spBox2.setRange(0, 10000)
        self.spBox2.setValue(100)
        self.spBox2.setStyleSheet(Mstyle.QSpinBox())

        # link and break
        linkLab = QtGui.QGroupBox('link and break data', mian)
        linkLab.setGeometry(10, 195, 0, 0)
        linkLab.setFixedHeight(50)
        linkLab.setFixedWidth(280)
        linkLab.setStyleSheet(Mstyle.QGroupBox())

        self.BtnA5 = QtGui.QPushButton('linkData', linkLab)
        self.BtnA5.setGeometry(10, 20, 0, 0)
        self.BtnA5.setEnabled(True)
        self.BtnA5.setFixedHeight(20)
        self.BtnA5.setFixedWidth(120)
        self.BtnA5.setStyleSheet(Mstyle.QPushButton())

        self.BtnA8 = QtGui.QPushButton('linkBreak', linkLab)
        self.BtnA8.setGeometry(150, 20, 0, 0)
        self.BtnA8.setEnabled(True)
        self.BtnA8.setFixedHeight(20)
        self.BtnA8.setFixedWidth(120)
        self.BtnA8.setStyleSheet(Mstyle.QPushButton(kw='off'))

        # record and bake
        bakeLab = QtGui.QGroupBox('record and bake data', mian)
        bakeLab.setGeometry(10, 250, 0, 0)
        bakeLab.setFixedHeight(50)
        bakeLab.setFixedWidth(280)
        bakeLab.setStyleSheet(Mstyle.QGroupBox())

        self.BtnA6 = QtGui.QPushButton('recordAnim', bakeLab)
        self.BtnA6.setGeometry(10, 20, 0, 0)
        self.BtnA6.setEnabled(True)
        self.BtnA6.setFixedHeight(20)
        self.BtnA6.setFixedWidth(120)
        self.BtnA6.setStyleSheet(Mstyle.QPushButton())

        self.BtnA7 = QtGui.QPushButton('bakeAnim', bakeLab)
        self.BtnA7.setGeometry(150, 20, 0, 0)
        self.BtnA7.setEnabled(True)
        self.BtnA7.setFixedHeight(20)
        self.BtnA7.setFixedWidth(120)
        self.BtnA7.setStyleSheet(Mstyle.QPushButton())

        # link and break
        IKFKLab = QtGui.QGroupBox('Fk/Ik frames', mian)
        IKFKLab.setGeometry(10, 305, 0, 0)
        IKFKLab.setFixedHeight(50)
        IKFKLab.setFixedWidth(280)
        IKFKLab.setStyleSheet(Mstyle.QGroupBox())

        self.BtnA8 = QtGui.QPushButton('FK->IK', IKFKLab)
        self.BtnA8.setGeometry(10, 20, 0, 0)
        self.BtnA8.setEnabled(True)
        self.BtnA8.setFixedHeight(20)
        self.BtnA8.setFixedWidth(120)
        self.BtnA8.setStyleSheet(Mstyle.QPushButton())

        self.BtnA9 = QtGui.QPushButton('IK->FK', IKFKLab)
        self.BtnA9.setGeometry(150, 20, 0, 0)
        self.BtnA9.setEnabled(True)
        self.BtnA9.setFixedHeight(20)
        self.BtnA9.setFixedWidth(120)
        self.BtnA9.setStyleSheet(Mstyle.QPushButton(kw='b'))

        self.BtnA1.clicked.connect(self.BtnA1Fn)
        self.BtnA2.clicked.connect(self.BtnA2Fn)
        self.BtnA3.clicked.connect(self.BtnA3Fn)
        self.BtnA4.clicked.connect(self.BtnA4Fn)
        self.BtnA5.clicked.connect(self.BtnA5Fn)
        self.BtnA6.clicked.connect(self.BtnA6Fn)
        self.BtnA7.clicked.connect(self.BtnA7Fn)
        self.radBtn1.clicked.connect(self.RadioChanged)
        self.radBtn2.clicked.connect(self.RadioChanged)
        self.BtnA8.clicked.connect(self.BtnA8Fn)
        self.BtnA9.clicked.connect(self.BtnA9Fn)

    # --------------button Fns-----------------------------


    def BtnA1Fn(self):
        QFD = QtGui.QFileDialog(self)
        # QFD.setFilter(("Maya Files(*.ma);"))
        if self.lastPath == '':
            self.lastPath = 'D://'
        theFile = QFD.getOpenFileName(self, 'open Charactor', self.lastPath, ("Ma Files( *.ma )"))

        print theFile

        if theFile[0]:
            self.lastPath = theFile[0]
            path = theFile[0]
            Nspace = 'cha_' + path.split('/')[-1].split('_')[2].lower()
            # print Nspace
            cmds.file(path, i=True, ignoreVersion=1, namespace=Nspace)
            # cmds.file(theFile[0],open=True,f=1)
        else:
            print 'cancel import charactor'

    def BtnA2Fn(self):
        QFD = QtGui.QFileDialog(self)
        # QFD.setFilter(("Maya Files(*.ma);"))
        if self.lastPath == '':
            self.lastPath = 'D://'
        theFile = QFD.getOpenFileName(self, 'import Fbx', self.lastPath, ("FBX data( *.fbx )"))
        if theFile[0]:
            self.lastPath = theFile[0]
            path = theFile[0]
            Nspace = 'data_' + path.split('/')[-1].split('_')[2].lower()
            # print Nspace
            cmds.file(path, r=True, ignoreVersion=1, namespace=Nspace, options="fbx")
            # cmds.file(theFile[0],r=True,ignoreVersion=1,namespace=Nspace,options="fbx")
            # cmds.file(theFile[0],r=True,ignoreVersion=1,namespace="motionData:",options="fbx") cmds.file(theFile[0],open=True,f=1)
        else:
            print 'cancel import Fbx'

    def BtnA3Fn(self):
        sel = pm.ls(sl=1)[0]
        rootName = str(sel.root())
        self.chaLab.setTitle(rootName)
        chaRoot = PyNode(self.chaLab.title())
        self.cNs = chaRoot.namespace()

    def BtnA4Fn(self):
        selection = pm.ls(sl=1)
        if selection:
            dataRoot = PyNode(selection[0])
            dNs = dataRoot.namespace()
            rootTemp = pm.ls(dNs + '*_Reference')
            if rootTemp:
                sel = pm.ls(sl=1)[0]
                rootName = str(sel.root())
                self.dataLab.setTitle(rootName)
                rootLoc = rootTemp[0]
                # self.prefix=''
                if dNs:
                    self.prefix = dNs + (rootLoc.split(dNs)[1].split('_')[0]) + '_'
                else:
                    self.prefix = rootLoc.split('_')[0] + '_'
            else:
                print 'no data in scence'

    def BtnA5Fn(self):
        # link mop to rigs
        if self.chaLab.title() == 'empty charactor' or self.dataLab.title() == 'empty data':
            return False
            print 'nothing login'
        else:
            rotCons = pm.ls('*:*_tempRotCons')
            if rotCons:
                cmds.delete(rotCons)
            posCons = pm.ls('*:*_tempPosCons')
            if posCons:
                cmds.delete(posCons)

            chaRoot = PyNode(self.chaLab.title())
            self.cNs = chaRoot.namespace()
            cmds.setAttr(self.cNs + "FKIKLeg_L.FKIKBlend", 0)
            cmds.setAttr(self.cNs + "FKIKLeg_R.FKIKBlend", 0)
            cmds.setAttr(self.cNs + "FKIKArm_L.FKIKBlend", 0)
            cmds.setAttr(self.cNs + "FKIKArm_R.FKIKBlend", 0)
            cmds.setAttr(self.cNs + "FKIKSpine_M.FKIKBlend", 0)
            self.standableAttr(nameSpace=self.cNs)
            try:
                self.shoulderGrps(Ns=self.cNs)
            except:
                pass

            dataRoot = PyNode(self.dataLab.title())
            dNs = dataRoot.namespace()
            rootLoc = pm.ls(dNs + '*_Reference')[0]
            # self.prefix=''
            if dNs:
                self.prefix = dNs + (rootLoc.split(dNs)[1].split('_')[0]) + '_'
            else:
                self.prefix = rootLoc.split('_')[0] + '_'

            rotArray = [
                ['FKHead_M', 'Head'],
                ['FKNeck_M', 'Neck'],
                ['FKChest_M', 'Spine2'],
                ['FKSpine2_M', 'Spine1'],
                ['FKSpine1_M', 'Spine'],
                ['FKRoot_M', 'Hips'],
                ['FKExtraHip_L', 'LeftUpLeg'],
                ['FKAnkle_L', 'LeftFoot'],
                ['FKExtraHip_R', 'RightUpLeg'],
                ['FKAnkle_R', 'RightFoot'],
                ['FKGlobalScapulaSDK_L', 'LeftShoulder'],
                ['FKExtraShoulder_L', 'LeftArm'],
                ['FKWrist_L', 'LeftHand'],
                ['FKGlobalScapulaSDK_R', 'RightShoulder'],
                ['FKExtraShoulder_R', 'RightArm'],
                ['FKWrist_R', 'RightHand']]
            for ra in rotArray:
                cmds.orientConstraint(self.prefix + ra[1], self.cNs + ra[0], n=self.cNs + ra[0] + '_tempRotCons')
            cmds.pointConstraint(self.prefix + 'Hips', self.cNs + 'RootX_M', n=self.cNs + 'RootX_M_tempPosCons')

            conArray = []
            for ra in rotArray:
                if cmds.objExists(self.cNs + ra[0] + '_tempRotCons'):
                    conArray.append(self.cNs + ra[0] + '_tempRotCons')
            if cmds.objExists(self.cNs + 'RootX_M_tempPosCons'):
                conArray.append(self.cNs + 'RootX_M_tempPosCons')

            cmds.currentTime(-1, e=1)

            self.singleAxisRot(self.prefix, ['LeftUpLeg', 'LeftLeg', 'LeftFoot'], self.cNs + 'FKKnee_L.rz', isInvert=-1)
            self.singleAxisRot(self.prefix, ['RightUpLeg', 'RightLeg', 'RightFoot'], self.cNs + 'FKKnee_R.rz',
                               isInvert=-1)
            self.singleAxisRot(self.prefix, ['RightArm', 'RightForeArm', 'RightHand'], self.cNs + 'FKElbow_R.rz',
                               isInvert=1)
            self.singleAxisRot(self.prefix, ['LeftArm', 'LeftForeArm', 'LeftHand'], self.cNs + 'FKElbow_L.rz',
                               isInvert=1)

            dataArray = [
                [[self.prefix + 'RightForeArm', self.prefix + 'RightArm', self.prefix + 'RightHand'],
                 [self.cNs + 'FKElbow_R', self.cNs + 'FKShoulder_R', self.cNs + 'FKWrist_R'],
                 self.cNs + 'ArmR_Xaxis_Plus'],
                [[self.prefix + 'LeftForeArm', self.prefix + 'LeftArm', self.prefix + 'LeftHand'],
                 [self.cNs + 'FKElbow_L', self.cNs + 'FKShoulder_L', self.cNs + 'FKWrist_L'],
                 self.cNs + 'ArmL_Xaxis_Plus'],
                [[self.prefix + 'RightLeg', self.prefix + 'RightUpLeg', self.prefix + 'RightFoot'],
                 [self.cNs + 'FKKnee_R', self.cNs + 'FKHip_R', self.cNs + 'FKAnkle_R'], self.cNs + 'LegR_Xaxis_Plus'],
                [[self.prefix + 'LeftLeg', self.prefix + 'LeftUpLeg', self.prefix + 'LeftFoot'],
                 [self.cNs + 'FKKnee_L', self.cNs + 'FKHip_L', self.cNs + 'FKAnkle_L'], self.cNs + 'LegL_Xaxis_Plus']
            ]

            for da in dataArray:
                pm.disconnectAttr(da[1][1] + '.rotateX')
                cmds.setAttr(da[1][1] + '.rotateX', 0)

            for da in dataArray:
                if not (cmds.objExists(da[-1])):
                    cmds.group(empty=1, n=da[-1])

            self.getTimeRange()
            timeMin = self.timeMin
            timeMax = self.timeMax
            for i in range(timeMin, timeMax):
                cmds.currentTime(i, e=1)
                for da in dataArray:
                    # nowRot=cmds.getAttr('angleBetween2.angle')
                    ov = Matrix(self.getMatrixFrom3Points(da[0]))
                    dv = Matrix(self.getMatrixFrom3Points(da[1]))
                    offsetMatrix = ov * dv.inverse()
                    gg = MTransformationMatrix(offsetMatrix)
                    rotAngle = math.degrees(gg.rotation().asEulerRotation().x)
                    # rotAngle=cmds.angleBetween(v1=(ov[4],ov[5],ov[6]),v2=(dv[4],dv[5],dv[6]))[-1]
                    if da[-1] == self.cNs + 'ArmL_Xaxis_Plus' or da[-1] == self.cNs + 'LegL_Xaxis_Plus':
                        cmds.setAttr(da[-1] + '.rx', -rotAngle)
                    else:
                        cmds.setAttr(da[-1] + '.rx', rotAngle)
                    cmds.setKeyframe(da[-1] + '.rx')
            for da in dataArray:
                cmds.connectAttr(da[-1] + '.rotateX', da[1][1] + '.rotateX', f=1)

    def BtnA6Fn(self):
        if self.cNs:
            self.mop_bakeAnimateToLoc(nameSpace=self.cNs)
        else:
            print 'no namespace select'

    def BtnA7Fn(self):
        dt = self.dt
        self.mop_disconnectLink(nameSpace=self.cNs)
        self.getTimeRange()
        timeMin = self.timeMin
        timeMax = self.timeMax

        for t in range(timeMin, timeMax):
            cmds.currentTime(t, e=1)
            for i in dt.keys():
                if dt[i][-1] == 0 or dt[i][-1] == 1:
                    self.dataBake0(i, nameSpace=self.cNs)
                elif dt[i][-1] == 2:
                    self.dataBake1(i, nameSpace=self.cNs)
                else:
                    pass
            self.fixShoulderX('ArmR_Xaxis_Plus', 'FKShoulder_R', nameSpace=self.cNs)
            self.fixShoulderX('ArmL_Xaxis_Plus', 'FKShoulder_L', nameSpace=self.cNs)
            self.fixShoulderX('LegR_Xaxis_Plus', 'FKHip_R', nameSpace=self.cNs)
            self.fixShoulderX('LegL_Xaxis_Plus', 'FKHip_L', nameSpace=self.cNs)

        tempLoc = pm.ls('*:*Bakedata*')
        cmds.delete(tempLoc)
        tempAxisPlus = pm.ls('*:*_Xaxis_Plus')
        cmds.delete(tempAxisPlus)

    def spBox1Fn(self):
        self.timeMin = self.spBox1.value()

    def spBox2Fn(self):
        self.timeMax = self.spBox2.value()

    def RadioChanged(self):
        state = (self.sender().text())
        if state == 'TimeRange':
            self.spBox1.setEnabled(False)
            self.spBox2.setEnabled(False)
            self.getTimeRange()
        elif state == 'Set':
            self.spBox1.setEnabled(True)
            self.spBox2.setEnabled(True)
            self.getTimeRange()

    def BtnA8Fn(self):
        print self.cNs
        self.FKtoIK(cNs=self.cNs)

    def BtnA9Fn(self):
        self.IKtoFK(cNs=self.cNs)

    # --------------FUNCTIONS-----------------------------
    def getTimeRange(self):
        if self.radBtn1.isChecked():
            self.timeMin = int(cmds.playbackOptions(q=1, min=1))
            self.timeMax = int(cmds.playbackOptions(q=1, max=1))
        if self.radBtn2.isChecked():
            self.timeMin = self.spBox1.value()
            self.timeMax = self.spBox2.value()

    def FKtoIK(self, cNs=''):
        # FKXOffsetElbow_L
        # FKElbow_L
        dt = {
            cNs + 'FKIKArm_L': [['FKXOffsetElbow_L', 'AlignIKToWrist_L'], ['IKArm_L', 'PoleArm_L']],
            cNs + 'FKIKArm_R': [['FKXOffsetElbow_R', 'AlignIKToWrist_R'], ['IKArm_R', 'PoleArm_R']],
            cNs + 'FKIKLeg_L': [['FKXOffsetKnee_L', 'AlignIKToAnkle_L'], ['IKLeg_L', 'PoleLeg_L']],
            cNs + 'FKIKLeg_R': [['FKXOffsetKnee_R', 'AlignIKToAnkle_R'], ['IKLeg_R', 'PoleLeg_R']]}
        opreateDt = {}
        sel = cmds.ls(sl=1)
        for s in sel:
            if s in dt.keys():
                opreateDt.update({s: dt[s]})

        if not (opreateDt.keys()):
            print 'no Arm//Leg IKFK switch in selected'
        else:
            for od, data in opreateDt.items():
                ikP = cNs + data[1][1]
                cmds.setAttr(ikP + '.follow', 0)
                cmds.setAttr(ikP + '.lock', 0)
            self.getTimeRange()
            timeMin = self.timeMin
            timeMax = self.timeMax
            for t in range(timeMin, timeMax):
                cmds.currentTime(t, e=1)
                for k, d in opreateDt.items():
                    worldT = pm.xform(cNs + d[0][0], q=1, ws=1, t=1)
                    pm.xform(cNs + d[1][1], ws=1, t=worldT)
                    cmds.setKeyframe([cNs + d[1][1] + '.tx', cNs + d[1][1] + '.ty', cNs + d[1][1] + '.tz'])

                    worldM = pm.xform(cNs + d[0][1], q=1, ws=1, m=1)
                    pm.xform(cNs + d[1][0], ws=1, m=worldM)
                    cmds.setKeyframe(
                        [cNs + d[1][0] + '.tx', cNs + d[1][0] + '.ty', cNs + d[1][0] + '.tz', cNs + d[1][0] + '.rx',
                         cNs + d[1][0] + '.ry', cNs + d[1][0] + '.rz'])

            for od in opreateDt.keys():
                cmds.setAttr(od + '.FKIKBlend', 10)

    def IKtoFK(self, cNs=''):
        dt = {
            cNs + 'FKIKArm_L': [['FKShoulder_L', 'FKElbow_L', 'FKWrist_L'],
                                ['IKXShoulder_L', 'IKXElbow_L', 'IKXWrist_L']],
            cNs + 'FKIKArm_R': [['FKShoulder_R', 'FKElbow_R', 'FKWrist_R'],
                                ['IKXShoulder_R', 'IKXElbow_R', 'IKXWrist_R']],
            cNs + 'FKIKLeg_L': [['FKHip_L', 'FKKnee_L', 'FKAnkle_L'], ['IKXHip_L', 'IKXKnee_L', 'IKXAnkle_L']],
            cNs + 'FKIKLeg_R': [['FKHip_R', 'FKKnee_R', 'FKAnkle_R'], ['IKXHip_R', 'IKXKnee_R', 'IKXAnkle_R']]}
        opreateDt = {}
        sel = cmds.ls(sl=1)
        for s in sel:
            if s in dt.keys():
                opreateDt.update({s: dt[s]})
        if not (opreateDt.keys()):
            print 'no Arm//Leg IKFK switch in selected'
        else:
            self.getTimeRange()
            timeMin = self.timeMin
            timeMax = self.timeMax
            for t in range(timeMin, timeMax):
                cmds.currentTime(t, e=1)
                for k, d in opreateDt.items():
                    fkSRot = pm.xform(cNs + d[1][0], q=1, ws=1, ro=1)
                    fkMRot = pm.xform(cNs + d[1][1], q=1, ws=1, ro=1)
                    fkERot = pm.xform(cNs + d[1][2], q=1, ws=1, ro=1)

                    cmds.xform(cNs + d[0][0], ws=1, ro=fkSRot)
                    pm.xform(cNs + d[0][1], ws=1, ro=fkMRot)
                    pm.xform(cNs + d[0][2], ws=1, ro=fkERot)

                    cmds.setKeyframe([cNs + d[0][0] + '.rx', cNs + d[0][0] + '.ry', cNs + d[0][0] + '.rz',
                                      cNs + d[0][1] + '.rx', cNs + d[0][1] + '.ry', cNs + d[0][1] + '.rz',
                                      cNs + d[0][2] + '.rx', cNs + d[0][2] + '.ry', cNs + d[0][2] + '.rz'])

            for od in opreateDt.keys():
                cmds.setAttr(od + '.FKIKBlend', 0)

    def singleAxisRot(self, chaname, sourceArray, targetAttr, isInvert=1):
        # chaname='LittleGirl'
        # sourceArray=['_LeftUpLeg','_LeftLeg','_LeftFoot']
        # targetAttr='FKKnee_L.rz'
        StartArray = cmds.ls(chaname + sourceArray[0])
        MidArray = cmds.ls(chaname + sourceArray[1])
        EndArray = cmds.ls(chaname + sourceArray[2])
        if len(StartArray) != 1 or len(MidArray) != 1 or len(EndArray) != 1:
            cmds.warning('same data in file')
        else:
            Startnode = StartArray[0]
            Midnode = MidArray[0]
            Endnode = EndArray[0]

            deposStart = cmds.shadingNode('decomposeMatrix', asUtility=1, n=chaname + '_deposStart')
            deposMid = cmds.shadingNode('decomposeMatrix', asUtility=1, n=chaname + '_deposMid')
            deposEnd = cmds.shadingNode('decomposeMatrix', asUtility=1, n=chaname + '_deposEnd')

            vector1 = cmds.shadingNode('plusMinusAverage', asUtility=1, n=chaname + '_vector1')
            vector2 = cmds.shadingNode('plusMinusAverage', asUtility=1, n=chaname + '_vector2')
            cmds.setAttr(vector1 + '.operation', 2)
            cmds.setAttr(vector2 + '.operation', 2)

            angleB = cmds.shadingNode('angleBetween', asUtility=1, n=chaname + '_angleB')
            finVal = cmds.shadingNode('plusMinusAverage', asUtility=1, n=chaname + '_finVal')
            rotVal = cmds.shadingNode('multiplyDivide', asUtility=1, n=chaname + '_rotVal')
            cmds.setAttr(rotVal + '.input2X', isInvert)  # if need invert value.set -1.

            cmds.connectAttr(Startnode + '.worldMatrix', deposStart + '.inputMatrix', f=1)
            cmds.connectAttr(Midnode + '.worldMatrix', deposMid + '.inputMatrix', f=1)
            cmds.connectAttr(Endnode + '.worldMatrix', deposEnd + '.inputMatrix', f=1)

            cmds.connectAttr(deposStart + '.outputTranslate', vector1 + '.input3D[0]', f=1)
            cmds.connectAttr(deposMid + '.outputTranslate', vector1 + '.input3D[1]', f=1)
            cmds.connectAttr(deposEnd + '.outputTranslate', vector2 + '.input3D[0]', f=1)
            cmds.connectAttr(deposMid + '.outputTranslate', vector2 + '.input3D[1]', f=1)

            cmds.connectAttr(vector1 + '.output3D', angleB + '.vector1', f=1)
            cmds.connectAttr(vector2 + '.output3D', angleB + '.vector2', f=1)

            valueTemp = cmds.getAttr(angleB + '.angle')
            cmds.setAttr(finVal + '.input1D[0]', valueTemp)
            cmds.setAttr(finVal + '.operation', 2)
            cmds.connectAttr(angleB + '.angle', finVal + '.input1D[1]', f=1)

            cmds.connectAttr(finVal + '.output1D', rotVal + '.input1X', f=1)
            cmds.connectAttr(rotVal + '.output.outputX', targetAttr, f=1)

    def standableAttr(self, nameSpace=''):
        PyNode(nameSpace + 'IKLeg_L').legAim.set(0)
        PyNode(nameSpace + 'IKLeg_R').legAim.set(0)

    def shoulderGrps(self, Ns=''):
        shoulderLParent = PyNode(Ns + 'FKExtraScapula_L').firstParent()
        shoulderRParent = PyNode(Ns + 'FKExtraScapula_R').firstParent()
        dataArray = [
            [Ns + 'FKGlobalScapulaZero_L', shoulderLParent, Ns + 'FKGlobalScapulaSDK_L'],
            [Ns + 'FKGlobalScapulaSDK_L', Ns + 'FKGlobalScapulaZero_L', Ns + 'FKExtraScapula_L'],
            [Ns + 'FKGlobalScapula1Zero_L', Ns + 'LegAimScapula1_L', Ns + 'FKGlobalScapula1SDK_L'],
            [Ns + 'FKGlobalScapula1SDK_L', Ns + 'FKGlobalScapula1Zero_L', Ns + 'FKExtraScapula1_L'],

            [Ns + 'FKGlobalScapulaZero_R', shoulderRParent, Ns + 'FKGlobalScapulaSDK_R'],
            [Ns + 'FKGlobalScapulaSDK_R', Ns + 'FKGlobalScapulaZero_R', Ns + 'FKExtraScapula_R'],
            [Ns + 'FKGlobalScapula1Zero_R', Ns + 'LegAimScapula1_R', Ns + 'FKGlobalScapula1SDK_R'],
            [Ns + 'FKGlobalScapula1SDK_R', Ns + 'FKGlobalScapula1Zero_R', Ns + 'FKExtraScapula1_R']
        ]

        for i in dataArray:
            isNodeExist = cmds.objExists(i[0])

            if isNodeExist:
                # check parent state
                tNode = PyNode(i[0])
                check = tNode.getParent()
                if check != (i[0]):
                    tNode.setParent(i[1])
                    tNode.setTranslation([0, 0, 0])
                    tNode.setRotation([0, 0, 0])
                    tNode.setScale([1, 1, 1])
            else:
                tNode = pm.group(empty=1, n=i[0])
                tNode.setParent(i[1])
                tNode.setTranslation([0, 0, 0])
                tNode.setRotation([0, 0, 0])
                tNode.setScale([1, 1, 1])

            isExist = cmds.objExists(i[2])
            if isExist:
                tNode = PyNode(i[2])
                check = tNode.getParent()
                if check != (i[0]):
                    tNode.setParent(i[0])

    def dataTransFunction0(self, Key, DataArray, sn=''):
        target = sn + DataArray[0]
        Key = sn + Key
        Ax = cmds.getAttr(target + '.rx')
        Ay = cmds.getAttr(target + '.ry')
        Az = cmds.getAttr(target + '.rz')
        cmds.setAttr(Key + '_Bakedata.rx', Ax)
        cmds.setAttr(Key + '_Bakedata.ry', Ay)
        cmds.setAttr(Key + '_Bakedata.rz', Az)
        cmds.setKeyframe([Key + '_Bakedata.rx', Key + '_Bakedata.ry', Key + '_Bakedata.rz'])
        # return localRot

    def dataTransFunction2(self, Key, DataArray, sn=''):
        Target = sn + DataArray[0]
        Key = sn + Key
        Tx = cmds.getAttr(Target + '.tx')
        Ty = cmds.getAttr(Target + '.ty')
        Tz = cmds.getAttr(Target + '.tz')
        cmds.setAttr(Key + '_Bakedata.tx', Tx)
        cmds.setAttr(Key + '_Bakedata.ty', Ty)
        cmds.setAttr(Key + '_Bakedata.tz', Tz)
        cmds.setKeyframe([Key + '_Bakedata.tx', Key + '_Bakedata.ty', Key + '_Bakedata.tz'])
        return [Tx, Ty, Tz]

    def dataTransFunction3(self, Key, DataArray, sn=''):
        Key = sn + Key
        root = ''
        for i in DataArray[0:-1]:
            # print i
            if 'Zero' in i:
                root = PyNode(sn + i)

        nood = PyNode(Key)

        calcuMatrix = root.transformationMatrix() * nood.transformationMatrix().inverse()

        mmix = MTransformationMatrix(calcuMatrix)
        Tx = math.degrees(mmix.rotation().asEulerRotation().x)
        Ty = math.degrees(mmix.rotation().asEulerRotation().y)
        Tz = math.degrees(mmix.rotation().asEulerRotation().z)

        cmds.setAttr(Key + '_Bakedata.rx', Tx)
        cmds.setAttr(Key + '_Bakedata.ry', Ty)
        cmds.setAttr(Key + '_Bakedata.rz', Tz)
        cmds.setKeyframe([Key + '_Bakedata.rx', Key + '_Bakedata.ry', Key + '_Bakedata.rz'])
        return [Tx, Ty, Tz]

    def mop_bakeAnimateToLoc(self, nameSpace=''):
        bakeGrp = ''
        if cmds.objExists(nameSpace + 'Bakedata_Grp'):
            bakeGrp = PyNode(nameSpace + 'Bakedata_Grp')
        else:
            bakeGrp = PyNode(cmds.group(em=1, n=nameSpace + 'Bakedata_Grp'))

        for i in self.dt.keys():
            if cmds.objExists(nameSpace + i + '_Bakedata'):
                tempNode = PyNode(nameSpace + i + '_Bakedata')
                tempNode.setParent(bakeGrp)
            else:
                tempNode = PyNode(cmds.group(em=1, n=nameSpace + i + '_Bakedata'))
                tempNode.setParent(bakeGrp)
        self.getTimeRange()
        timeMin = self.timeMin
        timeMax = self.timeMax

        for t in range(timeMin, timeMax):
            cmds.currentTime(t, e=1)
            dt = self.dt
            for i in dt.keys():
                if dt[i][-1] == 0:
                    self.dataTransFunction0(i, dt[i], sn=nameSpace)
                elif dt[i][-1] == 1:
                    pass
                elif dt[i][-1] == 2:
                    self.dataTransFunction2(i, dt[i], sn=nameSpace)
                elif dt[i][-1] == 3:
                    self.dataTransFunction3(i, dt[i], sn=nameSpace)

    def mop_disconnectLink(self, nameSpace=''):
        rotCons = pm.ls('*:*_tempRotCons')
        cmds.delete(rotCons)
        posCons = pm.ls('*:*_tempPosCons')
        cmds.delete(posCons)

        loopArray = self.dt.keys()
        loopArray = loopArray + ['FKExtraHip_L', 'FKExtraHip_R', 'FKExtraShoulder_L', 'FKExtraShoulder_R']

        for d in loopArray:
            pm.disconnectAttr(nameSpace + d + '.rx')
            cmds.setAttr(nameSpace + d + '.rx', 0)
            pm.disconnectAttr(nameSpace + d + '.ry')
            cmds.setAttr(nameSpace + d + '.ry', 0)
            pm.disconnectAttr(nameSpace + d + '.rz')
            cmds.setAttr(nameSpace + d + '.rz', 0)

        cmds.xform(nameSpace + 'RootX_M', os=1, t=[0, 0, 0])

    # -------------bake-----------------------

    def dataBake0(self, Key, nameSpace=''):
        Key = nameSpace + Key
        Ax = cmds.getAttr(Key + '_Bakedata.rx')
        Ay = cmds.getAttr(Key + '_Bakedata.ry')
        Az = cmds.getAttr(Key + '_Bakedata.rz')
        cmds.setAttr(Key + '.rx', Ax)
        cmds.setAttr(Key + '.ry', Ay)
        cmds.setAttr(Key + '.rz', Az)
        cmds.setKeyframe([Key + '.rx', Key + '.ry', Key + '.rz'])
        return True

    def dataBake1(self, Key, nameSpace=''):
        Key = nameSpace + Key
        Ax = cmds.getAttr(Key + '_Bakedata.tx')
        Ay = cmds.getAttr(Key + '_Bakedata.ty')
        Az = cmds.getAttr(Key + '_Bakedata.tz')
        cmds.setAttr(Key + '.tx', Ax)
        cmds.setAttr(Key + '.ty', Ay)
        cmds.setAttr(Key + '.tz', Az)
        cmds.setKeyframe([Key + '.tx', Key + '.ty', Key + '.tz'])
        return True

    def fixShoulderX(self, frNode, toNode, nameSpace=''):
        # frNode='ArmR_Xaxis_Plus'
        # toNode='FKShoulder_R'
        frNode = nameSpace + frNode
        toNode = nameSpace + toNode
        Ax = cmds.getAttr(frNode + '.rx')
        cmds.rotate(Ax, 0, 0, toNode, r=1, os=1, fo=1, xyz=1)
        cmds.setKeyframe([toNode + '.rx', toNode + '.ry', toNode + '.rz'])
        return Ax

    def getMatrixFrom3Points(self, tArray):
        pa = Point(cmds.xform(tArray[0], q=1, ws=1, t=1))
        pb = Point(cmds.xform(tArray[1], q=1, ws=1, t=1))
        pc = Point(cmds.xform(tArray[2], q=1, ws=1, t=1))

        va = Vector(pb - pa)
        va.normalize()
        tvb = Vector(pc - pa)
        tvb.normalize()
        vc = va.cross(tvb).normal()
        vb = va.cross(vc).normal()
        return [va[0], va[1], va[2], 0, vb[0], vb[1], vb[2], 0, vc[0], vc[1], vc[2], 0, 0, 0, 0, 1]

        # --------------edit event-----------------------------

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

    def closeEvent(self, event):
        self.deleteLater()

    # ------------define swtich--------------------

    def Op_Ui(self):
        self.CreateUI()
        self.setParent(getMayaWindow())
        self.show()

    def Cl_Ui(self):
        self.close()


mopImportRT = mopImportUI_TOOL()
mopImportRT.Op_Ui()
# mopImportRT.Cl_Ui()
