from world.actors.cat import Cat
from world.actors.dog import Dog
from world.actors.controller.keyboard_controller import KeyboardController
from world.actors.controller.random_contoller import RandomController
from world.actors.player import Player
from world.field.cell import Cell
from world.field.field_generator import FieldGenerator
from world.field.views.full_field_view import FullFieldView
from world.game import Game

if __name__ == "__main__":
    print("Demo")
    for _ in range(1):
        fg = FieldGenerator((3, 3))
        field = fg.get_field()
        view = FullFieldView(field)
        player, cat, dog = Player(), Cat(), Dog()
        field.place_actor(player, (1, 1))
        field.place_actor(cat, (0, 0))
        field.place_actor(dog, (2, 2))
        field.cells[1][0] = Cell(False, "#")
        field.cells[1][2] = Cell(False, "#")
        controllers = [KeyboardController(field, player), RandomController(field, cat), RandomController(field, dog)]
        game = Game(field, controllers)
        game.start(10)
