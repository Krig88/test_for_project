from dataclasses import dataclass


@dataclass(frozen=True)
class GameConfig:
    # Game settings
    num_of_games: int = 10  # number of games to be played
    iterations: int = 50  # count of steps in game

    # gent settings
