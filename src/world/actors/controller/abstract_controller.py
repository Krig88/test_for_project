from abc import ABC, abstractmethod

from src.environment import Environment
from src.world.actors.actor import Actor
from src.world.coordinates import Coordinates
from src.world.field.field import Field


class AbstractController(ABC):
    def __init__(self, field: Field, actors: list[Actor], env: Environment = None):
        self.field = field
        self.actors = actors
        self.env = env

    @abstractmethod
    def make_decision(self, state: list = None) -> list[tuple[Actor, Coordinates]]:
        raise NotImplemented
