from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtCore import Qt


class assetManager_userLoginUI(QtWidgets.QMainWindow):
    resultSinal = QtCore.Signal(list)
    UITitle='userLoginUI'
    x=250
    y=150
    result=''
    iconPath=''
    def __init__(self, parent = None):

        
        #------Style Set----------------------------

        super(assetManager_userLoginUI, self).__init__(parent)
        self.m_DragPosition=self.pos()
        self.setFixedHeight(self.y)
        self.setFixedWidth(self.x)
        #self.resize(self.x,self.y)
        
        self.setWindowFlags(Qt.SubWindow|Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setStyleSheet('QWidget {background-color :rgb(68,68,68);border:0px solid rgb(143,143,143);color:rgb(206,206,206);}')
        self.setWindowTitle(self.UITitle)
        
        self.CreateLogin()

        
    def CreateLogin(self):
        #mian=QtGui.QWidget(self)
        #mian.resize(self.x,self.y)
        #close Btn Set                                       
        Xbtn=QtWidgets.QPushButton('x',self)
        Xbtn.setGeometry(0,0,0,0)
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())
        Xbtn.clicked.connect(self.Cl_Ui)
        
        #TitleLabel
        TitleLab=QtWidgets.QLabel(self.UITitle,self)
        TitleLab.setGeometry(40,5,0,0)
        TitleLab.setFixedHeight(20)
        TitleLab.setFixedWidth(140)
        TitleLab.setStyleSheet(Mstyle.QLabel(fontSize='12px'))

        #cha sel
        mainGrp=QtWidgets.QGroupBox('login',self)
        mainGrp.setGeometry(10,25,0,0)
        mainGrp.setFixedHeight(self.y*0.8)
        mainGrp.setFixedWidth(self.x*0.9)
        mainGrp.setStyleSheet(Mstyle.QGroupBox())
        
        okBtn=QtWidgets.QPushButton('OK',mainGrp)
        okBtn.setGeometry(20,85,0,0)
        okBtn.setFixedHeight(20)
        okBtn.setFixedWidth(80)
        okBtn.setStyleSheet(Mstyle.QPushButton(kw='on'))
        
        cancelBtn=QtWidgets.QPushButton('cancel',mainGrp)
        cancelBtn.setGeometry(120,85,0,0)
        cancelBtn.setFixedHeight(20)
        cancelBtn.setFixedWidth(80)
        cancelBtn.setStyleSheet(Mstyle.QPushButton(kw='b'))
        
        
        userLab=QtWidgets.QLabel('user',mainGrp)
        userLab.setGeometry(10,20,0,0)
        userLab.setFixedHeight(20)
        userLab.setFixedWidth(40)
        userLab.setStyleSheet('QLabel{background:transparent;font-size:15px}')
        userLab.setAlignment(Qt.AlignRight)
        
        
        passwordLab=QtWidgets.QLabel('pass',mainGrp)
        passwordLab.setGeometry(10,50,0,0)
        passwordLab.setFixedHeight(20)
        passwordLab.setFixedWidth(40)
        passwordLab.setStyleSheet('QLabel{background:transparent;font-size:15px}')
        passwordLab.setAlignment(Qt.AlignRight)
        
        self.userLE=QtWidgets.QLineEdit(mainGrp)
        #self.userLE.setText('user')
        self.userLE.setGeometry(60,20,0,0)
        self.userLE.setFixedHeight(20)
        self.userLE.setFixedWidth(self.x*0.6)
        self.userLE.setStyleSheet(Mstyle.QLineEdit(fontSize='15px'))
        
        self.passwordLE=QtWidgets.QLineEdit(mainGrp)
        #self.passwordLE.setText('password')
        self.passwordLE.setGeometry(60,50,0,0)
        self.passwordLE.setFixedHeight(20)
        self.passwordLE.setFixedWidth(self.x*0.6)
        self.passwordLE.setStyleSheet(Mstyle.QLineEdit(fontSize='15px'))
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
        
#gg=assetManager_userLoginUI()
#gg.Op_Ui()