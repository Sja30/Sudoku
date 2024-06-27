import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel,
                             QMessageBox, QVBoxLayout, QWidget, QGridLayout,
                             QFrame, QLineEdit, QGraphicsLineItem, QHBoxLayout,
                             QLineEdit, QGraphicsScale, QStackedLayout)
from PyQt5.QtGui import QPixmap, QPainter, QColor, QFont, QIntValidator, QPen, QBrush
from PyQt5.QtCore import Qt
import random


# Класс для заполнения поля
class SudokuGenerator:
    def __init__(self):
        self.board = [[0] * 9 for _ in range(9)]

    # Генерация заполнения поля
    def generate_full_board(self):
        self.fill_board()
        return self.board

    # Создает пустой массив с начальными координатами (0,0)
    def fill_board(self):
        self.board = [[0] * 9 for _ in range(9)]
        self._fill_board(0, 0)

    # Заполнение поля
    def _fill_board(self, row, col):
        if row == 9:
            return True
        if col == 9:
            return self._fill_board(row + 1, 0)
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for number in numbers:
            if self._is_safe_to_place(row, col, number):
                self.board[row][col] = number
                if self._fill_board(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def _is_safe_to_place(self, row, col, number):
        if number in self.board[row]:
            return False
        if number in [self.board[i][col] for i in range(9)]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == number:
                    return False
        return True

    # Случайное удаление чисел из поля
    def remove_numbers_from_board(self, num_holes):
        count = 0
        while count < num_holes:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count += 1


# Создание главного окна
class sudoky(QMainWindow):
    def __init__(self):
        super(sudoky, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Судоку")
        self.setFixedSize(700, 600)

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("qwerty/menu.jpg"))
        self.background.setGeometry(0, 0, 700, 600)
        self.background.setScaledContents(True)

        self.Main_nadpis1 = QLabel(self)
        self.Main_nadpis1.setText("Судоку")
        self.Main_nadpis1.setStyleSheet("font: 75 italic 30pt \"Arial\";\n" "color: rgb(0, 0, 0);")
        self.Main_nadpis1.setGeometry(270, 160, 200, 70)

        self.igrat = QtWidgets.QPushButton(self)
        self.igrat.setText("Играть")
        self.igrat.setStyleSheet("font: 75 italic 24pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.igrat.setGeometry(250, 250, 200, 50)
        self.igrat.clicked.connect(self.open_window2)

        self.end = QPushButton('Выход', self)
        self.end.setGeometry(250, 380, 200, 50)
        self.end.setStyleSheet("font: 75 italic 24pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.end.clicked.connect(self.close)

        self.prav = QPushButton('Правила', self)
        self.prav.setGeometry(250, 314, 200, 50)
        self.prav.setStyleSheet("font: 75 italic 24pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.prav.clicked.connect(self.open_window)

    def open_window(self):
        self.one_window = OneWindow(self)
        self.hide()
        self.one_window.show()

    def open_window2(self):
        self.two_window = TwoWindow(self)
        self.hide()
        self.two_window.show()


# Окно правила
class OneWindow(QMainWindow):
    def __init__(self, first_window):
        super().__init__()
        self.setWindowTitle('Правила')
        self.setFixedSize(700, 600)

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("qwerty/pravila.png"))
        self.background.setGeometry(0, 0, 700, 600)
        self.background.setScaledContents(True)

        self.back = QPushButton('X', self)
        self.back.setGeometry(600, 70, 78, 78)
        self.back.setStyleSheet(
            "border-radius: 39; border: 2px solid gray; font: 75 italic 28pt \"Arial\";\n""color:rgb(255, 255, 255);background-color : gray")
        self.back.clicked.connect(lambda: self.back_open(first_window))

    def back_open(self, first_window):
        first_window.show()
        self.close()


# Окно расположения уровней
class TwoWindow(QMainWindow):
    def __init__(self, second_window):
        super().__init__()
        self.level_window = ThreeWindow(self, 'Легкий')
        self.level1_window = ThreeWindow(self, 'Средний')
        self.level2_window = ThreeWindow(self, 'Сложный')
        self.setWindowTitle('Выбор уровня сложности')
        self.setFixedSize(700, 600)

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("qwerty/menu.jpg"))
        self.background.setGeometry(0, 0, 700, 600)
        self.background.setScaledContents(True)

        self.back = QPushButton('Назад', self)
        self.back.setGeometry(40, 520, 150, 50)
        self.back.setStyleSheet("font: 75 italic 24pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.back.clicked.connect(lambda: self.back_open(second_window))

        self.level1 = QPushButton('Легкий', self)
        self.level1.setGeometry(80, 150, 150, 150)
        self.level1.setStyleSheet("font: 75 italic 20pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.level1.clicked.connect(self.open_easy_window)

        self.level2 = QPushButton('Средний', self)
        self.level2.setGeometry(280, 150, 150, 150)
        self.level2.setStyleSheet("font: 75 italic 20pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.level2.clicked.connect(self.open_medium_window)

        self.level3 = QPushButton('Сложный', self)
        self.level3.setGeometry(480, 150, 150, 150)
        self.level3.setStyleSheet("font: 75 italic 20pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.level3.clicked.connect(self.open_hard_window)

    def back_open(self, first_window):
        first_window.show()
        self.close()

    def open_easy_window(self):
        self.hide()
        self.level_window.show()

    def open_medium_window(self):
        self.hide()
        self.level1_window.show()

    def open_hard_window(self):
        self.hide()
        self.level2_window.show()


# Создание окон для уровней
class ThreeWindow(QMainWindow):
    def __init__(self, parent, difficulty):
        super().__init__()
        self.difficulty = difficulty
        self.setWindowTitle('Уровень')
        self.setFixedSize(700, 610)
        self.num_holes = self.get_num_holes()

        # Создание центрального виджета для кнопок и поля Sudoku
        central_widget = QWidget(self)

        # Установка центрального виджета в окне
        self.setCentralWidget(central_widget)

        # Установка фонового изображения окна
        self.set_background("qwerty/уровни.jpg")

        # Создание кнопки "Назад"
        self.back = QPushButton('Назад', central_widget)
        self.back.setStyleSheet("font: 75 italic 24pt \"Arial\"; color: rgb(255, 255, 255); background-color: black;")
        self.back.clicked.connect(lambda: self.back_open(parent))

        # Создание кнопки "Сгенерировать"
        self.generate_button = QPushButton('Сгенерировать', central_widget)
        self.generate_button.setStyleSheet(
            "font: 75 italic 24pt \"Arial\"; color: rgb(255, 255, 255); background-color: black;")
        self.generate_button.clicked.connect(self.generate_sudoku)

        # Создание кнопки "Проверить"
        self.check_button = QPushButton('Проверить', central_widget)
        self.check_button.setStyleSheet(
            "font: 75 italic 24pt \"Arial\"; color: rgb(255, 255, 255); background-color: black;")
        self.check_button.clicked.connect(self.check_sudoku)
        self.check_button.setEnabled(False)  # Начально кнопка неактивна

        # Создание виджета для поля Sudoku
        self.board_widget = QWidget(self)
        grid_layout = QGridLayout(self.board_widget)
        grid_layout.setSpacing(0)
        grid_layout.setContentsMargins(0, 0, 0, 0)

        self.board = [[QLineEdit(self) for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cell = self.board[i][j]
                cell.setFixedSize(60, 60)
                cell.setAlignment(Qt.AlignCenter)
                cell.setFont(QFont("Arial", 16))
                cell.setValidator(QIntValidator(1, 9))
                cell.textChanged.connect(self.check_input)

                grid_layout.addWidget(cell, i, j)

        # Создание разметки для центрального виджета
        central_layout = QVBoxLayout(central_widget)
        central_layout.addWidget(self.back)
        central_layout.addWidget(self.generate_button)
        central_layout.addWidget(self.check_button)
        central_layout.addWidget(self.board_widget)

    def set_background(self, image_path):
        # Установка фонового изображения окна через стиль CSS
        style_str = f"background-image: url('{image_path}'); background-position: center; background-repeat: no-repeat; background-attachment: fixed;"
        central_widget = self.centralWidget()
        central_widget.setStyleSheet(style_str)

    # Заполнение поля в зависимости от уровня сложности
    def get_num_holes(self):
        if self.difficulty == 'Легкий':
            return 30
        elif self.difficulty == 'Средний':
            return 40
        elif self.difficulty == 'Сложный':
            return 50

    # Кнопка назад
    def back_open(self, level_window):
        level_window.show()
        self.close()

    # Генерация игрового поля с учетом количества пустых клеток
    def generate_sudoku(self):
        generator = SudokuGenerator()
        generator.generate_full_board()
        generator.remove_numbers_from_board(self.num_holes)
        board = generator.board

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                cell = self.board[i][j]
                if value != 0:
                    cell.setText(str(value))
                    cell.setReadOnly(True)
                else:
                    cell.clear()
                    cell.setReadOnly(False)
                self.check_button.setEnabled(True)

    # Проверка корректности введенных значений
    def check_input(self, text):
        sender = self.sender()  # Получаем объект QLineEdit, который послал сигнал
        if text.strip() == '':
            return

        value = int(text) if text.isdigit() else None
        if value is None or not (1 <= value <= 9):
            QMessageBox.warning(self, "Ошибка", "Введите число от 1 до 9")
            sender.clear()

    # проверка правильности решения
    def check_sudoku(self):
        if self.is_valid_board():
            QMessageBox.information(self, "Поздравляем", "Вы решили правильно!")
        else:
            QMessageBox.warning(self, "Ошибка", "Неправильное положение цифры ")

    # проверка корректности всего поля
    def is_valid_board(self):
        for i in range(9):
            for j in range(9):
                if not self.is_valid_row(i, j) or not self.is_valid_column(i, j) or not self.is_valid_square(i, j):
                    return False
        return True

    # проверка корректности строки
    def is_valid_row(self, row, col):
        current_text = self.board[row][col].text().strip()
        if current_text == '':
            return False
        current_value = int(current_text)
        for j in range(9):
            if j != col:
                cell_text = self.board[row][j].text().strip()
                if cell_text != '' and int(cell_text) == current_value:
                    return False
        return True

    # проверка корректности столбца
    def is_valid_column(self, row, col):
        current_text = self.board[row][col].text().strip()
        if current_text == '':
            return True  # Пустая ячейка считается валидной
        current_value = int(current_text)
        for i in range(9):
            if i != row:
                cell_text = self.board[i][col].text().strip()
                if cell_text != '' and int(cell_text) == current_value:
                    return False
        return True

    # проверка корректности квадрата 3х3
    def is_valid_square(self, row, col):
        current_text = self.board[row][col].text().strip()
        if current_text == '':
            return True  # Пустая ячейка считается валидной
        current_value = int(current_text)
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if i != row and j != col:
                    cell_text = self.board[i][j].text().strip()
                    if cell_text != '' and int(cell_text) == current_value:
                        return False
        return True


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = sudoky()
    application.show()
    sys.exit(app.exec_())
