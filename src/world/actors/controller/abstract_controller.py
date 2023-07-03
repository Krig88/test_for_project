from abc import ABC, abstractmethod
from environment import Environment
from world.actors.actor import Actor
from world.field.field import Field
from world.coordinates import Coordinates


class AbstractController(ABC):
    def __init__(self, field: Field, actors: list[Actor], env: Environment = None):
        self.field = field
        self.actors = actors
        self.env = env

    @abstractmethod
    def make_decision(self, state: list = None) -> list[tuple[Actor, Coordinates]]:
        raise NotImplemented
