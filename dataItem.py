#theItem
from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2
import sys
import os


qssString = ''





class dataButton(qw.QFrame):

    def setWidth(self,val):
        print 'setWidth'
        self.setFixedWidth(val)
    def setHeight(self,val):
        print 'setHeight'
        self.setFixedHeight(val)

    def setupUi(self):

        #self = qw.QFrame(self.dataListWidget)

        self.setFrameShape(qw.QFrame.StyledPanel)
        self.setFrameShadow(qw.QFrame.Raised)
        self.setObjectName(("frame"))
        self.devLab = qw.QLabel(self)
        self.devLab.setGeometry(QtCore.QRect(2, 2, 120, 80))
        self.devLab.setMinimumSize(QtCore.QSize(120, 80))
        #self.devLab.setPixmap(qw.QPixmap(("../Pictures/timg.jpg")))
        self.devLab.setObjectName(("devLab"))
        self.devLab.setText('lookDev')

        self.nameLab = qw.QLabel(self)
        self.nameLab.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.nameLab.setObjectName(("nameLab"))
        self.nameLab.setText('001003hello')

        self.verLab = qw.QLabel(self)
        self.verLab.setGeometry(QtCore.QRect(10, 30, 54, 12))
        self.verLab.setObjectName(("verLab"))
        self.verLab.setText('default')

        self.addToChartButton = qw.QPushButton(self)
        self.addToChartButton.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.addToChartButton.setObjectName(("addToChartButton"))
        self.addToChartButton.setText('+')
        #self.flowLayout.addWidget(self, 0, 0, 1, 1)

    def Op_Ui(self):
    	self.setupUi()
        self.setWidth(140)
        self.setHeight(180)
    	self.show()

if __name__ == '__main__':
    import os
    app = qw.QApplication.instance()
    if not app:
        app = qw.QApplication( [])




	gg = dataButton()
	gg.Op_Ui()
	

    gg.raise_()
    try:
        sys.exit(app.exec_())
    except: pass
