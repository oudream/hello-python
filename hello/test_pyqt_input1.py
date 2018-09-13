
import sys
from PyQt4 import QtGui

def showQuery():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    bOk = False
    sVaule = ''
    sText = QtGui.QInputDialog.getText(w, "输入框",
                                        '提示', QtGui.QLineEdit.Normal,
                                         sVaule)
    print(sVaule)
    print(sText)
