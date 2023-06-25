from src.world.field_components.Field import Field
from src.world.actors.Actor import Actor
from src.world.actors.Player import Player

from src.world.field_components.Cell import Cell


class Generator:
    def generate(size: tuple[int, int] = (5,5)) -> tuple(Field, list[Actor]):
        '''
        line = []
        cells = []
        player = Player()
        for i in range(0, size[1]):
            for j in range(0, size[0]):
                line.append(Cell())
            cells.append(line.copy())
            line.clear()
        actors = {player:(0,0)}
        cells[0][0].actor = player
        field = Field(actors, cells)
        return (field, [player]) 
        '''
        raise NotImplementedError()
