import curses
import time
from enum import Enum, auto
from entities import Player, Stats
from displaybuffer import DisplayBuffer
from sprites import text_frame, frame, warrior_sprite, cyclops_sprite
from sprite import Sprite
from inputhandler import InputHandler, Action
from uihandler import UIHandler

class IntroScene():
    def __init__(self):
        pass

    def update(self, action):
        return None

    def draw(self, display):
        pass

class RoamingScene():
    def __init__(self):
        pass

    def update(self, action):
        return None

    def draw(self):
        pass

class Game():
    def __init__(self, curses_window):
        #modules
        self.display = DisplayBuffer(curses_window)
        self.input = InputHandler(curses_window)
        self.ui = UIHandler()

        #game objects
        self.current_scene = IntroScene()
        self.player = Player(name="Oskar", sprite=warrior_sprite,stats=Stats(hp=10, attack=10, defence=10), x=0, y=0)
        self.is_running = True
    
    def run(self):
        self.update()

    def update(self):
        action = self.input.get_action()
        next_scene = self.current_scene.update(action)
        
        if next_scene:
            self.current_scene = next_scene

        self.display.clear_buffer()
        self.current_scene.draw(self.display)
        self.display.render_buffer()

    def print_message(self, message):
        self.display.add_sprite(1,8, text_frame)
        self.display.add_string(3,9, message)
