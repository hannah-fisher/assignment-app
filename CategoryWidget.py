from PySide6 import QtWidgets

from Style import Style

from AssignmentWidget import AssignmentWidget

class CategoryWidget(QtWidgets.QWidget):
    def __init__(self, name, color):
        super().__init__()
        label = QtWidgets.QLabel(self)
        label.setText(name)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(label)
        self.setLayout(self.layout)
        Style.backgroundColorWidget(self, color)

    def add_assignment(self, assignment):
        assignmentWidget = AssignmentWidget(assignment)
        self.layout.addWidget(assignmentWidget)
