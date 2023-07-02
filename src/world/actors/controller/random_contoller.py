import random
from world.actors.actor import Actor
from world.actors.controller.abstract_controller import AbstractController
from world.field.field import Field
from world.coordinates import Coordinates
from environment import Environment


class RandomController(AbstractController):
    def __init__(self, field: Field, actors: list[Actor], is8=False, env: Environment = None):
        super().__init__(field, actors, is8)

    def make_decision(self, state: list = None) -> list[tuple[Actor, Coordinates]]:
        results = []
        for actor in self.actors:
            if not self.is8:
                v = random.randint(-1, 1)
                h = 0
                if v == 0:
                    h = random.randint(0, 1)
                    if h == 0:
                        h = -1
                results.append((actor, Coordinates(v, h)))
            results.append((actor, Coordinates(random.randint(-1, 1), random.randint(-1, 1))))
        return results
