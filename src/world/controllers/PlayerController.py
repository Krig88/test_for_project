from .ActorController import ActorController
from world.field_components.Field import Field
from world.actors.Actor import Actor


class PlayerController(ActorController):
    def __init__(self, field: Field, actor: Actor) -> None:
        super().__init__(field, actor)

    def choose_direction(self) -> tuple[int, int]:
        while True:
            direction = tuple(map(int, input().split()))
            if len(direction) == 2 and direction[0] in range(-1,2) and direction[1] in range(-1,2):
                return direction[0], direction[1]
