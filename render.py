import sys
import time

def render_string(x: int, y: int, txt: str):
    move_cursor(x, y)
    sys.stdout.write(f"{symbol}")

def render_string_slow(x: int, y: int, txt: str):
    move_cursor(x, y)
    for char in txt:
        sys.stdout.write(f"{char}")
        sys.stdout.flush()
        time.sleep(0.05)

def render(x: int, y: int, render_obj):
    if isinstance(render_obj, Sprite):
        for dx, dy, symbol in render_obj.relational_map:
            target_x = x + dx
            target_y = y + dy

            render_char(target_x, target_y, symbol)
    elif isinstance(render_obj, str):
        render_string(x, y, render_obj)

def move_cursor(x: int, y: int):
    sys.stdout.write(f"\033[{y};{x}H")
