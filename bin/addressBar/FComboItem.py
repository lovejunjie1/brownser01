#theItem
from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2
import sys
import os
import logging

class FComboWidget(qw.QComboBox):

    def keyPressEvent(self,event):
        if event.key() == QtCore.Qt.Key_Enter:
            logging.debug( 'enter pressed')


class spoiler(qw.QFrame):
    #clicked = QtCore.Signal(dict)


    def __init__(self,parent=''):
        super(spoiler,self).__init__()
        self.setupUi()
        

    def setupUi(self):

        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setBold(True)
        

        
        self.setFrameShape(qw.QFrame.StyledPanel)
        self.setFrameShadow(qw.QFrame.Raised)
        #self.setObjectName(("frame"))

        self.pushButton = FComboWidget(self)
        #self.pushButton.setEditable(True)
        testHbox = qw.QHBoxLayout(self.pushButton)
        self.pushButton.setLayout(testHbox)
        testHbox.addWidget(qw.QPushButton('hello'))
        #self.pushButton.setMouseTracking(True)
        #self.pushButton.clicked.connect(self.clickAction)
        
        #self.pushButton.setFixedSize(240,160)


        self.Vlay = qw.QVBoxLayout()
        #print dir(self.Vlay)
        self.Vlay.setContentsMargins(3,10,3,3)
        self.Vlay.setSpacing(1)
        self.setLayout(self.Vlay)

        self.Vlay.addWidget(self.pushButton)


    def Op_Ui(self):
        '''
        self.setupUi()
        self.setWidth(240)
        self.setHeight(180)
        picPath = 'D:/unit/asset/Main/CHR_WolfGirl_thum.jpg'
        self.setPicture(picPath)
        self.setName('001001XiaoHunDan')
        self.setVarient('default')
        self.setDep('LookDev')
        '''
        self.show()

if __name__ == '__main__':
    import os
    app = qw.QApplication.instance()
    if not app:
        app = qw.QApplication( [])




    gg = spoiler()
    gg.Op_Ui()
    

    gg.raise_()
    try:
        sys.exit(app.exec_())
    except: pass
