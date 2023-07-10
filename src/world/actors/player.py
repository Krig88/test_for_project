from src.configurations.game_config import GameConfig as Conf
from src.world.actors.actor import Actor


class Player(Actor):
    def __init__(self, distance_of_view: int = 1, score: int = Conf.start_score) -> None:
        super().__init__(distance_of_view)
        self.distance_of_view = distance_of_view
        self.score = score
        self.cats = 0
        self.dogs = 0
        self.reward = 0
