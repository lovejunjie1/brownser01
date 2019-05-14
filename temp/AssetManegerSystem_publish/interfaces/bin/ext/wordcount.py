from Qt import QtWidgets as qw,QtGui,QtCore

class docWritter_WordCount(qw.QDialog):
    def __init__(self,parent = None):
        qw.QDialog.__init__(self, parent)

        self.parent = parent
         
        self.initUI()
 
    def initUI(self):

        # Word count in selection
        currentLabel = qw.QLabel("Current selection",self)
        currentLabel.setStyleSheet("font-weight:bold; font-size: 15px;")

        currentWordsLabel = qw.QLabel("Words: ", self)
        currentSymbolsLabel = qw.QLabel("Symbols: ",self)
        
        self.currentWords = qw.QLabel(self)
        self.currentSymbols = qw.QLabel(self)

        # Total word/symbol count
        totalLabel = qw.QLabel("Total",self)
        totalLabel.setStyleSheet("font-weight:bold; font-size: 15px;")

        totalWordsLabel = qw.QLabel("Words: ", self)
        totalSymbolsLabel = qw.QLabel("Symbols: ",self)

        self.totalWords = qw.QLabel(self)
        self.totalSymbols = qw.QLabel(self)

        # Layout
        
        layout = qw.QGridLayout(self)

        layout.addWidget(currentLabel,0,0)
        
        layout.addWidget(currentWordsLabel,1,0)
        layout.addWidget(self.currentWords,1,1)

        layout.addWidget(currentSymbolsLabel,2,0)
        layout.addWidget(self.currentSymbols,2,1)

        spacer = qw.QWidget()
        spacer.setFixedSize(0,5)

        layout.addWidget(spacer,3,0)

        layout.addWidget(totalLabel,4,0)

        layout.addWidget(totalWordsLabel,5,0)
        layout.addWidget(self.totalWords,5,1)

        layout.addWidget(totalSymbolsLabel,6,0)
        layout.addWidget(self.totalSymbols,6,1)

        self.setWindowTitle("Word count")
        self.setGeometry(300,300,200,200)
        self.setLayout(layout)

    def getText(self):

        # Get the text currently in selection
        text = self.parent.text.textCursor().selectedText()

        # Split the text to get the word count
        words = str(len(text.split()))

        # And just get the length of the text for the symbols
        # count
        symbols = str(len(text))

        self.currentWords.setText(words)
        self.currentSymbols.setText(symbols)

        # For the total count, same thing as above but for the
        # total text
        
        text = self.parent.text.toPlainText()

        words = str(len(text.split()))
        symbols = str(len(text))

        self.totalWords.setText(words)
        self.totalSymbols.setText(symbols)
