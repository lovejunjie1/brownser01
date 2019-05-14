# -*- coding:gbk -*-
import sys, subprocess, time, os, shutil
from PySide2 import QtGui, QtCore, QtWidgets
from PySide2.QtCore import Qt


class FTextEdit(QtWidgets.QTextEdit):
    copySignal = QtCore.Signal(str)

    def keyPressEvent(self, e):
        if (e.type() == QtCore.QEvent.KeyPress):
            if e.matches(QtGui.QKeySequence.Paste):
                self.copySignal.emit('copy')
        super(FTextEdit, self).keyPressEvent(e)


class assetManager_writterUI(QtWidgets.QMainWindow):
    saveSignal = QtCore.Signal(list)
    initPath = ''
    savePath = ''
    itemName = ''
    filename = ''

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.changesSaved = True

        self.initPath = getAssetManagerPath()['icon'] + '\\writer_icon\\'

        self.setWindowFlags(Qt.Widget | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet('QWidget{background:rgb(68,68,68)}')
        # self.initUI()

    def initToolbar(self):
        # print self.initPath+"new.png"
        self.newAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "new.png"), "New", self)
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.setStatusTip("Create a new document from scratch.")
        self.newAction.triggered.connect(self.new)

        self.openAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "open.png"), "Open file", self)
        self.openAction.setStatusTip("Open existing document")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)

        self.saveAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "save.png"), "Save", self)
        self.saveAction.setStatusTip("Save document")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)

        self.saveasAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "save.png"), "Save as ...", self)
        self.saveasAction.setStatusTip("Save document as ...")
        self.saveasAction.setShortcut("Ctrl+SHIFT+S")
        self.saveasAction.triggered.connect(self.saveas)

        self.cutImageAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "print.png"), "Cut Image", self)
        self.cutImageAction.setStatusTip("Cut windows Image")
        self.cutImageAction.setShortcut("Alt+A")
        self.cutImageAction.triggered.connect(self.cutImage)

        self.previewAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "preview.png"), "Page view", self)
        self.previewAction.setStatusTip("Preview page before printing")
        self.previewAction.setShortcut("Ctrl+Shift+P")
        self.previewAction.triggered.connect(self.preview)

        self.closeAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "cross.png"), "Close Widget", self)
        self.closeAction.setStatusTip("Close whole edit window")
        self.closeAction.setShortcut("Ctrl+Shift+W")
        self.closeAction.triggered.connect(self.Cl_Ui)

        self.findAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "find.png"), "Find and replace", self)
        self.findAction.setStatusTip("Find and replace words in your document")
        self.findAction.setShortcut("Ctrl+F")
        self.findAction.triggered.connect(docWritter_Find(self).show)

        self.cutAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "cut.png"), "Cut to clipboard", self)
        self.cutAction.setStatusTip("Delete and copy text to clipboard")
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.triggered.connect(self.text.cut)

        self.copyAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "copy.png"), "Copy to clipboard", self)
        self.copyAction.setStatusTip("Copy text to clipboard")
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.text.copy)

        self.pasteAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "paste.png"), "Paste from clipboard", self)
        self.pasteAction.setStatusTip("Paste text from clipboard")
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.pasteFn)

        self.undoAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "undo.png"), "Undo last action", self)
        self.undoAction.setStatusTip("Undo last action")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.text.undo)

        self.redoAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "redo.png"), "Redo last undone thing", self)
        self.redoAction.setStatusTip("Redo last undone thing")
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.text.redo)

        dateTimeAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "calender.png"), "Insert current date/time", self)
        dateTimeAction.setStatusTip("Insert current date/time")
        dateTimeAction.setShortcut("Ctrl+D")
        # dateTimeAction.triggered.connect(datetime.DateTime(self).show)

        wordCountAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "count.png"), "See word/symbol count", self)
        wordCountAction.setStatusTip("See word/symbol count")
        wordCountAction.setShortcut("Ctrl+W")
        wordCountAction.triggered.connect(self.wordCount)

        tableAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "table.png"), "Insert table", self)
        tableAction.setStatusTip("Insert table")
        tableAction.setShortcut("Ctrl+T")
        tableAction.triggered.connect(docWritter_Table(self).show)

        imageAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "image.png"), "Insert image", self)
        imageAction.setStatusTip("Insert image")
        imageAction.setShortcut("Ctrl+Shift+I")
        imageAction.triggered.connect(self.insertImage)

        bulletAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "bullet.png"), "Insert bullet List", self)
        bulletAction.setStatusTip("Insert bullet list")
        bulletAction.setShortcut("Ctrl+Shift+B")
        bulletAction.triggered.connect(self.bulletList)

        numberedAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "number.png"), "Insert numbered List", self)
        numberedAction.setStatusTip("Insert numbered list")
        numberedAction.setShortcut("Ctrl+Shift+L")
        numberedAction.triggered.connect(self.numberList)

        self.toolbar = self.addToolBar("Options")

        # self.toolbar.addAction(self.newAction)
        # self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)
        self.toolbar.addAction(self.previewAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)
        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.findAction)
        self.toolbar.addAction(dateTimeAction)
        self.toolbar.addAction(wordCountAction)
        self.toolbar.addAction(tableAction)
        self.toolbar.addAction(imageAction)
        self.toolbar.addAction(self.cutImageAction)
        self.toolbar.addSeparator()

        self.toolbar.addAction(bulletAction)
        self.toolbar.addAction(numberedAction)
        self.toolbar.addSeparator()

        self.toolbar.addAction(self.closeAction)

        self.addToolBarBreak()

    def initFormatbar(self):
        dFormat = QtGui.QTextCharFormat()
        dFormat.setFontPointSize(16)
        dFormat.setFontFamily('Microsoft YaHei')

        fontBox = QtWidgets.QFontComboBox(self)
        fontBox.currentFontChanged.connect(lambda font: self.text.setCurrentFont(font))
        fontBox.setCurrentFont(QtGui.QFont('Microsoft YaHei'))
        # self.text.setCurrentFont('Microsoft YaHei')

        fontBox.setStyleSheet('QComboBox{border:1px solid gray;border-radius:8px;padding:1px18px1px3px;min-width:6em;}'
                              'QComboBox:editable {background: #2b2b2b;}'
                              'QComboBox:!editable,QComboBox::drop-down:editable {background: #333333;border-radius:8px}'
                              'QComboBox:!editable:on,QComboBox::drop-down:editable:on {background: #555555}'
                              'QComboBox:on {padding-top:3px;padding-left:4px;}'
                              'QComboBox::drop-down {subcontrol-origin: padding;subcontrol-position: top right;width:15px;'
                              'border-left-width:1px;border-left-color: darkgray;border-left-style: solid;/* just a single line */'
                              'border-top-right-radius:3px;border-bottom-right-radius:3px;}'
                              'QComboBox::down-arrow {image: url(D:/rig_manager_box/icon/writer_icon/arrowDown.png);}'
                              'QComboBox::down-arrow:on {top:1px;left:1px;}'
                              'QComboBox QAbstractItemView{border:1px solid darkgray;selection-background-color: lightgray;}'
                              'QScrollBar {border: 0px solid grey;background: #89d962;width: 8px;}'
                              'QScrollBar::handle {background: #89d962;min-height: 20px;border-radius:4px;}'
                              )

        fontSize = QtWidgets.QSpinBox(self)

        # Will display " pt" after each value
        fontSize.setSuffix(" pt")

        fontSize.valueChanged.connect(lambda size: self.text.setFontPointSize(size))

        fontSize.setValue(16)
        fontSize.setStyleSheet(
            'QSpinBox {padding-right: 12px;border-radius:8px;border:1px solid gray;}'
            'QSpinBox::up-button {subcontrol-origin: border;subcontrol-position: top right;width: 16px;border-width: 1px;}'
            'QSpinBox::up-button:hover {image: url(D:/rig_manager_box/icon/writer_icon/arrowUp_hover.png);}'
            'QSpinBox::up-button:pressed {background:lightgray;border-radius:3px}'
            'QSpinBox::up-arrow {image: url(D:/rig_manager_box/icon/writer_icon/arrowUp.png);width: 7px;height: 7px;}'
            'QSpinBox::up-arrow:disabled, QSpinBox::up-arrow:off {image: url(:/images/up_arrow_disabled.png);}'
            'QSpinBox::down-button {subcontrol-origin: border;subcontrol-position: bottom right;width: 16px;border-width: 1px;border-top-width: 0;}'
            'QSpinBox::down-button:hover {image: url(D:/rig_manager_box/icon/writer_icon/arrowDown_hover.png);}'
            'QSpinBox::down-button:pressed {background:lightgray;border-radius:3px}'
            'QSpinBox::down-arrow {image: url(D:/rig_manager_box/icon/writer_icon/arrowDown.png);width: 7px;height: 7px;}'
            'QSpinBox::down-arrow:disabled,QSpinBox::down-arrow:off {image: url(:/images/down_arrow_disabled.png);}')

        self.text.setCurrentCharFormat(dFormat)

        fontColor = QtWidgets.QAction(QtGui.QIcon(self.initPath + "font-color.png"), "Change font color", self)
        fontColor.triggered.connect(self.fontColorChanged)

        boldAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "bold.png"), "Bold", self)
        boldAction.triggered.connect(self.bold)

        italicAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "italic.png"), "Italic", self)
        italicAction.triggered.connect(self.italic)

        underlAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "underline.png"), "Underline", self)
        underlAction.triggered.connect(self.underline)

        strikeAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "strike.png"), "Strike-out", self)
        strikeAction.triggered.connect(self.strike)

        superAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "superscript.png"), "Superscript", self)
        superAction.triggered.connect(self.superScript)

        subAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "subscript.png"), "Subscript", self)
        subAction.triggered.connect(self.subScript)

        alignLeft = QtWidgets.QAction(QtGui.QIcon(self.initPath + "align-left.png"), "Align left", self)
        alignLeft.triggered.connect(self.alignLeft)

        alignCenter = QtWidgets.QAction(QtGui.QIcon(self.initPath + "align-center.png"), "Align center", self)
        alignCenter.triggered.connect(self.alignCenter)

        alignRight = QtWidgets.QAction(QtGui.QIcon(self.initPath + "align-right.png"), "Align right", self)
        alignRight.triggered.connect(self.alignRight)

        alignJustify = QtWidgets.QAction(QtGui.QIcon(self.initPath + "align-justify.png"), "Align justify", self)
        alignJustify.triggered.connect(self.alignJustify)

        indentAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "indent.png"), "Indent Area", self)
        indentAction.setShortcut("Ctrl+Tab")
        indentAction.triggered.connect(self.indent)

        dedentAction = QtWidgets.QAction(QtGui.QIcon(self.initPath + "dedent.png"), "Dedent Area", self)
        dedentAction.setShortcut("Shift+Tab")
        dedentAction.triggered.connect(self.dedent)

        backColor = QtWidgets.QAction(QtGui.QIcon(self.initPath + "highlight.png"), "Change background color", self)
        backColor.triggered.connect(self.highlight)

        self.formatbar = self.addToolBar("Format")

        self.formatbar.addWidget(fontBox)
        self.formatbar.addWidget(fontSize)

        self.formatbar.addSeparator()

        self.formatbar.addAction(fontColor)
        self.formatbar.addAction(backColor)

        self.formatbar.addSeparator()

        self.formatbar.addAction(boldAction)
        self.formatbar.addAction(italicAction)
        self.formatbar.addAction(underlAction)
        self.formatbar.addAction(strikeAction)
        self.formatbar.addAction(superAction)
        self.formatbar.addAction(subAction)

        self.formatbar.addSeparator()

        self.formatbar.addAction(alignLeft)
        self.formatbar.addAction(alignCenter)
        self.formatbar.addAction(alignRight)
        self.formatbar.addAction(alignJustify)

        self.formatbar.addSeparator()

        self.formatbar.addAction(indentAction)
        self.formatbar.addAction(dedentAction)

    def initMenubar(self):

        menubar = self.menuBar()

        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")

        # Add the most important actions to the menubar

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)
        file.addAction(self.saveasAction)
        file.addAction(self.cutImageAction)
        file.addAction(self.previewAction)
        file.addAction(self.closeAction)

        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)
        edit.addAction(self.findAction)

        # Toggling actions for the various bars
        toolbarAction = QtWidgets.QAction("Toggle Toolbar", self)
        toolbarAction.triggered.connect(self.toggleToolbar)

        formatbarAction = QtWidgets.QAction("Toggle Formatbar", self)
        formatbarAction.triggered.connect(self.toggleFormatbar)

        statusbarAction = QtWidgets.QAction("Toggle Statusbar", self)
        statusbarAction.triggered.connect(self.toggleStatusbar)

        view.addAction(toolbarAction)
        view.addAction(formatbarAction)
        view.addAction(statusbarAction)

    def initUI(self):

        self.text = FTextEdit()
        self.text.setParent(self)
        self.text.copySignal.connect(self.pasteFn)
        # Set the tab stop width to around 33 pixels which is
        # more or less 8 spaces
        self.text.setTabStopWidth(33)

        self.initToolbar()
        self.initFormatbar()
        self.initMenubar()

        self.setCentralWidget(self.text)

        # Initialize a statusbar for the window
        self.statusbar = self.statusBar()

        # If the cursor position changes, call the function that displays
        # the line and column number
        self.text.cursorPositionChanged.connect(self.cursorPosition)

        # We need our own context menu for tables
        self.text.setContextMenuPolicy(Qt.CustomContextMenu)
        self.text.customContextMenuRequested.connect(self.context)

        self.text.textChanged.connect(self.changed)

        self.setGeometry(0, 0, 0, 0)
        self.setWindowTitle("Writer")
        self.setWindowIcon(QtGui.QIcon(self.initPath + "icon.png"))

    def changed(self):
        self.changesSaved = False

    def closeEvent(self, event):

        if self.changesSaved:

            event.accept()

        else:

            popup = QtWidgets.QMessageBox(self)

            popup.setIcon(QtWidgets.QMessageBox.Warning)

            popup.setText("The document has been modified")

            popup.setInformativeText("Do you want to save your changes?")

            popup.setStandardButtons(QtWidgets.QMessageBox.Save |
                                     QtWidgets.QMessageBox.Cancel |
                                     QtWidgets.QMessageBox.Discard)

            popup.setDefaultButton(QtWidgets.QMessageBox.Save)

            answer = popup.exec_()

            if answer == QtWidgets.QMessageBox.Save:
                self.save()

            elif answer == QtWidgets.QMessageBox.Discard:
                event.accept()

            else:
                event.ignore()

    def pasteFn(self):
        self.clipboard = QtWidgets.QApplication.clipboard()
        MD = self.clipboard.mimeData()
        isPic = MD.hasImage()
        if isPic:
            tempPath = 'D:/Program Files/figo/QtDoc_picTemp/'
            if not os.path.exists(tempPath):
                os.makedirs(tempPath)

            data = self.clipboard.pixmap()
            image = data.toImage()
            # image = QtGui.QImage(filename)
            cursor = self.text.textCursor()
            ctime = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
            filename = tempPath + 'FigoCut' + ctime + '.png'
            cursor.insertImage(image, filename)
            data.save(filename)
        else:

            self.text.paste()  # wtf

    def context(self, pos):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table, if there is one
        table = cursor.currentTable()

        # Above will return 0 if there is no current table, in which case
        # we call the normal context menu. If there is a table, we create
        # our own context menu specific to table interaction
        if table:

            menu = QtWidgets.QMenu(self)

            appendRowAction = QtWidgets.QAction("Append row", self)
            appendRowAction.triggered.connect(lambda: table.appendRows(1))

            appendColAction = QtWidgets.QAction("Append column", self)
            appendColAction.triggered.connect(lambda: table.appendColumns(1))

            removeRowAction = QtWidgets.QAction("Remove row", self)
            removeRowAction.triggered.connect(self.removeRow)

            removeColAction = QtWidgets.QAction("Remove column", self)
            removeColAction.triggered.connect(self.removeCol)

            insertRowAction = QtWidgets.QAction("Insert row", self)
            insertRowAction.triggered.connect(self.insertRow)

            insertColAction = QtWidgets.QAction("Insert column", self)
            insertColAction.triggered.connect(self.insertCol)

            mergeAction = QtWidgets.QAction("Merge cells", self)
            mergeAction.triggered.connect(lambda: table.mergeCells(cursor))

            # Only allow merging if there is a selection
            if not cursor.hasSelection():
                mergeAction.setEnabled(False)

            splitAction = QtWidgets.QAction("Split cells", self)

            cell = table.cellAt(cursor)

            # Only allow splitting if the current cell is larger
            # than a normal cell
            if cell.rowSpan() > 1 or cell.columnSpan() > 1:

                splitAction.triggered.connect(lambda: table.splitCell(cell.row(), cell.column(), 1, 1))

            else:
                splitAction.setEnabled(False)

            menu.addAction(appendRowAction)
            menu.addAction(appendColAction)

            menu.addSeparator()

            menu.addAction(removeRowAction)
            menu.addAction(removeColAction)

            menu.addSeparator()

            menu.addAction(insertRowAction)
            menu.addAction(insertColAction)

            menu.addSeparator()

            menu.addAction(mergeAction)
            menu.addAction(splitAction)

            # Convert the widget coordinates into global coordinates
            pos = self.mapToGlobal(pos)

            # Add pixels for the tool and formatbars, which are not included
            # in mapToGlobal(), but only if the two are currently visible and
            # not toggled by the user

            if self.toolbar.isVisible():
                pos.setY(pos.y() + 45)

            if self.formatbar.isVisible():
                pos.setY(pos.y() + 45)

            # Move the menu to the new position
            menu.move(pos)

            menu.show()

        else:

            event = QtGui.QContextMenuEvent(QtGui.QContextMenuEvent.Mouse, QtCore.QPoint())

            self.text.contextMenuEvent(event)

    def removeRow(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Delete the cell's row
        table.removeRows(cell.row(), 1)

    def removeCol(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Delete the cell's column
        table.removeColumns(cell.column(), 1)

    def insertRow(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Insert a new row at the cell's position
        table.insertRows(cell.row(), 1)

    def insertCol(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        # Grab the current table (we assume there is one, since
        # this is checked before calling)
        table = cursor.currentTable()

        # Get the current cell
        cell = table.cellAt(cursor)

        # Insert a new row at the cell's position
        table.insertColumns(cell.column(), 1)

    def toggleToolbar(self):

        state = self.toolbar.isVisible()

        # Set the visibility to its inverse
        self.toolbar.setVisible(not state)

    def toggleFormatbar(self):

        state = self.formatbar.isVisible()

        # Set the visibility to its inverse
        self.formatbar.setVisible(not state)

    def toggleStatusbar(self):

        state = self.statusbar.isVisible()

        # Set the visibility to its inverse
        self.statusbar.setVisible(not state)

    def new(self):

        spawn = textEditorMain()

        spawn.show()

    def open(self):

        # Get filename and show only .writer files
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', ".", "(*.writer)")[0]

        if self.filename:
            with open(self.filename, "rt") as file:
                textInFile = file.read().decode('utf-8')
                self.text.setText(textInFile)

    def save(self):
        strTime = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        folderPath = str(self.savePath + '\\' + strTime)

        if not os.path.exists(folderPath):
            os.makedirs(folderPath)
        filePath = folderPath + '\\' + self.itemName + '_' + strTime + '_note.writer'

        # Before update,has update local picture to server-figo
        # print self.text.toHtml()
        newText = ''
        gg = self.text.toHtml().split('<img ')

        if len(gg) > 1:
            data = gg[1:]
            if data:
                newData = [gg[0]]
                for d in data:
                    dsp = d.split('"')
                    address = dsp[1]
                    dir = os.path.dirname(address) + '/'
                    name = os.path.basename(address)
                    sAddress = folderPath + '\\' + name
                    if sAddress == address:
                        print 'same and skip'
                        # print d
                        newData.append(d)
                    else:
                        shutil.copyfile(address, sAddress)
                        shutil.copystat(address, sAddress)
                        print 'file {} already copy to {}'.format(address, sAddress)
                        dsp[1] = sAddress
                        # print ('"'.join(dsp))
                        newData.append('"'.join(dsp))
                newText = '<img '.join(newData)
        else:
            newText = self.text.toHtml()

        # print newText
        encodeText = unicode(newText).encode('utf-8')
        # print encodeText
        # We just store the contents of the text file along with the
        # format in html, which Qt does in a very nice way for us

        with open(filePath, "wt") as file:
            file.write(encodeText)

        simpleInfo = self.text.toPlainText()

        encodeInfo = simpleInfo.encode('utf-8')
        infoPath = folderPath + '\\' + self.itemName + '_' + strTime + '_note.json'

        with open(infoPath, "wt") as file:
            file.write(encodeInfo)

        self.changesSaved = True
        self.saveSignal.emit([filePath])
        self.Cl_Ui()

    def saveas(self):

        # Only open dialog if there is no filename yet
        if not self.filename:
            self.filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save as')[0]

        if self.filename:

            # Append extension if not there yet
            if not str(self.filename).endswith(".writer"):
                self.filename += ".writer"

            newText = ''
            gg = self.text.toHtml().split('<img ')

            if len(gg) > 1:
                data = gg[1:]
                if data:
                    newData = [gg[0]]
                    for d in data:
                        dsp = d.split('"')
                        address = dsp[1]
                        dir = os.path.dirname(address) + '/'
                        name = os.path.basename(address)
                        sAddress = folderPath + '\\' + name
                        if sAddress == address:
                            print 'same and skip'
                            # print d
                            newData.append(d)
                        else:
                            shutil.copyfiles(address, sAddress)
                            shutil.copystat(address, sAddress)
                            print 'file {} already copy to {}'.format(address, sAddress)
                            dsp[1] = sAddress
                            # print ('"'.join(dsp))
                            newData.append('"'.join(dsp))
                    newText = '<img '.join(newData)
            else:
                newText = self.text.toHtml()

            # We just store the contents of the text file along with the
            # format in html, which Qt does in a very nice way for us
            with open(self.filename, "wt") as file:
                file.write(newText)

            self.changesSaved = True
            self.saveSignal.emit(self.filename)

    def preview(self):

        # Open preview dialog
        preview = QtWidgets.QPrintPreviewDialog()

        # If a print is requested, open print dialog
        preview.paintRequested.connect(lambda p: self.text.print_(p))

        preview.exec_()

    def cutImage(self):
        notRun = True
        runPath = (getAssetManagerPath()['main'] + '\\maya2017\\bin\\PrScrn.dll')
        if os.path.exists(runPath):
            subprocess.call(r'rundll32.exe ' + runPath + ' PrScrn')
            notRun = False
        if notRun:
            print 'no right path install or function missing'

    def cursorPosition(self):

        cursor = self.text.textCursor()

        # Mortals like 1-indexed things
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()

        self.statusbar.showMessage("wrote for {} | Line: {} | Column: {}".format(self.itemName, line, col))

    def wordCount(self):

        wc = docWritter_WordCount(self)

        wc.getText()

        wc.show()
        # 3014897692

    def insertImage(self):

        # Get image file name
        filename = \
        QtWidgets.QFileDialog.getOpenFileName(self, 'Insert image', ".", "Images (*.png *.xpm *.jpg *.bmp *.gif)")[0]
        print filename
        if filename:

            # Create image object
            image = QtGui.QImage(filename)

            # Error if unloadable
            if image.isNull():

                popup = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical,
                                          "Image load error",
                                          "Could not load image file!",
                                          QtWidgets.QMessageBox.Ok,
                                          self)
                popup.show()

            else:

                cursor = self.text.textCursor()

                cursor.insertImage(image, filename)

    def fontColorChanged(self):

        # Get a color from the text dialog
        color = QtWidgets.QColorDialog.getColor()

        # Set it as the new text color
        self.text.setTextColor(color)

    def highlight(self):

        color = QtWidgets.QColorDialog.getColor()

        self.text.setTextBackgroundColor(color)

    def bold(self):

        if self.text.fontWeight() == QtGui.QFont.Bold:

            self.text.setFontWeight(QtGui.QFont.Normal)

        else:

            self.text.setFontWeight(QtGui.QFont.Bold)

    def italic(self):

        state = self.text.fontItalic()

        self.text.setFontItalic(not state)

    def underline(self):

        state = self.text.fontUnderline()

        self.text.setFontUnderline(not state)

    def strike(self):

        # Grab the text's format
        fmt = self.text.currentCharFormat()

        # Set the fontStrikeOut property to its opposite
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())

        # And set the next char format
        self.text.setCurrentCharFormat(fmt)

    def superScript(self):

        # Grab the current format
        fmt = self.text.currentCharFormat()

        # And get the vertical alignment property
        align = fmt.verticalAlignment()

        # Toggle the state
        if align == QtGui.QTextCharFormat.AlignNormal:

            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)

        else:

            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

        # Set the new format
        self.text.setCurrentCharFormat(fmt)

    def subScript(self):

        # Grab the current format
        fmt = self.text.currentCharFormat()

        # And get the vertical alignment property
        align = fmt.verticalAlignment()

        # Toggle the state
        if align == QtGui.QTextCharFormat.AlignNormal:

            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)

        else:

            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)

        # Set the new format
        self.text.setCurrentCharFormat(fmt)

    def alignLeft(self):
        self.text.setAlignment(Qt.AlignLeft)

    def alignRight(self):
        self.text.setAlignment(Qt.AlignRight)

    def alignCenter(self):
        self.text.setAlignment(Qt.AlignCenter)

    def alignJustify(self):
        self.text.setAlignment(Qt.AlignJustify)

    def indent(self):

        # Grab the cursor
        cursor = self.text.textCursor()

        if cursor.hasSelection():

            # Store the current line/block number
            temp = cursor.blockNumber()

            # Move to the selection's end
            cursor.setPosition(cursor.anchor())

            # Calculate range of selection
            diff = cursor.blockNumber() - temp

            direction = QtGui.QTextCursor.Up if diff > 0 else QtGui.QTextCursor.Down

            # Iterate over lines (diff absolute value)
            for n in range(abs(diff) + 1):
                # Move to start of each line
                cursor.movePosition(QtGui.QTextCursor.StartOfLine)

                # Insert tabbing
                cursor.insertText("\t")

                # And move back up
                cursor.movePosition(direction)

        # If there is no selection, just insert a tab
        else:

            cursor.insertText("\t")

    def handleDedent(self, cursor):

        cursor.movePosition(QtGui.QTextCursor.StartOfLine)

        # Grab the current line
        line = cursor.block().text()

        # If the line starts with a tab character, delete it
        if line.startswith("\t"):

            # Delete next character
            cursor.deleteChar()

        # Otherwise, delete all spaces until a non-space character is met
        else:
            for char in line[:8]:

                if char != " ":
                    break

                cursor.deleteChar()

    def dedent(self):

        cursor = self.text.textCursor()

        if cursor.hasSelection():

            # Store the current line/block number
            temp = cursor.blockNumber()

            # Move to the selection's last line
            cursor.setPosition(cursor.anchor())

            # Calculate range of selection
            diff = cursor.blockNumber() - temp

            direction = QtGui.QTextCursor.Up if diff > 0 else QtGui.QTextCursor.Down

            # Iterate over lines
            for n in range(abs(diff) + 1):
                self.handleDedent(cursor)

                # Move up
                cursor.movePosition(direction)

        else:
            self.handleDedent(cursor)

    def bulletList(self):

        cursor = self.text.textCursor()

        # Insert bulleted list
        cursor.insertList(QtGui.QTextListFormat.ListDisc)

    def numberList(self):

        cursor = self.text.textCursor()

        # Insert list with numbers
        cursor.insertList(QtGui.QTextListFormat.ListDecimal)

    def Cl_Ui(self):
        self.close()
        self.deleteLater()



#TEmain = assetManager_writterUI()
#TEmain.resize(500,500)
#TEmain.show()
#TEmain.Cl_Ui()