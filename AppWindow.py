from PySide6 import QtGui, QtWidgets

from Serializer import Serializer
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

        fileMenu = self.menuBar().addMenu("File")
        editMenu = self.menuBar().addMenu("Edit")
        viewMenu = self.menuBar().addMenu("View")
        preferencesMenu = self.menuBar().addMenu("Preferences")
        helpMenu = self.menuBar().addMenu("Help")

        saveAction = QtGui.QAction("Save as", self)
        saveAction.triggered.connect(self.save_action)
        loadAction = QtGui.QAction("Load from file", self)
        loadAction.triggered.connect(self.load_action)
        clearAction = QtGui.QAction("Clear all data", self)
        clearAction.triggered.connect(self.clear_action)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(loadAction)
        fileMenu.addAction(clearAction)

        layout = QtWidgets.QHBoxLayout()
        self.controlPanelWidget = ControlPanelWidget(self.appData, self.appDataChanged)
        self.displayAreaWidget = DisplayAreaWidget(self.appData, self.appDataChanged)
        self.upcomingWidget = UpcomingWidget(self.appData)
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
        if self.appData[0] is not None:
            self.displayAreaWidget.reload_display()
            self.upcomingWidget.reload_display()

    def save_action(self):
        filename, other = QtWidgets.QFileDialog.getSaveFileName(self, "Save App Data", "/home/", "*.json")
        Serializer.serialize(filename, self.appData[0])

    def load_action(self):
        filename, other = QtWidgets.QFileDialog.getOpenFileName(self, "Load App Data", "/home/", "*.json")
        self.appData[0] = Serializer.deserialize(filename)
        self.appDataChanged()

    def clear_action(self):
        self.appData[0].clear_all_data()
        self.appDataChanged()
