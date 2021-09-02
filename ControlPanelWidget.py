from PySide6 import QtWidgets

from ControlPanelEditWidget import ControlPanelEditWidget
from ControlPanelViewWidget import ControlPanelViewWidget
from Style import Style


class ControlPanelWidget(QtWidgets.QWidget):
    def __init__(self, appData, appDataChanged):
        super().__init__()
        Style.backgroundColorWidget(self, Style.ControlPanelWidgetColor)
        title = QtWidgets.QLabel(self)
        title.setText("Control Panel")
        self.controlPanelEditWidget = ControlPanelEditWidget(
            appData, appDataChanged)
        self.controlPanelViewWidget = ControlPanelViewWidget()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(self.controlPanelEditWidget)
        layout.addWidget(self.controlPanelViewWidget)
        layout.setStretch(0, 1)
        layout.setStretch(1, 5)
        layout.setStretch(2, 5)
        self.setLayout(layout)

    def recolor(self):
        Style.backgroundColorWidget(self, Style.ControlPanelWidgetColor)
        self.controlPanelEditWidget.recolor()
        self.controlPanelViewWidget.recolor()
