from src.world.field_components import Cell
from src.world.actors import Actor


class Player(Actor):
    def __init__(self, distance_of_view: int  =1, 
                 score: int = 0) -> None:
        self.distance_of_view = distance_of_view
        self.score = score
    
    def interact_with(self, actor:Actor)->None:
        pass 

