from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QRadioButton, QButtonGroup, QGroupBox, QSpinBox, QHBoxLayout, QWidget, QPushButton, QLabel, QVBoxLayout


menu_win = QWidget()
menu_win.setWindowTitle("Memori Card")
menu_win.resize(400,200)
menu_win.move(200,200)

title_lb = QLabel("Статистика")
count_lb = QLabel("Разів Відповіли")
right_lb = QLabel("Правельних Відовідей")
succes_lb = QLabel("Успишність")

black_btn = QPushButton("Назад")

V_line = QVBoxLayout()
V_line.addWidget(title_lb)
V_line.addWidget(count_lb)
V_line.addWidget(right_lb)
V_line.addWidget(succes_lb)
V_line.addWidget(black_btn)

menu_win.setLayout(V_line)