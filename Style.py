from PySide6 import QtCore


class Style:

    AppWindowColor = "white"
    ControlPanelWidgetColor = "#D4F1F9"  # Water
    ControlPanelEditWidgetColor = "#BEEAC2"  # Tea green
    ControlPanelViewWidgetColor = "#BEEAC2"  # Tea green
    DisplayAreaWidgetColor = "#F5FFFD"  # Mint cream
    UpcomingWidgetColor = "#D4F1F9"  # Water

    def __init__():
        pass

    @classmethod
    def backgroundColorWidget(cls, widget, color):
        widget.setAttribute(QtCore.Qt.WA_StyledBackground, True)
        widget.setStyleSheet('background-color: {}'.format(color))

    @classmethod
    def funTheme(cls):
        Style.AppWindowColor = "white"
        Style.ControlPanelWidgetColor = "#D4F1F9"  # Water
        Style.ControlPanelEditWidgetColor = "#BEEAC2"  # Tea green
        Style.ControlPanelViewWidgetColor = "#BEEAC2"  # Tea green
        Style.DisplayAreaWidgetColor = "#F5FFFD"  # Mint cream
        Style.UpcomingWidgetColor = "#D4F1F9"  # Water

    @classmethod
    def grayTheme(cls):
        Style.AppWindowColor = "#DFDFDF"
        Style.ControlPanelWidgetColor = "#BEBEBE"
        Style.ControlPanelEditWidgetColor = "#A3A3A3"
        Style.ControlPanelViewWidgetColor = "#A3A3A3"
        Style.DisplayAreaWidgetColor = "#8D8D8D"
        Style.UpcomingWidgetColor = "#BEBEBE"
