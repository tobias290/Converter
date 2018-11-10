import ctypes
import locale
import platform
import sys
from typing import List

from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, QEvent
from PyQt5.QtGui import QFontDatabase, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QComboBox, QLabel, QVBoxLayout, \
    QScrollArea, QWidget

import helpers
from convertions import CONVERSIONS, get_list_from_conversion_name as glfcn

# https://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
# Needed so the taskbar will use the app icon (Answer found at above URL(

app_id = "tobyessex.converter.1.1"  # Arbitrary string

if platform.system() == "Window":
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    locale.setlocale(locale.LC_ALL, 'en_US')


class MainWindow(QMainWindow):
    """
    Main class which holds all code relating to the main window and GUI interface
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # noinspection PyArgumentList
        # noinspection PyCallByClass
        QFontDatabase.addApplicationFont("fonts/krub/Krub-Regular.ttf")

        # Set window properties
        self.setWindowTitle("Converter")
        self.setWindowIcon(QIcon("images/app/logo.png"))
        self.setFixedSize(300, 500)
        self.setObjectName("main")

        self.setStyleSheet(open("main.css").read())

        # Navigation buttons/labels placeholders
        self.previous: QLabel = None
        self.current: QLabel = None
        self.next: QLabel = None

        # Animation property for the navigation buttons/labels
        self.animation: QPropertyAnimation = None

        # List of available conversions
        self.options: helpers.ListHelper = helpers.ListHelper(CONVERSIONS)
        self.current_option_symbol: str = glfcn(self.options.current)[0].symbol

        # Create the navigation
        self.create_navigation()

        # Main conversion UI placeholders
        self.input: QLineEdit = None
        self.convert: QPushButton = None
        self.clear: QPushButton = None
        self.combo: QComboBox = None
        self.results: List[QLabel] = []

        self.container: QWidget = None
        self.v_layout: QVBoxLayout = None
        self.scroll_area: QScrollArea = None

        # Create the main UI
        self.create_ui()

        # Show all
        self.show()

    def create_navigation(self):
        """
        Creates the navigation UI
        """
        self.previous = QLabel(self.options.previous, self)
        self.previous.mousePressEvent = self.previous_button_click
        self.previous.installEventFilter(self)
        self.previous.setToolTip(self.options.previous)
        self.previous.setObjectName("previous-category")
        self.previous.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.previous.setGeometry(-125, 20, 150, 50)

        self.current = QLabel(self.options.current, self)
        self.current.setObjectName("current-category")
        self.current.setAlignment(Qt.AlignCenter)
        self.current.setGeometry(helpers.set_to_middle(300, 200), 20, 200, 50)

        self.next = QLabel(self.options.next, self)
        self.next.mousePressEvent = self.next_button_click
        self.next.installEventFilter(self)
        self.next.setToolTip(self.options.next)
        self.next.setObjectName("next-category")
        self.next.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.next.setGeometry(275, 20, 150, 50)

    def create_ui(self):
        """
        Creates the main UI for the conversions
        """
        self.input = QLineEdit(self)
        self.input.setGeometry(0, 90, 250, 70)

        self.combo = QComboBox(self)
        self.combo.currentIndexChanged.connect(self.change_option_symbol)
        self.combo.setObjectName("combo")
        self.combo.addItems(glfcn(self.options.current))
        self.combo.setGeometry(230, 90, 70, 70)

        self.convert = QPushButton("Convert", self)
        self.convert.clicked.connect(self.convert_click)
        self.convert.setObjectName("convert")
        self.convert.setGeometry(0, 160, 150, 70)

        self.clear = QPushButton("Clear", self)
        self.clear.clicked.connect(self.clear_click)
        self.clear.setObjectName("clear")
        self.clear.setGeometry(150, 160, 150, 70)

    def eventFilter(self, obj, event):
        """
        Event filter for when the user hovers over the previous/next options in the navigation UI
        :param obj: Instance of the object that was clicked on
        :param event: Event type
        :return: Return true if event occurred
        """

        if event.type() == QEvent.HoverEnter:
            self.animation = QPropertyAnimation(obj, b"geometry")
            self.animation.setDuration(100)
            self.animation.setStartValue(QRect(275, 20, 150, 50) if obj == self.next else QRect(-125, 20, 150, 50))
            self.animation.setEndValue(QRect(265, 20, 150, 50) if obj == self.next else QRect(-115, 20, 150, 50))
            self.animation.start()
            return True
        elif event.type() == QEvent.HoverLeave:
            self.animation = QPropertyAnimation(obj, b"geometry")
            self.animation.setDuration(100)
            self.animation.setStartValue(QRect(265, 20, 150, 50) if obj == self.next else QRect(-115, 20, 150, 50))
            self.animation.setEndValue(QRect(275, 20, 150, 50) if obj == self.next else QRect(-125, 20, 150, 50))
            self.animation.start()
            return True
        return False

    def update_navigation(self):
        """
        Update the navigation when the user navigates between options
        """
        # Set new option titles
        self.previous.setText(self.options.previous)
        self.previous.setToolTip(self.options.previous)
        self.current.setText(self.options.current)
        self.next.setText(self.options.next)
        self.next.setToolTip(self.options.next)

        # Update UI components
        self.previous.update()
        self.current.update()
        self.next.update()

    def previous_button_click(self, event):
        """
        Called when the previous option button is clicked.
        Changes the conversion to the previous option
        :param event: Event type
        """
        self.options.change_previous_to_current()
        self.combo.clear()
        self.combo.addItems(glfcn(self.options.current))
        self.update_navigation()

    def next_button_click(self, event):
        """
        Called when the next option button is clicked.
        Changes the conversion to the next option
        :param event: Event type
       """
        self.options.change_next_to_current()
        self.combo.clear()
        self.combo.addItems(glfcn(self.options.current))
        self.update_navigation()

    def change_option_symbol(self, i):
        """
        Called when the user changed the unit of conversion for the given conversion type
        :param i: Current index
        """
        self.current_option_symbol = glfcn(self.options.current)[i].symbol

    def convert_click(self):
        """
        Called when the user clicks the convert button
        Takes the given input and outputs all the possible conversions
        """
        # If no input don't attempt to convert
        if self.input.text() == "" or self.input.text().isspace():
            return

        if self.container is not None:
            self.container.deleteLater()
            self.container.update()
            self.v_layout.deleteLater()
            self.v_layout.update()
            self.scroll_area.deleteLater()
            self.scroll_area.update()

        # Delete all the current results
        for result in self.results:
            result.deleteLater()
            result.update()

        # Clear the results list
        self.results.clear()

        # Create the converter
        converter = \
            glfcn(self.options.current)\
            .get_unit_from_symbol(self.current_option_symbol)\
            .cls(self.input.text())

        self.container = QWidget(self)
        self.v_layout = QVBoxLayout()

        # Get all the results and append them to the results list and crate a visible label for each result
        for i, (key, value) in enumerate(converter.all().items()):
            value = round(value, 6) if type(value) != str else value
            label = QLabel(f"{value} <strong>{key}</strong>", self)
            label.setProperty("class", "result" if i != len(converter.all().items()) - 1 else "result no-border")
            label.setGeometry(0, 230 + (i * 70), 300, 70)
            label.setFixedSize(300, 70)

            self.v_layout.addWidget(label, alignment=Qt.AlignLeft)

            # Append the results
            self.results.append(label)

        self.container.setLayout(self.v_layout)
        self.container.setFixedWidth(300)

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.container)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setGeometry(0, 230, 300, 270)

        self.scroll_area.show()
        self.container.show()

    def clear_click(self):
        """
        Clears the input box
        """
        self.input.clear()

        if self.container is not None:
            self.container.deleteLater()
            self.container.update()
            self.v_layout.deleteLater()
            self.v_layout.update()
            self.scroll_area.deleteLater()
            self.scroll_area.update()

        # Delete all the current results
        for result in self.results:
            result.deleteLater()
            result.update()

        # Clear the results list
        self.results.clear()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook

    # Create the application and give the window a name
    app = QApplication(sys.argv)
    app.setApplicationName("Test")

    # Create the main window
    MainWindow()

    app.exec_()
