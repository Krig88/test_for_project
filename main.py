import logging

from src.configurations.first_configuration import configurate
from src.world.actors.player import Player

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w')

if __name__ == "__main__":
    game = configurate()
    game.start(1000)
    i = 1
    for controller in game.actor_controllers:
        for actor in controller.actors:
            if isinstance(actor, Player):
                print(f"actor{i} score is {actor.score}")
                i += 1
