#theItem
from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2
import sys
import os




class spoiler(qw.QWidget):
    #clicked = QtCore.Signal(dict)
    animationDuration = 300

    def __init__(self,parent=''):
        super(spoiler,self).__init__()

        self.setupUi()
        

    def setupUi(self):
        self.setFixedSize(200,400)
        self.mainLayout = qw.QGridLayout()
        
        
        self.toggleAnimation = QtCore.QParallelAnimationGroup()
        self.contentArea = qw.QScrollArea()


        self.font = QtGui.QFont()
        self.font.setFamily("Arial")
        self.font.setBold(True)

        self.toggleButton = qw.QToolButton()
        self.toggleButton.setStyleSheet("QToolButton { border: none; }")
        self.toggleButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        print dir(QtCore.Qt.ArrowType)
        self.toggleButton.setArrowType(QtCore.Qt.RightArrow)
        self.toggleButton.setText('theTestTitle')
        self.toggleButton.setCheckable(True)
        self.toggleButton.setChecked(False)

        self.headerLine = qw.QFrame()
        self.headerLine.setFrameShape(qw.QFrame.HLine)
        self.headerLine.setFrameShadow(qw.QFrame.Sunken)
        self.headerLine.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Maximum)

        self.contentArea.setStyleSheet("QScrollArea { background-color: white; border: none; }")
        self.contentArea.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Fixed)
        # start out collapsed
        self.contentArea.setMaximumHeight(0)
        self.contentArea.setMinimumHeight(0)
        # let the entire widget grow and shrink with its content
        self.toggleAnimation.addAnimation(QtCore. QPropertyAnimation(self, "minimumHeight"))
        self.toggleAnimation.addAnimation(QtCore. QPropertyAnimation(self, "maximumHeight"))
        self.toggleAnimation.addAnimation(QtCore. QPropertyAnimation(self.contentArea, "maximumHeight"))
        # don't waste space
        self.mainLayout.setVerticalSpacing(0)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        row = 0
        self.mainLayout.addWidget(    self.toggleButton, row, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.mainLayout.addWidget(    self.headerLine, row+1, 2, 1, 1)
        self.mainLayout.addWidget(    self.contentArea, row, 0, 1, 3)
        self.setLayout(    self.mainLayout)

        self.toggleButton.clicked.connect(self.clickedAction)


    def clickedAction(self):
        if self.toggleButton.isChecked():
            self.toggleButton.setArrowType(QtCore.Qt.DownArrow)
            self.toggleAnimation.setDirection(QtCore.QAbstractAnimation.Forward)
        else:
            self.toggleButton.setArrowType(QtCore.Qt.RightArrow)
            self.toggleAnimation.setDirection(QtCore.QAbstractAnimation.Backward)

        self.toggleAnimation.start()


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

    def setContentLayout(self,inputLayout):
        self.contentArea.setLayout(inputLayout)

        #delete contentArea.layout();
        #contentArea.setLayout(&contentLayout);
        collapsedHeight = self.height() - self.contentArea.maximumHeight();
        contentHeight = inputLayout.sizeHint().height()
        for i in range(self.toggleAnimation.animationCount()):
            spoilerAnimation = QtCore.QPropertyAnimation(self.toggleAnimation.animationAt(i))
            
            spoilerAnimation.setDuration(self.animationDuration)
            spoilerAnimation.setStartValue(collapsedHeight)
            spoilerAnimation.setEndValue(collapsedHeight + contentHeight)
        
        contentAnimation = QtCore.QPropertyAnimation(self.toggleAnimation.animationAt(self.toggleAnimation.animationCount() - 1))
        contentAnimation.setDuration(self.animationDuration)
        contentAnimation.setStartValue(0)
        contentAnimation.setEndValue(contentHeight)
        #self.Op_Ui()


if __name__ == '__main__':
    import os
    app = qw.QApplication.instance()
    if not app:
        app = qw.QApplication( [])

    tempWidget = qw.QWidget()
    tempWidget.setFixedSize(500,500)
    tempLayout=qw.QVBoxLayout()
    tempWidget.setLayout(tempLayout)
    txtLayout = qw.QVBoxLayout()
    tempLabel = qw.QLabel('hello there1')
    txtLayout.addWidget(tempLabel)
    print 1

    gg = spoiler()
    gg.setContentLayout(txtLayout)
    tempLayout.addWidget(gg)
    
    print 2
    tempLabe2 = qw.QLabel('hello there2')
    tempLayout.addWidget(tempLabe2)
    tempLayout.addStretch()

    tempWidget.show()
    print 3
    tempWidget.raise_()
    try:
        sys.exit(app.exec_())
    except: pass
