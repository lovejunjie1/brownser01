from PySide import QtGui, QtCore
from PySide.QtCore import Qt
from data.redBlackStyleSheet08 import RedBlackStyleSheet
Mstyle=RedBlackStyleSheet()
class userLoginUI(QtGui.QMainWindow):
    resultSinal = QtCore.Signal(list)
    UITitle='userLoginUI'
    x=250
    y=150
    result=''
    iconPath=''
    def __init__(self, parent = None):

        
        #------Style Set----------------------------

        super(userLoginUI, self).__init__(parent)
        self.m_DragPosition=self.pos()
        self.setFixedHeight(self.y)
        self.setFixedWidth(self.x)
        #self.resize(self.x,self.y)
        
        self.setWindowFlags(Qt.SubWindow|Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setStyleSheet(Mstyle.mainWidgetStyle())
        self.setWindowTitle(self.UITitle)
        
        self.CreateLogin()

        
    def CreateLogin(self):
        #mian=QtGui.QWidget(self)
        #mian.resize(self.x,self.y)
        #close Btn Set                                       
        Xbtn=QtGui.QPushButton('x',self)
        Xbtn.setGeometry(0,0,0,0)
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())
        Xbtn.clicked.connect(self.Cl_Ui)
        
        #TitleLabel
        TitleLab=QtGui.QLabel(self.UITitle,self)
        TitleLab.setGeometry(40,5,0,0)
        TitleLab.setFixedHeight(20)
        TitleLab.setFixedWidth(140)
        TitleLab.setStyleSheet(Mstyle.LabelStyle(fontSize='12px'))

        #cha sel
        mainGrp=QtGui.QGroupBox('login',self)
        mainGrp.setGeometry(10,25,0,0)
        mainGrp.setFixedHeight(self.y*0.8)
        mainGrp.setFixedWidth(self.x*0.9)
        mainGrp.setStyleSheet(Mstyle.GroupBoxStyle())
        
        okBtn=QtGui.QPushButton('OK',mainGrp)
        okBtn.setGeometry(20,85,0,0)
        okBtn.setFixedHeight(20)
        okBtn.setFixedWidth(80)
        okBtn.setStyleSheet(Mstyle.pushBtnStyle(kw='on'))
        
        cancelBtn=QtGui.QPushButton('cancel',mainGrp)
        cancelBtn.setGeometry(120,85,0,0)
        cancelBtn.setFixedHeight(20)
        cancelBtn.setFixedWidth(80)
        cancelBtn.setStyleSheet(Mstyle.pushBtnStyle(kw='b'))
        
        
        userLab=QtGui.QLabel('user',mainGrp)
        userLab.setGeometry(10,20,0,0)
        userLab.setFixedHeight(20)
        userLab.setFixedWidth(40)
        userLab.setStyleSheet('QLabel{background:transparent;font-size:15px}')
        userLab.setAlignment(Qt.AlignRight)
        
        
        passwordLab=QtGui.QLabel('pass',mainGrp)
        passwordLab.setGeometry(10,50,0,0)
        passwordLab.setFixedHeight(20)
        passwordLab.setFixedWidth(40)
        passwordLab.setStyleSheet('QLabel{background:transparent;font-size:15px}')
        passwordLab.setAlignment(Qt.AlignRight)
        
        self.userLE=QtGui.QLineEdit(mainGrp)
        #self.userLE.setText('user')
        self.userLE.setGeometry(60,20,0,0)
        self.userLE.setFixedHeight(20)
        self.userLE.setFixedWidth(self.x*0.6)
        self.userLE.setStyleSheet(Mstyle.LineEditStyle(fontSize='15px'))
        
        self.passwordLE=QtGui.QLineEdit(mainGrp)
        #self.passwordLE.setText('password')
        self.passwordLE.setGeometry(60,50,0,0)
        self.passwordLE.setFixedHeight(20)
        self.passwordLE.setFixedWidth(self.x*0.6)
        self.passwordLE.setStyleSheet(Mstyle.LineEditStyle(fontSize='15px'))
        self.passwordLE.setEchoMode(self.passwordLE.Password)

        self.userLE.selectionChanged.connect(self.pwLEFn)
        self.passwordLE.selectionChanged.connect(self.pwLEFn)
        
        okBtn.clicked.connect(self.BtnA1Fn)
        cancelBtn.clicked.connect(self.Cl_Ui)
        Xbtn.clicked.connect(self.Cl_Ui)
    #--------------button Fns-----------------------------
    def pwLEFn(self):
        sender=self.sender()
        sender.setText('')
    
    def BtnA1Fn(self):
        self.resultSinal.emit([self.userLE.text(),self.passwordLE.text()])
        self.Cl_Ui()

    #--------------FUNCTIONS-----------------------------


              
    #--------------edit event-----------------------------
    def mousePressEvent(self,event):
        if event.button()==Qt.LeftButton or event.button()==Qt.RightButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
            
    def mouseMoveEvent(self,QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self,QMouseEvent):
        self.m_drag=False

    #------------define swtich--------------------
    def Op_Ui(self):
        self.move(QtGui.QCursor.pos())
        self.show()
        
        
    def Cl_Ui(self):
        self.close()
        self.deleteLater()