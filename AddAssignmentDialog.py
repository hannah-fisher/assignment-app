import datetime
import uuid

from PySide6 import QtWidgets

class AddAssignmentDialog(QtWidgets.QDialog):
    def __init__(self, appData, appDataChanged):
        super().__init__()
        self.appData = appData
        self.appDataChanged = appDataChanged
        self.resize(600, 400)
        self.setWindowTitle("Add Assignment")
        layout = QtWidgets.QVBoxLayout()

        self.categoryInput = QtWidgets.QLineEdit()
        self.titleInput = QtWidgets.QLineEdit()
        self.dueDateInput = QtWidgets.QLineEdit()
        self.notesInput = QtWidgets.QLineEdit()
        self.priorityInput = QtWidgets.QLineEdit()

        self.categoryInput.setPlaceholderText("Category Name")
        self.titleInput.setPlaceholderText("Title")
        self.dueDateInput.setPlaceholderText("Due Date (dd mm yyyy hh)")
        self.notesInput.setPlaceholderText("Notes")
        self.priorityInput.setPlaceholderText("Priority (1/2/3/4)")

        createButton = QtWidgets.QPushButton("add assignment", self)
        createButton.clicked.connect(self.add_assignment_button_clicked)

        layout.addWidget(self.categoryInput)
        layout.addWidget(self.titleInput)
        layout.addWidget(self.dueDateInput)
        layout.addWidget(self.notesInput)
        layout.addWidget(self.priorityInput)
        layout.addWidget(createButton)

        self.setLayout(layout)

    def add_assignment_button_clicked(self):
        category = self.categoryInput.text()
        title = self.titleInput.text()
        dueDate = self.dueDateInput.text()
        notes = self.notesInput.text()
        priority = self.priorityInput.text()
        # check that due date input is valid
        try:
            dueDateParts = dueDate.split(" ")
            dueDate = datetime.datetime(int(dueDateParts[2]), int(dueDateParts[1]), int(dueDateParts[0]), hour=int(dueDateParts[3]))
        except ValueError as e:
            # TODO show the error
            print("error when making due date")
            return
        # check that priority input is valid
        try:
            priority = int(priority)
            assert priority >= 0
            assert priority < 4
        except (ValueError, AssertionError) as e:
            # TODO show the error
            print("error when making priority")
            return
        # create the assignment
        self.appData[0].add_assignment(category, str(uuid.uuid1()), title, dueDate, notes, priority)
        self.appDataChanged()
        self.close()
