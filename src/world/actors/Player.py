from src.world.field_components import Cell
from src.world.actors import Actor


class Player(Actor):
    def __init__(self, cell: Cell, score: int = 0) -> None:
        raise NotImplementedError()
