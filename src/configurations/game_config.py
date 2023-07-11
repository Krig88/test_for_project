from dataclasses import dataclass


@dataclass(frozen=True)
class GameConfig:
    # Game settings
    num_of_games: int = 1  # number of games to be played
    iterations: int = 100000  # count of steps in game
    mortality: bool = False  # Agents death possibility

    # Rewards settings
    cat_reward: int = 3
    dog_reward: int = -3
    iteration_reward: int = 0
    skip_reward: int = -10

    # Agent settings
    start_score: int = 0
    steps_to_update_model: int = 1
    learning_rate: float = 0.005
