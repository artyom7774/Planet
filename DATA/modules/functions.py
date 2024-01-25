from DATA.files.files.difficulties.easy import easy_init
from DATA.files.files.difficulties.normal import normal_init
from DATA.files.files.difficulties.hard import hard_init

from DATA.modules.base.table import Table
from DATA.modules.base.button import Button
from DATA.modules.dice import Dice

from DATA.modules.variables import *

from datetime import datetime
from datetime import date

import pygame
import random
import json
import os


class Functions:
    #
    # playing menu buttons func
    #

    @classmethod
    def func_play_buttons(cls, game, i):
        game.play_menu_buttons["activate"] = i if game.play_menu_buttons["activate"] != i else None

    @classmethod
    def func_play_menu_back(cls, game):
        game.play_menu_buttons["activate"] = None

    @classmethod
    def func_inventory_buttons(cls, game, i):
        game.play_inventory_buttons["active_button"] = i if game.play_inventory_buttons["active_button"] != i else None

    @classmethod
    def func_play_menu_quit_quit(cls, game, save=False):
        cls.play_quit(game, save)

        game.menu = "menu"

    @classmethod
    def func_play_menu_inventory_truns(cls, game):
        player = game.players.players[game.players.turn]
        number = game.play_inventory_buttons["active_button"]

        if number is None:
            return 0

        if number >= len(player.inventory):
            return 0

        if player.now == "attack":
            return 0

        if game.map.map[player.x][player.y]["name"] == "null":
            game.map.map[player.x][player.y] = game.cash["cells"][player.inventory[number]]

        else:
            player.add_item_inventory(player.x, player.y, True)
            game.map.map[player.x][player.y] = game.cash["cells"][player.inventory[number]]

        game.map.map[player.x][player.y]["visible"] = True

        player.inventory.pop(number)

        game.play_inventory_buttons["active_button"] = None

    @classmethod
    def func_play_menu_inventory_using(cls, game):
        player = game.players.players[game.players.turn]
        number = game.play_inventory_buttons["active_button"]

        if number is None:
            return 0

        if number >= len(player.inventory):
            return 0

        if game.cash["cells"][player.inventory[number]]["tag"].find("h") == -1:
            return 0

        player.health["now"] += min(player.health["max"], game.cash["cells"][player.inventory[number]]["add_health"])

        player.inventory.pop(number)
        player.add_item_inventory(player.x, player.y)

        game.play_inventory_buttons["active_button"] = None

    #
    # attack monster func
    #

    @classmethod
    def func_button_attack_tnt(cls, game):
        player = game.players.players[game.players.turn]

        if "tnt" in player.inventory:
            game.players.players[game.players.turn].now = "go"

            game.map.map[player.x][player.y] = game.cash["cells"]["null"]

            for i in range(player.x - 1, player.x + 2):
                for j in range(player.y - 1, player.y + 2):
                    if 0 <= i <= 11 and 0 <= j <= 11:
                        if not game.map.map[i][j]["visible"]:
                            game.map.map[i][j]["visible"] = True

                            game.stats.money_for_game += GET_MONEY_FOR_OPEN_CELL

            game.players.next_tern()

            game.stats.money_for_game += GET_MONEY_FOR_KILL

            player.inventory.remove("tnt")

    @classmethod
    def func_button_live(cls, game):
        if game.cash["dices"]["live"] > BUTTON_LIVE:
            game.cash["dices"]["live"] = BUTTON_LIVE

    #
    # create play dices
    #

    @classmethod
    def create_go_dice(cls, game, get):
        game.cash["dices"] = {
            "draw": True,
            "button": Dice(
                game,
                200,
                200,
                200,
                200,
                (255, 255, 255),
                game.cash["sprites"]["dices"]["go"][str(get)],
                lambda: cls.func_button_live(game),
                "go"
            ),
            "live": 100000000000
        }

    @classmethod
    def create_attack_dice(cls, game, get):
        game.cash["dices"] = {
            "draw": True,
            "button": Dice(
                game,
                50,
                200,
                200,
                200,
                (255, 255, 255),
                game.cash["sprites"]["dices"]["attack"][str(get)],
                lambda: cls.func_button_live(game),
                "attack"
            ),
            "live": 100000000000
        }

        game.cash["button"] = {
            "draw": True,
            "button": Button(
                game,
                350,
                200,
                200,
                200,
                [
                    game.cash["sprites"]["dices"]["attack"]["null"],
                    game.cash["sprites"]["dices"]["attack"]["4"]
                ],
                lambda: cls.func_button_attack_tnt(game),
                (None, None, None)
            )
        }

    #
    # settings buttons
    #

    @classmethod
    def func_settings_menu(cls, game, unext):
        menues = [
            "auto",
            "summer",
            "autumn",
            "winter",
            "spring"
        ]

        if unext:
            for i, element in enumerate(menues):
                if element == game.settings["game_background"]:
                    game.settings["game_background"] = menues[(i + 1) % len(menues)]
                    break

            else:
                raise NameError("settings: game background not found")

        else:
            if game.settings["game_background"] == "auto":
                time = datetime.now()
                time = time.strftime("%m")

                game.couple = game.couples[time]

            else:
                game.couple = game.settings["game_background"]

        if unext:
            game.menu_settings_buttons["buttons"][0].text_box.text = translate.translate("Menu") + ": " + translate.translate(game.settings["game_background"])
            game.cash["settings_confirm"] = True

            game.menu_back_button.text_box.text = translate.translate("Quit")

        return game.couple

    @classmethod
    def func_settings_font(cls, game):
        fonts = [
            "lucida",
            "arial"
        ]

        for i, element in enumerate(fonts):
            if element == game.settings["font"]:
                game.settings["font"] = fonts[(i + 1) % len(fonts)]
                break

        game.menu_settings_buttons["buttons"][1].text_box.text = translate.translate("Font") + ": " + translate.translate(game.settings["font"])
        game.cash["settings_confirm"] = True

        game.menu_back_button.text_box.text = translate.translate("Quit")

    @classmethod
    def func_settings_lang(cls, game):
        langs = [
            "RU",
            "EN"
        ]

        for i, element in enumerate(langs):
            if element == game.settings["lang"]:
                game.settings["lang"] = langs[(i + 1) % len(langs)]
                break

        game.menu_settings_buttons["buttons"][2].text_box.text = translate.translate("Language") + ": " + cls.func_spec_translate_language(game.settings["lang"])
        game.cash["settings_confirm"] = True

        game.menu_back_button.text_box.text = translate.translate("Quit")

    @classmethod
    def func_settings_particles(cls, game):
        particles = [
            "ON",
            "OFF"
        ]

        for i, element in enumerate(particles):
            if element == game.settings["particles"]:
                game.settings["particles"] = particles[(i + 1) % len(particles)]
                break

        game.menu_settings_buttons["buttons"][3].text_box.text = translate.translate("Particles") + ": " + translate.translate(game.settings["particles"])
        game.cash["settings_confirm"] = True

        game.menu_back_button.text_box.text = translate.translate("Quit")

    @classmethod
    def func_settings_display_fps(cls, game):
        fps = [
            "ON",
            "OFF"
        ]

        for i, element in enumerate(fps):
            if element == game.settings["display_fps"]:
                game.settings["display_fps"] = fps[(i + 1) % len(fps)]
                break

        game.menu_settings_buttons["buttons"][4].text_box.text = translate.translate("Display FPS") + ": " + translate.translate(game.settings["display_fps"])
        game.cash["settings_confirm"] = True

        game.menu_back_button.text_box.text = translate.translate("Quit")

    @classmethod
    def func_settings_fps(cls, game):
        fps = [
            "ON",
            "OFF"
        ]

        for i, element in enumerate(fps):
            if element == game.settings["fps"]:
                game.settings["fps"] = fps[(i + 1) % len(fps)]
                break

        game.menu_settings_buttons["buttons"][5].text_box.text = translate.translate("Full screen") + ": " + str(game.settings["fps"])
        game.cash["settings_confirm"] = True

        game.menu_back_button.text_box.text = translate.translate("Quit")

    @classmethod
    def func_settings_reset(cls, game):
        with open("DATA/files/save/game.json", "w"):
            pass

        game.menu_settings_buttons["buttons"][6].action = lambda: cls.func_settings_reset_confirm(game)
        game.menu_settings_buttons["buttons"][6].text_box.text = translate.translate("Confirm")

        game.menu_back_button.text_box.text = translate.translate("Quit")

        game.cash["settings_confirm"] = True

    @classmethod
    def func_settings_reset_confirm(cls, game):
        game.menu_settings_buttons["buttons"][6].text_box.text = translate.translate("Save reset")

        game.cash["delete_save"] = True

    #
    # menu func
    #

    @classmethod
    def func_menu_quit(cls, game):
        game.play = False

    @classmethod
    def func_menu_play(cls, game):
        if not game.cash["save"]:
            game.menu = "choice_difficult"

        else:
            game.menu = "play"

    @classmethod
    def func_menu_history(cls, game):
        cls.func_menu_back_append(game)

        game.menu_history_buttons["text"][0].spec["auto_spawn_text"]["now"] = 0
        game.menu_history_buttons["text"][0].spec["scroll"]["add"] = 0

        game.menu = "history"

    @classmethod
    def func_menu_upgrade(cls, game):
        cls.func_menu_back_append(game)

        game.menu_upgrade_buttons["upgrade"][0].init()

        game.menu = "upgrade"

    @classmethod
    def func_menu_help(cls, game):
        cls.func_menu_back_append(game)

        game.menu = "menu_help"

    @classmethod
    def func_menu_settings(cls, game):
        cls.func_menu_back_append(game)

        game.menu = "settings"

    @classmethod
    def func_menu_stats(cls, game):
        cls.func_menu_back_append(game)

        game.cash["stats_table"] = Table(game)
        game.cash["stats_table"].init()

        game.menu = "stats"

    @classmethod
    def func_menu_authors(cls, game):
        cls.func_menu_back_append(game)

        game.menu = "authors"

    @classmethod
    def func_menu_game_win(cls, game):
        cls.func_menu_back_append(game)
        cls.play_quit(game)

        game.menu = "game_win"

    @classmethod
    def func_menu_game_over(cls, game):
        cls.func_menu_back_append(game)
        cls.play_quit(game)

        game.menu = "game_over"

    @classmethod
    def func_menu_shop_menu(cls, game):
        cls.func_menu_back_append(game)

        game.menu_shop_buttons["shop"][0].init()

        game.menu = "menu_shop"

    @classmethod
    def func_menu_shop(cls, game):
        cls.func_menu_back_append(game)

        game.menu_shop_buttons["shop"][0].init()

        game.menu = "shop"

    @classmethod
    def func_menu_to_help(cls, game):
        cls.func_menu_back_append(game)

        for text in game.menu_help_buttons["text"]:
            try:
                text.spec["auto_spawn_text"]["now"] = 0

            except:
                pass

        game.menu = "help"

    @classmethod
    def func_history_listen(cls, game):
        game.sound.sound(game.cash["history"][LANG.lower()])

    @classmethod
    def func_history_fill(cls, game):
        game.menu_history_buttons["text"][0].spec["auto_spawn_text"]["now"] = 10000000000000000

    @classmethod
    def func_help_listen(cls, game):
        game.sound.sound(game.cash["help"][LANG.lower()][abs(game.menu_help_buttons["path"]) % 4], f"help_{game.menu_help_buttons['path'] % 4}")

    @classmethod
    def func_help_fill(cls, game):
        game.menu_help_buttons["text"][abs(game.menu_help_buttons["path"]) % 4].spec["auto_spawn_text"]["now"] = 10000000000000000

    @classmethod
    def func_help_path_left(cls, game):
        game.menu_help_buttons["path"] -= 1

    @classmethod
    def func_help_path_right(cls, game):
        game.menu_help_buttons["path"] += 1

    #
    # menu back button
    #

    @classmethod
    def func_menu_back_append(cls, game):
        game.last_menu.append(game.menu)

    @classmethod
    def func_menu_back(cls, game, menu=None):
        game.map.game_complite = False
        game.players.players[0].was_killed = False

        try:
            if menu is None:
                if len(game.last_menu) == 0:
                    game.menu = "menu"
                    return 0

                game.menu = str(game.last_menu[-1])
                game.last_menu.pop(len(game.last_menu) - 1)

            else:
                game.menu = menu

        except any:
            game.menu = "menu"

        pygame.mixer.stop()

        if game.cash["settings_confirm"]:
            game.play = False

    #
    # choice game difficult
    #

    @classmethod
    def func_choice_easy(cls, game, players, map):
        if not game.cash["save"]:
            game.cash["cells"] = easy_init(game)

            game.cash["game_id"] = random.randrange(10000000000)

            game.players = players(game)

            game.map = map(game)

            game.map.generate()

            game.cash["difficult"] = 1

            cls.use_upgrades(game)

        game.play_inventory_buttons["active_button"] = None
        game.play_menu_buttons["activate"] = None

        game.menu = "play"

    @classmethod
    def func_choice_normal(cls, game, players, map):
        if not game.cash["save"]:
            game.cash["cells"] = normal_init(game)

            game.cash["game_id"] = random.randrange(10000000000)

            game.players = players(game)
            game.map = map(game)

            game.map.generate()

            game.cash["difficult"] = 2

            cls.use_upgrades(game)

        game.play_inventory_buttons["active_button"] = None
        game.play_menu_buttons["activate"] = None

        game.menu = "play"

    @classmethod
    def func_choice_hard(cls, game, players, map):
        if not game.cash["save"]:
            game.cash["cells"] = hard_init(game)

            game.cash["game_id"] = random.randrange(10000000000)

            game.players = players(game)
            game.map = map(game)

            game.map.generate()

            game.cash["difficult"] = 3

            cls.use_upgrades(game)

        game.play_inventory_buttons["active_button"] = None
        game.play_menu_buttons["activate"] = None

        game.menu = "play"

    @classmethod
    def use_upgrades(cls, game):
        for i, upgrade in enumerate(game.stats.upgrades):
            if upgrade["count"] <= 0:
                game.stats.upgrades.pop(i)
                continue

            player = random.choice(game.players.players)

            while len(player.inventory) == 5:
                player = random.choice([player for player in game.players.players if len(player.inventory) < 5])

            player.inventory.append(upgrade["add"])

            game.stats.upgrades[i]["count"] -= 1

    #
    # leave for game
    #

    @classmethod
    def play_quit(cls, game, save=False):
        if not save:
            game.cash["save"] = False

            if game.map.game_complite:
                game.stats.money += game.stats.money_for_game

                if game.stats.best_moves is not None:
                    game.stats.best_moves = min(game.stats.moves, game.stats.best_moves)

                else:
                    game.stats.best_moves = game.stats.moves

                game.stats.game_stats.append({
                    "id": game.cash["game_id"],

                    "win": 1,

                    "difficult": game.cash["difficult"],
                    "moves": game.stats.moves,
                    "time": game.stats.time_in_level,
                    "rtime": [str(date.today()), str(datetime.now().time())]
                })

            else:
                game.stats.game_stats.append({
                    "id": game.cash["game_id"],

                    "win": 0,

                    "difficult": game.cash["difficult"],
                    "moves": game.stats.moves,
                    "time": game.stats.time_in_level,
                    "rtime": [str(date.today()), str(datetime.now().time())]
                })

            game.stats.money_for_game = 0

        else:
            game.cash["save"] = True

        game.menu = "menu"

    #
    # base settings
    #

    @classmethod
    def play_save(cls, game):
        if game.cash["delete_save"]:
            return 0

        path = "DATA/files/save/"

        with open(path + "game.json", "w") as file:
            json.dump({
                "money": game.stats.money,
                "best_moves": game.stats.best_moves,
                "time_in_game": game.stats.time_in_game,
                "upgrades": game.stats.upgrades,
                "skills": game.stats.skills,
                "game_stats": game.stats.game_stats
            }, file, indent=4)

        with open(path + "settings.json", "w") as file:
            json.dump(game.settings, file, indent=4)

    @classmethod
    def play_load(cls, game):
        path = "DATA/files/save/"

        if os.path.exists(path + "game.json"):
            try:
                with open(path + "game.json", "r") as file:
                    stats = json.load(file)

                game.stats.money = stats["money"]
                game.stats.best_moves = stats["best_moves"]
                game.stats.time_in_game = stats["time_in_game"]
                game.stats.upgrades = stats["upgrades"]
                game.stats.skills = stats["skills"]
                game.stats.game_stats = stats["game_stats"]

            except:
                pass

        if os.path.exists(path + "settings.json"):
            with open(path + "settings.json", "r") as file:
                stats = json.load(file)

            game.settings = stats

        else:
            game.settings = {
                "game_background": "auto",
                "font": "lucida",
                "lang": "EN",
                "particles": "ON",
                "display_fps": "OFF",
                "fps": "OFF"
            }

    #
    # spec func
    #

    @classmethod
    def func_spec_translate_language(cls, name):
        languages = {
            "RU": "Русский",
            "EN": "English"
        }

        return languages[name]

    @classmethod
    def func_spec_shop_buy(cls, game, slot):
        if game.stats.money < slot.cost:
            return 0

        game.stats.money -= slot.cost

        add = {
            "name": slot.stats["name"],
            "add": slot.stats["get"]["add"],
            "count": slot.stats["on"]
        }

        for element in game.stats.upgrades:
            if element["name"] == add["name"]:
                element["count"] += add["count"]
                break

        else:
            game.stats.upgrades.append(add)

        slot.init()
