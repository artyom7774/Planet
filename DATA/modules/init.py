from DATA.files.files.difficulties.easy import easy_init

import pygame
import json


def init(game):
    """
    s - spawn
    e - enemy
    g - get
    h - health
    """

    path = "DATA/files/sprites/"

    game.cash["settings_confirm"] = False
    game.cash["save"] = False

    game.cash["difficult"] = -1
    game.cash["game_id"] = -1

    game.cash["stats_table"] = None

    game.cash["delete_save"] = False

    game.cash["internet_error_text"] = None

    game.cash["dices"] = {
        "draw": False,
        "button": None,
        "live": 0
    }

    game.cash["button"] = {
        "draw": False,
        "button": None
    }

    game.cash["shop_sprites"] = {
        "health_add_1": pygame.image.load(path + "shop/health_add_1.png"),
        "health_add_3": pygame.image.load(path + "shop/health_add_3.png"),
        "tnt": pygame.image.load(path + "shop/tnt.png"),
        "gun_1": pygame.image.load(path + "shop/gun_1.png")
    }

    with open("DATA/files/files/shop/shop.json", "r") as file:
        game.cash["shop"] = json.load(file)

    with open("DATA/files/files/shop/upgrades.json", "r") as file:
        game.cash["upgrades"] = json.load(file)

    for i, element in enumerate(game.cash["shop"]):
        element["image"] = game.cash["shop_sprites"][element["image"]]

        game.cash["shop"][i] = element

    game.cash["history"] = {
        "ru": """
            /t Космонавты искали новую планету, так как Земля стала непригодной для жизни. Они очень долго исследовали космос. Топливо и еда должны были закончиться через 30 дней, а новых планет не было на радаре...
            /n /n /t Вдруг они обнаружили, что в 100000 км от корабля есть Планета, схожая с Землёй. Так как им могло не хватить топлива и еды путешествовать дальше по космосу, они решили исследовать Планету, - в надежде, что им больше не придётся бороздить по космосу. Космонавты поставили ориентир на эту планету, и им пришлось ждать 25 дней, чтобы добраться до этой планеты, и за это время они даже не готовились к тому, что на Планете могут обитать опасные существа. Когда они добрались до Планеты и преодолели атмосферу, в их корабль попал снаряд, и корабль начал падать. Космонавтам пришлось катапультироваться, чтобы не разбиться. Корабль упал где-то на неизведанной планете, а космонавты приземлились полным составом на неизведанную планету.
            /n /n /t Теперь главной их задачей будет не исследование Планеты, а поиск корабля, так как Планета оказалась заселена агрессивно настроенными существами. Так как у корабля осталось мало топлива, надо найти замену топлива или синтезировать его из инопланетных ресурсов. Также от корабля отлетела деталь, без которой корабль не взлетит, - её нужно отыскать. Ну и, конечно же, надо найти сам корабль. И только тогда, когда команда найдёт корабль, починит его и улетит с этой планеты, игра будет считаться пройденной… А пока что вас ждёт увлекательное путешествие по неизведанной планете, сбор ресурсов, поиск корабля, сражения с пришельцами и многое другое. В игре вы научитесь работать в команде, помогать друг другу, также вы можете продумывать, как лучше поступать в сложных ситуациях, как распоряжаться своими ресурсами и многое другое.
            /n /n /t Помни, когда мы едины - мы непобедимы.
        """,

        "en": """
            /t The astronauts were looking for a new planet, as the Earth had become uninhabitable. They have been exploring space for a very long time. Fuel and food were supposed to run out in 30 days, and there were no new planets on the radar...
            /n /n /t Suddenly they discovered that 100,000 km from the ship there is a Planet similar to Earth. Since they might not have enough fuel and food to travel further into space, they decided to explore the Planet - in the hope that they would no longer have to surf through space. The astronauts set a landmark on this planet, and they had to wait 25 days to get to this planet, and during that time they did not even prepare for the fact that dangerous creatures could inhabit the Planet. When they reached the Planet and overcame the atmosphere, a shell hit their ship, and the ship began to fall. The astronauts had to eject in order not to crash. The ship crashed somewhere on an unknown planet, and the astronauts landed in full force on an unknown planet.
            /n /n /t Now their main task will not be to explore the Planet, but to search for a ship, since the Planet turned out to be inhabited by aggressive creatures. Since the ship has little fuel left, it is necessary to find a fuel replacement or synthesize it from alien resources. Also, a part flew away from the ship, without which the ship will not take off - it needs to be found. And, of course, we need to find the ship itself. And only when the team finds the ship, repairs it and leaves this planet, the game will be considered completed… In the meantime, you will have an exciting journey through an unknown planet, collecting resources, searching for a ship, fighting with aliens and much more. In the game you will learn how to work in a team, help each other, you can also think about how best to act in difficult situations, how to manage your resources and much more.
            /n /n /t Remember, when we are united, we are invincible.
        """
    }

    game.cash["help"] = {
        "ru": [
            """
                /t Старт игры: 
                /n - Каждому игроку даётся определенное количество сердечек, а по ходу игры игрок может найти дополнительные сердечки на карте. Всего у игрока может быть максимум 5 единиц сердечек. 
                /n - Игроки выставляются на клетку старта и начинают игру.
                /n - У всех игроков имеется 5 ячеек инвентаря, то есть больше 5 предметов игроку нельзя носить. Всё лишнее он может выбросить на карте или использовать.
                /n /n /t Финиш игры:
                /n - Игра будет считаться пройденной, когда игроки починят корабль (найдя сам корабль, деталь от корабля и 2 компонента бензина) и дружно улетят с Планеты, где игрокам оказались не рады.
                /n - Игра будет считаться проигранной, если у всех игроков нет здоровья.
                /n - В случае победы, результат игры попадает в таблицу статистики.
            """,
            """
                /t Для ходьбы мы используем кубик "Для ходьбы". Ходить можно вперёд, назад, вправо и влево. По диагонали ходить нельзя. 
                /n /n /t Какое число выпадает на кубике, столько шагов мы и можем сделать. Управление Левой кнопкой мышки, либо стрелками на клавиатуре, либо клавишами WASD. 
                /n /n /t Клетка, на которую мы ходим, может оказаться или пустой или что-либо содержать (корабль, запчасть от корабля, полезный бонус, пришелец).
                /n /n /t Полезные вещи (кроме корабля) можно забрать в рюкзак. С пришельцем нужно сразиться.
            """,
            """
                /t Для сражений нам понадобится кубик "Для сражений". На кубике есть: БЕГ, -1 сердечко и выстрел.
                /n - Если у нас есть Динамит, то мы можем без сражения одолеть пришельца (динамит тратится).
                /n - Если выпал Выстрел и у нас есть Оружие, то мы можем им воспользоваться и одолеть пришельца.
                /n - Если же у нас нет Оружия и Динамита, то мы кидаем кубик повторно. 
                /n - Если выпал Бег, то возращаемся на предыдущую клетку без сражения.
                /n - Если закончились сердечки, то персонаж выбывает из игры. Его инвентарь будет разбросан по всей карте.
            """,
            """
                /t В Магазине возможно приобрести временные бонусы на старт игры. Также можно накопить монетки,пройдя Викторину.
            """
        ],

        "en": [
            """
                /t Game start:
                /n - Each player is given a certain number of hearts, and during the game the player can find additional hearts on the map. A player can have a maximum of 5 hearts in total.
                /n - Players are placed on the starting square and start the game.
                /n - All players have 5 inventory cells, that is, the player cannot carry more than 5 items. He can throw away anything superfluous on the map or use it.
                /n /n /t The finish of the game:
                / n - The game will be considered completed when the players repair the ship (having found the ship itself, a part from the ship and 2 components of gasoline) and fly away from the Planet together, where the players were not welcome.
                /n - The game will be considered lost if all players have no health.
                /n - In case of victory, the result of the game gets into the statistics table.
            """,
            """
                /t For walking, we use the cube "For walking". You can walk forward, backward, right and left. You can't walk diagonally.
                /n /n /t What number falls on the cube, that's how many steps we can take. Control with the left mouse button, either with the arrows on the keyboard, or with the WASD keys.
                /n /n /t The cell we go to may turn out to be either empty or contain something (a ship, a spare part from a ship, a useful bonus, an alien).
                /n /n /t Useful items (except the ship) can be taken in a backpack. You need to fight the alien.
            """,
            """
                /t For battles, we will need a cube "For battles". There are: RUNNING, -1 heart and a shot on the cube.
                /n - If we have Dynamite, then we can defeat the alien without a battle (dynamite is spent).
                /n - If a Shot is fired and we have a Weapon, then we can use it and defeat the alien.
                /n - If we do not have Weapons and Dynamite, then we roll the dice again.
                /n - If a Run falls out, then we return to the previous cell without a battle.
                /n - If the hearts run out, the character is eliminated from the game. His inventory will be scattered all over the map.
            """,
            """
                /t In the store you can get temporary bonuses at the start of the game. You can also save coins by passing the Quiz.
            """
        ]
    }

    game.cash["authors"] = {
        "ru": """
            Тимур - геймдизайнер, художник
            /n
            /n Артём - программист
        """,

        "en": """
            Timur - game designer, artist
            /n
            /n Artyom - programmer
        """
    }

    game.cash["menues"] = {
        "winter": {
            "bg": pygame.image.load(path + "menues/winter/bg.jpg").convert_alpha(game.surface),
            "mouse": pygame.image.load(path + "menues/winter/mouse.png").convert_alpha(game.surface),

            "button_color": [(200, 200, 240, 20), (200, 200, 240, 60), (200, 200, 240)],
            "font_color": (200, 200, 240),
            "snow_color": (180, 180, 220)
        },

        "summer": {
            "bg": pygame.image.load(path + "menues/summer/bg.jpg").convert_alpha(game.surface),
            "mouse": pygame.image.load(path + "menues/summer/mouse.png").convert_alpha(game.surface),

            "button_color": [(170, 180, 130, 20), (170, 180, 130, 60), (170, 180, 130)],
            "font_color": (170, 180, 130, 110 + 20),
        },

        "autumn": {
            "bg": pygame.image.load(path + "menues/autumn/bg.jpg").convert_alpha(game.surface),
            "mouse": pygame.image.load(path + "menues/autumn/mouse.png").convert_alpha(game.surface),

            "button_color": [(220, 130, 80, 20), (220, 130, 80, 60), (220, 130, 80)],
            "font_color": (220, 130, 80),
        },

        "spring": {
            "bg": pygame.image.load(path + "menues/spring/bg.jpg").convert_alpha(game.surface),
            "mouse": pygame.image.load(path + "menues/spring/mouse.png").convert_alpha(game.surface),

            "button_color": [(170, 180, 130, 20), (170, 180, 130, 60), (170, 180, 130)],
            "font_color": (170, 180, 130),
        }
    }

    game.cash["sprites"] = {
        "map": pygame.transform.scale(pygame.image.load(path + "map.png").convert_alpha(game.surface), (1000, 1000)),
        "step": pygame.image.load(path + "step.png").convert_alpha(game.surface),
        "mouse": pygame.image.load(path + "mouse.png").convert_alpha(game.surface),

        "died": pygame.image.load(path + "died.png").convert_alpha(game.surface),

        "ship": {
            "1": pygame.image.load(path + "cells/ship_bar_1.png").convert_alpha(game.surface),
            "2": pygame.image.load(path + "cells/ship_bar_2.png").convert_alpha(game.surface),
            "3": pygame.image.load(path + "cells/ship_bar_3.png").convert_alpha(game.surface)
        },

        "actions": {
            "1": pygame.image.load(path + "actions/1.png").convert_alpha(game.surface),
            "2": pygame.image.load(path + "actions/2.png").convert_alpha(game.surface),
            "3": pygame.image.load(path + "actions/3.png").convert_alpha(game.surface),
            "4": pygame.image.load(path + "actions/4.png").convert_alpha(game.surface)
        },

        "fields": {
            "4_1": pygame.image.load(path + "fields/4_1.png").convert_alpha(game.surface),
            "4_4": pygame.image.load(path + "fields/4_4.png").convert_alpha(game.surface)
        },

        "menu_button": {
            "1": pygame.image.load(path + "menu_button.png").convert_alpha(game.surface)
        },

        "dices": {
            "go": {
                "0": pygame.image.load(path + "dices/go/0.png").convert_alpha(game.surface),
                "1": pygame.image.load(path + "dices/go/1.png").convert_alpha(game.surface),
                "2": pygame.image.load(path + "dices/go/2.png").convert_alpha(game.surface),
                "3": pygame.image.load(path + "dices/go/3.png").convert_alpha(game.surface),
                "4": pygame.image.load(path + "dices/go/4.png").convert_alpha(game.surface),
                "5": pygame.image.load(path + "dices/go/5.png").convert_alpha(game.surface),
                "6": pygame.image.load(path + "dices/go/6.png").convert_alpha(game.surface),

                "null": pygame.image.load(path + "dices/go/null.png").convert_alpha(game.surface),
            },

            "attack": {
                "0": pygame.image.load(path + "dices/attack/0.png").convert_alpha(game.surface),
                "1": pygame.image.load(path + "dices/attack/1.png").convert_alpha(game.surface),
                "2": pygame.image.load(path + "dices/attack/2.png").convert_alpha(game.surface),
                "3": pygame.image.load(path + "dices/attack/3.png").convert_alpha(game.surface),
                "4": pygame.image.load(path + "dices/attack/4.png").convert_alpha(game.surface),

                "null": pygame.image.load(path + "dices/attack/null.png").convert_alpha(game.surface),
            }
        },

        "player": {
            "health": [
                pygame.image.load(path + "health/health.png").convert_alpha(game.surface),
                pygame.image.load(path + "health/empty_health.png").convert_alpha(game.surface)
            ]
        },

        "cells": {
            "null": pygame.image.load(path + "cells/null.png").convert_alpha(game.surface),
            "enemy_1": pygame.image.load(path + "cells/enemy_1.png").convert_alpha(game.surface),
            "enemy_2": pygame.image.load(path + "cells/enemy_2.png").convert_alpha(game.surface),
            "enemy_3": pygame.image.load(path + "cells/enemy_3.png").convert_alpha(game.surface),
            "tnt": pygame.image.load(path + "cells/tnt.png").convert_alpha(game.surface),
            "gun_1": pygame.image.load(path + "guns/1.png").convert_alpha(game.surface),
            "gun_2": pygame.image.load(path + "guns/2.png").convert_alpha(game.surface),
            "gun_3": pygame.image.load(path + "guns/3.png").convert_alpha(game.surface),
            "gun_4": pygame.image.load(path + "guns/4.png").convert_alpha(game.surface),
            "gun_5": pygame.image.load(path + "guns/5.png").convert_alpha(game.surface),
            "health_add_1": pygame.image.load(path + "cells/health_add_1.png").convert_alpha(game.surface),
            "health_add_3": pygame.image.load(path + "cells/health_add_3.png").convert_alpha(game.surface),
            "fuel": pygame.image.load(path + "cells/fuel.png").convert_alpha(game.surface),
            "detail": pygame.image.load(path + "cells/detail.png").convert_alpha(game.surface),
            "ship": pygame.image.load(path + "cells/ship.png").convert_alpha(game.surface),
            "not_open": pygame.image.load(path + "cells/not_open.png").convert_alpha(game.surface)
        }
    }

    game.cash["cells"] = easy_init(game)
