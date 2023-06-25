import random

from ActorController import ActorController
from src.world.field_components.Field import Field
from src.world.actors import Actor


class NpcController(ActorController):
    def __init__(self, field: Field, actor: Actor) -> None:
        super().__init__(field, actor)

    def choose_direction(self) -> tuple[int, int]:
        return random.randint(-1, 1), random.randint(-1, 1)
