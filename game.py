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
    def __init__(self):
        self.display = DisplayBuffer()
        self.state = GameState.BATTLE
        self.player_char = None
        self.current_mob = None
        self.is_running = True
    
    def run(self):
        sys.stdout.write(CLEAR_SCREEN + HIDE_CURSOR)
        sys.stdout.flush()
        while self.is_running:
            self.update()
            time.sleep(0.05)

    def update(self):
        match self.state:
            case GameState.CHAR_CREATION:
                print(self.state)
            case GameState.ROAM:
                pass
            case GameState.EXPOSITION:
                print(self.state)
            case GameState.BATTLE:
                player_x = 3
                player_y = 8
                monster_x = 30
                monster_y = 2
                self.display.clear_buffer()
                self.display.draw_sprite(0, 0, frame)
                self.display.draw_sprite(player_x,player_y, warrior_sprite)
                self.display.draw_sprite(monster_x, monster_y, cyclops_sprite)
                self.display.render_buffer()

    def change_state(self, new_state):
        if not isinstance(new_state, GameState):
            print("Invalid new state")
            return
        self.state = new_state

