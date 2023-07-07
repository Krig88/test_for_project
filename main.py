import logging

from src.configurations.first_configuration import configurate
from src.world.actors.player import Player

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w')

if __name__ == "__main__":
    print(f"steps:{game.steps}")
    for j in range(100):
        game = configurate()
        game.start(5000)
        i = 1
        for controller in game.actor_controllers:
            for actor in controller.actors:
                if isinstance(actor, Player):
                    print(f"cats:{actor.cats}")
                    print(f"dogs:{actor.dogs}")
                    print(f"actor{i} score is {actor.score}")
                    i += 1
        print(f"steps:{game.steps}")



