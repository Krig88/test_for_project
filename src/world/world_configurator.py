import logging
from typing import Any

from src.world.coordinates import Coordinates
from src.world.field.cell import Cell
from src.world.field.field import Field


class WorldConfigurator:
    def __init__(self, field_size: Coordinates) -> None:
        logging.debug("field initialized with %s size", field_size)
        self.field_size = field_size
        self.field = Field([[Cell() for _ in range(field_size.y)] for _ in range(field_size.x)])
        self.applied_rules = []

    def apply_rules(self, rules: tuple, arguments: tuple[tuple, ...]) -> None:
        for rule, args in zip(rules, arguments):
            if (rule, args) not in self.applied_rules:
                self.applied_rules.append((rule, args))
            if args is None:
                rule(self.field)
                continue
            rule(self.field, args)

    def reset_field(self, field_size: Coordinates = None) -> None:
        field_size = self.field.size
        self.field = Field([[Cell() for _ in range(field_size.y)] for _ in range(field_size.x)])
        #logging.info("field reset", field_size)
        if field_size is None:
            field_size = self.field_size
        self.field = Field([[Cell() for _ in range(field_size.y)] for _ in range(field_size.x)])

    def get_field(self) -> Field:
        return self.field
