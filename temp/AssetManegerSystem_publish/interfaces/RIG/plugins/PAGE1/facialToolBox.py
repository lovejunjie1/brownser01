import sys
from PySide import QtCore, QtGui
from PySide.QtCore import Qt
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin



class mirrorDrivenKey(QtCore.QObject):

    def getNextConnection(self, input, cAttr='output'):
        #print input
        newCheck = input + '.' + cAttr
        #print newCheck
        isExt = cmds.objExists(newCheck)
        if isExt:
            newgets = cmds.connectionInfo(newCheck, destinationFromSource=1)
            return newgets
        else:
            return False

    def getKeyInfomations(self, sAttr):
        newgets = cmds.connectionInfo(sAttr, destinationFromSource=1)

        dictArray = {}

        for i in newgets:
            spi = i.split('.')
            nowNode = spi[0]
            driven = ''
            for t in range(5):
                subGet = self.getNextConnection(nowNode)
                if subGet:
                    nowNode = subGet[0].split('.')[0]
                    if cmds.objectType(nowNode) == 'transform':
                        driven = subGet[0]
                        break

            mirrorKey = False
            spDriven = driven.split('.')
            if spDriven[1] in ['translateX', 'rotateY', 'rotateZ']:
                mirrorKey = True

            timeArray = cmds.keyframe(spi[0], q=True, floatChange=1)
            valueArray = cmds.keyframe(spi[0], q=True, valueChange=1)

            tempDict = {'source': sAttr, 'driver': spi[0] + '.output', 'time': timeArray, 'value': valueArray,
                        'driven': driven, 'isMirror': mirrorKey}

            dictArray.update({driven: tempDict})

        return dictArray

    def mirrorKeyInfomations(self, sAttr):

        keyArray = self.getKeyInfomations(sAttr)
        # get orig key datas

        spSa = sAttr.split('.')
        sideKey = 'l'
        if spSa[1][0] == 'l':
            sideKey = 'r'
        # get mirror side

        mAttr = spSa[0] + '.' + sideKey + spSa[1][1:]
        isExt = cmds.objExists(mAttr)
        # get mirror attribute name and check it exists.

        if isExt:
            for i in keyArray:
                oDrv = keyArray[i]['driver']
                oDrn = keyArray[i]['driven']
                source = keyArray[i]['source']
                spSrc = source.split('.')
                mirSrc = spSrc[0] + '.' + sideKey + spSrc[1][1:]
                mDrv = sideKey + oDrv[1:]
                mDrn = sideKey + oDrn[1:]

                cmds.setDrivenKeyframe(mDrn, cd=mirSrc)
            # recreate the link

            mkeyArray = self.getKeyInfomations(mAttr)
            # get mirror key datas

            for key, itm in keyArray.items():

                sTimArray = itm['time']
                sValArray = itm['value']
                isMirror = itm['isMirror']

                mDrv = mkeyArray[sideKey + key[1:]]['driver'].split('.')[0]
                # name of animCurve at mirror side.

                for i in range(len(sTimArray)):
                    value = float(sValArray[i])
                    if isMirror:
                        value = float(sValArray[i]) * -1
                    cmds.setKeyframe(mDrv, float=float(sTimArray[i]), value=value)
                    # mirror keys.
        else:
            return False

    def copyKeyInfomations(self, sAttr, transKey='RtoL'):
        keyArray = self.getKeyInfomations(sAttr)
        # get orig key datas
        fromKey = ''
        toKey = ''
        if transKey == 'LtoR':
            fromKey = 'l'
            toKey = 'r'
        elif transKey == 'RtoL':
            fromKey = 'r'
            toKey = 'l'
        else:
            pass

        drivenArray = []
        for i in keyArray:
            drn = keyArray[i]['driven']
            # source = keyArray[i]['source']
            if drn[0] == fromKey:
                drv = keyArray[i]['driver']
                drivenArray.append(toKey + drn[1:])
            if drn[0] == toKey:
                drv = keyArray[i]['driver']
                drvNode = drv.split('.')[0]
                cmds.delete(drvNode)


        for drn in drivenArray:
            cmds.setDrivenKeyframe(drn, cd=sAttr, itt='linear', ott='linear')

        rekeyArray = self.getKeyInfomations(sAttr)
        for key, itm in rekeyArray.items():

            if key[0] == fromKey:
                sTimArray = itm['time']
                sValArray = itm['value']
                isMirror = itm['isMirror']
                mDrv = rekeyArray[toKey + key[1:]]['driver'].split('.')[0]
                for i in range(len(sTimArray)):
                    value = float(sValArray[i])
                    if isMirror:
                        value = float(sValArray[i]) * -1
                    cmds.setKeyframe(mDrv, float=float(sTimArray[i]), value=value, itt='linear', ott='linear')

    def breakKeyInfomations(self,sAttr):
        keyArray = self.getKeyInfomations(sAttr)

        for i in keyArray:
            drv = keyArray[i]['driver']
            drvNode = drv.split('.')[0]
            cmds.delete(drvNode)



    def middleMirrorKeyInfomations(self, sAttr):
        keyArray = self.getKeyInfomations(sAttr)
        lArray = []
        rArray = []
        mArray = []
        driverToDeleteArray = []
        for i in keyArray:
            drn = keyArray[i]['driven']
            drv = keyArray[i]['driver']
            driverToDeleteArray.append(drv)
            if drn[0] == 'l':
                lArray.append(drn)
            if drn[0] == 'r':
                rArray.append(drn)
            if drn[0] == 'm':
                mArray.append(drn)

        for delDrv in driverToDeleteArray:
            cmds.delete(delDrv)

        for drn in lArray:
            cmds.setDrivenKeyframe('r' + drn[1:], cd=sAttr)
        for drn in rArray:
            cmds.setDrivenKeyframe('l' + drn[1:], cd=sAttr)
        for drn in mArray:
            cmds.setDrivenKeyframe(drn, cd=sAttr)

        rekeyArray = self.getKeyInfomations(sAttr)

        for key, itm in keyArray.items():
            if key[0] != 'm':
                sTimArray = itm['time']
                sValArray = itm['value']
                isMirror = itm['isMirror']
                inverseKey = 'l'
                if key[0] == 'l':
                    inverseKey = 'r'
                mDrv = rekeyArray[inverseKey + key[1:]]['driver'].split('.')[0]
                for i in range(len(sTimArray)):
                    value = float(sValArray[i])
                    if isMirror:
                        value = float(sValArray[i]) * -1
                    cmds.setKeyframe(mDrv, float=float(sTimArray[i]), value=value, itt='linear', ott='linear')

            if key[0] == 'm':
                sTimArray = itm['time']
                sValArray = itm['value']
                isMirror = itm['isMirror']
                Drv = rekeyArray[key]['driver'].split('.')[0]
                for i in range(len(sTimArray)):
                    value = float(sValArray[i])
                    if isMirror:
                        value = float(sValArray[i]) * -1
                    cmds.setKeyframe(Drv, float=float(sTimArray[i]), value=value, itt='linear', ott='linear')


class maya2016FacialTool_figo(MayaQWidgetDockableMixin, QtGui.QDialog, mirrorDrivenKey):
    titleName = 'maya2016FacialTool_figo'
    widgetHeight = 600
    widgetWidth = 250

    # initPath=''
    def createTab(self):
        self.tabWid = QtGui.QTabWidget(self)
        self.tabWid.setStyleSheet(Mstyle.QTabWidget())
        self.tabWid.resize(self.width(), self.height())
        self.tabWid.setTabPosition(QtGui.QTabWidget.West)
        self.tabWid.setContentsMargins(0, 0, 0, 0)
        self.dialogVbox.addWidget(self.tabWid)
        # ---page0----
        self.createGeneralTab()

        self.tabWid.currentChanged.connect(self.tabWidChangedFn)

    def tabWidChangedFn(self):
        pass

    def createGeneralTab(self):
        self.GWid = QtGui.QWidget()
        self.GWid.setAttribute(Qt.WA_StyledBackground)
        self.GWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        self.GWid.setAttribute(Qt.WA_DeleteOnClose)

        GVbox = QtGui.QVBoxLayout()
        self.GWid.setLayout(GVbox)
        # main defined

        self.sysShow = QtGui.QLabel('unknow system')
        self.sysShow.setFixedHeight(16)
        self.sysShow.setStyleSheet(Mstyle.QLabel(fontSize='16px'))

        sysPick = QtGui.QPushButton('<<')
        sysPick.setFixedHeight(16)
        sysPick.setFixedWidth(40)
        sysPick.setStyleSheet(Mstyle.QPushButton())

        h1box = QtGui.QHBoxLayout()
        h1box.addWidget(self.sysShow)
        h1box.addWidget(sysPick)
        GVbox.addLayout(h1box)
        # tile pick hub.




        radHBox = QtGui.QHBoxLayout()

        rad1 = QtGui.QPushButton('right')
        rad1.setFixedHeight(20)
        rad1.setStyleSheet(Mstyle.QPushButton(kw='radiobutton', bordRad='6px'))
        rad1.setAutoExclusive(True)
        rad1.setCheckable(True)
        rad1.setToolTip('right side')
        rad1.setChecked(True)
        radHBox.addWidget(rad1)

        rad2 = QtGui.QPushButton('middle')
        rad2.setFixedHeight(20)
        rad2.setStyleSheet(Mstyle.QPushButton(kw='radiobutton', bordRad='6px'))
        rad2.setAutoExclusive(True)
        rad2.setCheckable(True)
        rad2.setToolTip('middle side')
        radHBox.addWidget(rad2)

        rad3 = QtGui.QPushButton('left')
        rad3.setFixedHeight(20)
        rad3.setStyleSheet(Mstyle.QPushButton(kw='radiobutton', bordRad='6px'))
        rad3.setAutoExclusive(True)
        rad3.setCheckable(True)
        rad3.setToolTip('left side')
        radHBox.addWidget(rad3)

        self.radGrp = QtGui.QButtonGroup()
        self.radGrp.setExclusive(True)
        self.radGrp.addButton(rad1, 0)
        self.radGrp.addButton(rad2, 1)
        self.radGrp.addButton(rad3, 2)

        GVbox.addLayout(radHBox)
        # side sel rad group

        sliderHbox = QtGui.QHBoxLayout()

        self.slider = QtGui.QSlider(Qt.Horizontal)
        self.slider.setRange(0, 1000)
        # self.slider.setStyleSheet()
        sliderHbox.addWidget(self.slider)

        zeroAllBtn = QtGui.QPushButton('zAll')
        zeroAllBtn.setFixedSize(42, 20)
        zeroAllBtn.setStyleSheet(Mstyle.QPushButton())
        sliderHbox.addWidget(zeroAllBtn)

        GVbox.addLayout(sliderHbox)

        self.listTable = assetManager_commonRightClickTableWidget()
        self.listTable.setup()
        self.listTable.addButton('driver','save.png')
        self.listTable.addButton('driven','save.png')
        self.listTable.setColumnCount(2)
        self.listTable.setRowCount(1)
        self.listTable.setColumnWidth(0, 30)
        # self.listTable.setColumnWidth(1, self.width()-95)
        self.listTable.setHorizontalHeaderLabels(["No.", "Name"])
        self.listTable.verticalHeader().setVisible(False)
        self.listTable.setEditTriggers(QtGui.QTableWidget.NoEditTriggers)
        # self.listTable.setStyleSheet(Mstyle.QScrollBar())
        self.listTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.listTable.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        # self.listTable.setSpan(0,0,3,1) # combie (start x,start y,hor 3,ver 1)
        self.listTable.horizontalHeader().setStretchLastSection(True)
        # table_widget->horizontalHeader()->setResizeMode(QHeaderView::Stretch); strech every cell.
        self.listTable.setShowGrid(False)
        self.listTable.setFrameShape(QtGui.QFrame.NoFrame)
        self.listTable.setStyleSheet(
            Mstyle.QScrollBar() + "QTableWidget {gridline-color:red;background:rgb(128,128,128);selection-color:red;selection-background-color:lightgray;border:1px solid gray;}"
        )

        self.listTable.horizontalHeader().setFixedHeight(20)
        self.listTable.horizontalHeader().setStyleSheet("background-color:rgb(128,128,128);border-radius:6px");

        GVbox.addWidget(self.listTable)

        mirrorBtn = QtGui.QPushButton('mirror')
        mirrorBtn.setFixedHeight(20)
        mirrorBtn.setStyleSheet(Mstyle.QPushButton())
        GVbox.addWidget(mirrorBtn)

        breakBtn = QtGui.QPushButton('break')
        breakBtn.setFixedHeight(20)
        breakBtn.setStyleSheet(Mstyle.QPushButton())
        #GVbox.addWidget(breakBtn)

        copyBox = QtGui.QHBoxLayout()
        GVbox.addLayout(copyBox)

        self.LtoRBtn = QtGui.QPushButton('L to R')
        self.LtoRBtn.setFixedHeight(20)
        self.LtoRBtn.setStyleSheet(Mstyle.QPushButton())
        self.LtoRBtn.setVisible(False)

        self.RtoLBtn = QtGui.QPushButton('R to L')
        self.RtoLBtn.setFixedHeight(20)
        self.RtoLBtn.setStyleSheet(Mstyle.QPushButton())
        self.RtoLBtn.setVisible(False)

        copyBox.addWidget(self.LtoRBtn)
        copyBox.addWidget(self.RtoLBtn)

        refreshBtn = QtGui.QPushButton('refresh')
        refreshBtn.setFixedHeight(20)
        refreshBtn.setStyleSheet(Mstyle.QPushButton(kw='b'))
        GVbox.addWidget(refreshBtn)

        self.tabWid.addTab(self.GWid, 'general')
        sysPick.clicked.connect(self.sysPickFn)
        self.radGrp.buttonClicked[int].connect(self.radGrpFn)
        self.slider.sliderMoved.connect(self.sliderFn)
        zeroAllBtn.clicked.connect(self.zeroAllBtnFn)
        refreshBtn.clicked.connect(self.refreshFn)

        mirrorBtn.clicked.connect(self.mirrorFn)
        breakBtn.clicked.connect(self.breakFn)
        self.RtoLBtn.clicked.connect(self.copyKeyToOtherSideFn)
        self.LtoRBtn.clicked.connect(self.copyKeyToOtherSideFn)
        self.listTable.choosed.connect(self.tableChoosedFn)
        self.listTable.currentCellChanged.connect(self.tableCellChangedFn)

    def copyKeyToOtherSideFn(self):

        sender = self.sender()
        mData = self.listTable.selectedItems()

        if mData:
            mainName = self.sysShow.text() + '.'
            for i in mData:
                data = i.text()
                if not (data.isdigit()):
                    if sender.text() == 'L to R':
                        self.copyKeyInfomations(mainName + data, transKey='LtoR')
                    else:
                        self.copyKeyInfomations(mainName + data, transKey='RtoL')

            mel.eval('print "copy finish"')

    def tableCellChangedFn(self, x, y, z, b):

        cRow = self.listTable.currentRow()
        cItm = self.listTable.item(cRow, 1)
        if cItm and cRow:
            mainsys = str(self.sysShow.text()) + '.' + cItm.text()
            if cmds.objExists(mainsys):
                val = cmds.getAttr(mainsys)
                self.slider.setValue(val * 100.0)

    def tableChoosedFn(self, data):
        mainsys = str(self.sysShow.text())
        if data == 'driver':
            cmds.select(cl=1)
            cmds.select(mainsys)

        elif data == 'driven':
            reArray = []
            for i in self.listTable.selectedItems():
                theTxt = i.text()
                if not (theTxt.isdigit()):
                    reArray.append(theTxt)
        drivenData = []
        for i in reArray:
            newgets = cmds.connectionInfo(mainsys + '.' + i, destinationFromSource=1)
            if newgets:
                for g in newgets:
                    driven = ''
                    nowNode = g.split('.')[0]
                    for t in range(5):
                        # print nowNode
                        subGet = self.getNextConnection(nowNode)
                        if subGet:
                            nowNode = subGet[0].split('.')[0]
                            if cmds.objectType(nowNode) == 'transform':
                                driven = subGet[0]
                                break
                    spDriven = driven.split('.')
                    if not (spDriven[0] in drivenData):
                        drivenData.append(spDriven[0])
        #print drivenData
        cmds.select(cl=1)
        for i in drivenData:
            if i:
                cmds.select(i, add=1)
            # drivenData.append(g)
            # print drivenData

    def breakFn(self):
        mData = self.listTable.selectedItems()

        if mData:
            dataArray = []
            mainName = self.sysShow.text() + '.'
            for i in mData:
                data = i.text()
                if not (data.isdigit()):
                    dataArray.append(mainName+data)

            listStr = '\n'.join(dataArray)
            ans = QtGui.QMessageBox.warning(self,
                                    'double check 1/2',
                                    'this is >> not << a undo button\nif you wanna break link,it >> can\'t << be come back \n' + listStr,
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if ans == QtGui.QMessageBox.Yes:
                reply = QtGui.QMessageBox.warning(self,
                                                'double check 2/2',
                                                'do you relly wanna >> break << the link?\n' + listStr,
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
                    for da in dataArray:
                        self.breakKeyInfomations(da)
                    self.refreshFn()
        pass

    def mirrorFn(self):

        mData = self.listTable.selectedItems()

        if mData:
            checkID = self.radGrp.checkedId()
            mainName = self.sysShow.text() + '.'
            for i in mData:
                data = i.text()
                if not (data.isdigit()):
                    if checkID == 1:
                        self.middleMirrorKeyInfomations(mainName + data)
                    else:
                        self.mirrorKeyInfomations(mainName + data)

                mel.eval('print "mirror finish"')
        pass
        # self.mirrorKeyInfomations

    def refreshFn(self):
        checkID = self.radGrp.checkedId()
        if checkID == 0:
            self.fillTableFn(self.rArray, mirror='l')
        if checkID == 1:
            self.fillTableFn(self.mArray, mirror='')
        if checkID == 2:
            self.fillTableFn(self.lArray, mirror='r')

    def zeroAllBtnFn(self):

        if self.sysShow.text() != 'unknow system':
            count = self.listTable.rowCount()
            mainName = self.sysShow.text() + '.'
            self.slider.setValue(0)

            checkID = self.radGrp.checkedId()
            theArray = []
            if checkID == 0:
                theArray = self.rArray
            if checkID == 1:
                theArray = self.mArray
            if checkID == 2:
                theArray = self.lArray

            for i in theArray:
                try:
                    cmds.setAttr(mainName + i, 0)
                except:
                    pass
        pass

    def sliderFn(self, val):
        mData = self.listTable.selectedItems()

        if mData:
            mainName = self.sysShow.text() + '.'
            for i in mData:
                data = i.text()
                if not (data.isdigit()):
                    cmds.setAttr(mainName + data, val / 100.0)
        pass

    def radGrpFn(self, val):
        if self.sysShow.text() != 'unknow system':
            if val == 0:
                self.fillTableFn(self.rArray, mirror='l')
                self.RtoLBtn.setVisible(False)
                self.LtoRBtn.setVisible(False)
            if val == 1:
                self.fillTableFn(self.mArray, mirror='')
                self.RtoLBtn.setVisible(True)
                self.LtoRBtn.setVisible(True)
            if val == 2:
                self.fillTableFn(self.lArray, mirror='r')
                self.RtoLBtn.setVisible(False)
                self.LtoRBtn.setVisible(False)

        pass

    def sysPickFn(self):
        sel = cmds.ls(sl=1)
        if len(sel) == 1:
            self.sysName = str(sel[0])

            Attrs = cmds.listAttr(self.sysName, ud=1)
            self.lArray = []
            self.rArray = []
            self.mArray = []
            self.oArray = []
            if Attrs:
                self.sysShow.setText(self.sysName)
                for i in Attrs:
                    if i[0] == 'l':
                        self.lArray.append(i)
                    elif i[0] == 'r':
                        self.rArray.append(i)
                    elif i[0] == 'c':
                        self.mArray.append(i)
                    else:
                        self.oArray.append(i)

                self.refreshFn()
            else:
                cmds.warning('no user defined attributes in selected node.')
        else:
            cmds.warning('you must just select drivSys only')

    def fillTableFn(self, arr, mirror=''):
        if arr:
            self.listTable.clear()
            self.listTable.setHorizontalHeaderLabels(["No.", "Name"])
            self.listTable.setRowCount(len(arr))
            okBrushFore = QtGui.QBrush(QtGui.QColor(40, 93, 126))
            noBrushBack = QtGui.QBrush(QtGui.QColor(86, 86, 86))
            noBrushFore = QtGui.QBrush(QtGui.QColor(55, 55, 55))
            for count, i in enumerate(arr):

                theItm = QtGui.QTableWidgetItem()
                theItm.setText(str(count))
                theItm.setTextAlignment(Qt.AlignCenter)
                self.listTable.setItem(count, 0, theItm)

                testItm = QtGui.QTableWidgetItem()
                testItm.setText(i)
                testItm.setTextAlignment(Qt.AlignCenter)
                self.listTable.setItem(count, 1, testItm)

                if mirror:
                    mirArr = self.lArray
                    if mirror == 'r':
                        mirArr = self.rArray
                    otherSide = mirror + i[1:]
                    if not (otherSide in mirArr):
                        theItm.setBackground(noBrushBack)
                        theItm.setForeground(noBrushFore)

                        testItm.setBackground(noBrushBack)
                        testItm.setForeground(noBrushFore)

                checkData = cmds.connectionInfo((self.sysName + '.' + i), destinationFromSource=1)
                if checkData:
                    theItm.setForeground(okBrushFore)
                    testItm.setForeground(okBrushFore)
        pass

    def createUI(self):
        self.dialogVbox = QtGui.QVBoxLayout()
        self.setLayout(self.dialogVbox)

        self.createTab()

    def dockCloseEventTriggered(self):
        """
        Handle stuff when the dock is closed
        """
        self.close()
        self.deleteLater()

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

    def resizeEvent(self, event):
        self.tabWid.resize(self.width(), self.height())

    def Op_Ui(self):
        self.cleanOpenWindow()
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle(self.titleName)
        self.setMinimumWidth(self.widgetWidth)
        self.createUI()
        self.show()
        self.setDockableParameters(dockable=True, floating=False, area='left')
        self.raise_()


m2016FasiTool = maya2016FacialTool_figo()
m2016FasiTool.Op_Ui()
# gg.close()
# dir(QtGui.QMainWindow)



























