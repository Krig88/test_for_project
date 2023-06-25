from __future__ import annotations
from src.world import Cell


class Actor:
    def __init__(self, cell: Cell, distance_of_view: int = 1) -> None:
        raise NotImplementedError()

    def move(self, district: tuple[int, int]) -> None:    
        
       raise NotImplementedError()

    def get_area(self) -> str:
        raise NotImplementedError()

    def interaction(self, actor: Actor) -> None:
        raise NotImplementedError()
