from world.actors.actor import Actor
from world.coordinates import Coordinates
from world.field.field import Field


# topology_function(coordinates: Coordinates, direction: Coordinates) -> tuple[bool, Coordinates]

class Environment:
    def __init__(self, field: Field, connectedness, topology_function=None) -> None:
        self.field = field
        self.areas = {}
        self.connectedness = connectedness
        self.topology_function = topology_function
        self.directions = [Coordinates(0, 1), Coordinates(1, 0), Coordinates(-1, 0), Coordinates(0, -1)]

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
            raise ValueError(f"this actor {actor} marked as {actor.symbol} not at Field")
        if direction not in self.directions:
            return False
        if position.x not in (0, self.field.size.x-1) and position.y not in (0, self.field.size.y-1):
            # what to do if more special cells?
            return self.is_in_area(type(actor), position + direction) \
                and self.field.get_cell_at(position + direction).passable
        topology_valid, cell = self.topology_function(self, position, direction)
        if not topology_valid:
            return False
        return self.is_in_area(type(actor), position + direction) \
            and self.field.get_cell_at(position + direction).passable

    def get_near_cells(self, coordinates: Coordinates) -> list[Coordinates]:
        """return tuple of near cells taking into account topology function and connectedness"""
        near_cells = []
        is_special = False
        if coordinates.x in (0, self.field.size.x-1) and coordinates.y in (0, self.field.size.y-1):
            is_special = True
        for direction in self.directions:
            if is_special:
                topology_valid, cell = self.topology_function(self, coordinates, direction)
                if not topology_valid:
                    continue
            near_cells.append(coordinates + direction)
        return near_cells


def tf(env: Environment, coordinates: Coordinates, direction: Coordinates) -> tuple[bool, Coordinates]:
    if coordinates.x not in (0, env.field.size.x) and coordinates.y not in (0, env.field.size.y):
        return True if direction in env.directions else False, coordinates + direction
    result = True
    if coordinates.x == 0 and direction == Coordinates(-1, 0):
        result = False
    if coordinates.x == env.field.size.x-1 and direction == Coordinates(1, 0):
        result = False
    if coordinates.y == 0 and direction == Coordinates(0, -1):
        result = False
    if coordinates.y == env.field.size.y - 1 and direction == Coordinates(0, 1):
        result = False
    return result, coordinates + direction
