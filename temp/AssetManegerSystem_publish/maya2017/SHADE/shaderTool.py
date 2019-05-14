import hashlib


class shaderAssetManager(assetManager_BaseClass):
    def extraInit(self):
        self.departmentName = 'SHADE'
        self.projectName = 'PIG'

    def howToUseFn(self):
        dirPath = self.initPath
        docxPath = dirPath + '\\maya2017\\'+self.departmentName+'\\help.docx'
        docPath = dirPath + '\\maya2017\\'+self.departmentName+'\\help.doc'
        if os.path.exists(docPath):
            os.startfile(docPath)
            return True
        if os.path.exists(docxPath):
            os.startfile(docxPath)
    def getHash(self, f):
        line = f.readline()
        hash = hashlib.md5()
        while (line):
            hash.update(line)
            line = f.readline()
        return hash.hexdigest()

    def IsHashEqual(self, f1, f2):
        str1 = self.getHash(f1)
        str2 = self.getHash(f2)
        return str1 == str2

    def changeFileNodePath(self, newPath):
        fileNodes = cmds.ls(type='file')
        for i in fileNodes:
            filePath = cmds.getAttr(i + '.fileTextureName')
            fileName = os.path.basename(filePath)
            fixedPath = newPath + '\\' + fileName
            try:
                cmds.setAttr(i + '.fileTextureName', fixedPath, type='string')
            except:
                print i + 'not changed'

    def tool1actFn(self):

        inputString, ok3 = QtWidgets.QInputDialog.getText(self, "modify texture path", "new path :",
                                                          QtWidgets.QLineEdit.Normal, "")
        if ok3:
            isPass = False
            if inputString:

                if inputString[1] == ':':
                    if inputString[2] == '\\' or inputString[2] == '/':
                        if '/' in inputString:
                            spIs = inputString.split('/')
                            inputString = '\\'.join(spIs)
                        if inputString[-1] == '\\':
                            inputString = inputString[:-1]
                            isPass = True

            if isPass:
                print inputString
                self.changeFileNodePath(inputString)
            else:
                cmds.warning('input path is illegal')

    def tool2actFn(self):

        setwd = os.chdir('Z:\\archive\\software\\Script\\maya')
        osdir = os.getcwd()

        def filedict(self):
            dictall = {}
            name = os.listdir(self)
            for i in name:
                if os.path.isdir(i) == 1:
                    dictall[i] = os.listdir(self + '/' + i)
                else:
                    pass
            return dictall

        WindowName = 'ScriptManager'
        if cmds.window(WindowName, exists=True):
            cmds.deleteUI(WindowName)

        window = cmds.window(WindowName, title="Script Manager", widthHeight=(460, 740))
        form = cmds.formLayout()
        tabs = cmds.tabLayout(innerMarginWidth=2, innerMarginHeight=2)
        cmds.formLayout(form, edit=True,
                        attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))

        for i in filedict(osdir):
            child = cmds.rowColumnLayout(numberOfColumns=3)
            for k in range(len(filedict(osdir)[i])):
                n = filedict(osdir)[i][k]
                filePath = osdir + '\\' + i + '\\' + n
                spname = ''.join(n.split('.')[0:-1])
                cmds.button(label=spname, w=150, h=30, command=lambda k=k, n=n, filePath=filePath: execfile(filePath))
            cmds.setParent('..')

            cmds.tabLayout(tabs, edit=True, tabLabel=((child, i)))

        cmds.showWindow(window)

    def createGeneralTab(self):
        toolMn = QtWidgets.QMenu('Tool', self.MainMenuBar)
        self.MainMenuBar.addMenu(toolMn)
        tool1act = toolMn.addAction("change texture Path")
        tool2act = toolMn.addAction("TD's tool")

        self.GWid = QtWidgets.QWidget()
        self.GWid.setAttribute(Qt.WA_StyledBackground)
        self.GWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        self.GWid.setAttribute(Qt.WA_DeleteOnClose)

        self.GWid.setAttribute(Qt.WA_StyledBackground)
        self.GWid.setAttribute(Qt.WA_DeleteOnClose)
        msgVB = QtWidgets.QVBoxLayout()

        titleHB = QtWidgets.QHBoxLayout()

        self.preBtn = QtWidgets.QToolButton()
        self.preBtn.setText('<--')
        self.preBtn.setToolTip('pre item')
        self.preBtn.setIcon(QtGui.QIcon(self.iconPath + '\\prePage_red.png'))
        self.preBtn.setIconSize(QtCore.QSize(16, 16))
        self.preBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.preBtn.setAutoRaise(True)

        self.titleLabel = QtWidgets.QLabel('charactorName')
        self.titleLabel.setToolTip('charactorName')
        self.titleLabel.setStyleSheet(Mstyle.QLabel(fontSize='20px'))

        self.nextBtn = QtWidgets.QToolButton()
        self.nextBtn.setText('-->')
        self.nextBtn.setToolTip('next item')
        self.nextBtn.setIcon(QtGui.QIcon(self.iconPath + '\\nextPage_red.png'))
        self.nextBtn.setIconSize(QtCore.QSize(16, 16))
        self.nextBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.nextBtn.setAutoRaise(True)

        titleHB.addWidget(self.preBtn)
        titleHB.addStretch(1)
        titleHB.addWidget(self.titleLabel)
        titleHB.addStretch(1)
        titleHB.addWidget(self.nextBtn)
        msgVB.addLayout(titleHB)

        self.chaPixmap = QtGui.QPixmap()
        self.chaPixmap.load(self.nowPicPath)
        self.chaPixmap = self.chaPixmap.scaledToWidth(300)

        picHbox = QtWidgets.QHBoxLayout()
        self.plabPic = clickLabel('', self)
        self.plabPic.setToolTip('undefined')
        self.plabPic.setPixmap(self.chaPixmap)
        self.plabPic.setMaximumWidth(300)
        self.plabPic.resize(self.chaPixmap.width(), self.chaPixmap.height())
        picHbox.addWidget(self.plabPic)
        msgVB.addLayout(picHbox)

        modelGrp = QtWidgets.QGroupBox('Texture')
        modelGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        modelGrp.setMaximumHeight(120)
        modGVB = QtWidgets.QVBoxLayout()
        modGVB.setContentsMargins(5, 5, 5, 5)
        modGVB.setSpacing(4)
        modGHB1 = QtWidgets.QHBoxLayout()
        modGHB2 = QtWidgets.QHBoxLayout()

        labServerDate = QtWidgets.QLabel('Serve Texture : ', self.GWid)
        labServerDate.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB1.addWidget(labServerDate)
        modGHB1.addStretch(1)

        self.labServerText = QtWidgets.QLabel('', self.GWid)
        self.labServerText.setToolTip('print servTexture')
        self.labServerText.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB1.addWidget(self.labServerText)
        modGHB1.addStretch(1)

        labLocalDate = QtWidgets.QLabel('Local Texture  : ', self.GWid)
        labLocalDate.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB2.addWidget(labLocalDate)
        modGHB2.addStretch(1)

        self.labLocalText = QtWidgets.QLabel('', self.GWid)
        self.labLocalText.setToolTip('print localTexture')
        self.labLocalText.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB2.addWidget(self.labLocalText)
        modGHB2.addStretch(1)

        modGHBtn = QtWidgets.QHBoxLayout()
        downloadConceptBtn = QtWidgets.QPushButton('update')
        downloadConceptBtn.setStyleSheet(Mstyle.QPushButton(bordRad='8px'))
        downloadConceptBtn.setToolTip('updateTexture')
        viewConceptBtn = QtWidgets.QPushButton('refrence')
        viewConceptBtn.setStyleSheet(Mstyle.QPushButton(bordRad='8px', kw='b'))
        viewConceptBtn.setToolTip('refrenceTexture')
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
        self.lastmsg = QtWidgets.QLabel('', self.GWid)

        self.lastmsg.setToolTip('lastmsg')
        self.lastmsg.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b', lang='c'))
        lastmsgHB.addWidget(labLastMsgTitle)
        lastmsgHB.addWidget(self.lastmsg)
        lastmsgHB.addStretch(1)

        infoGHB1 = QtWidgets.QHBoxLayout()
        lab4 = QtWidgets.QLabel('Artist : ', self.GWid)
        lab4.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.artistlab = QtWidgets.QLabel('', self.GWid)
        self.artistlab.setToolTip('artist')
        self.artistlab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        infoGHB1.addWidget(lab4)
        infoGHB1.addWidget(self.artistlab)
        infoGHB1.addStretch(1)

        infoGHB2 = QtWidgets.QHBoxLayout()
        lab5 = QtWidgets.QLabel('Passing : ', self.GWid)
        lab5.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.passinglab = QtWidgets.QLabel('none days', self.GWid)
        self.passinglab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        self.passinglab.setToolTip('passing')
        infoGHB2.addWidget(lab5)
        infoGHB2.addWidget(self.passinglab)
        infoGHB2.addStretch(1)

        infoGHB3 = QtWidgets.QHBoxLayout()
        lab6 = QtWidgets.QLabel('StartDate :     ', self.GWid)
        lab6.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.startdatelab = QtWidgets.QLabel('', self.GWid)
        self.startdatelab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        self.startdatelab.setToolTip('startdate')
        infoGHB3.addWidget(lab6)
        infoGHB3.addWidget(self.startdatelab)
        infoGHB3.addStretch(1)

        infoGHB6 = QtWidgets.QHBoxLayout()
        lab11 = QtWidgets.QLabel('UpdateData : ', self.GWid)
        lab11.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.updatedatelab = QtWidgets.QLabel('', self.GWid)
        self.updatedatelab.setToolTip('updatedate')
        self.updatedatelab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        infoGHB6.addWidget(lab11)
        infoGHB6.addWidget(self.updatedatelab)
        infoGHB6.addStretch(1)

        infoGHB4 = QtWidgets.QHBoxLayout()
        lab7 = QtWidgets.QLabel('ConfirmData : ', self.GWid)
        lab7.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.confirmdatelab = QtWidgets.QLabel('', self.GWid)
        self.confirmdatelab.setToolTip('confirmdate')
        self.confirmdatelab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        infoGHB4.addWidget(lab7)
        infoGHB4.addWidget(self.confirmdatelab)
        infoGHB4.addStretch(1)

        infoGHB5 = QtWidgets.QHBoxLayout()
        lab8 = QtWidgets.QLabel('Machine : ', self.GWid)
        lab8.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.machinelab = QtWidgets.QLabel('', self.GWid)
        self.machinelab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        self.machinelab.setToolTip('machine')
        infoGHB5.addWidget(lab8)
        infoGHB5.addWidget(self.machinelab)
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

        oprGHB2 = QtWidgets.QHBoxLayout()
        oprbtn_confirm = QtWidgets.QPushButton('confirm', self.GWid)
        oprbtn_confirm.setFixedHeight(25)
        oprbtn_confirm.setStyleSheet(Mstyle.QPushButton(kw='b', bordRad='12px'))
        oprbtn_confirm.setToolTip('open confirm window')
        oprGHB2.addWidget(oprbtn_confirm)

        oprGVB.addLayout(oprGHB1)
        oprGVB.addLayout(oprGHB2)
        oprGrp.setLayout(oprGVB)
        msgVB.addWidget(oprGrp)
        msgVB.addStretch(1)

        self.GWid.setLayout(msgVB)

        self.tabWid.addTab(self.GWid, 'general')

        self.preBtn.clicked.connect(self.aboveItemFn)
        self.nextBtn.clicked.connect(self.belowItemFn)

        oprbtn_upload.clicked.connect(self.oprbtn_openUploadFn)
        oprbtn_confirm.clicked.connect(self.oprbtn_openConfirmFn)

        tool1act.triggered.connect(self.tool1actFn)
        tool2act.triggered.connect(self.tool2actFn)
        downloadConceptBtn.clicked.connect(self.downloadModelFn)
        viewConceptBtn.clicked.connect(self.refrenceModelFn)

    def downloadModelFn(self):
        if self.nowHighModel:
            if os.path.exists(self.nowHighModel):
                if os.path.exists(self.modelDownloadPath):
                    os.remove(self.modelDownloadPath)

                shutil.copyfile(self.nowHighModel, self.modelDownloadPath)
                shutil.copystat(self.nowHighModel, self.modelDownloadPath)
            else:
                print 'texture file not exists'
                return False
        # update file over

        itemNode = self.nowSelMainTreeItem

        userName = self.fileMn.title()
        if userName.lower() == 'login':
            ans = cmds.confirmDialog(title='confirm',
                                     m='user not login,do you wanna user machine ID or input by yourself.',
                                     b=['machineID', 'input'], cancelButton='machineID', defaultButton='machineID')
            if ans == 'machineID':
                userName = getpass.getuser()
            elif ans == 'input':
                try:
                    userName = raw_input()
                except EOFError:
                    userName = getpass.getuser()

        sDate = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime(time.time()))
        dataDict = {'artist': userName, 'date': sDate, 'machine': getpass.getuser(),
                    'message': 'start work', 'type': 'downloadPreDepartment'}
        # get common data from system.over

        dict = self.loadJson(self.timeNodePath)
        firstData = dict['firstDownload']
        for key, itm in firstData.items():
            if not itm:
                dict['firstDownload'] = dataDict
        dict['lastDownload'] = dataDict
        dict['log'].append(dataDict)
        self.saveJson(dict, self.timeNodePath)

        # save infomations to timenode.json

        historypath = self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + itemNode.text(
            0) + '\\history.html'
        if not (os.path.exists(historypath)):
            self.HTML_CreateEmptyStyle(historypath)

        innerMsg = '[ ' + self.departmentName + ' ][ download ] copy the model from TEXTURE path to ' + self.departmentName + ' path'
        htmlMsg = self.HTML_createMsg(innerMsg, userName, '', side=1, initPath=self.initPath)
        self.HTML_addMsg(historypath, htmlMsg)

        # html message over

        self.loadGeneralPageData()
        return True

    def refrenceModelFn(self):
        if self.modelDownloadPath:
            if os.path.exists(self.modelDownloadPath):
                cmds.file(self.modelDownloadPath, reference=True, type='mayaAscii', namespace='mod')
            else:
                print 'high file not exists'
                return False

    def loadGeneralPageData(self):
        changeTabItm = self.nowSelMainTreeItem
        # load title label
        self.titleLabel.setText(changeTabItm.text(0))

        filePath = self.serverPath + '\\asset\\' + self.departmentName + '\\' + self.nowTreePage + '\\' + changeTabItm.text(
            0) + '\\'
        files = self.getFiles(filePath)
        if files:
            # load file list from Json
            maFile = ''
            infoJson = ''
            screenShot = ''
            for f in files:
                if f[-3:] == '.ma':
                    maFile = filePath + f
                elif f == 'infomation.json':
                    infoJson = filePath + f
                elif f[-4:] == '.png':
                    screenShot = filePath + f

            if screenShot:
                self.chaPixmap.load(screenShot)
                self.chaPixmap = self.chaPixmap.scaledToWidth(300)
                self.plabPic.setToolTip(screenShot)
                self.plabPic.setPixmap(self.chaPixmap)
            else:
                self.chaPixmap.load(self.iconPath + '\\currentPic.png')
                self.chaPixmap = self.chaPixmap.scaledToWidth(300)
                self.plabPic.setToolTip(self.iconPath + '\\currentPic.png')
                self.plabPic.setPixmap(self.chaPixmap)

            # load infomation
            if os.path.exists(infoJson):

                infoData = self.loadJson(infoJson)

                self.machinelab.setText(infoData['machine'][-1])

                self.lastmsg.setText(infoData['message'][-1])

                self.updatedatelab.setText(infoData['uploadDate'][-1])

                self.artistlab.setText(infoData['artist'][-1])

            else:

                self.machinelab.setText('')

                self.lastmsg.setText('')

                self.updatedatelab.setText('')

                self.artistlab.setText('')

        # load model info
        hFile = ''
        sp = self.serverPath.split('\\')
        sp.append('asset')
        sp.append('TEXTURE')
        sp.append(self.nowTreePage)
        sp.append(changeTabItm.text(0))
        modelPath = '\\'.join(sp)
        if os.path.exists(modelPath):
            mFiles = os.listdir(modelPath)
            for m in mFiles:
                if m[-11:] == '_texture.ma':
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

                highArray = [self.projectName, Ctype, changeTabItm.text(0), 'texture.ma']
                highName = '_'.join(highArray)
                self.modelDownloadPath = downLoadModelPath + '\\' + highName

                if os.path.exists(self.modelDownloadPath):
                    strTime = time.strftime("%m-%d %H:%M:%S %Y",
                                            time.localtime(os.path.getmtime(self.modelDownloadPath)))
                    self.labLocalText.setText(strTime)
                else:
                    self.labLocalText.setText('')

            else:
                os.makedirs(downLoadModelPath)

        if hFile:
            strTime = time.strftime("%m-%d %H:%M:%S %Y", time.localtime(os.path.getmtime(hFile)))
            self.labServerText.setText(strTime)
        else:
            self.labServerText.setText('')

        # load infomation
        self.timeNodePath = self.serverPath + '\\asset\\' + self.departmentName + '\\' + self.nowTreePage + '\\' + changeTabItm.text(
            0) + '\\timeNode.json'
        isExt = os.path.exists(self.timeNodePath)

        art = ''
        passs = ''
        sDate = ''
        cDate = ''
        uDate = ''
        machin = ''
        msg = ''

        if isExt:
            dict = self.loadJson(self.timeNodePath)
            mainData = dict['log']
            if mainData:
                art = mainData[-1]['artist']
                msg = mainData[-1]['message']
                machin = mainData[-1]['machine']
                sDate = dict['firstDownload']['date']
                cDate = dict['lastConfirm']['date']
                uDate = dict['lastUpload']['date']

        else:
            emptyDict = {
                'lastUpload': {'type': '', 'artist': '', 'message': '', 'machine': '', 'date': ''},
                'lastDownload': {'type': '', 'artist': '', 'message': '', 'machine': '', 'date': ''},
                'firstDownload': {'type': '', 'artist': '', 'message': '', 'machine': '', 'date': ''},
                'lastConfirm': {'type': '', 'artist': '', 'message': '', 'machine': '', 'date': ''},
                'lastWriteNote': {'type': '', 'artist': '', 'message': '', 'machine': '', 'date': ''},
                'lastReadNote': {'type': '', 'artist': '', 'message': '', 'machine': '', 'date': ''},
                'log': [],
                'state': ''}
            self.saveJson(emptyDict, self.timeNodePath)

        self.updatedatelab.setText(uDate)
        self.artistlab.setText(art)
        self.passinglab.setText(passs)
        self.startdatelab.setText(sDate)
        self.confirmdatelab.setText(cDate)
        self.machinelab.setText(machin)
        self.lastmsg.setText(msg)
        # load infomations over
        pass

    def oprbtn_openConfirmFn(self):
        if self.treeWid.currentItem():
            itemNode = self.nowSelMainTreeItem

            servSp = self.serverPath.split('\\')
            servSp.append('asset')
            servSp.append(self.departmentName)
            servSp.append(self.nowTreePage)
            servSp.append(itemNode.text(0))
            servSp.append('uploadTemp')
            servPath = '\\'.join(servSp)

            confirm = assetManager_confirmTool()
            confirm.setParent(self)
            confirm.searchPath = servPath
            confirm.localPath = self.localPath
            confirm.serverPath = self.serverPath
            confirm.workName = itemNode.text(0)
            confirm.createUI()
            confirm.fillListWidget()
            confirm.Op_Ui()
            #confirm.BtnA2.setEnabled(True)
            confirm.resize(self.width(), self.height())
            confirm.confirmClicked.connect(self.confirmFn)
            confirm.checkClicked.connect(self.confirmCheckFn)
        else:
            print 'need select item first'

    def oprbtn_openUploadFn(self):
        # self.pictureArray = theList
        submitTool = assetManager_submitTool()
        submitTool.getNotifyFromTxt(self.initPath + '\\maya2017\\' + self.departmentName + '\\notify.txt')
        submitTool.createUI()
        submitTool.setParent(self)
        submitTool.BtnA2.setVisible(False)
        submitTool.BtnA1.setText('upload')
        submitTool.BtnA1.setEnabled(False)
        submitTool.Op_Ui()

        submitTool.lowClicked.connect(self.oprbtn_uploadFn)
        submitTool.highClicked.connect(self.oprbtn_uploadFn)
        submitTool.resize(self.width(), self.height())

    def oprbtn_uploadFn(self, data):

        changeTabItm = self.nowSelMainTreeItem

        reply = QtWidgets.QMessageBox.information(self,
                                                  "double check",
                                                  ("upload to\n" + str(changeTabItm.text(0))),
                                                  QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        # double check

        if reply == QtWidgets.QMessageBox.Yes:

            userName = str(self.fileMn.title())
            if userName.lower() == 'login':
                userName = getpass.getuser()
            # get user name from label
            uploadTime = time.localtime(time.time())
            nowdate = time.strftime("%Y-%m-%d %H:%M:%S",uploadTime)
            # get update time
            chaPath = self.serverPath + '\\asset\\' + self.departmentName + '\\' + self.nowTreePage + '\\' + changeTabItm.text(
                0)
            # combie self department path string
            tyStr = ''
            if self.nowTreePage == 'Char':
                tyStr = 'cha'
            else:
                tyStr = self.nowTreePage.lower()
            # get upload type

            linedate = time.strftime("%Y%m%d%H%M%S", uploadTime)
            filename = self.projectName + '_' + tyStr + '_' + changeTabItm.text(
                0) + '_' + self.departmentName.lower() + '.ma'
            uploadPath = chaPath + '\\uploadTemp\\' + linedate + '\\'
            os.makedirs(uploadPath)
            # get upload path and create date folder

            cmds.file(rename=uploadPath + filename)
            cmds.file(save=True, type='mayaAscii')
            # upload .ma file over

            dataDict = {'artist': userName, 'date': nowdate, 'machine': getpass.getuser(), 'message': data[-1],
                        'type': 'upload'}

            dict = self.loadJson(self.timeNodePath)
            dict['lastUpload'] = dataDict
            dict['log'].append(dataDict)

            self.saveJson(dict, uploadPath + 'timeNode.json')
            self.saveJson(dict, self.timeNodePath)
            # save the common infomations to the json file of uploadtempPath and mainPath

            #nameDict = {}
            #for i in self.pictureArray:
            #    picName = os.path.basename(i)
            #    picHash = ''
            #    with open(i, 'rb') as f:
            #        picHash = self.getHash(f)
            #    nameDict.update({picName: picHash})

            #jsonPath = chaPath + '\\uploadTemp\\' + linedate + '\\'
            #self.saveJson(dataDict, jsonPath + 'infomation.json')
            # save infomation json

            shutil.copyfile(data[1], chaPath + '\\uploadTemp\\' + linedate + '\\sceenshot.png')
            shutil.copystat(data[1], chaPath + '\\uploadTemp\\' + linedate + '\\sceenshot.png')
            # copy screenshot form local to server
            mel.eval('print "done"')

            producePath = self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + changeTabItm.text(0)
            if not (os.path.exists(producePath)):
                os.makedirs(producePath)
            historypath = producePath + '\\history.html'
            if not (os.path.exists(historypath)):
                self.HTML_CreateEmptyStyle(historypath)
            # make sure produce folder

            innerMsg = '[ ' + self.departmentName + ' ][ upload ] ' + ' <br> updateTime : ' + nowdate + '<br>update by ' + userName
            htmlMsg = self.HTML_createMsg(innerMsg, userName, '', side=1, initPath=self.initPath)
            self.HTML_addMsg(historypath, htmlMsg)
            # history data update over

    def confirmCheckFn(self, signData):
        pass

    def confirmFn(self, cData):
        itemNode = self.nowSelMainTreeItem

        servSp = self.serverPath.split('\\')
        servSp.append('asset')
        servSp.append(self.departmentName)
        servSp.append(self.nowTreePage)
        servSp.append(itemNode.text(0))
        chaPath = '\\'.join(servSp)
        # get charactor path - server
        tempPath = os.path.dirname(cData[2])
        updateFiles = os.listdir(tempPath)
        # get  the upload temp path and files in the path.

        for uf in updateFiles:
            spUf = uf.split('.')
            mainPathFile = chaPath + '\\' + uf
            updatePathFile = tempPath + '\\' + uf

            if os.path.exists(mainPathFile):
                if uf == 'timeNode.json':
                    continue
                else:
                    try:
                        os.remove(mainPathFile)
                    except:
                        print mainPathFile + 'cannot update'
                        continue

            if uf[0] != '.':
                if not (spUf[-1] in ['ma']):
                    shutil.copyfile(updatePathFile, mainPathFile)
                    shutil.copystat(updatePathFile, mainPathFile)
                elif spUf[-1] == 'ma':
                    #self.changeFileNodePath(ctexturePath)

                    cmds.file(rename=mainPathFile)
                    cmds.file(save=True, type='mayaAscii')
                else:
                    continue
        # save current file to mainPath and replace all texturePath to confirmTexture path.

        userName = self.fileMn.title()
        if userName.lower() == 'login':
            ans = cmds.confirmDialog(title='confirm',
                                     m='user not login,do you wanna user machine ID or input by yourself.',
                                     b=['machineID', 'input'], cancelButton='machineID', defaultButton='machineID')
            if ans == 'machineID':
                userName = getpass.getuser()
            elif ans == 'input':
                try:
                    userName = raw_input()
                except EOFError:
                    userName = getpass.getuser()
        nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        # get base infomations form system
        tempTimeNode = tempPath + '\\timeNode.json'
        tempDict = self.loadJson(tempTimeNode)
        # timeNode from uploadTemp Path.
        # self.timeNodePath

        dataDict = {'artist': userName, 'date': nowTime, 'machine': getpass.getuser(),
                    'message': tempDict['lastUpload']['message'], 'type': 'confirm'}

        dict = self.loadJson(self.timeNodePath)
        dict['lastConfirm'] = dataDict
        dict['log'].append(dataDict)

        self.saveJson(dict, tempTimeNode)
        self.saveJson(dict, self.timeNodePath)
        # save main infomations over.

        producePath = self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + itemNode.text(0)
        if not (os.path.exists(producePath)):
            os.makedirs(producePath)
        historypath = producePath + '\\history.html'
        if not (os.path.exists(historypath)):
            self.HTML_CreateEmptyStyle(historypath)
        # make sure producePath is ok.
        innerMsg = '[ ' + self.departmentName + ' ][ confirm ] ' + ' <br> confirmTime : ' + nowTime + '<br>confirm by ' + userName
        htmlMsg = self.HTML_createMsg(innerMsg, userName, '', side=1, initPath=self.initPath)
        self.HTML_addMsg(historypath, htmlMsg)
        # history data saved.
        self.loadGeneralPageData()

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
                self.artistlab.setText(msgData[mainName][-1]['artist'])
                timeStr = msgData[mainName][-1]['updateDate']
                formTime = '{}-{}-{} {}:{}:{}'.format(timeStr[0:4], timeStr[4:6], timeStr[6:8], timeStr[8:10],
                                                      timeStr[10:12], timeStr[12:14])
                self.updatedatelab.setText(formTime)
                self.lastmsg.setText(msgData[mainName][-1]['message'])
                self.machinelab.setText(msgData[mainName][-1]['machine'])
            else:
                self.artistlab.setText('')
                self.updatedatelab.setText('')
                self.lastmsg.setText('')
                self.machinelab.setText('')

            if mainName in infoData.keys():
                self.confirmdatelab.setText(infoData[mainName])
                hasConfirm = True
            else:
                self.confirmdatelab.setText('')
            if 'startTime' in infoData.keys():
                self.startdatelab.setText(infoData['startTime'])
                hasStart = True
            else:
                self.startdatelab.setText('')

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

            self.passinglab.setText(passingStr)


#sam = shaderAssetManager()

#sam.Op_Ui()
