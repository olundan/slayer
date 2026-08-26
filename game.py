import curses
import time
from enum import Enum, auto
from entities import Player, Stats
from displaybuffer import DisplayBuffer
from sprites import text_frame, frame, warrior_sprite, cyclops_sprite
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
        self.game.display.add_sprite(0,0, frame)
        self.game.print_message("hello, world")
#        intro_message = "Wake up adventurer!\nYou have been kindapped by\nan evil wizard! \nHe is keeping you locked\nin his labyrinth..\n"
#
#        line = 0
#        row = 0
#        for char in intro_message:
#            self.game.display.add_char(row,line, char)
#            row += 1
#            if char == "\n":
#                line += 1
#                row = 0
#
#            time.sleep(0.05)
#            self.game.display.render_buffer()

class RoamingScene():
    def __init__(self, game):
        self.game = game

    def update(self):
        return None

class Game():
    def __init__(self, main_curses_window):
        self.main_curses_window = main_curses_window
        self.message_window = self.main_curses_window.subwin(5, 38, 8, 1)
        self.display = DisplayBuffer(main_curses_window)
        self.input = InputHandler(main_curses_window)
        #self.menu = MenuHandler(main_curses_window)
        self.current_scene = IntroScene(self)
        self.player = Player(name="Oskar", sprite=warrior_sprite,stats=Stats(hp=10, attack=10, defence=10), x=0, y=0)
        self.is_running = True
    
    def run(self):
        self.update()
        self.display.add_sprite(0,0,frame)
        self.display.render_buffer()

    def update(self):
        next_scene = self.current_scene.update()

        if next_scene is not None:
            self.current_scene = next_scene

        self.display.render_buffer()

    def print_message(self, message):
        self.text_display = DisplayBuffer(self.message_window, height=4, width=38)
        self.text_display.add_sprite(0,0,text_frame)
        self.text_display.add_string(1,1,message)
        self.text_display.render_buffer()
