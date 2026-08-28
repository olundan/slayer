import random
import curses
import time
from enum import Enum, auto

from core import Stats, Entity, Player, Sprite, SceneID
from engine import DisplayBuffer, InputHandler
from data import *

from scenes import IntroScene
from scenes import RoamingScene
from scenes import EndingScene

SCENE_REGISTRY = {
        SceneID.INTRO: IntroScene,
        SceneID.ROAM: RoamingScene,
        SceneID.ENDING: EndingScene,
        }

class Game():
    def __init__(self, curses_window):
        #modules
        self.display = DisplayBuffer(curses_window)
        self.input = InputHandler(curses_window)

        #game objects
        self.player = Player(name="Oskar", sprite=warrior_sprite,stats=Stats(hp=10, attack=10, defence=10), x=0, y=0)
        self.current_scene = IntroScene(self)
        self.is_running = True
    
    def run(self):
        self.update()

    def update(self):
        action = self.input.get_action()
        next_scene = self.current_scene.update(action)
        
        if next_scene is not None:
            self.current_scene = SCENE_REGISTRY.get(next_scene)(self)

        self.display.clear_buffer()
        self.current_scene.draw()
        self.display.render_buffer()

    def print_message(self, message):
        self.display.add_sprite(1,8, text_frame)
        self.display.add_string(3,9, message)
