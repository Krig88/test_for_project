from world.field_components.Cell import Cell
from world.field_components.Field import Field
from world.actors.Actor import Actor


# TODO: write viewer with fild of view


class ConsoleFieldView:
    def __init__(
            self,
            symbols: dict[str:str]
    ) -> None:
        self.symbols = symbols

    def draw(self, field: Field, actor: Actor) -> None:
        cell_from = field.actors[actor]
        fow = actor.distance_of_view
        for i, row in enumerate(field.cells):
            row_string = ''
            for j, cell in enumerate(row):
                new_symbol = ''
                if cell.actor:
                    new_symbol = self.symbols[cell.actor.__class__.__name__]
                else:
                    new_symbol = self.symbols[Cell.__name__][0 if cell.passable else 1]
                if abs(i - cell_from[0]) > fow or abs(j - cell_from[1]) > fow \
                        or abs(i - cell_from[0]) + abs(j - cell_from[1]) > fow:
                    continue
                row_string += new_symbol
            if row_string:
                print(row_string.center(fow*2+1, ' '))
