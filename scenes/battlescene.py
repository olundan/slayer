import random
import curses
import time
from enum import Enum, auto

from core import Stats, Entity, Player, Sprite, SceneID
from engine import Action

from data.sprites import *

class BattleScene():
    def __init__(self, game):
        self.display = game.display
        self.player = game.player

    def update(self, action) -> SceneID | None:
        if not action == Action.ENTER:
            pass
        else:
            return SceneID.ROAM
        return None

    def draw(self):
        self.print_message("A monster appeared!")

    def print_message(self, message):
        self.display.add_sprite(1,8, text_frame)
        self.display.add_string(3,9, message)
