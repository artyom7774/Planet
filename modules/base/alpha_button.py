from DATA.modules.variables import *
import pygame


class AlphaButton:
    def __init__(self, game, x, y, width, height, action):
        self.game = game

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.action = action

    def draw(self, x=None, y=None):
        if x is None:
            x = self.x

        if y is None:
            y = self.y

        click = pygame.mouse.get_pressed()

        if x <= self.game.mouse[0] <= x + self.width:
            if y <= self.game.mouse[1] <= y + self.height:
                if click[0] and self.game.mcd <= 0:
                    if self.action is not None:
                        self.game.mcd = MOUSE_COLDDOWN

                        self.action()

                    return True

        return False
