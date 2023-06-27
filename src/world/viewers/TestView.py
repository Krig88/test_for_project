from world.field_components.Field import Field
from world.actors.Actor import Actor
from world.actors.Player import Player
from world.field_components.Cell import Cell


#TODO: write viwer with whole fild

class TestView:
    def __init__(self):
        symb = {Player: 'P'}
    def draw(self,field: Field)->None:
        symb_str = ''
        for i in field.cells:
            for j in i:
                if not j.passable:
                    symb_str += '#'
                if j.actor:
                    symb_str += 'p'
                if not j.actor and j.passable:
                    symb_str += '.'
            print(symb_str)
            symb_str = ''
        print("it is fild ")