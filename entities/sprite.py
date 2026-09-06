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
    
    def cropped(self, start_x: int, start_y: int, end_x: int, end_y: int):
        new_sprite = Sprite("") 
        new_pattern = [row[start_x:end_x] for row in self.pattern[start_y:end_y]]
        new_sprite.pattern = new_pattern
        
        new_sprite.relational_map = [
            (dx - start_x, dy - start_y, symbol)
            for dx, dy, symbol in self.relational_map
            if start_x <= dx < end_x and start_y <= dy < end_y
        ]
        return new_sprite


