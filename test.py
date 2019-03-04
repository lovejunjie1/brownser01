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

'''

import sys

addPathArray = [r'D:\gitLab\ssToolShelf',r'C:\gitLab\ssToolShelf',r'C:\Python27\Lib\site-packages']
for pt in addPathArray:
    if not pt in sys.path:
        #sys.path.append(pt)
        pass


import sys, os, time, json, shutil, random, math

from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2

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

import bin.Mstyle_RB as Mstyle_RB

Mstyle = Mstyle_RB.RedBlackStyleSheet()
'''
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = qw.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return qw.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return qw.QApplication.translate(context, text, disambig)

class Ui_MainWindow(qw.QMainWindow):
    def setupUi(self):
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(1024, 528)
        self.setMinimumSize(QtCore.QSize(1024, 528))
        self.setWindowOpacity(0.9)
        self.setStyleSheet(_fromUtf8("QPushButton {color:rgb(170, 85, 255);font: 75 9pt \"Arial\";}\n"
"QPushButton#closeBtn { background-color: red }\n"
"QLineEdit{ background-color: red }\n"
"QLineEdit[readOnly=\"true\"]{ background-color: gray }"))
        self.centralwidget = qw.QWidget(self)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = qw.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = qw.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = qw.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_3 = qw.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem = qw.QSpacerItem(0, 0, qw.QSizePolicy.Expanding, qw.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.progressBar = qw.QProgressBar(self.centralwidget)
        self.progressBar.setMinimumSize(QtCore.QSize(50, 0))
        self.progressBar.setMaximumSize(QtCore.QSize(200, 16777215))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(True)
        self.progressBar.setTextDirection(qw.QProgressBar.TopToBottom)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout_4.addWidget(self.progressBar)
        self.pushButton_9 = qw.QPushButton(self.centralwidget)
        self.pushButton_9.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.horizontalLayout_4.addWidget(self.pushButton_9)
        self.closeBtn = qw.QPushButton(self.centralwidget)
        self.closeBtn.setMaximumSize(QtCore.QSize(25, 25))
        self.closeBtn.setObjectName(_fromUtf8("closeBtn"))
        self.horizontalLayout_4.addWidget(self.closeBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = qw.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setSizeConstraint(qw.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.guildButton = qw.QPushButton(self.centralwidget)
        self.guildButton.setMinimumSize(QtCore.QSize(40, 40))
        self.guildButton.setMaximumSize(QtCore.QSize(40, 40))
        self.guildButton.setFlat(False)
        self.guildButton.setObjectName(_fromUtf8("guildButton"))
        self.horizontalLayout_2.addWidget(self.guildButton)
        self.pushButton_5 = qw.QPushButton(self.centralwidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_5.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton = qw.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_8 = qw.QPushButton(self.centralwidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_8.setMaximumSize(QtCore.QSize(0, 40))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.comboBox = qw.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 40))
        self.comboBox.setEditable(True)
        self.comboBox.setSizeAdjustPolicy(qw.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.pushButton_4 = qw.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_4.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_6 = qw.QPushButton(self.centralwidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_6.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_2 = qw.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = qw.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_3.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_7 = qw.QPushButton(self.centralwidget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_7.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = qw.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget = qw.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3 = qw.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.splitter = qw.QSplitter(self.widget)
        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.Minimum, qw.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(qw.QFrame.NoFrame)
        self.splitter.setLineWidth(0)
        self.splitter.setMidLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget_2 = qw.QWidget(self.splitter)
        self.widget_2.setMinimumSize(QtCore.QSize(400, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.verticalLayout_5 = qw.QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_5 = qw.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lineEdit = qw.QLineEdit(self.widget_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.pushButton_12 = qw.QPushButton(self.widget_2)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.horizontalLayout_5.addWidget(self.pushButton_12)
        self.pushButton_11 = qw.QPushButton(self.widget_2)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.horizontalLayout_5.addWidget(self.pushButton_11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.gridLayout = qw.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = qw.QFrame(self.widget_2)
        self.frame.setMinimumSize(QtCore.QSize(120, 72))
        self.frame.setMaximumSize(QtCore.QSize(80, 60))
        self.frame.setFrameShape(qw.QFrame.StyledPanel)
        self.frame.setFrameShadow(qw.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_4 = qw.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(2, 2, 120, 80))
        self.label_4.setMinimumSize(QtCore.QSize(120, 80))
        self.label_4.setText(_fromUtf8(""))
        #self.label_4.setPixmap(qw.QPixmap(_fromUtf8("../Pictures/timg.jpg")))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = qw.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = qw.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 54, 12))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_10 = qw.QPushButton(self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        spacerItem1 = qw.QSpacerItem(160, 40, qw.QSizePolicy.Minimum, qw.QSizePolicy.MinimumExpanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.widget_3 = qw.QWidget(self.splitter)
        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.MinimumExpanding, qw.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout_2 = qw.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea = qw.QScrollArea(self.widget_3)
        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.Minimum, qw.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = qw.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 548, 337))
        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.Minimum, qw.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_3 = qw.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = qw.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.MinimumExpanding, qw.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.toolBox = qw.QToolBox(self.scrollAreaWidgetContents)
        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.Minimum, qw.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMinimumSize(QtCore.QSize(0, 200))
        self.toolBox.setMaximumSize(QtCore.QSize(16777215, 400))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = qw.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 530, 180))
        self.page.setMinimumSize(QtCore.QSize(0, 150))
        self.page.setMaximumSize(QtCore.QSize(16777215, 240))
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_4 = qw.QVBoxLayout(self.page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.webView = QtWebKit.QWebView(self.page)
        self.webView.setMaximumSize(QtCore.QSize(16777215, 200))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout_4.addWidget(self.webView)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.toolBox)
        self.toolBox_2 = qw.QToolBox(self.scrollAreaWidgetContents)
        sizePolicy = qw.QSizePolicy(qw.QSizePolicy.Minimum, qw.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox_2.sizePolicy().hasHeightForWidth())
        self.toolBox_2.setSizePolicy(sizePolicy)
        self.toolBox_2.setObjectName(_fromUtf8("toolBox_2"))
        self.page_3 = qw.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 530, 69))
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.toolBox_2.addItem(self.page_3, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.toolBox_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_3.addWidget(self.splitter)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = qw.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(0)
        self.toolBox_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "logoPic", None))
        self.label_3.setText(_translate("MainWindow", "TextLabel", None))
        self.pushButton_9.setText(_translate("MainWindow", "Max", None))
        self.closeBtn.setText(_translate("MainWindow", "x", None))
        self.guildButton.setText(_translate("MainWindow", "Guild", None))
        self.pushButton_5.setText(_translate("MainWindow", "←", None))
        self.pushButton.setText(_translate("MainWindow", "↑", None))
        self.pushButton_8.setText(_translate("MainWindow", "projectName", None))
        self.pushButton_4.setToolTip(_translate("MainWindow", "切换视图模式", None))
        self.pushButton_4.setText(_translate("MainWindow", "㗊", None))
        self.pushButton_6.setStatusTip(_translate("MainWindow", "开启/关闭属性栏", None))
        self.pushButton_6.setText(_translate("MainWindow", "三", None))
        self.pushButton_2.setStatusTip(_translate("MainWindow", "批量操作列表", None))
        self.pushButton_2.setText(_translate("MainWindow", "车", None))
        self.pushButton_3.setStatusTip(_translate("MainWindow", "待定设置", None))
        self.pushButton_3.setText(_translate("MainWindow", "other", None))
        self.pushButton_7.setStatusTip(_translate("MainWindow", "设置", None))
        self.pushButton_7.setText(_translate("MainWindow", "…", None))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton", None))
        self.label_5.setText(_translate("MainWindow", "TextLabel", None))
        self.label_6.setText(_translate("MainWindow", "TextLabel", None))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton", None))
        self.label.setText(_translate("MainWindow", "TextLabel", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Page 1", None))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_3), _translate("MainWindow", "Page 2", None))



if __name__ == '__main__':
    import os
    app = qw.QApplication.instance()
    if not app:
        app = qw.QApplication([])




	gg = Ui_MainWindow()
	gg.setupUi()
	
	gg.show()
	gg.resize(500,500)
	gg.move(0,0)

    gg.raise_()
    try:
        sys.exit(app.exec_())
    except: pass