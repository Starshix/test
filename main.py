import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont, QColor

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("Тренажёр таблицы умножения")
        self.setStyleSheet("background-color: #575300")

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.example_label = QLabel()
        self.example_label.setFont(QFont("Arial", 20))
        self.grid.addWidget(self.example_label, 0, 0, 1, 3)

        self.answer_label = QLabel("Ответ:")
        self.answer_label.setFont(QFont("Arial", 16))
        self.grid.addWidget(self.answer_label, 1, 0)

        self.answer_input = QLineEdit()
        self.answer_input.setStyleSheet('background-color: white')
        self.answer_input.setFont(QFont("Arial", 16))
        self.grid.addWidget(self.answer_input, 1, 1)

        self.check_button = QPushButton("Проверить")
        self.check_button.setFont(QFont("Arial", 16))
        self.check_button.setStyleSheet("background-color: #d65300")
        self.check_button.clicked.connect(self.check_answer)
        self.grid.addWidget(self.check_button, 1, 2)

        self.result_label = QLabel()
        self.result_label.setFont(QFont("Arial", 16))
        self.grid.addWidget(self.result_label, 2, 0, 1, 3)

        self.hint_button = QPushButton("Подсказка")
        self.hint_button.setFont(QFont("Arial", 16))
        self.hint_button.setStyleSheet("background-color: #74539a")
        self.hint_button.clicked.connect(self.show_hint)
        self.grid.addWidget(self.hint_button, 3, 2)

        self.generate_example()

    def generate_example(self):
        self.factor1 = random.randint(1, 20)
        self.factor2 = random.randint(1, 20)
        self.example_label.setText(f"{self.factor1} x {self.factor2} =")

    def check_answer(self):
        answer = int(self.answer_input.text())
        correct_answer = self.factor1 * self.factor2

        if answer == correct_answer:
            self.result_label.setText("Правильно!")
            self.result_label.setStyleSheet("color: #00FF00")
        else:
            self.result_label.setText("Неправильно!")
            self.result_label.setStyleSheet("color: #FF0000")

    def show_hint(self):
        self.result_label.setText(f"Правильный ответ: {self.factor1 * self.factor2}")
        self.result_label.setStyleSheet("color: #000000")


app = QApplication(sys.argv)

trainer = MainWindow()
trainer.show()

sys.exit(app.exec_())