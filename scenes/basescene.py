from abc import ABC, abstractmethod
from core import SceneID

class Scene(ABC):
    @abstractmethod
    def __init__(self, game):
        self.display = game.display
        self.player = game.player

    @abstractmethod
    def update(self, action) -> SceneID | None:
        pass

    @abstractmethod
    def draw(self)
        pass
