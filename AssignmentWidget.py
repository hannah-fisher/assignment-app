from PySide6 import QtWidgets

from Style import Style

from AssignmentDialog import AssignmentDialog

class AssignmentWidget(QtWidgets.QWidget):
    def __init__(self, assignment, complete_assignment_func, reload_display_func):
        super().__init__()
        self.assignment = assignment
        self.complete_assignment_func = complete_assignment_func
        self.reload_display_func = reload_display_func
        self.label = QtWidgets.QLabel(self)
        self.set_label_text()
        self.setStyleSheet("""
            QLabel::hover {
                background-color: red;
            }
        """)
        self.setFixedHeight(40) # should do this as fraction of window height

    def set_label_text(self):
        assignment = self.assignment
        text = ""
        text += "!" * assignment.priority
        if text != "":
            text += " "
        text += assignment.title
        text += " due "
        text += str(assignment.due_date.month) + "/" + str(assignment.due_date.day)
        text += " at " + str(assignment.due_date.hour % 12)
        text += " am" if assignment.due_date.hour < 12 else " pm"
        if assignment.notes != "":
            text += " ..."
        self.label.setText(text)

    def mousePressEvent(self, event):
        dialog = AssignmentDialog(self.assignment, self.complete_assignment_func, self.reload_display_func)
        dialog.exec()
