from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import Qt
import sys
filePath = __file__
spPath = filePath.split('AssetManegerSystem')
path = spPath[0] + 'AssetManegerSystem'
if not path in sys.path: sys.path.append(path)
if not path+'\\data' in sys.path: sys.path.append(path+'\\data')
import redBlackStyleSheet_0_10 as RBStyle
Mstyle = RBStyle.RedBlackStyleSheet()


class writerReaderUI(QtGui.QWidget):
    UITitle = 'writerReaderUI'
    x = 620
    y = 750
    textWin = ''
    mian = ''

    def __init__(self, parent=None):
        # ------Style Set----------------------------

        super(writerReaderUI, self).__init__(parent)
        self.m_DragPosition = self.pos()
        self.resize(self.x, self.y)
        self.move(402, 200)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setWindowTitle(self.UITitle)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setStyleSheet('QWidget:{background:rgb(68,68,68);}')
        self.CreateUI()
        
    def CreateUI(self):
        self.mian = QtGui.QWidget(self)
        self.mian.resize(self.x, self.y)
        # close Btn Set
        Vbox = QtGui.QVBoxLayout()

        Xbtn = QtGui.QPushButton('x')
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())
        Xbtn.clicked.connect(self.Cl_Ui)

        btn2 = QtGui.QPushButton("_", self)
        btn2.clicked.connect(self.showMinimized)
        btn2.setStyleSheet(Mstyle.xBtnStyle())
        btn2.setFixedHeight(28)
        btn2.setFixedWidth(28)
        btn3 = QtGui.QPushButton("o", self)
        btn3.clicked.connect(self.showMaximized)
        btn3.setStyleSheet(Mstyle.xBtnStyle())
        btn3.setFixedHeight(28)
        btn3.setFixedWidth(28)

        Hbox=QtGui.QHBoxLayout()
        Hbox.addWidget(Xbtn)
        Hbox.addWidget(btn2)
        Hbox.addWidget(btn3)
        Hbox.addStretch(1)
        Vbox.addLayout(Hbox)

        self.textWin = QtGui.QTextEdit(self.mian)
        self.textWin.setReadOnly(True)
        self.textWin.setStyleSheet(Mstyle.QTextEdit()+Mstyle.QScrollBar())
        Vbox.addWidget(self.textWin)
        self.mian.setLayout(Vbox)

    # ------------define swtich--------------------
    def setText(self, data):
        self.textWin.setText(data)

    def Op_Ui(self):
        self.show()

    def Cl_Ui(self):
        self.close()


    def resizeEvent(self, event):
        self.mian.resize(self.width(), self.height()-25)
        #self.textWin.resize(self.width(), self.height()-25)


# mopImportRT=writerReaderUI()
# mopImportRT.Op_Ui()
# cleanUIRT.Cl_Ui()
