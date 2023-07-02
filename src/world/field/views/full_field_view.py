from world.field.field import Field
from world.field.views.abstract_view import AbstractView
from world.coordinates import Coordinates


class FullFieldView(AbstractView):
    def __init__(self, field: Field) -> None:
        super().__init__(field)

    def get_view(self, coordinates: Coordinates = None) -> str:
        result = [[self.get_cell_char(Coordinates(i, j)) for j in range(self.field.size.y)] for i in range(self.field.size.x)]
        return "\n".join(["".join(result[i]) for i in range(self.field.size.x)])
