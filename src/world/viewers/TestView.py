from world.field_components.Field import Field
from world.field_components.Cell import Cell


# TODO: write viewer with whole fild

class TestView:
    def __init__(self, symbols):
        self.symbols = symbols

    def draw(self, field: Field) -> None:
        for row in field.cells:
            row_string = ''
            for cell in row:
                new_symbol = ''
                if cell.actor:
                    new_symbol = self.symbols[cell.actor.__class__.__name__]
                else:
                    new_symbol = self.symbols[Cell.__name__][0 if cell.passable else 1]
                row_string += new_symbol
            print(row_string)
