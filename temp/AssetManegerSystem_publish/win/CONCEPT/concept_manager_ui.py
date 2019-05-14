# -*- coding: utf-8 -*-
# pyqt4 in windows everioment


# Form implementation generated from reading ui file 'conceptLayout.ui'
#
# Created: Fri Nov 17 15:54:43 2017
#      by: PyQt4 UI code generator 4.10.3
# 2017-12-8 17:32:14 figo
#   finished the main funciton
#   we need cache all the pictures in this program.but now i doesn't work on this function,maybe later
#   concept department temp function finished,in tabwidget page 3
#   now I work on the tabwidget page 1.


from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt
import sys, os, time, json, shutil, sqlite3, getpass, datetime

reload(sys)
sys.setdefaultencoding('utf-8')
filePath = os.path.realpath(__file__)
filePathsp = filePath.split('AssetManegerSystem_publish')

path = filePathsp[0] + '\\AssetManegerSystem_publish'
if not path in sys.path: sys.path.append(path)
if not path + '\\data' in sys.path: sys.path.append(path + '\\data')
if not path + '\\win\\bin' in sys.path: sys.path.append(path + '\\win\\bin')
if not path + '\\win\\CONCEPT' in sys.path: sys.path.append(path + '\\win\\CONCEPT')

import script
import redBlackStyleSheet_0_10 as RBStyle

Mstyle = RBStyle.RedBlackStyleSheet()
Mstyle.setIconPath(script.getAssetManagerPath()['icon'])

import win_baseClass as BC
import text_dargbox as dragBox

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)




class ConceptManagerBoxUI(BC.assetManagerBoxUI_win_baseClass):
    titleName = 'ConceptManagerBoxUI'
    widgetHeight = 750
    widgetWidth = 600




    def extraInit(self):
        self.departmentName = 'CONCEPT'

    def howToUseFn(self):
        pass

    def createAcceptTab(self):
        listWid = QtGui.QWidget()
        listWid.setAttribute(Qt.WA_StyledBackground)
        listWid.setStyleSheet('QWidget{background:rgb(109,109,109);border-radius: 12px}')
        listWid.setAttribute(Qt.WA_DeleteOnClose)

        listVB = QtGui.QVBoxLayout()
        listVB.setContentsMargins(0, 0, 0, 0)
        listVB.setSpacing(0)

        listHbox = QtGui.QHBoxLayout()
        listHbox.setContentsMargins(0, 0, 0, 0)
        listHbox.setSpacing(0)

        listAcceptBtn = QtGui.QPushButton('accept')
        listAcceptBtn.setStyleSheet(Mstyle.QPushButton(kw='c'))
        listAcceptBtn.setToolTip('accept')
        listAcceptBtn.setFixedHeight(40)

        listEditBtn = QtGui.QPushButton('show')
        listEditBtn.setStyleSheet(Mstyle.QPushButton(kw='c'))
        listEditBtn.setToolTip('show')
        listEditBtn.setFixedHeight(40)
        listEditBtn.setEnabled(True)

        listRefuseBtn = QtGui.QPushButton('refuse')
        listRefuseBtn.setStyleSheet(Mstyle.QPushButton(kw='c'))
        listRefuseBtn.setToolTip('refuse')
        listRefuseBtn.setFixedHeight(40)

        listHbox.addWidget(listAcceptBtn)
        listHbox.addWidget(listEditBtn)
        listHbox.addWidget(listRefuseBtn)

        self.listLE = QtGui.QListWidget()
        self.listLE.verticalScrollBar().setStyleSheet(Mstyle.QScrollBar())
        self.listLE.setIconSize(QtCore.QSize(48, 48))
        self.listLE.setLayoutMode(QtGui.QListWidget.Batched)

        listLineE = QtGui.QLineEdit()
        listLineE.setText('search bar')
        listLineE.setAlignment(Qt.AlignHCenter)
        listLineE.setFixedHeight(24)
        listLineE.setStyleSheet(Mstyle.QLineEdit(fontSize='14px', bordRad='12px', kw='d', lang='c'))

        listVB.addWidget(listLineE)
        listVB.addWidget(self.listLE)
        listVB.addLayout(listHbox)
        listWid.setLayout(listVB)
        self.tabWid.addTab(listWid, 'List')

        listAcceptBtn.pressed.connect(self.acceptConceptFn)
        listRefuseBtn.pressed.connect(self.refuseConceptFn)
        listEditBtn.pressed.connect(self.showConceptFn)
        listLineE.cursorPositionChanged.connect(self.clearSreachBar)

        listLineE.textChanged.connect(self.searchListNote)


    def searchListNote(self, str):
        # print str
        itmCount = self.listLE.count()
        for i in range(itmCount):
            itmCell = self.listLE.item(i)
            if str in itmCell.text():  # .encode('utf-8')
                itmCell.setHidden(False)
                # print itmCell.text()
            else:
                itmCell.setHidden(True)


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

    # arrow functions over


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

    # changed functions over

    def showConceptFn(self):
        itm = self.listLE.currentItem()

        servSp = self.serverPath.split('\\')
        servSp.append('asset')
        servSp.append(self.departmentName)
        servSp.append(self.nowTreePage)
        servSp.append(str(self.nowSelMainTreeItem.text(0)))

        servSp.append('uploadTemp')
        servSp.append(str(itm.text().split('\n')[0]))
        tempPath = '\\'.join(servSp)
        os.startfile(tempPath)

    def refuseConceptFn(self):
        itm = self.listLE.currentItem()
        emptyColor = QtGui.QColor(Qt.transparent)
        itm.setBackground(emptyColor)

        servSp = self.serverPath.split('\\')
        servSp.append('asset')
        servSp.append(self.departmentName)
        servSp.append(self.nowTreePage)
        servSp.append(str(self.nowSelMainTreeItem.text(0)))
        mainPath = '\\'.join(servSp)
        servSp.append('uploadTemp')
        servSp.append('acceptList.json')
        jsonPath = '\\'.join(servSp)
        jsonData = {}
        if os.path.exists(jsonPath):
            jsonData = self.loadJson(jsonPath)
        else:
            self.saveJson(jsonData, jsonPath)
        itmTxt = str(itm.text().split('\n')[0])
        if itmTxt in jsonData.keys():
            jsonData[itmTxt] = False
        else:
            jsonData.update({itmTxt: False})
        self.saveJson(jsonData, jsonPath)
        # save the accept infomation to acceptList.json

        tarPath = mainPath + '\\' + itmTxt
        spName = ''
        if os.path.exists(tarPath):
            os.remove(tarPath)
            spName = itmTxt.split('.')[0]

            os.remove(mainPath + '\\' + spName + '_small.jpg')
            os.remove(mainPath + '\\' + spName + '_middle.jpg')

        rDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        historypath = self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + str(
            self.nowSelMainTreeItem.text(0)) + '\\history.html'
        if not (os.path.exists(historypath)):
            self.HTML_CreateEmptyStyle(historypath)

        userName = self.getUser()
        innerMsg = '[ CONCEPT ][ refuse ] ' + spName + ' <br> refuseTime : ' + rDate + '<br>refuse by ' + userName
        htmlMsg = self.HTML_createMsg(innerMsg, userName, '', side=1, initPath=self.initPath)
        self.HTML_addMsg(historypath, str(htmlMsg))

    def acceptConceptFn(self):
        itm = self.listLE.currentItem()
        linearGradient = QtGui.QLinearGradient(60, 50, 200, 200)
        linearGradient.setColorAt(0, Qt.transparent)
        linearGradient.setColorAt(0.89, Qt.transparent)
        linearGradient.setColorAt(0.9, QtGui.QColor(200, 200, 200))
        linearGradient.setColorAt(0.94, QtGui.QColor(200, 200, 200))
        linearGradient.setColorAt(0.95, QtGui.QColor(0, 200, 0))
        linearGradient.setColorAt(1.0, QtGui.QColor(0, 200, 0))
        itm.setBackground(QtGui.QBrush(linearGradient))
        # draw color in listLE.item for green

        servSp = self.serverPath.split('\\')
        servSp.append('asset')
        servSp.append('CONCEPT')
        servSp.append(self.nowTreePage)
        servSp.append(str(self.nowSelMainTreeItem.text(0)))
        mainPath = '\\'.join(servSp)
        servSp.append('uploadTemp')
        tempPath = '\\'.join(servSp)
        servSp.append('acceptList.json')
        jsonPath = '\\'.join(servSp)
        jsonData = {}
        if os.path.exists(jsonPath):
            jsonData = self.loadJson(jsonPath)
        else:
            self.saveJson(jsonData, jsonPath)
        itmTxt = str(itm.text().split('\n')[0])
        if itmTxt in jsonData.keys():
            jsonData[itmTxt] = True
        else:
            jsonData.update({itmTxt: True})
        self.saveJson(jsonData, jsonPath)
        # save the accept infomation to acceptList.json

        sorPath = tempPath + '\\' + itmTxt
        tarPath = mainPath + '\\' + itmTxt
        if os.path.exists(tarPath):
            os.remove(tarPath)
        shutil.copyfile(sorPath, tarPath)
        shutil.copystat(sorPath, tarPath)
        # copy big picture
        spName = itmTxt.split('.')[0]

        shutil.copyfile(tempPath + '\\' + spName + '_small.jpg', mainPath + '\\' + spName + '_small.jpg')
        shutil.copystat(tempPath + '\\' + spName + '_small.jpg', mainPath + '\\' + spName + '_small.jpg')

        shutil.copyfile(tempPath + '\\' + spName + '_middle.jpg', mainPath + '\\' + spName + '_middle.jpg')
        shutil.copystat(tempPath + '\\' + spName + '_middle.jpg', mainPath + '\\' + spName + '_middle.jpg')
        # copy file to main path.

        sorLog = tempPath + '\\message.json'
        tarLog = mainPath + '\\message.json'
        if os.path.exists(tarLog):
            os.remove(tarLog)
        shutil.copyfile(sorLog, tarLog)
        shutil.copystat(sorLog, tarLog)

        msgData = self.loadJson(tarLog)
        uString = msgData[itmTxt][-1]['updateDate']
        uTime = '{}-{}-{} {}:{}:{}'.format(uString[0:4], uString[4:6], uString[6:8], uString[8:10], uString[10:12],
                                           uString[12:14])
        uUser = msgData[itmTxt][-1]['artist']
        # update the infomations to mainPath

        tarInfo = mainPath + '\\infomation.json'
        # confirm time and start time
        tarData = {}
        if os.path.exists(tarInfo):
            tarData = self.loadJson(tarInfo)
        else:
            self.saveJson(tarData, tarInfo)

        cDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        if not ('confirm' in tarData.keys()):
            tarData.update({'startTime': cDate})
        # itmTxt=str(itm.text().split('\n')[0])
        if itmTxt in tarData.keys():
            tarData[itmTxt] = cDate
        else:
            tarData.update({itmTxt: cDate})
        self.saveJson(tarData, tarInfo)
        # list page button functions over

        historypath = self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + str(
            self.nowSelMainTreeItem.text(0)) + '\\history.html'
        if not (os.path.exists(historypath)):
            self.HTML_CreateEmptyStyle(historypath)

        userName = self.getUser()
        innerMsg = '[ CONCEPT ][ confirm ] ' + spName + ' <br> updateTime : ' + uTime + '<br>update by ' + uUser + ' <br> confirmTime : ' + cDate + '<br>confirm by ' + userName
        htmlMsg = self.HTML_createMsg(innerMsg, userName, '', side=1, initPath=self.initPath)
        self.HTML_addMsg(historypath, str(htmlMsg))

        nextPartSp = self.serverPath.split('\\')
        nextPartSp.append('asset')
        nextPartSp.append('MODEL')
        nextPartSp.append(self.nowTreePage)
        nextPartSp.append(str(self.nowSelMainTreeItem.text(0)))
        npPath = '\\'.join(nextPartSp)
        if not os.path.exists(npPath):
            os.makedirs(npPath)

    def oprbtn_openUploadFn(self):
        box = dragBox.PictureUploadUI()
        box.setParent(self)
        box.Op_Ui()
        box.upload.connect(self.picUploadFn)
        box.move(0, 0)
        box.resize(self.width(), self.height())

    def copyConceptToModelFn(self):
        # print self.conceptPath
        # print self.conceptDownloadPath

        conceptArray = []
        concepttime = ''
        if os.path.exists(self.conceptPath):
            cFiles = os.listdir(self.conceptPath)
            for c in cFiles:
                if '.jpg' in c:
                    conceptArray.append(self.conceptPath + '\\' + c)
                    gettime = os.path.getmtime(self.conceptPath + '\\' + c)
                    if gettime > concepttime or concepttime == '':
                        concepttime = gettime
        else:
            pass

        modelArray = []
        modeltime = ''
        if os.path.exists(self.conceptDownloadPath):
            dFiles = os.listdir(self.conceptDownloadPath)
            for d in dFiles:
                if '.jpg' in d:
                    modelArray.append(self.conceptDownloadPath + '\\' + d)
                    gettime = os.path.getmtime(self.conceptDownloadPath + '\\' + d)
                    if gettime > modeltime or modeltime == '':
                        modeltime = gettime
        else:
            pass

        # copy the concept from CONCEPT to CONCEPT and local CONCEPT
        if modeltime == '' or concepttime > modeltime:
            files = os.listdir(self.conceptDownloadPath)
            if files:
                for f in files:
                    checkpath = self.conceptDownloadPath + '\\' + f
                    if os.path.isfile(checkpath):
                        os.remove(checkpath)
            # clear files above the path.

            timeStr = time.strftime("%Y%m%d%H%M%S", time.localtime(concepttime))
            backupPath = self.conceptDownloadPath + '\\history\\' + timeStr
            if os.path.exists(backupPath):
                files = os.listdir(backupPath)
                if files:
                    for f in files:
                        checkpath = backupPath + '\\' + f
                        if os.path.isfile(checkpath):
                            os.remove(checkpath)
            else:
                os.makedirs(backupPath)

            for c in conceptArray:
                base = os.path.basename(c)
                targetBase = backupPath + '\\' + base
                targetView = self.conceptDownloadPath + '\\' + base

                shutil.copyfile(c, targetBase)
                shutil.copystat(c, targetBase)
                shutil.copyfile(c, targetView)
                shutil.copystat(c, targetView)
            # copy to CONCEPT over



            itm = self.treeWid.currentItem()
            changeTabItm = ''
            if itm.parent():
                changeTabItm = itm.parent()
            else:
                changeTabItm = itm

            infoPath = self.serverPath + '\\asset\\CONCEPT\\' + self.nowTreePage + '\\' + changeTabItm.text(
                0) + '\\infomation.json'
            dict = self.loadJson(infoPath)

            artName = ''
            if self.fileMn.title().lower() != 'login':
                artName = self.fileMn.title()
            else:
                artName = getpass.getuser()
            if not (artName in dict['artist']):
                dict['artist'].append(artName)

            sDate = time.strftime("%m-%d %H:%M:%S %Y", time.localtime(time.time()))
            dict['startDate'].append(sDate)
            dict['machine'].append(getpass.getuser())
            self.saveJson(dict, infoPath)

            self.loadGeneralPageData()
            # load and add general page data .over


            historypath = self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + changeTabItm.text(
                0) + '\\history.html'
            if not (os.path.exists(historypath)):
                self.HTML_CreateEmptyStyle(historypath)

            userName = self.getUser()
            innerMsg = '[ CONCEPT ] {} copy the concept from concept path to model path'.format(userName)
            htmlMsg = self.HTML_createMsg(innerMsg, userName, '', side=1, initPath=self.initPath)
            self.HTML_addMsg(historypath, str(htmlMsg))

            # html message over
            return True


    def refrenceModelFn(self):

        path = self.serverPath + '\\asset\\CONCEPT\\' + self.nowTreePage + '\\' + self.itemNode.text(
            0) + '\\DownloadConcept'

        modelArray = []
        dFiles = os.listdir(path)
        for d in dFiles:
            if '.jpg' in d:
                modelArray.append(path + '\\' + d)

        localMainPath = path.replace(self.serverPath, self.localPath)
        if not os.path.exists(localMainPath):
            os.makedirs(localMainPath)

        for i in modelArray:
            localP = i.replace(self.serverPath, self.localPath)
            if os.path.exists(localP):
                localMtime = round(os.path.getmtime(localP), 2)
                serveMtime = round(os.path.getmtime(i), 2)
                # retain two decimal places

                if localMtime != serveMtime:
                    lt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(localMtime))
                    st = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(serveMtime))
                    message = os.path.basename(
                        localP) + '\n\nwhich one do you want...?\nlocal  : {}\nserver : {}'.format(lt, st)
                    rlt = cmds.confirmDialog(m=message, b=['local', 'server'])
                    if rlt == 'server':
                        os.remove(localP)
                        shutil.copyfile(i, localP)
                        shutil.copystat(i, localP)
                        # if the times are diffrent,use dialog to choose which one do you want.
            else:
                shutil.copyfile(i, localP)
                shutil.copystat(i, localP)

        os.startfile(localMainPath)

    def picUploadFn(self, list):
        # codec = QtCore.QTextCodec.codecForName("GB2312")
        # leftMsg = unicode(codec.toUnicode(list[0]))
        # codec = QtCore.QTextCodec.codecForName("utf-8")
        # gg = codec.toUnicode(list[0])
        # print gg

        localtime = time.localtime(time.time())
        nowtime = time.strftime("%Y%m%d%H%M%S", localtime)
        tyStr = ''
        if self.nowTreePage == 'Char':
            tyStr = 'cha'
        else:
            tyStr = self.nowTreePage.lower()

        servSp = self.serverPath.split('\\')
        servSp.append('asset')
        servSp.append(self.departmentName)
        servSp.append(self.nowTreePage)
        servSp.append(str(self.nowSelMainTreeItem.text(0)))
        servSp.append('uploadTemp')
        servPath = ''

        tempPath = '\\'.join(servSp)
        if not os.path.exists(tempPath):
            os.makedirs(tempPath)

        jsonPath = tempPath + '\\message.json'
        if not os.path.exists(jsonPath):
            emptyDic = {}
            self.saveJson(emptyDic, jsonPath)

        userName = str(self.fileMn.title())
        if userName.lower() == 'login':
            userName = getpass.getuser()

        jsonData = self.loadJson(jsonPath)
        fileString = ''
        for i in list[1]:
            filename = os.path.basename(str(i))
            spName = filename.split('.')
            tarPath = tempPath + '\\' + filename
            tarMid = tempPath + '\\' + spName[0] + '_middle.jpg'
            tarSmall = tempPath + '\\' + spName[0] + '_small.jpg'
            if os.path.exists(tarPath):
                quickMsg = QtGui.QMessageBox.question(self, "Question",
                                                      filename + '\nfile exists.do you want replace?',
                                                      QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel,
                                                      QtGui.QMessageBox.Ok)
                if quickMsg == QtGui.QMessageBox.Cancel:
                    continue
                os.remove(tarPath)
                if os.path.exists(tarMid):
                    os.remove(tarMid)
                if os.path.exists(tarSmall):
                    os.remove(tarSmall)
            shutil.copyfile(i, tarPath)
            shutil.copystat(i, tarPath)
            # copy orig pic

            origPic = QtGui.QPixmap(i)
            midPic = origPic.scaledToHeight(400)
            smallPic = origPic.scaledToHeight(100)
            midPic.save(tarMid)
            smallPic.save(tarSmall)
            # scale and copy

            fileString = fileString + filename + '<br>'
            if filename in jsonData.keys():
                item = jsonData[filename]
                item.append({"updateDate": nowtime,
                             "artist": userName,
                             "machine": getpass.getuser(),
                             "message": list[0]})
                jsonData[filename] = item
            else:

                jsonData.update({filename: [{"updateDate": nowtime,
                                             "artist": userName,
                                             "machine": getpass.getuser(),
                                             "message": list[0]}]})

        self.saveJson(jsonData, jsonPath)

        historypath = self.serverPath + '\\asset\\PRODUCE\\' + self.nowTreePage + '\\' + str(
            self.nowSelMainTreeItem.text(0)) + '\\history.html'
        if not (os.path.exists(historypath)):
            self.HTML_CreateEmptyStyle(historypath)

        userName = self.getUser()
        innerMsg = '[ CONCEPT ][ update ] upload <br>' + fileString + ' updateTime : ' + time.strftime(
            "%Y-%m-%d %H:%M:%S", localtime) + '<br>update by ' + userName + '<br> message:' + list[0]
        htmlMsg = self.HTML_createMsg(innerMsg, userName, '', side=1, initPath=self.initPath)
        self.HTML_addMsg(historypath, str(htmlMsg))

    def loadGeneralPageData(self):
        changeTabItm = self.nowSelMainTreeItem
        servDate = ''
        localDate = ''

        for c in self.tabWid.currentWidget().children():
            if type(c) == QtGui.QGroupBox:
                if c.title() == 'concept':
                    for cc in c.children():
                        if type(cc) != QtGui.QVBoxLayout:
                            if cc.toolTip() == 'print servDate':
                                servDate = cc
                            elif cc.toolTip() == 'print localDate':
                                localDate = cc

        filePath = self.serverPath + '\\asset\\CONCEPT\\' + self.nowTreePage + '\\' + str(changeTabItm.text(0)) + '\\'
        print '-------------'
        print filePath
        print '-------------'
        files = self.getFiles(filePath)
        hasPic = []
        print 'picture under folder'
        for f in files:
            if '.jpg' in f:
                print f
                if (not '_middle.jpg' in f) and (not '_small.jpg' in f):
                    hasPic.append(filePath + f)
        print '-------------'
        if hasPic:
            self.nowPicPath = hasPic[0]
        else:
            self.nowPicPath = self.initPath + '\\data\\currentPic.png'

        # load title label
        self.titleLabel.setText(changeTabItm.text(0))
        # load concept info
        sp = self.serverPath.split('\\')
        sp.append('asset')
        sp.append(self.departmentName)
        sp.append(self.nowTreePage)
        sp.append(str(changeTabItm.text(0)))
        self.conceptPath = '\\'.join(sp)
        print 'conceptPath is :' + self.conceptPath
        cFiles = os.listdir(self.conceptPath)
        conceptArray = []
        concepttime = ''
        conceptStrTime = ''
        if os.path.exists(self.conceptPath):
            for c in cFiles:
                if '.jpg' in c:
                    print 'file under path: ' + c
                    conceptArray.append(self.conceptPath + '\\' + c)
                    gettime = os.path.getmtime(self.conceptPath + '\\' + c)
                    if concepttime == '':
                        concepttime = gettime
                    if gettime > concepttime:
                        concepttime = gettime
                    conceptStrTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(concepttime))
        else:
            os.makedirs(self.conceptPath)
            conceptStrTime = ''

        sp = self.serverPath.split('\\')
        sp.append('asset')
        sp.append(self.departmentName)
        sp.append(self.nowTreePage)
        sp.append(str(changeTabItm.text(0)))
        sp.append('DownloadConcept')
        self.conceptDownloadPath = '\\'.join(sp)
        print 'concept download path is :' + self.conceptDownloadPath

        modelArray = []
        modeltime = ''
        modelStrTime = ''
        if os.path.exists(self.conceptDownloadPath):
            cFiles = os.listdir(self.conceptDownloadPath)
            if cFiles:
                for c in cFiles:
                    if '.jpg' in c:
                        modelArray.append(self.conceptDownloadPath + '\\' + c)
                        gettime = os.path.getmtime(self.conceptDownloadPath + '\\' + c)
                        if modeltime == '':
                            modeltime = gettime
                        if gettime > modeltime:
                            modeltime = gettime
                        modelStrTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(modeltime))
            else:
                modelStrTime = ''

        else:
            os.makedirs(self.conceptDownloadPath)
            modelStrTime = ''

        # load concept infomations over
        self.picView.clear()
        Picsp = self.serverPath.split('\\')
        Picsp.append('asset')
        Picsp.append('CONCEPT')
        Picsp.append(self.nowTreePage)
        Picsp.append(str(changeTabItm.text(0)))
        tp = '\\'.join(Picsp)
        print 'main pic path is :' + tp
        tf = os.listdir(tp)
        print '---file under main path---'
        print tf
        print '--------------------------'
        isFill = False
        for t in tf:
            Qstring = tp + '\\' + t
            if os.path.isfile(Qstring) and ('.jpg' in t):
                if (not '_middle.jpg' in t) and (not '_small.jpg' in t):
                    spName = t.split('.')[0]
                    qp = QtGui.QPixmap(tp + '\\' + spName + '_small.jpg')
                    tempIcon = QtGui.QIcon()
                    tempIcon.addPixmap(qp)
                    tempItem = QtGui.QListWidgetItem()
                    tempItem.setToolTip(Qstring)
                    tempItem.setIcon(tempIcon)
                    self.picView.addItem(tempItem)
                    isFill = True
        if isFill:
            self.picView.setCurrentRow(0)
        else:
            tempPic = QtGui.QPixmap(self.initPath + '\\data\\currentPic.png')
            self.plabPic.setPixmap(tempPic)
            self.plabPic.setToolTip('empty pic')
        # load charactor pictures over

        pass

    def loadConceptPictureData(self):

        changeTabItm = self.nowSelMainTreeItem
        # load concept pictures
        # tab,page3,in a Qlistwidget to add some

        linearGradient = QtGui.QLinearGradient(60, 50, 200, 200)
        linearGradient.setColorAt(0, Qt.transparent)
        linearGradient.setColorAt(0.89, Qt.transparent)
        linearGradient.setColorAt(0.9, QtGui.QColor(200, 200, 200))
        linearGradient.setColorAt(0.94, QtGui.QColor(200, 200, 200))
        linearGradient.setColorAt(0.95, QtGui.QColor(0, 200, 0))
        linearGradient.setColorAt(1.0, QtGui.QColor(0, 200, 0))
        # define a gradient background color for accept items.


        self.listLE.clear()
        emptyItm = QtGui.QListWidgetItem()
        emptyItm.setText('empty')
        self.listLE.addItem(emptyItm)
        # default state

        self.conceptPath = self.serverPath + '\\asset\\CONCEPT\\' + self.nowTreePage + '\\' + changeTabItm.text(
            0) + '\\uploadTemp'
        isConceptExt = os.path.exists(self.conceptPath)
        msgPath = self.conceptPath + '\\message.json'
        isMsgExt = os.path.exists(msgPath)
        print 'pic path is : ' + self.conceptPath
        print 'msg path is : ' + msgPath

        if isConceptExt and isMsgExt:
            jsonData = self.loadJson(msgPath)
            acceptData = {}
            acceptPath = self.conceptPath + '\\acceptList.json'
            print 'acc path is : ' + acceptPath
            if os.path.exists(acceptPath):
                acceptData = self.loadJson(acceptPath)
            temps = os.listdir(self.conceptPath)
            if temps:
                self.listLE.clear()
                # clear default items.
                for i in temps:
                    if '.jpg' in i:
                        if (not '_middle.jpg' in i) and (not '_small.jpg' in i):
                            spName = i.split('.')[0]
                            iconPath = self.conceptPath + '\\' + spName + '_small.jpg'
                            itmData = jsonData[i][-1]
                            itmStringTmp = ''
                            for key in itmData.keys():
                                itmStringTmp += str(key) + ':' + str(itmData[key]) + '\n'
                            codec = QtCore.QTextCodec.codecForName("utf-8")
                            itmString = codec.toUnicode(itmStringTmp)

                            icn = QtGui.QIcon(iconPath)
                            itm = QtGui.QListWidgetItem()
                            itm.setText(i + '\nArtist : ' + str(itmData['artist']))
                            itm.setSizeHint(QtCore.QSize(225, 48))
                            itm.setIcon(icn)
                            itm.setToolTip(itmString)
                            if i in acceptData.keys():
                                state = acceptData[i]
                                if state:
                                    itm.setBackground(QtGui.QBrush(linearGradient))
                            self.listLE.addItem(itm)


    # -------------------- ui functions -------------



    # ------------widget enter--------------
    def Op_Ui(self):
        self.show()
        self.resize(600, 800)
        self.move(400, 100)

    def createGeneralPage(self):
        msgWid = QtGui.QWidget()
        msgWid.setAttribute(Qt.WA_StyledBackground)
        msgWid.setAttribute(Qt.WA_DeleteOnClose)
        msgVB = QtGui.QVBoxLayout()

        titleHB = QtGui.QHBoxLayout()

        preBtn = QtGui.QToolButton()
        preBtn.setText('<--')
        preBtn.setToolTip('pre item')
        preBtn.setIcon(QtGui.QIcon(path + '\\icon\\prePage_red.png'))
        preBtn.setIconSize(QtCore.QSize(16, 16))
        preBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        preBtn.setAutoRaise(True)

        self.titleLabel = QtGui.QLabel('charactorName')
        self.titleLabel.setStyleSheet(Mstyle.QLabel(fontSize='20px'))

        nextBtn = QtGui.QToolButton()
        nextBtn.setText('-->')
        nextBtn.setToolTip('next item')
        nextBtn.setIcon(QtGui.QIcon(path + '\\icon\\nextPage_red.png'))
        nextBtn.setIconSize(QtCore.QSize(16, 16))
        nextBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        nextBtn.setAutoRaise(True)

        titleHB.addWidget(preBtn)
        titleHB.addStretch(1)
        titleHB.addWidget(self.titleLabel)
        titleHB.addStretch(1)
        titleHB.addWidget(nextBtn)
        msgVB.addLayout(titleHB)

        picHbox = QtGui.QHBoxLayout()
        self.plabPic = BC.clickLabel('', self)
        self.plabPic.setMinimumWidth(350)
        picHbox.addStretch(1)
        picHbox.addWidget(self.plabPic)
        picHbox.addStretch(1)
        msgVB.addLayout(picHbox)

        picviewHB = QtGui.QHBoxLayout()
        prePicBtn = QtGui.QToolButton()
        prePicBtn.setText('<--')
        prePicBtn.setToolTip('pre pic')
        prePicBtn.setIcon(QtGui.QIcon(path + '\\icon\\prePage_red.png'))
        prePicBtn.setIconSize(QtCore.QSize(32, 32))
        prePicBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        prePicBtn.setAutoRaise(True)

        nextPicBtn = QtGui.QToolButton()
        nextPicBtn.setText('-->')
        nextPicBtn.setToolTip('next pic')
        nextPicBtn.setIcon(QtGui.QIcon(path + '\\icon\\nextPage_red.png'))
        nextPicBtn.setIconSize(QtCore.QSize(32, 32))
        nextPicBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        nextPicBtn.setAutoRaise(True)

        self.picView = QtGui.QListWidget()
        self.picView.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum);
        self.picView.setViewMode(QtGui.QListView.IconMode)
        self.picView.setFixedHeight(70)
        self.picView.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.picView.setMovement(QtGui.QListView.Static)
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

        modelGrp = QtGui.QGroupBox('source')
        modelGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        modelGrp.setMaximumHeight(120)
        modGVB = QtGui.QVBoxLayout()
        modGVB.setContentsMargins(5, 5, 5, 5)
        modGVB.setSpacing(4)
        modGHB1 = QtGui.QHBoxLayout()
        modGHB2 = QtGui.QHBoxLayout()
        modGHB3 = QtGui.QHBoxLayout()
        modGHB4 = QtGui.QHBoxLayout()

        labServerDate = QtGui.QLabel('Serve Date : ', msgWid)
        labServerDate.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB1.addWidget(labServerDate)
        modGHB1.addStretch(1)
        labServerText = QtGui.QLabel('', msgWid)
        labServerText.setToolTip('print servDate')
        labServerText.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB1.addWidget(labServerText)
        modGHB1.addStretch(1)

        labLocalDate = QtGui.QLabel('Local Date  : ', msgWid)
        labLocalDate.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB2.addWidget(labLocalDate)
        modGHB2.addStretch(1)
        labLocalText = QtGui.QLabel('', msgWid)
        labLocalText.setToolTip('print localDate')
        labLocalText.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        modGHB2.addWidget(labLocalText)
        modGHB2.addStretch(1)

        modGHB22 = QtGui.QHBoxLayout()
        downloadConceptBtn = QtGui.QPushButton('download new')
        downloadConceptBtn.setStyleSheet(Mstyle.QPushButton(bordRad='8px'))
        downloadConceptBtn.setToolTip('dowloadConcept')
        viewConceptBtn = QtGui.QPushButton('view')
        viewConceptBtn.setStyleSheet(Mstyle.QPushButton(bordRad='8px', kw='b'))
        viewConceptBtn.setToolTip('viewConcept')
        modGHB22.addWidget(downloadConceptBtn)
        modGHB22.addWidget(viewConceptBtn)

        modGVB.addLayout(modGHB3)
        modGVB.addLayout(modGHB4)
        modGVB.addLayout(modGHB1)
        modGVB.addLayout(modGHB2)
        modGVB.addLayout(modGHB22)
        modelGrp.setLayout(modGVB)
        msgVB.addWidget(modelGrp)

        self.infoGrp = QtGui.QGroupBox('infomation')
        self.infoGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        self.infoGrp.setMaximumHeight(150)
        infoGVB = QtGui.QVBoxLayout()

        lastmsgHB = QtGui.QHBoxLayout()
        labLastMsgTitle = QtGui.QLabel('LastMsg : ', msgWid)
        labLastMsgTitle.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        labLastMsg = QtGui.QLabel('', msgWid)

        labLastMsg.setToolTip('lastmsg')
        labLastMsg.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b', lang='c'))
        lastmsgHB.addWidget(labLastMsgTitle)
        lastmsgHB.addWidget(labLastMsg)
        lastmsgHB.addStretch(1)

        infoGHB1 = QtGui.QHBoxLayout()
        lab4 = QtGui.QLabel('Artist : ', msgWid)
        lab4.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        lab4data = QtGui.QLabel('', msgWid)
        lab4data.setToolTip('artist')
        lab4data.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        infoGHB1.addWidget(lab4)
        infoGHB1.addWidget(lab4data)
        infoGHB1.addStretch(1)

        infoGHB2 = QtGui.QHBoxLayout()
        lab5 = QtGui.QLabel('Passing : ', msgWid)
        lab5.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        lab5data = QtGui.QLabel('none days', msgWid)
        lab5data.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        lab5data.setToolTip('passing')
        infoGHB2.addWidget(lab5)
        infoGHB2.addWidget(lab5data)
        infoGHB2.addStretch(1)

        infoGHB3 = QtGui.QHBoxLayout()
        lab6 = QtGui.QLabel('StartDate :     ', msgWid)
        lab6.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        lab6data = QtGui.QLabel('', msgWid)
        lab6data.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        lab6data.setToolTip('startdate')
        infoGHB3.addWidget(lab6)
        infoGHB3.addWidget(lab6data)
        infoGHB3.addStretch(1)

        infoGHB6 = QtGui.QHBoxLayout()
        lab11 = QtGui.QLabel('UpdateData : ', msgWid)
        lab11.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        lab11data = QtGui.QLabel('', msgWid)
        lab11data.setToolTip('updatedate')
        lab11data.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        infoGHB6.addWidget(lab11)
        infoGHB6.addWidget(lab11data)
        infoGHB6.addStretch(1)

        infoGHB4 = QtGui.QHBoxLayout()
        lab7 = QtGui.QLabel('ConfirmData : ', msgWid)
        lab7.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        lab7data = QtGui.QLabel('', msgWid)
        lab7data.setToolTip('confirmdate')
        lab7data.setStyleSheet(Mstyle.QLabel(fontSize='13px', kw='b'))
        infoGHB4.addWidget(lab7)
        infoGHB4.addWidget(lab7data)
        infoGHB4.addStretch(1)

        infoGHB5 = QtGui.QHBoxLayout()
        lab8 = QtGui.QLabel('Machine : ', msgWid)
        lab8.setStyleSheet(Mstyle.QLabel(fontSize='10px', kw='b'))
        lab8data = QtGui.QLabel('', msgWid)
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

        oprGrp = QtGui.QGroupBox('opreate')
        oprGrp.setStyleSheet(Mstyle.QGroupBox(kw='b'))
        oprGrp.setMaximumHeight(150)
        oprGVB = QtGui.QVBoxLayout()

        oprGHB1 = QtGui.QHBoxLayout()
        oprbtn_uploadLow = QtGui.QPushButton('upload', msgWid)
        oprbtn_uploadLow.setFixedHeight(25)
        oprbtn_uploadLow.setStyleSheet(Mstyle.QPushButton(bordRad='12px'))
        oprbtn_uploadLow.setToolTip('open upload window')
        oprGHB1.addWidget(oprbtn_uploadLow)

        oprGVB.addLayout(oprGHB1)
        oprGrp.setLayout(oprGVB)
        msgVB.addWidget(oprGrp)
        msgVB.addStretch(1)

        msgWid.setLayout(msgVB)
        preBtn.clicked.connect(self.aboveItemFn)
        nextBtn.clicked.connect(self.belowItemFn)

        prePicBtn.clicked.connect(self.prePicFn)
        nextPicBtn.clicked.connect(self.nextPicFn)

        downloadConceptBtn.clicked.connect(self.copyConceptToModelFn)
        viewConceptBtn.clicked.connect(self.refrenceModelFn)
        oprbtn_uploadLow.clicked.connect(self.oprbtn_openUploadFn)

        self.picView.currentItemChanged.connect(self.changePicFn)
        return msgWid


if __name__ == "__main__":
    import sys
    import multiprocessing

    multiprocessing.freeze_support()
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet('QWidget {background-color:rgb(68,68,68);color:rgb(206,206,206)}')
    loadPic = QtGui.QPixmap(path + '\\icon\\loading.png')
    loadingPic = QtGui.QSplashScreen(loadPic, Qt.WindowStaysOnTopHint)

    loadingPic.show()
    app.processEvents()
    loadingPic.showMessage('loading images...', Qt.AlignLeft | Qt.AlignBottom, Qt.white)

    ui = ConceptManagerBoxUI()
    ui.Op_Ui()
    loadingPic.finish(ui)
    sys.exit(app.exec_())
