import Cell
from src.world.actors import Actor

class Generator:
    def __init__(self, 
             field_size: tuple[int,int] = (5, 5))-> None:
        raise NotImplementedError()
    
    def generate_field(self) -> Cell: 
        first_in_prev_line = None 
        for i in range(0, self.field_size[1]):
            first_in_line = Cell((i,0), {(0,-1):first_in_prev_line})
            if not i: first_cell = first_in_line
            prev_cell = first_in_line 
            upper_cell = first_in_prev_line
            for j in range (1, self.field_size[0]):
                if not first_in_prev_line:
                    cur_cell = Cell((i,j), {(-1,0):prev_cell})
                else:
                    upper_cell = upper_cell.get_neighbours().get((1,0))
                    cur_cell = Cell((i,j), {(-1,0):prev_cell, (0,-1):upper_cell})
                    upper_cell.get_neighbours()[(0,1)] = cur_cell 
                prev_cell.get_neighbours()[(1,0)] = cur_cell 
                prev_cell = cur_cell
            first_in_prev_line = first_in_line  
        return first_in_line
