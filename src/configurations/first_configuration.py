from src.environment import tf, Environment, Connectedness
from src.world.actors.cat import Cat
from src.world.actors.controller.random_contoller import RandomController
from src.world.actors.controller.keyboard_controller import KeyboardController
from src.world.actors.dog import Dog
from src.world.actors.player import Player
from src.world.coordinates import Coordinates
from src.world.game import Game
from src.world.world_configurator import WorldConfigurator
from src.world.actors.controller.catdog import CatDog
from .configuration_rules import places
from src.world.actors.controller.agent_controller import AgentController

wc = None


def configurate() -> Game:
    global wc
    wc = WorldConfigurator(Coordinates(4, 4))
    field = wc.get_field()
    env = Environment(field, Connectedness.FOUR_CONNECTEDNESS, tf)
    player1, cat1, dog, cat2, dog2 = Player(), Cat(), Dog(), Cat(), Dog()
    wc.apply_rules(
        rules=(places.place_walls, places.place_actors),
        arguments=(
            (),
            (
                (player1, Coordinates(1, 1)),
                # (player2, Coordinates(4, 2)),
                (cat1, Coordinates(0, 0)),
                # (dog, Coordinates(0, 1)),
                (dog2, Coordinates(0, 1)),
                (cat2, Coordinates(0, 2)),
            )
        )
    )
    # AgentController(field, [player1], env)
    game = Game(field, [AgentController(field, [player1], env), RandomController(field, [cat1, cat2, dog2])], env)
    return game
