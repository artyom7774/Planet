from DATA.modules.functions import Functions

from DATA.modules.variables import *
import pygame


class Update:
    def __init__(self, game):
        self.game = game

    def update(self):
        self.game.mouse = list(pygame.mouse.get_pos())

        self.game.mouse[0] *= WIDTH / SYSTEM_WIDTH
        self.game.mouse[1] *= HEIGHT / SYSTEM_HEIGHT

        self.game.mouse[0] = round(self.game.mouse[0])
        self.game.mouse[1] = round(self.game.mouse[1])

        self.game.particles.update()

        self.game.mcd -= 1

        self.game.stats.update()

        self.game.play_stats_buttons["text"][0].text = translate.translate("Number of moves") + ": " + str(self.game.stats.moves)
        self.game.play_stats_buttons["text"][1].text = translate.translate("Money") + ": " + str(self.game.stats.money_for_game)

        for player in self.game.players.players:
            for last_step in player.last_steps:
                self.game.map.map[last_step[0]][last_step[1]]["visible"] = True

            player.move()

        if not self.game.cash["dices"]["button"].draw or self.game.cash["dices"]["button"].type != "attack":
            self.game.cash["button"]["draw"] = False

        self.game.cash["dices"]["live"] -= 1
        if self.game.cash["dices"]["live"] == 0:
            player = self.game.players.players[self.game.players.turn]

            self.game.cash["dices"]["draw"] = False

            if self.game.cash["dices"]["button"].type == "go":
                self.game.players.step = int(self.game.players.get_go)

            if self.game.cash["dices"]["button"].type == "attack":
                if self.game.players.get_attack == 1:
                    player.health["now"] -= 1

                    player.kill()

                if self.game.players.get_attack == 2:
                    for i in range(5):
                        if f"gun_{i + 1}" in player.inventory:
                            player.now = "go"

                            self.game.map.map[player.x][player.y] = self.game.cash["cells"]["null"]
                            self.game.players.next_tern()

                            player.inventory.remove(f"gun_{i + 1}")

                            self.game.stats.money_for_game += GET_MONEY_FOR_KILL

                            break

                if self.game.players.get_attack == 3:
                    player.now = "go"

                    player.x, player.y = player.last_steps[len(player.last_steps) - 1]

                    self.game.players.next_tern()

        for i in range(self.game.map.height):
            for j in range(self.game.map.width):
                if self.game.map.map[j][i]["name"] == "start":
                    self.game.map.map[j][i]["visible"] = True

                if self.game.debug["full_vision"]:
                    self.game.map.map[j][i]["visible"] = True

        if self.game.menu == "play":
            if all(player.was_killed for player in self.game.players.players):
                Functions.func_menu_game_over(self.game)

            if self.game.map.game_complite and all(len(player.move_list) == 0 for player in self.game.players.players):
                Functions.func_menu_game_win(self.game)

        if self.game.menu == "shop":
            if self.game.fpsc % 5 == 0:
                self.game.menu_shop_buttons["text"][1].text = translate.translate("Money") + ": " + str(self.game.stats.money)
                self.game.menu_shop_buttons["text"][1].init()

        if self.game.players.active_circle["radius"]["now"] <= 0:
            self.game.players.active_circle["radius"]["now"] = self.game.players.active_circle["radius"]["max"]
        else:
            self.game.players.active_circle["radius"]["now"] -= 1.5
