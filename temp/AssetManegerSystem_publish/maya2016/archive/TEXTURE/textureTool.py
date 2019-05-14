class assetManager_textureRightClickTreeWidget(QtWidgets.QTreeWidget):
    choosed = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(assetManager_textureRightClickTreeWidget, self).__init__(parent)
        self.pathList = getAssetManagerPath()
        self.initPath = self.pathList['main']
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.setSelectionMode(self.ExtendedSelection)

    def showContextMenu(self, pos):
        iconPath = self.pathList['icon']

        self.contextMenu = QtWidgets.QMenu(self)
        self.contextMenu.setStyleSheet(Mstyle.QMenu())

        if not (self.currentItem().parent()):
            actionA = self.contextMenu.addAction(QtGui.QIcon(iconPath + 'save.png'), u'download')
            actionA.triggered.connect(self.actionAFn)
            actionA = self.contextMenu.addAction(QtGui.QIcon(iconPath + 'save.png'), u'download all')
            actionA.triggered.connect(self.actionBFn)
            actionB = self.contextMenu.addAction(QtGui.QIcon(iconPath + 'open.png'), u'open folder')
            actionB.triggered.connect(self.actionCFn)

        self.contextMenu.exec_(QtGui.QCursor.pos())  # show menu on cursor pos

    def actionAFn(self):
        self.choosed.emit('download')

    def actionBFn(self):
        self.choosed.emit('downloadAll')

    def actionCFn(self):
        self.choosed.emit('openFolder')


class textureAssetManager(assetManager_BaseClass):
    def extraInit(self):
        self.departmentName = 'TEXTURE'

    def createGeneralTab(self):
        self.GWid = QtWidgets.QWidget()
        self.GWid.setAttribute(Qt.WA_StyledBackground)
        self.GWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        self.GWid.setAttribute(Qt.WA_DeleteOnClose)

        self.GWid.setAttribute(Qt.WA_StyledBackground)
        self.GWid.setAttribute(Qt.WA_DeleteOnClose)
        msgVB = QtWidgets.QVBoxLayout()

        titleHB = QtWidgets.QHBoxLayout()

        preBtn = QtWidgets.QToolButton()
        preBtn.setText('<--')
        preBtn.setToolTip('pre item')
        preBtn.setIcon(QtGui.QIcon(self.iconPath + '\\prePage_red.png'))
        preBtn.setIconSize(QtCore.QSize(16, 16))
        preBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        preBtn.setAutoRaise(True)

        self.titleLabel = QtWidgets.QLabel('charactorName')
        self.titleLabel.setToolTip('charactorName')
        self.titleLabel.setStyleSheet(Mstyle.QLabel(fontSize='20px'))

        nextBtn = QtWidgets.QToolButton()
        nextBtn.setText('-->')
        nextBtn.setToolTip('next item')
        nextBtn.setIcon(QtGui.QIcon(self.iconPath + '\\nextPage_red.png'))
        nextBtn.setIconSize(QtCore.QSize(16, 16))
        nextBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        nextBtn.setAutoRaise(True)

        titleHB.addWidget(preBtn)
        titleHB.addStretch(1)
        titleHB.addWidget(self.titleLabel)
        titleHB.addStretch(1)
        titleHB.addWidget(nextBtn)
        msgVB.addLayout(titleHB)

        self.itmTreeWid = assetManager_textureRightClickTreeWidget()

        self.itmTreeWid.setHeaderLabels(['name', 'aritst', 'date'])
        self.itmTreeWid.setMinimumHeight(350)
        self.itmTreeWid.setColumnWidth(0, 220)
        self.itmTreeWid.setColumnWidth(1, 70)
        self.itmTreeWid.setColumnWidth(2, 70)
        self.itmTreeWid.setStyleSheet(Mstyle.QTreeWidget() + Mstyle.QScrollBar())
        msgVB.addWidget(self.itmTreeWid)

        emptyHBox = QtWidgets.QHBoxLayout()
        nameLab = QtWidgets.QLabel('no empty shader file')
        nameBtn = QtWidgets.QPushButton('select')
        nameBtn.setStyleSheet(Mstyle.QPushButton())
        nameBtn.setFixedWidth(85)
        emptyHBox.addWidget(nameLab)
        emptyHBox.addWidget(nameBtn)
        msgVB.addLayout(emptyHBox)

        modelGrp = QtWidgets.QGroupBox('model')
        modelGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        modelGrp.setMaximumHeight(120)
        modGVB = QtWidgets.QVBoxLayout()
        modGVB.setContentsMargins(5, 5, 5, 5)
        modGVB.setSpacing(4)
        modGHB1 = QtWidgets.QHBoxLayout()
        modGHB2 = QtWidgets.QHBoxLayout()

        labServerDate = QtWidgets.QLabel('Serve Mod : ', self.GWid)
        labServerDate.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB1.addWidget(labServerDate)
        modGHB1.addStretch(1)

        self.labServerText = QtWidgets.QLabel('', self.GWid)
        self.labServerText.setToolTip('print servMod')
        self.labServerText.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB1.addWidget(self.labServerText)
        modGHB1.addStretch(1)

        labLocalDate = QtWidgets.QLabel('Local Mod  : ', self.GWid)
        labLocalDate.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB2.addWidget(labLocalDate)
        modGHB2.addStretch(1)

        self.labLocalText = QtWidgets.QLabel('', self.GWid)
        self.labLocalText.setToolTip('print localMod')
        self.labLocalText.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB2.addWidget(self.labLocalText)
        modGHB2.addStretch(1)

        modGHBtn = QtWidgets.QHBoxLayout()
        downloadConceptBtn = QtWidgets.QPushButton('update')
        downloadConceptBtn.setStyleSheet(Mstyle.QPushButton(bordRad='8px'))
        downloadConceptBtn.setToolTip('updateModel')
        viewConceptBtn = QtWidgets.QPushButton('refrence')
        viewConceptBtn.setStyleSheet(Mstyle.QPushButton(bordRad='8px', kw='b'))
        viewConceptBtn.setToolTip('refrenceModel')
        modGHBtn.addWidget(downloadConceptBtn)
        modGHBtn.addWidget(viewConceptBtn)

        modGVB.addLayout(modGHB1)
        modGVB.addLayout(modGHB2)
        modGVB.addLayout(modGHBtn)
        modelGrp.setLayout(modGVB)
        msgVB.addWidget(modelGrp)

        self.infoGrp = QtWidgets.QGroupBox('infomation')
        self.infoGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        self.infoGrp.setMaximumHeight(150)
        infoGVB = QtWidgets.QVBoxLayout()

        lastmsgHB = QtWidgets.QHBoxLayout()
        labLastMsgTitle = QtWidgets.QLabel('LastMsg : ', self.GWid)
        labLastMsgTitle.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        labLastMsg = QtWidgets.QLabel('', self.GWid)

        labLastMsg.setToolTip('lastmsg')
        labLastMsg.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b', lang='c'))
        lastmsgHB.addWidget(labLastMsgTitle)
        lastmsgHB.addWidget(labLastMsg)
        lastmsgHB.addStretch(1)

        infoGHB1 = QtWidgets.QHBoxLayout()
        lab4 = QtWidgets.QLabel('Artist : ', self.GWid)
        lab4.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        lab4data = QtWidgets.QLabel('', self.GWid)
        lab4data.setToolTip('artist')
        lab4data.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        infoGHB1.addWidget(lab4)
        infoGHB1.addWidget(lab4data)
        infoGHB1.addStretch(1)

        infoGHB2 = QtWidgets.QHBoxLayout()
        lab5 = QtWidgets.QLabel('Passing : ', self.GWid)
        lab5.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        lab5data = QtWidgets.QLabel('none days', self.GWid)
        lab5data.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        lab5data.setToolTip('passing')
        infoGHB2.addWidget(lab5)
        infoGHB2.addWidget(lab5data)
        infoGHB2.addStretch(1)

        infoGHB3 = QtWidgets.QHBoxLayout()
        lab6 = QtWidgets.QLabel('StartDate :     ', self.GWid)
        lab6.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        lab6data = QtWidgets.QLabel('', self.GWid)
        lab6data.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        lab6data.setToolTip('startdate')
        infoGHB3.addWidget(lab6)
        infoGHB3.addWidget(lab6data)
        infoGHB3.addStretch(1)

        infoGHB6 = QtWidgets.QHBoxLayout()
        lab11 = QtWidgets.QLabel('UpdateData : ', self.GWid)
        lab11.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        lab11data = QtWidgets.QLabel('', self.GWid)
        lab11data.setToolTip('updatedate')
        lab11data.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        infoGHB6.addWidget(lab11)
        infoGHB6.addWidget(lab11data)
        infoGHB6.addStretch(1)

        infoGHB4 = QtWidgets.QHBoxLayout()
        lab7 = QtWidgets.QLabel('ConfirmData : ', self.GWid)
        lab7.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        lab7data = QtWidgets.QLabel('', self.GWid)
        lab7data.setToolTip('confirmdate')
        lab7data.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        infoGHB4.addWidget(lab7)
        infoGHB4.addWidget(lab7data)
        infoGHB4.addStretch(1)

        infoGHB5 = QtWidgets.QHBoxLayout()
        lab8 = QtWidgets.QLabel('Machine : ', self.GWid)
        lab8.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        lab8data = QtWidgets.QLabel('', self.GWid)
        lab8data.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        lab8data.setToolTip('machine')
        infoGHB5.addWidget(lab8)
        infoGHB5.addWidget(lab8data)
        infoGHB5.addStretch(1)

        infoGVB.addLayout(lastmsgHB)
        infoGVB.addLayout(infoGHB1)
        infoGVB.addLayout(infoGHB2)
        infoGVB.addLayout(infoGHB3)
        infoGVB.addLayout(infoGHB6)
        infoGVB.addLayout(infoGHB4)
        infoGVB.addLayout(infoGHB5)
        self.infoGrp.setLayout(infoGVB)
        msgVB.addWidget(self.infoGrp)

        oprGrp = QtWidgets.QGroupBox('opreate')
        oprGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        oprGrp.setMaximumHeight(150)
        oprGVB = QtWidgets.QVBoxLayout()

        oprGHB1 = QtWidgets.QHBoxLayout()
        oprbtn_upload = QtWidgets.QPushButton('upload', self.GWid)
        oprbtn_upload.setFixedHeight(25)
        oprbtn_upload.setStyleSheet(Mstyle.QPushButton(bordRad='12px'))
        oprbtn_upload.setToolTip('open upload window')
        oprGHB1.addWidget(oprbtn_upload)

        oprGVB.addLayout(oprGHB1)
        oprGrp.setLayout(oprGVB)
        msgVB.addWidget(oprGrp)
        msgVB.addStretch(1)

        self.GWid.setLayout(msgVB)

        self.tabWid.addTab(self.GWid, 'general')

        preBtn.clicked.connect(self.aboveItemFn)
        nextBtn.clicked.connect(self.belowItemFn)

        self.itmTreeWid.choosed.connect(self.choosedFn)
        oprbtn_upload.clicked.connect(self.oprbtn_openUploadFn)

        # return self.GWid

    def choosedFn(self, strSign):
        print strSign

    def oprbtn_openUploadFn(self):
        print 'open check list'

    def loadGeneralPageData(self, changeTabItm):
        preBtn = ''
        nextBtn = ''
        picLabel = ''
        titleLabel = ''

        artistlab = ''
        passinglab = ''
        startdatelab = ''
        confirmdatelab = ''
        machinelab = ''
        lastmsglab = ''
        for c in self.tabWid.currentWidget().children():
            if type(c) == QtWidgets.QPushButton:
                if c.toolTip() == 'pre item':
                    preBtn = c
                if c.toolTip() == 'next item':
                    nextBtn = c
            if type(c) == QtWidgets.QLabel:
                if c.toolTip() == 'charactorName':
                    titleLabel = c
            if type(c) == QtWidgets.QGroupBox:
                if c.title() == 'infomation':
                    for cc in c.children():
                        if type(cc) != QtWidgets.QVBoxLayout:
                            if cc.toolTip() == 'artist':
                                artistlab = cc
                            if cc.toolTip() == 'passing':
                                passinglab = cc
                            if cc.toolTip() == 'startdate':
                                startdatelab = cc
                            if cc.toolTip() == 'confirmdate':
                                confirmdatelab = cc
                            if cc.toolTip() == 'machine':
                                machinelab = cc
                            if cc.toolTip() == 'lastmsg':
                                lastmsg = cc
                                # from widget , load every lab in variable,over

        filePath = self.serverPath + '\\asset\\' + self.departmentName + '\\' + self.nowTreePage + '\\' + changeTabItm.text(
            0) + '\\'
        files = self.getFiles(filePath)
        print files

        hasPic = []
        for f in files:
            spf = f.split('.')
            if spf[-1] in ['png', 'jpg', 'exr']:
                hasPic.append(filePath + f)

        self.itmTreeWid.clear()
        for i in hasPic:
            bName = os.path.basename(i)
            itm = QtWidgets.QTreeWidgetItem()
            itm.setText(0, bName)
            itm.setText(1, 'undefined')
            itm.setText(2, 'xxxx-xx-xx yy:yy:yy')
            self.itmTreeWid.addTopLevelItem(itm)

        # load .jpg .png .exr files under folder over

        # load title label
        titleLabel.setText(changeTabItm.text(0))
        # load model info

        hFile = ''
        sp = self.serverPath.split('\\')
        sp.append('asset')
        sp.append('MODEL')
        sp.append(self.nowTreePage)
        sp.append(changeTabItm.text(0))
        modelPath = '\\'.join(sp)
        mFiles = os.listdir(modelPath)
        for m in mFiles:
            if m[-3:] == '.ma':
                if '_high' in m:
                    hFile = modelPath + '\\' + m
                    self.nowHighModel = hFile

        sp = self.serverPath.split('\\')
        sp.append('asset')
        sp.append(self.departmentName)
        sp.append(self.nowTreePage)
        sp.append(changeTabItm.text(0))
        sp.append('DownloadModel')
        downLoadModelPath = '\\'.join(sp)
        if os.path.exists(downLoadModelPath):
            Ctype = self.nowTreePage.lower()
            if Ctype == 'char':
                Ctype = 'cha'

            highArray = ['PIG', Ctype, changeTabItm.text(0), 'mod', 'high.ma']
            highName = '_'.join(highArray)
            self.nowHighModelLocal = downLoadModelPath + '\\' + highName

            if os.path.exists(self.nowHighModelLocal):
                strTime = time.strftime("%m-%d %H:%M:%S %Y", time.localtime(os.path.getmtime(self.nowHighModelLocal)))
                self.labLocalText.setText(strTime)
            else:
                self.labLocalText.setText('')


        # self.labServerText self.labLocalText
        else:
            os.makedirs(downLoadModelPath)

        if hFile:
            strTime = time.strftime("%m-%d %H:%M:%S %Y", time.localtime(os.path.getmtime(hFile)))
            self.labServerText.setText(strTime)
        else:
            self.labServerText.setText('')
        '''
        '''

    def Op_Ui(self):
        self.show()
        self.resize(450, 900)
        self.move(100, 100)

    def aboveItemFn(self):
        node = self.treeWid.itemAbove(self.treeWid.currentItem())
        if node:
            self.treeWid.setCurrentItem(node)

    def belowItemFn(self):
        node = self.treeWid.itemBelow(self.treeWid.currentItem())
        if node:
            self.treeWid.setCurrentItem(node)

    def prePicFn(self):
        nowRow = self.picView.currentRow()
        nowRow -= 1
        if nowRow < 0:
            nowRow = 0
        self.picView.setCurrentRow(nowRow)
        self.changePicFn()

    def nextPicFn(self):
        nowRow = self.picView.currentRow()
        nowRow += 1
        if nowRow > self.picView.count():
            nowRow = self.picView.count()
        self.picView.setCurrentRow(nowRow)
        self.changePicFn()

    def changePicFn(self):
        nowsel = self.picView.currentItem()
        if nowsel:
            spPath = os.path.split(str(nowsel.toolTip()))
            spName = spPath[-1].split('.')[0]
            nowPic = QtGui.QPixmap(spPath[0] + '\\' + spName + '_middle.jpg')

            self.plabPic.setPixmap(nowPic)
            self.plabPic.setToolTip(str(nowsel.toolTip()))

            artistlab = ''
            passinglab = ''
            startdatelab = ''
            confirmdatelab = ''
            machinelab = ''
            lastmsg = ''
            updatedatelab = ''
            for cc in self.infoGrp.children():
                if type(cc) != QtGui.QVBoxLayout and type(cc) != QtGui.QHBoxLayout:
                    if cc.toolTip() == 'artist':
                        artistlab = cc
                    if cc.toolTip() == 'passing':
                        passinglab = cc
                    if cc.toolTip() == 'startdate':
                        startdatelab = cc
                    if cc.toolTip() == 'confirmdate':
                        confirmdatelab = cc
                    if cc.toolTip() == 'machine':
                        machinelab = cc
                    if cc.toolTip() == 'lastmsg':
                        lastmsg = cc
                    if cc.toolTip() == 'updatedate':
                        updatedatelab = cc

            mainPath = os.path.dirname(str(nowsel.toolTip()))
            mainName = os.path.basename(str(nowsel.toolTip()))
            msgData = {}
            if os.path.exists(mainPath + '\\message.json'):
                msgData = self.loadJson(mainPath + '\\message.json')

            infoData = {}
            if os.path.exists(mainPath + '\\infomation.json'):
                infoData = self.loadJson(mainPath + '\\infomation.json')

            hasConfirm = False
            hasStart = False
            if mainName in msgData.keys():
                artistlab.setText(msgData[mainName][-1]['artist'])
                timeStr = msgData[mainName][-1]['updateDate']
                formTime = '{}-{}-{} {}:{}:{}'.format(timeStr[0:4], timeStr[4:6], timeStr[6:8], timeStr[8:10],
                                                      timeStr[10:12], timeStr[12:14])
                updatedatelab.setText(formTime)
                lastmsg.setText(msgData[mainName][-1]['message'])
                machinelab.setText(msgData[mainName][-1]['machine'])
            else:
                artistlab.setText('')
                updatedatelab.setText('')
                lastmsg.setText('')
                machinelab.setText('')

            if mainName in infoData.keys():
                confirmdatelab.setText(infoData[mainName])
                hasConfirm = True
            else:
                confirmdatelab.setText('')
            if 'startTime' in infoData.keys():
                startdatelab.setText(infoData['startTime'])
                hasStart = True
            else:
                startdatelab.setText('')

            passingStr = ''
            if hasStart:
                spSD = infoData['startTime'].split(' ')
                daySD = int(spSD[0].split('-')[2])
                monSD = int(spSD[0].split('-')[1])
                yearSD = int(spSD[0].split('-')[0])
                # passingStr
                if hasConfirm:
                    spED = infoData[mainName].split(' ')
                    dayED = int(spED[0].split('-')[2])
                    monED = int(spED[0].split('-')[1])
                    yearED = int(spED[0].split('-')[0])

                else:
                    nowdate = time.strftime("%m-%d-%Y", time.localtime(time.time()))
                    dayED = int(nowdate.split('-')[1])
                    monED = int(nowdate.split('-')[0])
                    yearED = int(nowdate.split('-')[2])

                d1 = datetime.datetime(yearSD, monSD, daySD)
                d2 = datetime.datetime(yearED, monED, dayED)
                passingStr = str((d2 - d1).days) + ' days'

            passinglab.setText(passingStr)


sam = textureAssetManager()

sam.Op_Ui()
