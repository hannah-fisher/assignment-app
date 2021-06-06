from PySide6 import QtWidgets

from Style import Style

class UpcomingWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        label = QtWidgets.QLabel(self)
        label.setText("upcoming widget")
        Style.backgroundColorWidget(self, "blue")
