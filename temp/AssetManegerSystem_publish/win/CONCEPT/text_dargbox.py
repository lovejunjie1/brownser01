# -- coding: utf-8 --
import sys, os, json

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt, QRect
filePath = os.path.realpath(__file__)
spPath = filePath.split('AssetManegerSystem_publish')
path = spPath[0] + 'AssetManegerSystem_publish'
if not path in sys.path: sys.path.append(path)
if not path+'\\data' in sys.path: sys.path.append(path+'\\data')
import redBlackStyleSheet_0_10 as RBStyle
Mstyle = RBStyle.RedBlackStyleSheet()



class dragToolListWidget(QtGui.QListWidget):
    isDrag = True
    dragStruct=''

    def __init__(self, parent=None):
        super(dragToolListWidget, self).__init__(parent)

    def mouseMoveEvent(self, e):
        if e.buttons() != QtCore.Qt.LeftButton:
            return

        if not self.isDrag:
            return
        cNode = self.currentItem()
        path = cNode.filePath
        mimeData = QtCore.QMimeData()
        url = QtCore.QUrl.fromLocalFile(QtCore.QFileInfo(path).absoluteFilePath())
        mimeData.setUrls([url])
        self.dragStruct = QtGui.QDrag(self)
        self.dragStruct.setMimeData(mimeData)
        self.dragStruct.setHotSpot(e.pos() - self.rect().topLeft())
        self.dragStruct.exec_(Qt.CopyAction)
        e.accept()

    def mouseDoubleClickEvent(self, e):
        print 'double click'


class dragToolListItem (QtGui.QListWidgetItem):
    # initPath inhert by parent
    filePath = ''
    isDrag = True

    def mouseMoveEvent(self, e):
        if e.buttons() != QtCore.Qt.LeftButton:
            return
        if not self.isDrag:
            return

        mimeData = QtCore.QMimeData()
        url = QtCore.QUrl.fromLocalFile(QtCore.QFileInfo(self.filePath).absoluteFilePath())
        mimeData.setUrls([url])
        self.dragStruct = QtGui.QDrag(self)
        self.dragStruct.setMimeData(mimeData)
        self.dragStruct.setHotSpot(e.pos() - self.rect().topLeft())
        self.dragStruct.exec_(Qt.CopyAction)
        e.accept()


class PictureUploadUI(QtGui.QDialog):
    upload = QtCore.pyqtSignal(list)
    titleName = 'PictureUploadUI'
    widgetHeight = 750
    widgetWidth = 350
    initPath = ''
    UIitems = {}
    jsonPath = ''
    isShowDetail = True
    uploadPicturePath = 'Z:/AssetManegerSystem_publish/icon/conceptUploadPicture.png'
    def __init__(self, parent=None):
        super(PictureUploadUI, self).__init__(parent=None)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle(self.titleName)
        self.setAcceptDrops(True)

        self.createListPage()

    def Cl_Ui(self):
        self.deleteLater()
        self.close()

    def createListPage(self):
        Vbox = QtGui.QVBoxLayout()
        th = QtGui.QHBoxLayout()

        Xbtn = QtGui.QPushButton('x')
        Xbtn.setFixedHeight(28)
        Xbtn.setFixedWidth(28)
        Xbtn.setStyleSheet(Mstyle.xBtnStyle())

        Xbtn.clicked.connect(self.Cl_Ui)
        th.addStretch(1)
        th.addWidget(Xbtn)
        Vbox.addLayout(th)

        notifyLab = QtGui.QLabel()
        notifyLab.setStyleSheet(Mstyle.QLabel(fontSize='13px'))
        notifyLab.setText('please type in the message into textEdit\nplease drag the file into the block')
        # notifyLab write the message to tip user how to use tool
        Vbox.addWidget(notifyLab)

        codec = QtCore.QTextCodec.codecForName("utf-8")
        msg = codec.toUnicode("这个人很懒，什么信息都没留下")
        self.messageBlock = QtGui.QTextEdit()
        self.messageBlock.setFixedHeight(100)
        self.messageBlock.setText(msg)
        self.messageBlock.setStyleSheet(Mstyle.QTextEdit(lang='c')+'QTextEdit {border:1px solid rgb(220,200,200);}')
        Vbox.addWidget(self.messageBlock)

        self.list = dragToolListWidget(self)
        self.list.setIconSize(QtCore.QSize(128, 128))
        self.list.setGeometry(20, 10, 0, 0)
        self.list.setAcceptDrops(True)
        print path

        winPathTemp=path.split('\\')
        winPath='/'.join(winPathTemp)

        print winPath
        self.list.setStyleSheet('QListWidget {border:0px;background:url("' + self.uploadPicturePath + '");background-position:center ;background-repeat: no-repeat}')
        Vbox.addWidget(self.list)
        # drag list created

        subHbox = QtGui.QHBoxLayout()

        uploadBtn = QtGui.QPushButton('upload')
        uploadBtn.setStyleSheet(Mstyle.QPushButton(kw='on'))

        removeBtn = QtGui.QPushButton('remove')
        removeBtn.setStyleSheet(Mstyle.QPushButton(kw='b'))

        subHbox.addWidget(removeBtn)
        subHbox.addWidget(uploadBtn)
        Vbox.addLayout(subHbox)

        self.setLayout(Vbox)

        uploadBtn.clicked.connect(self.uploadFn)
        removeBtn.clicked.connect(self.removeFn)
        return True

    def removeFn(self):
        currentSel = self.list.currentRow()
        self.list.takeItem(currentSel)

    def uploadFn(self):
        count = self.list.count()
        uploadList = []
        for i in range(count):
            itm = self.list.item(i)
            uploadList.append(itm.toolTip())

        msg = self.messageBlock.toPlainText()
        uniMsg = unicode(msg)
        self.upload.emit([uniMsg, uploadList])
        self.Cl_Ui()
    # -------------json--------------

    def saveJson(self, data, path):
        jsonDump = json.dumps(data)
        file_object = open(path, 'w')
        file_object.write(jsonDump)
        file_object.close()

    def loadJson(self, path):
        file_object = open(path, 'r')
        data = json.load(file_object)
        return data

    # ------event rewrite-----------

    def dragEnterEvent(self, e):
        if (e.mimeData().hasFormat("text/uri-list")):
            e.acceptProposedAction()

    def dropEvent(self, e):
        urls = e.mimeData().urls()
        if len(urls) == 0:
            return

        cnt = self.list.count()
        existsArray = []
        for i in range(cnt):
            existsArray.append(self.list.item(i).toolTip())


        picArray = []
        for url in urls:
            strUrl = url.path()[1:]
            fromUrl = '\\'.join(str(strUrl).split('/'))
            if '.jpg' in fromUrl:
                if fromUrl in existsArray:
                    continue
                else:
                    picArray.append(fromUrl)

        for f in picArray:
            icon = QtGui.QIcon(f)
            itm = dragToolListItem(os.path.basename(f))
            itm.setSizeHint(QtCore.QSize(128, 128))
            itm.setIcon(icon)

            itm.filePath = f
            itm.setToolTip(f)
            self.list.addItem(itm)
        self.list.setStyleSheet('QListWidget {border:0px;}')

    def closeEvent(self, e):
        self.deleteLater()

    # ------------widget enter--------------
    def Op_Ui(self):
        self.show()

    def Cl_Ui(self):
        self.close()

'''
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyleSheet('QWidget {background-color:rgb(68,68,68);color:rgb(206,206,206)}')
    MDtoolBUI = PictureUploadUI()
    MDtoolBUI.Op_Ui()
    sys.exit(app.exec_())

'''



