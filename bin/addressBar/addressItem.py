# -*- coding: utf-8 -*-
# https://github.com/Longxr/QtAddressBar
from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2
import sys
import os


ARROW_WIDTH = 17
SPACE_WIDTH = 8
ITEM_HEIGHT = 20
#qw.QMenu()
class MenuWidget(qw.QWidget):
    SClickPath = QtCore.Signal(str)
    setupPath = ''
    def main(self,dataString):
        self.setupPath = dataString
        
        dataString = dataString.replace('\\','/')
        dataList = dataString.split('/')
        #print 'dataList',dataList
        self.dataModel = QtCore.QStringListModel()
        self.dataModel.setStringList(dataList)
        #self.dataModel.setReadOnly(True)

        theMV = qw.QVBoxLayout()
        theMV.setMargin(0)
        self.setLayout(theMV)

        theList = qw.QListView()
        theList.setSpacing(0)
        theList.setViewMode(qw.QListView.ListMode)
        theList.setResizeMode(qw.QListView.Adjust)
        theList.setDragEnabled(False)
        
        theList.setEditTriggers(qw.QAbstractItemView.NoEditTriggers)
        
        theList.setModel(self.dataModel)
        theMV.addWidget(theList)

        theList.clicked.connect(self.onClick)

    def updateList(self,dataArray):
        if isinstance(dataArray,list):
            self.dataModel.setStringList(dataArray)
        else:
            print 'type error,please input list type'

    def onClick(self,curr):
        #gg = dir(curr)
        #for g in gg :print g
        #print curr.row()
        #print curr.data()
        self.SClickPath.emit(curr.data())
        #self.hide()

class AddressItem (qw.QPushButton):
    SClickPath = QtCore.Signal(str)
    m_pressed = False
    m_pressedText = False
    m_moveflag = False
    m_bRoot = False

    m_clickmenu = ''
    m_pMenuWidget = ''

    m_textWidth = ''
    m_font = ''

    m_path = ''
    m_text = ''
    def __init__(self,inputStr,parent=None):
        qw.QPushButton.__init__(self, parent=parent)

        inputStr = inputStr.replace('\\','/')
        spStr = inputStr.split('/')
        self.m_text = spStr[-1]
        self.m_path = inputStr

        #def InitUI(self):
        self.m_font = self.parent().font()
        if len(self.m_text) == 0:
            self.m_textWidth= 0
            self.setFixedSize(ARROW_WIDTH,21)
        else:
            fm=QtGui.QFontMetrics(self.m_font)
            self.m_textWidth = fm.width(self.m_text) + SPACE_WIDTH
            self.setFixedSize(self.m_textWidth + ARROW_WIDTH,21)
        # =================
        self.m_normalIcon = QtGui.QPixmap("C:/gitLab/brownser01/icon/back.png")
        self.m_checkedIcon = QtGui.QPixmap("C:/gitLab/brownser01/icon/down.png")

        self.InitUI()

    def setBackIcon(self,flag):


        if(flag) :
            self.m_normalIcon = QtGui.QPixmap("C:/gitLab/brownser01/icon/down.png")
        
        else :
            self.m_normalIcon = QtGui.QPixmap("C:/gitLab/brownser01/icon/back.png")



    def paintEvent(self,event):
        painter = QtGui.QPainter(self)

        if  (self.m_moveflag):
    
            painter.setPen(QtGui.QColor(205, 232, 254));
            painter.fillRect(QtCore.QRectF(0, 0, self.m_textWidth+ARROW_WIDTH, ITEM_HEIGHT), QtGui.QBrush(QtGui.QColor(229, 243, 254)));
            painter.drawRect(QtCore.QRectF(0,0, self.m_textWidth, ITEM_HEIGHT));
            painter.drawRect(QtCore.QRectF(self.m_textWidth, 0, ARROW_WIDTH, ITEM_HEIGHT));
    
        #print 'self.isChecked()',self.isChecked()
        if (self.m_pressed or self.isChecked()):
    
            painter.setPen(QtGui.QColor(153, 209, 255));
            painter.fillRect(QtCore.QRectF(0, 0, self.m_textWidth+ARROW_WIDTH, ITEM_HEIGHT), QtGui.QBrush(QtGui.QColor(204, 232, 255)));
            painter.drawRect(QtCore.QRectF(0,0, self.m_textWidth, ITEM_HEIGHT))
            painter.drawRect(QtCore.QRectF(self.m_textWidth, 0, ARROW_WIDTH, ITEM_HEIGHT))

            painter.setPen(QtGui.QColor(0, 0, 0))
            painter.setFont(self.m_font)
            painter.drawText(QtCore.QRectF(1,1, self.m_textWidth, ITEM_HEIGHT), self.m_text)
            painter.drawPixmap(QtCore.QRectF(self.m_textWidth, 0, ARROW_WIDTH, ITEM_HEIGHT), self.m_checkedIcon, QtCore.QRectF(self.m_checkedIcon.rect()))
        
        else:
        
            painter.setPen(QtGui.QColor(0, 0, 0))
            painter.setFont(self.m_font)
            painter.drawText(QtCore.QRectF(0,0, self.m_textWidth, ITEM_HEIGHT), self.m_text)
            #painter.drawText(self,QtCore.QRectF(0,0, self.m_textWidth, ITEM_HEIGHT), QtCore.Qt.AlignCenter, self.m_text);
            painter.drawPixmap(QtCore.QRectF(self.m_textWidth, 0, ARROW_WIDTH, ITEM_HEIGHT), self.m_normalIcon, QtCore.QRectF(self.m_normalIcon.rect()))


    def mousePressEvent(self,event):
        if(event.button() == QtCore.Qt.LeftButton and self.hitButton(event.pos())) :
            self.m_pressed = True


            if(QtCore.QRectF(0,0, self.m_textWidth, ITEM_HEIGHT).contains(event.pos())):
                self.m_pressed = True

            
            elif(QtCore.QRectF(self.m_textWidth, 0, ARROW_WIDTH, ITEM_HEIGHT).contains(event.pos())) :

                self.update()
                return super(AddressItem, self).mousePressEvent(event)
            
            #print self.text(),event.pos()
            #print 'hit the btn'
            self.update()


    def mouseReleaseEvent(self,event):
        if (event.button() == QtCore.Qt.LeftButton):
            if (self.m_pressedText) :
                print "clicked item";
                self.SClickPath.emit(self.m_path)
            

            self.m_pressedText = False
            self.m_pressed = False

            self.update()

            return super(AddressItem, self).mouseReleaseEvent(event)

    def enterEvent(self,event):
        self.m_moveflag = True
        #print 'enter',self.m_text
        self.update()

    def leaveEvent(self,event):
        self.m_moveflag = False
        #print 'leave',self.m_text
        self.update()

    def menuAboutToHide(self):
        self.m_moveflag = False
        self.m_pressed = False

    def onClickMenuItem(self):
        actionPath = self.m_path + self.sender.text()

        print "clicked menu";
        self.SClickPath.emit(actionPath)

    def onCheckChanged(self,_checked):
        self.update()

        if _checked:
        
            if  not self.m_clickmenu.isVisible(): 
                print 'self.m_text',self.m_text
                print 'self.m_path',self.m_path
                #QPoint GlobalPoint(this->mapToGlobal(QPoint(0,0)));
                GlobalPoint = QtCore.QPoint(self.mapToGlobal(QtCore.QPoint(0,0)))
                GlobalPoint.setX(GlobalPoint.x() + ARROW_WIDTH+ self.m_textWidth - 30)
                GlobalPoint.setY(GlobalPoint.y() + ITEM_HEIGHT)
                self.m_clickmenu.move(GlobalPoint)
                self.m_clickmenu.show()

        else:
            self.m_clickmenu.close()


    def InitUI(self):
        #m_normalIcon = QPixmap(":/res/arrow_right.png");
        #m_checkedIcon = QPixmap(":/res/arrow_down.png");

        self.m_clickmenu = qw.QMenu(self)
        self.m_clickmenu.setWindowFlags(QtCore.Qt.ToolTip)
        #//    setAttribute(Qt::WA_TransparentForMouseEvents);
        #connect(m_clickmenu, SIGNAL(aboutToHide()), this, SLOT(menuAboutToHide()));

        self.m_clickmenu.aboutToHide.connect(self.menuAboutToHide)

        action = qw.QWidgetAction(self)
        self.m_pMenuWidget = MenuWidget()
        self.m_pMenuWidget.main(self.m_path)
        action.setDefaultWidget(self.m_pMenuWidget)
        self.m_clickmenu.addAction(action)

        self.m_clickmenu.setStyleSheet("QMenu {background-color:rgb(242,242,242); border: 1px solid rgb(100,100,100);}\
                         QMenu::item {font-size: 9pt; color: rgb(0,0,0); padding:4px 20px 4px 20px;margin:1px 2px;}\
                         QMenu::item:selected { background-color:rgb(196,222,244);}");

        self.setMouseTracking(True)
        self.setCheckable(True)

        #connect(this, &AddressItem::toggled, this, &AddressItem::onCheckChanged);
        self.toggled.connect(self.onCheckChanged)
        #connect(m_pMenuWidget, &MenuWidget::SClickPath, this, &AddressItem::SClickPath);

        self.m_pMenuWidget.SClickPath.connect(self.SClickPath)