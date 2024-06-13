import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QMainWindow,
                             QMessageBox, QVBoxLayout, QWidget,
                             QGridLayout, QFrame, QLineEdit, QGraphicsLineItem, QHBoxLayout,
                             QLineEdit, QGraphicsScale)
from PyQt5.QtGui import QPixmap, QPainter, QColor, QFont, QIntValidator, QPen
from PyQt5.QtCore import Qt


class sudoky(QMainWindow):

    def __init__(self):
        super(sudoky, self).__init__()
        self.two_window = TwoWindow(self)
        self.background = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sudoky")
        self.setGeometry(0, 0, 700, 600)

        # Создание фонового изображения
        self.background.setPixmap(QPixmap("qwerty/menu.jpg"))
        self.background.setGeometry(0, 0, 700, 600)
        self.background.setScaledContents(True)

        # Создание надписи судок
        self.Main_nadpis1 = QLabel(self)
        self.Main_nadpis1.setText("Судоку")
        self.Main_nadpis1.setStyleSheet("font: 75 italic 30pt \"Arial\";\n" "color: rgb(0, 0, 0);")
        self.Main_nadpis1.setGeometry(270, 160, 200, 70)

        # Создание кнопки начала игры
        self.igrat = QtWidgets.QPushButton(self)
        self.igrat.setText("Играть")
        self.igrat.setStyleSheet("font: 75 italic 24pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.igrat.setGeometry(250, 250, 200, 50)
        self.igrat.clicked.connect(self.open_window2)

        # Настройки кнопки Выход
        self.end = QPushButton('Выход', self)
        self.end.setGeometry(250, 380, 200, 50)
        self.end.setStyleSheet("font: 75 italic 24pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.end.clicked.connect(self.close)

        # Настройка кнопки Правила
        self.prav = QPushButton('Правила', self)
        self.prav.setGeometry(250, 314, 200, 50)
        self.prav.setStyleSheet("font: 75 italic 24pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.prav.clicked.connect(self.open_window)

    # Создание окна правила
    def open_window(self):
        self.one_window = OneWindow(self)
        self.hide()
        self.one_window.show()

    # Создание окна начала игры
    def open_window2(self):
        self.hide()
        self.two_window.show()

    # Правила


class OneWindow(QMainWindow):
    def __init__(self, first_window):
        super().__init__()
        self.setWindowTitle('Sudoky')
        self.setGeometry(0, 0, 700, 600)

        # Создание фонового изображения
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("qwerty/pravila.png"))
        self.background.setGeometry(0, 0, 700, 600)
        self.background.setScaledContents(True)

        # Создание кнопки назад
        self.back = QPushButton('X', self)
        self.back.setGeometry(600, 70, 78, 78)
        self.back.setStyleSheet(
            "border-radius: 39; border: 2px solid gray; font: 75 italic 28pt \"Arial\";\n""color:rgb(255, 255, 255);background-color : gray")
        self.back.clicked.connect(lambda: self.back_open(first_window))

    def back_open(self, first_window):
        first_window.show()
        self.close()

    # Создание окна начало


class TwoWindow(QMainWindow):
    def __init__(self, second_window):
        super().__init__()
        self.level_window = ThreeWindow(self)
        self.level1_window = FourWindow(self)
        self.level2_window = FiveWindow(self)
        self.setWindowTitle('Sudoky')
        self.setGeometry(0, 0, 700, 600)

        # Создание фонового изображения окна начало
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("qwerty/menu.jpg"))
        self.background.setGeometry(0, 0, 700, 600)
        self.background.setScaledContents(True)

        # Создание кнопки назад в окне начало
        self.back = QPushButton('Назад', self)
        self.back.setGeometry(40, 520, 150, 50)
        self.back.setStyleSheet("font: 75 italic 24pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.back.clicked.connect(lambda: self.back_open(second_window))

        # Создание кнопки уровень легкий в окне начало
        self.level1 = QPushButton('Легкий', self)
        self.level1.setGeometry(80, 100, 150, 50)
        self.level1.setStyleSheet("font: 75 italic 20pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.level1.clicked.connect(self.open3_window)

        # Создание кнопки уровень средний в окне начало
        self.level2 = QPushButton('Средний', self)
        self.level2.setGeometry(280, 100, 150, 50)
        self.level2.setStyleSheet("font: 75 italic 20pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.level2.clicked.connect(self.open4_window)

        # Создание кнопки уровень сложный в окне начало
        self.level3 = QPushButton('Сложный', self)
        self.level3.setGeometry(480, 100, 150, 50)
        self.level3.setStyleSheet("font: 75 italic 20pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.level3.clicked.connect(self.open5_window)

    def back_open(self, first_window):
        first_window.show()
        self.close()

    # Создание окна уровень 1
    def open3_window(self):
        self.hide()
        self.level_window.show()

    # Создание окна уровень 2
    def open4_window(self):
        self.hide()
        self.level1_window.show()

    # Создание окна уровень 3
    def open5_window(self):
        self.hide()
        self.level2_window.show()

    # Уровень 1


class ThreeWindow(QMainWindow):
    def __init__(self, level_window):
        super().__init__()
        self.setWindowTitle('Sudoky')
        self.setGeometry(0, 0, 700, 600)

        # Создание фонового изображения окна уровень 1
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("qwerty/menu.jpg"))
        self.background.setGeometry(0, 0, 700, 600)
        self.background.setScaledContents(True)

        # Кнопка проверки
        self.proverka = QPushButton('Проверка', self)
        self.proverka.setGeometry(40, 200, 180, 50)
        self.proverka.setStyleSheet("font: 75 italic 20pt \"Arial\";\n""color:rgb(0, 0, 0);")

        # Кнопка назад на уровень 1
        self.back1 = QPushButton('Назад', self)
        self.back1.setGeometry(5, 5, 150, 50)
        self.back1.setStyleSheet("font: 75 italic 20pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.back1.clicked.connect(lambda: self.back_open(level_window))

        self.sudoku_board = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.sudoku_board[i][j] = QLineEdit(self)
                self.sudoku_board[i][j].setGeometry(300 + j * 40, 120 + i * 40, 40, 40)
                self.sudoku_board[i][j].setAlignment(Qt.AlignCenter)
                self.sudoku_board[i][j].setValidator(QIntValidator(1, 9))  # Ограничение на ввод чисел от 1 до 9

        # Добавление надписи над полем
        self.Main_nadpis2 = QLabel(self)
        self.Main_nadpis2.setText("Уровень: легкий")
        self.Main_nadpis2.setStyleSheet("font: 75 italic 25pt \"Arial\";\n" "color: rgb(255, 255, 255);")
        self.Main_nadpis2.setGeometry(320, 40, 400, 100)

    # Кнопка назад на окне уровень 1
    def back_open(self, level_windows):
        level_windows.show()
        self.close()

    # Уровень 2


class FourWindow(QMainWindow):
    def __init__(self, level1_windows):
        super().__init__()
        self.setWindowTitle('Sudoky')
        self.setGeometry(0, 0, 700, 600)

        # Создание фонового изображения окна уровень 2
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("qwerty/menu.jpg"))
        self.background.setGeometry(0, 0, 700, 600)
        self.background.setScaledContents(True)

        # Создание кнопки назад на окне уровень 2
        self.back2 = QPushButton('Назад', self)
        self.back2.setGeometry(5, 5, 150, 50)
        self.back2.setStyleSheet("font: 75 italic 20pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.back2.clicked.connect(lambda: self.back_open(level1_windows))

        self.back3 = QPushButton('Проверка', self)
        self.back3.setGeometry(40, 200, 180, 50)
        self.back3.setStyleSheet("font: 75 italic 20pt \"Arial\";\n""color:rgb(0, 0, 0);")

        self.sudoku_board = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.sudoku_board[i][j] = QLineEdit(self)
                self.sudoku_board[i][j].setGeometry(300 + j * 40, 120 + i * 40, 40, 40)
                self.sudoku_board[i][j].setAlignment(Qt.AlignCenter)
                self.sudoku_board[i][j].setValidator(QIntValidator(1, 9))  # Ограничение на ввод чисел от 1 до 9

                if random.random() < 0.4:
                    random_number = random.randint(1, 9)
                    self.sudoku_board[i][j].setText(str(random_number))

        self.Main_nadpis3 = QLabel(self)
        self.Main_nadpis3.setText("Уровень: средний")
        self.Main_nadpis3.setStyleSheet("font: 75 italic 25pt \"Arial\";\n" "color: rgb(255, 255, 255);")
        self.Main_nadpis3.setGeometry(320, 40, 400, 100)

    # Кнопка назад на окне уровень 2
    def back_open(self, level1_windows):
        level1_windows.show()
        self.close()

    # Уровень 3


class FiveWindow(QMainWindow):
    def __init__(self, level2_window):
        super().__init__()
        self.sudoku_board = None
        self.setWindowTitle('Sudoky')
        self.setGeometry(0, 0, 700, 600)

        # Создание фонового изображения окна уровень 3
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("qwerty/menu.jpg"))
        self.background.setGeometry(0, 0, 700, 600)
        self.background.setScaledContents(True)

        # Кнопка назад на окне уровень 3
        self.back3 = QPushButton('Назад', self)
        self.back3.setGeometry(5, 5, 150, 50)
        self.back3.setStyleSheet("font: 75 italic 20pt \"Arial\";\n""color:rgb(0, 0, 0);")
        self.back3.clicked.connect(lambda: self.back_open1(level2_window))

        self.back3 = QPushButton('Проверка', self)
        self.back3.setGeometry(40, 200, 180, 50)
        self.back3.setStyleSheet("font: 75 italic 20pt \"Arial\";\n""color:rgb(0, 0, 0);")

        self.sudoku_board = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.sudoku_board[i][j] = QLineEdit(self)
                self.sudoku_board[i][j].setGeometry(300 + j * 40, 120 + i * 40, 40, 40)
                self.sudoku_board[i][j].setAlignment(Qt.AlignCenter)
                self.sudoku_board[i][j].setValidator(QIntValidator(1, 9))  # Ограничение на ввод чисел от 1 до 9

                if random.random() < 0.3:
                    random_number = random.randint(1, 9)
                    self.sudoku_board[i][j].setText(str(random_number))

                self.Main_nadpis4 = QLabel(self)
                self.Main_nadpis4.setText("Уровень: сложный")
                self.Main_nadpis4.setStyleSheet("font: 75 italic 25pt \"Arial\";\n" "color: rgb(255, 255, 255);")
                self.Main_nadpis4.setGeometry(320, 40, 400, 100)

                # Кнопка назад на уровень 3

    def back_open1(self, level2_windows):
        level2_windows.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = sudoky()
    main_window.show()
    sys.exit(app.exec_())
