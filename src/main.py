import logging

from environment import Environment, tf
from world.actors.cat import Cat
from world.actors.dog import Dog
from world.actors.controller.keyboard_controller import KeyboardController
from world.actors.controller.random_contoller import RandomController
from world.actors.player import Player
from world.field.field_generator import FieldGenerator
from world.field.views.full_field_view import FullFieldView
from world.game import Game
from world.actors.controller.magent_controller import MAgentController
from world.coordinates import Coordinates

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w')

if __name__ == "__main__":
    fg = FieldGenerator(Coordinates(3, 3))  # (first - x, second -y)
    field = fg.get_field()
    env = Environment(field, None, tf)
    view = FullFieldView(field)
    player, cat, dog = Player(), Cat(), Dog()
    field.place_actor(player, Coordinates(0, 2))
    field.place_actor(cat, Coordinates(0, 0))
    field.place_actor(dog, Coordinates(0, 1))
    controllers = [MAgentController(KeyboardController, field, [player]),
                   MAgentController(RandomController, field, [cat, dog])]
    game = Game(field, controllers, env)
    game.start(2)
