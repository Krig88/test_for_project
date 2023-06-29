from world.field.field import Field
from world.field.views.abstract_view import AbstractView


class FullFieldView(AbstractView):
    def __init__(self, field: Field) -> None:
        super().__init__(field)

    def get_view(self, coordinates: tuple[int, int]) -> str:
        result = [[self.get_cell_char((i, j)) for j in range(self.field.size[1])] for i in range(self.field.size[0])]
        return "\n".join(["".join(result[i]) for i in range(self.field.size[0])])
