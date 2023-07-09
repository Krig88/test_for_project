import logging
import os
from src.configurations.first_configuration import configurate
from src.world.actors.player import Player
from src.configurations.game_config import GameConfig as Conf
import log_operations

log_dir = "logs"
log_operations.log_init(log_dir)


if __name__ == "__main__":
    # print(f"steps:{game.steps}")
    for j in range(Conf.num_of_games):
        handler = logging.FileHandler(log_dir + f'/game{j}.log')
        logging.getLogger().addHandler(handler)
        game = configurate()
        game.start(Conf.iterations)
        i = 1
        for controller in game.actor_controllers:
            for actor in controller.actors:
                if isinstance(actor, Player):
                    logging.info(f"cats:{actor.cats}")
                    logging.info(f"dogs:{actor.dogs}")
                    logging.info(f"actor{i} score is {actor.score}")
                    i += 1
        logging.info(f"steps:{game.steps}")
        handler.close()
        logging.getLogger().removeHandler(handler)
        print(f"game{j} finished")


