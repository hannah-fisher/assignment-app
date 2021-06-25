from PySide6 import QtWidgets

class AssignmentDialog(QtWidgets.QDialog):
    def __init__(self, assignment, complete_assignment_func, reload_display_func):
        super().__init__()
        self.assignment = assignment
        self.complete_assignment_func = complete_assignment_func
        self.reload_display_func = reload_display_func
        self.setWindowTitle(assignment.title)
        layout = QtWidgets.QVBoxLayout()

        titleLabel = QtWidgets.QLabel(self)
        titleLabel.setText(assignment.title)
        priorityLabel = QtWidgets.QLabel(self)
        priorityLabel.setText("Priority: " + "!" * assignment.priority)
        dueLabel = QtWidgets.QLabel(self)
        dueLabel.setText("Due: " + str(assignment.due_date))
        notesLabel = QtWidgets.QLabel(self)
        notesLabel.setText("Notes: " + assignment.notes)
        completedButton = QtWidgets.QPushButton("mark as complete", self)
        completedButton.clicked.connect(self.completedButtonClicked)

        layout.addWidget(titleLabel)
        layout.addWidget(priorityLabel)
        layout.addWidget(dueLabel)
        layout.addWidget(notesLabel)
        layout.addWidget(completedButton)
        self.setLayout(layout)

    def completedButtonClicked(self):
        self.complete_assignment_func(self.assignment)
        self.reload_display_func()
