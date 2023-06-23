from src.world import Cell
from src.world.actors import Actor


class DogCat(Actor):
    def __init__(self, cell: Cell, score_diff: int = 0) -> None:
        raise NotImplementedError()
