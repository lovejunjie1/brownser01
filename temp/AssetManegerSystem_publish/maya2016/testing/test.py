from shiboken import wrapInstance
from PySide import QtGui
import maya.OpenMayaUI as omUI

import maya.cmds as cmds
from maya.OpenMayaUI import MQtUtil


def maya_window():
    return wrapInstance(long(MQtUtil.mainWindow()), QtGui.QWidget)


class testScreenShot(QtGui.QWidget):
    titleName = 'test'

    def __init__(self, parent=None):
        super(testScreenShot, self).__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setStyleSheet('QWidget{background:rgb(68,68,68);border-radius: 12px}')
        # self.setObjectName('test')
        self.createUI()

    def createUI(self):
        mv = QtGui.QVBoxLayout()
        self.setLayout(mv)

        editor = cmds.modelEditor("test__ME1")
        cmds.modelEditor(editor,
                         edit=True,
                         camera='persp',
                         interactive=False,
                         displayAppearance='smoothShaded',
                         displayTextures=True,
                         headsUpDisplay=False,
                         shadows=True)
        ptr_me = omUI.MQtUtil.findControl(editor)
        self.labPanel = wrapInstance(long(ptr_me), QtGui.QLabel)

        #modPanel = cmds.modelPanel()
        #self.labPanel = wrapInstance(long(MQtUtil.findControl(modPanel)), QtWidgets.QLabel)
        self.labPanel.setFixedSize(400, 300)
        mv.addWidget(self.labPanel)

        saveImageBtn = QtGui.QPushButton('save', self)
        saveImageBtn.setStyleSheet(Mstyle.QPushButton())
        mv.addWidget(saveImageBtn)

        saveImageBtn.clicked.connect(self.btnFn1)

    def btnFn1(self):
        print 'btn1'
        getmap = self.labPanel.pixmap()
        print getmap

    def Op_Ui(self):
        self.setFixedSize(450, 500)
        self.show()

    def Cl_Ui(self):
        self.close()


TSS = testScreenShot()
TSS.Op_Ui()

# TSS.close()

