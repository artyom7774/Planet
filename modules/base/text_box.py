from DATA.modules.base.print_text import print_text
from DATA.modules.variables import *
from PIL import ImageFont


class TextBox:
    def __init__(self, game, x, y, width, height, text, font_size=20, font_type=BASE_FONT, font_color=FRAME_COLOR, type="center"):
        self.game = game

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

        if self.type == "center":
            self.tx = self.width / 2 - self.ttf.getbbox(self.text)[2] / 2

        elif self.type == "left":
            self.tx = 0

        elif self.type == "right":
            self.tx = self.width - self.ttf.getbbox(self.text)[2]

        self.ty = self.height / 2 - self.ttf.getbbox(self.text + "AgАр")[3] / 2

        print_text(self.game.screen, x + self.tx, y + self.ty, self.text, self.font_size, self.font_type, self.font_color)
