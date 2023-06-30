from world.actors.actor import Actor
from world.field.field import Field
from world.coordinates import Coordinates

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
            if destination_cell.actor is not None:
                try:
                    destination_cell.actor.interact_with(actor)
                    self.field.actors[destination_cell.actor] = None
                    #self.random_respawn_actor(destination_cell.actor)
                    destination_cell.actor = actor

                except ValueError:
                    '''
                    position_cell.actor.interact_with(destination_cell.actor)
                    self.actors[position_cell.actor] = None
                    position_cell.actor = None
                    '''
                    return
                except NotImplementedError:
                    return
                # except ValueError:
                #     return
                # call respawn?

            destination_cell.actor = actor
            position_cell.actor = None
            self.field.actors[actor] = destination
        except IndexError:
            ...

