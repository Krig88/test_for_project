from  src.world.actors.Actor import Actor 
from Cell import Cell

class Field:
    def __init__(
        self, 
        actors: dict[Actor:(int,int)],
        cells: list[list[Cell]]
    ) -> None:
        raise NotImplementedError()
    
    def move(
            actor: Actor,
            direction: tuple[int, int]
    )->None: 
        print("do something")