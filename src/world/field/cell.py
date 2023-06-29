from dataclasses import dataclass

from world.actors.actor import Actor


class Cell:
    def __init__(self, passable: bool = True, symbol: chr = ".", actor: Actor = None):
        self.passable = passable
        self.symbol = "." if passable else "#"
        self.actor = actor

    # TODO: passable property
