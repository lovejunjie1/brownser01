from PySide import QtCore,QtGui
from PySide.QtCore import Qt



class writerReaderUI(QtGui.QMainWindow):
    UITitle='writerReaderUI'
    x=620
    y=750
    
    def __init__(self, parent = None):
        #------Style Set----------------------------

        super(writerReaderUI, self).__init__(parent)
        self.m_DragPosition=self.pos()
        self.resize(self.x,self.y)
        self.move(402,200)
        #self.setWindowFlags(Qt.SubWindow|Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setWindowTitle(self.UITitle)
        
        self.CreateUI()
        
    def CreateUI(self):
        mian=QtGui.QWidget(self)
        mian.resize(self.x,self.y)
        #close Btn Set   
        Vbox=QtGui.QVBoxLayout()                                    
        self.textWin=QtGui.QTextEdit(mian)
        self.textWin.setReadOnly(True)     
        Vbox.addWidget(self.textWin)
        mian.setLayout(Vbox)

        
        #main btn connect
        
        #self.BtnA1.clicked.connect(self.BtnA1Fn)

    #------------define swtich--------------------
    def setText(self.data):
        self.textWin.setText(data)
    def Op_Ui(self):
        self.show()
    def Cl_Ui(self):
        self.close()
       
#mopImportRT=writerReaderUI()
#mopImportRT.Op_Ui()
#cleanUIRT.Cl_Ui()