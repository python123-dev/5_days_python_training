#Python GUI with PyQt5 - window, widgets, layout and a click event
#run this file directly: python pyqt_basics.py
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
)


class DemoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 Basics')
        self.resize(300, 200)
        self.build_ui()

    def build_ui(self):
        #widgets
        self.title_label = QLabel('PyQt5 Widgets Demo')
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText('Enter your name')
        self.greet_button = QPushButton('Greet')
        self.result_label = QLabel('')

        #event - connect the button's click signal to a handler method
        self.greet_button.clicked.connect(self.on_greet_clicked)

        #layout - stack widgets vertically, with a horizontal row for the input+button
        input_row = QHBoxLayout()
        input_row.addWidget(self.name_input)
        input_row.addWidget(self.greet_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addLayout(input_row)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

    def on_greet_clicked(self):
        name = self.name_input.text() or 'stranger'
        self.result_label.setText(f'Hello, {name}!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoWindow()
    window.show()
    sys.exit(app.exec_())
