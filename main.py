import random
import time
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
HIGHLIGHT = "\033[7m"  
RESET = "\033[0m"

def move_cursor(x: int, y: int):
    sys.stdout.write(f"\033[{y};{x}H")

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

def get_character_name() -> str:
    while True:
        min_name_size = 2
        max_name_size = 10
        character_name = input("Vad är ditt namn kämpe?\n").strip().capitalize() or "Hjälte"
        if not len(character_name) > min_name_size or len(character_name) > max_name_size:
            print(f"Giltigt namn är {min_name_size}-{max_name_size} långt och får endast innehålla bokstäver.")
        else:
            print(f"Så ditt namn är {character_name}... din resa kommer att vara lång och svår. Faror runt varje hörn. Lycka till")
            input("Tryck på valfri tangent för att fortsätta..")
            return character_name.strip(' ').capitalize()

def get_character_class() -> CharacterClass:
    classes = list(CharacterClass)
    print("Vilken typ av kämpe är du?")
    print("Din klass avgör vilka förmågor din karaktär kan lära sig.")
    for index, charClass in enumerate(classes, start=1):
        print(f"{index}. {charClass.class_name}\n{charClass.description}")

    while True:
        choice = input(f"Ange 1-{len(classes)} för att välja klass \n")
        if choice.isdigit():
            validated_choice = int(choice)
            if 1 <= validated_choice <= len(classes):
                print(f"Du valde klassen: {classes[validated_choice -1].class_name}")
                input("Tryck på valfri tangent för att fortsätta..")
                return classes[validated_choice - 1]
        print(f"Ogiltigt val. Försök igen.")

def create_character() -> PlayerCharacter:
    while True:
        character_name = get_character_name()
        character_class = get_character_class()
        return PlayerCharacter(character_name, character_class, character_class.initial_stats)

def main():
    sys.stdout.write(HIDE_CURSOR)
    sys.stdout.write(CLEAR_SCREEN)
    render_string_slow(0,0,"Du vaknar upp*")
    sys.stdout.write(CLEAR_SCREEN)
    render_string_slow(0,0,"Du drömde om att någonting jagade dig... Nu inser du att det kanske inte var en dröm.")
    sys.stdout.write(CLEAR_SCREEN)
    render_string_slow(0,0,"Omkring dig ser du endast mörka korridorer.")
    sys.stdout.write(CLEAR_SCREEN)
    render_string_slow(0,0,'"Vart är jag? - Hinner du fråga dig själv innan du hör en röst."')
    player_character = create_character()
    print(player_character)

if __name__ == "__main__":
    main()


