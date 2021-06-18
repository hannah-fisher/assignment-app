from PySide6 import QtWidgets

from math import ceil, floor, sqrt
from Style import Style

from CategoryWidget import CategoryWidget

class DisplayAreaWidget(QtWidgets.QWidget):
    def __init__(self, appData):
        super().__init__()
        self.appData = appData
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        Style.backgroundColorWidget(self, "red")

    def reload_display(self):
        appData = self.appData[0]
        category_count = len(appData.categories)
        column_count = ceil(sqrt(category_count))
        row_count = ceil(category_count / column_count)
        added_category_count = 0
        for category in appData.categories:
            column = floor(added_category_count / column_count)
            row = added_category_count - (column * column_count)
            categoryWidget = CategoryWidget(category.name, category.color)
            for assignment in category.assignments:
                categoryWidget.add_assignment(assignment)
            self.layout.addWidget(categoryWidget, row, column)
            added_category_count += 1
