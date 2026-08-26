import curses
import time
from enum import Enum, auto
from entities import Player
from displaybuffer import DisplayBuffer
from sprites import frame, warrior_sprite, cyclops_sprite
from sprite import Sprite
from inputhandler import InputHandler, Action
from menuhandler import MenuHandler, test_menu


class IntroScene():
    def __init__(self, game):
        self.game = game

    def update(self):
        self.print_intro()
        return None

    def print_intro(self):
        intro_message = "Wake up adventurer!\nYou have been kindapped by\nan evil wizard! \nHe is keeping you locked\nin his labyrinth..\n"

        line = 0
        row = 0
        for char in intro_message:
            self.game.display.add_char(row,line, char)
            row += 1
            if char == "\n":
                line += 1
                row = 0

            time.sleep(0.05)
            self.game.display.render_buffer()

class RoamingScene():
    def __init__(self, game):
        self.game = game

    def update(self):
        self.game.display.add_string(0,0, "Hello, World 2")
        return None

class Game():
    def __init__(self, stdscr):
        self.display = DisplayBuffer(stdscr)
        self.input = InputHandler(stdscr)
        self.menu = MenuHandler()
        self.current_scene = IntroScene(self)
        self.is_running = True
    
    def run(self):
        self.update()

    def update(self):
        next_scene = self.current_scene.update()

        if next_scene is not None:
            self.current_scene = next_scene

        self.display.render_buffer()
        self.display.stdscr.getch() #Tillfällig för flowvisualisering
