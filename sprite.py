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

