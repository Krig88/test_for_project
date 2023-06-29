from world.actors.actor import Actor
from world.field.cell import Cell


class Field:
    # TODO: rewrite with overflow_function
    def __init__(self, cells: list[list[Cell]], is8: bool = False, overflow_function=None):
        self.cells = cells
        self.size = len(cells), len(cells[0])
        self._is8 = is8
        self.actors = dict()
        self.overflow_function = overflow_function

    def dist(self, src: tuple[int, int], to: tuple[int, int]) -> int:
        if self._is8:
            return NotImplemented
        return abs(src[0] - to[0]) + abs(src[1] - to[1])

    def place_actor(self, actor: Actor, coordinates: tuple[int, int]) -> None:
        if actor in self.actors:
            raise ValueError(f"actor already on board")
        cell = self.cells[coordinates[0]][coordinates[1]]
        if cell.actor is not None:
            raise ValueError(f"cell at {coordinates} has actor!")
        cell.actor = actor
        self.actors[actor] = coordinates

    def move_actor(self, actor: Actor, direction: tuple[int, int]) -> None:
        if actor not in self.actors:
            raise ValueError(f"this actor {actor} marked as {actor.symbol} not at Field")
        if self.actors[actor] is None:
            return
        position = self.actors[actor]
        position_cell = self.get_cell_at(position)
        try:
            destination = (position[0] + direction[0], position[1] + direction[1])
            destination_cell = self.get_cell_at(destination)
            if destination_cell.actor is not None:
                try:
                    destination_cell.actor.interact_with(actor)
                    self.actors[destination_cell.actor] = None
                    destination_cell.actor = actor
                except ValueError:
                    position_cell.actor.interact_with(destination_cell.actor)
                    self.actors[position_cell.actor] = None
                    position_cell.actor = None
                    return
                except NotImplementedError:
                    return
                # except ValueError:
                #     return
                # call respawn?
            destination_cell.actor = actor
            position_cell.actor = None
            self.actors[actor] = destination
        except IndexError:
            ...
            # print(f"IndexError({actor.symbol}) at {self.actors[actor]} {direction}")

    def get_cell_at(self, coordinates: tuple[int, int]) -> Cell:
        if 0 <= coordinates[0] < self.size[0] and 0 <= coordinates[1] < self.size[1]:
            return self.cells[coordinates[0]][coordinates[1]]
        # TODO: rewrite with overflow_function
        raise IndexError
