from dataclasses import dataclass

from world.actors.actor import Actor


@dataclass
class Cell:
    passable: bool = True
    symbol: chr = "." if passable else "#"
    actor: Actor = None
