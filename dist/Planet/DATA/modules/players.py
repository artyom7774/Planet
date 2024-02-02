from DATA.modules.player import Player

from DATA.modules.functions import Functions
from DATA.modules.base.alpha_rect import alpha_rect
from DATA.modules.base.print_text import print_text

from DATA.modules.variables import *
import pygame
import random


class Players:
    sprites = [
        [
            pygame.image.load("DATA/files/sprites/player/game/1.png"),
            pygame.image.load("DATA/files/sprites/player/avatars/1.png")
        ],
        [
            pygame.image.load("DATA/files/sprites/player/game/2.png"),
            pygame.image.load("DATA/files/sprites/player/avatars/2.png")
        ],
        [
            pygame.image.load("DATA/files/sprites/player/game/3.png"),
            pygame.image.load("DATA/files/sprites/player/avatars/3.png")
        ],
        [
            pygame.image.load("DATA/files/sprites/player/game/4.png"),
            pygame.image.load("DATA/files/sprites/player/avatars/4.png")
        ]
    ]

    def __init__(self, game):
        self.game = game

        avatar = [0, 1, 2, 3]
        random.shuffle(avatar)

        names = [i for i in range(len(PLAYERS_NAMES))]
        random.shuffle(names)

        self.players = [
            Player(self.game, 0, 0, self.sprites[avatar[0]], PLAYERS_NAMES[names[0]]),
            Player(self.game, 11, 0, self.sprites[avatar[1]], PLAYERS_NAMES[names[1]]),
            Player(self.game, 11, 11, self.sprites[avatar[2]], PLAYERS_NAMES[names[2]]),
            Player(self.game, 0, 11, self.sprites[avatar[3]], PLAYERS_NAMES[names[3]]),
        ]

        self.active_circle = {
            "color": (44, 72, 108),
            "radius": {
                "max": 35,
                "now": 0
            }
        }

        self.turn = 0
        self.step = 0

        self.get_go = random.randint(1, 6)
        self.get_attack = random.randint(1, 3)

        Functions.create_go_dice(self.game, self.get_go)

    def get_pos(self, dx, dy):
        return [self.players[self.turn].x * CELLSIZE + dx, self.players[self.turn].y * CELLSIZE + dy]

    def next_tern(self):
        self.step = 0

        if self.turn == len(self.players) - 1:
            self.turn = 0
        else:
            self.turn += 1

        self.game.play_inventory_buttons["use_button"] = None

        var = 0
        while self.players[self.turn].health["now"] <= 0 and var < 4:
            self.turn += 1

            if self.turn > len(self.players) - 1:
                self.turn = 0

            var += 1

        self.get_go = random.randint(1, 6)

        Functions.create_go_dice(self.game, self.get_go)

    def update(self, x, y):
        if not self.players[self.turn].update(x, y, self.step):
            return 0

        self.game.mcd = MOUSE_COLDDOWN

        self.step -= 1

        if self.players[self.turn].now == "attack":
            self.step = -1

        if self.step == 0:
            self.next_tern()

    def draw(self):
        for i, player in enumerate(self.players):
            self.game.screen.blit(player.get(), (player.x * CELLSIZE, player.y * CELLSIZE))

            pygame.draw.rect(self.game.screen, BG_COLOR, (601, 1 + i * 100, 398, 100))

            # avatar
            print_text(self.game.screen, 702, 1 + i * 100, player.name, 20, font_color=AV_COLOR)
            pygame.draw.rect(self.game.screen, AV_COLOR, (603, 3 + i * 100, 96, 96))
            if i == self.turn:
                alpha_rect(self.game.screen, 96, 96, 603, 3 + i * 100, (80, 125, 181, 120))

            self.game.screen.blit(player.sprite[1], (602, 2 + i * 100))

            for j in range(5):
                pygame.draw.rect(self.game.screen, AV_COLOR, (702 + j * 53, 49 + i * 100, 50, 50))

            for j, item in enumerate(player.inventory):
                self.game.screen.blit(self.game.cash["cells"][item]["sprite"], (702 + j * 53, 49 + i * 100))

            for j in range(player.health["now"]):
                self.game.screen.blit(
                    self.game.cash["sprites"]["player"]["health"][0],
                    (797 + j * 34, 3 + i * 100)
                )

            if player.health["now"] > 0:
                for j in range(player.health["now"], player.health["max"]):
                    self.game.screen.blit(
                        self.game.cash["sprites"]["player"]["health"][1],
                        (797 + j * 34, 3 + i * 100)
                    )

            else:
                self.game.screen.blit(self.game.cash["sprites"]["died"], (601, 1 + i * 100))

            if i == self.turn:
                for j in range(self.step):
                    self.game.screen.blit(self.game.cash["sprites"]["step"], (701 + j * 10, 22 + i * 100))

        pygame.draw.circle(
            self.game.screen,
            self.active_circle["color"],
            self.get_pos(25, 25),
            self.active_circle["radius"]["now"],
            2
        )

        if any([player.now == "attack" and not player.was_killed for player in self.players]) and not self.game.cash["dices"]["draw"]:
            self.get_attack = random.randint(1, 3)
            Functions.create_attack_dice(self.game, self.get_attack)
