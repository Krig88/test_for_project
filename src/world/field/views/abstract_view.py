from abc import ABC, abstractmethod

from src.world.coordinates import Coordinates
from src.world.field.field import Field


class AbstractView(ABC):
    def __init__(self, field: Field) -> None:
        self.field = field

    @abstractmethod
    def get_view(self, coordinates: Coordinates) -> str:
        raise NotImplemented

