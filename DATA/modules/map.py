from DATA.modules.base.path_find import AlgorithmPathFound

import random


class Map:
    def __init__(self, game):
        self.game = game

        self.width = 12
        self.height = 12

        self.ship_complite = 0
        self.game_complite = False

        self.map = [[dict(self.game.cash["cells"]["null"]) for _ in range(self.height)] for _ in range(self.width)]

    def generate(self):
        self.ship_complite = 0

        for i in range(self.height):
            for j in range(self.width):
                self.map[j][i]["visible"] = False

        self.map[0][0] = self.game.cash["cells"]["start"]
        self.map[0][self.height - 1] = self.game.cash["cells"]["start"]
        self.map[self.width - 1][self.height - 1] = self.game.cash["cells"]["start"]
        self.map[self.width - 1][0] = self.game.cash["cells"]["start"]

        for cell in self.game.cash["cells"].values():
            for _ in range(cell["count"]):
                i = random.randrange(self.width)
                j = random.randrange(self.height)

                while self.map[i][j]["name"] != "null":
                    i = random.randrange(self.width)
                    j = random.randrange(self.height)

                self.map[i][j] = dict(cell)

    def scrap(self, inventory):
        while len(inventory) > 0:
            rx = random.randint(0, 11)
            ry = random.randint(0, 11)

            while 11 >= rx >= 0 and 11 >= ry >= 0 and self.map[rx][ry]["name"] != "null":
                rx = random.randint(0, 11)
                ry = random.randint(0, 11)

            if self.map[rx][ry]["visible"]:
                self.map[rx][ry] = dict(self.game.cash["cells"][inventory[0]])
                self.map[rx][ry]["visible"] = True

            else:
                self.map[rx][ry] = dict(self.game.cash["cells"][inventory[0]])
                self.map[rx][ry]["visible"] = False

            inventory.pop(0)

    def out(self, px, py):
        map = [[0 for _ in range(self.height)] for _ in range(self.width)]

        fx = 0
        fy = 0

        for i in range(self.height):
            for j in range(self.width):
                if self.map[j][i]["tag"].find("e") != -1:
                    map[j][i] = -1

                if self.map[j][i]["name"] == "ship":
                    fx, fy = i, j

        for player in self.game.players.players:
            if player.was_killed:
                continue

            if player.x == px and player.y == py:
                continue

            alg = AlgorithmPathFound(map, player.y, player.x, fx, fy)

            for element in alg.start():
                player.move_list.append([*element, "time"])
