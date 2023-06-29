
class Coordinates:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x, self.y = x, y

    def __eq__(self, other) -> bool:
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):
        return (self.x != other.x) and (self.y != other.y)

    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinates(self.x - other.x, self.y - other.y)
