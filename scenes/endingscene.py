import random
import curses
import time
from enum import Enum, auto

from core import Stats, Entity, Player, Sprite

class EndingScene():
    def __init__(self, game):
        self.display = game.display

    def update(self, action) -> SceneID | None:
        return None

    def draw(self):
        self.display.add_string(0, 0, "You escaped!")
