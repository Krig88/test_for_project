from src.environment import Environment
from src.world.actors.actor import Actor
from src.world.actors.cat import Cat
from src.world.actors.dog import Dog
from src.world.field.field import Field


class StateGen:
    def __init__(self, field: Field, env: Environment = None) -> None:
        self.field = field
        self.env = env

    def get_state(self, actor: Actor) -> list[list[int]]:
        state = [0]*12
        coordinates = self.field.actors[actor]
        near_cells = self.env.get_near_cells(coordinates)
        for i in range(0, 12, 3):
            if near_cells[i//3] is None:
                state[i] = 1
                continue
            cell = self.field.get_cell_at(near_cells[i//3])
            if not cell.passable:
                state[i] = 1
                continue
            if cell.actor is not None:
                if isinstance(cell.actor, Dog):
                    state[i+1] = 1
                    continue
                if isinstance(cell.actor, Cat):
                    state[i+2] = 1
                    continue
        return state
