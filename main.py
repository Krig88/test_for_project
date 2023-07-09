from src.configurations.first_configuration import configurate
from src.world.actors.player import Player
from src.configurations.game_config import GameConfig as Conf
from for_logging import log_operations
from for_logging import  agents_statistic as AS

log_dir = "logs"
log_operations.log_init()


if __name__ == "__main__":
    # print(f"steps:{game.steps}")
    for j in range(Conf.num_of_games + 1):
        log_operations.change_logging_file(f'game{j}.log')
        log_operations.log_game_statistic(f"Game number {j}")
        game = configurate()

        for controller in game.actor_controllers:
            for actor in controller.actors:
                if isinstance(actor, Player):
                    AS.add_agent_to_folder(actor)

        game.start(Conf.iterations)
        i = 1
        for controller in game.actor_controllers:
            for actor in controller.actors:
                if isinstance(actor, Player):
                    log_operations.log_game_statistic(f"cats:{AS.get_statistic(actor).cats}")
                    log_operations.log_game_statistic(f"dogs:{AS.get_statistic(actor).dogs}")
                    log_operations.log_game_statistic(f"actor{i} score is {actor.score}")
                    i += 1
        log_operations.log_game_statistic(f"steps:{game.steps}")
        log_operations.log_game_statistic("-----------------------------")
        print(f"game{j} finished")


