from PySide6 import QtWidgets
from PySide6.QtCore import Qt

from Style import Style

from AssignmentWidget import AssignmentWidget

class CategoryWidget(QtWidgets.QWidget):
    def __init__(self, name, color):
        super().__init__()
        label = QtWidgets.QLabel(self)
        label.setText(name)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(label)

        self.scroll = QtWidgets.QScrollArea()
        self.widget = QtWidgets.QWidget()
        self.vbox = QtWidgets.QVBoxLayout()
        self.widget.setLayout(self.vbox)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.layout.addWidget(self.scroll)
        self.setLayout(self.layout)

        Style.backgroundColorWidget(self, color)

    def add_assignment(self, assignment):
        assignmentWidget = AssignmentWidget(assignment)
        self.vbox.addWidget(assignmentWidget)
