from enum import Enum
from dataclasses import dataclass, field
from sprite import Sprite

@dataclass
class Stats:
    hp: int
    attack: int
    defence: int

@dataclass
class Entity:
    name: str
    sprite: Sprite
    stats: Stats

@dataclass
class Player(Entity):
    x: int = 0
    y: int = 0
    current_xp: int = 0
    role: str = "Adventurer"
    description: str = ""

@dataclass
class Mob(Entity):
    exp_gain: int = 10

class CharacterClass(Enum):
    WARRIOR = ("Warrior", "Våld")
    PRIEST = ("Priest", "Helande")
    ROGUE = ("Rogue", "Smygande")

    def __init__(self, name: str, description: str):
        self.class_name = name
        self.class_description = description

    @property
    def initial_stats(self) -> Stats:
        match self:
            case CharacterClass.WARRIOR:
                return Stats(hp=20, attack=10, defence=10)
            case CharacterClass.PRIEST:
                return Stats(hp=10, attack=5, defence=10)
            case CharacterClass.ROGUE:
                return Stats(hp=15, attack=8, defence=10)

