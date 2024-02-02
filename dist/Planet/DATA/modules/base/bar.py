from DATA.modules.base.print_text import print_text

from DATA.modules.variables import *

from PIL import ImageFont
import pygame


class Bar:
    def __init__(self, game, x, y, width, height, color, rama_color, font_size=20, font_type=BASE_FONT, font_color=(0, 0, 0)):
        self.game = game

        self.x = x
        self.y = y

        self.width = width - 2
        self.height = height

        self.color = color

        self.rama_color = rama_color

        self.font_size = font_size
        self.font_type = font_type
        self.font_color = font_color

        self.ttf = ImageFont.truetype(self.font_type, self.font_size)

    def draw(self, text, dnow, dmax, x=None, y=None):
        if x is None:
            x = self.x

        if y is None:
            y = self.y

        if text == "":
            tx = 0
            ty = 0
        
        else:
            tx = (self.width / 2) - self.ttf.getbbox(text)[2] / 2
            ty = (self.height / 2) - self.ttf.getbbox(text)[3] / 2

        d = (min(dnow, dmax) / dmax) * self.width

        pygame.draw.rect(self.game.surface, self.rama_color, (x, y, self.width + 2, self.height), 1)

        pygame.draw.rect(
            self.game.surface, self.color,
            (x + 1, y + 1, d, self.height - 2)
        )

        print_text(
            self.game.screen, x + tx, y + ty,
            text, self.font_size, self.font_type, self.font_color
        )
