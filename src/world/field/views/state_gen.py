from world.field.field import Field
from world.field.views.abstract_view import AbstractView
from world.coordinates import Coordinates
from environment import Environment
from world.actors.cat import Cat
from world.actors.dog import Dog


class StateGen:

    def __init__(self, field: Field, env: Environment = None) -> None:
        self.field = field
        self.env = env

    def get_state(self, coordinates: Coordinates) -> list[list[int]]:
        state = [[0 for _ in range(3)] for _ in range(4)]
        near_cells = self.env.get_near_cells(coordinates)
        for i in range(0, len(near_cells)):
            if near_cells[i] is None:
                state[i][0] = 1
                continue
            cell = self.field.get_cell_at(near_cells[i])
            if not cell.passable:
                state[i][0] = 1
                continue
            if cell.actor is not None:
                if isinstance(cell.actor, Cat):
                    state[i][1] = 1
                    continue
                if isinstance(cell.actor, Cat):
                    state[i][2] = 1
                    continue
        return state
