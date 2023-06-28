from __future__ import annotations
from abc import ABC, abstractmethod


class Actor(ABC):
    def __init__(self, distance_of_view: int = 1) -> None:
        self.distance_of_view = distance_of_view
    
    def interact_with(self, actor: Actor) -> None:
        raise NotImplementedError()