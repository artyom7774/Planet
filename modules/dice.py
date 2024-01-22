from DATA.modules.variables import *
import pygame


class Dice:
    def __init__(self, game, x, y, width, height, color, sprite, action, type):
        self.game = game

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.color = color

        self.using = True

        self.activate = False

        self.sprite = sprite
        self.action = action

        self.type = type

    def draw(self):
        self.game.screen.blit(self.game.cash["sprites"]["dices"][self.type]["null"], (self.x, self.y))

        if self.game.fpsc % 30 < 15 and not self.activate:
            self.game.screen.blit(self.game.cash["sprites"]["dices"][self.type]["0"], (self.x, self.y))

        click = pygame.mouse.get_pressed()

        if self.x <= self.game.mouse[0] <= self.x + self.width:
            if self.y <= self.game.mouse[1] <= self.y + self.height:
                if self.action is not None and click[0] and self.using and self.game.mcd < 0 and self.game.menu == "play":
                    self.game.mcd = MOUSE_COLDDOWN

                    self.activate = True
                    self.action()

        if self.activate:
            self.game.screen.blit(self.sprite, (self.x, self.y))
