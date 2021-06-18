from PySide6 import QtWidgets

from Style import Style

class ControlPanelViewWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        label = QtWidgets.QLabel(self)
        label.setText("control panel view widget")
        Style.backgroundColorWidget(self, Style.ControlPanelViewWidgetColor)
