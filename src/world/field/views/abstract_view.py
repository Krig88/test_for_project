from abc import ABC, abstractmethod
from world.coordinates import Coordinates
from world.field.field import Field


class AbstractView(ABC):
    def __init__(self, field: Field) -> None:
        self.field = field

    @abstractmethod
    def get_view(self, coordinates: Coordinates) -> str:
        raise NotImplemented

    def get_cell_char(self, coordinates: Coordinates):
        try:
            cell = self.field.cells[coordinates.x][coordinates.y]
            if cell.actor is None:
                return cell.symbol
            return cell.actor.symbol
        except IndexError:
            return " "
