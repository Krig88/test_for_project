from src.world.actors.Actor import Actor
from src.world.actors.Player import Player
from src.world.actors.DogCat import DogCat
from Cell import Cell


class Field:
    def __init__(self, actors: dict[Actor:(int, int)], cells: list[list[Cell]]) -> None:
        self.actors = actors
        self.cells = cells
    
    def move(self, actor: Actor, direction: tuple[int, int]) -> None:
        cur_position = self.actors[actor]
        step_to = (cur_position[0] + direction[0], cur_position[1] + cur_position[1])

        # write out-of-bounds check

        if self.cells[step_to[1]][step_to[0]].passable:
            if self.cells[step_to[1]][step_to[0]].actor:
                if isinstance(actor, Player):
                    self.cells[step_to[1]][step_to[0]].actor.interact_with(actor)
                else:
                    pass

            self.cells[step_to[1]][step_to[0]].actor, self.cells[cur_position[1]][cur_position[0]].actor = actor, None
            self.actors[actor] = step_to

        