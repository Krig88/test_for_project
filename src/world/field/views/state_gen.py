from src.environment import Environment
from src.world.actors.cat import Cat
from src.world.actors.dog import Dog
from src.world.coordinates import Coordinates
from src.world.field.field import Field
from src.world.actors.actor import Actor


class StateGen:
    def __init__(self, field: Field, env: Environment = None) -> None:
        self.field = field
        self.env = env

    def get_state(self, actor: Actor) -> list[list[int]]:
        state = [[0 for _ in range(3)] for _ in range(4)]
        coordinates = self.field.actors[actor]
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
                if isinstance(cell.actor, Dog):
                    state[i][1] = 1
                    continue
                if isinstance(cell.actor, Cat):
                    state[i][2] = 1
                    continue
        return state
