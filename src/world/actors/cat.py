from src.world.actors.actor import Actor


class Cat(Actor):
    def __init__(self, distance_of_view: int = 1, score_penalty: int = 1) -> None:
        super().__init__(distance_of_view)
        self.distance_of_view = distance_of_view
        self.score_penalty = score_penalty


