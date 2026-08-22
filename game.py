import time
from enum import Enum, auto
import sys
from entities import Player
from renderer import CLEAR_SCREEN, HIDE_CURSOR, DisplayBuffer
from data import frame, warrior_sprite, cyclops_sprite
from data import Sprite

class GameState(Enum):
    INTRO = auto()
    CHAR_CREATION = auto()
    EXPOSITION = auto()
    ROAM= auto()
    BATTLE = auto()

class Game():
    def __init__(self, stdscr):
        self.display = DisplayBuffer(stdscr)
        self.input = None
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
                self.display.draw_sprite(0,0,warrior_sprite)
            case GameState.ROAM:
                self.display.draw_sprite(0,0,warrior_sprite)
            case GameState.EXPOSITION:
                self.display.draw_sprite(0,0,warrior_sprite)
            case GameState.BATTLE:
                self.display.draw_sprite(0,0,warrior_sprite)
                self.display.draw_sprite(0,10,warrior_sprite)
                self.display.render_buffer()

    def change_state(self, new_state):
        if not isinstance(new_state, GameState):
            self.display.draw_char("Invalid new state")
            return
        self.state = new_state

