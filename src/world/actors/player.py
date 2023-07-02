import logging

from world.actors.actor import Actor


class Player(Actor):
    def __init__(self, distance_of_view: int = 1, score: int = 0) -> None:
        super().__init__(distance_of_view)
        self.distance_of_view = distance_of_view
        self.score = score

    def interact_with(self, actor: Actor) -> None:
        logging.debug("Player cannot interact with %s", actor.__class__)
        raise ValueError(f"Player can't interact with {actor.__class__}")
