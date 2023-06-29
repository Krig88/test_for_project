from world.field.field import Field
from world.field.views.abstract_view import AbstractView


class FowFieldOfView(AbstractView):
    def __init__(self, field: Field) -> None:
        super().__init__(field)

    def get_view(self, coordinates: tuple[int, int]) -> str:
        actor = self.field.cells[coordinates[0]][coordinates[1]].actor
        if actor is None:
            raise ValueError(f"No actor at coordinates {coordinates}")
        fow = actor.distance_of_view

        # TODO: Move this to Field till @HERE
        h_min = coordinates[0] - fow
        h_min = h_min if h_min >= 0 else 0
        h_max = coordinates[0] + fow
        h_max = h_max if h_max <= self.field.size[0] * 2 + 1 else self.field.size[0]

        w_min = coordinates[1] - fow
        w_min = w_min if w_min >= 0 else 0
        w_max = coordinates[1] + fow
        w_max = w_max if w_max <= self.field.size[1] * 2 + 1 else self.field.size[1]

        cells = self.field.cells[h_min:h_max+1]

        for i in range(len(cells)):
            cells[i] = cells[i][w_min: w_max + 1]
        # TODO: till HERE

        result = [[" " for _ in range(len(cells[0]))] for _ in range(len(cells))]

        for i in range(len(cells)):
            for j, cell in enumerate(cells[i]):
                if cells[i][j] is None or self.field.dist(coordinates, (h_min + i, w_min + j)) >= fow+1:
                    continue
                result[i][j] = cell.actor.symbol if cell.actor else cell.symbol
        return "\n".join(["".join(result[i]) for i in range(len(result))])
