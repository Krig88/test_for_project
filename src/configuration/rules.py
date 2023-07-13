from src.world.actors.actor import Actor
from src.world.coordinates import Coordinates
from src.world.field.field import Field


def place_walls(field: Field, coordinates: tuple[Coordinates]):
    for coordinate in coordinates:
        field.place_wall(coordinate)


def place_actors(field: Field, coordinates: tuple[tuple[Actor, Coordinates]]):
    for actor, coordinate in coordinates:
        field.place_actor(actor, coordinate)
