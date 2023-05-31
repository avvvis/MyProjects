from tkinter import *
from quiz_brain import QuizBrain
from question_model import Question
from time import sleep


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.q_text = self.quiz.next_question()

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        self.question = Canvas(self.window, bg="white", height=250, width=300)
        self.question.grid(row=1, column=0, columnspan=2, pady=(20, 20))
        self.question_text = self.question.create_text(150, 125, text=self.q_text, fill=THEME_COLOR,
                                                       font=("Arial", 15, "italic"), width=260)

        self.score = 0
        self.score_count = Label(self.window, text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_count.configure(font=("Arial", 10, "bold"))
        self.score_count.grid(row=0, column=1, pady=(20, 20))

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(self.window, image=self.true_image, highlightthickness=0,
                                  command=lambda: self.check_answer("true"))
        self.true_button.grid(row=2, column=0, pady=(20, 20))

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(self.window, image=self.false_image, highlightthickness=0,
                                   command=lambda: self.check_answer("false"))
        self.false_button.grid(row=2, column=1, pady=(20, 20))

        self.window.mainloop()

    def check_answer(self, ans):
        result = self.quiz.check_answer(ans)
        if result == 1:
            self.score += 1
            self.score_count.configure(text=f"score: {self.score}")
            self.flash_green()

        else:
            self.flash_red()

    def get_next_question(self):
        self.question.configure(bg="white")
        if self.quiz.still_has_questions():
            self.q_text = self.quiz.next_question()
            self.question.itemconfig(self.question_text, text=self.q_text)
        else:
            self.question.itemconfig(self.question_text, text="You've reached the end of the quiz !")
            self.false_button.config(state="disable")
            self.true_button.config(state="disable")

    def flash_green(self):
        self.question.configure(bg="green")
        self.window.after(1000, self.get_next_question)

    def flash_red(self):
        self.question.configure(bg="red")
        self.window.after(1000, self.get_next_question)




