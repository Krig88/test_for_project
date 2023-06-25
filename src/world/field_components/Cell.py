from src.world.actors import Actor
from dataclasses import dataclass


@dataclass
class Cell:
    passable: bool = True
    actor: Actor = None
    position: tuple[int, int] = (0, 0) 
    