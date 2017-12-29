import sys
from PyQt4 import QtGui


def hello():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    b = QtGui.QLabel(w)
    b.setText("Hello World!")
    w.setGeometry(100, 100, 200, 50)
    b.move(50, 20)
    w.setWindowTitle('PyQt')
    w.show()
    sys.exit(app.exec_())