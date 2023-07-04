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


def configurate() -> Game:
    wc = WorldConfigurator(Coordinates(1, 7))
    field = wc.get_field()
    env = Environment(field, Connectedness.FOUR_CONNECTEDNESS, tf)
    player1, player2, cat, dog = Player(), Player(), Cat(), Dog()
    wc.apply_rules(
        rules=(places.place_walls, places.place_actors),
        arguments=(
            (),
            (
                (player1, Coordinates(0, 1)),
                #(player2, Coordinates(4, 2)),
                (cat, Coordinates(0, 0)),
                #(dog, Coordinates(4, 3)),
            )
        )
    )
    game = Game(field, [KeyboardController(field, [player1]), CatDog(field, [cat], env)], env)
    return game
