# you should install PySide :-)
# command line: pip install pyside

from PySide import QtCore, QtGui

class MyMainWindow(QtGui.QMainWindow):

  __textEdit = None

  def __init__(self):

    super(MyMainWindow, self).__init__()

    self.setWindowTitle('My own text editor!')
    self.resize(600, 300)

    # create the widget to edit
    self.__textEdit = QtGui.QPlainTextEdit(self)
    self.setCentralWidget(self.__textEdit)

    # create some menus!
    menuBar = QtGui.QMenuBar()
    self.setMenuBar(menuBar)

    fileMenu = menuBar.addMenu('File')
    newAction = fileMenu.addAction('New')
    openAction = fileMenu.addAction('Open')
    saveAction = fileMenu.addAction('Save')
    fileMenu.addSeparator()
    quitAction = fileMenu.addAction('Quit')

    # set some standard shortcuts!
    newAction.setShortcuts(QtGui.QKeySequence.New)
    openAction.setShortcuts(QtGui.QKeySequence.Open)
    saveAction.setShortcuts(QtGui.QKeySequence.Save)

    # connect the menu actions to methods of this class!
    newAction.triggered.connect(self.onNewFile)
    openAction.triggered.connect(self.onOpenFile)
    saveAction.triggered.connect(self.onSaveFile)
    quitAction.triggered.connect(self.close)

  def showEvent(self, event):
    print 'We are about to show - let us load a config?'

  def closeEvent(self, event):
    print 'We are closing, we could save a config file here!'

  def onNewFile(self):
    self.__textEdit.setPlainText("")

  def onOpenFile(self):
    filePath = QtGui.QFileDialog.getOpenFileName(self, 'Pick a file', '', '*.txt')
    if filePath:
      text = open(filePath[0], 'r').read()
      self.__textEdit.setPlainText(text)

  def onSaveFile(self):
    filePath = QtGui.QFileDialog.getSaveFileName(self, 'Pick a file', '', '*.txt')
    if filePath:
      text = self.getText()
      open(filePath[0], 'w').write(text)

  def getText(self):
    return self.__textEdit.toPlainText()

# you always need to have an app first
app = QtGui.QApplication([])

# create the dialog and show it modally
window = MyMainWindow()
window.show()
app.exec_()
