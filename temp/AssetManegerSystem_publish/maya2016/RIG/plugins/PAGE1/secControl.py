
from PySide import QtCore, QtGui
from PySide.QtCore import Qt
from pymel.core import PyNode
import maya.cmds as cmds
import pymel.all as pm
import maya.mel as mel



class secondCtrl_RIG_TOOL(QtGui.QMainWindow):
    UITitle = 'secondCtrl_RIG_TOOL'
    x = 300
    y = 400
    nowKey = 'normal'

    def createUI(self):
        self.m_DragPosition = self.pos()
        self.resize(self.x, self.y)
        self.move(402, 350)
        self.setWindowFlags(Qt.SubWindow | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setWindowTitle(self.UITitle)

        cWidget = QtGui.QWidget(self)
        cWidget.setAttribute(Qt.WA_StyledBackground)
        cWidget.setStyleSheet(Mstyle.QWidget())
        self.setCentralWidget(cWidget)
        # mian.resize(self.x,self.y)


        mainVB = QtGui.QVBoxLayout(self)
        cWidget.setLayout(mainVB)

        line1box = QtGui.QHBoxLayout(self)
        mainVB.addLayout(line1box)
        # close Btn Set
        Xbtn = QtGui.QPushButton('x')
        Xbtn.setGeometry(0, 0, 0, 0)
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())
        Xbtn.clicked.connect(self.Cl_Ui)
        line1box.addWidget(Xbtn)
        line1box.addStretch(1)
        # TitleLabel
        TitleLab = QtGui.QLabel(self.UITitle)
        # TitleLab.setGeometry(40,5,0,0)
        TitleLab.setFixedHeight(20)
        TitleLab.setFixedWidth(140)
        TitleLab.setStyleSheet(Mstyle.QLabel(fontSize='12px'))
        line1box.addWidget(TitleLab)
        line1box.addStretch(1)

        # line2box = QtGui.QHBoxLayout(self)

        autoGrp = QtGui.QGroupBox('')
        autoGrp.setStyleSheet(Mstyle.QGroupBox(kw='c'))
        mainVB.addWidget(autoGrp)
        groupMB = QtGui.QVBoxLayout()
        autoGrp.setLayout(groupMB)

        groupline1 = QtGui.QHBoxLayout()
        groupMB.addLayout(groupline1)

        self.btnGrp = QtGui.QButtonGroup(autoGrp)

        rad1 = QtGui.QRadioButton(autoGrp)
        rad1.setFixedHeight(20)
        rad1.setFixedWidth(20)
        rad1.setChecked(True)
        self.btnGrp.addButton(rad1, 0)
        groupline1.addWidget(rad1)

        self.radBtn1 = QtGui.QPushButton('normal')
        self.radBtn1.setEnabled(True)
        self.radBtn1.setFixedHeight(20)
        self.radBtn1.setFixedWidth(70)
        self.radBtn1.setStyleSheet(Mstyle.QPushButton(kw='b'))
        groupline1.addWidget(self.radBtn1)

        rad2 = QtGui.QRadioButton(autoGrp)
        rad2.setFixedHeight(20)
        rad2.setFixedWidth(20)
        self.btnGrp.addButton(rad2, 1)
        groupline1.addWidget(rad2)

        self.radBtn2 = QtGui.QPushButton('pick')
        self.radBtn2.setEnabled(False)
        self.radBtn2.setFixedHeight(20)
        self.radBtn2.setFixedWidth(120)
        self.radBtn2.setStyleSheet(Mstyle.QPushButton(kw='off'))
        groupline1.addWidget(self.radBtn2)

        gLine2 = QtGui.QHBoxLayout()

        self.pinBtn = QtGui.QCheckBox('pin')
        self.pinBtn.setChecked(True)
        self.pinBtn.setFixedHeight(20)
        self.pinBtn.setFixedWidth(40)
        self.pinBtn.setStyleSheet(Mstyle.QCheckBox())
        gLine2.addWidget(self.pinBtn)

        self.lwBtn = QtGui.QCheckBox('lock')
        self.lwBtn.setChecked(True)
        self.lwBtn.setFixedHeight(20)
        self.lwBtn.setFixedWidth(45)
        self.lwBtn.setStyleSheet(Mstyle.QCheckBox())
        gLine2.addWidget(self.lwBtn)

        auroCreateBtn = QtGui.QPushButton('auto create')
        auroCreateBtn.setFixedHeight(20)
        auroCreateBtn.setStyleSheet(Mstyle.QPushButton())
        gLine2.addWidget(auroCreateBtn)

        groupMB.addLayout(gLine2)

        fixGrp = QtGui.QGroupBox('fix')
        fixGrp.setStyleSheet(Mstyle.QGroupBox())
        mainVB.addWidget(fixGrp)
        fixMB = QtGui.QVBoxLayout()
        fixGrp.setLayout(fixMB)

        fixline1 = QtGui.QHBoxLayout()
        fixMB.addLayout(fixline1)

        self.namelab = QtGui.QLabel('empty')
        self.namelab.setStyleSheet(Mstyle.QLabel() + 'QLabel {background:transparent;}')
        self.namelab.setFixedHeight(20)
        fixline1.addWidget(self.namelab)

        pickinBtn = QtGui.QPushButton('<<')
        pickinBtn.setStyleSheet(Mstyle.QPushButton())
        pickinBtn.setFixedSize(50, 20)
        fixline1.addWidget(pickinBtn)

        self.tableWid = assetManager_commonRightClickTableWidget()
        self.tableWid.setup()
        self.tableWid.addButton('fix','save.png')
        self.tableWid.setColumnCount(2)
        self.tableWid.setRowCount(1)
        self.tableWid.setHorizontalHeaderLabels(["jnt", "index"])
        self.tableWid.verticalHeader().setVisible(False)
        self.tableWid.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        self.tableWid.setColumnWidth(0, 200)
        # self.tableWid.setStyleSheet(Mstyle.QScrollBar())
        self.tableWid.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWid.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tableWid.horizontalHeader().setStretchLastSection(True)
        self.tableWid.setShowGrid(False)
        self.tableWid.setFrameShape(QtGui.QFrame.NoFrame)
        self.tableWid.setStyleSheet(
            Mstyle.QScrollBar() + "QTableWidget {gridline-color:red;background:rgb(128,128,128);selection-color:red;selection-background-color:lightgray;border:1px solid gray;}"
        )

        self.tableWid.horizontalHeader().setFixedHeight(20)
        self.tableWid.horizontalHeader().setStyleSheet("background-color:rgb(128,128,128);border-radius:6px");

        fixMB.addWidget(self.tableWid)

        self.radBtn1.clicked.connect(self.radBtn1Fn)
        self.radBtn2.clicked.connect(self.radBtn2Fn)
        self.btnGrp.buttonClicked[int].connect(self.btnGrpFn)
        auroCreateBtn.clicked.connect(self.autoCreateFn)
        pickinBtn.clicked.connect(self.pickinFn)
        self.tableWid.choosed.connect(self.choosedFn)
    # --------------button Fns-----------------------------
    def choosedFn(self,data):
        print data
        cr = self.tableWid.currentRow()
        str = self.tableWid.cellWidget(cr,0).currentText()
        id = self.tableWid.item(cr,1).text()
        #print 'make link from ' + str + '.worldInverseMatrix[0] to ' + self.namelab.text() + '.bindPreMatrix[' + id + ']'

        cmds.connectAttr(str + '.worldInverseMatrix[0]', self.namelab.text() + '.bindPreMatrix[' + id + ']', f=1)
        print 'fix over.True'

    def pickinFn(self):
        sel = cmds.ls(sl=1)
        if sel:

            baseSkinCls = mel.eval('findRelatedSkinCluster("' + sel[0] + '")')
            if baseSkinCls:
                self.namelab.setText(baseSkinCls)

                jotSkin = cmds.listConnections(baseSkinCls + '.matrix')
                # self.tableWid
                self.tableWid.setRowCount(len(jotSkin))

                addStyle = ('QComboBox               {border: 1px solid gray;border - radius: 3px;padding: 1px 2px 1px 2px;min - width: 9em;}'
                            'QComboBox::drop - down  {subcontrol - origin: padding;subcontrol - position: topright;height: 20px;}'
                            'QComboBox  QAbstractItemView::item           {height: 25px;}'
                            'QComboBox  QAbstractItemView::item:selected  {background - color: rgba(54, 98, 180);}'

                             )
                for count, i in enumerate(jotSkin):
                    jntAttr = i + '.worldMatrix[0]'
                    jntLink = ''
                    jntLinks = cmds.connectionInfo(jntAttr, destinationFromSource=1)
                    for jl in jntLinks:
                        if baseSkinCls in jl:
                            jntLink = jl
                    spVal = jntLink.split('[')[-1][:-1]


                    theItm = QtGui.QTableWidgetItem()
                    theItm.setText(str(spVal))
                    theItm.setTextAlignment(Qt.AlignCenter)
                    self.tableWid.setItem(count, 1, theItm)

                    parentArray = [i]
                    for c in range(4):
                        getP = cmds.listRelatives(parentArray[-1],p=1)
                        if getP:
                            parentArray.append(getP[0])
                        else:
                            break


                    cellCombo = QtGui.QComboBox()
                    for pa in parentArray:
                        cellCombo.addItem(pa)
                    itemDelegate = QtGui.QStyledItemDelegate()
                    cellCombo.setItemDelegate(itemDelegate)
                    #itemDelegate.setStyleSheet('QAbstractItemView::item{height: 25px;}')
                    cellCombo.setStyleSheet(Mstyle.QComboBox() + addStyle)

                    self.tableWid.setCellWidget(count, 0, cellCombo)

            else:
                self.namelab.setText('empty')

    def autoCreateFn(self):
        lwCheck = False
        if self.lwBtn.checkState() == Qt.CheckState.Checked:
            lwCheck = True

        pinCheck = False
        if self.pinBtn.checkState() == Qt.CheckState.Checked:
            pinCheck = True
        if self.nowKey != 'pick':
            self.makeSeconedControl(matrixType=self.nowKey, isPin=pinCheck, lockWeight=lwCheck)
        else:
            cmds.warning('you must pick a axis node')

    def radBtn1Fn(self):
        sender = self.sender()
        classA = 'normal'
        classB = 'world'

        if sender.text() == classA:
            sender.setText(classB)
            self.nowKey = classB
        elif sender.text() == classB:
            sender.setText(classA)
            self.nowKey = classA

    def radBtn2Fn(self):

        sender = self.sender()
        sel = cmds.ls(sl=1)
        if sel:
            sender.setText(sel[0])
            self.nowKey = sel[0]

    def btnGrpFn(self, val):
        if val == 1:
            self.radBtn1.setEnabled(False)
            self.radBtn1.setStyleSheet(Mstyle.QPushButton(kw='off'))
            self.radBtn2.setEnabled(True)
            self.radBtn2.setStyleSheet(Mstyle.QPushButton(kw='b'))
            self.nowKey = str(self.radBtn2.text())
        elif val == 0:
            self.radBtn2.setEnabled(False)
            self.radBtn2.setStyleSheet(Mstyle.QPushButton(kw='off'))
            self.radBtn1.setEnabled(True)
            self.radBtn1.setStyleSheet(Mstyle.QPushButton(kw='b'))
            self.nowKey = str(self.radBtn1.text())
            # --------------FUNCTIONS-----------------------------

    def makeSeconedControl(self, matrixType='normal', isPin=False, lockWeight=True):
        sel = cmds.ls(sl=1, fl=1)
        filterArray = []
        for i in sel:
            if '.vtx[' in i:
                filterArray.append(i)

        if filterArray:
            for node in filterArray:
                vertNum = node.split('.vtx[')[-1][:-1]
                nodeName = node.split('.')[0]
                mainName = nodeName + '_SecCtrlP' + vertNum

                matrix = []
                if matrixType == 'world':
                    vp = cmds.pointPosition(node, w=1)
                    vp.append(1)
                    matrix = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0] + vp
                    # get world matrix

                elif matrixType == 'normal':
                    vp = cmds.pointPosition(node, w=1)
                    vp.append(1)
                    vm = cmds.polyNormalPerVertex(node, q=1, xyz=1)
                    matrix = vm + vp
                    # get vert matrix
                else:
                    isExt = cmds.objExists(matrixType)
                    if isExt:
                        vp = cmds.pointPosition(node, w=1)
                        vp.append(1)
                        getM = cmds.xform(matrixType, q=1, ws=1, m=1)
                        matrix = getM[:-4] + vp
                        # get object matrix
                    else:
                        print 'matrix not install.return false'
                        return False

                cmds.select(cl=1)
                skinJnt = cmds.joint(n=mainName + '_jnt')
                cmds.xform(skinJnt, ws=1, m=matrix)
                cmds.setAttr(skinJnt + '.sx', 1)
                cmds.setAttr(skinJnt + '.sy', 1)
                cmds.setAttr(skinJnt + '.sz', 1)
                matrix = cmds.xform(skinJnt, ws=1, q=1, m=1)

                crv = cmds.curve(n=mainName + '_crv', d=1,
                                 p=[(0, 1, 0), (0, 0.92388, 0.382683), (0, 0.707107, 0.707107), (0, 0.382683, 0.92388),
                                    (0, 0, 1), (0, -0.382683, 0.92388), (0, -0.707107, 0.707107),
                                    (0, -0.92388, 0.382683), (0, -1, 0), (0, -0.92388, -0.382683),
                                    (0, -0.707107, -0.707107), (0, -0.382683, -0.92388), (0, 0, -1),
                                    (0, 0.382683, -0.92388), (0, 0.707107, -0.707107), (0, 0.92388, -0.382683),
                                    (0, 1, 0), (0.382683, 0.92388, 0), (0.707107, 0.707107, 0), (0.92388, 0.382683, 0),
                                    (1, 0, 0), (0.92388, -0.382683, 0), (0.707107, -0.707107, 0),
                                    (0.382683, -0.92388, 0), (0, -1, 0), (-0.382683, -0.92388, 0),
                                    (-0.707107, -0.707107, 0), (-0.92388, -0.382683, 0), (-1, 0, 0),
                                    (-0.92388, 0.382683, 0), (-0.707107, 0.707107, 0), (-0.382683, 0.92388, 0),
                                    (0, 1, 0), (0, 0.92388, -0.382683), (0, 0.707107, -0.707107),
                                    (0, 0.382683, -0.92388), (0, 0, -1), (-0.382683, 0, -0.92388),
                                    (-0.707107, 0, -0.707107), (-0.92388, 0, -0.382683), (-1, 0, 0),
                                    (-0.92388, 0, 0.382683), (-0.707107, 0, 0.707107), (-0.382683, 0, 0.92388),
                                    (0, 0, 1), (0.382683, 0, 0.92388), (0.707107, 0, 0.707107), (0.92388, 0, 0.382683),
                                    (1, 0, 0), (0.92388, 0, -0.382683), (0.707107, 0, -0.707107),
                                    (0.382683, 0, -0.92388), (0, 0, -1)],
                                 k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                    23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
                                    44, 45, 46, 47, 48, 49, 50, 51, 52])
                ggrp = cmds.group(crv, n=mainName + '_grp')
                dgrp = cmds.group(ggrp, n=mainName + '_sdk')
                zgrp = cmds.group(dgrp, n=mainName + '_zero')

                cmds.xform(zgrp, ws=1, m=matrix)
                cmds.parent(skinJnt, crv)
                # create basic joint and ctrl

                baseSkinCls = mel.eval('findRelatedSkinCluster("' + nodeName + '")')
                if type(baseSkinCls) == list:
                    baseSkinCls = baseSkinCls[0]

                if baseSkinCls == '':
                    baseSkinCls = cmds.skinCluster(skinJnt, nodeName, tsb=True, sm=2)
                else:
                    cmds.skinCluster(baseSkinCls, edit=True, ai=skinJnt, lw=lockWeight)
                    # make skin with new joint.

                dataDict = {}
                jntAttr = skinJnt + '.worldMatrix[0]'
                jntLink = ''
                jntLinks = cmds.connectionInfo(jntAttr, destinationFromSource=1)
                for jl in jntLinks:
                    if baseSkinCls in jl:
                        jntLink = jl
                pGrpAttr = zgrp + '.worldInverseMatrix[0]'
                spVal = jntLink.split('[')
                skinAttr = baseSkinCls + '.bindPreMatrix[' + spVal[-1]
                cmds.connectAttr(pGrpAttr, skinAttr, f=1)
                # inverse sec control matrix.
                if isPin:
                    nameLocator = cmds.createNode('transform', n=mainName + "_rivet")
                    #locArray.append(nameLocator)
                    cmds.select(cl=1)
                    cmds.select(node)
                    cmds.select(nameLocator, add=1)
                    mel.eval(
                        'doCreatePointOnPolyConstraintArgList 2 {   "0" ,"0" ,"0" ,"1" ,"" ,"1" ,"0" ,"0" ,"0" ,"0" };')

                    rvt_crv = cmds.curve(n=mainName + '_rvt_crv', d=1,
                                         p=[(0, 1, 0), (0, 0.92388, 0.382683), (0, 0.707107, 0.707107),
                                            (0, 0.382683, 0.92388), (0, 0, 1), (0, -0.382683, 0.92388),
                                            (0, -0.707107, 0.707107), (0, -0.92388, 0.382683), (0, -1, 0),
                                            (0, -0.92388, -0.382683), (0, -0.707107, -0.707107),
                                            (0, -0.382683, -0.92388), (0, 0, -1), (0, 0.382683, -0.92388),
                                            (0, 0.707107, -0.707107), (0, 0.92388, -0.382683), (0, 1, 0),
                                            (0.382683, 0.92388, 0), (0.707107, 0.707107, 0), (0.92388, 0.382683, 0),
                                            (1, 0, 0), (0.92388, -0.382683, 0), (0.707107, -0.707107, 0),
                                            (0.382683, -0.92388, 0), (0, -1, 0), (-0.382683, -0.92388, 0),
                                            (-0.707107, -0.707107, 0), (-0.92388, -0.382683, 0), (-1, 0, 0),
                                            (-0.92388, 0.382683, 0), (-0.707107, 0.707107, 0), (-0.382683, 0.92388, 0),
                                            (0, 1, 0), (0, 0.92388, -0.382683), (0, 0.707107, -0.707107),
                                            (0, 0.382683, -0.92388), (0, 0, -1), (-0.382683, 0, -0.92388),
                                            (-0.707107, 0, -0.707107), (-0.92388, 0, -0.382683), (-1, 0, 0),
                                            (-0.92388, 0, 0.382683), (-0.707107, 0, 0.707107), (-0.382683, 0, 0.92388),
                                            (0, 0, 1), (0.382683, 0, 0.92388), (0.707107, 0, 0.707107),
                                            (0.92388, 0, 0.382683), (1, 0, 0), (0.92388, 0, -0.382683),
                                            (0.707107, 0, -0.707107), (0.382683, 0, -0.92388), (0, 0, -1)],
                                         k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                                            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
                                            40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52])
                    rvt_ggrp = cmds.group(rvt_crv, n=mainName + '_rvt_grp')
                    rvt_dgrp = cmds.group(rvt_ggrp, n=mainName + '_rvt_sdk')
                    rvt_zgrp = cmds.group(rvt_dgrp, n=mainName + '_rvt_zero')

                    transInvse = cmds.createNode('multiplyDivide', n=crv + '_trans_invse')
                    cmds.connectAttr(rvt_crv + '.translate', transInvse + '.input1', f=1)
                    cmds.setAttr(transInvse + '.input2X', -1)
                    cmds.setAttr(transInvse + '.input2Y', -1)
                    cmds.setAttr(transInvse + '.input2Z', -1)
                    cmds.connectAttr(transInvse + '.output', rvt_dgrp + '.translate', f=1)

                    rotInvse = cmds.createNode('multiplyDivide', n=crv + '_rot_invse')
                    cmds.connectAttr(rvt_crv + '.rotate', rotInvse + '.input1', f=1)
                    cmds.setAttr(rotInvse + '.input2X', -1)
                    cmds.setAttr(rotInvse + '.input2Y', -1)
                    cmds.setAttr(rotInvse + '.input2Z', -1)
                    cmds.connectAttr(rotInvse + '.output', rvt_dgrp + '.rotate', f=1)

                    cmds.xform(rvt_zgrp, ws=1, m=matrix)
                    cmds.parent(rvt_zgrp, nameLocator)

                    cmds.connectAttr(rvt_crv + '.translate', crv + '.translate', f=1)
                    cmds.connectAttr(rvt_crv + '.rotate', crv + '.rotate', f=1)
                    cmds.setAttr(crv + '.visibility', 0, l=1)

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

    def cleanOpenWindow(self, event):
        gmw = getMayaWindow()
        for g in gmw.children():
            if type(self) == type(g):
                g.setParent(None)
                g.deleteLater()

    def closeEvent(self, event):
        self.deleteLater()

    # ------------define swtich--------------------
    def Op_Ui(self):
        self.createUI()
        self.setParent(getMayaWindow())

        self.show()

    def Cl_Ui(self):
        self.close()


secondCtrlUIRT = secondCtrl_RIG_TOOL()
secondCtrlUIRT.Op_Ui()
