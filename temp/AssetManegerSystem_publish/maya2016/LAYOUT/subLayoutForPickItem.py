from PySide import QtCore, QtGui
from PySide.QtCore import Qt
import maya.cmds as cmds
import maya.mel as mel


class selectCharactor_ANIM_TOOL(QtGui.QMainWindow):
    addClicked = QtCore.Signal(list)
    titleName = 'selectCharactor_ANIM_TOOL'
    x = 300
    y = 400
    serverPath = 'W:\\project\\PIG'
    def createUI(self):
        self.assetPath = self.serverPath + '\\asset'

        self.m_DragPosition = self.pos()
        self.resize(self.x, self.y)
        self.move(402, 350)
        self.setWindowFlags(Qt.SubWindow | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setWindowTitle(self.titleName)

        cWidget = QtGui.QWidget(self)
        cWidget.setAttribute(Qt.WA_StyledBackground)
        cWidget.setStyleSheet(Mstyle.QWidget())
        self.setCentralWidget(cWidget)

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
        TitleLab = QtGui.QLabel(self.titleName)
        TitleLab.setFixedHeight(20)
        TitleLab.setFixedWidth(140)
        TitleLab.setStyleSheet(Mstyle.QLabel(fontSize='12px'))
        line1box.addWidget(TitleLab)
        line1box.addStretch(1)

        # new widget add in this part
        comboBoxStyle = ('QComboBox{border:1px solid gray;border-radius:8px;padding-left:4px;;min-width:6em;}'
                         'QComboBox:on {padding-top:3px;padding-left:4px;}'   
                         'QComboBox::drop-down {subcontrol-origin: padding;subcontrol-position: top right;width:15px;'
                         'border-left-width:1px;border-left-color: darkgray;border-left-style: solid;/* just a single line */'
                         'border-top-right-radius:3px;border-bottom-right-radius:3px;}'
                         'QComboBox::down-arrow {image: url(D:/rig_manager_box/icon/writer_icon/arrowDown.png);}'
                         'QComboBox::down-arrow:on {top:1px;left:1px;}'
                         'QComboBox QAbstractItemView{border:1px solid darkgray;selection-background-color: lightgray;}'
                         'QScrollBar {border: 0px solid grey;background: #89d962;width: 8px;}'
                         'QScrollBar::handle {background: #89d962;min-height: 20px;border-radius:4px;}'
                         )
        pathHbox = QtGui.QHBoxLayout()
        self.sectionA = QtGui.QComboBox()
        self.sectionA.setStyleSheet(comboBoxStyle)
        self.sectionA.setToolTip('department')
        self.sectionA.addItem('RIG')
        self.sectionA.addItem('MODEL')

        self.sectionB = QtGui.QComboBox()
        self.sectionB.setStyleSheet(comboBoxStyle)
        self.sectionB.setToolTip('type')
        #self.sectionB.setEnabled(False)
        self.sectionB.addItem('Char')
        self.sectionB.addItem('Prop')
        self.sectionB.addItem('Env')


        self.sectionC = QtGui.QComboBox()
        self.sectionC.setStyleSheet(comboBoxStyle)
        self.sectionC.setToolTip('version')
        #self.sectionC.setEnabled(False)
        self.sectionC.addItem('low')
        self.sectionC.addItem('high')

        pathHbox.addWidget(self.sectionA)
        pathHbox.addWidget(self.sectionB)
        pathHbox.addWidget(self.sectionC)
        mainVB.addLayout(pathHbox)

        comLineE = QtGui.QLineEdit()
        comLineE.setText('search bar')
        comLineE.setAlignment(Qt.AlignHCenter)
        comLineE.setFixedHeight(24)
        comLineE.setStyleSheet(Mstyle.QLineEdit(fontSize='14px', bordRad='12px', kw='d', lang='c'))
        mainVB.addWidget(comLineE)

        self.assetTable = QtGui.QTableWidget()
        self.assetTable.setColumnCount(2)
        self.assetTable.setRowCount(1)
        self.assetTable.setHorizontalHeaderLabels(['picture', 'infomation'])
        self.assetTable.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.assetTable.verticalHeader().setDefaultSectionSize(80)
        mainVB.addWidget(self.assetTable)


        arHbox = QtGui.QHBoxLayout()
        addBtn = QtGui.QPushButton('add')
        addBtn.setFixedHeight(16)
        addBtn.setFixedWidth(86)
        addBtn.setStyleSheet(Mstyle.QPushButton(kw='on'))

        arHbox.addStretch(1)
        arHbox.addWidget(addBtn)
        mainVB.addLayout(arHbox)


    # --------------functions-----------------------------

        addBtn.clicked.connect(self.addFn)
        comLineE.textChanged.connect(self.searchFn)
        self.sectionA.currentIndexChanged.connect(self.itemchange)
        self.sectionB.currentIndexChanged.connect(self.itemchange)
        self.sectionC.currentIndexChanged.connect(self.itemchange)
    # --------------edit event-----------------------------

    def addFn(self):
        cRow = self.assetTable.currentRow()
        cellWidget = self.assetTable.cellWidget(cRow,1)
        toolTip = cellWidget.toolTip()
        #print toolTip
        self.addClicked.emit(toolTip)
        self.Cl_Ui()

    def searchFn(self,strs):
        nowCount = self.assetTable.rowCount()
        showArray = []
        for i in range(nowCount):
            cellWidget = self.assetTable.cellWidget(i,1)
            toolTip = cellWidget.toolTip()
            bName = os.path.basename(toolTip)
            if strs.lower() in bName.lower():
                showArray.append(True)
            else:
                showArray.append(False)
        for count,sa in enumerate(showArray):
            if sa:
                self.assetTable.showRow(count)
            else:
                self.assetTable.hideRow(count)

    def fillTableFn(self,path,versionName):
        files = os.listdir(self.finalPath)
        if files:

            '''
            for f in range(count):
                cmv = QtGui.QVBoxLayout()
                cellWidget = QtGui.QWidget()
                cellWidget.setAttribute(Qt.WA_StyledBackground)
                cellWidget.setStyleSheet('QWidget {background:transparent;}')
                cellWidget.setLayout(cmv)

                label = QtGui.QLabel(files[f])
                cmv.addWidget(label)
                print files[f]
                self.assetTable.setCellWidget(f,1,cellWidget)

            '''
            #versionName = 'high'

            listArray = []
            for f in files:
                subPath = self.finalPath + '\\' + f
                subFiles = os.listdir(subPath)
                isAppend = False
                tempDict = {'file': '', 'pic': '', 'date': ''}
                for sf in subFiles:

                    if os.path.isfile(subPath + '\\' + sf):
                        #print sf[-3:]
                        if sf[-3:] == '.ma':
                            spsf = sf.split('_')
                            if (len(spsf) == 5) and (versionName in spsf[-1]):
                                tempDict.update({'file':subPath + '\\' + sf})
                                isAppend = True
                        if sf[-3:] == 'png':
                            tempDict.update({'pic':subPath + '\\' + sf})

                if isAppend:
                    listArray.append(tempDict)
                # print files
            count = len(listArray)
            self.assetTable.clear()
            self.assetTable.setHorizontalHeaderLabels(['picture', 'infomation'])
            self.assetTable.setRowCount(count)

            for f in range(count):
                cmv = QtGui.QVBoxLayout()
                cellWidget = QtGui.QWidget()
                #print files[f]
                cellWidget.setToolTip(listArray[f]['file'])
                cellWidget.setAttribute(Qt.WA_StyledBackground)
                cellWidget.setStyleSheet('QWidget {background:transparent;}')
                cellWidget.setLayout(cmv)

                basename = os.path.basename(listArray[f]['file'])
                label = QtGui.QLabel(basename)
                cmv.addWidget(label)

                self.assetTable.setCellWidget(f,1,cellWidget)

                pixmap = QtGui.QPixmap(listArray[f]['pic'])
                pixmap = pixmap.scaledToWidth(150)
                piclabel = QtGui.QLabel()
                piclabel.setPixmap(pixmap)
                self.assetTable.setCellWidget(f,0,piclabel)


    def itemchange(self):
        sender = self.sender()
        #msg = sender.toolTip()
        selA = str(self.sectionA.currentText())
        selB = str(self.sectionB.currentText())
        selC = str(self.sectionC.currentText())
        self.finalPath = '\\'.join([self.assetPath,selA,selB])
        if self.finalPath:
            self.fillTableFn(self.finalPath,selC)


    def mousePressEvent(self, event):
        #if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
            #self.m_drag = True
            #self.m_DragPosition = event.globalPos() - self.pos()
            #event.accept()
        pass

    def mouseMoveEvent(self, QMouseEvent):
        #if QMouseEvent.buttons() and Qt.LeftButton:
            #self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            #QMouseEvent.accept()
        pass

    def mouseReleaseEvent(self, QMouseEvent):
        #self.m_drag = False
        pass

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

    def closeEvent(self, event):
        self.deleteLater()

    # ------------define swtich--------------------
    def Op_Ui(self):
        self.cleanOpenWindow()
        self.createUI()
        #self.setParent(getMayaWindow())
        self.show()

    def Cl_Ui(self):
        self.close()


#cleanCtrlUIRT = selectCharactor_ANIM_TOOL()
#cleanCtrlUIRT.Op_Ui()
