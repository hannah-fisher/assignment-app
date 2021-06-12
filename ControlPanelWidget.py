from PySide6 import QtWidgets

from ControlPanelEditWidget import ControlPanelEditWidget
from ControlPanelViewWidget import ControlPanelViewWidget
from Style import Style

class ControlPanelWidget(QtWidgets.QWidget):
    def __init__(self, appData):
        super().__init__()
        Style.backgroundColorWidget(self, "green")
        title = QtWidgets.QLabel(self)
        title.setText("Control Panel")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(ControlPanelEditWidget(appData))
        layout.addWidget(ControlPanelViewWidget())
        layout.setStretch(0, 1)
        layout.setStretch(1, 5)
        layout.setStretch(2, 5)
        self.setLayout(layout)
