from DATA.modules.variables import *

import socket
import pygame
import gtts
import os


class Sound:
    def __init__(self):
        pass

    @staticmethod
    def internet():
        try:
            socket.create_connection(("www.google.com", 80))
            return True

        except OSError:
            return False

    @staticmethod
    def sound(text, name: str = "history"):
        pygame.mixer.stop()

        while text.find("/n") != -1:
            text = text.replace("/n", "")

        while text.find("/t") != -1:
            text = text.replace("/t", "")

        if not os.path.exists(f"DATA/files/sound/{name}_{LANG.lower()}.mp3"):
            s = gtts.gTTS(text=text, lang=LANG.lower())
            s.save(f"DATA/files/sound/{name}_{LANG.lower()}.mp3")

        pygame.mixer.Sound(f"DATA/files/sound/{name}_{LANG.lower()}.mp3").play()
