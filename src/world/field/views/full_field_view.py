from src.world.actors.cat import Cat
from src.world.actors.dog import Dog
from src.world.actors.player import Player
from src.world.coordinates import Coordinates
from src.world.field.field import Field
from src.world.field.views.abstract_view import AbstractView


class FullFieldView(AbstractView):

    def __init__(self, field: Field) -> None:
        super().__init__(field)
        self.view = {Cat: 'C', Dog: 'D', Player: 'P'}

    def get_view(self, coordinates: Coordinates = None) -> str:
        result = ''
        for i in range(self.field.size.x):
            for j in range(self.field.size.y):
                cell = self.field.get_cell_at(Coordinates(i, j))
                if not cell.passable:
                    result += '#'
                    continue
                if cell.actor is None:
                    result += '.'
                    continue
                result += self.view[type(cell.actor)]
            result += '\n'

        return result


