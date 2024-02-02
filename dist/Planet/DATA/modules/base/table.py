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


class Table:
    def __init__(self, game):
        self.game = game

        self.out = []

        self.font = pygame.font.Font(BASE_FONT, 20)

        self.hards = {
            "1": "easy",
            "2": "normal",
            "3": "hard"
        }

    def init(self):
        for stats in self.game.stats.game_stats:
            if stats["win"] == 1:
                time = stats["time"] // 60
                second = round(time % 60)
                minute = round(time // 60 % 60)

                t = stats["rtime"]
                data = ".".join(t[0].replace("-", " ").split()[::-1])
                time = t[1][:5]

                self.out.append([
                    stats["moves"],
                    translate.translate(self.hards[str(stats["difficult"])]),
                    f"{minute}m {second}s",
                    [data, time]
                ])

    def rect(self, color, x, y):
        pygame.draw.rect(self.game.screen, color, (x, y, 600, 50), 1)
        for i in range(3):
            pygame.draw.line(self.game.screen, color, (x + 150 * (i + 1), y), (x + 150 * (i + 1), y + 50))

    def draw(self):
        font_color = self.game.cash["menues"][self.game.couple]["font_color"]
        button_color = self.game.cash["menues"][self.game.couple]["button_color"][2]

        o = [
            translate.translate("Moves"),
            translate.translate("Difficult"),
            translate.translate("Game time"),
            translate.translate("Date")
        ]

        x = 200
        y = 100

        self.rect(button_color, x, y)

        for j in range(4):
            TextBox(
                self.game, x + (j * 150), y, 150, 50, f"{o[j]}", self.font,
                font_color=font_color
            ).draw()

        for i in range(len(self.out)):
            y += 50

            self.rect(button_color, x, y - i - 1)

            for j in range(4):
                if j == 3:
                    for k in range(2):
                        TextBox(
                            self.game, x + (j * 150), y + k * 25, 150, 25, f"{self.out[i][j][k]}", self.font,
                            font_color=font_color
                        ).draw()

                else:
                    TextBox(
                        self.game, x + (j * 150), y, 150, 50, f"{self.out[i][j]}", self.font,
                        font_color=font_color
                    ).draw()
