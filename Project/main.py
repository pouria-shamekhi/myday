import sys
import json
import os
from PyQt5 import QtWidgets

def loadset():
    if os.path.exists("settings.json"):
        try:
            with open("settings.json", "r") as file:
                data = json.load(file)
                return data.get("theme", "dark")
        except json.JSONDecodeError:
            return "dark"
    return "dark"

def restart_app():
    print("Restarting application...")
    QtWidgets.QApplication.quit()
    os.execl(sys.executable, sys.executable, *sys.argv)

def main():
    app = QtWidgets.QApplication(sys.argv)

    theme = loadset()

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

    if hasattr(ui, 'settings_dialog'):
        ui.settings_dialog.theme_changed.connect(restart_app)
    else:
        print("Settings dialog not found!")

    main_window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
