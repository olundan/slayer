import random
import curses
import time
from enum import Enum, auto

from core import Stats, Entity, Player, Sprite, SceneID
from engine import Action, Camera

class RoamingScene():
    def __init__(self, game):
        self.reset(game)

    def update(self, action) -> SceneID | None:
        if not self.escaped:
            if not self.maze:
                scale = 3
                self.maze = self.generate_scaled_ascii_maze(self.maze_width, self.maze_height, scale)
                self.player.x, self.player.y = self.calculate_center(self.maze_width * scale, self.maze_height * scale)

            match action:
                case Action.UP:
                    self.try_move(self.player, dx=0, dy=-1)
                    if self.combat_roll():
                        return SceneID.BATTLE
                case Action.DOWN:
                    self.try_move(self.player, dx=0, dy=1)
                    if self.combat_roll():
                        return SceneID.BATTLE
                case Action.LEFT:
                    self.try_move(self.player, dx=-1, dy=0)
                    if self.combat_roll():
                        return SceneID.BATTLE
                case Action.RIGHT:
                    self.try_move(self.player, dx=1, dy=0)
                    if self.combat_roll():
                        return SceneID.BATTLE


        else:
            self.reset(self.game)
            return SceneID.ENDING

        return None

    def try_move(self, character, dx: int, dy: int):
        new_x = character.x + dx
        new_y = character.y + dy

        if not self.cordinates_is_wall(new_x, new_y):
            character.x = new_x
            character.y = new_y

    def cordinates_is_wall(self, x: int, y: int) -> bool:
        #bug wating to happen (gonna fix soon tm)
        try:
            return self.maze[y][x] == 1
        except IndexError:
            self.escaped = True
    
    def combat_roll(self):
        i = random.randint(0,100)
        if i < 1:
            return True
        else:
            False

    def draw(self):
        camera = Camera(width=41, height=13)
        camera.follow(self.player.x, self.player.y)
        camera.draw_sprite(self.display, 0, 0, Sprite(self.maze_to_string(self.maze)))
        camera.draw_sprite(self.display, self.player.x, self.player.y, Sprite("@"))
        
        debug_camera = Camera(width=80, height=24)
        debug_camera.draw_sprite(self.display, 45,0, Sprite(f"Player_x: {self.player.x}"))
        debug_camera.draw_sprite(self.display, 45,1, Sprite(f"Player_y: {self.player.y}"))

    def generate_scaled_ascii_maze(self, width: int, height: int, scale: int = 3) -> list[list[int]]:
        # Dimensions must be odd
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

        maze[height - 2][width - 1] = 0  # Single Exit (wants to be updated to randomize)
        center_y, center_x = height // 2, width // 2
        maze[center_y][center_x] = 0
        maze[center_y][center_x + 1] = 0
        maze[center_y][center_x + 2] = 0
        maze[center_y][center_x + 3] = 0
        maze[center_y][center_x - 1] = 0
        maze[center_y][center_x - 2] = 0
        maze[center_y][center_x - 3] = 0
        maze[center_y + 1][center_x] = 0
        maze[center_y + 2][center_x] = 0
        maze[center_y + 3][center_x] = 0

        scaled_height = height * scale
        scaled_width = width * scale
        scaled_grid = [[1 for _ in range(scaled_width)] for _ in range(scaled_height)]

        for y in range(height):
            for x in range(width):
                if maze[y][x] == 0:
                    for dy in range(scale):
                        for dx in range(scale):
                            scaled_grid[y * scale + dy][x * scale + dx] = 0

        return scaled_grid

    def maze_to_string(self, maze: list[list[int]], wall_char: str = "█", path_char: str = " ") -> str:
        return "\n".join(
            "".join(wall_char if cell == 1 else path_char for cell in row)
            for row in maze
        )
    
    
    def calculate_center(self, width:int, height: int) -> (int, int):
        center_x = (width // 2) if (width // 2) % 2 != 0 else (width // 2) - 1
        center_y = (height // 2) if (height // 2) % 2 != 0 else (height // 2) - 1
        return (center_x, center_y)

    def print_message(self, message):
        self.display.add_sprite(1,8, text_frame)
        self.display.add_string(3,9, message)

    def reset(self, game):
        self.game = game
        self.display = game.display
        self.player = game.player
        self.maze = []
        self.maze_height = 19
        self.maze_width = 41
        self.escaped = False
