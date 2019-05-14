# -*- coding: utf-8 -*-
import hashlib


class assetManager_RigBoxUI(assetManager_BaseClass):
    nowHighModelLocal = ''
    nowHighModelServer = ''
    nowLowModelLocal = ''
    nowLowModelServer = ''

    def extraInit(self):
        self.departmentName = 'RIG'
        self.projectName = 'PIG'

    def howToUseFn(self):
        dirPath = self.initPath
        docxPath = dirPath + '\\maya2016\\' + self.departmentName + '\\help.docx'
        docPath = dirPath + '\\maya2016\\' + self.departmentName + '\\help.doc'
        if os.path.exists(docPath):
            os.system(docPath)
            return True
        if os.path.exists(docxPath):
            os.system(docxPath)

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

    def createGeneralTab(self):
        toolMn = QtGui.QMenu('Tool', self.MainMenuBar)
        self.MainMenuBar.addMenu(toolMn)
        tool1act = toolMn.addAction("change texture Path")
        tool2act = toolMn.addAction("TD's tool")

        self.GWid = QtGui.QWidget()
        self.GWid.setAttribute(Qt.WA_StyledBackground)
        self.GWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        self.GWid.setAttribute(Qt.WA_DeleteOnClose)
        self.GWid.setAttribute(Qt.WA_StyledBackground)

        msgVB = QtGui.QVBoxLayout()

        titleHB = QtGui.QHBoxLayout()

        self.preBtn = QtGui.QToolButton()
        self.preBtn.setText('<--')
        self.preBtn.setToolTip('pre item')
        self.preBtn.setIcon(QtGui.QIcon(self.iconPath + '\\prePage_red.png'))
        self.preBtn.setIconSize(QtCore.QSize(16, 16))
        self.preBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.preBtn.setAutoRaise(True)

        self.titleLabel = QtGui.QLabel('charactorName')
        self.titleLabel.setToolTip('charactorName')
        self.titleLabel.setStyleSheet(Mstyle.QLabel(fontSize='20px'))

        self.nextBtn = QtGui.QToolButton()
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

        picHbox = QtGui.QHBoxLayout()
        self.plabPic = clickLabel('', self)
        self.plabPic.setToolTip('undefined')
        self.plabPic.setPixmap(self.chaPixmap)
        self.plabPic.setMaximumWidth(300)
        self.plabPic.resize(self.chaPixmap.width(), self.chaPixmap.height())
        picHbox.addWidget(self.plabPic)
        msgVB.addLayout(picHbox)

        modelGrp = QtGui.QGroupBox('model')
        modelGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        modelGrp.setMaximumHeight(120)
        modGVB = QtGui.QVBoxLayout()
        modGVB.setContentsMargins(5, 5, 5, 5)
        modGVB.setSpacing(4)
        modGHB1 = QtGui.QHBoxLayout()
        modGHB2 = QtGui.QHBoxLayout()
        modGHB3 = QtGui.QHBoxLayout()
        modGHB4 = QtGui.QHBoxLayout()

        servModHigh = QtGui.QLabel('Serv-High : ', self.GWid)
        servModHigh.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB1.addWidget(servModHigh)
        modGHB1.addStretch(1)

        self.serverModHighdata = QtGui.QLabel('', self.GWid)
        self.serverModHighdata.setToolTip('print servModel High')
        self.serverModHighdata.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB1.addWidget(self.serverModHighdata)
        modGHB1.addStretch(1)

        localModhigh = QtGui.QLabel('Local-High  : ', self.GWid)
        localModhigh.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB2.addWidget(localModhigh)
        modGHB2.addStretch(1)

        self.localModHighdata = QtGui.QLabel('', self.GWid)
        self.localModHighdata.setToolTip('print localModel High')
        self.localModHighdata.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB2.addWidget(self.localModHighdata)
        modGHB2.addStretch(1)

        modGHBtn = QtGui.QHBoxLayout()
        downloadModHighBtn = QtGui.QPushButton('update')
        downloadModHighBtn.setStyleSheet(Mstyle.QPushButton(bordRad='8px'))
        downloadModHighBtn.setToolTip('highUpdate')
        refrenceModHighBtn = QtGui.QPushButton('refrence')
        refrenceModHighBtn.setStyleSheet(Mstyle.QPushButton(bordRad='8px', kw='b'))
        refrenceModHighBtn.setToolTip('highRefrence')
        modGHBtn.addWidget(downloadModHighBtn)
        modGHBtn.addWidget(refrenceModHighBtn)

        servModLow = QtGui.QLabel('Serv-Low  : ', self.GWid)
        servModLow.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB3.addWidget(servModLow)
        modGHB3.addStretch(1)
        self.serverModLowdata = QtGui.QLabel('', self.GWid)
        self.serverModLowdata.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.serverModLowdata.setToolTip('print servModel Low')
        modGHB3.addWidget(self.serverModLowdata)
        modGHB3.addStretch(1)

        localModLow = QtGui.QLabel('Local-Low  : ', self.GWid)
        localModLow.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB4.addWidget(localModLow)
        modGHB4.addStretch(1)
        self.localModLowdata = QtGui.QLabel('', self.GWid)
        self.localModLowdata.setToolTip('print localModel Low')
        self.localModLowdata.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB4.addWidget(self.localModLowdata)
        modGHB4.addStretch(1)

        modGHB44 = QtGui.QHBoxLayout()
        downloadModLowBtn = QtGui.QPushButton('update')
        downloadModLowBtn.setStyleSheet(Mstyle.QPushButton(bordRad='8px'))
        downloadModLowBtn.setToolTip('lowUpdate')
        refrenceModLowBtn = QtGui.QPushButton('refrence')
        refrenceModLowBtn.setStyleSheet(Mstyle.QPushButton(bordRad='8px', kw='b'))
        refrenceModLowBtn.setToolTip('lowRefrence')
        modGHB44.addWidget(downloadModLowBtn)
        modGHB44.addWidget(refrenceModLowBtn)

        modGVB.addLayout(modGHB3)
        modGVB.addLayout(modGHB4)
        modGVB.addLayout(modGHB44)

        modGVB.addLayout(modGHB1)
        modGVB.addLayout(modGHB2)
        modGVB.addLayout(modGHBtn)
        modelGrp.setLayout(modGVB)
        msgVB.addWidget(modelGrp)

        self.infoGrp = QtGui.QGroupBox('infomation')
        self.infoGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        self.infoGrp.setMaximumHeight(150)
        infoGVB = QtGui.QVBoxLayout()

        lastmsgHB = QtGui.QHBoxLayout()
        labLastMsgTitle = QtGui.QLabel('LastMsg : ', self.GWid)
        labLastMsgTitle.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.lastmsg = QtGui.QLabel('', self.GWid)

        self.lastmsg.setToolTip('lastmsg')
        self.lastmsg.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b', lang='c'))
        lastmsgHB.addWidget(labLastMsgTitle)
        lastmsgHB.addWidget(self.lastmsg)
        lastmsgHB.addStretch(1)

        infoGHB1 = QtGui.QHBoxLayout()
        lab4 = QtGui.QLabel('Artist : ', self.GWid)
        lab4.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.artistlab = QtGui.QLabel('', self.GWid)
        self.artistlab.setToolTip('artist')
        self.artistlab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        infoGHB1.addWidget(lab4)
        infoGHB1.addWidget(self.artistlab)
        infoGHB1.addStretch(1)

        infoGHB2 = QtGui.QHBoxLayout()
        lab5 = QtGui.QLabel('Passing : ', self.GWid)
        lab5.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.passinglab = QtGui.QLabel('none days', self.GWid)
        self.passinglab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        self.passinglab.setToolTip('passing')
        infoGHB2.addWidget(lab5)
        infoGHB2.addWidget(self.passinglab)
        infoGHB2.addStretch(1)

        infoGHB3 = QtGui.QHBoxLayout()
        lab6 = QtGui.QLabel('StartDate :     ', self.GWid)
        lab6.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.startdatelab = QtGui.QLabel('', self.GWid)
        self.startdatelab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        self.startdatelab.setToolTip('startdate')
        infoGHB3.addWidget(lab6)
        infoGHB3.addWidget(self.startdatelab)
        infoGHB3.addStretch(1)

        infoGHB6 = QtGui.QHBoxLayout()
        lab11 = QtGui.QLabel('UploadDate : ', self.GWid)
        lab11.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.updatedatelab = QtGui.QLabel('', self.GWid)
        self.updatedatelab.setToolTip('uploaddate')
        self.updatedatelab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        infoGHB6.addWidget(lab11)
        infoGHB6.addWidget(self.updatedatelab)
        infoGHB6.addStretch(1)

        infoGHB4 = QtGui.QHBoxLayout()
        lab7 = QtGui.QLabel('ConfirmData : ', self.GWid)
        lab7.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.confirmdatelab = QtGui.QLabel('', self.GWid)
        self.confirmdatelab.setToolTip('confirmdate')
        self.confirmdatelab.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        infoGHB4.addWidget(lab7)
        infoGHB4.addWidget(self.confirmdatelab)
        infoGHB4.addStretch(1)

        infoGHB5 = QtGui.QHBoxLayout()
        lab8 = QtGui.QLabel('Machine : ', self.GWid)
        lab8.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        self.machinelab = QtGui.QLabel('', self.GWid)
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

        oprGrp = QtGui.QGroupBox('opreate')
        oprGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        oprGrp.setMaximumHeight(150)
        oprGVB = QtGui.QVBoxLayout()

        oprGHB1 = QtGui.QHBoxLayout()
        oprbtn_upload = QtGui.QPushButton('upload', self.GWid)
        oprbtn_upload.setFixedHeight(25)
        oprbtn_upload.setStyleSheet(Mstyle.QPushButton(bordRad='12px'))
        oprbtn_upload.setToolTip('open upload window')
        oprGHB1.addWidget(oprbtn_upload)

        oprGHB2 = QtGui.QHBoxLayout()
        oprbtn_confirm = QtGui.QPushButton('confirm', self.GWid)
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

        tool2act.triggered.connect(self.tool2actFn)
        downloadModLowBtn.clicked.connect(self.downloadFn)
        downloadModHighBtn.clicked.connect(self.downloadFn)

        refrenceModHighBtn.clicked.connect(self.refrenceFn)
        refrenceModLowBtn.clicked.connect(self.refrenceFn)

    def loadGeneralPageData(self):
        changeTabItm = self.nowSelMainTreeItem
        tyStr = ''
        if self.nowTreePage == 'Char':
            tyStr = 'cha'
        else:
            tyStr = self.nowTreePage.lower()

        filenameHigh = self.projectName + '_' + tyStr + '_' + changeTabItm.text(
            0) + '_mod_high.ma'
        filenameLow = self.projectName + '_' + tyStr + '_' + changeTabItm.text(
            0) + '_mod_low.ma'

        filePath = self.serverPath + '\\asset\\' + self.departmentName + '\\' + self.nowTreePage + '\\' + changeTabItm.text(
            0) + '\\'
        files = self.getFiles(filePath)
        hasPic = []
        for f in files:
            if '.png' in f:
                hasPic.append(filePath + f)

        if hasPic:
            self.nowPicPath = hasPic[0]
        else:
            self.nowPicPath = self.iconPath + '\\currentPic.png'
        self.plabPic.pixmap().load(self.nowPicPath)
        scalePic = self.plabPic.pixmap().scaledToWidth(300)
        self.plabPic.setPixmap(scalePic)
        self.plabPic.setToolTip(self.nowPicPath)
        # load picmap under folder over

        # load title label
        self.titleLabel.setText(changeTabItm.text(0))

        # load model info
        sp = self.serverPath.split('\\')
        sp.append('asset')
        sp.append('MODEL')
        sp.append(self.nowTreePage)
        sp.append(changeTabItm.text(0))
        preDepartmentPath = '\\'.join(sp)

        self.nowHighModelServer = preDepartmentPath + '\\' + filenameHigh
        servHighDate = ''
        self.nowLowModelServer = preDepartmentPath + '\\' + filenameLow
        servLowDate = ''

        if os.path.exists(preDepartmentPath):
            if os.path.exists(self.nowHighModelServer):
                gettime = os.path.getmtime(self.nowHighModelServer)
                servHighDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(gettime))

            if os.path.exists(self.nowLowModelServer):
                gettime = os.path.getmtime(self.nowLowModelServer)
                servLowDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(gettime))
        else:
            os.makedirs(preDepartmentPath)

        # get preDepartment info over.path and date of high and low models.

        sp = self.serverPath.split('\\')
        sp.append('asset')
        sp.append(self.departmentName)
        sp.append(self.nowTreePage)
        sp.append(changeTabItm.text(0))
        sp.append('DownloadModel')
        self.downloadPath = '\\'.join(sp)

        self.nowHighModelLocal = self.downloadPath + '\\' + filenameHigh
        localHighDate = ''
        self.nowLowModelLocal = self.downloadPath + '\\' + filenameLow
        localLowDate = ''

        if os.path.exists(self.downloadPath):

            if os.path.exists(self.nowHighModelLocal):
                gettime = os.path.getmtime(self.nowHighModelLocal)
                localHighDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(gettime))
            if os.path.exists(self.nowLowModelLocal):
                gettime = os.path.getmtime(self.nowLowModelLocal)
                localLowDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(gettime))
        else:
            os.makedirs(self.downloadPath)

        self.localModLowdata.setText(localLowDate)
        self.serverModLowdata.setText(servLowDate)
        self.localModHighdata.setText(localHighDate)
        self.serverModHighdata.setText(servHighDate)

        # load concept infomations over

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

    def refrenceFn(self):
        itemNode = self.nowSelMainTreeItem
        sender = self.sender()
        path = self.serverPath + '\\asset\\' + self.departmentName + '\\' + self.nowTreePage + '\\' + itemNode.text(
            0) + '\\DownloadModel\\'

        keyword = '_low.ma'
        if 'high' in sender.toolTip():
            keyword = '_high.ma'

        thefile = ''
        dirs = os.listdir(path)
        for i in dirs:
            if keyword in i:
                thefile = path + i

        if os.path.exists(thefile):
            cmds.file(thefile, reference=True, type='mayaAscii', namespace='mod')
        else:
            print 'file not exists,you need update file from pre-department'

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

    def downloadFn(self):

        sender = self.sender()
        buttonKey = ''

        if 'low' in sender.toolTip():
            buttonKey = 'low'
            if self.nowLowModelServer:
                if os.path.exists(self.nowLowModelLocal):
                    os.remove(self.nowLowModelLocal)

                shutil.copyfile(self.nowLowModelServer, self.nowLowModelLocal)
                shutil.copystat(self.nowLowModelServer, self.nowLowModelLocal)
            else:
                print 'low file not exists'
                return False

        if 'high' in sender.toolTip():
            buttonKey = 'high'
            if self.nowHighModelServer:
                if os.path.exists(self.nowHighModelLocal):
                    os.remove(self.nowHighModelLocal)

                shutil.copyfile(self.nowHighModelServer, self.nowHighModelLocal)
                shutil.copystat(self.nowHighModelServer, self.nowHighModelLocal)
            else:
                print 'high file not exists'
                return False

        changeTabItm = self.nowSelMainTreeItem

        artName = ''
        if self.fileMn.title().lower() != 'login':
            artName = self.fileMn.title()
        else:
            artName = getpass.getuser()

        sDate = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime(time.time()))

        dataDict = {'artist': artName, 'date': sDate, 'machine': getpass.getuser(), 'message': 'download ' + buttonKey,
                    'type': 'downloadPreDepartment'}

        dict = self.loadJson(self.timeNodePath)
        firstData = dict['firstDownload']
        for key, itm in firstData.items():
            if not itm:
                dict['firstDownload'] = dataDict

        dict['lastDownload'] = dataDict
        dict['log'].append(dataDict)

        self.saveJson(dict, self.timeNodePath)

        self.loadGeneralPageData()
        # load and add general page data .over


        historypath = self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + changeTabItm.text(
            0) + '\\history.html'
        if not (os.path.exists(historypath)):
            self.HTML_CreateEmptyStyle(historypath)

        innerMsg = '[ ' + self.departmentName + ' ] copy the concept from concept path to model path'
        htmlMsg = self.HTML_createMsg(innerMsg, artName, '', side=1, initPath=self.initPath)
        self.HTML_addMsg(historypath, htmlMsg)

        # html message over
        return True

    def oprbtn_openConfirmFn(self):
        if self.treeWid.currentItem():
            itemNode = self.nowSelMainTreeItem
            tyStr = ''
            if self.nowTreePage == 'Char':
                tyStr = 'cha'
            else:
                tyStr = self.nowTreePage.lower()

            servSp = self.serverPath.split('\\')
            servSp.append('asset')
            servSp.append(self.departmentName)
            servSp.append(self.nowTreePage)
            servSp.append(itemNode.text(0))
            servSp.append('uploadTemp')
            servPath = '\\'.join(servSp)

            if os.path.exists(servPath):
                confirm = assetManager_confirmTool()
                confirm.setParent(self)
                confirm.searchPath = servPath
                confirm.workName = itemNode.text(0)
                confirm.createUI()
                confirm.fillListWidget()
                confirm.localPath = self.localPath
                confirm.serverPath = self.serverPath
                confirm.Op_Ui()
                #confirm.BtnA2.setEnabled(True)
                confirm.resize(self.width(), self.height())
                confirm.confirmClicked.connect(self.confirmFn)
                confirm.checkClicked.connect(self.confirmCheckFn)
            else:
                print 'no upload log.can not open confirm dialog'
        else:
            print 'need select item first'

    def oprbtn_openUploadFn(self):
        submitTool = assetManager_submitTool()
        submitTool.getNotifyFromTxt(self.initPath + '\\maya2016\\' + self.departmentName + '\\notify.txt')
        submitTool.createUI()
        submitTool.setParent(self)
        # submitTool.BtnA2.setVisible(False)
        submitTool.BtnA1.setText('upload_high')
        submitTool.BtnA1.setEnabled(False)
        submitTool.BtnA2.setText('upload_low')
        submitTool.BtnA2.setEnabled(False)
        submitTool.Op_Ui()

        submitTool.lowClicked.connect(self.oprbtn_uploadFn)
        submitTool.highClicked.connect(self.oprbtn_uploadFn)
        submitTool.resize(self.width(), self.height())

    def oprbtn_uploadFn(self, data):

        changeTabItm = self.nowSelMainTreeItem

        reply = QtGui.QMessageBox.information(self,
                                              "double check",
                                              ("upload to\n" + str(changeTabItm.text(0))),
                                              QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        # double check

        if reply == QtGui.QMessageBox.Yes:

            userName = str(self.fileMn.title())
            if userName.lower() == 'login':
                userName = getpass.getuser()
            # get user name from label

            uploadTime = time.localtime(time.time())
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

            uploadVersion = 'low'
            if data[0] == 'h':
                uploadVersion = 'high'

            linedate = time.strftime("%Y%m%d%H%M%S", uploadTime)
            filename = self.projectName + '_' + tyStr + '_' + changeTabItm.text(
                0) + '_' + self.departmentName.lower() + '_' + uploadVersion + '.ma'
            uploadPath = chaPath + '\\uploadTemp\\' + uploadVersion + '\\' + linedate + '\\'
            os.makedirs(uploadPath)
            # get upload path and create date folder

            cmds.file(rename=uploadPath + filename)
            cmds.file(save=True, type='mayaAscii')
            # upload .ma file over



            nowdate = time.strftime("%Y-%m-%d %H:%M:%S ", uploadTime)

            dataDict = {'artist': userName, 'date': nowdate, 'machine': getpass.getuser(), 'message': data[-1],
                        'type': 'upload'}

            dict = self.loadJson(self.timeNodePath)
            dict['lastUpload'] = dataDict
            dict['log'].append(dataDict)

            self.saveJson(dict, uploadPath + 'timeNode.json')
            self.saveJson(dict, self.timeNodePath)
            self.loadGeneralPageData()
            # save infomation json

            shutil.copyfile(data[1], uploadPath + '\\sceenshot.png')
            shutil.copystat(data[1], uploadPath + '\\sceenshot.png')
            # copy screenshot form local to server
            mel.eval('print "done"')

            producePath = self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + changeTabItm.text(0)
            if not (os.path.exists(producePath)):
                os.makedirs(producePath)
            historypath = producePath + '\\history.html'
            if not (os.path.exists(historypath)):
                self.HTML_CreateEmptyStyle(historypath)
            # make sure produce folder

            innerMsg = '[ ' + self.departmentName + ' ][ upload ] ' + ' <br> updateTime : ' + time.strftime(
                "%Y-%m-%d %H:%M:%S",
                uploadTime) + '<br>update by ' + userName
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
                if spUf[-1] == 'json':
                    continue
                else:
                    try:
                        os.remove(mainPathFile)
                    except:
                        print mainPathFile + 'cannot update'
                        continue
            if uf[0] != '.':
                if not (spUf[-1] in ['ma', 'json']):
                    shutil.copyfile(updatePathFile, mainPathFile)
                    shutil.copystat(updatePathFile, mainPathFile)
                elif spUf[-1] == 'ma':
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
        tempTimeNode = tempPath + '\\timeNode.json'
        tempDict = self.loadJson(tempTimeNode)

        dataDict = {'artist': userName, 'date': nowTime, 'machine': getpass.getuser(),
                    'message': tempDict['lastUpload']['message'], 'type': 'confirm'}

        dict = self.loadJson(self.timeNodePath)
        dict['lastConfirm'] = dataDict
        dict['log'].append(dataDict)

        self.saveJson(dict, tempTimeNode)
        self.saveJson(dict, self.timeNodePath)

        producePath = self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + itemNode.text(0)
        if not (os.path.exists(producePath)):
            os.makedirs(producePath)
        historypath = producePath + '\\history.html'
        if not (os.path.exists(historypath)):
            self.HTML_CreateEmptyStyle(historypath)

        innerMsg = '[ ' + self.departmentName + ' ][ confirm ] ' + ' <br> confirmTime : ' + nowTime + '<br>confirm by ' + userName
        htmlMsg = self.HTML_createMsg(innerMsg, userName, '', side=1, initPath=self.initPath)
        self.HTML_addMsg(historypath, htmlMsg)

        self.loadGeneralPageData()

    def Op_Ui(self):
        self.show()
        self.resize(450, 900)
        self.move(100, 100)
        self.setDockableParameters(dockable=True, floating=False, area='left')

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

# sam = assetManager_RigBoxUI()

# sam.Op_Ui()
