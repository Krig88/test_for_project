from abc import ABC, abstractmethod

from world.actors.actor import Actor
from world.field.field import Field
from world.coordinates import Coordinates

class AbstractController(ABC):
    def __init__(self, field: Field, actor: Actor, is8=False):
        self.field = field
        self.actor = actor
        self.is8 = is8

    @abstractmethod
    def make_decision(self) -> Coordinates:
        raise NotImplemented
