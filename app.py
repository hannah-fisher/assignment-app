from PySide6 import QtCore, QtWidgets, QtGui

from AppWindow import AppWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    appWindow = AppWindow()
    appWindow.show()
    app.exec_()
