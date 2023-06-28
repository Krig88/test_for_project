from world.field_components.Cell import Cell
from world.actors.Player import Player
from world.field_components.Field import Field
from world.actors.Dog import Dog
from world.actors.Cat import Cat



class Generator:

    def __init__(self, size: tuple[int, int] = (5, 5)) -> None:
        self.field = Field([[Cell() for _ in range(size[0])] for _ in range(size[1])], size)
        self.actors = []

    def generate(self, set_player: int = 0, set_npc: int = 0, set_walls: int = 0) -> None:
        self.field.cells[1][1].passable = False
        self.field.cells[3][4].passable = False
        self.field.cells[4][2].passable = False
        self.place_player()

        dog = Dog()
        cat = Cat()
        self.field.set_actor(cat, (2,2))
        self.actors.append(cat)
        self.field.set_actor(dog, (2, 3))
        self.actors.append(dog)

        #TODO create current controllers. replace the actors by there controllers


    def place_walls(self, count_of_walls: int = 3):
        raise NotADirectoryError

    def place_player(self, player_pos: tuple[int, int] = (0, 0)) -> None:
        player = Player()
        self.actors.append(player)
        self.field.set_actor(player, player_pos)
        # self.actors.append(player)
