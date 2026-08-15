import random
import time
from enum import Enum
import sys
import os
from data import *
from render import render, render_string_slow
from game_state import Game, GameState

# Microslop compgarbage
if sys.platform == "win32":
    os.system("")  # Enables ANSI/VT100

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')  #UTF-8

CLEAR_SCREEN = "\033[2J"
HIDE_CURSOR  = "\033[?25l"
SHOW_CURSOR  = "\033[?25h"
HIGHLIGHT = "\033[7m"  
RESET = "\033[0m"




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
    game = Game()
    game.update()

if __name__ == "__main__":
    main()


