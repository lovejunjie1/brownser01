from Qt import QtWidgets as qw,QtGui,QtCore

class docWritter_Table(qw.QDialog):
    def __init__(self,parent = None):
        qw.QDialog.__init__(self, parent)

        self.parent = parent
         
        self.initUI()
 
    def initUI(self):

        # Rows
        rowsLabel = qw.QLabel("Rows: ",self)
        
        self.rows = qw.QSpinBox(self)

        # Columns
        colsLabel = qw.QLabel("Columns",self)
        
        self.cols = qw.QSpinBox(self)

        # Cell spacing (distance between cells)
        spaceLabel = qw.QLabel("Cell spacing",self)
        
        self.space = qw.QSpinBox(self)

        # Cell padding (distance between cell and inner text)
        padLabel = qw.QLabel("Cell padding",self)

        self.pad = qw.QSpinBox(self)
        
        self.pad.setValue(10)

        # Button
        insertButton = qw.QPushButton("Insert",self)
        insertButton.clicked.connect(self.insert)

        # Layout
        layout = qw.QGridLayout()

        layout.addWidget(rowsLabel,0,0)
        layout.addWidget(self.rows,0,1)

        layout.addWidget(colsLabel,1,0)
        layout.addWidget(self.cols,1,1)

        layout.addWidget(padLabel,2,0)
        layout.addWidget(self.pad,2,1)
        
        layout.addWidget(spaceLabel,3,0)
        layout.addWidget(self.space,3,1)

        layout.addWidget(insertButton,4,0,1,2)

        self.setWindowTitle("Insert Table")
        self.setGeometry(300,300,200,100)
        self.setLayout(layout)

    def insert(self):

        cursor = self.parent.text.textCursor()

        # Get the configurations
        rows = self.rows.value()

        cols = self.cols.value()

        if not rows or not cols:

            popup = qw.QMessageBox(qw.QMessageBox.Warning,
                                      "Parameter error",
                                      "Row and column numbers may not be zero!",
                                      qw.QMessageBox.Ok,
                                      self)
            popup.show()

        else:

            padding = self.pad.value()

            space = self.space.value()

            # Set the padding and spacing
            fmt = qw.QTextTableFormat()
            
            fmt.setCellPadding(padding)

            fmt.setCellSpacing(space)

            # Inser the new table
            cursor.insertTable(rows,cols,fmt)

            self.close()
