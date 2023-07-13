import argparse


from for_logging import log_operations
from src.configuration.config_reader import configurate
from src.configuration.game_config import GameConfig as Conf

args_parser = argparse.ArgumentParser(description="Adventures In Cat Dog World")
args_parser.add_argument('-l', '--log_dir', type=str, default="logs",
                         help='provide a name (path) for logs directory')
args_parser.add_argument('-c', '--config_file', type=str, default="configurations/example.json",
                         help='provide a name (path) for config file')

if __name__ == "__main__":
    args = args_parser.parse_args()
    log_operations.log_init(args.log_dir)

    for j in range(Conf.num_of_games):
        field, env, game, wc = configurate(args.config_file)
        log_operations.change_logging_file(f'game{j}.log')
        game.start(Conf.iterations)
        log_operations.log_game_statistic(j)
        # wc.reset_field() так падает, почему?
        print(f"game{j} finished")
