from DATA.modules.variables import *


from DATA.modules.base.print_text import print_text
from DATA.modules.variables import *
from PIL import ImageFont


class Player:
    def __init__(self, game, x, y, sprite, name):
        self.game = game

        self.now = "go"

        self.health = {
            "max": 5,
            "now": 3
        }

        self.last_steps = [[x, y]]

        self.was_killed = False

        self.name = name

        self.sprite = sprite

        for i, sprite in enumerate(self.sprite):
            self.sprite[i] = sprite.convert_alpha(self.game.surface)

        self.x = x
        self.y = y

        self.inventory = []
        self.move_list = []

    def add_item_inventory(self, x, y, already=False):
        if self.game.map.map[x][y]["tag"].find("g") != -1:
            if len(self.inventory) < 5:
                self.inventory.append(self.game.map.map[x][y]["name"])
                self.game.map.map[x][y] = self.game.cash["cells"]["null"]

            elif already:
                self.inventory.append(self.game.map.map[x][y]["name"])
                self.game.map.map[x][y] = self.game.cash["cells"]["null"]

            else:
                return 0

    def go(self):
        x = self.move_list[0][0]
        y = self.move_list[0][1]

        if not self.game.map.map[x][y]["visible"]:
            self.game.stats.money_for_game += GET_MONEY_FOR_OPEN_CELL

            self.game.map.map[x][y]["visible"] = True

        self.x = x
        self.y = y

        self.move_list.pop(0)

    def move(self):
        if len(self.move_list) > 0:
            if self.move_list[0][2] == "now":
                self.go()

            elif self.move_list[0][2] == "time":
                if self.game.fpsc % 20 == 0:
                    self.go()

            else:
                pass

    def update(self, x, y, step):
        tx = abs(self.x - x)
        ty = abs(self.y - y)

        for player in self.game.players.players:
            if player.x == x and player.y == y:
                return False

        if step == 0:
            return False

        if self.now == "attack":
            return False

        if not (tx <= 1 and ty <= 1 and (tx != 1 or ty != 1) and (tx != 0 or ty != 0)):
            return False

        self.add_item_inventory(x, y)

        self.last_steps.append([self.x, self.y])

        if not self.game.map.map[x][y]["visible"]:
            self.game.stats.money_for_game += GET_MONEY_FOR_OPEN_CELL

            self.game.map.map[x][y]["visible"] = True

        if self.game.map.map[x][y]["tag"].find("e") != -1:
            self.now = "attack"

        if self.game.map.map[x][y]["name"] == "ship":
            for element in self.inventory:
                if element == "fuel":
                    self.game.map.ship_complite += 1
                    self.inventory.remove(element)
                    break

                if element == "detail":
                    self.game.map.ship_complite += 1
                    self.inventory.remove(element)
                    break

            if self.game.map.ship_complite == COUNT_DETAILS:
                self.game.map.game_complite = True

                self.game.map.out(x, y)

            return False

        self.move_list.append([x, y, "now"])

        return True

    def kill(self):
        if self.health["now"] <= 0:
            self.was_killed = True

            self.game.map.scrap(self.inventory)

            self.game.players.next_tern()

    def get(self):
        return self.sprite[0]

    def draw(self):
        self.game.screen.blit(self.get(), (self.x * CELLSIZE, self.y * CELLSIZE))
