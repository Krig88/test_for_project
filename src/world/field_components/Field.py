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

        if step_to_actor:

            if not(isinstance(actor, DogCat) ^ isinstance(step_to_actor, DogCat)):
                raise Exception
            
            #если один из экторов DogСat он делает  raise Exception 
            
            dog_cat = step_to_actor if isinstance(step_to_actor, DogCat) else actor
            player = step_to_actor if isinstance(step_to_actor, Player) else actor
            player.interact_with(dog_cat)

            self.cells[cur_position[0]][cur_position[1]].actor = None 
            # здесь не происходит отчистка догкэта, а по идее он должен проподать

        step_to_actor, self.cells[cur_position[0]][cur_position[1]].actor = actor, None
        self.actors[actor] = step_to
        
    def set_actor(self, actor: Actor, actor_pos: tuple(int,int)) -> None:
        if not(self.cells[actor_pos[0]][actor_pos[1]].actor):
            self.cells[actor_pos[0]][actor_pos[1]].actor = actor 
            self.actors[actor] = actor_pos
        else:
            raise Exception