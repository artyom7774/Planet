from DATA.modules.translate import Translate
import json

WIDTH = 1000
HEIGHT = 600

ICONNAME = "DATA/files/sprites/cells/ship.png"

with open("DATA/files/save/settings.json", "r") as file:
    var = json.load(file)

LANG = var["lang"]
translate = Translate(LANG)

NAME = translate.translate("Planet")
BASE_FONT = f"DATA/files/fonts/{var['font']}.ttf"
FPS = var["fps"]

MOUSE_COLDDOWN = 25

BUTTON_LIVE = 60

COUNT_DETAILS = 3

PLAYERS_NAMES = [
    "Artyom",
    "Timur",
    "Ilya",
    "Andrei",
    "Alexei",
    "Vlad",
    "Vadim",
    "Denis",
    "Eugene",
    "Kirill",
    "Maxim",
    "Mark",
    "Sergei",
    "Jack"
]

for i, name in enumerate(PLAYERS_NAMES):
    PLAYERS_NAMES[i] = translate.translate(name)

# colors
BG_COLOR = (40, 40, 40)
FRAME_COLOR = (20, 20, 20)
AV_COLOR = (100, 100, 100)

RED_COLOR = [(200, 0, 0, 20), (200, 0, 0, 60), (200, 0, 0)]

CELLSIZE = 50

# stats
GET_MONEY_FOR_KILL = 8
GET_MONEY_FOR_OPEN_CELL = 1
