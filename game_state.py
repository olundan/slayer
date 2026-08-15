from enum import Enum, auto
import sys
from entities import Player, Mob
from renderer import *


class GameState(Enum):
    INTRO = auto()
    CHAR_CREATION = auto()
    EXPOSITION = auto()
    ROAM= auto()
    BATTLE = auto()

class Game():
    def __init__(self):
        self.state = GameState.CHAR_CREATION
        self.player_char = None
        self.current_mob = None

    def update(self):
        match self.state:
            case GameState.CHAR_CREATION:
                print(self.state)
            case GameState.ROAM:
                print(self.state)
            case GameState.EXPOSITION:
                print(self.state)
            case GameState.BATTLE:
                print(self.state)

