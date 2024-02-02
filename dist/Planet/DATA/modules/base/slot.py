from DATA.modules.functions import *

from DATA.modules.base.text_field import TextField
from DATA.modules.base.button import Button

from PIL import ImageFont

from DATA.modules.variables import *

import pygame


class TextBox:
    def __init__(self, game, x, y, width, height, text, font, font_size=20, font_type=BASE_FONT, font_color=FRAME_COLOR, type="center"):
        self.game = game

        self.font = font

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.text = text

        self.font_size = font_size
        self.font_color = font_color
        self.font_type = font_type

        self.type = type

        self.ttf = None

        self.tx = 0
        self.ty = 0

        self.init()

    def init(self):
        self.ttf = ImageFont.truetype(self.font_type, self.font_size)

        if self.type == "center":
            self.tx = self.width / 2 - self.ttf.getbbox(self.text)[2] / 2

        elif self.type == "left":
            self.tx = 0

        elif self.type == "right":
            self.tx = self.width - self.ttf.getbbox(self.text)[2]

        self.ty = self.height / 2 - self.ttf.getbbox(self.text + "AgАр")[3] / 2

    def draw(self, x=None, y=None):
        if x is None:
            x = self.x

        if y is None:
            y = self.y

        self.ty = self.height / 2 - self.ttf.getbbox(self.text + "AgАр")[3] / 2

        text = self.font.render(self.text, True, self.font_color)
        self.game.screen.blit(text, (x + self.tx, y + self.ty))


class Slot:
    def __init__(self, game, font, x, y, image, stats):
        self.game = game

        self.font = font

        self.x = x
        self.y = y

        self.color = self.game.cash["menues"][self.game.couple]["button_color"]

        self.image = image

        self.stats = stats

        self.name = stats["name"]
        self.cost = stats["cost"]
        self.on = stats["on"]

        self.button = Button(
            self.game, self.x, self.y + 99, 275, 50, [], lambda: Functions.func_spec_shop_buy(self.game, self), self.color,
            TextBox(self.game, self.x, self.y + 99, 250, 50, translate.translate("Buy"), self.font, font_color=self.color[2])
        )

        self.text = None

        self.init()

    def init(self):
        for element in self.game.stats.upgrades:
            if element["name"] == self.name:
                count = element["count"]
                break

        else:
            count = 0

        self.text = TextField(
            self.game, self.x + 102, self.y + 2, 300, 100, font_color=self.color[2], font_size=19,
            text=f"""
            {translate.translate("cost")}: {self.cost}
            /n {translate.translate("buy")}: {self.on}
            /n 
            /n 
            /n {translate.translate("buyed")}: {count}
            """
        )

    def draw(self):
        pygame.draw.rect(self.game.screen, self.color[2], (self.x, self.y, 275, 149), 1)
        pygame.draw.rect(self.game.screen, self.color[2], (self.x, self.y, 100, 100), 1)

        if self.image is not None:
            self.game.screen.blit(self.image, (self.x, self.y))

        self.button.draw()
        self.text.draw()
