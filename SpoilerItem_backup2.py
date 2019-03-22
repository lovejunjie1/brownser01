#theItem
from Qt import QtWidgets as qw, QtGui, QtCore, IsPySide, IsPySide2
import sys
import os



class FrameLayout(qw.QWidget):
    def __init__(self, parent=None, title=None):
        qw.QFrame.__init__(self, parent=parent)

        self._is_collasped = True
        self._title_frame = None
        self._content, self._content_layout = (None, None)

        self._main_v_layout = qw.QVBoxLayout(self)
        self._main_v_layout.addWidget(self.initTitleFrame(title, self._is_collasped))
        self._main_v_layout.addWidget(self.initContent(self._is_collasped))

        self.initCollapsable()

    def initTitleFrame(self, title, collapsed):
        self._title_frame = self.TitleFrame(title=title, collapsed=collapsed)

        return self._title_frame

    def initContent(self, collapsed):
        self._content = qw.QWidget()
        self._content_layout = qw.QVBoxLayout()

        self._content.setLayout(self._content_layout)
        self._content.setVisible(not collapsed)

        return self._content

    def addWidget(self, widget):
        self._content_layout.addWidget(widget)

    def initCollapsable(self):
        QtCore.QObject.connect(self._title_frame, QtCore.SIGNAL('clicked()'), self.toggleCollapsed)

    def toggleCollapsed(self):
        self._content.setVisible(self._is_collasped)
        self._is_collasped = not self._is_collasped
        self._title_frame._arrow.setArrow(int(self._is_collasped))

    ############################
    #           TITLE          #
    ############################
    class TitleFrame(qw.QFrame):
        def __init__(self, parent=None, title="", collapsed=False):
            qw.QFrame.__init__(self, parent=parent)

            self.setMinimumHeight(24)
            self.move(QtCore.QPoint(24, 0))
            self.setStyleSheet("border:1px solid rgb(41, 41, 41); ")

            self._hlayout = qw.QHBoxLayout(self)
            self._hlayout.setContentsMargins(0, 0, 0, 0)
            self._hlayout.setSpacing(0)

            self._arrow = None
            self._title = None

            self._hlayout.addWidget(self.initArrow(collapsed))
            self._hlayout.addWidget(self.initTitle(title))

        def initArrow(self, collapsed):
            self._arrow = FrameLayout.Arrow(collapsed=collapsed)
            self._arrow.setStyleSheet("border:0px")

            return self._arrow

        def initTitle(self, title=None):
            self._title = qw.QLabel(title)
            self._title.setMinimumHeight(24)
            self._title.move(QtCore.QPoint(24, 0))
            self._title.setStyleSheet("border:0px")

            return self._title

        def mousePressEvent(self, event):
            self.emit(QtCore.SIGNAL('clicked()'))

            return super(FrameLayout.TitleFrame, self).mousePressEvent(event)


    #############################
    #           ARROW           #
    #############################
    class Arrow(qw.QFrame):
        def __init__(self, parent=None, collapsed=False):
            qw.QFrame.__init__(self, parent=parent)

            self.setMaximumSize(24, 24)

            # horizontal == 0
            self._arrow_horizontal = (QtCore.QPointF(7.0, 8.0), QtCore.QPointF(17.0, 8.0), QtCore.QPointF(12.0, 13.0))
            # vertical == 1
            self._arrow_vertical = (QtCore.QPointF(8.0, 7.0), QtCore.QPointF(13.0, 12.0), QtCore.QPointF(8.0, 17.0))
            # arrow
            self._arrow = None
            self.setArrow(int(collapsed))

        def setArrow(self, arrow_dir):
            if arrow_dir:
                self._arrow = self._arrow_vertical
            else:
                self._arrow = self._arrow_horizontal

        def paintEvent(self, event):
            painter = qw.QPainter()
            painter.begin(self)
            painter.setBrush(qw.QColor(192, 192, 192))
            painter.setPen(qw.QColor(64, 64, 64))
            painter.drawPolygon(*self._arrow)
            painter.end()

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
