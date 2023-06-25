from __future__ import annotations
from abc import ABC, abstractmethod


class Actor(ABC):
    def __init__(self, distance_of_view: int = 1) -> None:
        raise NotImplementedError()
    def interact_with(self, actor: Actor) -> None:
        raise NotImplementedError()