# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\main_browser.ui'
#
# Created: Mon Mar  4 22:55:20 2019
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2
#import Qt
#print dir(Qt)
from PyQt4 import QtWebKit

import sys
import os
import dataItem
import spoilerItem

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
    scale = 2
    def getScale(self):
        return self.scale

    def setScale(self,val):
        self.scale = int(val)
        # reload ui form

    def setupUi(self):
        uiWidth = 1280 * self.scale
        uiHeight = 728 * self.scale
        unitSize = 32 * self.scale
        fontHeight = 20 * self.scale

        self.setObjectName(u'浏览器界面')
        self.setMinimumSize(QtCore.QSize(uiWidth*0.5, uiHeight*0.5))
        self.resize(uiWidth, uiHeight)
        self.setWindowOpacity(0.95)
        self.setStyleSheet(("QPushButton {color:rgb(170, 85, 255);font: 75 9pt \"Arial\";}\n"
"QPushButton#closeBtn { background-color: red }\n"
"QsearchLine{ background-color: red }\n"
"QsearchLine[readOnly=\"true\"]{ background-color: gray }"))


        self.centralwidget = qw.QWidget(self)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName(("centralwidget"))

        self.verticalLayout = qw.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(("mainVLayout"))

        self.horizontalLayout_4 = qw.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(("titleHLayout"))

        self.logoLab = qw.QLabel(self.centralwidget)
        self.logoLab.setMaximumSize(QtCore.QSize(16777215, fontHeight))
        self.logoLab.setObjectName(("logoLab"))

        self.horizontalLayout_4.addWidget(self.logoLab)
        self.titleLab = qw.QLabel(self.centralwidget)
        self.titleLab.setMaximumSize(QtCore.QSize(16777215, fontHeight))
        self.titleLab.setObjectName(("titleLab"))
        self.horizontalLayout_4.addWidget(self.titleLab)
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
        self.horizontalLayout_4.addWidget(self.maxResumeUI)
        self.closeBtn = qw.QPushButton(self.centralwidget)
        self.closeBtn.setMaximumSize(QtCore.QSize(fontHeight, fontHeight))
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
        self.horizontalLayout_2.addWidget(self.guildButton)
        self.backButton = qw.QPushButton(self.centralwidget)
        self.backButton.setMinimumSize(QtCore.QSize(unitSize,unitSize))
        self.backButton.setMaximumSize(QtCore.QSize(unitSize,unitSize))
        self.backButton.setObjectName(("backButton"))
        self.horizontalLayout_2.addWidget(self.backButton)
        self.upButton = qw.QPushButton(self.centralwidget)
        self.upButton.setMinimumSize(QtCore.QSize(unitSize,unitSize))
        self.upButton.setMaximumSize(QtCore.QSize(unitSize,unitSize))
        self.upButton.setObjectName(("upButton"))
        self.horizontalLayout_2.addWidget(self.upButton)
        self.projectButton = qw.QPushButton(self.centralwidget)
        self.projectButton.setMinimumSize(QtCore.QSize(unitSize,unitSize))
        self.projectButton.setMaximumSize(QtCore.QSize(0, unitSize))
        self.projectButton.setObjectName(("projectButton"))
        self.horizontalLayout_2.addWidget(self.projectButton)
        self.comboBox = qw.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, unitSize))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, unitSize))
        self.comboBox.setEditable(True)
        self.comboBox.setSizeAdjustPolicy(qw.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox.setObjectName(("comboBox"))
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.moduleButton = qw.QPushButton(self.centralwidget)
        self.moduleButton.setMinimumSize(QtCore.QSize(unitSize,unitSize))
        self.moduleButton.setMaximumSize(QtCore.QSize(unitSize,unitSize))
        self.moduleButton.setObjectName(("moduleButton"))
        self.horizontalLayout_2.addWidget(self.moduleButton)
        self.attributeButton = qw.QPushButton(self.centralwidget)
        self.attributeButton.setMinimumSize(QtCore.QSize(unitSize,unitSize))
        self.attributeButton.setMaximumSize(QtCore.QSize(unitSize,unitSize))
        self.attributeButton.setObjectName(("attributeButton"))
        self.horizontalLayout_2.addWidget(self.attributeButton)
        self.batchButton = qw.QPushButton(self.centralwidget)
        self.batchButton.setMinimumSize(QtCore.QSize(unitSize,unitSize))
        self.batchButton.setMaximumSize(QtCore.QSize(unitSize,unitSize))
        self.batchButton.setObjectName(("batchButton"))
        self.horizontalLayout_2.addWidget(self.batchButton)
        self.pushButton_3 = qw.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(unitSize,unitSize))
        self.pushButton_3.setMaximumSize(QtCore.QSize(unitSize,unitSize))
        self.pushButton_3.setObjectName(("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.setupButton = qw.QPushButton(self.centralwidget)
        self.setupButton.setMinimumSize(QtCore.QSize(unitSize,unitSize))
        self.setupButton.setMaximumSize(QtCore.QSize(unitSize,unitSize))
        self.setupButton.setObjectName(("setupButton"))
        self.horizontalLayout_2.addWidget(self.setupButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        #====================== tool bar over ==========================

        self.horizontalLayout = qw.QHBoxLayout()
        self.horizontalLayout.setObjectName(("horizontalLayout"))
        self.widget = qw.QWidget(self.centralwidget)
        self.widget.setObjectName(("widget"))
        self.horizontalLayout_3 = qw.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(("horizontalLayout_3"))
        self.splitter = qw.QSplitter(self.widget)
        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.Maximum, qw.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(qw.QFrame.NoFrame)
        self.splitter.setLineWidth(0)
        self.splitter.setMidLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName(("splitter"))
        self.dataListWidget = qw.QWidget(self.splitter)
        self.dataListWidget.setMinimumSize(QtCore.QSize(uiWidth*0.6, 0))
        self.dataListWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dataListWidget.setObjectName(("dataListWidget"))
        self.verticalLayout_5 = qw.QVBoxLayout(self.dataListWidget)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(("verticalLayout_5"))
        self.dataListWidget.setLayout(self.verticalLayout_5)
        self.horizontalLayout_5 = qw.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(("horizontalLayout_5"))
        self.searchLine = qw.QLineEdit(self.dataListWidget)
        self.searchLine.setMinimumSize(QtCore.QSize(0, 0))
        self.searchLine.setReadOnly(True)
        self.searchLine.setObjectName(("searchLine"))
        self.horizontalLayout_5.addWidget(self.searchLine)
        self.configSearchButton = qw.QPushButton(self.dataListWidget)
        self.configSearchButton.setObjectName(("configSearchButton"))
        self.horizontalLayout_5.addWidget(self.configSearchButton)
        self.ruleSearchButton = qw.QPushButton(self.dataListWidget)
        self.ruleSearchButton.setObjectName(("ruleSearchButton"))
        self.horizontalLayout_5.addWidget(self.ruleSearchButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.flowLayout = qw.QGridLayout()
        self.flowLayout.setObjectName(("flowLayout"))

        self.frame = dataItem.dataButton('LookDev','default','001003hello','D:/unit/asset/Main')
        self.flowLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.verticalLayout_5.addLayout(self.flowLayout)
        spacerItem1 = qw.QSpacerItem(160, 40, qw.QSizePolicy.Minimum, qw.QSizePolicy.MinimumExpanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.attributeWidget = qw.QWidget(self.splitter)
        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.MinimumExpanding, qw.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.attributeWidget.sizePolicy().hasHeightForWidth())
        self.attributeWidget.setSizePolicy(sizePolicy)
        self.attributeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.attributeWidget.setMinimumSize(QtCore.QSize(uiWidth*0.3, 16777215))
        self.attributeWidget.setObjectName(("attributeWidget"))
        self.verticalLayout_2 = qw.QVBoxLayout(self.attributeWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(("verticalLayout_2"))
        self.scrollArea = qw.QScrollArea(self.attributeWidget)
        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.Minimum, qw.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(("scrollArea"))
        self.scrollAreaWidgetContents = qw.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 548, 337))

        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.Minimum, qw.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())

        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName(("scrollAreaWidgetContents"))
        self.verticalLayout_3 = qw.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(("verticalLayout_3"))
        self.label = qw.QLabel(self.scrollAreaWidgetContents)

        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.MinimumExpanding, qw.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())

        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(("attributeName"))
        self.verticalLayout_3.addWidget(self.label)

        self.webPage = spoilerItem.FrameLayout(title="Unit History")
        # 这就是折叠页，自己写的

        self.webPage.addWidget(qw.QPushButton('a'))
        
        self.verticalLayout_3.addWidget(self.webPage)


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

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.logoLab.setText(_translate("MainWindow", "logoPic", None))
        self.titleLab.setText(_translate("MainWindow", "TextLabel", None))
        self.maxResumeUI.setText(_translate("MainWindow", "Max", None))
        self.closeBtn.setText(_translate("MainWindow", "x", None))
        self.guildButton.setText(_translate("MainWindow", "Guild", None))
        self.backButton.setText(_translate("MainWindow", "←", None))
        self.upButton.setText(_translate("MainWindow", "↑", None))
        self.projectButton.setText(_translate("MainWindow", "projectName", None))
        self.moduleButton.setToolTip(_translate("MainWindow", "切换视图模式", None))
        self.moduleButton.setText(_translate("MainWindow", "㗊", None))
        self.attributeButton.setStatusTip(_translate("MainWindow", "开启/关闭属性栏", None))
        self.attributeButton.setText(_translate("MainWindow", "三", None))
        self.batchButton.setStatusTip(_translate("MainWindow", "批量操作列表", None))
        self.batchButton.setText(_translate("MainWindow", "车", None))
        self.pushButton_3.setStatusTip(_translate("MainWindow", "待定设置", None))
        self.pushButton_3.setText(_translate("MainWindow", "other", None))
        self.setupButton.setStatusTip(_translate("MainWindow", "设置", None))
        self.setupButton.setText(_translate("MainWindow", "…", None))
        self.configSearchButton.setText(_translate("MainWindow", "search", None))
        self.ruleSearchButton.setText(_translate("MainWindow", "config", None))

        self.label.setText(_translate("MainWindow", "TextLabel", None))
if __name__ == '__main__':
    import os
    app = qw.QApplication.instance()
    if not app:
        app = qw.QApplication( [])




	gg = Ui_MainWindow()
	gg.setupUi()
	
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