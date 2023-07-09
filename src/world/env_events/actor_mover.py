import logging
import random

from src.environment import Environment
from src.world.actors.actor import Actor
from src.world.coordinates import Coordinates
from src.world.field.field import Field


class ActorMover:
    def __init__(self, field: Field, env: Environment) -> None:
        self.field = field
        self.env = env

    def move_actor(self, actor: Actor, direction: Coordinates) -> None:
        position = self.field.actors[actor]
        position_cell = self.field.get_cell_at(position)
        if not self.env.is_move_valid(actor, position, direction):
            logging.debug("move from %s with direction %s is not valid", position, direction)
            return
        _, destination = self.env.topology_function(self.env, position, direction)
        destination_cell = self.field.get_cell_at(destination)
        eaten_actor = None
        if destination_cell.actor is not None:
            try:
                self.env.actors_interact(destination_cell.actor, position_cell.actor)
                #self.env.actors_interact(Dog(), Cat())
                self.field.actors[destination_cell.actor] = None
                eaten_actor = destination_cell.actor
                logging.info("actor %s interacted with %s", actor, destination_cell.actor)
            except ValueError as ve:
                return
            except AttributeError as ate:
                logging.debug("none interacting")
                return
        destination_cell.actor = actor
        position_cell.actor = None
        self.field.actors[actor] = destination
        logging.info("actor %s moved from %s to %s", actor, position, destination)
        self.random_respawn(eaten_actor)

    def random_respawn(self, actor: Actor) -> None:
        if not actor:
            return
        clear_cells = []
        for i in range(0, self.field.size.y):
            for j in range(0, self.field.size.x):
                if self.field.is_clear(Coordinates(j, i)) and self.env.is_in_area(type(actor), Coordinates(j, i)):
                    clear_cells.append(Coordinates(j, i))
        cell_cords = clear_cells[random.randint(0, len(clear_cells) - 1)]
        self.field.place_actor(actor, cell_cords)
        logging.info("actor %s respawned at %s", actor, cell_cords)
