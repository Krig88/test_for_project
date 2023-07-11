import logging
from enum import Enum
import random

import for_logging.agents_statistic as agents_statistic
from src.configurations.game_config import GameConfig as Conf
from src.world.actors.actor import Actor
from src.world.actors.cat import Cat as Cat
from src.world.actors.dog import Dog as Dog
from src.world.actors.player import Player
from src.world.coordinates import Coordinates
from src.world.field.field import Field


class Connectedness(Enum):
    FOUR_CONNECTEDNESS = 0
    EIGHT_CONNECTEDNESS = 1


class Environment:
    def __init__(self, field: Field, connectedness, topology_function=None) -> None:
        self.cat_reward = Conf.cat_reward
        self.dog_reward = Conf.dog_reward
        self.field = field
        self.areas = {}
        self.connectedness = connectedness
        self.topology_function = topology_function
        self.directions = [Coordinates(0, 1), Coordinates(0, -1), Coordinates(1, 0), Coordinates(-1, 0)]
        if self.connectedness == Connectedness.EIGHT_CONNECTEDNESS:
            self.directions += [Coordinates(1, 1), Coordinates(-1, -1), Coordinates(1, -1), Coordinates(-1, 1)]

    def register_area(self, actor_type: type, area: tuple[Coordinates, Coordinates], set_to: bool = True) -> None:
        """edit area for actor_type on field.\n
        if not created, create it and fill as `default`"""
        # TODO: raise errors
        from_coordinates = area[0]
        to_coordinates = area[1]
        if actor_type not in self.areas.keys():
            self.areas[actor_type] = [[not set_to for _ in range(self.field.size.x)] for _ in range(self.field.size.y)]
        for i in range(from_coordinates.y, to_coordinates.y):
            for j in range(from_coordinates.x, to_coordinates.x):
                self.areas[actor_type][i][j] = set_to

    def set_area(self, actor_type: type, area: list[list[bool]]):
        # TODO: raise errors
        self.areas[actor_type] = area

    def is_in_area(self, actor_type: type, coordinates: Coordinates) -> bool:
        """check is in area for given coordinates"""
        if actor_type not in self.areas.keys():
            return True
        return self.areas[actor_type][coordinates.y][coordinates.x]

    def is_move_valid(self, actor: Actor, position: Coordinates, direction: Coordinates) -> bool:
        """check is move valid taking into account topology function and registered area"""
        if actor not in self.field.actors or self.field.actors[actor] is None:
            raise ValueError(f"this actor {actor} marked as {actor} not at Field")
        if direction not in self.directions:
            return False
        if position.x not in (0, self.field.size.x - 1) and position.y not in (0, self.field.size.y - 1):
            # what to do if more special cells?
            return self.is_in_area(type(actor), position + direction) \
                and self.field.get_cell_at(position + direction).passable
        topology_valid, cell = self.topology_function(self, position, direction)
        if not topology_valid:
            return False
        return self.is_in_area(type(actor), position + direction) \
            and self.field.get_cell_at(position + direction).passable

    def get_near_cells(self, coordinates: Coordinates) -> list[Coordinates | None]:
        """return tuple of near cells taking into account topology function and connectedness"""
        near_cells = [None for _ in range(len(self.directions))]
        is_special = False
        if coordinates.x in (0, self.field.size.x - 1) or coordinates.y in (0, self.field.size.y - 1):
            is_special = True
        for i in range(0, len(self.directions)):
            direction = self.directions[i]
            if is_special:
                topology_valid, cell = self.topology_function(self, coordinates, direction)
                if not topology_valid:
                    continue
            near_cells[i] = coordinates + direction
        return near_cells

    def actors_interact(self, interacting_actor: Actor, actor: Actor | None):
        logging.info("interacting %s to %s", interacting_actor, actor)
        if not isinstance(actor, Player):
            raise ValueError
        # TODO: add hooks to change interaction to environment
        if isinstance(interacting_actor, Cat):
            actor.reward = self.cat_reward
            agents_statistic.get_statistic(actor).cats += 1
            return
        if isinstance(interacting_actor, Dog):
            actor.reward = self.dog_reward
            agents_statistic.get_statistic(actor).dogs += 1
            return

    def interact_with_player(self, interacting_actor: Actor, player: Player) -> Actor|None:
        match interacting_actor:
            case Cat():
                player.reward = self.cat_reward
                agents_statistic.get_statistic(player).cats += 1

                return interacting_actor
            case Dog():
                player.reward = self.dog_reward
                agents_statistic.get_statistic(player).dogs += 1
                return interacting_actor
            case _:
                return None

    def random_respawn(self, actor: Actor) -> None:
        clear_cells = []
        for i in range(0, self.field.size.y):
            for j in range(0, self.field.size.x):
                if self.field.is_clear(Coordinates(j, i)) and self.is_in_area(type(actor), Coordinates(j, i)):
                    clear_cells.append(Coordinates(j, i))
        cell_cords = clear_cells[random.randint(0, len(clear_cells) - 1)]
        self.field.place_actor(actor, cell_cords)
        logging.info("actor %s respawned at %s", actor, cell_cords)

    def move_actor(self, actor: Actor, direction: Coordinates) -> None:
        position = self.field.actors[actor]
        position_cell = self.field.get_cell_at(position)
        if not self.is_move_valid(actor, position, direction):
            logging.debug("move from %s with direction %s is not valid", position, direction)
            if isinstance(actor, Player):
                actor.reward += Conf.skip_reward
                agents_statistic.agents_statistic_folder[actor].skips += 1
            return
        _, destination = self.topology_function(self, position, direction)
        destination_cell = self.field.get_cell_at(destination)
        eaten_actor = None

        # TODO remove this try(make it by case)

        if destination_cell.actor is not None:
            match  actor:
                case Player():
                    eaten_actor = self.interact_with_player(destination_cell.actor, actor)
                case _:
                    return

        self.field.move_actor(position, destination)

        if eaten_actor is not None:
            self.field.actors.pop(eaten_actor)
            self.random_respawn(eaten_actor)


def tf(env: Environment, coordinates: Coordinates, direction: Coordinates) -> tuple[bool, Coordinates]:
    if coordinates.x not in (0, env.field.size.x - 1) and coordinates.y not in (0, env.field.size.y - 1):
        return True if direction in env.directions else False, coordinates + direction
    result = True
    if coordinates.x == 0 and direction == Coordinates(-1, 0):
        result = False
    if coordinates.x == env.field.size.x - 1 and direction == Coordinates(1, 0):
        result = False
    if coordinates.y == 0 and direction == Coordinates(0, -1):
        result = False
    if coordinates.y == env.field.size.y - 1 and direction == Coordinates(0, 1):
        result = False
    return result, coordinates + direction


