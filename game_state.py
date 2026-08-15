from enum import Enum, auto
from entities import *

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

class GameState(Enum):
    INTRO = auto()
    CHAR_CREATION = auto()
    EXPOSITION = auto()
    ROAM= auto()
    BATTLE = auto()

class Game():
    def __init__(self):
        self.state = GameState.CHAR_CREATION
        self.player_char = None

    def update(self):
        match self.state:
            case GameState.CHAR_CREATION:
                self.player_char = create_character()
                self.state = GameState.ROAM
                self.update()
            case GameState.ROAM:
                print(self.state)
            case GameState.EXPOSITON:
                print(self.state)
            case GameState.BATTLE:
                print(self.state)

