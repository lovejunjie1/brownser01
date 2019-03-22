# -*- coding: utf-8 -*-
# https://github.com/Longxr/QtAddressBar
from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2
import sys
import os



qw.QMenu()


class AddressItem (qw.QPushButton):
    SClickPath = QtCore.QSignal(str)
    m_pressed = ''
    m_pressedText = ''
    m_moveflag = ''
    m_bRoot = ''

    m_clickmenu = ''
    m_pMenuWidget = ''

    m_textWidth = ''
    m_font = ''

    m_path = ''
    m_text = ''

    m_normalIcon = ''
    m_checkedIcon = ''

    def paintEvent(self,event):
        pass
    def mousePressEvent(self,event):
        pass
    def mouseReleaseEvent(self,event):
        pass
    def enterEvent(self,event):
        pass
    def leaveEvent(self,event):
        pass
    def menuAboutToHide(self):
        pass
    def onClickMenuItem(self):
        pass
    def onCheckChanged(self):
        pass
    def InitUI(self):
        pass
