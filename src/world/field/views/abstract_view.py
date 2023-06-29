from abc import ABC, abstractmethod

from world.field.field import Field


class AbstractView(ABC):
    def __init__(self, field: Field) -> None:
        self.field = field

    @abstractmethod
    def get_view(self, coordinates: tuple[int, int]) -> str:
        raise NotImplemented

    def get_cell_char(self, coordinates: tuple[int, int]):
        try:
            cell = self.field.cells[coordinates[0]][coordinates[1]]
            if cell.actor is None:
                return cell.symbol
            return cell.actor.symbol
        except IndexError:
            return " "
