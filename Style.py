from PySide6 import QtCore

class Style:

    AppWindowColor = "white"
    ControlPanelWidgetColor = "#D4F1F9" # Water
    ControlPanelEditWidgetColor = "#BEEAC2" # Tea green
    ControlPanelViewWidgetColor = "#BEEAC2" # Tea green
    DisplayAreaWidgetColor = "#F5FFFD" # Mint cream
    UpcomingWidgetColor = "#D4F1F9" # Water

    def __init__():
        pass

    @classmethod
    def backgroundColorWidget(cls, widget, color):
        widget.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        widget.setStyleSheet('background-color: {}'.format(color))
