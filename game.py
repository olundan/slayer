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
from scenes import BattleScene

SCENE_REGISTRY = {
        SceneID.INTRO: IntroScene,
        SceneID.ROAM: RoamingScene,
        SceneID.BATTLE: BattleScene,
        SceneID.ENDING: EndingScene,
        }

class Game():
    def __init__(self, curses_window):
        #modules
        self.curses_window = curses_window
        self.display = DisplayBuffer(curses_window)
        self.input = InputHandler(curses_window)

        #game objects
        self.player = Player(name="Oskar", sprite=warrior_sprite,stats=Stats(hp=10, attack=10, defence=10), x=0, y=0)
        self.scenes = {}
        self.switch_scene(SceneID.INTRO)
        self.is_running = True
    
    def run(self):
        self.update()

    def update(self):
        action = self.input.get_action()
        next_scene = self.current_scene.update(action)
        
        if next_scene is not None:
            self.switch_scene(next_scene)

        self.display.clear_buffer()
        self.current_scene.draw()
        self.display.render_buffer()

    def switch_scene(self, scene_id):
        if scene_id not in self.scenes:
            self.scenes[scene_id] = SCENE_REGISTRY.get(scene_id)(self)

        self.current_scene = self.scenes[scene_id]
