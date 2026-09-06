import random
import curses
import time
from enum import Enum, auto

from core import Stats, Entity, Player, Sprite, SceneID
from engine import Action

class RoamingScene():
    def __init__(self, game):
        self.game = game
        self.display = game.display
        self.player = game.player
        self.maze = []
        self.escaped = False

    def update(self, action) -> SceneID | None:
        if not self.escaped:
            maze_height, maze_width = (10, 41)
            if not self.maze:
                self.maze = self.generate_ascii_maze(maze_width, maze_height)
                self.player.x, self.player.y = (15,15)

            try:
                match action:
                    case Action.UP:
                        self.player.y -= 1
                    case Action.DOWN:
                        self.player.y += 1
                    case Action.LEFT:
                        self.player.x -= 1
                    case Action.RIGHT:
                        self.player.x += 1
            except IndexError:
                self.escaped = True
        else:
            return SceneID.ENDING

        return None

    def cordinates_is_wall(self, x: int, y: int) -> bool:
        return self.maze[y][x] == 1

    def draw(self):
        crop_start_x = self.player.x - 10
        crop_start_y = self.player.y - 5
        crop_end_x = self.player.x + 10
        crop_end_y = self.player.y + 5
        map_sprite = Sprite(self.maze_to_string(self.maze))
        self.display.add_sprite(0,0, map_sprite.cropped(crop_start_x,crop_start_y,crop_end_x,crop_end_y))
        self.display.add_sprite(10,5, Sprite("@"))

    def generate_ascii_maze(self, width: int, height: int, scale: int = 2) -> list[list[int]]:
        base_maze = self.generate_prims_maze(width, height)
        actual_height = len(base_maze)
        actual_width = len(base_maze[0])

        scaled_height = actual_height * scale
        scaled_width = actual_width * scale

        # 1 represents wall, 0 represents path
        scaled_grid = [[1 for _ in range(scaled_width)] for _ in range(scaled_height)]

        for y in range(actual_height):
            for x in range(actual_width):
                if base_maze[y][x] == 0:
                    for dy in range(scale):
                        for dx in range(scale):
                            scaled_grid[y * scale + dy][x * scale + dx] = 0

        return scaled_grid

    def maze_to_string(self, maze: list[list[int]], wall_char: str = "█", path_char: str = " ") -> str:
        return "\n".join(
            "".join(wall_char if cell == 1 else path_char for cell in row)
            for row in maze
        )
    
    def generate_prims_maze(self, width: int, height: int) -> list[list[int]]:
        # Dimensions muust be uneven
        if width % 2 == 0:
            width += 1
        if height % 2 == 0:
            height += 1

        maze = [[1 for _ in range(width)] for _ in range(height)]

        start_x, start_y = self.calculate_center(width, height)

        maze[start_y][start_x] = 0

        frontier = []

        def add_frontier(cx: int, cy: int):
            directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 < nx < width - 1 and 0 < ny < height - 1:
                    if maze[ny][nx] == 1:
                        frontier.append((cx + dx // 2, cy + dy // 2, nx, ny))

        add_frontier(start_x, start_y)

        while frontier:
            idx = random.randint(0, len(frontier) - 1)
            wx, wy, nx, ny = frontier.pop(idx)

            if maze[ny][nx] == 1:
                maze[wy][wx] = 0  
                maze[ny][nx] = 0 
                add_frontier(nx, ny)

        maze[height - 2][width - 1] = 0  # Single Exit

        return maze
    
    def calculate_center(self, width:int, height: int) -> (int, int):
        center_x = (width // 2) if (width // 2) % 2 != 0 else (width // 2) - 1
        center_y = (height // 2) if (height // 2) % 2 != 0 else (height // 2) - 1
        return (center_x, center_y)

    def print_message(self, message):
        self.display.add_sprite(1,8, text_frame)
        self.display.add_string(3,9, message)
