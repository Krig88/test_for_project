import logging
import os
from src.configurations.first_configuration import configurate
from src.world.actors.player import Player
from src.configurations.game_config import GameConfig as Conf
import log_operations

log_dir = "logs"
log_operations.log_init()


if __name__ == "__main__":
    # print(f"steps:{game.steps}")
    for j in range(Conf.num_of_games):
        log_operations.change_logging_file(f'game{j}.log')
        log_operations.log_game_statistic(f"Game number {j}")
        game = configurate()
        game.start(Conf.iterations)
        i = 1
        for controller in game.actor_controllers:
            for actor in controller.actors:
                if isinstance(actor, Player):
                    log_operations.log_game_statistic(f"cats:{actor.cats}")
                    log_operations.log_game_statistic(f"dogs:{actor.dogs}")
                    log_operations.log_game_statistic(f"actor{i} score is {actor.score}")
                    i += 1
        log_operations.log_game_statistic(f"steps:{game.steps}")
        log_operations.log_game_statistic("-----------------------------")
        print(f"game{j} finished")


