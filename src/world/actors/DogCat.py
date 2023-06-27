
from .Actor import Actor


class DogCat(Actor):
    def __init__(self, score_diff: int = 1) -> None:
        self.score_diff = score_diff

    def interact_with(self, actor: Actor) -> None:
        pass
