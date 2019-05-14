import maya.cmds as cmds
from PySide import QtCore, QtGui
from PySide.QtCore import Qt


class overrideColorUI_RIG_TOOL(QtGui.QWidget):
    overrideColorDialog = None
    colorData = [
        [120, 120, 120],
        [0, 0, 0],
        [64, 64, 64],
        [153, 153, 153],
        [155, 0, 40],
        [0, 4, 96],
        [0, 0, 255],
        [0, 70, 25],
        [38, 0, 67],
        [200, 0, 200],
        [138, 72, 51],
        [63, 35, 31],
        [153, 38, 0],
        [255, 0, 0],
        [0, 255, 0],
        [0, 65, 153],
        [255, 255, 255],
        [255, 255, 0],
        [100, 220, 255],
        [67, 255, 163],
        [255, 176, 176],
        [228, 172, 121],
        [255, 255, 99],
        [0, 153, 84],
        [160, 105, 48],
        [160, 160, 48],
        [105, 160, 48],
        [48, 160, 93],
        [48, 160, 160],
        [48, 105, 160],
        [111, 48, 160],
        [160, 48, 105]
        ]
    
    def createUI(self):

        # ------Style Set----------------------------

        self.m_DragPosition = self.pos()
        self.setParent(getMayaWindow())
        self.resize(280, 600)
        self.move(400, 312)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setStyleSheet(Mstyle.QWidget())
        self.setAttribute(Qt.WA_StyledBackground)
        # -----close Btn Set----------------
        VLy = QtGui.QVBoxLayout(self)
        self.setLayout(VLy)
        girdLy = QtGui.QGridLayout(self)
        HLy = QtGui.QHBoxLayout(self)
        VLy.addLayout(HLy)
        VLy.addLayout(girdLy)
        VLy.setSpacing(10)
                                                      
        Xbtn = QtGui.QPushButton('x',self)
        Xbtn.setGeometry(0, 0, 0, 0)
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())
        HLy.addWidget(Xbtn)  
        Xbtn.clicked.connect(self.Cl_Ui)
        
        # -----TitleLabel-----------------------
        TitleLab=QtGui.QLabel('change select color',self)
        TitleLab.setGeometry(30, 5, 0, 0)
        TitleLab.setFixedHeight(20)
        TitleLab.setFixedWidth(100)
        TitleLab.setStyleSheet(Mstyle.QLabel(fontSize='13px'))
        HLy.addWidget(TitleLab)  
        
        self.clickWithclose = QtGui.QCheckBox('click with close',self)
        self.clickWithclose.setCheckState(Qt.Checked)
        HLy.addWidget(self.clickWithclose)  

        # ------main btn-----------------------
        
        self.BtnArray = []
        
        for index, g in enumerate(self.colorData):
            Btn = QtGui.QPushButton(str(index+1),self)
            Btn.setEnabled(True)
            Btn.setFixedHeight(36)
            Btn.setFixedWidth(36)
            Btn.setStyleSheet(self.quickChangeBtnBgc(g[0], g[1], g[2])) 
            Btn.clicked.connect(self.BtnA1Fn) 
            self.BtnArray.append(Btn)

        lineCount = 0
        spacing = 3
        for count, ba in enumerate(self.BtnArray):
            if count % spacing == 0:
                for l in range(spacing):
                    try:
                        girdLy.addWidget(self.BtnArray[count+l], lineCount, l)
                    except:
                        pass  
                lineCount = lineCount+1

        # ------main btn connect----------------------------
                
    def quickChangeBtnBgc(self,R,G,B):
        darkR = R-80
        if darkR < 0:
            darkR = 0
        darkG = G-80
        if darkG < 0:
            darkG = 0
        darkB = B-80
        if darkB < 0:
            darkB = 0
        btnOnStyle = (  'QPushButton   {font-family:Verdana;font-size:13px;font-weight:None;font-style:oblique;'
                        'border-radius:8px;padding-top:0px;padding-bottom:0px;padding-left:10px;padding-right:10px;'
                        'color:rgb('+str(darkR)+','+str(darkG)+','+str(darkB)+');'
                        'background: rgb('+str(R)+','+str(G)+','+str(B)+');}'
                                    
                        'QPushButton:hover{border-radius:8px;padding-top:-1px;padding-bottom:0px;padding-left:10px;padding-right:10px;'
                        'color:rgb(255,255,255);background: rgb('+str(R)+','+str(G)+','+str(B)+');}'
                                    
                        'QPushButton:pressed{border-radius:8px;padding-top:-1px;padding-bottom:0px;padding-left:10px;padding-right:10px;'
                        'color:rgb(150,150,150);background: rgb('+str(darkR)+','+str(darkG)+','+str(darkB)+');}')
        return btnOnStyle

    # --------main function--------------
    
    def BtnA1Fn(self):
        sender = self.sender() 
        theIndex = int(sender.text())
        theIndex = theIndex-1
        sel = cmds.ls(sl=1)
        
        for s in sel:
            cmds.setAttr(s+'.overrideEnabled', 1)
            cmds.setAttr(s+'.overrideColor', theIndex)
            chids = cmds.listRelatives(s, s=1)
            if chids:
                for c in chids:
                    cmds.setAttr(c+'.overrideEnabled', 0)
                
        if self.clickWithclose.checkState() == Qt.Checked:
            self.close()
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos()-self.pos()
            event.accept()
            
    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
            
    def Op_Ui(self):
        self.show()
        
    def Cl_Ui(self):
        self.deleteLater()
        self.close()


overrideColorUIRT = overrideColorUI_RIG_TOOL()
overrideColorUIRT.createUI()
overrideColorUIRT.Op_Ui()
