from DATA.modules.base.question import Question

import random
import json


class Quiz:
    def __init__(self, game):
        self.game = game

        self.questions = []
        self.class_questions = []

        self.get = []

        self.now = 0
        self.max_question = 1

    def init(self):
        self.questions = []
        self.class_questions = []

        self.get = []

        self.now = 0

        with open("DATA/files/files/quiz.json", "r", encoding="utf-8") as file:
            questions = list(json.load(file).values())

        self.max_question = 5

        random.shuffle(questions)

        for i in range(self.max_question):
            self.questions.append(questions[i])
            self.class_questions.append(
                Question(self.game, self, self.questions[i])
            )

            self.class_questions[i].init()

    def next(self):
        if self.now + 1 < self.max_question:
            self.now += 1

        else:
            self.game.stats.money += sum(self.get)
            self.game.menu = "quiz_end"

    def draw(self):
        self.class_questions[self.now].draw()
