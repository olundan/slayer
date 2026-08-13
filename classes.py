### BASE CLASSES ####
from enum import Enum
from dataclasses import dataclass

@dataclass
class Stats():
    hp: int
    attack: int
    
class CharacterClass(Enum):
    WARRIOR = ("Krigare", "Du löser alla dina problem med våld.")
    PRIEST = ("Präst", "Ett liv av bön har gett dig förmågan att kalla på gud för att läka sår.")
    ROUGE= ("Tjuv", "Ett liv på gatan har gett dig snabba reflexer och tivivelaktig moral.")

    def __init__(self, display_name: str, description: str):
        self.display_name = display_name
        self.description = description

    @property
    def initial_stats(self) -> Stats:
        match self:
            case CharacterClass.WARRIOR:
                return Stats(
                        hp = 20,
                        attack = 10
                        )
            case CharacterClass.PRIEST:
                return Stats(
                        hp = 10,
                        attack = 5
                        )
            case CharacterClass.ROUGE:
                return Stats(
                        hp = 15,
                        attack = 8
                        )

@dataclass
class Player:
    name: str
    class_type: CharacterClass
    stats: Stats






class Sprite:
    def __init__(self, str_sprite: str):
        pattern = self.BuildPattern(str_sprite)

        self.relational_map: list[tuple[int,int,str]] = []
        for dy in range(len(pattern)):
            for dx in range(len(pattern[dy])):
                symbol = pattern[dy][dx]
                if symbol != ' ':
                    self.relational_map.append((dx, dy, symbol))

    def BuildPattern(self, str_sprite: str):
        return [list(line) for line in str_sprite.strip('\n').split('\n')]

