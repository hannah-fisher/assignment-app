from PySide6 import QtWidgets

from math import ceil, floor, sqrt
from Style import Style

from CategoryWidget import CategoryWidget

class DisplayAreaWidget(QtWidgets.QWidget):
    def __init__(self, appData, appDataChanged):
        super().__init__()
        self.appData = appData
        self.appDataChanged = appDataChanged
        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)
        Style.backgroundColorWidget(self, Style.DisplayAreaWidgetColor)

    def reload_display(self):
        # clear all category widgets
        while self.layout.count():
            child = self.layout.takeAt(0)
            child.widget().deleteLater()
        # re-add new category widgets
        appData = self.appData[0]
        category_count = len(appData.categories)
        if category_count == 0:
            return
        column_count = ceil(sqrt(category_count))
        row_count = ceil(category_count / column_count)
        added_category_count = 0
        for category in appData.categories:
            column = floor(added_category_count / column_count)
            row = added_category_count - (column * column_count)
            categoryWidget = CategoryWidget(category.name, category.color)
            for assignment in category.assignments:
                categoryWidget.add_assignment(assignment, appData.complete_assignment, self.appDataChanged)
            self.layout.addWidget(categoryWidget, row, column)
            added_category_count += 1

    def recolor(self):
        Style.backgroundColorWidget(self, Style.DisplayAreaWidgetColor)
