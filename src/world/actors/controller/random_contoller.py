import random
from world.actors.actor import Actor
from world.actors.controller.abstract_controller import AbstractController
from world.field.field import Field


class RandomController(AbstractController):
    def __init__(self, field: Field, actor: Actor, is8=False):
        super().__init__(field, actor, is8)

    def make_decision(self) -> tuple[int, int]:
        if not self.is8:
            v = random.randint(-1, 1)
            h = 0
            if v == 0:
                h = random.randint(0, 1)
                if h == 0:
                    h = -1
            return v, h
        return random.randint(-1, 1), random.randint(-1, 1)
