from __future__ import annotations
from src.world import Cell
from src.world.actors import Actor
from src.world import Generator


class Game:
    def __init__(self,
                 field: Cell,
                 actors: list[Actor]) -> None:
        raise NotImplementedError()

    def start(self):
        raise NotImplementedError()
