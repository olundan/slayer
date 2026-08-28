import curses
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
        self.stdscr.nodelay(True)
        return self.keymap.get(self.stdscr.getch())

    def get_action_blocking(self) -> Action:
        self.stdscr.nodelay(False)
        return self.keymap.get(self.stdscr.getch())
