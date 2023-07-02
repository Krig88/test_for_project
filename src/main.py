from environment import Environment, tf
from world.actors.cat import Cat
from world.actors.dog import Dog
from world.actors.controller.keyboard_controller import KeyboardController
from world.actors.controller.random_contoller import RandomController
from world.actors.player import Player
from world.field.cell import Cell
from world.field.field_generator import FieldGenerator
from world.field.views.full_field_view import FullFieldView
from world.game import Game
from world.actors.controller.magent_controller import MAgentController
from world.coordinates import Coordinates

if __name__ == "__main__":
    m = {Coordinates(0, 0): 1}
    print(m[Coordinates(0, 0)])
    print("Demo")
    fg = FieldGenerator(Coordinates(10, 10))  # (first - x, second -y)
    field = fg.get_field()

    env = Environment(field, None, tf)

    view = FullFieldView(field)
    player, player1, cat, dog = Player(), Player(), Cat(), Dog()  # , player2 Player(),
    field.place_actor(player, Coordinates(5, 5))
    field.place_actor(player1, Coordinates(0, 3))
    field.place_actor(cat, Coordinates(1, 0))
    field.place_actor(dog, Coordinates(0, 1))
    # field.place_actor(dog, Coordinates(3, 0))
    # field.place_wall(Coordinates(4, 0))
    # field.cells[1][0] = Cell(False, "#")
    # field.cells[1][2] = Cell(False, "#")
    controller = KeyboardController(field, [player, player1])

    game = Game(field, [controller], env)
    game.start(10000)

    # for _ in range(1):
    #     fg = FieldGenerator(Coordinates(10, 10)) #(first - x, second -y)
    #     field = fg.get_field()
    #     view = FullFieldView(field)
    #     player, player2, cat, dog = Player(), Player(), Cat(), Dog()
    #     field.place_actor(player, Coordinates(0, 0))
    #     field.place_actor(player2, Coordinates(0, 1))
    #     field.place_actor(cat, Coordinates(1, 0))
    #     field.place_actor(dog, Coordinates(5, 0))
    #     #field.place_actor(dog, Coordinates(3, 0))
    #     #field.place_wall(Coordinates(4, 0))
    #     #field.cells[1][0] = Cell(False, "#")
    #     #field.cells[1][2] = Cell(False, "#")
    #     p_controllers = MAgentController(KeyboardController, field, [player, player2])
    #     a_controllers = MAgentController(RandomController, field, [cat, dog])
    #     game = Game(field, [p_controllers, a_controllers])
    #     game.start(10)
