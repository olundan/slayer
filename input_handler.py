import curses
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

class InputHandler:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.keymap = {
                curses.KEY_UP : Action.UP,
                curses.KEY_DOWN: Action.DOWN,
                curses.KEY_LEFT: Action.LEFT,
                curses.KEY_RIGHT: Action.RIGHT,
                10: Action.ENTER,
                13: Action.ENTER,
                curses.KEY_ENTER: Action.ENTER
                }

    def get_action(self) -> Action:
        return self.keymap.get(self.stdscr.getch())
