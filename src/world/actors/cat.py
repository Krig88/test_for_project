from world.actors.actor import Actor
from world.actors.player import Player


class Cat(Actor):
    def __init__(self, distance_of_view: int = 1, symbol: str = "C", score_penalty: int = 1) -> None:
        super().__init__(distance_of_view, symbol)
        self.distance_of_view = distance_of_view
        self.score_penalty = score_penalty

    def interact_with(self, actor: Actor) -> None:
        if not isinstance(actor, Player):
            raise NotImplementedError(f"Cat cannot interact with {actor.__class__}")
        actor.score += self.score_penalty
