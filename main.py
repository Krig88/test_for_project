from src.configurations.first_configuration import configurate
from src.world.actors.player import Player
from src.configurations.game_config import GameConfig as Conf
from for_logging import log_operations
from for_logging import agents_statistic as a_stat

log_dir = "logs"
log_operations.log_init()


if __name__ == "__main__":
    # print(f"steps:{game.steps}")
    for j in range(Conf.num_of_games + 1):
        log_operations.change_logging_file(f'game{j}.log')
        game = configurate()
        game.start(Conf.iterations)
        log_operations.log_game_statistic(j)
        print(f"game{j} finished")


