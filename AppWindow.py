from PySide6 import QtWidgets

from Style import Style

from AssignmentAppData import AssignmentAppData
from ControlPanelWidget import ControlPanelWidget
from DisplayAreaWidget import DisplayAreaWidget
from UpcomingWidget import UpcomingWidget

class AppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.appData = [AssignmentAppData()]
        self.resize(800, 600)
        self.setWindowTitle("Assignment App")
        layout = QtWidgets.QHBoxLayout()
        self.controlPanelWidget = ControlPanelWidget(self.appData, self.appDataChanged)
        self.displayAreaWidget = DisplayAreaWidget(self.appData)
        self.upcomingWidget = UpcomingWidget()
        layout.addWidget(self.controlPanelWidget)
        layout.addWidget(self.displayAreaWidget)
        layout.addWidget(self.upcomingWidget)
        layout.setStretch(0, 1)
        layout.setStretch(1, 3)
        layout.setStretch(2, 1)
        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        Style.backgroundColorWidget(self, Style.AppWindowColor)

    def appDataChanged(self):
        # call this whenever appdata changes
        # update gui
        self.displayAreaWidget.reload_display()
