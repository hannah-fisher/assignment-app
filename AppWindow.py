from PySide6 import QtWidgets

from ControlPanelWidget import ControlPanelWidget
from DisplayAreaWidget import DisplayAreaWidget
from UpcomingWidget import UpcomingWidget

class AppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle("Assignment App")
        layout = QtWidgets.QHBoxLayout()
        controlPanelWidget = ControlPanelWidget()
        displayAreaWidget = DisplayAreaWidget()
        upcomingWidget = UpcomingWidget()
        layout.addWidget(controlPanelWidget)
        layout.addWidget(displayAreaWidget)
        layout.addWidget(upcomingWidget)
        layout.setStretch(0, 1)
        layout.setStretch(1, 3)
        layout.setStretch(2, 1)
        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)