import datetime
import uuid

from PySide6 import QtWidgets
from AssignmentAppData import Priority


class AddAssignmentDialog(QtWidgets.QDialog):
    def __init__(self, appData, appDataChanged):
        super().__init__()
        self.appData = appData
        self.appDataChanged = appDataChanged
        self.resize(600, 400)
        self.setWindowTitle("Add Assignment")
        layout = QtWidgets.QVBoxLayout()

        self.categoryInput = QtWidgets.QComboBox()
        self.titleInput = QtWidgets.QLineEdit()
        self.dueDateInput = QtWidgets.QLineEdit()
        self.notesInput = QtWidgets.QLineEdit()
        self.priorityInput = QtWidgets.QComboBox()

        for categoryName in appData[0].get_category_names():
            self.categoryInput.addItem(categoryName)
        self.titleInput.setPlaceholderText("Title")
        self.dueDateInput.setPlaceholderText("Due Date (dd mm yyyy hh)")
        self.notesInput.setPlaceholderText("Notes")
        for n in ["none", "low", "medium", "high"]:
            self.priorityInput.addItem(n)

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
        category = self.categoryInput.currentText()
        title = self.titleInput.text()
        dueDate = self.dueDateInput.text()
        notes = self.notesInput.text()
        priority = self.priorityInput.currentText()
        # check that due date input is valid
        try:
            dueDateParts = dueDate.split(" ")
            dueDate = datetime.datetime(int(dueDateParts[2]),
                                        int(dueDateParts[1]),
                                        int(dueDateParts[0]),
                                        hour=int(dueDateParts[3]))
        except ValueError as e:
            # TODO show the error
            print("error when making due date")
            return
        # create the assignment
        self.appData[0].add_assignment(category, str(uuid.uuid1()), title,
                                       dueDate, notes,
                                       Priority[priority].value)
        self.appDataChanged()
        self.close()
