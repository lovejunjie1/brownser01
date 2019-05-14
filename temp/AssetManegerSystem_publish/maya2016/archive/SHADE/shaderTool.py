class shaderAssetManager(assetManager_BaseClass):
    def extraInit(self):
        self.departmentName = 'SHADE'
        
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

        selHbox = QtWidgets.QHBoxLayout()
        selCombo = QtWidgets.QComboBox()
        selCombo.setStyleSheet(Mstyle.QComboBox())
        selMain = QtWidgets.QPushButton('texture')
        selMain.setStyleSheet(Mstyle.QPushButton(kw='off')+'QPushButton:checked {background:rgb(235,75,57);color:rgb(95,25,15)}')
        selMain.setAutoExclusive(True)
        selMain.setCheckable(True)       
        selMain.setChecked(True)
        
        selRender = QtWidgets.QPushButton('render')
        selRender.setStyleSheet(Mstyle.QPushButton(kw='off')+'QPushButton:checked {background:rgb(235,75,57);color:rgb(95,25,15)}')
        selRender.setAutoExclusive(True)
        selRender.setCheckable(True)
        
        selHbox.addWidget(selCombo)
        selHbox.addWidget(selMain)
        selHbox.addWidget(selRender)
        msgVB.addLayout(selHbox)

        self.radGrp = QtWidgets.QButtonGroup()
        self.radGrp.setExclusive(True)
        self.radGrp.addButton(selMain, 0)
        self.radGrp.addButton(selRender, 1)




        picHbox = QtWidgets.QHBoxLayout()
        self.plabPixmap = QtGui.QPixmap(self.iconPath + '\\currentPic.png')
        self.plabPic = clickLabel('', self)
        self.plabPic.setMinimumWidth(350)
        self.plabPic.setPixmap(self.plabPixmap)
        picHbox.addStretch(1)
        picHbox.addWidget(self.plabPic)
        picHbox.addStretch(1)
        msgVB.addLayout(picHbox)

        picviewHB = QtWidgets.QHBoxLayout()
        prePicBtn = QtWidgets.QToolButton()
        prePicBtn.setText('<--')
        prePicBtn.setToolTip('pre pic')
        prePicBtn.setIcon(QtGui.QIcon(self.iconPath + '\\prePage_red.png'))
        prePicBtn.setIconSize(QtCore.QSize(32, 32))
        prePicBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        prePicBtn.setAutoRaise(True)

        nextPicBtn = QtWidgets.QToolButton()
        nextPicBtn.setText('-->')
        nextPicBtn.setToolTip('next pic')
        nextPicBtn.setIcon(QtGui.QIcon(self.iconPath + '\\nextPage_red.png'))
        nextPicBtn.setIconSize(QtCore.QSize(32, 32))
        nextPicBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        nextPicBtn.setAutoRaise(True)

        self.picView=QtWidgets.QListWidget()
        self.picView.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum);
        self.picView.setViewMode(QtWidgets.QListView.IconMode)
        self.picView.setFixedHeight(70)
        self.picView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.picView.setMovement(QtWidgets.QListView.Static)
        self.picView.setIconSize(QtCore.QSize(120, 160))
        self.picView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.picView.horizontalScrollBar().setStyleSheet(
            'QScrollBar{      background:rgb(98,98,98); height:6px;border-radius:5px; }'
            'QScrollBar::handle                 {background:rgb(245,75,57); border-radius:3px; }'
            'QScrollBar::handle:hover           {background:rgb(255,95,77);border-radius:3px; }'
            'QScrollBar::handle:pressed         {background:rgb(205,53,43);}'
            'QScrollBar::sub-line               {background:transparent;}'
            'QScrollBar::add-line               {background:transparent;}' 
            'QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal{background:transparent;border-radius:3px;}')
        self.picView.setWrapping(False)
        self.picView.setCurrentRow(0)

        picviewHB.addWidget(prePicBtn)
        picviewHB.addWidget(self.picView)
        picviewHB.addWidget(nextPicBtn)
        msgVB.addLayout(picviewHB)

        modelGrp = QtWidgets.QGroupBox('model')
        modelGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        modelGrp.setMaximumHeight(120)
        modGVB = QtWidgets.QVBoxLayout()
        modGVB.setContentsMargins(5, 5, 5, 5)
        modGVB.setSpacing(4)
        modGHB1 = QtWidgets.QHBoxLayout()
        modGHB2 = QtWidgets.QHBoxLayout()
        modGHB3 = QtWidgets.QHBoxLayout()
        modGHB4 = QtWidgets.QHBoxLayout()

        labServerDate = QtWidgets.QLabel('Serve Mod : ', self.GWid)
        labServerDate.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB1.addWidget(labServerDate)
        modGHB1.addStretch(1)
        labServerText = QtWidgets.QLabel('', self.GWid)
        labServerText.setToolTip('print servMod')
        labServerText.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB1.addWidget(labServerText)
        modGHB1.addStretch(1)

        labLocalDate = QtWidgets.QLabel('Local Mod  : ', self.GWid)
        labLocalDate.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB2.addWidget(labLocalDate)
        modGHB2.addStretch(1)
        labLocalText = QtWidgets.QLabel('', self.GWid)
        labLocalText.setToolTip('print localMod')
        labLocalText.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB2.addWidget(labLocalText)
        modGHB2.addStretch(1)

        modGHB22 = QtWidgets.QHBoxLayout()
        downloadConceptBtn = QtWidgets.QPushButton('update')
        downloadConceptBtn.setStyleSheet(Mstyle.QPushButton(bordRad='8px'))
        downloadConceptBtn.setToolTip('updateModel')
        viewConceptBtn = QtWidgets.QPushButton('refrence')
        viewConceptBtn.setStyleSheet(Mstyle.QPushButton(bordRad='8px', kw='b'))
        viewConceptBtn.setToolTip('refrenceModel')
        modGHB22.addWidget(downloadConceptBtn)
        modGHB22.addWidget(viewConceptBtn)

        modGVB.addLayout(modGHB3)
        modGVB.addLayout(modGHB4)
        modGVB.addLayout(modGHB1)
        modGVB.addLayout(modGHB2)
        modGVB.addLayout(modGHB22)
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

        prePicBtn.clicked.connect(self.prePicFn)
        nextPicBtn.clicked.connect(self.nextPicFn)

        #downloadConceptBtn.clicked.connect(self.copyConceptToModelFn)
        #viewConceptBtn.clicked.connect(self.refrenceModelFn)
        oprbtn_upload.clicked.connect(self.oprbtn_openUploadFn)

        self.picView.currentItemChanged.connect(self.changePicFn)
        #return self.GWid

    def oprbtn_openUploadFn(self):
        print 'open check list'


    def loadGeneralPageData(self,changeTabItm):
        print changeTabItm
        
    def Op_Ui(self):
        self.show()
        self.resize(450,900)
        self.move(100,100)
        
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
            nowPic = QtGui.QPixmap(spPath[0]+'\\'+spName+'_middle.jpg')

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
            
            
sam = shaderAssetManager()

sam.Op_Ui()
