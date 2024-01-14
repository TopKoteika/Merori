from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QRadioButton, QButtonGroup, QGroupBox, QSpinBox, QHBoxLayout, QWidget, QPushButton, QLabel, QVBoxLayout

menu_btn = QPushButton("Меню")
rest_btn = QPushButton("Відпочити")

time_spin = QSpinBox()
time_spin.setValue(3)
time_lb = QLabel("хвилин")

row1 = QHBoxLayout()
row1.addWidget(menu_btn)
row1.addStretch(1)
row1.addWidget(rest_btn)
row1.addWidget(time_spin)
row1.addWidget(time_lb)

question_lb = QLabel("Питання")

btn1 = QRadioButton("варіант1")
btn2 = QRadioButton("варіант2")
btn3 = QRadioButton("варіант3")
btn4 = QRadioButton("варіант4")

row2 = QHBoxLayout()
radio_group = QButtonGroup()
radio_group.addButton(btn1)
radio_group.addButton(btn2)
radio_group.addButton(btn3)
radio_group.addButton(btn4)


group_box = QGroupBox("Варіанти перекладу")
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn1)
col1.addWidget(btn2)
col2.addWidget(btn3)
col2.addWidget(btn4)

row2.addLayout(col1)
row2.addLayout(col2)

group_box.setLayout(row2)
# ПАНЕЛЬ РЕЗУЛЬТАТУ
result_box = QGroupBox("Результат")
result_text = QLabel("Правильно")
right_answer_text = QLabel("відповідь")

result_line = QVBoxLayout()
result_line.addWidget(result_text)
result_line.addWidget(right_answer_text, alignment=Qt.AlignCenter, stretch=2)

result_box.setLayout(result_line)
result_box.hide()

answer_btn = QPushButton("Відповісти")

main_line = QVBoxLayout()
main_line.addLayout(row1, stretch = 1)
main_line.addWidget(question_lb, stretch = 2, alignment=Qt.AlignCenter)
main_line.addWidget(group_box, stretch = 6)
main_line.addWidget(result_box, stretch = 6)
main_line.addWidget(answer_btn, stretch = 3)
