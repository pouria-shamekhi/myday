from PyQt5 import QtCore, QtGui, QtWidgets
import json
from settings import SettingsDialog
import os
import pygame


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

        self.month = QtWidgets.QLabel("month 2025")
        self.month.setStyleSheet("font: bold 16px; color: white;")

        self.ghabl = QtWidgets.QPushButton("<")
        self.next = QtWidgets.QPushButton(">")
        self.ghabl.setStyleSheet("font: bold 14px; color: white; background-color: gray; border: none;")
        self.ghabl.setFixedSize(30, 30)
        self.next.setStyleSheet("font: bold 14px; color: white; background-color: gray; border: none;")
        self.next.setFixedSize(30, 30)

        self.ghabl.clicked.connect(self.go_to_previous_month)
        self.next.clicked.connect(self.go_to_next_month)

        header_layout.addWidget(self.ghabl)
        header_layout.addWidget(self.month)
        header_layout.addWidget(self.next)

        main_layout.addLayout(header_layout)
        main_layout.addLayout(days_layout)

        self.day_bs = []
        for i in range(6):
            for j in range(7):
                day_b = QtWidgets.QPushButton("")
                day_b.setFixedSize(40, 40)
                day_b.setStyleSheet("border-radius: 20px; background-color: gray; color: white;")
                day_b.clicked.connect(self.on_day_clicked)
                days_layout.addWidget(day_b, i, j)
                self.day_bs.append(day_b)

        self.current_date = QtCore.QDate.currentDate()
        self.selected_button = None

        self.update_calendar()

    def update_calendar(self):
        self.month.setText(self.current_date.toString("MMMM yyyy"))
        first_day = self.current_date.addDays(-self.current_date.day() + 1)
        start_day_of_week = first_day.dayOfWeek()
        days_in_month = self.current_date.daysInMonth()

        for button in self.day_bs:
            button.setText("")
            button.setStyleSheet("border-radius: 20px; background-color: gray; color: white;")

        for day in range(1, days_in_month + 1):
            index = start_day_of_week - 1 + day - 1
            button = self.day_bs[index]
            button.setText(str(day))

            if day == self.current_date.day():
                button.setStyleSheet("border-radius: 20px; background-color: blue; color: white;")

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
                self.selected_button.setStyleSheet("border-radius: 20px; background-color: gray; color: white;")

            sender.setStyleSheet("border-radius: 20px; background-color: gray; border: 2px solid blue; color: white;")
            self.selected_button = sender

            self.date_changed.emit(self.current_date)

class Ui_Form(object):
    def setupUi(self, Form):
        self.Form = Form
        Form.setWindowIcon(QtGui.QIcon("app.ico"))

        Form.setObjectName("My Day")
        Form.setStyleSheet("background-color: rgb(30, 30, 30); ")
        Form.setFixedSize(1100, 700)

        self.label = QtWidgets.QLabel(Form)
        self.line = QtWidgets.QLabel(Form)
        self.line.setGeometry(QtCore.QRect(375, 0, 2, 700))
        self.line.setStyleSheet("background-color: blue;")
        self.line.setObjectName("divider")

        self.label.setGeometry(QtCore.QRect(4, 0, 371, 701))
        self.label.setStyleSheet("background-color: rgb(10, 9, 8);")
        self.label.setObjectName("label")

        self.calendc = calend(Form)
        self.calendc.setGeometry(QtCore.QRect(20, 100, 341, 331))

        self.date_label = QtWidgets.QLabel(Form)
        self.date_label.setGeometry(QtCore.QRect(400, 640, 661, 30))
        self.date_label.setStyleSheet("font: 81 10pt \"JetBrains Mono ExtraBold\"; color: rgb(255, 255, 255); background-color: none;")
        self.date_label.setAlignment(QtCore.Qt.AlignRight)
        self.date_label.setObjectName("date_label")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 200, 33))
        self.label_2.setStyleSheet("font: 81 italic 17pt \"JetBrains Mono ExtraBold\";\n"
                                   "color: rgb(45, 0, 247);\n"
                                   "background-color: none")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("MyDay!")

        self.jam_shavande = QtWidgets.QPushButton(Form)
        self.jam_shavande.setGeometry(QtCore.QRect(10, 10, 32, 28))
        self.jam_shavande.setIcon(QtGui.QIcon("Notebook.png"))
        self.jam_shavande.setIconSize(QtCore.QSize(32, 28))
        self.jam_shavande.setStyleSheet("background: none; border: none;")
        self.jam_shavande.clicked.connect(self.blue_line)

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(400, 110, 661, 511))
        self.listWidget.setStyleSheet("color: white; font: 81 10pt \"JetBrains Mono\"; background-color: black; border: none; padding: 10px;")
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("""
            QListWidget::item {
                border-bottom: 1px solid #505050;
                margin: 5px;
            }
            QListWidget::item:selected {
                background-color: #1E1E1E;
            }
        """)

        self.todo_input = QtWidgets.QLineEdit(Form)
        self.todo_input.setGeometry(QtCore.QRect(400, 70, 661, 30))
        self.todo_input.setPlaceholderText("Type todo here")
        self.todo_input.setStyleSheet("color: gray; font: 81 10pt \"JetBrains Mono\"; background-color: black; border: 1px solid white;")
        self.todo_input.returnPressed.connect(self.add_todo)


        self.settingsb = QtWidgets.QPushButton(Form)
        self.settingsb.setGeometry(QtCore.QRect(20, 640, 341, 41))
        self.settingsb.setStyleSheet(
            "font: 81 10pt \"JetBrains Mono\"; color: rgb(30, 30, 30); background-color: #E8E8E8; border-radius: 10px;")
        self.settingsb.setText("Settings")
        self.settingsb.clicked.connect(self.openset)
        self.settings_dialog = SettingsDialog()
        self.settings_dialog.theme_changed.connect(self.switch_theme)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(400, 30, 101, 16))
        self.label_3.setStyleSheet("font: 81 10pt \"JetBrains Mono ExtraBold\";\n"
                                   "color: white;\n"
                                   "background-color: none\n")
        self.label_3.setText("To-Do-List")

        QtCore.QMetaObject.connectSlotsByName(Form)

        self.calendc.date_changed.connect(self.update_date)

        self.update_date(self.calendc.current_date)
        self.loadtodo()

        self.line_on = True

        self.music = QtWidgets.QWidget(Form)
        self.music.setGeometry(QtCore.QRect(20, 520, 341, 100))
        self.music.setStyleSheet("background-color: blue; border-radius: 10px;")

        music_layout = QtWidgets.QVBoxLayout(self.music)

        self.song_label = QtWidgets.QLabel("No Song Playing")
        self.song_label.setStyleSheet("font: bold 12pt 'JetBrains Mono'; color: white;")
        self.song_label.setAlignment(QtCore.Qt.AlignCenter)
        music_layout.addWidget(self.song_label)

        buttonl = QtWidgets.QHBoxLayout()

        self.ghabli = QtWidgets.QPushButton("Previous")
        self.ghabli.setStyleSheet("""
                    QPushButton {
                        background-color: #45A1FF;
                        color: white;
                        font: bold 10pt 'JetBrains Mono';
                        border-radius: 5px;
                        padding: 5px;
                    }
                    QPushButton:hover {
                        background-color: #007BFF;
                    }
                """)
        self.ghabli.setFixedSize(80, 30)
        buttonl.addWidget(self.ghabli)

        self.badi = QtWidgets.QPushButton("Next")
        self.badi.setStyleSheet("""
                    QPushButton {
                        background-color: #45A1FF;
                        color: white;
                        font: bold 10pt 'JetBrains Mono';
                        border-radius: 5px;
                        padding: 5px;
                    }
                    QPushButton:hover {
                        background-color: #007BFF;
                    }
                """)
        self.badi.setFixedSize(80, 30)
        buttonl.addWidget(self.badi)

        self.playb = QtWidgets.QPushButton("Play")
        self.playb.setStyleSheet("""
                    QPushButton {
                        background-color: #45A1FF;
                        color: white;
                        font: bold 10pt 'JetBrains Mono';
                        border-radius: 5px;
                        padding: 5px;
                    }
                    QPushButton:hover {
                        background-color: #007BFF;
                    }
                """)
        self.playb.setFixedSize(80, 30)
        buttonl.addWidget(self.playb)

        music_layout.addLayout(buttonl)

        self.ghabli.clicked.connect(self.play_ghabli)
        self.badi.clicked.connect(self.play_badi)
        self.playb.clicked.connect(self.play_music)
        pygame.mixer.init()
        self.songfolder("musics")



    def play_music(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
            self.playb.setText("Pause")
        else:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
                self.playb.setText("Play")

    def play_badi(self):
        self.playings_index = (self.playings_index + 1) % len(self.songs)
        self.playsong(self.playings_index)

    def play_ghabli(self):
        self.playings_index = (self.playings_index - 1) % len(self.songs)
        self.playsong(self.playings_index)

    def playsong(self, index):
        if 0 <= index < len(self.songs):
            pygame.mixer.music.load(self.songs[index])
            pygame.mixer.music.play()
            self.song_label.setText(os.path.basename(self.songs[index]))
            self.playings_index = index

    def songfolder(self, folder_path):
        self.songs = []
        for file in os.listdir(folder_path):
            if file.endswith(".mp3"):
                self.songs.append(os.path.join(folder_path, file))
        if self.songs:
            self.playsong(0)

    def update_date(self, date):
        self.date_label.setText(date.toString("yyyy-MM-dd"))
        self.loadtodo()

    def add_todo(self):
        text = self.todo_input.text().strip()
        if text:
            self.newitem(text)
            self.todo_input.clear()
            self.savetodo()

    def newitem(self, text, checked=False):
        todo_item = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()

        checkbox = QtWidgets.QCheckBox()
        checkbox.setFixedSize(24, 24)
        checkbox.setChecked(checked)
        checkbox.stateChanged.connect(lambda state, item=todo_item: self.checkornot(state, item))
        checkbox.setStyleSheet("""
            QCheckBox::indicator {
                width: 24px;
                height: 24px;
                border-radius: 5px;
                border: 2px solid #E8E8E8;
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
        label.setStyleSheet("color: white; font: 81 10pt \"JetBrains Mono\";")
        if checked:
            label.setStyleSheet("color: gray; font: 81 10pt \"JetBrains Mono\"; text-decoration: line-through;")

        removeb = QtWidgets.QPushButton()
        removeb.setStyleSheet("background: blue; border: none; color: #E8E8E8; margin-left: 10px;")
        removeb.clicked.connect(lambda _, item=todo_item: self.remtodo(item))

        layout.addWidget(checkbox)
        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(removeb)
        layout.setContentsMargins(10, 10, 10, 10)

        todo_item.setLayout(layout)
        list_item = QtWidgets.QListWidgetItem()
        list_item.setSizeHint(QtCore.QSize(0, 60))
        self.listWidget.addItem(list_item)
        self.listWidget.setItemWidget(list_item, todo_item)

    def checkornot(self, state, todo_item):
        label = todo_item.findChild(QtWidgets.QLabel)
        if state == QtCore.Qt.Checked:
            label.setStyleSheet("color: gray; font: 81 10pt \"JetBrains Mono\"; text-decoration: line-through;")
        else:
            label.setStyleSheet("color: white; font: 81 10pt \"JetBrains Mono\";")
        self.savetodo()

    def remtodo(self, todo_item):
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            if self.listWidget.itemWidget(item) == todo_item:
                self.listWidget.takeItem(i)
                break
        self.savetodo()


    def openset(self):
        dialog = SettingsDialog()
        dialog.exec_()


    def savetodo(self):
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

        data = self.loadfile()
        date = self.date_label.text()
        data[date] = todos

        with open("todos.json", "w") as file:
            json.dump(data, file, indent=4)

    def loadfile(self):
        try:
            with open("todos.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def loadtodo(self):
        self.listWidget.clear()
        data = self.loadfile()
        date = self.date_label.text()
        if date in data:
            for todo in data[date]:
                self.newitem(todo["text"], todo["checked"])

    def switch_theme(self, theme):
        self.Form.close()  # بستن پنجره فعلی
        if theme == "dark":
            from pyx1 import Ui_Form as DarkUi
            new_window = QtWidgets.QWidget()
            new_ui = DarkUi()
            new_ui.setupUi(new_window)
            new_window.show()
        elif theme == "light":
            from ight import Ui_Form as LightUi
            new_window = QtWidgets.QWidget()
            new_ui = LightUi()
            new_ui.setupUi(new_window)
            new_window.show()

    def blue_line(self):
        if self.line_on:
            self.label.hide()
            self.line.hide()
            self.calendc.hide()
            self.settingsb.hide()
            self.label_2.hide()
            self.music.hide()
            self.listWidget.setGeometry(QtCore.QRect(20, 110, 1061, 511))
            self.todo_input.setGeometry(QtCore.QRect(20, 70, 1061, 30))
            self.label_3.setGeometry(QtCore.QRect(20, 30, 101, 16))
        else:
            self.label.show()
            self.line.show()
            self.calendc.show()
            self.settingsb.show()
            self.label_2.show()
            self.music.show()
            self.listWidget.setGeometry(QtCore.QRect(400, 110, 661, 511))
            self.todo_input.setGeometry(QtCore.QRect(400, 70, 661, 30))
            self.label_3.setGeometry(QtCore.QRect(400, 30, 101, 16))

        self.line_on = not self.line_on
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec_())