import random
import curses
import time
from enum import Enum, auto

from core import Stats, Entity, Player, Sprite, SceneID
from engine import Action

class IntroScene():
    def __init__(self, game):
        self.game = game
        self.display = game.display
        self.pressed_continue= False

    def update(self, action) -> SceneID | None:
        if not action == Action.ENTER:
            pass
        else:
            return SceneID.ROAM
        return None

    def draw(self):
        self.display.add_string(0,0, "Wake up Adventurer!")
        self.display.add_string(0,1, "You have been kindapped.")
        self.display.add_string(0,2, "Escape!")
        self.display.add_string(0,3, "Press Enter to continue..")
