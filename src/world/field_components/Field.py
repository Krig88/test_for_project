from world.actors.Actor import Actor
from world.actors.Player import Player
from world.actors.DogCat import DogCat
from .Cell import Cell


class Field:
    def __init__(self, cells: list[list[Cell]], field_size: tuple[int, int], actors: dict[Actor:tuple[int, int]] = None) -> None:
        self.actors = {}
        self.cells = cells
        self.field_size = field_size

    def move(self, actor: Actor, direction: tuple[int, int]) -> None:
        cur_position = self.actors[actor]
        
        #step_to = (cur_position[0] + direction[0], cur_position[1] + cur_position[1])
        # write out-of-bounds check
        #if not self.cells[step_to[0]][step_to[1]].passable:
        #   raise Exception

        step_to = self.out_of_bounds_check(cur_position, direction)
        
        print('step to: |', step_to[0], ' ' ,step_to[1], '|')

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

            #self.cells[cur_position[0]][cur_position[1]].actor = None 

        #step_to_actor, self.cells[cur_position[0]][cur_position[1]].actor = actor, None
        self.cells[step_to[0]][step_to[1]].actor = actor
        self.cells[cur_position[0]][cur_position[1]].actor = None 
        self.actors[actor] = step_to
        
    def set_actor(self, new_actor: Actor, actor_pos: tuple[int,int]) -> None:
        if  not self.cells[actor_pos[0]][actor_pos[1]].actor:
            self.cells[actor_pos[0]][actor_pos[1]].actor = new_actor 
            self.actors[new_actor] = actor_pos
        else:
            raise Exception
    
    def out_of_bounds_check(self, cur_position: tuple[int, int], direction: tuple[int,int]):
        step_to_cords = (cur_position[0]+direction[0], cur_position[1]+direction[1])
        
        if step_to_cords[0] < 0 or step_to_cords[0] >= self.field_size[0] or step_to_cords[1] < 0 or step_to_cords[1] >= self.field_size[1]:
            raise Exception

        
        return step_to_cords

