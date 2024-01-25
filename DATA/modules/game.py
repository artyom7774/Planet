from DATA.modules.base.text_field import TextField
from DATA.modules.base.text_box import TextBox
from DATA.modules.base.button import Button

from DATA.modules.base.upgrade_map import UpgradeMap
from DATA.modules.base.shop import Shop

from DATA.modules.functions import Functions
from DATA.modules.particles import Particles
from DATA.modules.players import Players
from DATA.modules.render import Render
from DATA.modules.update import Update
from DATA.modules.map import Map

from DATA.modules.base.sound import Sound
from DATA.modules.init import init

from DATA.modules.variables import *

import pygame


class Stats:
    def __init__(self, game):
        self.game = game

        self.money_for_game = 0
        self.money = 0

        self.time_in_game = 0
        self.time_in_level = 0

        self.game_stats = []
        self.upgrades = []
        self.skills = []

        self.best_moves = None
        self.moves = 0

    def update(self):
        self.moves = sum([len(player.last_steps) for player in self.game.players.players]) - 4


class Game:
    version = "1.1.2 release"

    def __init__(self):
        pygame.init()

        self.couples = {
            "01": "winter",
            "02": "winter",
            "03": "spring",
            "04": "spring",
            "05": "spring",
            "06": "summer",
            "07": "summer",
            "08": "summer",
            "09": "autumn",
            "10": "autumn",
            "11": "autumn",
            "12": "winter",
        }

        self.last_menu = []
        self.menu = "menu"

        self.surface = pygame.display.set_mode((SYSTEM_WIDTH, SYSTEM_HEIGHT))

        self.screen = pygame.Surface((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.stats = Stats(self)

        self.settings = {}
        self.cash = {}

        init(self)

        self.play = True

        self.particles = Particles(self)

        self.render = Render(self)
        self.update = Update(self)

        self.players = Players(self)
        self.map = Map(self)

        self.mcd = 0

        Functions.play_load(self)

        self.couple = Functions.func_settings_menu(self, 0)

        self.sound = Sound()

        self.debug = {
            "fps": False,
            "full_vision": True,
            "draw_map": True,
            "cells": True,
            "particles": True if self.settings["particles"] == "ON" else False,
            "hard_difficult_map_visiable": False,
            "debug_rect": True
        }

        font_color = self.cash["menues"][self.couple]["font_color"]
        button_color = self.cash["menues"][self.couple]["button_color"]

        self.menu_back_button = Button(
            self, 0, 500, 200, 100, [], lambda: Functions.func_menu_back(self), button_color,
            text_box=TextBox(self, 25, 475, 200, 100, translate.translate("Back"), font_size=30, font_color=font_color)
        )

        self.menu_menu_buttons = {
            "text": [
                TextBox(
                    self, 250, 0, 500, 150, translate.translate("Planet"),
                    font_size=100, font_type="DATA/files/fonts/magnolia.ttf", font_color=font_color
                ),

                TextBox(
                    self, 4, HEIGHT - 30, WIDTH, 35, translate.translate("Version") + ": " + self.version,
                    font_size=24, font_color=font_color, type="left"
                )
            ],

            "buttons": [
                Button(
                    self, 250, 150, 200, 100, [], lambda: Functions.func_menu_play(self), button_color,
                    text_box=TextBox(self, 250, 150, 200, 100, translate.translate("Start"), font_size=30, font_color=font_color)
                ),

                Button(
                    self, 550, 150, 200, 100, [], lambda: Functions.func_menu_shop_menu(self), button_color,
                    text_box=TextBox(self, 550, 150, 200, 100, translate.translate("Shop"), font_size=30, font_color=font_color)
                ),

                Button(
                    self, 250, 300, 200, 100, [], lambda: Functions.func_menu_stats(self), button_color,
                    text_box=TextBox(self, 250, 300, 200, 100, translate.translate("Stats"), font_size=30, font_color=font_color),
                ),

                Button(
                    self, 550, 300, 200, 100, [], lambda: Functions.func_menu_help(self), button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Help"), font_size=30, font_color=font_color)
                ),

                Button(
                    self, 250, 450, 200, 100, [], lambda: Functions.func_menu_settings(self), button_color,
                    text_box=TextBox(self, 250, 450, 200, 100, translate.translate("Settings"), font_size=30, font_color=font_color)
                ),

                Button(
                    self, 550, 450, 200, 100, [], lambda: Functions.func_menu_quit(self), button_color,
                    text_box=TextBox(self, 550, 450, 200, 100, translate.translate("Exit"), font_size=30, font_color=font_color)
                ),
            ]
        }

        self.play_menu_buttons = {
            "buttons": [
                Button(
                    self, 603, 403, 361, 46, [], lambda: Functions.func_play_buttons(self, 0), (AV_COLOR, (60, 60, 60), None),
                    text_box=TextBox(self, 603, 403, 361, 46, translate.translate("Inventory"))
                ),

                Button(
                    self, 603, 453, 361, 46, [], lambda: Functions.func_play_buttons(self, 1), (AV_COLOR, (60, 60, 60), None),
                    text_box=TextBox(self, 603, 553, 361, 46, translate.translate(""))
                ),

                Button(
                    self, 603, 503, 361, 46, [], lambda: Functions.func_play_buttons(self, 2), (AV_COLOR, (60, 60, 60), None),
                    text_box=TextBox(self, 603, 553, 361, 46, translate.translate("Stats"))
                ),

                Button(
                    self, 603, 553, 361, 46, [], lambda: Functions.func_play_buttons(self, 3), (AV_COLOR, (60, 60, 60), None),
                    text_box=TextBox(self, 603, 553, 361, 46, translate.translate("Quit"))
                )
            ],

            "back": Button(
                self, 603, 403, 361, 46, [], lambda: Functions.func_play_menu_back(self), (AV_COLOR, (60, 60, 60), None),
                text_box=TextBox(self, 603, 403, 361, 46, translate.translate("Back"))
            ),

            "activate": None
        }

        self.play_inventory_buttons = {
            "use_buttons": [
                Button(
                    self, 603, 553, 178, 46, [], lambda: Functions.func_play_menu_inventory_using(self), (AV_COLOR, (60, 60, 60), None),
                    text_box=TextBox(self, 603, 553, 178, 46, translate.translate("Using"))
                ),

                Button(
                    self, 785, 553, 179, 46, [], lambda: Functions.func_play_menu_inventory_truns(self), (AV_COLOR, (60, 60, 60), None),
                    text_box=TextBox(self, 785, 553, 179, 46, translate.translate("Scrap"))
                ),
            ],

            "buttons": [
                Button(self, 702 + 0 * 53, 499, 50, 50, [], lambda: Functions.func_inventory_buttons(self, 0), (AV_COLOR, (60, 60, 60), None)),
                Button(self, 702 + 1 * 53, 499, 50, 50, [], lambda: Functions.func_inventory_buttons(self, 1), (AV_COLOR, (60, 60, 60), None)),
                Button(self, 702 + 2 * 53, 499, 50, 50, [], lambda: Functions.func_inventory_buttons(self, 2), (AV_COLOR, (60, 60, 60), None)),
                Button(self, 702 + 3 * 53, 499, 50, 50, [], lambda: Functions.func_inventory_buttons(self, 3), (AV_COLOR, (60, 60, 60), None)),
                Button(self, 702 + 4 * 53, 499, 50, 50, [], lambda: Functions.func_inventory_buttons(self, 4), (AV_COLOR, (60, 60, 60), None))
            ],

            "active_button": None
        }

        self.play_quit_buttons = {
            "buttons": [
                Button(
                    self, 603, 503, 361, 46, [], lambda: Functions.func_play_menu_quit_quit(self, True), (AV_COLOR, (60, 60, 60), None),
                    text_box=TextBox(self, 603, 503, 361, 46, translate.translate("Save and quit"))
                ),

                Button(
                    self, 603, 553, 361, 46, [], lambda: Functions.func_play_menu_quit_quit(self), (AV_COLOR, (60, 60, 60), None),
                    text_box=TextBox(self, 603, 553, 361, 46, translate.translate("Quit"))
                )
            ]
        }

        self.play_stats_buttons = {
            "text": [
                TextBox(self, 603, 453, 361, 25, "", type="left"),
                TextBox(self, 603, 476, 361, 25, "", type="left")
            ]
        }

        self.menu_choice_buttons = {
            "text": [
                TextBox(
                    self, 250, 0, 500, 100, translate.translate("Difficult"),
                    font_size=70, font_type="DATA/files/fonts/magnolia.ttf", font_color=font_color
                ),
            ],

            "buttons": [
                Button(
                    self, 400, 150, 200, 100, [], lambda: Functions.func_choice_easy(self, Players, Map), button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Easy"), font_size=30, font_color=font_color)
                ),

                Button(
                    self, 400, 300, 200, 100, [], lambda: Functions.func_choice_normal(self, Players, Map), button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Normal"), font_size=30, font_color=font_color)
                ),

                Button(
                    self, 400, 450, 200, 100, [], lambda: Functions.func_choice_hard(self, Players, Map), button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Hard"), font_size=30, font_color=font_color)
                )
            ]
        }

        self.menu_history_buttons = {
            "text": [
                TextField(
                    self, 205, 100, 590, HEIGHT - 270, self.cash["history"][LANG.lower()], font_color=font_color, font_size=19,
                    spec={"scroll": {"add": 0}, "auto_spawn_text": {"now": 0, "step": 0.5}}
                ),

                TextBox(
                    self, 250, 0, 500, 100, translate.translate("History"),
                    font_size=70, font_type="DATA/files/fonts/magnolia.ttf", font_color=font_color
                )
            ],

            "buttons": [
                Button(
                    self, 150, 450, 200, 100, [], lambda: Functions.func_menu_back(self), button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Back"), font_size=30, font_color=font_color)
                ),

                Button(
                    self, 400, 450, 200, 100, [], lambda: Functions.func_history_listen(self), button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Listen"), font_size=30, font_color=font_color)
                ),

                Button(
                    self, 650, 450, 200, 100, [], lambda: Functions.func_history_fill(self), button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Fill"), font_size=30, font_color=font_color)
                )
            ]
        }

        self.menu_help_menu_buttons = {
            "text": [
                TextBox(
                    self, 250, 0, 500, 100, translate.translate("Help"),
                    font_size=70, font_type="DATA/files/fonts/magnolia.ttf", font_color=font_color
                )
            ],

            "buttons": [
                Button(
                    self, 400, 150, 200, 100, [], lambda: Functions.func_menu_history(self), button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("History"), font_size=30, font_color=font_color)
                ),

                Button(
                    self, 400, 300, 200, 100, [], lambda: Functions.func_menu_to_help(self), button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Help"), font_size=30, font_color=font_color)
                ),

                Button(
                    self, 400, 450, 200, 100, [], lambda: Functions.func_menu_authors(self), button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Authors"), font_size=30, font_color=font_color)
                )
            ]
        }

        self.menu_settings_buttons = {
            "buttons": [
                Button(
                    self, 200, 10, 600, 50, [], lambda: Functions.func_settings_menu(self, 1), button_color,
                    text_box=TextBox(
                        self, 200, 0, 600, 50,
                        translate.translate("Menu") + ": " + translate.translate(self.settings["game_background"]),
                        font_size=26, font_color=font_color
                    )
                ),

                Button(
                    self, 200, 70, 600, 50, [], lambda: Functions.func_settings_font(self), button_color,
                    text_box=TextBox(
                        self, 200, 0, 600, 50,
                        translate.translate("Font") + ": " + translate.translate(self.settings["font"]),
                        font_size=26, font_color=font_color
                    )
                ),

                Button(
                    self, 200, 130, 600, 50, [], lambda: Functions.func_settings_lang(self), button_color,
                    text_box=TextBox(
                        self, 200, 0, 600, 50,
                        translate.translate("Language") + ": " + Functions.func_spec_translate_language(self.settings["lang"]),
                        font_size=26, font_color=font_color
                    )
                ),

                Button(
                    self, 200, 190, 600, 50, [], lambda: Functions.func_settings_particles(self), button_color,
                    text_box=TextBox(
                        self, 200, 0, 600, 50,
                        translate.translate("Particles") + ": " + translate.translate(self.settings["particles"]),
                        font_size=26, font_color=font_color
                    )
                ),

                Button(
                    self, 200, 250, 600, 50, [], lambda: Functions.func_settings_display_fps(self), button_color,
                    text_box=TextBox(
                        self, 200, 0, 600, 50,
                        translate.translate("Display FPS") + ": " + translate.translate(self.settings["display_fps"]),
                        font_size=26, font_color=font_color
                    )
                ),

                Button(
                    self, 200, 310, 600, 50, [], lambda: Functions.func_settings_fps(self), button_color,
                    text_box=TextBox(
                        self, 200, 0, 600, 50,
                        translate.translate("Full screen") + ": " + str(translate.translate(self.settings["fps"])),
                        font_size=26, font_color=font_color
                    )
                ),

                Button(
                    self, 200, 370, 600, 50, [], lambda: Functions.func_settings_reset(self), RED_COLOR,
                    text_box=TextBox(
                        self, 200, 0, 600, 50,
                        translate.translate("Delete save"),
                        font_size=26, font_color=RED_COLOR[2]
                    )
                )
            ]
        }

        self.menu_shop_buttons = {
            "text": [
                TextBox(
                    self, 250, 0, 500, 100, translate.translate("Shop"),
                    font_size=70, font_type="DATA/files/fonts/magnolia.ttf", font_color=font_color
                ),

                TextBox(
                    self, 250, 576, 500, 24, translate.translate("Money") + ": " + str(self.stats.money),
                    font_size=24, font_color=font_color
                )
            ],

            "shop": [
                Shop(self, self.cash["shop"])
            ]
        }

        self.menu_game_win_buttons = {
            "text": [
                TextBox(
                    self, 250, 0, 500, 100, translate.translate("Game Win!"),
                    font_size=70, font_type="DATA/files/fonts/magnolia.ttf", font_color=font_color
                )
            ],

            "buttons": [
                Button(
                    self, 400, 450, 200, 100, [], lambda: Functions.func_menu_back(self, "menu"), button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Back"), font_size=30, font_color=font_color)
                )
            ]
        }

        self.menu_game_over_buttons = {
            "text": [
                TextBox(
                    self, 250, 0, 500, 100, translate.translate("Game Over!"),
                    font_size=70, font_type="DATA/files/fonts/magnolia.ttf", font_color=font_color
                )
            ],

            "buttons": [
                Button(
                    self, 400, 450, 200, 100, [], lambda: Functions.func_menu_back(self, "menu"), button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Back"), font_size=30, font_color=font_color)
                )
            ]
        }

        self.menu_authors_buttons = {
            "text": [
                TextBox(
                    self, 250, 0, 500, 100, translate.translate("Authors"),
                    font_size=70, font_type="DATA/files/fonts/magnolia.ttf", font_color=font_color
                ),

                TextBox(
                    self, 0, 575, 1000, 20, "© 2023 - 2024 " + translate.translate("Vitebsk"),
                    font_size=20, font_type="DATA/files/fonts/magnolia.ttf", font_color=font_color
                ),

                TextField(
                    self, 200, 100, 600, HEIGHT - 170, self.cash["authors"][LANG.lower()], font_color=font_color,
                    font_size=19, spec={}
                )
            ]
        }

        self.menu_stats_buttons = {
            "text": [
                TextBox(
                    self, 250, 0, 500, 100, translate.translate("Stats"),
                    font_size=70, font_type="DATA/files/fonts/magnolia.ttf", font_color=font_color
                )
            ]
        }

        self.menu_help_buttons = {
            "path": 0,
            "text": [
                TextField(
                    self, 205, 100, 590, HEIGHT - 270, self.cash["help"][LANG.lower()][0], font_color=font_color,
                    font_size=19, spec={"scroll": {"add": 0}, "auto_spawn_text": {"now": 0, "step": 0.5}}
                ),

                TextField(
                    self, 205, 100, 590, HEIGHT - 270, self.cash["help"][LANG.lower()][1], font_color=font_color,
                    font_size=19, spec={"scroll": {"add": 0}, "auto_spawn_text": {"now": 0, "step": 0.5}}
                ),

                TextField(
                    self, 205, 100, 590, HEIGHT - 270, self.cash["help"][LANG.lower()][2], font_color=font_color,
                    font_size=19, spec={"scroll": {"add": 0}, "auto_spawn_text": {"now": 0, "step": 0.5}}
                ),

                TextField(
                    self, 205, 100, 590, HEIGHT - 270, self.cash["help"][LANG.lower()][3], font_color=font_color,
                    font_size=19, spec={"scroll": {"add": 0}, "auto_spawn_text": {"now": 0, "step": 0.5}}
                ),

                TextBox(
                    self, 250, 0, 500, 100, translate.translate("Help"),
                    font_size=70, font_type="DATA/files/fonts/magnolia.ttf", font_color=font_color
                )
            ],

            "buttons": [
                Button(
                    self, 150, 450, 200, 100, [], lambda: Functions.func_menu_back(self), button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Back"), font_size=30, font_color=font_color)
                ),

                Button(
                    self, 400, 450, 200, 100, [], lambda: Functions.func_help_listen(self), button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Listen"), font_size=30, font_color=font_color)
                ),

                Button(
                    self, 650, 450, 200, 100, [], lambda: Functions.func_help_fill(self), button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Fill"), font_size=30, font_color=font_color)
                ),

                Button(
                    self, 150, 150, 50, 150, [], lambda: Functions.func_help_path_left(self), button_color,
                    text_box=TextBox(self, 150, 150, 50, 150, translate.translate(""), font_size=30, font_color=font_color)
                ),

                Button(
                    self, 800, 150, 50, 150, [], lambda: Functions.func_help_path_right(self), button_color,
                    text_box=TextBox(self, 800, 150, 50, 150, translate.translate(""), font_size=30, font_color=font_color)
                )
            ]
        }

        self.menu_shop_menu_buttons = {
            "text": [
                TextBox(
                    self, 250, 0, 500, 100, translate.translate("Shop"),
                    font_size=70, font_type="DATA/files/fonts/magnolia.ttf", font_color=font_color
                )
            ],

            "buttons": [
                Button(
                    self, 400, 150, 200, 100, [], lambda: Functions.func_menu_shop(self), button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Shop"), font_size=30, font_color=font_color)
                ),

                Button(
                    self, 400, 300, 200, 100, [], None, button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Upgrades"), font_size=30, font_color=font_color)
                ),

                Button(
                    self, 400, 450, 200, 100, [], None, button_color,
                    text_box=TextBox(self, 550, 300, 200, 100, translate.translate("Later"), font_size=30, font_color=font_color)
                )
            ]
        }

        self.menu_upgrade_buttons = {
            "text": [
                TextBox(
                    self, 250, 0, 500, 100, translate.translate("Upgrades"),
                    font_size=70, font_type="DATA/files/fonts/magnolia.ttf", font_color=font_color
                )
            ],

            "upgrade": [
                UpgradeMap(self, self.cash["upgrades"])
            ]
        }

        self.mouse = [0, 0]
        self.fpsc = 0

        pygame.display.set_caption(NAME, ICONNAME)

    def start(self):
        while self.play:
            self.stats.time_in_game += 1 * (60 / max(self.clock.get_fps(), 0.1))

            if self.menu == "play":
                self.stats.time_in_level += 1 * (60 / max(self.clock.get_fps(), 0.1))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        x = self.players.players[self.players.turn].x + 1
                        y = self.players.players[self.players.turn].y

                        if 0 <= x <= 11 and 0 <= y <= 11:
                            self.players.update(x, y)

                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        x = self.players.players[self.players.turn].x - 1
                        y = self.players.players[self.players.turn].y

                        if 0 <= x <= 11 and 0 <= y <= 11:
                            self.players.update(x, y)

                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        x = self.players.players[self.players.turn].x
                        y = self.players.players[self.players.turn].y - 1

                        if 0 <= x <= 11 and 0 <= y <= 11:
                            self.players.update(x, y)

                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        x = self.players.players[self.players.turn].x
                        y = self.players.players[self.players.turn].y + 1

                        if 0 <= x <= 11 and 0 <= y <= 11:
                            self.players.update(x, y)

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and self.menu == "play":
                        x = (self.mouse[0] - 1) // CELLSIZE
                        y = (self.mouse[1] - 1) // CELLSIZE

                        if 0 <= x <= 11 and 0 <= y <= 11:
                            self.players.update(x, y)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        if self.menu == "history":
                            if self.menu_history_buttons["text"][0].spec["scroll"]["add"] > 0:
                                self.menu_history_buttons["text"][0].spec["scroll"]["add"] -= 1

                        if self.menu == "help":
                            if self.menu_help_buttons["text"][abs(self.menu_help_buttons["path"]) % 4].spec["scroll"]["add"] > 0:
                                self.menu_help_buttons["text"][abs(self.menu_help_buttons["path"]) % 4].spec["scroll"]["add"] -= 1

                    if event.button == 5:
                        if self.menu == "history":
                            if self.menu_history_buttons["text"][0].spec["scroll"]["add"] < self.menu_history_buttons["text"][0].width // self.menu_history_buttons["text"][0].hstep:
                                self.menu_history_buttons["text"][0].spec["scroll"]["add"] += 1

                        if self.menu == "help":
                            if self.menu_help_buttons["text"][abs(self.menu_help_buttons["path"]) % 4].spec["scroll"]["add"] < self.menu_help_buttons["text"][abs(self.menu_help_buttons["path"]) % 4].width // self.menu_help_buttons["text"][abs(self.menu_help_buttons["path"]) % 4].hstep:
                                self.menu_help_buttons["text"][abs(self.menu_help_buttons["path"]) % 4].spec["scroll"]["add"] += 1

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Functions.func_menu_back(self)

            self.render.render()
            self.update.update()

            self.surface.blit(pygame.transform.scale(self.screen, (SYSTEM_WIDTH, SYSTEM_HEIGHT)), (0, 0))

            self.fpsc += 1

            self.clock.tick(FPS)

        Functions.play_save(self)

        pygame.quit()
