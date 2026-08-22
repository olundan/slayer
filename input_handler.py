import sys
import select
import tty
import termios
from enum import Enum, auto

class Action(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    ENTER = auto()
