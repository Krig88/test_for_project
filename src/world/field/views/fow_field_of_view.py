from src.world.coordinates import Coordinates
from src.world.field.field import Field
from src.world.field.views.abstract_view import AbstractView


class FowFieldOfView(AbstractView):
    def __init__(self, field: Field) -> None:
        super().__init__(field)

    def get_view(self, coordinates: Coordinates) -> str:
        actor = self.field.cells[coordinates.x][coordinates.y].actor
        if actor is None:
            raise ValueError(f"No actor at coordinates {coordinates.x, coordinates.y}")
        fow = actor.distance_of_view

        h_min = coordinates.x - fow
        h_min = h_min if h_min >= 0 else 0
        h_max = coordinates.x + fow
        h_max = h_max if h_max <= self.field.size.x * 2 + 1 else self.field.size.x

        w_min = coordinates.y - fow
        w_min = w_min if w_min >= 0 else 0
        w_max = coordinates.y + fow
        w_max = w_max if w_max <= self.field.size.y * 2 + 1 else self.field.size.y

        cells = self.field.cells[h_min:h_max+1]

        for i in range(len(cells)):
            cells[i] = cells[i][w_min: w_max + 1]

        result = [[" " for _ in range(len(cells[0]))] for _ in range(len(cells))]

        for i in range(len(cells)):
            for j, cell in enumerate(cells[i]):
                if cells[i][j] is None or self.field.dist(coordinates, Coordinates(h_min + i, w_min + j)) >= fow+1:
                    continue
                result[i][j] = cell.actor.symbol if cell.actor else cell.symbol
        return "\n".join(["".join(result[i]) for i in range(len(result))])
