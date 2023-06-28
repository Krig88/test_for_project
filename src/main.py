from world.Game import Game
from world.actors import Player, Cat
from world.field_components import Cell

if __name__ == '__main__':
    symbols = {'Player': "P", 'Cat': "c", 'Dog': "d", 'Cell': ".#"}
    iterations = 100  # TODO: how to set in docker ?
    game = Game(iterations)
    game.start(symbols)
