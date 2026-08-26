import curses
from enum import Enum, auto

class test_menu(Enum):
    Attack = auto()
    Run = auto()

class MenuHandler():
    def get_menu_items(self,menu) -> list[tuple[int, str]]:
        items = []
        for index, option in enumerate(menu):
            items.append((index, option.name))
        return items



