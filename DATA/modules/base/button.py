from DATA.modules.base.alpha_rect import alpha_rect

from DATA.modules.variables import *
import pygame


class Button:
    def __init__(self, game, x, y, width, height, sprites, action, colors=None, text_box=None, types=None):
        if types is None:
            types = {}

        self.game = game

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.sprites = sprites
        self.text_box = text_box

        if colors is not None:
            self.rect_color = colors[0]
            self.input_color = colors[1]
            self.rama_color = colors[2]

        else:
            self.rect_color = AV_COLOR
            self.input_color = None
            self.rama_color = None

        self.action = action

        self.types = types

    def draw(self, x=None, y=None):
        if x is None:
            x = self.x

        if y is None:
            y = self.y

        if self.rect_color is not None:
            alpha_rect(self.game.screen, self.width, self.height, x, y, self.rect_color)

        for i, sprite in enumerate(self.sprites):
            if self.types.get(str(i)) is not None:
                if self.game.fpsc % self.types[str(i)][0] < self.types[str(i)][1]:
                    self.game.screen.blit(sprite, (x, y))

            else:
                self.game.screen.blit(sprite, (x, y))

        click = pygame.mouse.get_pressed()

        if x <= self.game.mouse[0] <= x + self.width:
            if y <= self.game.mouse[1] <= y + self.height:
                if self.input_color is not None:
                    alpha_rect(self.game.screen, self.width, self.height, x, y, self.input_color)

                if click[0]:
                    if self.game.mcd <= 0 and self.action is not None:
                        self.game.mcd = MOUSE_COLDDOWN

                        self.action()

        if self.rama_color is not None:
            pygame.draw.rect(self.game.screen, self.rama_color, (x, y, self.width, self.height), 1)

        if self.text_box is not None:
            self.text_box.draw(x=x, y=y)

