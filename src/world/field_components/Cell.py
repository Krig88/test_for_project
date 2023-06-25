from typing import Any
from actors import Actor


class Cell:
    def __init__(self,
                 passable: bool = True,
                 actor: Actor = None,
                 position: tuple[int, int] = (0, 0),
                 neighbours: dict = None) -> None: 
        raise NotImplementedError()
    
#getters block (mb use getatter?)
    def get_passable(self)-> bool:
        return self.passable 
    def get_actor(self) -> Actor:
        return self.actor
    def get_position(self)-> tuple[int, int]:
        return self.position
    def get_neighbours(self)->dict:
        return dict
    
#setters block
    def set_passable(self, received_passability:bool) -> None:
        self.passable = received_passability
    def set_actor(self, received_actor:Actor) -> None:
        self.actor = received_actor
    def set_position(self, recieved_position: tuple[int, int]) -> None:
        self.position = recieved_position
    def set_neighbours(self, resieved_neighbours: dict) -> None:
        self.neighbours = resieved_neighbours