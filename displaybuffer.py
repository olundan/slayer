from data import Sprite

class DisplayBuffer:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.width = 40
        self.height = 13
        self.grid = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def add_char(self, x: int, y: int, char: str):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = char
    
    def add_string(self, x: int, y: int, string: str):
        pos_x = x
        for char in string:
            self.add_char(pos_x, y, char)
            pos_x += 1

    def add_sprite(self, x: int, y: int, sprite):
        for dx, dy, symbol in sprite.relational_map:
            self.add_char(x + dx, y + dy, symbol)

    def clear_buffer(self):
        self.grid = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def render_buffer(self):
        self.stdscr.move(0, 0)
        for y, row in enumerate(self.grid):
            self.stdscr.addstr(y, 0, "".join(row))
        self.stdscr.refresh()
