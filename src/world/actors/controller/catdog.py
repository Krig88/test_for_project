import random

from src.environment import Environment
from src.world.actors.actor import Actor
from src.world.actors.cat import Cat
from src.world.actors.controller.abstract_controller import AbstractController
from src.world.actors.dog import Dog
from src.world.actors.player import Player
from src.world.coordinates import Coordinates
from src.world.field.field import Field
import random


class CatDog(AbstractController):

    def __init__(self, field: Field, actors: list[Actor], env: Environment):
        super().__init__(field, actors, env)
        self.last_turn_actors = {i: True for i in actors}

    def make_decision(self, state: list = None) -> list[tuple[Actor, Coordinates]]:
        decisions = []
        for actor_counter, actor in enumerate(self.actors):
            actor_pos = self.field.actors[actor]
            near_cells = self.env.get_near_cells(actor_pos)
            near_players = self.is_player_near(near_cells)
            if near_players:
                print("player is near")
                if self.last_turn_actors[actor]:
                    decisions.append((actor, Coordinates(0, 0)))
                    continue
                new_actor = self.change_me(actor, actor_counter, actor_pos)
                decisions.append((new_actor, Coordinates(0, 0)))
                continue
            print("player not near")
            decision = self.choose_direction(near_cells)
            if self.is_player_near(self.env.get_near_cells(decision)) and not self.last_turn_actors[actor]:
                actor = self.change_me(actor, actor_counter, actor_pos)
            decisions.append((actor, decision - actor_pos))
            print("decisions:", decisions)
            self.last_turn_actors[actor] = False
        return decisions

    def is_player_near(self, near_cells: list[Coordinates]) -> bool:
        players_near = []
        for i in near_cells:
            if i is None:
                continue
            cell = self.field.get_cell_at(i)
            if type(cell.actor) == Player:
                return True
        return False

    def choose_direction(self, near_cells) -> Coordinates:
        directions = []
        for i in near_cells:
            if i is None:
                continue
            cell = self.field.get_cell_at(i)
            if not cell.passable:
                continue
            if cell.actor is not None:
                continue
            print(i)
            directions.append(i)
        print("Catdog direction:", directions)
        return directions[random.randint(0, len(directions) - 1)]

    def change_me(self, actor: Actor, actors_pos_in_list: int, actor_pos: Coordinates) -> Actor:
        # TODO: implement zone check
        # def dont change actor in the cell on board
        new_actor = Cat() if random.randint(0, 0) else Dog()
        self.field.actors.pop(actor)
        self.field.actors[new_actor] = actor_pos
        self.field.get_cell_at(actor_pos).actor = new_actor
        self.actors[actors_pos_in_list] = new_actor
        self.last_turn_actors.pop(actor)
        self.last_turn_actors[new_actor] = True
        return new_actor
