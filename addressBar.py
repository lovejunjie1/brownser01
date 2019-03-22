# -*- coding: utf-8 -*-

from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2
import sys
import os

class QtAddressBar (qw.QLineEdit):
    SCurrentPathChanged = QtCore.QSignal(str)
    m_pressed = False
    m_bSelectText = False
    m_currentPath = ''


    def tempInit(self):
        m_pMainLayout = qw.QHBoxLayout()
        m_pMainLayout.setContentsMargins(1, 1, 1, 1)
        m_pMainLayout.setSpacing(0)
        self.setLayout(m_pMainLayout)

        m_addressGroup = qw. QButtonGroup(self)
        m_addressGroup.setExclusive(True)
        m_lastCheckBtn = ''

        m_addressGroup.buttonClicked.connect(self.onGroupBtnClicked)
        self.clearFocus()

        self.setMouseTracking(True)


    def onGroupBtnClicked(self,theBtn):
        pass

    def UpdateCurrentPath(self,thePath):
        self.clearFocus()
        self.clearAddressItem()

        m_currentPath = thePath.replace("\\", "/")
        # self.setText(m_currentPath)

        itemsWidth = 0;
        contentWidth = self.width()

        itemList = m_currentPath.split("/")

        # add root icon
        rootIcon = qw. QLabel(self)
        rootIcon.setFixedSize(17, 20);
        rootIcon.setStyleSheet("QLabel{background-image: url(:/res/dir.png);}")

        m_pMainLayout.addWidget(rootIcon)

        # add path draw control
        root = AddressItem('', '', True, self)
        m_pMainLayout.addWidget(root)
        m_addressGroup.addButton(root, 0)

        contentWidth = contentWidth - 17

        for i in range(len(itemList)):
            fullPath = ''
            for j in len(i):
                fullPath = itemList[j] + '/'
            item = AddressItem(itemList[i],fullPath,false,self)
            itemsWidth += item.width()
            print itemsWidth


            m_pMainLayout.insertWidget(2, item)
            item.SClickPath.connect(self.SCurrentPathChanged)

        if itemsWidth < contentWidth:
            item.show()
            m_addressGroup.addButton(item,i)
        else:
            item.hide()


        if itemsWidth > contentWidth:

            root.setBackIcon(True)

        m_pMainLayout.addStretch()

    def closeMenu(self):
        if  m_lastCheckBtn:
            m_addressGroup.setExclusive(False);
            m_lastCheckBtn.setChecked(False);
            m_addressGroup.setExclusive(True);

            m_lastCheckBtn = False

    def mousePressEvent(self,event):
        if event.button()==QtCore.Qt.LeftButton:

            m_pressed = True

        qw.QLineEdit.mousePressEvent(event)

    def mouseReleaseEvent(self,event):
        if event.button()==QtCore.Qt.LeftButton and m_pressed
            print "click white space"
            m_pressed = False
            clearAddressItem()

            self.setText(m_currentPath)

        if m_bSelectText:
            self.deselect()
            m_bSelectText = False
        
        else:
            self.selectAll()
            m_bSelectText = True


        qw.QLineEdit.mouseReleaseEvent(event)

    def mouseMoveEvent(self,event):
        if (0 != m_addressGroup.checkedButton()):

       #foreach (QAbstractButton *button, m_addressGroup->buttons()) {
        for button in m_addressGroup.buttons():
          if button.geometry().contains(event->pos()) and m_addressGroup.checkedButton() != button:
              btn = button
              btn.setChecked(True)
              m_lastCheckBtn = btn


        qw.QLineEdit.mouseMoveEvent(event)

    def focusInEvent(self,event):
        qw.QLineEdit.focusInEvent(event)

    def focusOutEvent(self,event):
        info = qw.QFileInfo(self.text())
        if (info.isDir()) :
            m_currentPath = info.absoluteFilePath()
        

        self.UpdateCurrentPath(m_currentPath)

        qw.QLineEdit.focusOutEvent(event)

    def resizeEvent(self,event):
        if (m_pMainLayout.count() >= 2) :

            contentWidth = event.size().width() - 17
            itemsWidth = 0

            for button in m_addressGroup.buttons():
                m_addressGroup.removeButton(button)
            m_lastCheckBtn = None

            for i in range(m_pMainLayout->count()-2,2,-1): #root item(0,1) always show, count()-1 is space item
            
                item = m_pMainLayout.itemAt(i) #QLayoutItem
                addressItem = item.widget() #qobject_cast<AddressItem *>(item->widget());
                if (addressItem != 0):
                
                    addressItem.hide()
                    itemsWidth += addressItem.width()

                    if (itemsWidth < contentWidth):
                        addressItem.show()
                        m_addressGroup.addButton(addressItem, i)

            

            root = m_pMainLayout.itemAt(1)
            rootItem = root.widget() #qobject_cast<AddressItem *>(root->widget());
            if (itemsWidth > contentWidth) :
                rootItem.setBackIcon(True)
            
            else:
                rootItem.setBackIcon(False)
        self.clearFocus()

        qw.QLineEdit.resizeEvent(event)

    def keyPressEvent(self,event):
        if (event.key() == QtCore.Qt.Key_Return):
        pathStr = self.text()
        pathStr.replace("\\", "/");
        info = qw.QFileInfo(pathStr);

        if (info.isDir()):
            m_currentPath = info.absoluteFilePath()
        
        else :
            print "not dir";
        

        self.UpdateCurrentPath(m_currentPath)
    

        qw.QLineEdit.keyPressEvent(event)


    def onGroupBtnClicked(self,button):

        if (button == m_lastCheckBtn):
            m_addressGroup.setExclusive(False)
            button.setChecked(False)
            m_addressGroup.setExclusive(True)

            m_lastCheckBtn = None
        
        else:
            m_lastCheckBtn = button


    def clearAddressItem(self):
        for button in m_addressGroup:
            m_addressGroup.removeButton(button)
    
        m_lastCheckBtn = None

        child = qw.QLayoutItem()
        while ((child = m_pMainLayout.takeAt(0)) != 0):
            if child.widget():
            
                child.widget().deleteLater()
            
            child.parent(None)



    # private slots:
    # void onGroupBtnClicked(QAbstractButton*);
    # private:
    # void clearAddressItem();
