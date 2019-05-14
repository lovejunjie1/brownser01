from PySide2 import QtWidgets,QtCore,QtGui
from PySide2.QtCore import Qt

class assetManager_RightClickTreeWidget(QtWidgets.QTreeWidget):

    def __init__(self, parent=None):
        super(assetManager_RightClickTreeWidget, self).__init__(parent)
        self.pathList = getAssetManagerPath()
        self.initPath = self.pathList['main']
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.setSelectionMode(self.ExtendedSelection)


    def showContextMenu(self, pos):
        iconPath = self.pathList['icon']

        self.contextMenu = QtWidgets.QMenu(self)
        self.contextMenu.setStyleSheet(Mstyle.QMenu())

        if self.currentItem().parent():
            actionA = self.contextMenu.addAction(QtGui.QIcon(iconPath + brush.png), u'rename')
            actionA.triggered.connect(self.actionAFn)
            actionB = self.contextMenu.addAction(QtGui.QIcon(iconPath + cross.png), u'delete')
            actionB.triggered.connect(self.actionBFn)

        self.contextMenu.exec_(QtGui.QCursor.pos())  # show menu on cursor pos

    def checkName(self,Name):
        ans = [False,'']
        tag = ['dif','spc','bmp','nor','dis','sss','gls','msk','trs']
        spName = Name.split('.')
        fileName = spName[0]
        if '.' in fileName:
            ans[1] = 'too many . in '+fileName
            return ans
         
        spFile = fileName.split('_')
        if len(spFile)>3:
            ans[1] = 'too many _ in '+fileName+'nTip  [chaName]_[partName]_[tag]'
        elif len(spFile)<3:
            ans[1] = 'name length not enough.nTip  [chaName]_[partName]_[tag]'   
        elif len(spFile)==3:
            if spFile[-1] in tag:
                ans[0]=True
                ans[1]='pass'
            else:
                ans[1]='tag name '+spFile[-1]+' not legal.n Tip  dif,spc,bmp,nor,dis,sss,gls,msk,trs'
        

    def actionAFn(self):
        
        name,ok = QtWidgets.QInputDialog.getText(self,'inputName','please input name',
                                       QtWidgets.QLineEdit.Normal,'chaname_partname_tag')
        if ok and (len(name)!=0):
            print name
            ans = self.checkName(name)
            print ans
