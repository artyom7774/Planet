from DATA.modules.variables import *

from PIL import ImageFont
import pygame


class TextField:
    """
    spec = {
        "scroll": {
            "add": int
        },

        "auto_spawn_text": {
            "step": int,
            "now": int
        }
    }

    """

    def __init__(self, game, x, y, width, height, text, font_size=20,
                 font_type=BASE_FONT, font_color=FRAME_COLOR, spec=None):

        if spec is None:
            self.spec = {}
        else:
            self.spec = spec

        self.game = game

        self.x = x
        self.y = y

        self.text = text

        self.font_size = font_size
        self.font_type = font_type
        self.font_color = font_color

        self.ttf = ImageFont.truetype(self.font_type, self.font_size)

        self.width = width
        self.height = height

        self.text = self.text.split()

        self.out = []

        self.hstep = self.ttf.getbbox("Ag")[3]
        self.wstep = 0

        while self.ttf.getbbox((self.wstep + 1) * "_")[2] < self.width:
            self.wstep += 1

        self.init()

    def init(self):
        l = 0
        r = len(self.text) - 1

        if self.text[0] == "/t":
            self.out = [" " * 3]

        else:
            self.out = [self.text[0]]

        while l < r:
            if len(self.out[len(self.out) - 1]) + len(self.text[l + 1]) + 1 < self.wstep:
                if self.text[l + 1] == "/n":
                    self.out.append("")

                elif self.text[l + 1] == "/t":
                    self.out[len(self.out) - 1] += " " * 4

                else:
                    if len(self.out[len(self.out) - 1]) == 0:
                        self.out[len(self.out) - 1] += f"{self.text[l + 1]}"

                    else:
                        self.out[len(self.out) - 1] += f" {self.text[l + 1]}"

                l += 1

            else:
                self.out.append("")

    def draw(self, x=None, y=None):
        if x is None:
            x = self.x

        if y is None:
            y = self.y

        if self.spec.get("auto_spawn_text") is not None:
            self.spec["auto_spawn_text"]["now"] += self.spec["auto_spawn_text"]["step"]

        font = pygame.font.Font(self.font_type, self.font_size)

        if self.spec.get("scroll") is not None:
            add = self.spec["scroll"]["add"]

        else:
            add = 0

        if self.spec.get("auto_spawn_text") is not None:
            step = self.spec["auto_spawn_text"]["now"]

        else:
            step = 10000000000000000000

        # print(self.out)

        now = 0
        for i, element in enumerate(self.out):
            if now + len(element) > step:
                if self.hstep * (i - add) <= self.height and i - add >= 0:
                    text = font.render(element[:round(step - now)], True, self.font_color)
                    self.game.screen.blit(text, (x, y + self.hstep * (i - add)))

                return 0

            else:
                if self.hstep * (i - add) <= self.height and i - add >= 0:
                    text = font.render(element, True, self.font_color)
                    self.game.screen.blit(text, (x, y + self.hstep * (i - add)))

            now += len(element)
