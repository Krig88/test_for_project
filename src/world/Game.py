from __future__ import annotations
from src.world.field_components.Field import Field
from src.world.actors.Actor import Actor
from src.world.Generator import Generator


class Game:
    def __init__(self,
                 field: Field,
                 actors: list[Actor]) -> None:
        raise NotImplementedError()
        
    def start(self):
        raise NotImplementedError()
        
