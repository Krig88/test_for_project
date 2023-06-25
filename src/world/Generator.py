from src.world.field_components.Field import Field
from src.world.actors.Actor import Actor
from src.world.actors.Player import Player

from src.world.field_components.Cell import Cell


class Generator:

    def __init__(self, actors: list[Actor] ,field: Field, size: tuple[int, int] = (5,5))-> None:
        self.field = [[Cell() for j in range(size[0])] for i in range(size[1])]
        self.actors = []
        
        
    def generate(self, set_player: int, set_npc: int, set_walls: int) -> tuple[Field, list[Actor]]:
        raise NotADirectoryError
    
    def place_walls(self, count_of_walls: int = 3):
        raise NotADirectoryError
    
    def place_player(self, player_pos: tuple[int, int] = (0,0))->None:
        self.field.set_actor(player_pos, Player)
        self.actors.append(Player)
        