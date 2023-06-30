from world.actors.actor import Actor
from world.actors.player import Player
from world.field.cell import Cell
from world.coordinates import Coordinates
import random


class Field:
    # TODO: rewrite with overflow_function
    def __init__(self, cells: list[list[Cell]], is8: bool = False, overflow_function=None) -> None:
        self.cells = cells
        self.size = Coordinates(len(cells), len(cells[0]))
        self._is8 = is8
        self.actors = dict()
        self.overflow_function = overflow_function

    def dist(self, src: Coordinates, to: Coordinates) -> int:
        if self._is8:
            return NotImplemented
        return abs(src.x - to.x) + abs(src.y - to.y)

    def place_actor(self, actor: Actor, coordinates: Coordinates) -> None:
        if actor in self.actors:
            raise ValueError(f"actor already on board")
        cell = self.cells[coordinates.x][coordinates.y]
        if cell.actor is not None:
            raise ValueError(f"cell at {coordinates} has actor!")
        cell.actor = actor
        self.actors[actor] = coordinates

    def place_wall(self, coordinates: Coordinates) -> None:
        cell = self.cells[coordinates.x][coordinates.y]
        if cell.passable and (not cell.actor):
            cell.passable, cell.symbol = False, '#'
        else:
            raise Exception
    def get_cell_at(self, coordinates: Coordinates) -> Cell:
        if 0 <= coordinates.x < self.size.x and 0 <= coordinates.y < self.size.y:
            return self.cells[coordinates.x][coordinates.y]
        # TODO: rewrite with overflow_function
        raise IndexError


