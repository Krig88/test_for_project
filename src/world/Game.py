from __future__ import annotations

from world.Generator import Generator
from world.controllers.PlayerController import PlayerController
from world.viewers.ConsoleFieldView import ConsoleFieldView
from world.viewers.TestView import TestView


class Game:
    def __init__(self, iterations: int) -> None:
        generator = Generator()
        generator.generate()
        self.field = generator.field
        self.actors = generator.actors
        self.iterations = iterations

    def start(self, symbols):
        viewer = ConsoleFieldView(symbols)
        p_controller = PlayerController(self.field, self.actors[0])
        for i in range(self.iterations):
            # viewer.draw(self.field)
            viewer.draw(self.field, self.actors[0])
            p_controller.make_move()
