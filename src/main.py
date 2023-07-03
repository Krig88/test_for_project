import logging

from environment import Environment, tf
from world.actors.cat import Cat
from world.actors.controller.random_contoller import RandomController
from world.actors.dog import Dog
from world.actors.player import Player
from world.coordinates import Coordinates
from world.field.field_generator import FieldGenerator
from world.field.views.full_field_view import FullFieldView
from world.game import Game

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w')
    fg = FieldGenerator(Coordinates(1, 3))  # (first - x, second -y)
    field = fg.get_field()

    env = Environment(field, None, tf)

    view = FullFieldView(field)
    player, player1, cat, dog = Player(), Player(), Cat(), Dog()  # , player2 Player(),
    field.place_actor(player, Coordinates(0, 0))
    field.place_actor(player1, Coordinates(0, 1))
    field.place_actor(cat, Coordinates(0, 2))

    game = Game(field, [RandomController(field, [player, player1, cat])], env)

    game.start(10000)
