
class Coordinates:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x, self.y = x, y

    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinates(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def __hash__(self):
        return self.x + self.y

    def __str__(self):
        return f"x = {self.x} y = {self.y}\t"
