from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import choice , shuffle
from time import sleep
app = QApplication([]) #сторюємо віконний додаток

from window import * 
from menu import *


class Question():
    current = None
    count_ans = 0
    count_right_ans = 0

    def __init__(self, text , right_ans, ans2 , ans3 , ans5
                 ):
        self.text = text
        self.right_ans = right_ans
        self.text = text
        self.ans2 = ans2
        self.ans3 = ans3
        self.ans5 = ans5
       


questions = [
    Question("два", "two","nine"," twos"," tvo"),
    Question("один", "one","ohe"," nega"," nifne"),
    Question("сім", "seven","eibt"," fara"," nigne"),
    Question("Вісім", "eight","egith"," zero"," nihne"),
    Question("девять", "nine","niger"," hani"," vanki"),

]
radio_list = [btn1 , btn2 , btn3 ,  btn4]
win = QWidget() # створємо вікно
win.resize(600, 600)
win.setWindowTitle("Memory Card")
win.setLayout(main_line)

def Next_Question():
    Question.current = choice(questions)
    question_lb.setText(Question.current.text)
    shuffle(radio_list)
    radio_list[0].setText(Question.current.right_ans)
    radio_list[1].setText(Question.current.ans2)
    radio_list[2].setText(Question.current.ans3)
    radio_list[3].setText(Question.current.ans5)


def check_answer():
    Question.count_ans += 1
    if radio_list[0].isChecked():
        Question.count_right_ans += 1
        result_text.setText("Правельно")
    else:
        result_text.setText("Неправельно")
    
    radio_group.setExclusive(False)
    for btn in radio_list:
        btn.setChecked(False)
    radio_group.setExclusive(True)





def asnwer_click():
    if answer_btn.text() == "Відповісти":
        if radio_group.checkedButton():
            group_box.hide()
            check_answer()
            result_box.show()
            answer_btn.setText("Наступне питання")
    else:
        Next_Question()
        group_box.show()
        result_box.hide()
        answer_btn.setText("Відповісти")

def show_menu():
    count_lb.setText("Разів відповіли " + str(Question.count_ans))
    right_lb.setText("Правельній відповідей" + str(Question.count_right_ans))
    try:
        succes =  round(Question.count_right_ans/ Question.count_ans * 100 , 2)
    except:
        succes = 0
    succes_lb.setText("Успішність" + str(succes))
    win.hide()
    menu_win.show()

def hide_menu():
    win.show()
    menu_win.hide()
        
def relaks():
    paus_time = int(time_spin.value()) *60
    win.hide()
    sleep(paus_time)
    time_lb()
answer_btn.clicked.connect(asnwer_click)
menu_btn.clicked.connect(show_menu)
black_btn.clicked.connect(hide_menu)
rest_btn.clicked.connect(relaks)

# вкінці
Next_Question()
win.show() #показує вікно
app.exec_() # запускаємо додаток