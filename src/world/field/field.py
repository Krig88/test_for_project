import logging

from src.world.actors.actor import Actor
from src.world.coordinates import Coordinates
from src.world.field.cell import Cell


class Field:
    def __init__(self, cells: list[list[Cell]]) -> None:
        self.cells = cells
        self.size = Coordinates(len(cells), len(cells[0]))
        self.actors = dict()

    def place_actor(self, actor: Actor, coordinates: Coordinates) -> None:
        if actor in self.actors and self.actors[actor]:
            logging.error(f"actor already on board")
            raise ValueError(f"actor already on board")
        cell = self.cells[coordinates.x][coordinates.y]
        if cell.actor is not None:
            logging.error("cell at {coordinates} has actor!")
            raise ValueError(f"cell at {coordinates} has actor!")
        cell.actor = actor
        self.actors[actor] = coordinates

    def place_wall(self, coordinates: Coordinates) -> None:
        cell = self.cells[coordinates.x][coordinates.y]
        if cell.passable and (not cell.actor):
            cell.passable = False
            return
        logging.error("Index Error trying to place wall at %s, field size is %s", coordinates, self.size)
        raise IndexError

    def get_cell_at(self, coordinates: Coordinates) -> Cell:
        if 0 <= coordinates.x < self.size.x and 0 <= coordinates.y < self.size.y:
            return self.cells[coordinates.x][coordinates.y]
        logging.error("Index Error trying to get cell at %s", coordinates)
        raise IndexError

    def is_clear(self, coordinates: Coordinates) -> bool:
        cell = self.get_cell_at(coordinates)
        if cell.passable and (cell.actor is None):
            return True
        return False

    def move_actor(self, cur_pos: Coordinates, destination_pos: Coordinates) -> None:
        # from -> to
        pos_cell, destination_cell = self.get_cell_at(cur_pos), self.get_cell_at(destination_pos)
        destination_cell.actor, pos_cell.actor = pos_cell.actor, None
        self.actors[destination_cell.actor] = destination_pos
        logging.info("actor %s moved from %s to %s", destination_cell.actor, cur_pos, destination_pos)

