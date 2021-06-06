from PySide6 import QtCore

class Style:
    def __init__():
        pass

    @classmethod
    def backgroundColorWidget(cls, widget, color):
        widget.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        widget.setStyleSheet('background-color: {}'.format(color))
