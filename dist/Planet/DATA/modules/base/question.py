from DATA.modules.base.text_field import TextField
from DATA.modules.base.text_box import TextBox
from DATA.modules.base.button import Button
from DATA.modules.base.bar import Bar

from DATA.modules.functions import Functions

from DATA.modules.variables import *
import random


class Question:
    def __init__(self, game, quiz, task):
        self.game = game
        self.quiz = quiz

        self.task = task

        self.answers = []

        self.buttons = []
        self.texts = []

        self.stime = 0
        self.time = 0

        self.get_answer = False
        self.get_answer_number = -1
        self.get_answer_cd = 0

        self.init()

    def ans(self, number):
        if not self.get_answer:
            self.get_answer = True
            self.get_answer_number = number

            for i, element in enumerate(self.task["answers"]):
                if element["answer"] and i == self.get_answer_number:
                    self.quiz.get.append(round(GET_MONEY_QUIZ * (self.time / self.stime)))

                    break

            else:
                self.quiz.get.append(0)

    def init(self):
        font_color = self.game.cash["menues"][self.game.couple]["font_color"]
        button_color = self.game.cash["menues"][self.game.couple]["button_color"]

        self.answers = self.task["answers"]
        random.shuffle(self.answers)

        self.stime = self.task["time"] * 60
        self.time = self.task["time"] * 60

        self.buttons = [
            Button(
                self.game, 50, 200, 400, 150, [], lambda: self.ans(0), button_color,
                text_box=TextBox(self.game, 50, 200, 400, 150, self.task["answers"][0]["text"], font_size=30, font_color=font_color)
            ),

            Button(
                self.game, 550, 200, 400, 150, [], lambda: self.ans(1), button_color,
                text_box=TextBox(self.game, 550, 200, 400, 150, self.task["answers"][1]["text"], font_size=30, font_color=font_color)
            ),

            Button(
                self.game, 50, 400, 400, 150, [], lambda: self.ans(2), button_color,
                text_box=TextBox(self.game, 50, 400, 400, 150, self.task["answers"][2]["text"], font_size=30, font_color=font_color)
            ),

            Button(
                self.game, 550, 400, 400, 150, [], lambda: self.ans(3), button_color,
                text_box=TextBox(self.game, 550, 400, 400, 150, self.task["answers"][3]["text"], font_size=30, font_color=font_color)
            )
        ]

        self.texts = [
            TextField(
                self.game, 50, 20, WIDTH - 100, 60 + 25, self.task["question"], font_color=font_color
            )
        ]

    def draw(self):
        for button in self.buttons:
            button.draw()

        for text in self.texts:
            text.draw()

        Bar(self.game, 50, 150, WIDTH - 100, 25, (255, 0, 0), self.game.cash["menues"][self.game.couple]["font_color"]).draw("", self.time, self.stime)

        if self.get_answer:
            self.get_answer_cd += 1

            self.buttons[self.get_answer_number].rama_color = (255, 0, 0)

            for i, element in enumerate(self.task["answers"]):
                if element["answer"]:
                    self.buttons[i].rama_color = (0, 255, 0)

            TextBox(self.game, 0, 550, WIDTH, 50, translate.translate("Your get: ") + str(round(self.quiz.get[self.quiz.now])), font_color=self.game.cash["menues"][self.game.couple]["font_color"]).draw()

        else:
            self.time -= 1

        if self.time <= 0:
            self.get_answer = True
            self.get_answer_number = -1

            self.quiz.get.append(0)

        if self.get_answer_cd > 100:
            self.quiz.next()
