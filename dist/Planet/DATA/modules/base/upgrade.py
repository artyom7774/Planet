from DATA.modules.base.alpha_button import AlphaButton

import pygame


class Upgrade:
    def __init__(self, game, stats):
        self.game = game

        self.id, self.cost, self.dependencies, self.image, self.radius, self.x, self.y = list(stats.values())

        self.purchased = False

        self.color = self.game.cash["menues"][self.game.couple]["button_color"]

        self.button = AlphaButton(
            self.game, self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2, None
        )

    def init(self):
        for element in self.game.stats.skills:
            if element["id"] == self.id:
                self.purchased = True
                break

        else:
            self.purchased = False

    def draw(self):
        pygame.draw.circle(
            self.game.screen, self.color[2], (self.x, self.y), self.radius, 1
        )

        if self.image is not None:
            self.game.screen.blit(self.image, (self.x - self.radius, self.y - self.radius))

        self.button.draw()
