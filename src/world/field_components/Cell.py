from world.actors.Actor import Actor
from dataclasses import dataclass


@dataclass
class Cell:
    passable: bool = True
    actor: Actor = None
