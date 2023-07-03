from src.environment import tf, Environment, Connectedness
from src.world.actors.cat import Cat
from src.world.actors.controller.random_contoller import RandomController
from src.world.actors.dog import Dog
from src.world.actors.player import Player
from src.world.coordinates import Coordinates
from src.world.game import Game
from src.world.world_configurator import WorldConfigurator

from .configuration_rules import places


def configurate() -> Game:
    wc = WorldConfigurator(Coordinates(5, 5))
    field = wc.get_field()
    env = Environment(field, Connectedness.FOUR_CONNECTEDNESS, tf)
    player1, player2, cat, dog = Player(), Player(), Cat(), Dog()
    wc.apply_rules(
        rules=(places.place_walls, places.place_actors),
        arguments=(
            (Coordinates(2, 2), Coordinates(1, 2), Coordinates(3, 2)),
            (
                (player1, Coordinates(0, 2)),
                (player2, Coordinates(4, 2)),
                (cat, Coordinates(1, 0)),
                (dog, Coordinates(4, 3)),
            )
        )
    )
    game = Game(field, [RandomController(field, [player1, player2, cat, dog])], env)
    return game
