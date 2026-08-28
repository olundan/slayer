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
            maze_height = 13
            maze_width = 41
            if not self.maze:
                self.maze = self.generate_prims_maze(maze_width, maze_height)
                self.player.x, self.player.y = self.calculate_center(maze_width, maze_height)

            try:
                match action:
                    case Action.UP:
                        self.player.y -= 1
                        if self.cordinates_is_wall(self.player.x, self.player.y):
                            self.player.y += 1
                    case Action.DOWN:
                        self.player.y += 1
                        if self.cordinates_is_wall(self.player.x, self.player.y):
                            self.player.y -= 1
                    case Action.LEFT:
                        self.player.x -= 1
                        if self.cordinates_is_wall(self.player.x, self.player.y):
                            self.player.x += 1
                    case Action.RIGHT:
                        self.player.x += 1
                        if self.cordinates_is_wall(self.player.x, self.player.y):
                            self.player.x -= 1
            except IndexError:
                self.escaped = True
        else:
            return SceneID.ENDING
        return None

    def cordinates_is_wall(self, x: int, y: int) -> bool:
        return self.maze[y][x] == 1

    def draw(self):
        map_sprite = Sprite(self.maze_to_string(self.maze))
        self.display.add_sprite(0,0, map_sprite)
        self.display.add_sprite(self.player.x, self.player.y, Sprite("@"))

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
