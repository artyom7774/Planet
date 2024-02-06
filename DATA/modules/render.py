from DATA.modules.base.print_text import print_text
from DATA.modules.base.alpha_rect import alpha_rect
from DATA.modules.base.text_box import TextBox

from DATA.modules.variables import *
import pygame
import random


class Render:
    def __init__(self, game):
        self.game = game

    def play(self):
        if self.game.debug["draw_map"]:
            self.game.screen.blit(self.game.cash["sprites"]["map"], (-200, -200))

        alpha_rect(self.game.screen, WIDTH, HEIGHT, 0, 0, (0, 120, 0, 5))

        pygame.draw.rect(self.game.screen, BG_COLOR, (600, 0, 600, HEIGHT))

        for i in range(self.game.map.height):
            for j in range(self.game.map.width):
                if self.game.map.map[j][i]["visible"] or (self.game.cash["difficult"] == 3 and self.game.debug["hard_difficult_map_visiable"]):
                    if self.game.map.map[j][i]["name"] != "null" and self.game.map.map[j][i]["sprite"] is not None:
                        self.game.screen.blit(self.game.map.map[j][i]["sprite"], (j * CELLSIZE, i * CELLSIZE))

                    if self.game.map.map[j][i]["name"] == "ship" and self.game.map.ship_complite != 0:
                        self.game.screen.blit(self.game.cash["sprites"]["ship"][str(self.game.map.ship_complite)], (j * CELLSIZE + 1, i * CELLSIZE))

                else:
                    self.game.screen.blit(self.game.cash["sprites"]["cells"]["not_open"], (j * CELLSIZE - 25, i * CELLSIZE - 25))
                    # pygame.draw.rect(self.game.screen, FRAME_COLOR, (j * CELLSIZE, i * CELLSIZE, CELLSIZE, CELLSIZE))

        if self.game.debug["cells"]:
            for i in range(self.game.map.height):
                for j in range(self.game.map.width):
                    pygame.draw.rect(self.game.screen, BG_COLOR, (j * CELLSIZE, i * CELLSIZE, CELLSIZE, CELLSIZE), 1)

        self.game.players.draw()

        if self.game.cash["dices"]["draw"]:
            self.game.cash["dices"]["button"].draw()

        if self.game.cash["button"]["draw"]:
            self.game.cash["button"]["button"].draw()

        if self.game.play_menu_buttons["activate"] is not None:
            self.game.play_menu_buttons["back"].draw()

            pygame.draw.rect(self.game.screen, BG_COLOR, (603, 453, 361, 146))

            player = self.game.players.players[self.game.players.turn]

            if self.game.play_menu_buttons["activate"] == 0:
                for button in self.game.play_inventory_buttons["buttons"]:
                    button.draw()

                for button in self.game.play_inventory_buttons["use_buttons"]:
                    button.draw()

                print_text(self.game.screen, 702, 451, player.name, 20, font_color=AV_COLOR)
                pygame.draw.rect(self.game.screen, AV_COLOR, (603, 453, 96, 96))
                self.game.screen.blit(player.sprite[1], (602, 452))

                for j, item in enumerate(player.inventory):
                    self.game.screen.blit(self.game.cash["cells"][item]["sprite"], (702 + j * 53, 499))

                if self.game.play_inventory_buttons["active_button"] is not None:
                    alpha_rect(self.game.screen, 50, 50, 702 + self.game.play_inventory_buttons["active_button"] * 53, 499, (80, 125, 181, 100))

            if self.game.play_menu_buttons["activate"] == 1:
                pass

            if self.game.play_menu_buttons["activate"] == 2:
                for text in self.game.play_stats_buttons["text"]:
                    text.draw()

            if self.game.play_menu_buttons["activate"] == 3:
                for button in self.game.play_quit_buttons["buttons"]:
                    button.draw()

        else:
            for button in self.game.play_menu_buttons["buttons"]:
                button.draw()

        pygame.draw.rect(self.game.screen, AV_COLOR, (967, 3, 32, 596))

    def menu(self):
        self.draw_background()

        for button in self.game.menu_menu_buttons["buttons"]:
            button.draw()

        for text in self.game.menu_menu_buttons["text"]:
            text.draw()

    def choice_difficult(self):
        self.draw_background()

        for button in self.game.menu_choice_buttons["buttons"]:
            button.draw()

        for text in self.game.menu_choice_buttons["text"]:
            text.draw()

        self.game.menu_back_button.draw()

    def stats(self):
        self.draw_background()

        font_color = self.game.cash["menues"][self.game.couple]["font_color"]

        self.game.cash["stats_table"].draw()

        time = self.game.stats.time_in_game // 60

        hour = round(time // 3600 % 60)
        minute = round(time // 60 % 60)
        second = round(time % 60)

        TextBox(
            self.game, 205, 575, WIDTH, 25, translate.translate("Time in game") + ": " + f"{hour}h {minute}m {second}s",
            type="left", font_color=font_color
        ).draw()

        for text in self.game.menu_stats_buttons["text"]:
            text.draw()

        self.game.menu_back_button.draw()

    def menu_help(self):
        self.draw_background()

        for button in self.game.menu_help_menu_buttons["buttons"]:
            button.draw()

        for text in self.game.menu_help_menu_buttons["text"]:
            text.draw()

        self.game.menu_back_button.draw()

    def menu_shop(self):
        self.draw_background()

        for text in self.game.menu_shop_menu_buttons["text"]:
            text.draw()

        for button in self.game.menu_shop_menu_buttons["buttons"]:
            button.draw()

        self.game.menu_back_button.draw()

    def shop(self):
        self.draw_background()

        for text in self.game.menu_shop_buttons["text"]:
            text.draw()

        for shop in self.game.menu_shop_buttons["shop"]:
            shop.draw()

        self.game.menu_back_button.draw()

    def quiz(self):
        self.draw_background()

        for button in self.game.menu_quiz_buttons["buttons"]:
            button.draw()

        for text in self.game.menu_quiz_buttons["text"]:
            text.draw()

        if self.game.cash["internet_error_text"] is not None:
            self.game.cash["internet_error_text"]["text"].draw()
            self.game.cash["internet_error_text"]["live"] -= 1

            if self.game.cash["internet_error_text"]["live"] < 0:
                self.game.cash["internet_error_text"] = None

        self.game.menu_back_button.draw()

    def quiz_start(self):
        self.draw_background()

        for quiz in self.game.menu_quiz_start_buttons["quiz"]:
            quiz.draw()

    def quiz_end(self):
        self.draw_background()

        for text in self.game.menu_quiz_end_buttons["text"]:
            text.draw()

        TextBox(
            self.game, 250, 100, 500, 50,
            translate.translate("Your get: ") + str(round(sum(self.game.menu_quiz_start_buttons["quiz"][0].get))),
            font_color=self.game.cash["menues"][self.game.couple]["font_color"]
        ).draw()

        self.game.menu_back_button.draw()

    def history(self):
        self.draw_background()

        for button in self.game.menu_history_buttons["buttons"]:
            button.draw()

        for text in self.game.menu_history_buttons["text"]:
            text.draw()

    def help(self):
        self.draw_background()

        color = self.game.cash["menues"][self.game.couple]["font_color"]

        for button in self.game.menu_help_buttons["buttons"]:
            button.draw()

        self.game.menu_help_buttons["text"][abs(self.game.menu_help_buttons["path"]) % 4].draw()
        self.game.menu_help_buttons["text"][4].draw()

        pygame.draw.polygon(
            self.game.screen, color,
            [[155 + 650, 155], [195 + 650, 220], [155 + 650, 295]], 2
        )

        pygame.draw.polygon(
            self.game.screen, color,
            [[155 + 40, 155], [195 - 40, 220], [155 + 40, 295]], 2
        )

    def settings(self):
        self.draw_background()

        for button in self.game.menu_settings_buttons["buttons"]:
            button.draw()

        if self.game.cash["settings_confirm"]:
            TextBox(self.game, 200, 500, 600, 100, translate.translate("Request restarting!"), font_size=30, font_color=self.game.cash["menues"][self.game.couple]["font_color"]).draw()

        self.game.menu_back_button.draw()

    def game_win(self):
        self.draw_background()

        for button in self.game.menu_game_win_buttons["buttons"]:
            button.draw()

        for text in self.game.menu_game_win_buttons["text"]:
            text.draw()

        for st in self.game.stats.game_stats:
            if st["id"] == self.game.cash["game_id"]:
                stats = dict(st)

                break

        else:
            raise NameError("stats not found")

        time = stats["time"] // 60

        hour = round(time // 3600 % 60)
        minute = round(time // 60 % 60)
        second = round(time % 60)

        difficults = {
            "1": "easy",
            "2": "normal",
            "3": "hard"
        }

        difficult = difficults[str(stats["difficult"])]

        TextBox(
            self.game, 205, 110, 600, 20, translate.translate("Difficult") + ": " + translate.translate(difficult),
            font_size=20, font_color=self.game.cash["menues"][self.game.couple]["font_color"], type="left"
        ).draw()

        TextBox(
            self.game, 205, 160, 600, 20, translate.translate("Moves") + ": " + str(stats["moves"]),
            font_size=20, font_color=self.game.cash["menues"][self.game.couple]["font_color"], type="left"
        ).draw()

        TextBox(
            self.game, 205, 185, 600, 20, translate.translate("Time") + ": " + f"{hour}h {minute}m {second}s",
            font_size=20, font_color=self.game.cash["menues"][self.game.couple]["font_color"], type="left"
        ).draw()

    def game_over(self):
        self.draw_background()

        for button in self.game.menu_game_over_buttons["buttons"]:
            button.draw()

        for text in self.game.menu_game_over_buttons["text"]:
            text.draw()

    def authors(self):
        self.draw_background()

        for text in self.game.menu_authors_buttons["text"]:
            text.draw()

        self.game.menu_back_button.draw()

    def draw_background(self):
        self.game.screen.blit(self.game.cash["menues"][self.game.couple]["bg"], (0, 0))
        self.draw_menu()

        # pygame.draw.rect(self.game.screen, (255, 0, 0), (200, 0, 600, 600), 1)

        if self.game.debug["particles"]:
            if self.game.couple == "winter":
                self.game.particles.create(
                    random.randint(0, 1400), random.randint(-100, 0),
                    self.game.cash["menues"][self.game.couple]["snow_color"],
                    90, 8, random.randint(5, 7), 0.035
                )

    def draw_menu(self):
        alpha_rect(self.game.screen, WIDTH, HEIGHT, 0, 0, (0, 0, 0, 50))

    def render(self):
        self.game.screen.fill(BG_COLOR)

        if self.game.debug["fps"]:
            pygame.display.set_caption(str(round(self.game.clock.get_fps(), 1)))

        getattr(self, self.game.menu)()

        if self.game.settings["display_fps"] == "ON":
            print_text(self.game.screen, 0, 0, f"FPS: {round(self.game.clock.get_fps(), 1)}", 20, font_color=self.game.cash["menues"][self.game.couple]["font_color"])

        self.game.particles.draw()

        pygame.display.update()
