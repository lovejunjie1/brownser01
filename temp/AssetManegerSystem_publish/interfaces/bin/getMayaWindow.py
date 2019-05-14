import Qt
from Qt import QtWidgets as qw
if Qt.IsPySide:
    from shiboken import wrapInstance
    
if Qt.IsPySide2:
    from shiboken2 import wrapInstance

import maya.OpenMayaUI as OpenMayaUI
def getMayaWindow():
    """
    Get Maya window
    :return: maya wnd
    """
    mayaMainWindowPtr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(mayaMainWindowPtr), qw.QWidget)