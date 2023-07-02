from world.field.cell import Cell
from world.field.field import Field
from world.coordinates import Coordinates


class FieldGenerator:
    def __init__(self, field_size: Coordinates) -> None:
        self.field_size = field_size
        self.field = Field([[Cell() for _ in range(field_size.y)] for _ in range(field_size.x)])

    def apply_rules(self, rules: tuple, arguments: tuple[tuple | None]) -> None:
        for rule, args in zip(rules, arguments):
            if args is None:
                rule(self.field)
                continue
            rule(self.field, *args)

    def reset_field(self, field_size: Coordinates = None) -> None:
        if field_size is None:
            field_size = self.field_size
        self.field = Field([[Cell() for _ in range(field_size.x)] for _ in range(field_size.y)])

    def get_field(self) -> Field:
        return self.field
