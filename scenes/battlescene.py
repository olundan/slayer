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
        self.reset()

    def update(self, action) -> SceneID | None:
        if not action == Action.ENTER:
            pass
        else:
            self.battle_confirmed = True

        if self.battle_confirmed:
            return SceneID.ROAM

    def draw(self):
        if self.battle_confirmed:
            self.display.add_sprite(7,7,self.player.sprite)
            self.display.add_sprite(25,4,self.monster.sprite)
            self.display.add_sprite(0,0, frame)
        else:
            self.print_message("A monster appeared!")

    def print_message(self, message):
        self.display.add_sprite(1,8, text_frame)
        self.display.add_string(3,9, message)

    def reset(self):
        self.battle_confirmed = False
        self.monster = self.generate_monster(self.player.lvl)

    def generate_monster(self, player_lvl):
        return Entity("Cyclops", sprite=cyclops_sprite, stats=Stats(hp=100, attack=10, defence=10))
