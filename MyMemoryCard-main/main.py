from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import choice , shuffle
app = QApplication([]) #сторюємо віконний додаток

from window import * 

class Question():
    current = None

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






def asnwer_click():
    if answer_btn.text() == "Відповісти":
        group_box.hide()
        result_box.show()
        answer_btn.setText("Наступне питання")
    else:
        Next_Question()
        group_box.show()
        result_box.hide()
        answer_btn.setText("Відповісти")
        

answer_btn.clicked.connect(asnwer_click)

# вкінці
Next_Question()
win.show() #показує вікно
app.exec_() # запускаємо додаток