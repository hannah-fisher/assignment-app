from PySide6 import QtWidgets
from PySide6.QtCore import Qt

from Style import Style


class UpcomingWidget(QtWidgets.QWidget):
    def __init__(self, appData):
        super().__init__()
        self.appData = appData
        label = QtWidgets.QLabel(self)
        label.setText("Upcoming Assignments")
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

        Style.backgroundColorWidget(self, Style.UpcomingWidgetColor)

    def reload_display(self):
        # clear all assignments
        while self.vbox.count():
            child = self.vbox.takeAt(0)
            child.widget().deleteLater()
        # re-add new assignments
        for (a, c) in self.appData[0].get_soonest_n_assignments(5):
            assignment_label = QtWidgets.QLabel(self)
            label_string = ""
            label_string += str(a.due_date) + " "
            label_string += str(a.priority) + " "
            label_string += a.title + " "
            assignment_label.setText(label_string)
            Style.backgroundColorWidget(assignment_label, c)
            self.vbox.addWidget(assignment_label)

    def recolor(self):
        Style.backgroundColorWidget(self, Style.UpcomingWidgetColor)
