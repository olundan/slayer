from enum import Enum
from dataclasses import dataclass, field

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

    def __init__(self, display_name: str, description: str):
        self.display_name = display_name
        self.description = description

    @property
    def initial_stats(self) -> Stats:
        match self:
            case CharacterClass.WARRIOR:
                return Stats(hp=20, attack=10, defence=10)
            case CharacterClass.PRIEST:
                return Stats(hp=10, attack=5, defence=10)
            case CharacterClass.ROGUE:
                return Stats(hp=15, attack=8, defence=10)


class Sprite:
    def __init__(self, str_sprite: str):
        self.pattern = self.build_pattern(str_sprite)
        self.relational_map: list[tuple[int, int, str]] = self.build_rel_map()

    def build_pattern(self, str_sprite: str):
        return [list(line) for line in str_sprite.strip('\n').split('\n')]

    def build_rel_map(self) -> list[tuple[int, int, str]]:
        rel_map = []
        for dy in range(len(self.pattern)):
            for dx in range(len(self.pattern[dy])):
                symbol = self.pattern[dy][dx]
                if symbol != ' ':
                    rel_map.append((dx, dy, symbol))
        return rel_map
