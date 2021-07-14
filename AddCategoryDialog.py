from PySide6 import QtWidgets

class AddCategoryDialog(QtWidgets.QDialog):
    def __init__(self, appData, appDataChanged):
        super().__init__()
        self.appData = appData
        self.appDataChanged = appDataChanged
        self.resize(600, 400)
        self.setWindowTitle("Add Category")
        layout = QtWidgets.QVBoxLayout()

        self.nameInput = QtWidgets.QLineEdit()
        self.colorInput = QtWidgets.QLineEdit()

        self.nameInput.setPlaceholderText("Category Name")
        self.colorInput.setPlaceholderText("Color (#hexcode)")

        createButton = QtWidgets.QPushButton("add category", self)
        createButton.clicked.connect(self.add_category_button_clicked)

        layout.addWidget(self.nameInput)
        layout.addWidget(self.colorInput)
        layout.addWidget(createButton)

        self.setLayout(layout)

    def add_category_button_clicked(self):
        name = self.nameInput.text()
        color = self.colorInput.text()
        # check that color is valid
        if not len(color) == 7 or not color[0] == "#":
            # TODO show an error
            print("error when making category color")
            return
        for c in color[1:]:
            if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]:
                # TODO show an error
                print("error when making category color")
                return
        # create the category
        self.appData[0].add_category(name, color)
        self.appDataChanged()
        self.close()
