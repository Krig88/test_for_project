from __future__ import annotations
from abc import ABC, abstractmethod


class Actor(ABC):
    def __init__(self, distance_of_view: int = 1) -> None:
        if distance_of_view <= 0:
            raise ValueError("distance_of_view must be >= 0")
        self.distance_of_view = distance_of_view


    @abstractmethod
    def interact_with(self, actor: Actor) -> None:
        raise NotImplemented
