from PySide6 import QtWidgets

from Style import Style


class ControlPanelViewWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel(self)
        label.setText("View")
        categoryViewButton = QtWidgets.QPushButton("By Category", self)
        categoryViewButton.clicked.connect(self.category_view_button_clicked)
        layout.addWidget(label)
        layout.addWidget(categoryViewButton)
        self.setLayout(layout)
        Style.backgroundColorWidget(self, Style.ControlPanelViewWidgetColor)

    def recolor(self):
        Style.backgroundColorWidget(self, Style.ControlPanelViewWidgetColor)

    def category_view_button_clicked(self):
        # TODO
        # after other view types are added
        pass
