# you should install PySide :-)
# command line: pip install pyside

from PySide import QtCore, QtGui

class MyDialog(QtGui.QDialog):

  __uiElements = None

  def __init__(self):

    super(MyDialog, self).__init__()

    self.setWindowTitle('My very own dialog!')
    self.resize(300, 100)

    # create a layout for the UI
    layout = QtGui.QGridLayout()
    self.setLayout(layout)

    # create a bunch of ui elements
    self.__uiElements = {}
    self.__uiElements['checker'] = QtGui.QCheckBox(self)
    self.__uiElements['text'] = QtGui.QLineEdit(self)
    self.__uiElements['slider'] = QtGui.QSlider(self)
    self.__uiElements['slider'].setOrientation(QtCore.Qt.Horizontal)

    # add them to the layout, and add labels
    layout.addWidget(QtGui.QLabel('A checkbox', self), 0, 0)
    layout.addWidget(self.__uiElements['checker'], 0, 1)
    layout.addWidget(QtGui.QLabel('Some text', self), 1, 0)
    layout.addWidget(self.__uiElements['text'], 1, 1)
    layout.addWidget(QtGui.QLabel('A slider', self), 2, 0)
    layout.addWidget(self.__uiElements['slider'], 2, 1)

    # also add a bunch of buttons
    buttonBox = QtGui.QDialogButtonBox(self)
    buttonBox.addButton(QtGui.QDialogButtonBox.Cancel)
    buttonBox.addButton(QtGui.QDialogButtonBox.Ok)

    # add the buttons to the layout
    layout.addWidget(buttonBox, 3, 1)

    # also connect the buttons!
    buttonBox.accepted.connect(self.accept)
    buttonBox.rejected.connect(self.reject)

  def getChecker(self):
    return self.__uiElements['checker'].checkState() == QtCore.Qt.CheckState.Checked

  def getText(self):
    return self.__uiElements['text'].text()

  def getSlider(self):
    return self.__uiElements['slider'].value()


# you always need to have an app first
app = QtGui.QApplication([])

# create the dialog and show it modally
dlg = MyDialog()
result = dlg.exec_()
if not result:
  exit()

print dlg.getChecker()
print dlg.getText()
print dlg.getSlider()
