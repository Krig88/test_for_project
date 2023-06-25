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

        if not self.cells[step_to[0]][step_to[1]].passable:
            raise Exception

        step_to_actor = self.cells[step_to[0]][step_to[1]].actor

        if isinstance(actor, DogCat) ^ isinstance(step_to_actor, DogCat):
            raise Exception

        if step_to_actor:
            dog_cat = step_to_actor if isinstance(step_to_actor, DogCat) else actor
            player = step_to_actor if isinstance(step_to_actor, Player) else actor
            player.interact_with(dog_cat)

            if actor is dog_cat:
                return

        step_to_actor, self.cells[cur_position[0]][cur_position[1]].actor = actor, None
        self.actors[actor] = step_to
