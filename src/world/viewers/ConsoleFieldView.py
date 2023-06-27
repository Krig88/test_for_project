from world.field_components.Field import Field
from world.actors.Actor import Actor

#TODO: write viwer with fild of view 


class ConsoleFieldView:
    def __init__(
            self,
            field: Field,
            actors_views: dict[str:str] = {}
    ) -> None:
        raise NotImplementedError()

    def get_area(self, actor: Actor) -> list[list[str]]:
        raise NotImplementedError()
