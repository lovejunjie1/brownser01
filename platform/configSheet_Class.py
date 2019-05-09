# -*- coding: utf-8 -*-
import sys,os
toolPath = r'C:\gitLab\brownser01'
if toolPath not in sys.path:
    sys.path.append(toolPath)



from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2

if IsPySide:
    from PySide import QtWebKit
elif IsPySide2:
    from PySide2 import QtWebKit

else:
    from PyQt4 import QtWebKit


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

import json

class configTable(qw.QMainWindow):
    scale = 1
    jsonPath = ''
    def setupUi(self,confPath = ''):

        if os.path.exists(confPath):
            theDir = os.path.dirname(confPath)
            self.jsonPath = theDir + '/configs/universeSet.pipeSet'
            

        else:
            raise ValueError ('input string path error.file not exists')



        #-----------------------------------
        uiWidth = 1280 * self.scale
        uiHeight = 728 * self.scale
        unitSize = 32 * self.scale
        fontHeight = 20 * self.scale

        self.setObjectName('MainUI')
        self.setWindowTitle('pipeline config sheet')
        self.setMinimumSize(QtCore.QSize(uiWidth*0.5, uiHeight*0.5))
        self.resize(uiWidth, uiHeight)
        self.setWindowOpacity(1)
        self.setStyleSheet(("QPushButton {color:rgb(170, 85, 255);font: 75 9pt \"Arial\";}\n"
                    "QPushButton#closeBtn { background-color: red }\n"
                    "QsearchLine{ background-color: red }\n"
                    "QsearchLine[readOnly=\"true\"]{ background-color: gray }"))


        self.centralwidget = qw.QWidget(self)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName(("centralwidget"))
        self.setCentralWidget(self.centralwidget)

        self.mv = qw.QVBoxLayout(self.centralwidget)
        self.mv.setObjectName(("mainVLayout"))

        self.centralwidget.setLayout(self.mv)

        self.mainTable = qw.QTableWidget(0,3)
        self.mv.addWidget(self.mainTable)

        labels = ['Group','Attribute Name','Data']

        self.mainTable.setHorizontalHeaderLabels(labels)
        #print type(self.mainTable.horizontalHeader())
        self.mainTable.horizontalHeader().setResizeMode(0, qw.QHeaderView.Fixed)
        self.mainTable.horizontalHeader().resizeSection(0,400*self.scale)
        self.mainTable.horizontalHeader().setResizeMode(1, qw.QHeaderView.Fixed)
        self.mainTable.horizontalHeader().resizeSection(1,400*self.scale)
        self.mainTable.horizontalHeader().setResizeMode(2, qw.QHeaderView.Stretch)

        self.hor = qw.QHBoxLayout()
        addBtn = qw.QPushButton('add')
        removeBtn = qw.QPushButton('remove')
        saveBtn = qw.QPushButton('save')
        self.hor.addWidget(addBtn)
        self.hor.addWidget(removeBtn)
        self.hor.addStretch()
        self.hor.addWidget(saveBtn)

        self.mv.addLayout(self.hor)

        addBtn.clicked.connect(self.addRowData)
        removeBtn.clicked.connect(self.removeRowData)
        saveBtn.clicked.connect(self.saveTableData)

        self.loadTableData()

    def loadTableData(self):
        dataDict = {}
        with open(self.jsonPath,'r') as f:
            theStrs = f.read()
            dataDict = json.loads(theStrs)
        #self.mainTable.setRowCount()
        #print dataDict

        tableList = []
        for mk,mv in dataDict.items():
            theList = mv.keys()
            theList.sort()
            for key in theList:
                tableList.append([mk,key,mv[key]])

        self.mainTable.setRowCount(len(tableList))
        for count,i in enumerate(tableList):
            for j in range(len(i)):
                item = qw.QTableWidgetItem()
                self.mainTable.setItem(count,j, item);

                item.setText(i[j])
        '''
        for i in range(rowIndex):
            col1 = self.mainTable.item(i,0).text().lower()
            col2 = self.mainTable.item(i,1).text()
            col3 = self.mainTable.item(i,2).text()
            dataDict.update({col1:{col2:col3}})
            #print dir(self.mainTable.item(0,i))
        '''


    def saveTableData(self):
        dataDict = {}
        rowIndex = self.mainTable.rowCount()
        for i in range(rowIndex):
            col1 = self.mainTable.item(i,0).text().lower()
            col2 = self.mainTable.item(i,1).text()
            col3 = self.mainTable.item(i,2).text()

            subDict = {}
            if col1 in dataDict.keys():
                subDict = dict(dataDict[col1])
            subDict.update({col2:col3})

            dataDict.update({col1:subDict})
            #print dir(self.mainTable.item(0,i))
        jDmp = json.dumps(dataDict)
        with open(self.jsonPath,'w') as f:
            f.write(jDmp)

    def addRowData(self):
        rowIndex = self.mainTable.rowCount()
        #print rowIndex
        self.mainTable.setRowCount(rowIndex + 1)

    def removeRowData(self):
        rowIndex = self.mainTable.currentRow()
        if (rowIndex != -1):
             self.mainTable.removeRow(rowIndex)

if __name__ == '__main__':
    app = qw.QApplication.instance()
    if not app:
        app = qw.QApplication( [])

    gg = configTable()
    gg.setupUi(confPath = 'C:/gitLab/brownser01/__init__.py')
    gg.show()
    gg.move(0,0)

    gg.raise_()
    try:
        sys.exit(app.exec_())
    except: pass