# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\main_browser.ui'
#
# Created: Mon Mar  4 22:55:20 2019
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
toolPath = r'C:\gitLab\brownser01'
if toolPath not in sys.path:
    sys.path.append(toolPath)

binPath = r'C:\gitLab\brownser01\bin'
if binPath not in sys.path:
    sys.path.append(binPath)

from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2
#import Qt
#print dir(Qt)
if IsPySide:

    from PySide import QtWebKit
elif IsPySide2:
    from PySide2 import QtWebKit

else:
    from PyQt4 import QtWebKit

import sys
import os
import logging
import bin.relatives.dataItem as dataItem
reload(dataItem)
import bin.relatives.spoilerItem as spoilerItem
reload(spoilerItem)
import bin.relatives.flowLayout as flowLayout
reload(flowLayout)
import bin.relatives.gridWidget as gridWidget
reload(gridWidget)
import src.resources

if IsPySide:
    from shiboken import wrapInstance
elif IsPySide2:
    from shiboken2 import wrapInstance

try:
    import maya.OpenMayaUI as omui
    import maya.OpenMaya as om
    import pymel.core as pm
    import pymel.core.datatypes as dt
    import maya.cmds as cmds
    import maya.mel as mel
    # from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
    from Qt.QtCore import QRect

    def getMayaWindow():
        ptr = omui.MQtUtil.mainWindow()
        return wrapInstance(long(ptr), qw.QWidget)

    MayaParent = getMayaWindow()
except:
    MayaParent = ''
'''

import sys

addPathArray = [r'D:\gitLab\ssToolShelf',r'C:\gitLab\ssToolShelf',r'C:\Python27\Lib\site-packages']
for pt in addPathArray:
    if not pt in sys.path:
        #sys.path.append(pt)
        pass


import sys, os, time, json, shutil, random, math

from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2


import bin.Mstyle_RB as Mstyle_RB

Mstyle = Mstyle_RB.RedBlackStyleSheet()
'''


try:
    _encoding = qw.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return qw.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return qw.QApplication.translate(context, text, disambig)

class Ui_MainWindow(qw.QMainWindow):
    guildCheckList = []
    guildEnableList = []
    guildScale = 1 
    guildModule = ''
    guildSubListDefaultSelect = ''
    guildAddList = None

    _serverPath = ''
    _localCachePath = ''
    _prjName = ''
    _module = ''
    _moduleArray = ['_assets','_shots']
    scale = 1
    dataMatchDirList = [] # 储存data区域的扫描目录，以及过滤信息的列表

    def setBrowserModule(self,inputVal):
        if isinstance(inputVal,int):
            self._module = self._moduleArray[inputVal]
            #logging.info( 'self._module',self._module)
        elif isinstance(inputVal,str):
            if inputVal in self._moduleArray:

                self._module = inputVal
            else:
                raise AttributeError ('inputVal invalid. must be in ' + str(self._moduleArray))
    
    def getBrowserModule(self):
        return self._module

    def setProjectName(self,inputStr):
        self._prjName = str(inputStr)
        logging.info('update sub actions')
        logging.info('update search path')
        logging.info('restart ui')
        #print 'update sub actions'
        #print 'update search path'
        #print 'restart ui'

    def getProjectName(self):
        return self._prjName

    def setServerPath(self,inputStr):
        if os.path.exists(inputStr):
            self._serverPath = inputStr
        else:
            raise AttributeError (inputStr + 'inputStr is not an exists path')

    def getServerPath(self):
        return self._serverPath

    def setLocalCachePath(self,inputStr):
        if os.path.exits(inputStr):
            self._localCachePath = inputStr
        else:
            raise AttributeError ('inputStr is not a valid path')

    def getScale(self):
        return self.scale

    def setScale(self,val):
        self.scale = int(val)
        # reload ui form

    def setupUi(self):
        uiWidth = 1280 * self.scale
        uiHeight = 728 * self.scale
        unitSize = 32 * self.scale
        iconSize = unitSize - (6 * self.scale)
        fontHeight = 20 * self.scale

        self.setObjectName('MainUI')
        self.setMinimumSize(QtCore.QSize(uiWidth*0.5, uiHeight*0.5))
        self.resize(uiWidth, uiHeight)
        self.setWindowOpacity(1)
        '''
        self.setStyleSheet(("QPushButton {color:rgb(170, 85, 255);font: 75 9pt \"Arial\";}\n"
                    "QPushButton#closeBtn { background-color: red }\n"
                    "QsearchLine{ background-color: red }\n"
                    "QsearchLine[readOnly=\"true\"]{ background-color: gray }"))
        '''

        self.centralwidget = qw.QWidget(self)
        self.centralwidget.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName(("centralwidget"))

        self.verticalLayout = qw.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(("mainVLayout"))

        self.horizontalLayout_4 = qw.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(("titleHLayout"))

        self.logoLab = qw.QLabel(self.centralwidget)
        self.logoLab.setMaximumSize(QtCore.QSize(16777215, fontHeight))
        logoPixmap = QtGui.QPixmap.fromImage(QtGui.QImage(':/icon/alipay.png'))
        logoPixmap = logoPixmap.scaled(fontHeight,fontHeight,aspectRatioMode=QtCore.Qt.KeepAspectRatio)
        self.logoLab.setPixmap(logoPixmap)
        self.logoLab.setObjectName(("logoLab"))

        self.horizontalLayout_4.addWidget(self.logoLab)

        self.mainWindowName = qw.QLabel(self.centralwidget)



        self.horizontalLayout_4.addWidget(self.mainWindowName)
        spacerItem = qw.QSpacerItem(0, 0, qw.QSizePolicy.Expanding, qw.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.progressBar = qw.QProgressBar(self.centralwidget)
        self.progressBar.setMinimumSize(QtCore.QSize(fontHeight*2, 0))
        self.progressBar.setMaximumSize(QtCore.QSize(fontHeight*5, 16777215))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(True)
        self.progressBar.setTextDirection(qw.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(("progressBar"))
        self.horizontalLayout_4.addWidget(self.progressBar)

        self.maxResumeUI = qw.QPushButton(self.centralwidget)
        self.maxResumeUI.setMaximumSize(QtCore.QSize(fontHeight, fontHeight))
        self.maxResumeUI.setObjectName(("maxResumeUI"))
        self.maxResumeUI.setIcon(QtGui.QIcon(':/icon/maxium.png'))
        #self.maxResumeUI.setIconSize(QtCore.QSize(fontHeight, fontHeight))
        self.horizontalLayout_4.addWidget(self.maxResumeUI)

        self.closeBtn = qw.QPushButton(self.centralwidget)
        self.closeBtn.setMaximumSize(QtCore.QSize(fontHeight, fontHeight))
        self.closeBtn.setIcon(QtGui.QIcon(':/icon/closeWidget.png'))
        #self.closeBtn.setIconSize(QtCore.QSize(fontHeight, fontHeight))
        self.closeBtn.setObjectName(("closeBtn"))
        self.horizontalLayout_4.addWidget(self.closeBtn)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        # ================ titile part over =======================

        self.horizontalLayout_2 = qw.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setSizeConstraint(qw.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName(("horizontalLayout_2"))
        self.guildButton = qw.QPushButton(self.centralwidget)
        self.guildButton.setMinimumSize(QtCore.QSize(unitSize, unitSize))
        self.guildButton.setMaximumSize(QtCore.QSize(unitSize, unitSize))
        self.guildButton.setFlat(False)
        self.guildButton.setObjectName(("guildButton"))
        self.guildButton.setIcon(QtGui.QIcon(':/icon/grouplist.png'))
        self.guildButton.setIconSize(QtCore.QSize(iconSize, iconSize))
        self.guildButton.setStatusTip(_translate("MainWindow", "开启导航栏", None))


        self.horizontalLayout_2.addWidget(self.guildButton)
        self.backButton = qw.QPushButton(self.centralwidget)
        self.backButton.setMinimumSize(QtCore.QSize(unitSize,unitSize))
        self.backButton.setMaximumSize(QtCore.QSize(unitSize,unitSize))
        self.backButton.setObjectName(("backButton"))
        self.backButton.setIcon(QtGui.QIcon(':/icon/back.png'))
        self.backButton.setIconSize(QtCore.QSize(iconSize, iconSize))
        self.backButton.setStatusTip(_translate("MainWindow", "后退到上一次浏览的地址", None))


        self.horizontalLayout_2.addWidget(self.backButton)
        self.upButton = qw.QPushButton(self.centralwidget)
        self.upButton.setMinimumSize(QtCore.QSize(unitSize,unitSize))
        self.upButton.setMaximumSize(QtCore.QSize(unitSize,unitSize))
        self.upButton.setIcon(QtGui.QIcon(':/icon/refresh.png'))
        self.upButton.setIconSize(QtCore.QSize(iconSize, iconSize))
        self.upButton.setObjectName(("refreshButton"))
        self.upButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.upButton)
        self.projectButton = qw.QPushButton(self.centralwidget)
        self.projectButton.setMinimumSize(QtCore.QSize(unitSize,unitSize))
        self.projectButton.setMaximumSize(QtCore.QSize(0, unitSize))
        self.projectButton.setObjectName(("projectButton"))
        self.projectButton.setStatusTip(_translate("MainWindow", "切换项目", None))

        self.projectButton.setIcon(QtGui.QIcon(':/icon/switch.png'))
        self.projectButton.setIconSize(QtCore.QSize(iconSize, iconSize))
        self.horizontalLayout_2.addWidget(self.projectButton)

        self.comboBox = qw.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, unitSize))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, unitSize))
        self.comboBox.setEditable(True)
        self.comboBox.setSizeAdjustPolicy(qw.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox.setObjectName(("addressBar"))
        self.comboBox.setStatusTip(_translate("MainWindow", "显示曾经浏览过的地址栏", None))
        self.comboBox.lineEdit().setReadOnly(True)
        self.horizontalLayout_2.addWidget(self.comboBox)

        self.moduleButton = qw.QPushButton(self.centralwidget)
        self.moduleButton.setMinimumSize(QtCore.QSize(unitSize,unitSize))
        self.moduleButton.setMaximumSize(QtCore.QSize(unitSize,unitSize))
        self.moduleButton.setObjectName(("moduleButton"))
        self.moduleButton.setStatusTip(_translate("MainWindow", "列表模式/图标模式/大图标模式", None))
        self.moduleButton.setIcon(QtGui.QIcon(':/icon/iconManager.png'))
        self.moduleButton.setIconSize(QtCore.QSize(iconSize, iconSize))
        self.horizontalLayout_2.addWidget(self.moduleButton)

        self.attributeButton = qw.QPushButton(self.centralwidget)
        self.attributeButton.setMinimumSize(QtCore.QSize(unitSize,unitSize))
        self.attributeButton.setMaximumSize(QtCore.QSize(unitSize,unitSize))
        self.attributeButton.setObjectName(("attributeButton"))
        self.attributeButton.setIcon(QtGui.QIcon(':/icon/pin.png'))
        self.attributeButton.setIconSize(QtCore.QSize(iconSize, iconSize))
        self.horizontalLayout_2.addWidget(self.attributeButton)

        self.batchButton = qw.QPushButton(self.centralwidget)
        self.batchButton.setMinimumSize(QtCore.QSize(unitSize,unitSize))
        self.batchButton.setMaximumSize(QtCore.QSize(unitSize,unitSize))
        self.batchButton.setObjectName(("batchButton"))
        self.batchButton.setIcon(QtGui.QIcon(':/icon/batch.png'))
        self.batchButton.setIconSize(QtCore.QSize(iconSize, iconSize))
        self.horizontalLayout_2.addWidget(self.batchButton)

        self.pushButton_3 = qw.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(unitSize,unitSize))
        self.pushButton_3.setMaximumSize(QtCore.QSize(unitSize,unitSize))
        self.pushButton_3.setObjectName(("pushButton_3"))
        self.pushButton_3.setIcon(QtGui.QIcon(':/icon/more.png'))
        self.pushButton_3.setIconSize(QtCore.QSize(iconSize, iconSize))
        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.setupButton = qw.QPushButton(self.centralwidget)
        self.setupButton.setMinimumSize(QtCore.QSize(unitSize,unitSize))
        self.setupButton.setMaximumSize(QtCore.QSize(unitSize,unitSize))
        self.setupButton.setObjectName(("setupButton"))
        self.setupButton.setIcon(QtGui.QIcon(':/icon/setting.png'))
        self.setupButton.setIconSize(QtCore.QSize(iconSize, iconSize))
        self.horizontalLayout_2.addWidget(self.setupButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        #====================== tool bar over ==========================

        self.horizontalLayout = qw.QHBoxLayout()
        self.horizontalLayout.setObjectName(("horizontalLayout"))
        self.widget = qw.QWidget(self.centralwidget)
        self.widget.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.widget.setObjectName(("widget"))
        self.horizontalLayout_3 = qw.QHBoxLayout(self.widget)

        self.horizontalLayout_3.setObjectName(("horizontalLayout_3"))
        self.splitter = qw.QSplitter(self.widget)
        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.Maximum, qw.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        #self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(qw.QFrame.NoFrame)
        self.splitter.setLineWidth(0)
        self.splitter.setMidLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName(("splitter"))



        self.dataListWidget = qw.QWidget(self.splitter)
        self.dataListWidget.setAttribute(QtCore.Qt.WA_StyledBackground)
        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.Minimum, qw.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.dataScrollArea.sizePolicy().hasHeightForWidth())
        self.dataListWidget.setSizePolicy(sizePolicy)
        self.dataListWidget.setObjectName(("dataListWidget"))

        
        self.dataListMainVLayout = qw.QVBoxLayout(self.dataListWidget)
        
        self.dataListMainVLayout.setObjectName("dataListMainVLayout")
        self.dataListWidget.setLayout(self.dataListMainVLayout)
        



        #self.dataListLayout = flowLayout.FlowLayout()
        #self.dataListLayout.setObjectName("dataListLayout")
        #self.dataListWidget.setLayout(self.dataListLayout)

        self.dataListSearchBarHLayout = qw.QHBoxLayout()
        self.dataListSearchBarHLayout.setObjectName(("dataListSearchBarHLayout"))
        self.searchLine = qw.QLineEdit(self.dataListWidget)
        self.searchLine.setMinimumSize(QtCore.QSize(0, 0))
        #self.searchLine.setReadOnly(True)
        self.searchLine.setObjectName(("searchLine"))
        self.dataListSearchBarHLayout.addWidget(self.searchLine)
        self.configSearchButton = qw.QPushButton(self.dataListWidget)
        self.configSearchButton.setObjectName(("configSearchButton"))
        self.dataListSearchBarHLayout.addWidget(self.configSearchButton)
        self.ruleSearchButton = qw.QPushButton(self.dataListWidget)
        self.ruleSearchButton.setObjectName(("ruleSearchButton"))
        self.dataListSearchBarHLayout.addWidget(self.ruleSearchButton)
        self.dataListMainVLayout.addLayout(self.dataListSearchBarHLayout)



        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)

        self.dataScrollArea = qw.QScrollArea(self.splitter)
        #self.dataScrollArea.setSizePolicy(sizePolicy)
        #self.dataScrollArea.setMinimumSize(QtCore.QSize(0, 0))
        #self.dataScrollArea.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.dataScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.dataScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.dataScrollArea.setWidgetResizable(True)
        self.dataScrollArea.setObjectName(("dataScrollArea"))

        self.dataListMainVLayout.addWidget(self.dataScrollArea)

        flowWidget = qw.QWidget()
        flowWidget.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.dataScrollArea.setWidget(flowWidget)

        self.flowLayout = flowLayout.FlowLayout()
        self.flowLayout.setObjectName(("flowLayout"))
        flowWidget.setLayout(self.flowLayout)


        #self.dataScrollArea.setLayout(self.flowLayout)
        #spacerItem1 = qw.QSpacerItem(160, 40, qw.QSizePolicy.Minimum, qw.QSizePolicy.MinimumExpanding)
        #self.dataListMainVLayout.addItem(spacerItem1)

        self.attributeWidget = qw.QWidget(self.splitter)
        self.attributeWidget.setAttribute(QtCore.Qt.WA_StyledBackground)

        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.MinimumExpanding, qw.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        #sizePolicy.setHeightForWidth(self.attributeWidget.sizePolicy().hasHeightForWidth())
        self.attributeWidget.setSizePolicy(sizePolicy)
        self.attributeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.attributeWidget.setMinimumSize(QtCore.QSize(uiWidth*0.3, 16777215))
        self.attributeWidget.setObjectName(("attributeWidget"))

        self.verticalLayout_2 = qw.QVBoxLayout(self.attributeWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(("verticalLayout_2"))


        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.Minimum, qw.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.scrollArea = qw.QScrollArea(self.attributeWidget)
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(("scrollArea"))
        self.scrollAreaWidgetContents = qw.QWidget()
        self.scrollAreaWidgetContents.setAttribute(QtCore.Qt.WA_StyledBackground)
        #self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 548, 337))

        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.Minimum, qw.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())

        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName(("scrollAreaWidgetContents"))
        self.verticalLayout_3 = qw.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(("verticalLayout_3"))

        
        titleBox = qw.QHBoxLayout(self)

        self.titleLab_dep = qw.QLabel(self.centralwidget)
        self.titleLab_dep.setObjectName(("titleLab_dep"))
        self.titleLab_dep.setText('titleLab_dep')
        self.titleLab_dep.setFixedSize(75*self.scale,25*self.scale)
        self.titleLab_dep.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        titleBox.addWidget(self.titleLab_dep)

        self.titleLab_name = qw.QLabel(self.centralwidget)
        self.titleLab_name.setObjectName(("titleLab_name"))
        self.titleLab_name.setText('titleLab_name')
        self.titleLab_name.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        titleBox.addWidget(self.titleLab_name)

        self.titleLab_var = qw.QLabel(self.centralwidget)
        self.titleLab_var.setObjectName(("titleLab_var"))
        self.titleLab_var.setText('(titleLab_var)')
        self.titleLab_var.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        titleBox.addWidget(self.titleLab_var)


        self.titleLab_type = qw.QLabel(self.centralwidget)
        self.titleLab_type.setObjectName(("titleLab_type"))
        self.titleLab_type.setText('titleLab_type')
        self.titleLab_type.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        titleBox.addWidget(self.titleLab_type)

        self.verticalLayout_3.addLayout(titleBox)
        
        '''
        self.label = qw.QLabel(self.scrollAreaWidgetContents)

        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.MinimumExpanding, qw.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())

        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(("attributeName"))
        #self.label.setText('attributeName_999')
        self.verticalLayout_3.addWidget(self.label)'''

        self.webColPage = spoilerItem.FrameDialog()
        self.webColPage.setupLayout(title="Unit History")
        # 这就是折叠页，自己写的

        self.webColPage.addWidget(qw.QPushButton('a'))
        
        self.verticalLayout_3.addWidget(self.webColPage)

        self.fileColPage = spoilerItem.FrameDialog()
        self.fileColPage.setupLayout(title="File Struct")
        self.fileColPage.addWidget(qw.QLabel('fileStruct sheet'))
        self.verticalLayout_3.addWidget(self.fileColPage)

        self.actionColPage = spoilerItem.FrameDialog()
        self.actionColPage.setupLayout(title="actions",switch=True)

        self.verticalLayout_3.addWidget(self.actionColPage)


        self.eventColPage = spoilerItem.FrameDialog()
        self.eventColPage.setupLayout(title="events")
        self.eventColPage.addWidget(qw.QLabel('eventsA'))
        self.eventColPage.addWidget(qw.QLabel('eventsB'))
        self.verticalLayout_3.addWidget(self.eventColPage)
        self.verticalLayout_3.addStretch()

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_3.addWidget(self.splitter)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = qw.QStatusBar(self)
        self.statusbar.setObjectName(("statusbar"))
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)

        QtCore.QMetaObject.connectSlotsByName(self)
        self.guildButton.clicked.connect(self.openGuildWidget)
        self.comboBox.currentIndexChanged.connect(self.fillDataDialog)

        if not(IsPySide2 or IsPySide):
            # pyside不支持setMargin
            self.horizontalLayout_3.setMargin(0)
            self.verticalLayout_2.setMargin(0)
            self.dataListMainVLayout.setMargin(0)



    def clearDataDialog(self):

        itmCount = self.flowLayout.count()

        if itmCount:
            for i in reversed(range(itmCount)):
                widgetToRemove = self.flowLayout.itemAt(i).widget()
                self.flowLayout.removeWidget(widgetToRemove)
                widgetToRemove.setParent(None)

    def fillDataDialog(self):
        # 这个将来要移动到子线程里面去，目前先放着不动
        if self.dataMatchDirList:
            self.clearDataDialog()
            logging.info('change fill data dialog')

            searchPath = self.comboBox.lineEdit().text()
            #logging.info( 'searchPath',searchPath)
            dataType = searchPath.split('/')[-1]
            if os.path.exists(searchPath):
                loopArray = os.listdir(searchPath)

                for i in loopArray: # 扫的是相当于asset的角色名的那层目录
                    for t in self.dataMatchDirList: # 扫的是角色名下面的那个部门环节的目录
                        matchPath = t % {'name':i}
                        depName = t.split('/')[-1]
                        #print 'depName',depName
                        if os.path.exists(matchPath):
                            varArray = os.listdir(matchPath)
                            for va in varArray: # 扫的是变体的那一层目录
                                varPath = '%s/%s/Main' % (matchPath,va)
                                #print 'varPath',varPath
                                _frame = dataItem.dataButton(depName,va,i,varPath,dataType,sizeLevel=self.scale)
                                _frame.clicked.connect(self.dbClickedEvent_default)
                                _frame.played.connect(self.dbPlayedEvent_default)
                                _frame.addChart.connect(self.dbAddChartEvent_default)
                                _frame.setStatusTip('%s : %s - <%s> - %s' % (dataType,depName,va,i))
                                self.flowLayout.addWidget(_frame)

    def dbClickedEvent_default(self,dic):
        self.titleLab_type.setText(dic['dataType'])
        self.titleLab_var.setText(dic['varient'])
        self.titleLab_name.setText(dic['name'])
        self.titleLab_dep.setText(dic['dep'])
        self.titleLab_dep.setProperty("dep", dic['dep'].lower())
        print 'property',dic['dep'].lower()
        self.titleLab_dep.style().unpolish(self.titleLab_dep)
        self.titleLab_dep.style().polish(self.titleLab_dep)

        self.dbClickedEvent(dic)

    def dbPlayedEvent_default(self,dic):
        self.dbPlayedEvent(dic)  

    def dbAddChartEvent_default(self,dic):
        self.dbAddChartEvent(dic)  

    def dbClickedEvent(self,dic):
        pass  
    def dbPlayedEvent(self,dic):
        pass  
    def dbAddChartEvent(self,dic):
        pass  

    def updateAddressBar(self,inputArray):
        # D:\testDir\pipPrj\ZZZ\assets\Charactors\rabbit\Model\defaultVersion
        deplist = []
        self.dataMatchDirList = []
        substr = ''
        for i in inputArray:
            theStr = '%(serv)s/pipPrj/%(prj)s/%(module)s/%(sub)s/%(name)s/%(dep)s'  % {'prj':self._prjName,'serv':self._serverPath,'module':self._module,'dep':i[0],'sub':i[1],'name':'%(name)s'}
            self.dataMatchDirList.append(theStr)
            substr = i[1]
            deplist.append(i[0])
            #print theStr

        #depStr = '&&'.join(deplist)

        #fullStr = '%(serv)s/pipPrj/%(prj)s/%(module)s/%(sub)s/%(name)s/%(dep)s'  % {'prj':self._prjName,'serv':self._serverPath,'module':module,'dep':depStr,'sub':substr,'name':'%(name)s'}
        
        displayStr = '%(serv)s/pipPrj/%(prj)s/%(module)s/%(sub)s'  % {'prj':self._prjName,'serv':self._serverPath,'module':self._module,'sub':substr}
        
        #print 'display',fullStr

        checkFound = self.comboBox.findText(displayStr)
        #print 'checkFound',checkFound
        if checkFound > -1:
            self.comboBox.removeItem(checkFound)

        self.comboBox.addItem(displayStr)
        maxCom = self.comboBox.count() -1
        #print maxCom
        self.comboBox.setCurrentIndex (maxCom)

    def setGuildEnableList(self,theList):
        if isinstance(theList,list):
            self.guildEnableList = theList

    def setGuildCheckList(self,theList):
        if isinstance(theList,list):
            self.guildCheckList = theList

    def setGuildModule(self,theStr):
        self.guildModule = theStr


    def setGuildSubListDefaultSelect(self,theIncomming):
        self.guildSubListDefaultSelect = theIncomming

    def setGuildScale(self,theInt):
        self.guildScale = theInt

    def setGuildAddList(self,theData):
        self.guildAddList = theData

    #def setAddList

    def openGuildWidget(self):
        gg = gridWidget.gridWidget(self)
        gg.setParent(self)
        #print 'parent style',self.styleSheet()
        for i in self.guildEnableList:
            #logging.info( 'enable',i)
            gg.setEnableList(i)
        #gg.setEnableList('Rig')
        gg.applyEnableList()
        for i in self.guildCheckList:
            #logging.info( 'check',i)
            gg.setCheckList(i)

        
        #gg.setModule('asset')
        gg.setModule(_type = self._module)
        gg.addToList(self.guildAddList)
        #gg.addToList(['seq001'])
        gg.setSubListDefaultSelect(self.guildSubListDefaultSelect)
        gg.setScaleSize(self.scale)
        gg.clicked.connect(self.updateAddressBar)
        gg.emitTheSignal()
        #gg.setLeftVisable(False)
        #gg.setLeftVisable(True)
        gg.Op_Ui()
        #print self.searchLine.pos()
        #boxWidget.show()

        GlobalPoint = self.guildButton.mapToGlobal(QtCore.QPoint(-1 * self.pos().x() - (self.guildButton.width()*0.25), -1 * self.pos().y()-2*self.scale))
        gg.move(GlobalPoint)

        #gg.setStyleSheet('QWidget {background-color:#AAAAAA;}')
        gg.raise_()

    def addActionArea(self,inputFrame):
        if isinstance(inputFrame,qw.QFrame):
            self.actionColPage.addWidget(inputFrame)
        else:
            raise TypeError ('need QtGui.QFrame,incomming ' + type(inputFrame))


    def retranslateUi(self, MainWindow):
        self.mainWindowName.setText(_translate("MainWindow", "大马猴pipeline", None))
        MainWindow.setWindowTitle(_translate("MainWindow", "模型组提交工具", None))
        #self.logoLab.setText(_translate("MainWindow", "logoPic", None))
        #self.titleLab.setText(_translate("MainWindow", "TextLabel", None))
        #self.maxResumeUI.setText(_translate("MainWindow", "Max", None))
        #self.closeBtn.setText(_translate("MainWindow", "x", None))
        #self.guildButton.setText(_translate("MainWindow", "Guild", None))
        #self.backButton.setText(_translate("MainWindow", "←", None))
        #self.upButton.setText(_translate("MainWindow", "↑", None))
        #self.projectButton.setText(_translate("MainWindow", "projectName", None))
        self.moduleButton.setToolTip(_translate("MainWindow", "切换视图模式", None))
        #self.moduleButton.setText(_translate("MainWindow", "㗊", None))
        self.attributeButton.setStatusTip(_translate("MainWindow", "开启/关闭属性栏", None))
        #self.attributeButton.setText(_translate("MainWindow", "三", None))
        self.batchButton.setStatusTip(_translate("MainWindow", "批量操作列表", None))
        #self.batchButton.setText(_translate("MainWindow", "车", None))
        self.pushButton_3.setStatusTip(_translate("MainWindow", "待定设置", None))
        #self.pushButton_3.setText(_translate("MainWindow", "other", None))
        self.setupButton.setStatusTip(_translate("MainWindow", "设置", None))
        #self.setupButton.setText(_translate("MainWindow", "…", None))
        self.configSearchButton.setText(_translate("MainWindow", "search", None))
        self.ruleSearchButton.setText(_translate("MainWindow", "config", None))

        #self.label.setText(_translate("MainWindow", "TextLabel", None))


if __name__ == '__main__':
    import os
    app = qw.QApplication.instance()
    if not app:
        app = qw.QApplication( [])




    gg = Ui_MainWindow()
    #gg.setServerPath('D:/testDir')
    #gg.setProject('ZZZ')
    gg.setupUi()
    gg.setServerPath('D:/testDir')
    gg.setProjectName('ZZZ')
    #gg.fillDataDialog()

    testF = qw.QFrame()
    testV = qw.QVBoxLayout()
    testF.setLayout(testV)
    testV.addWidget(qw.QLabel('actionsA'))
    testV.addWidget(qw.QLabel('actionsV'))
    gg.addActionArea(testF)
    gg.show()
    #gg.resize(500,500)
    gg.move(0,0)

    gg.raise_()
    try:
        sys.exit(app.exec_())
    except: pass

'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
 
 
class Example(QWidget):
 
    def __init__(self):
        super().__init__()
 
        self.initUI()  # 界面绘制交给InitUi方法
 
    def initUI(self):
 
        self.desktop = QApplication.desktop()
 
        #获取显示器分辨率大小
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
 
        print(self.height)
        print(self.width)
 
        # 显示窗口
        self.show()
 
 
if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()

--------------------- 
作者：pursuit_zhangyu 
来源：CSDN 
原文：https://blog.csdn.net/pursuit_zhangyu/article/details/83508025 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''