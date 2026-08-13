import random
from enum import Enum
import sys
import os
from data import *
# Microslop compgarbage
if sys.platform == "win32":
    os.system("")  # Enables ANSI/VT100

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')  #UTF-8

CLEAR_SCREEN = "\033[2J"
HIDE_CURSOR  = "\033[?25l"
SHOW_CURSOR  = "\033[?25h"

def move_cursor(x: int, y: int):
    sys.stdout.write(f"\033[{y};{x}H")

def renderChar(x: int, y: int, symbol: str):
    move_cursor(x, y)
    sys.stdout.write(f"{symbol}")

def renderString(x: int, y: int, s: str):
    move_cursor(x, y)
    sys.stdout.write(f"{s}")

def render(x: int, y: int, render_obj):
    if isinstance(render_obj, Sprite):
        for dx, dy, symbol in render_obj.relational_map:
            target_x = x + dx
            target_y = y + dy

            renderChar(target_x, target_y, symbol)
    elif isinstance(render_obj, str):
        renderString(x, y, render_obj)


#def renderBattleScene(player, monster):
    #    sys.stdout.write(SHOW_CURSOR)
#    sys.stdout.write(CLEAR_SCREEN)
#    sys.stdout.write(HIDE_CURSOR)
#    test_text = Sprite("XP 10/55")
#    test_hp = Sprite("HP 32/50")
#    ability1 = Sprite("1.Attack1")
#    ability2 = Sprite("2.Attack2")
#    ability3 = Sprite("3.Attack3")
#    ability4 = Sprite("4.Attack4")
#    render(5,8,player.sprite)
#    render(30,3,monster.sprite)
#    render(19,2, monster.name)
#    render(1,1,frame)
#    render(3,2,test_text)
#    render(3,12, "Text")
#    render(30,2,test_hp)
#    render(18,11, ability1)
#    render(18,12, ability2)
#    render(29,11, ability3)
#    render(29,12, ability4)
#    input()

def main():

    player = Player(name="Hero", class_type=CharacterClass.WARRIOR, stats=CharacterClass.WARRIOR.initial_stats)
    print(f"{player.name}")
    print(f"{player.class_type.display_name}")
    print(f"{player.stats.hp}")
    print(f"{player.stats.attack}")

if __name__ == "__main__":
    main()
