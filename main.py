import argparse

from for_logging import log_operations
from src.configurations.first_configuration import configurate
from src.configurations.game_config import GameConfig as Conf

args_parser = argparse.ArgumentParser(description="Adventures In Cat Dog World")
args_parser.add_argument('-l', '--log_dir', type=str, default="logs",
                         help='provide a name for logs directory')  # path?
args_parser.add_argument('-c', '--config_file', type=str, default="config",
                         help='provide a name for config file')  # needs config reader? && path?

if __name__ == "__main__":
    args = args_parser.parse_args()
    log_operations.log_init(args.log_dir)

    for j in range(Conf.num_of_games + 1):
        log_operations.change_logging_file(f'game{j}.log')
        game = configurate()
        game.start(Conf.iterations)
        log_operations.log_game_statistic(j)
        print(f"game{j} finished")
