from PyQt5 import QtCore, QtGui, QtWidgets
import json
import os

class SettingsDialog(QtWidgets.QDialog):
    theme_changed = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setFixedSize(400, 200)
        self.init_ui()

    def init_ui(self):
        main_layout = QtWidgets.QVBoxLayout(self)

        label = QtWidgets.QLabel("Select Application Theme:")
        label.setStyleSheet("font: bold 14pt 'JetBrains Mono'; color: #333;")
        label.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.addWidget(label)

        self.themebox = QtWidgets.QComboBox()
        self.themebox.addItems(["Dark Mode", "Light Mode"])
        self.themebox.setStyleSheet("""
            QComboBox {
                font: 12pt 'JetBrains Mono';
                color: black;
                background-color: white;
                border: 1px solid gray;
                border-radius: 5px;
                padding: 5px;
            }
            QComboBox QAbstractItemView {
                background-color: white;
                border: 1px solid gray;
            }
        """)
        self.themebox.setCurrentText("Dark Mode")
        main_layout.addWidget(self.themebox)

        button_layout = QtWidgets.QHBoxLayout()
        apply_button = QtWidgets.QPushButton("Apply")
        cancel_button = QtWidgets.QPushButton("Cancel")

        apply_button.setStyleSheet("""
            QPushButton {
                background-color: #45A1FF;
                color: white;
                font: bold 12pt 'JetBrains Mono';
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #007BFF;
            }
        """)

        cancel_button.setStyleSheet("""
            QPushButton {
                background-color: gray;
                color: white;
                font: bold 12pt 'JetBrains Mono';
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: darkgray;
            }
        """)

        apply_button.clicked.connect(self.save_edit)
        cancel_button.clicked.connect(self.reject)

        button_layout.addWidget(cancel_button)
        button_layout.addWidget(apply_button)
        main_layout.addLayout(button_layout)

    def save_edit(self):
        selected_theme = self.themebox.currentText()
        if selected_theme == "Dark Mode":
            self.theme_changed.emit("dark")
            self.savetheme("dark")
        elif selected_theme == "Light Mode":
            self.theme_changed.emit("light")
            self.savetheme("light")
        self.accept()

    @staticmethod
    def savetheme(theme):
        with open("settings.json", "w") as file:
            json.dump({"theme": theme}, file)

    @staticmethod
    def loadtheme():
        if os.path.exists("settings.json"):
            try:
                with open("settings.json", "r") as file:
                    data = json.load(file)
                    return data.get("theme", "dark")
            except json.JSONDecodeError:
                return "dark"
        return "dark"


def change_themees(current_window, theme):
    current_window.close()

    if theme == "dark":
        from pyx1 import Ui_Form
    elif theme == "light":
        from ight import Ui_Form

    new_window = QtWidgets.QWidget()
    new_ui = Ui_Form()
    new_ui.setupUi(new_window)
    new_window.show()
    return new_window


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = SettingsDialog()
    dialog.exec_()