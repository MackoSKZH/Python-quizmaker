from tkinter import *
from tkinter import messagebox as mb
import json

class Quiz:

    def __init__(self):
        self.q_no = 0
        self.font = "Comic Sans MS"
        # self.display_title()
        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.button()
        self.display_question()
        self.data_size = len(question)
        self.correct = 0
        self.wrong_count = 0

    def display_results(self):
        correct = f"correct: {self.correct}"
        wrong = f"wrong: {self.wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"score: {score}%"
        mb.showinfo("RESULTS:", f"{result}\n{correct}\n{wrong}")

    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            return True

        else:
            self.wrong_count += 1
            self.q_no += 1

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.q_no += 1
            self.correct += 1

        if self.q_no == self.data_size:
            self.display_results()
            win.destroy()

        self.display_question()
        self.display_options()

    def button(self):
        next_button = Button(win, text="Next", command=self.next_btn, bd=6,width=11, bg="white", fg="black", font=(self.font, 16, "bold"))
        next_button.place(x=350, y=WIDTH-120)

        quit_button = Button(win, text="Quit", command=win.destroy, width=5,bd=4, bg="red", fg="white", font=(self.font, 16, "bold"))
        quit_button.place(x=770, y=5)

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):
        q_no = Label(win, text=question[self.q_no], bg="black", justify='center',width=62, fg="white", font=(self.font, 16, "bold"))
        q_no.place(x=5, y=100)

    def display_title(self):
        title = Label(win, text="KVIZ", bg="black", fg="white",width=55, font=(self.font, 20, "bold"))
        title.place(x=0, y=2)

    def radio_buttons(self):
        q_list = []
        y_pos = 300
        while len(q_list) < 4:
            radio_btn = Radiobutton(win, text=" ", variable=self.opt_selected, bd=6,cursor="hand2", bg="white", value=len(q_list) + 1, font=(self.font, 25, "bold"))
            q_list.append(radio_btn)
            radio_btn.place(x=50, y=y_pos)
            y_pos += 80
        return q_list

WIDTH = 850
HEIGHT = 850

win = Tk()
win.title("KVIZ")
win.resizable(False, False)

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x = int((screen_width/2) - (WIDTH/2))
y = int((screen_height/2) - (HEIGHT/2))

win.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
win.config(background="black")

with open('./otazky.json', errors='ignore') as f:
    data = json.load(f)

question = (data['question'])
options = (data['options'])
answer = (data['answer'])

quiz = Quiz()
win.mainloop()