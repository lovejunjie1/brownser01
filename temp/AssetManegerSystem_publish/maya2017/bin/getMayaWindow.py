import maya.OpenMayaUI as OpenMayaUI
from PySide2 import QtWidgets
def getMayaWindow():
    """
    Get Maya window
    :return: maya wnd
    """
    mayaMainWindowPtr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(mayaMainWindowPtr), QtWidgets.QWidget)