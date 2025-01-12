from PyQt5 import QtCore, QtGui, QtWidgets
import json
import os
from settings import SettingsDialog

class calend(QtWidgets.QWidget):
    date_changed = QtCore.pyqtSignal(QtCore.QDate)

    def __init__(self, parent=None):
        super(calend, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("background-color: rgb(30, 30, 30);")

        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)

        header_layout = QtWidgets.QHBoxLayout()
        days_layout = QtWidgets.QGridLayout()

        self.month_label = QtWidgets.QLabel("January 2025")
        self.month_label.setStyleSheet("font: bold 16px; color: #151515;background-color:#2D00F7")
        self.month_label.setAlignment(QtCore.Qt.AlignCenter)

        self.prev_button = QtWidgets.QPushButton("<")
        self.next_button = QtWidgets.QPushButton(">")
        self.prev_button.setStyleSheet("font: bold 14px; color: gray; background-color: white; border: none;")
        self.prev_button.setFixedSize(30, 30)
        self.next_button.setStyleSheet("font: bold 14px; color: gray; background-color: white; border: none;")
        self.next_button.setFixedSize(30, 30)

        self.prev_button.clicked.connect(self.go_to_previous_month)
        self.next_button.clicked.connect(self.go_to_next_month)

        header_layout.addWidget(self.prev_button)
        header_layout.addWidget(self.month_label)
        header_layout.addWidget(self.next_button)

        main_layout.addLayout(header_layout)
        main_layout.addLayout(days_layout)

        self.day_buttons = []
        for i in range(6):
            for j in range(7):
                day_button = QtWidgets.QPushButton("")
                day_button.setFixedSize(40, 40)
                day_button.setStyleSheet("border-radius: 20px; background-color: white; color: black;")
                day_button.clicked.connect(self.on_day_clicked)
                days_layout.addWidget(day_button, i, j)
                self.day_buttons.append(day_button)

        self.current_date = QtCore.QDate.currentDate()
        self.selected_button = None

        self.update_calendar()

    def update_calendar(self):
        self.month_label.setText(self.current_date.toString("MMMM yyyy"))
        first_day = self.current_date.addDays(-self.current_date.day() + 1)
        start_day_of_week = first_day.dayOfWeek()
        days_in_month = self.current_date.daysInMonth()

        for button in self.day_buttons:
            button.setText("")
            button.setStyleSheet("border-radius: 20px; background-color: white; color: black;")

        for day in range(1, days_in_month + 1):
            index = start_day_of_week - 1 + day - 1
            button = self.day_buttons[index]
            button.setText(str(day))

            if day == self.current_date.day():
                button.setStyleSheet("border-radius: 20px; background-color: blue; color: black;")

    def go_to_previous_month(self):
        self.current_date = self.current_date.addMonths(-1)
        self.update_calendar()

    def go_to_next_month(self):
        self.current_date = self.current_date.addMonths(1)
        self.update_calendar()

    def on_day_clicked(self):
        sender = self.sender()
        if sender.text() != "":
            selected_day = int(sender.text())
            self.current_date = self.current_date.addDays(selected_day - self.current_date.day())

            if self.selected_button is not None:
                self.selected_button.setStyleSheet("border-radius: 20px; background-color: white; color: black;")

            sender.setStyleSheet("border-radius: 20px; background-color: white; border: 2px solid blue; color: black;")
            self.selected_button = sender

            self.date_changed.emit(self.current_date)

class Ui_Form(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setWindowIcon(QtGui.QIcon("app.ico"))

        Form.setObjectName("My Day")
        Form.setStyleSheet("background-color: white;")
        Form.setFixedSize(1100, 700)

        self.label = QtWidgets.QLabel(Form)
        self.line = QtWidgets.QLabel(Form)
        self.line.setGeometry(QtCore.QRect(375, 0, 2, 700))
        self.line.setStyleSheet("background-color: blue;")
        self.line.setObjectName("divider")

        self.label.setGeometry(QtCore.QRect(4, 0, 371, 701))
        self.label.setStyleSheet("background-color: #A3A3A3;")
        self.label.setObjectName("label")

        self.calendc = calend(Form)
        self.calendc.setGeometry(QtCore.QRect(20, 180, 341, 331))
        self.calendc.setObjectName("customCalendar")

        self.date_label = QtWidgets.QLabel(Form)
        self.date_label.setGeometry(QtCore.QRect(400, 640, 661, 30))
        self.date_label.setStyleSheet("font: 81 10pt \"JetBrains Mono ExtraBold\"; color: black; background-color: none;")
        self.date_label.setAlignment(QtCore.Qt.AlignRight)
        self.date_label.setObjectName("date_label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 200, 31))
        self.label_2.setStyleSheet("font: 81 italic 17pt \"JetBrains Mono ExtraBold\";\n"
                                   "color: rgb(45, 0, 247);\n"
                                   "background-color: none")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("MyDay!")

        self.jam_shavande = QtWidgets.QPushButton(Form)
        self.jam_shavande.setGeometry(QtCore.QRect(10, 10, 32, 28))
        self.jam_shavande.setIcon(QtGui.QIcon("Notebookl.png"))
        self.jam_shavande.setIconSize(QtCore.QSize(32, 28))
        self.jam_shavande.setStyleSheet("background: none; border: none;")
        self.jam_shavande.clicked.connect(self.toggle_sidebar)

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(400, 110, 661, 511))
        self.listWidget.setStyleSheet("color: white; font: 81 10pt \"JetBrains Mono\"; background-color: white; border: none; padding: 10px;")
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("""
            QListWidget::item {
                border-bottom: 2px solid #505050;
                margin: 5px;
            }
            QListWidget::item:selected {
                background-color: #1E1E1E;
            }
        """)

        self.todo_input = QtWidgets.QLineEdit(Form)
        self.todo_input.setGeometry(QtCore.QRect(400, 70, 661, 30))
        self.todo_input.setPlaceholderText("Type todo here")
        self.todo_input.setStyleSheet("color: #B2B2B2; font: 81 10pt \"JetBrains Mono\"; background-color: black; border: 1px solid black;")
        self.todo_input.returnPressed.connect(self.add_todo)

        self.settings_button = QtWidgets.QPushButton(Form)
        self.settings_button.setGeometry(QtCore.QRect(20, 640, 341, 41))
        self.settings_button.setStyleSheet(
            "font: 81 10pt \"JetBrains Mono\"; color: rgb(30, 30, 30); background-color: #E8E8E8; border-radius: 10px;")
        self.settings_button.setText("Settings")
        self.settings_button.clicked.connect(self.open_settings)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(400, 30, 101, 16))
        self.label_3.setStyleSheet("font: 81 10pt \"JetBrains Mono ExtraBold\";\n"
                                   "color: black;\n"
                                   "background-color: none\n")
        self.label_3.setText("To-Do-List")

        QtCore.QMetaObject.connectSlotsByName(Form)

        self.calendc.date_changed.connect(self.update_date)

        self.update_date(self.calendc.current_date)
        self.load_todos()

        self.selected_item = None
        self.sidebar_visible = True

    def update_date(self, date):
        self.date_label.setText(date.toString("yyyy-MM-dd"))
        self.load_todos()

    def add_todo(self):
        text = self.todo_input.text().strip()
        if text:
            self.add_todo_item(text)
            self.todo_input.clear()
            self.save_todos()

    def add_todo_item(self, text, checked=False):
        todo_item = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()

        checkbox = QtWidgets.QCheckBox()
        checkbox.setFixedSize(24, 24)
        checkbox.setChecked(checked)
        checkbox.stateChanged.connect(lambda state, item=todo_item: self.checked_or_not(state, item))
        checkbox.setStyleSheet("""
            QCheckBox::indicator {
                width: 24px;
                height: 24px;
                border-radius: 5px;
                border: 2px solid black;
                background-color: transparent;
            }
            QCheckBox::indicator:checked {
                background-color: #45A1FF;
                border: 2px solid #007BFF;
            }
            QCheckBox::indicator:hover {
                background-color: #A1D1FF;
            }
        """)

        label = QtWidgets.QLabel(text)
        label.setStyleSheet("color: black; font: 81 10pt \"JetBrains Mono\";")
        if checked:
            label.setStyleSheet("color: gray; font: 81 10pt \"JetBrains Mono\"; text-decoration: line-through;")

        delete_button = QtWidgets.QPushButton()
        delete_button.setStyleSheet("background: blue; border: none; color: #E8E8E8; margin-left: 10px;")
        delete_button.clicked.connect(lambda _, item=todo_item: self.remove_item(item))

        layout.addWidget(checkbox)
        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(delete_button)
        layout.setContentsMargins(10, 10, 10, 10)

        todo_item.setLayout(layout)
        list_item = QtWidgets.QListWidgetItem()
        list_item.setSizeHint(QtCore.QSize(0, 60))
        self.listWidget.addItem(list_item)
        self.listWidget.setItemWidget(list_item, todo_item)

    def checked_or_not(self, state, todo_item):
        label = todo_item.findChild(QtWidgets.QLabel)
        if state == QtCore.Qt.Checked:
            label.setStyleSheet("color: gray; font: 81 10pt \"JetBrains Mono\"; text-decoration: line-through;")
        else:
            label.setStyleSheet("color: black; font: 81 10pt \"JetBrains Mono\";")
        self.save_todos()

    def remove_item(self, todo_item):
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            if self.listWidget.itemWidget(item) == todo_item:
                self.listWidget.takeItem(i)
                break
        self.save_todos()

    def open_settings(self):
        dialog = SettingsDialog()
        dialog.exec_()

    def save_todos(self):
        todos = []
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            widget = self.listWidget.itemWidget(item)
            label = widget.findChild(QtWidgets.QLabel)
            checkbox = widget.findChild(QtWidgets.QCheckBox)

            todos.append({
                "text": label.text(),
                "checked": checkbox.isChecked()
            })

        data = self.load_data()
        date = self.date_label.text()
        data[date] = todos

        with open("todos.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        try:
            with open("todos.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def load_todos(self):
        self.listWidget.clear()
        data = self.load_data()
        date = self.date_label.text()
        if date in data:
            for todo in data[date]:
                self.add_todo_item(todo["text"], todo["checked"])

    def toggle_sidebar(self):
        if self.sidebar_visible:
            self.label.hide()
            self.line.hide()
            self.calendc.hide()
            self.settings_button.hide()
            self.label_2.hide()

            self.listWidget.setGeometry(QtCore.QRect(20, 110, 1061, 511))
            self.todo_input.setGeometry(QtCore.QRect(20, 70, 1061, 30))
            self.label_3.setGeometry(QtCore.QRect(20, 30, 101, 16))
        else:
            self.label.show()
            self.line.show()
            self.calendc.show()
            self.settings_button.show()
            self.label_2.show()

            self.listWidget.setGeometry(QtCore.QRect(400, 110, 661, 511))
            self.todo_input.setGeometry(QtCore.QRect(400, 70, 661, 30))
            self.label_3.setGeometry(QtCore.QRect(400, 30, 101, 16))

        self.sidebar_visible = not self.sidebar_visible


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec_())