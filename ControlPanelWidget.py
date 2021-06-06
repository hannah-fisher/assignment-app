from PySide6 import QtWidgets

from Style import Style

class ControlPanelWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        label = QtWidgets.QLabel(self)
        label.setText("control panel widget")
        Style.backgroundColorWidget(self, "green")
