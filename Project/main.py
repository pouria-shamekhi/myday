import sys
import json
import os
from PyQt5 import QtWidgets

def load_theme_setting():
    if os.path.exists("settings.json"):
        try:
            with open("settings.json", "r") as file:
                data = json.load(file)
                return data.get("theme", "dark")
        except json.JSONDecodeError:
            return "dark"
    return "dark"

def main():
    app = QtWidgets.QApplication(sys.argv)

    theme = load_theme_setting()

    if theme == "dark":
        from pyx1 import Ui_Form
    elif theme == "light":
        from pyx1_light import Ui_Form
    else:
        print("Invalid theme :(")
        from pyx1 import Ui_Form

    main_window = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(main_window)
    main_window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
