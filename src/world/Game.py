from __future__ import annotations
from world.field_components.Field import Field
from world.actors.Actor import Actor
from world.Generator import Generator
from world.viewers.TestView import TestView 
from world.controllers.PlayerController import PlayerController

class Game:
    def __init__(self) -> None:
        generator = Generator()
        generator.generate()
        self.field = generator.field
        self.actors = generator.actors

#TODO: write game loop

        
    def start(self):
        viewer = TestView()
        p_controller = PlayerController(self.field, self.actors[0])
        while True:
            viewer.draw(self.field)
            p_controller.make_move()
            
            
        
