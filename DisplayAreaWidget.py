from PySide6 import QtWidgets

from Style import Style

class DisplayAreaWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        label = QtWidgets.QLabel(self)
        label.setText("display area widget")
        Style.backgroundColorWidget(self, "red")
