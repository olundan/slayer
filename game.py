import curses
import time
from enum import Enum, auto
from entities import Player
from displaybuffer import DisplayBuffer
from sprites import frame, warrior_sprite, cyclops_sprite
from sprite import Sprite
from inputhandler import InputHandler, Action
from menuhandler import MenuHandler, test_menu

class GameState(Enum):
    INTRO = auto()
    CHAR_CREATION = auto()
    EXPOSITION = auto()
    ROAM= auto()
    BATTLE = auto()

class Game():
    def __init__(self, stdscr):
        self.display = DisplayBuffer(stdscr)
        self.input = InputHandler(stdscr)
        self.menu = MenuHandler()
        self.state = GameState.BATTLE
        self.player_char = None
        self.current_mob = None
        self.is_running = True

    
    def run(self):
        self.update()
        self.display.stdscr.getkey()

    def update(self):
        match self.state:
            case GameState.CHAR_CREATION:
                self.start_char_creation()
            case GameState.ROAM:
                self.start_roam()
            case GameState.EXPOSITION:
                self.start:exposition()
            case GameState.BATTLE:
                self.start_battle()
        self.display.render_buffer()
                
    def change_state(self, new_state):
        if not isinstance(new_state, GameState):
            self.display.draw_char("Invalid new state")
            return
        self.state = new_state

    def start_battle(self):
        menu = self.menu.get_menu_items(test_menu)
        for option in menu:
            self.display.draw_string(0,option[0],option[1])
    def start_roam(self):
        self.display.draw_string(0,0,"starting battle")
    def start_char_creation(self):
        self.display.draw_string(0,0,"char creation")
    def start_exposition(self):
        self.display.draw_string(0,0,"Expositionating")
