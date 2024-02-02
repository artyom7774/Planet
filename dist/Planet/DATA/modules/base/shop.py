from DATA.modules.base.slot import Slot

from DATA.modules.variables import *

import pygame


class Shop:
    def __init__(self, game, items):
        self.game = game

        self.items = items

        self.font = pygame.font.Font(BASE_FONT, 20)

        self.x = 200
        self.y = 100
        self.width = 500
        self.height = 400

        self.out = []

        self.init()

    def init(self):
        self.out = []

        for i, item in enumerate(self.items):
            self.out.append(
                Slot(
                    self.game, self.font, self.x + (i % 2 * 325), self.y + (i // 2 * 200),
                    item["image"], item
                )
            )

    def draw(self):
        for slot in self.out:
            slot.draw()
