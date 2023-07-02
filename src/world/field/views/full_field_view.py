from world.field.field import Field
from world.field.views.abstract_view import AbstractView
from world.coordinates import Coordinates
from world.actors.player import Player
from world.actors.dog import Dog
from world.actors.cat import Cat


class FullFieldView(AbstractView):

    def __init__(self, field: Field) -> None:
        super().__init__(field)
        self.view = {Cat: 'C', Dog: 'D', Player: 'P'}

    def get_view(self, coordinates: Coordinates = None) -> str:
        result = ''
        #result = [[self.get_cell_char(Coordinates(i, j)) for j in range(self.field.size.y)] for i in range(self.field.size.x)]
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


