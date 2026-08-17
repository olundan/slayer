import sys
import time
from data import Sprite

CLEAR_SCREEN = "\033[2J"
HIDE_CURSOR  = "\033[?25l"
SHOW_CURSOR  = "\033[?25h"
HIGHLIGHT = "\033[7m"  
RESET = "\033[0m"

class DisplayBuffer:
    def __init__(self):
        self.width = 40
        self.height = 13
        self.grid = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def clear_buffer(self):
        self.grid = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def draw_char(self, x: int, y: int, char: str):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = char

    def draw_sprite(self, x: int, y: int, sprite):
        for dx, dy, symbol in sprite.relational_map:
            self.draw_char(x + dx, y + dy, symbol)

    def render_buffer(self):
        frame = "\033[1;1H" + "\n".join("".join(row) for row in self.grid)
        sys.stdout.write(frame)
        sys.stdout.flush()
