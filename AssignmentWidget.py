from PySide6 import QtWidgets

from Style import Style

class AssignmentWidget(QtWidgets.QWidget):
    def __init__(self, assignment):
        super().__init__()
        self.assignment = assignment
        label = QtWidgets.QLabel(self)
        label.setText(assignment.title + ", " + str(assignment.due_date))
        # TODO a much better display
