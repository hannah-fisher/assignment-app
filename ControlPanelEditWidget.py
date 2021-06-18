from PySide6 import QtWidgets

from Serializer import Serializer
from Style import Style

class ControlPanelEditWidget(QtWidgets.QWidget):
    def __init__(self, appData, appDataChanged):
        super().__init__()
        self.appData = appData
        self.appDataChanged = appDataChanged
        layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel(self)
        label.setText("control panel edit widget")
        loadFromFileButton = QtWidgets.QPushButton("load from file", self)
        loadFromFileButton.clicked.connect(self.load_from_file_button_clicked)
        layout.addWidget(label)
        layout.addWidget(loadFromFileButton)
        self.setLayout(layout)
        Style.backgroundColorWidget(self, Style.ControlPanelEditWidgetColor)

    def load_from_file_button_clicked(self):
        filename, other = QtWidgets.QFileDialog.getOpenFileName(self, "Load App Data", "/home/", "*.json")
        self.appData[0] = Serializer.deserialize(filename)
        self.appDataChanged()
