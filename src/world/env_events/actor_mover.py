import random

from world.actors.actor import Actor
from world.actors.player import Player
from world.field.field import Field
from world.coordinates import Coordinates
from world.field.cell import Cell


class ActorMover:

    def __init__(self, field: Field, ) -> None:
        self.field = field

    def move_actor(self, actor: Actor, direction: Coordinates) -> None:
        if actor not in self.field.actors:
            raise ValueError(f"this actor {actor} marked as {actor.symbol} not at Field")
        if self.field.actors[actor] is None:
            return
        position = self.field.actors[actor]
        position_cell = self.field.get_cell_at(position)
        try:
            destination = position + direction
            destination_cell = self.field.get_cell_at(destination)
            if not destination_cell.passable:
                return
            eaten_actor = None
            if destination_cell.actor is not None:
                destination_cell.actor.interact_with(position_cell.actor)
                self.field.actors[destination_cell.actor] = None
                eaten_actor = destination_cell.actor
            destination_cell.actor = actor
            position_cell.actor = None
            self.field.actors[actor] = destination
            self.random_respawn(eaten_actor)
        except IndexError:
            return
        except ValueError:
            return
        except NotImplementedError:
            return

    def random_respawn(self, actor: Actor) -> None:
        if not actor:
            return
        clear_cells = []
        for i in range(0, self.field.size.y):
            for j in range(0, self.field.size.x):
                if self.field.is_clear(Coordinates(j, i)):
                    clear_cells.append(Coordinates(j, i))

        cell_cords = clear_cells[random.randint(0, len(clear_cells) - 1)]
        self.field.place_actor(actor, cell_cords)
