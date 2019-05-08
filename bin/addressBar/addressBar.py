# -*- coding: utf-8 -*-

from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2
import sys
import os
import addressItem


ARROW_WIDTH = 17
SPACE_WIDTH = 8
ITEM_HEIGHT = 20
#qw.QMenu()

class QtAddressBar (qw.QLineEdit):
    SCurrentPathChanged = QtCore.Signal(str)
    m_pressed = False
    m_bSelectText = False
    m_currentPath = ''


    def tempInit(self):
        self.m_pMainLayout = qw.QHBoxLayout()
        self.m_pMainLayout.setContentsMargins(1, 1, 1, 1)
        self.m_pMainLayout.setSpacing(0)
        self.setLayout(self.m_pMainLayout)

        self.m_addressGroup = qw.QButtonGroup(self)
        self.m_addressGroup.setExclusive(True)
        self.m_lastCheckBtn = ''

        self.m_addressGroup.buttonClicked.connect(self.onGroupBtnClicked)
        self.clearFocus()

        self.setMouseTracking(True)



    def UpdateCurrentPath(self,thePath):
        self.clearFocus()
        self.clearAddressItem()

        self.m_currentPath = thePath.replace("\\", "/")
        # self.setText(m_currentPath)

        itemsWidth = 0;
        contentWidth = self.width()

        itemList = self.m_currentPath.split("/")
        #itemList = ['root','prj']

        # add root icon
        rootIcon = qw. QLabel(self)
        rootIcon.setFixedSize(17, 20);
        rootIcon.setStyleSheet("QLabel{background-image: url(C:/gitLab/brownser01/icon/home.png);}")

        self.m_pMainLayout.addWidget(rootIcon)

        # add path draw control
        #root = qw.QPushButton('root',self)
        #
        root = addressItem.AddressItem('root',self)
        root.m_pMenuWidget.updateList(['prj','prjWork'])
        #root.m_path = 'root'
        #root.InitUI()
        root.setFixedSize(80,40)
        self.m_pMainLayout.addWidget(root)
        self.m_addressGroup.addButton(root, 0)

        contentWidth = contentWidth - 17

        fullPath = root.m_path
        for i in range(1,len(itemList)):
            print 'itemList[i]',itemList[i]
            
            fullPath = fullPath + '/' + itemList[i]
            #item = addressItem.AddressItem(itemList[i],fullPath,self)
            item = addressItem.AddressItem(fullPath,self)
            item.m_pMenuWidget.updateList(['asset','shots'])
            #item.m_path = fullPath
            #item.InitUI()
            #item = qw.QPushButton(itemList[i],self)
            item.setFixedSize(80,40)
            itemsWidth += item.width()
            print itemsWidth
            self.m_addressGroup.addButton(item, i+1)

            #self.m_pMainLayout.insertWidget(2, item)
            self.m_pMainLayout.addWidget(item)
            #item.SClickPath.connect(self.SCurrentPathChanged)

            if itemsWidth < contentWidth:
                item.show()
                self.m_addressGroup.addButton(item,i)
            else:
                item.hide()


            if itemsWidth > contentWidth:

                root.setBackIcon(True)

        self.m_pMainLayout.addStretch()

    def closeMenu(self):
        if  self.m_lastCheckBtn:
            self.m_addressGroup.setExclusive(False);
            self.m_lastCheckBtn.setChecked(False);
            self.m_addressGroup.setExclusive(True);

            self.m_lastCheckBtn = None

    def mousePressEvent(self,event):
        if event.button()==QtCore.Qt.LeftButton:

           self.m_pressed = True
           print 'left click'
        #qw.QLineEdit.mousePressEvent(event)
        super(QtAddressBar, self).mousePressEvent(event)

    def mouseReleaseEvent(self,event):
        if event.button()==QtCore.Qt.LeftButton and self.m_pressed:
            print "click white space"
            self.m_pressed = False
            self.clearAddressItem()

            self.setText(self.m_currentPath)

        if self.m_bSelectText:
            self.deselect()
            self.m_bSelectText = False
        
        else:
            self.selectAll()
            self.m_bSelectText = True


        super(QtAddressBar, self).mouseReleaseEvent(event)

    def mouseMoveEvent(self,event):
        #print 'self.m_addressGroup.checkedButton()',self.m_addressGroup.checkedButton()
        if (0 != self.m_addressGroup.checkedButton()) and self.m_addressGroup.checkedButton():

            #foreach (QAbstractButton *button, self.m_addressGroup->buttons()) {
            for button in self.m_addressGroup.buttons():
                if button.geometry().contains(event.pos()) and self.m_addressGroup.checkedButton() != button:
                    btn = button
                    btn.setChecked(True)
                    self.m_lastCheckBtn = btn


        #qw.QLineEdit.mouseMoveEvent(event)
        super(QtAddressBar, self).mouseMoveEvent(event)

    def focusInEvent(self,event):
        #qw.QLineEdit.focusInEvent(event)
        pass

    def focusOutEvent(self,event):
        info = QtCore.QFileInfo(self.text())
        if (info.isDir()) :
            self.m_currentPath = info.absoluteFilePath()
        

        self.UpdateCurrentPath(self.m_currentPath)

        super(QtAddressBar, self).focusOutEvent(event)

    def resizeEvent(self,event):
        '''
        if (self.m_pMainLayout.count() >= 2) :

            contentWidth = event.size().width() - 17
            itemsWidth = 0

            for button in self.m_addressGroup.buttons():
                self.m_addressGroup.removeButton(button)
            self.m_lastCheckBtn = None

            for i in range(self.m_pMainLayout.count()-2,2,-1): #root item(0,1) always show, count()-1 is space item
            
                item = self.m_pMainLayout.itemAt(i) #QLayoutItem
                addressItem = item.widget() #qobject_cast<AddressItem *>(item->widget());
                if (addressItem != 0):
                
                    addressItem.hide()
                    itemsWidth += addressItem.width()

                    if (itemsWidth < contentWidth):
                        addressItem.show()
                        self.m_addressGroup.addButton(addressItem, i)

            

            root = self.m_pMainLayout.itemAt(1)
            rootItem = root.widget() #qobject_cast<AddressItem *>(root->widget());
            if (itemsWidth > contentWidth) :
                rootItem.setBackIcon(True)
            
            else:
                rootItem.setBackIcon(False)
        '''
        self.clearFocus()

        super(QtAddressBar, self).resizeEvent(event)

    def keyPressEvent(self,event):
        if (event.key() == QtCore.Qt.Key_Return):
            pathStr = self.text()
            pathStr.replace("\\", "/")
            self.setText('')
            '''
            info = QtCore.QFileInfo(pathStr)

            if (info.isDir()):
                self.m_currentPath = info.absoluteFilePath()
            
            else :
                print "not dir";
        
            '''
            #self.m_currentPath = 'root/prj'
            self.UpdateCurrentPath(self.m_currentPath)
    

        super(QtAddressBar, self).keyPressEvent(event)


    def onGroupBtnClicked(self,button):

        #def onGroupBtnClicked(self,theBtn):
        print 'bar click',button.m_text
        print ''

        if (button == self.m_lastCheckBtn):
            self.m_addressGroup.setExclusive(False)
            button.setChecked(False)
            self.m_addressGroup.setExclusive(True)

            self.m_lastCheckBtn = None
        
        else:
            self.m_lastCheckBtn = button


    def clearAddressItem(self):
        print ''
        print 'in clean'
        print self.m_addressGroup.buttons()
        for button in self.m_addressGroup.buttons():
            self.m_addressGroup.removeButton(button)
    
        self.m_lastCheckBtn = None

        #child = qw.QLayoutItem()
        for i in range(100):
            #try:
            child = self.m_pMainLayout.takeAt(0)
            if child:
                if child.widget():
                    print child
                    child.widget().deleteLater()
                
                #delete(child)
            #except:
            #    continue

    def tempAdd(self):
        self.m_currentPath = 'root/prj'
        self.UpdateCurrentPath(self.m_currentPath)


    # private slots:
    # void onGroupBtnClicked(QAbstractButton*);
    # private:
    # void clearAddressItem();
if __name__ == '__main__':
    import os
    app = qw.QApplication.instance()
    if not app:
        app = qw.QApplication( [])

    dirArray = ['root','asset','cha','lookdev']
    theWid = qw.QWidget()
    #theWid.setFixedSize(100,300)
    thelay = qw.QVBoxLayout()
    theWid.setLayout(thelay)

    QAds = QtAddressBar()
    QAds.tempInit()
    #QAds.m_currentPath = 
    thelay.addWidget(QAds)

    addBtn = qw.QPushButton('add')
    addBtn.clicked.connect(QAds.tempAdd)
    thelay.addWidget(addBtn)

    cleanBtn = qw.QPushButton('clean')
    cleanBtn.clicked.connect(QAds.clearAddressItem)
    thelay.addWidget(cleanBtn)
    
    thelay.addStretch()
    theWid.show()
    theWid.raise_()
    try:
        sys.exit(app.exec_())
    except: pass