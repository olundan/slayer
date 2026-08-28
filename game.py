import random
import curses
import time
from enum import Enum, auto
from entities import Player, Stats
from displaybuffer import DisplayBuffer
from sprites import text_frame, frame, warrior_sprite, cyclops_sprite
from sprite import Sprite
from inputhandler import InputHandler, Action
from uihandler import UIHandler

class IntroScene():
    def __init__(self):
        pass

    def update(self, action):
        return None

    def draw(self, display):
        pass

class RoamingScene():
    def __init__(self, player):
        self.maze = []
        self.player = player

    def update(self, action):
        maze_height = 13
        maze_width = 39
        if not self.maze:
            self.maze = self.generate_prims_maze(maze_width, maze_height)

        return None

    def draw(self, display):
        map_sprite = Sprite(self.maze_to_string(self.maze))
        display.add_sprite(0,0, map_sprite)

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

        start_x = (width // 2) if (width // 2) % 2 != 0 else (width // 2) - 1
        start_y = (height // 2) if (height // 2) % 2 != 0 else (height // 2) - 1

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



class Game():
    def __init__(self, curses_window):
        #modules
        self.display = DisplayBuffer(curses_window)
        self.input = InputHandler(curses_window)
        self.ui = UIHandler()

        #game objects
        self.player = Player(name="Oskar", sprite=warrior_sprite,stats=Stats(hp=10, attack=10, defence=10), x=0, y=0)
        self.current_scene = RoamingScene(self.player)
        self.is_running = True
    
    def run(self):
        self.update()

    def update(self):
        action = self.input.get_action()
        next_scene = self.current_scene.update(action)
        
        if next_scene:
            self.current_scene = next_scene

        self.display.clear_buffer()
        self.current_scene.draw(self.display)
        self.display.render_buffer()

    def print_message(self, message):
        self.display.add_sprite(1,8, text_frame)
        self.display.add_string(3,9, message)
