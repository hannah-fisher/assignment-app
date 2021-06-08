from PySide6 import QtWidgets

from Style import Style

class ControlPanelEditWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        label = QtWidgets.QLabel(self)
        label.setText("control panel edit widget")
        Style.backgroundColorWidget(self, "yellow")
