from world.actors.actor import Actor
from world.actors.controller.abstract_controller import AbstractController
from world.field.field import Field
from world.field.views.fow_field_of_view import FowFieldOfView
from world.field.views.full_field_view import FullFieldView
from world.coordinates import Coordinates
from environment import Environment
from world.actors.controller.random_contoller import RandomController
from world.actors.player import Player
import random
from world.actors.cat import Cat
from world.actors.dog import Dog


class CatDog(AbstractController):

    def __init__(self, field: Field, actors: list[Actor], env: Environment):
        super().__init__(field, actors, env)


    def make_decision(self, state: list = None) -> list[tuple[Actor, Coordinates]]:


        decisions = []
        for count, actor in enumerate(self.actors):
            local_decisions = []
            animal = None
            actor_pos = self.field.actors[actor]
            cells_near_actor = self.env.get_near_cells(actor_pos)
            for near_cell in cells_near_actor:
                if near_cell is None:
                    continue
                cell = self.field.get_cell_at(near_cell)
                if not cell.passable or cell.actor is not None:
                    continue
                local_decisions.append(near_cell)

            local_decision = local_decisions[random.randint(0, len(local_decisions) -1)]

            cells_near_decision = self.env.get_near_cells(local_decision)

            for i in cells_near_decision:
                if i is None:
                    continue
                cell = self.field.get_cell_at(i)
                if type(cell.actor) != Player:
                    continue
                if random.randint(0, 0):
                    animal_type = Cat
                else:
                    animal_type = Dog

                animal = animal_type()
                self.actors[count] = animal
                self.field.actors[animal] = self.field.actors[actor]
                self.field.actors.pop(actor)

                if animal is not None:
                    decisions.append((animal, local_decision))
        return decisions



