from abc import ABC, abstractmethod

from src.world.actors.Actor import Actor
from src.world.field_components.Field import Field


class ActorController(ABC):
    def __init__(self, field: Field, actor: Actor) -> None:
        self.field = field
        self.actor = actor

    def make_move(self) -> None:
        try:
            direction = self.choose_direction()
            self.field.move(self.actor, direction)
            return
        except:
            ...

    @abstractmethod
    def choose_direction(self) -> tuple[int, int]:
        ...
