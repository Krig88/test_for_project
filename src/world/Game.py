from src.world import Cell
from src.world.actors import Actor


class Game:
    def __init__(self,
                 field: Cell,
                 actors: list[Actor]) -> None:
        raise NotImplementedError()

    def start(self):
        raise NotImplementedError()
