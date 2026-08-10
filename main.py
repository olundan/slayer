import random
import sys
import os

CLEAR_SCREEN = "\033[2J"
HIDE_CURSOR  = "\033[?25l"
SHOW_CURSOR  = "\033[?25h"

class Sprite:
    def __init__(self, size_x: int, size_y: int, pattern: list[list[str]]):
        self.size_x = size_x
        self.size_y = size_y

        self.relational_map: list[tuple[int,int,str]] = []

        for dy in range(size_y):
            for dx in range(size_x):
                symbol = pattern[dy][dx]
                if symbol != ' ':
                    self.relational_map.append((dx, dy, symbol))

def move_cursor(x: int, y: int):
    sys.stdout.write(f"\033[{y};{x}H")

def render_character(x: int, y: int, symbol: str):
    move_cursor(x, y)
    sys.stdout.write(f"{symbol}")

def render(x: int, y: int, sprite: Sprite):
    for dx, dy, symbol in sprite.relational_map:
        target_x = x + dx
        target_y = y + dy
        
        render_character(target_x, target_y, symbol)

def main():
    sys.stdout.write(CLEAR_SCREEN)
    frame = Sprite(size_x=10,
                    size_y=10,
                    pattern = [
                        list('#' * 10),
                        ['#', ' ',' ',' ',' ',' ',' ',' ',' ','#'],
                        ['#', ' ',' ',' ',' ',' ',' ',' ',' ','#'],
                        ['#', ' ',' ',' ',' ',' ',' ',' ',' ','#'],
                        ['#', ' ',' ',' ',' ',' ',' ',' ',' ','#'],
                        ['#', ' ',' ',' ',' ',' ',' ',' ',' ','#'],
                        ['#', ' ',' ',' ',' ',' ',' ',' ',' ','#'],
                        ['#', ' ',' ',' ',' ',' ',' ',' ',' ','#'],
                        ['#', ' ',' ',' ',' ',' ',' ',' ',' ','#'],
                        ['#', '#','#','#','#','#','#','#','#','#'],
                        ]
                    )

    render(5,5,frame)

if __name__ == "__main__":
    main()
