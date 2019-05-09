# -*- coding: utf-8 -*-
# https://github.com/Longxr/QtAddressBar
from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2
import sys
import os


'''
class MenuWidget(qw.QWidget):
    SClickPath = QtCore.Sinal(str)
    m_bRoot = False
    m_pDirModel = None
    m_pRootModel = None

    def __init__(isRoot, parent = 0):
        
        ui.setupUi(this)

        if self.m_bRoot:
            m_pRootModel = qw. QStandardItemModel(self)
            ui.listView.setModel(m_pRootModel)
            self.setRootModel()
        
        else :
            self.m_pDirModel = new QDirModel(this);
            self.m_pDirModel.setReadOnly(false);
            self.m_pDirModel.setFilter(QDir::Dirs | QDir::NoDotAndDotDot);
            ui.listView.setModel(self.m_pDirModel);
        

            #//    ui.listView.setItemDelegate(m_Delegate);
        ui.listView.setSpacing(0);
        ui.listView.setViewMode(QListView::ListMode);
        ui.listView.setResizeMode(QListView::Adjust);
        ui.listView.setDragEnabled(false);

    def updateDirModel(_str):
        QFileInfo info(path);
        if(info.isDir()) :
            m_pDirModel->refresh(m_pDirModel->index(path));
            ui->listView->setRootIndex(m_pDirModel->index(path));


    def on_listView_clicked(_index):
        QString path = index.data(Qt::UserRole + 1).toString();
        qDebug() << "path: " << path;

        emit SClickPath(path);

    def adjustMenuSize():
        pass
    def setRootModel():
        m_pRootModel->clear();

        QStandardItem* item1 = new QStandardItem();
        item1->setData(QIcon(":/res/dir.png"), Qt::DecorationRole);
        item1->setData(tr("Desktop"), Qt::DisplayRole);
        item1->setData(QStandardPaths::writableLocation(QStandardPaths::DesktopLocation), Qt::UserRole + 1);
        m_pRootModel->appendRow(item1);

        QStandardItem* item2 = new QStandardItem();
        item2->setData(QIcon(":/res/dir.png"), Qt::DecorationRole);
        item2->setData(tr("Documents"), Qt::DisplayRole);
        item2->setData(QStandardPaths::writableLocation(QStandardPaths::DocumentsLocation), Qt::UserRole + 1);
        m_pRootModel->appendRow(item2);

        QStandardItem* item3 = new QStandardItem();
        item3->setData(QIcon(":/res/dir.png"), Qt::DecorationRole);
        item3->setData(tr("Pictures"), Qt::DisplayRole);
        item3->setData(QStandardPaths::writableLocation(QStandardPaths::PicturesLocation), Qt::UserRole + 1);
        m_pRootModel->appendRow(item3);
'''
class MenuWidget(qw.QWidget):
    SClickPath = QtCore.Signal(str)
    def main(self,dataList):
        #dataList = ['aa','vv','fff','ggg']
        self.dataModel = QtCore.QStringListModel()
        self.dataModel.setStringList(dataList)
        self.dataModel.setReadOnly(True)

        theMV = qw.QVBoxLayout()
        theMV.setMargin(0)
        self.setLayout(theMV)

        theList = qw.QListView()
        theList.setEditTriggers(qw.QAbstractItemView.NoEditTriggers)
        theList.setReadOnly(True)
        theList.setSpacing(0)
        theList.setViewMode(qw.QListView.ListMode)
        theList.setResizeMode(qw.QListView.Adjust)
        theList.setDragEnabled(False)
        
        theList.setModel(self.dataModel)
        theMV.addWidget(theList)

        theList.clicked.connect(self.onClick)
    def onClick(self,curr):
        #gg = dir(curr)
        #for g in gg :print g
        #print curr.row()
        #print curr.data()
        self.SClickPath.emit(curr.data())

        print 'emit',curr.data()
        self.Hide()






if __name__ == '__main__':
    import os
    app = qw.QApplication.instance()
    if not app:
        app = qw.QApplication( [])

    dirArray = ['root','asset','cha','lookdev']
    theWid = MenuWidget()
    theWid.main(dirArray)
    theWid.show()
    theWid.raise_()
    try:
        sys.exit(app.exec_())
    except: pass
