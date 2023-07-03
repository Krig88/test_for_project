import random

from src.environment import Environment
from src.world.actors.actor import Actor
from src.world.actors.controller.abstract_controller import AbstractController
from src.world.coordinates import Coordinates
from src.world.field.field import Field


class RandomController(AbstractController):
    def __init__(self, field: Field, actors: list[Actor], env: Environment = None):
        super().__init__(field, actors)

    def make_decision(self, state: list = None) -> list[tuple[Actor, Coordinates]]:
        results = []
        for actor in self.actors:
            v = random.randint(-1, 1)
            h = 0
            if v == 0:
                h = random.randint(0, 1)
                if h == 0:
                    h = -1
            results.append((actor, Coordinates(v, h)))
            #results.append((actor, Coordinates(random.randint(-1, 1), random.randint(-1, 1))))
        return results
