import maya.OpenMayaUI as OpenMayaUI
def getMayaWindow():
    """
    Get Maya window
    :return: maya wnd
    """
    mayaMainWindowPtr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(long(mayaMainWindowPtr), QtGui.QWidget)