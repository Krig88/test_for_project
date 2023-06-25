from ActorController import ActorController
from src.world.field_components.Field import Field
from src.world.actors import Actor


class NpcController(ActorController):
    def __init__(self, field: Field, actor: Actor) -> None:
        super().__init__(field, actor)
        raise NotImplementedError()
        